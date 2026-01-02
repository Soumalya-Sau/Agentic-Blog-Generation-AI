from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal, Annotated
from langchain_core.messages import SystemMessage, HumanMessage
import operator
from agents.llm import groq_invoke

class BlogState(TypedDict):
    topic: str
    blog: str
    evaluation: Literal["approved", "needs_improvement"]
    feedback: str
    iteration: int
    max_iteration: int
    blog_history: Annotated[list[str], operator.add]
    feedback_history: Annotated[list[str], operator.add]

def generate_blog(state: BlogState):
    messages = [
        SystemMessage(content="You are a professional technical blog writer."),
        HumanMessage(content=f"Write a detailed blog on: {state['topic']}")
    ]
    blog = groq_invoke(messages)
    return {"blog": blog, "blog_history": [blog]}

def evaluate_blog(state: BlogState):
    messages = [
        SystemMessage(content="You are a strict content reviewer."),
        HumanMessage(content=f"Review this blog:\n\n{state['blog']}")
    ]
    feedback = groq_invoke(messages)
    evaluation = "approved" if "approved" in feedback.lower() else "needs_improvement"
    return {
        "evaluation": evaluation,
        "feedback": feedback,
        "feedback_history": [feedback]
    }

def refine_blog(state: BlogState):
    messages = [
        SystemMessage(content="You improve blogs using feedback."),
        HumanMessage(content=f"Feedback:\n{state['feedback']}\n\nBlog:\n{state['blog']}")
    ]
    improved = groq_invoke(messages)
    return {
        "blog": improved,
        "iteration": state["iteration"] + 1,
        "blog_history": [improved]
    }

def route_blog(state: BlogState):
    if state["evaluation"] == "approved" or state["iteration"] >= state["max_iteration"]:
        return "approved"
    return "needs_improvement"

def build_workflow():
    graph = StateGraph(BlogState)

    graph.add_node("generate", generate_blog)
    graph.add_node("evaluate", evaluate_blog)
    graph.add_node("refine", refine_blog)

    graph.add_edge(START, "generate")
    graph.add_edge("generate", "evaluate")
    graph.add_conditional_edges("evaluate", route_blog, {
        "approved": END,
        "needs_improvement": "refine"
    })
    graph.add_edge("refine", "evaluate")

    return graph.compile()
