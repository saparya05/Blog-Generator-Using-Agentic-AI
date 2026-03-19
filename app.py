import streamlit as st
from langgraph.graph import StateGraph, START, END
from langgraph.types import Send
from schemas import State
from nodes.router import router_node
from nodes.research import research_node
from nodes.orchestrator import orchestrator_node
from nodes.worker import worker_node
from nodes.reducer import reducer_subgraph


# ---------------- UI ----------------
st.title("AI Blog Generator")

topic = st.text_input("Enter topic")
mode = st.selectbox("Select mode", ["fast", "detailed"])

generate = st.button("Generate Blog")


# ---------------- Graph Logic ----------------
def route_next(state: State) -> str:
    return "research" if state["needs_research"] else "orchestrator"


def fanout(state: State):
    return [
        Send(
            "worker",
            {
                "task": task.model_dump(),
                "topic": state["topic"],
                "mode": state["mode"],
                "plan": state["plan"].model_dump(),
                "evidence": [],
            },
        )
        for task in state["plan"].tasks
    ]


g = StateGraph(State)
g.add_node("router", router_node)
g.add_node("research", research_node)
g.add_node("orchestrator", orchestrator_node)
g.add_node("worker", worker_node)
g.add_node("reducer", reducer_subgraph)

g.add_edge(START, "router")
g.add_conditional_edges("router", route_next)
g.add_edge("research", "orchestrator")
g.add_conditional_edges("orchestrator", fanout, ["worker"])
g.add_edge("worker", "reducer")
g.add_edge("reducer", END)

app = g.compile()


# ---------------- RUN GRAPH ----------------
if generate and topic:
    try:
        st.write("Generating blog...")

        initial_state = {
            "topic": topic,
            "mode": mode,
            "needs_research": True,
            "plan": None,
            "draft": "",
            "evidence": []
        }

        result = app.invoke(initial_state)

        st.success("Done")
        st.write(result)

    except Exception as e:
        st.error(f"Error: {e}")