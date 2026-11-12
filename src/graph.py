from langgraph.graph import StateGraph,START,END

from src.state import ResearchState
from src.nodes.planner import planner_node
from src.nodes.researcher import researcher_node
from src.nodes.report_generator import report_generator_node

graph = StateGraph(ResearchState)

graph.add_node("planner", planner_node)
graph.add_node("researcher", researcher_node)
graph.add_node("report_generator", report_generator_node)

graph.add_edge(START, "planner")
graph.add_edge("planner", "researcher")
graph.add_edge("researcher", "report_generator")
graph.add_edge("report_generator", END)

graph_builder = graph.compile()


