import os
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(
    model=os.getenv("MODEL"),  # default model, can be overridden via env var
    temperature=0.7
)
