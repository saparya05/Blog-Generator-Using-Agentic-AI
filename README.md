# 🤖 Blog Generator Using Agentic AI
- An AI-powered multi-agent system that researches, plans, and writes complete blog posts automatically.

- Built using LangGraph, LangChain, and Streamlit, this project demonstrates how LLM agents can collaborate in a structured workflow to generate high-quality blog content.

# ✨ Features

- Agent-based architecture
- Automated research
- Structured blog planning
- Parallel section generation
- Evidence collection with citations
- Permanent blog memory
- Live Markdown preview
- Download blog as Markdown
- Execution logs & workflow tracking

# 🏛 Architecture
The system is built as a LangGraph workflow:

![ Architecture ](/assets/image.png)

# 🛠 Tech Stack

- LLM Orchestration: LangGraph
- LLM Framework: LangChain
- UI: Streamlit
- Research Tool: Tavily
- Data Handling: Pandas

# ⚙️ How It Works

- User enters a blog topic.
- Router agent decides if research is needed.
- Research agent gathers evidence.
- Orchestrator creates a structured blog plan.
- Worker agents generate blog sections.
- Reducer merges sections into a final Markdown blog.
- Blog is saved locally for future access.

# 🚀 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/saparya05/Blog-Generator-Using-Agentic-AI
cd AI-blog-writing-agent
```

### 2. Clone the repository

```bash
pip install -r requirements.txt
```

### 3. Add environment variables

Create a .env file in the project root with the following:

```bash
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key
```

### 4. Run the app

```bash
streamlit run frontend.py
```

#  📜 License

This project is open-source and available under the MIT License.