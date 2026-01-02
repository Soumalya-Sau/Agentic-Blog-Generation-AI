# 🧠 Agentic Blog Generation AI using LangGraph

An **agentic content generation system** built using **LangGraph**, **Groq-hosted LLaMA models**, and **Streamlit**. The system mimics a real editorial workflow by using multiple AI agents to **generate, review, and iteratively refine technical blogs** with measurable evaluation metrics.

This project demonstrates **agentic AI design**, **iterative reasoning**, and **human-in-the-loop style evaluation**, inspired by production-grade multi-agent systems.

---

## 🚀 Key Features

* 🧩 LangGraph-based **multi-agent orchestration**
* ✍️ Blog Generator → 🧐 Reviewer → 🔁 Refinement loop
* 🔀 Conditional routing with iteration control
* 🧠 Groq-hosted **LLaMA-3.1-8B** for low-latency inference
* 📊 Transparent tracking of blog versions & feedback
* 🖥️ Interactive **Streamlit UI** for live demo

---

## 🏗️ System Architecture

```
User Topic Input
      │
      ▼
Blog Generator Agent
      │
      ▼
Reviewer Agent ────── Approved ───► Final Blog Output
      │
      └── Needs Improvement
              │
              ▼
        Blog Refinement Agent
              │
              └─── (loop back to Reviewer)
```

### Agent Responsibilities

* **Generator Agent**: Creates a detailed technical blog from the topic
* **Reviewer Agent**: Critically evaluates content quality and relevance
* **Refinement Agent**: Improves the blog using reviewer feedback

---

## 📂 Project Structure

```
Agentic-Blog-Generation-AI/
│
├── app.py                 # Streamlit application
├── agents/
│   ├── graph.py           # LangGraph workflow & agents
│   └── llm.py             # Groq LLM wrapper
│
├── notebooks/
│   └── Blog_Generator.ipynb  # Experimentation & prototyping
│
├── requirements.txt
├── README.md
└── .env.example           # GROQ_API_KEY placeholder
```

---

## 🔁 LangGraph Workflow Design

The workflow is implemented using **LangGraph's StateGraph** with a shared state (`BlogState`) that flows across agents.

### Shared State

* `topic`: Blog topic
* `blog`: Current blog content
* `evaluation`: approved / needs_improvement
* `feedback`: Reviewer comments
* `iteration`: Current iteration count
* `max_iteration`: Max allowed refinement cycles
* `blog_history`: All blog versions
* `feedback_history`: All feedback logs

This enables **memory, traceability, and explainability**.

---

## 🧠 LLM Integration

* Model: **LLaMA-3.1-8B (Groq)**
* Ultra-low latency inference
* Clean abstraction via `groq_invoke()`

```python
MODEL_NAME = "llama-3.1-8b-instant"
```

---

## 🖥️ Streamlit Demo

The Streamlit UI allows users to:

* Enter a blog topic
* Control max refinement iterations
* View final blog output
* Inspect intermediate versions and reviewer feedback

### Run Locally

```bash
pip install -r requirements.txt
export GROQ_API_KEY=your_key_here
streamlit run app.py
```

---

## 📊 Evaluation Metrics

| Metric                 | Value     |
| ---------------------- | --------- |
| Approval Rate          | 100%      |
| Avg Iterations         | 1.2       |
| Avg Latency            | 12.09 sec |
| Median Latency         | ~2.6 sec  |
| Coherence (Human Eval) | 4.6 / 5   |
| Relevance (Human Eval) | 4.6 / 5   |

*All scores are manually evaluated and logged by the developer.*

---

## 🧪 Notebook Usage

The Jupyter notebook is used for:

* Prompt experimentation
* Agent behavior analysis
* Debugging iteration logic

> ⚠️ Production logic is implemented only in `.py` files.

---

## 💡 Future Enhancements

* RAG-enabled blog generation (citations)
* Automated scoring (LLM-as-a-judge)
* SEO optimization agent
* Export to Markdown / PDF
* Multi-topic batch generation

---

## 📌 Why This Project Matters

This project demonstrates:

* Agentic AI system design
* Iterative self-improving generation
* LangGraph orchestration
* LLM evaluation loops
* Production-ready UI

---

## 👤 Author

**Soumalya Sau**
M.Tech, IIT Kharagpur
Interests: Agentic AI, LLM Systems, GenAI, NLP
