from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")


llm = init_chat_model(
    mdodel= "openai/gpt-oss-120b",
    model_provider = "groq",
    temperature = 0.0,
    api_key = api_key,
)

def researcher_node(state):
    research_tasks = state["plan"] 
    
    findings = []
    
    for task in research_tasks:
        prompt = f"""
    you are an expert ai reasearcher.
    Research task: {task}

    Provide a concise research note.
    Include relevant facts, explanations and limitations.
    If you cannot verify a current fact, say so.
    """
        response = llm.invoke(prompt)
        findings.append(response.content)
    
    return {"findings": findings}




    
