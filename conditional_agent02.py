from typing import Dict, TypedDict, List
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
    num01 : int
    num02 : int
    final_value: int
    operation : str


def addition(state: AgentState)-> AgentState:
    state['final_value'] = state['num01'] + state['num02']
    return state

def subtraction(state: AgentState) -> AgentState:
    state['final_value'] = state['num01'] - state['num02']
    return state

def multiplication(state: AgentState) -> AgentState:
    state['final_value'] = state['num01'] * state['num02']
    return state

def divide(state: AgentState) -> AgentState:
    state['final_value'] = state['num01'] / state['num02']
    return state

def condition(state:AgentState) -> AgentState:
    if state['operation'] == "+":
     return "addition"
    elif state['operation'] == "-":
        return "subtraction"
    elif state['operation'] == "*" :
        return "multiplication"
    elif state['operation'] == "/":
        return "divide"
    

graph = StateGraph(AgentState)


graph.add_node('addition' ,addition)
graph.add_node('subtraction' ,subtraction)
graph.add_node('multiplication' ,multiplication)
graph.add_node('divide' ,divide)

graph.add_node("router", lambda state:state)

graph.add_edge(START, "router")
graph.add_conditional_edges(
    "router",
    condition,
    {
        "addition" : "addition",
        "subtraction": "subtraction",
        "multiplication" : "multiplication",
        "divide" : "divide"
    }
)

graph.add_edge("addition",END)
graph.add_edge("subtraction", END)
graph.add_edge("multiplication", END)
graph.add_edge("divide", END)


app = graph.compile()



result = app.invoke({"num01": 10, "operation": "*", "num02": 5})
print("the final answer is :", result)