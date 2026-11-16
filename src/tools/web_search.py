import os
from tavily import TavilyClient
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

tavilyclient = TavilyClient(
    api_key=api_key
)

def web_search(query:str):
    
    response = tavilyclient.search(
        query=query,
        max_results=5,
        search_depth="advanced"
    )
    
    results = []
    
    for item in response["results"]:
        results.append({
            "title": item["title"],
            "url": item["url"],
            "content": item["content"]
        })

    return results
