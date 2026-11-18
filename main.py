from src.graph import graph_builder

initial_state = {
    "question":"What are the advantages and challenges of solar energy",
    "plan":[],
    "findings":[],
    "sources":[],
    "final_report":""
}

result = graph_builder.invoke(initial_state)




print("\n========== RESEARCH PLAN ==========")

for task in result["plan"]:
    print("-", task)


print("\n========== RESEARCH FINDINGS ==========")

for finding in result["findings"]:
    print(finding)


print("\n========== SOURCES ==========")

for source in result["sources"]:
    print(source)


print("\n========== FINAL REPORT ==========")

print(result["final_report"])
