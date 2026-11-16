from typing import TypedDict

class Source(TypedDict):
    id:str
    title:str
    url:str

class ResearchState(TypedDict):
    question:str
    plan:list[str]
    findings:list[str]
    sources:list[str]
    final_report:str
 