from urllib.parse import urlparse,urlunparse

def validate_search_results(search_results,seen_urls):
    validated_results = []
    
    for item in search_results:
        
        #.Check whether the item required field exist
        title = item.get("title","").strip()
        url = item.get("url","").strip()
        content = item.get("content","").strip()
        
        if not title or not url or not content:
            continue
        
        #Validate url format
        parsed_url = urlparse(url)
        
        if parsed_url.scheme not in ("http","https"):
            continue
        
        if not parsed_url.netloc:
            continue
        
        if len(content) < 100:
            continue
        
        #Normalize url for duplicate checking
        normalized_url = urlunparse(
            (
                parsed_url.scheme.lower(),
                parsed_url.netloc.lower(),
                parsed_url.path.rstrip("/"),
                parsed_url.params,
                parsed_url.query,
                ""
            )
        )
        
        if normalized_url in seen_urls:
            continue
        
        seen_urls.add(normalized_url)
        
        validated_results.append({
            "title":title,
            "url":url,
            "content":content
        })
    return validated_results

