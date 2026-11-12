from typing import TypedDict
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

class ResearchPlan(TypedDict):
    plan:list[str]
    

llm = init_chat_model(
    model= "openai/gpt-oss-120b",
    model_provider = "groq",
    temperature = 0.0,
    api_key = api_key,
)


planner_llm = llm.with_structured_output(ResearchPlan)

def planner_node(state):
    question = state["question"]
    prompt = f"""
     You are an expert research planner.

    Break the following research question into
    5 clear and specific research tasks.

    Research Question: {question}

    Return a list of research tasks."""
    response = planner_llm.invoke(prompt)
    return {
        "plan":response["plan"]
    }