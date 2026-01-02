import os
from groq import Groq
from langchain_core.messages import SystemMessage, HumanMessage

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL_NAME = "llama-3.1-8b-instant"

def groq_invoke(messages):
    groq_messages = []
    for m in messages:
        if isinstance(m, SystemMessage):
            role = "system"
        elif isinstance(m, HumanMessage):
            role = "user"
        else:
            role = "assistant"

        groq_messages.append({
            "role": role,
            "content": m.content
        })

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=groq_messages,
        max_tokens=800
    )

    return response.choices[0].message.content
