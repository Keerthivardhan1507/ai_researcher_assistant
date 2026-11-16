from src.tools.web_search import web_search

results = web_search(
    "Advantages and challeges of sloar energy"
)

for result in results:
    print("\nTitle:", result["title"])
    print("URL:", result["url"])
    print("Content:", result["content"])
    print("-" * 60)