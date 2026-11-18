from langchain.chat_models import init_chat_model
from src.tools.web_search import web_search
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")


llm = init_chat_model(
    model= "openai/gpt-oss-120b",
    model_provider = "groq",
    temperature = 0.0,
    api_key = api_key,
)

def researcher_node(state):
    research_tasks = state["plan"] 
    
    findings = []
    sources = []
    
    for task in research_tasks:
        
        print(f"\nResearching:{task}")
        
        search_results = web_search(task)
        
        if not search_results:
            findings.append(
                f"Task:{task}\n No search results were found"
            )
            
            continue
        
        context = ""
        
        for index,item in enumerate(search_results,start = 1):
            
            source_id = f"S{len(sources) + 1}"
            
            
            sources.append({
                "id":source_id,
                "title":item["title"],
                "url":item["url"]
            })
            
            context += f"""
            Source ID: {source_id},
            Title:{item["title"]},
            URL:{item["url"]},
            Content:{item["content"]}
            """
            
        prompt = f"""
    you are an expert ai reasearcher.
    Research task: {task}
    
    Retrived web information:{context}
    
    Instructions:
        1. Summarize the relevant information.
        2. Use only information supported by the retrieved content.
        3. Add source IDs such as [S1] to support your statements.
        4. Mention when evidence is insufficient.
        5. Do not invent facts or references.
    """
        response = llm.invoke(prompt)

        findings.append(
        f"Research Task: {task}\n{response.content[:1200]}"
)
    
    return {
        "findings": findings,
        "sources":sources
    }


