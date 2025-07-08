import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o",  # default model, can be overridden via env var
    temperature=0.7
)
