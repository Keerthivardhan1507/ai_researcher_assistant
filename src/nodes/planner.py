from typing import TypedDict
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
import re
import json
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")



llm = init_chat_model(
    model= "openai/gpt-oss-120b",
    model_provider = "groq",
    temperature = 0.0,
    api_key = api_key,
)



def planner_node(state):
    question = state["question"]
    prompt = f"""
     You are an expert research planner.

    Break the following research question into
    5 clear and specific research tasks.

    Research Question: {question}

    Return Exactly five number tasks
    each task must be on a different line
    Do not include an introduction or conclusion.
    """
    response = llm.invoke(prompt)
    
    content = response.content
    
    tasks = re.findall(
        r"(?m)^\s*\d+[\.\)]\s+(.+?)(?=\s*(?:\n\s*[-*]\s+|\n\s*\d+[\.\)]|\Z))",
        content,
        re.DOTALL
    )
    
    tasks = [task.replace("\n"," ").strip() for task in tasks]
    
    if len(tasks) != 5:
        raise ValueError(
            f"Expected 5 research tasks, received {len(tasks)}. "
            f"Raw response: {content}"
        )

    return {"plan": tasks}