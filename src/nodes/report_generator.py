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
    sources = state["sources"]
    
    
    limit_findings = [
        finding[:400] for finding in findings[:3]
    ]
    # Limit source references
    limited_sources = [
        {
            "id": source["id"],
            "title": source["title"][:100],
            "url": source["url"]
        }
        for source in sources[:3]
    ]
    
    for finding in findings:
        limit_findings.append(finding)
        
    
    prompt = f"""
    you are a professional research report writer.
    Research Question: {question}
    Research Findings: {limit_findings}
    Available sources :{limited_sources}
    Create a concise research report containing:
    
    1. Introduction
    2. Key Findings
    3. Detailed Analysis
    4. Advantages and Limitations
    5. Conclusion

    Use clear headings and professional language.
    Do not invent facts or citations.
    """
    
    print("Number of findings:", len(limit_findings))
    print("Total finding characters:",
      sum(len(x) for x in limit_findings))
    print("Number of sources:", len(limited_sources))
    
    response = llm.invoke(prompt)
    return {"final_report": response.content}

    
