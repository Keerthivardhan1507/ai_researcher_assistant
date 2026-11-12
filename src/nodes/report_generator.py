from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
llm = init_chat_model(
    model= "openai/gpt-oss-120b",
    model_provider = "groq",
    api_key = api_key,
    temperature = 0.0,
)

def report_generator_node(state):
    question = state["question"]
    
    findings  = state["findings"]
    
    prompt = f"""
    you are a professional research report writer.
    Research Question: {question}
    Research Findings: {findings}
    Create a structured research report containing:

    1. Introduction
    2. Key Findings
    3. Detailed Analysis
    4. Advantages and Limitations
    5. Conclusion

    Use clear headings and professional language.
    Do not invent facts or citations.
    """
    
    response = llm.invoke(prompt)
    return {"final_report": response.content}

    
