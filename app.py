import streamlit as st
import time
from agents.graph import build_workflow

st.set_page_config(
    page_title="Agentic Blog Generator",
    layout="wide"
)

st.title("🧠 Agentic Blog Generation AI")
st.caption("LangGraph-powered multi-agent system with iterative review & refinement")

with st.sidebar:
    st.header("⚙️ Configuration")
    max_iter = st.slider("Max Iterations", 1, 5, 3)

workflow = build_workflow()

topic = st.text_input("📌 Enter a blog topic")

if st.button("🚀 Generate Blog") and topic:
    with st.spinner("Running agentic workflow..."):
        start = time.time()
        result = workflow.invoke({
            "topic": topic,
            "iteration": 1,
            "max_iteration": max_iter
        })
        latency = round(time.time() - start, 2)

    col1, col2 = st.columns(2)
    col1.metric("Iterations Used", result["iteration"])
    col2.metric("Latency (sec)", latency)

    st.subheader("✅ Final Blog Output")
    st.write(result["blog"])

    with st.expander("🔁 Blog Versions"):
        for i, blog in enumerate(result["blog_history"], 1):
            st.markdown(f"### Version {i}")
            st.write(blog)

    with st.expander("🔍 Reviewer Feedback"):
        for fb in result["feedback_history"]:
            st.write(fb)

