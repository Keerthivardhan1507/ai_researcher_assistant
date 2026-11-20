
from src.tools.source_validator import validate_search_results

# Sample Tavily search results
search_results = [
    {
        "title": "Solar Energy Guide",
        "url": "https://example.com/solar",
        "content": "Solar energy converts sunlight into electricity using photovoltaic cells. " * 5
    },
    {
        "title": "Short Content",
        "url": "https://example.com/short",
        "content": "Solar energy is useful."
    },
    {
        "title": "Invalid URL",
        "url": "invalid-url",
        "content": "This is a sufficiently long piece of content. " * 5
    },
    {
        "title": "Duplicate Solar Guide",
        "url": "https://example.com/solar",
        "content": "This is another version of the same page. " * 5
    }
]

seen_urls = set()

validated_results = validate_search_results(
    search_results,
    seen_urls
)

print("Total search results:", len(search_results))
print("Validated results:", len(validated_results))

for result in validated_results:
    print("\nTitle:", result["title"])
    print("URL:", result["url"])
