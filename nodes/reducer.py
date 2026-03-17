from pathlib import Path
from langgraph.graph import StateGraph, START, END
from schemas import State
from config import llm
from langchain_core.messages import SystemMessage, HumanMessage


def merge_content(state: State) -> dict:
    body = "\n\n".join(md for _, md in sorted(state["sections"]))
    return {"merged_md": f"# {state['plan'].blog_title}\n\n{body}"}

reducer_graph = StateGraph(State)
reducer_graph.add_node("merge", merge_content)
reducer_graph.add_edge(START, "merge")
reducer_graph.add_edge("merge", END)

reducer_subgraph = reducer_graph.compile()
