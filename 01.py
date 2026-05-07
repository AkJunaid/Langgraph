from typing import Dict, TypedDict, List
from langgraph.graph import StateGraph, START,END

class AgentState(TypedDict):
    message: str
    name: str
    id : str
    number01: int
    number02: int
    final_value: int


def profile(state: AgentState) ->AgentState:
    state['message'] = f"hey {state['name']}, how are you? this is your id {state['id']}"
    return state

def math(state:AgentState) -> AgentState:
    state['final_value'] = state['number01'] + state['number02']


graph = StateGraph(AgentState)

graph.add_node("pro", profile)
graph.add_node("math", math)

graph.add_edge(START, "pro")
graph.add_edge("pro", "math")
graph.add_edge("math", END)

app = graph.compile()

result = app.invoke({
    "name": "junaid",
    "number01": 1,
    "number02": 2,
    "id" : "2021867"
})


print(result)