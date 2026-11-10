from typing import TypedDict

class ResearchState(TypedDict):
    question:str
    plan:list[str]
    findings:list[str]
    sources:list[str]
    final_report:str
    