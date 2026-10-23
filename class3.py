"""
CLASS 3: Conditional edges (a fork in the road)

Idea: sometimes the computer must CHOOSE the next step.
"If raining -> take umbrella, otherwise -> wear sunglasses."
We write a "decider" function that returns the NAME of the next node.
"""
import random
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    weather: str
    action: str


def check_weather(state: State):
    return {"weather": random.choice(["rain", "sun"])}


def take_umbrella(state: State):
    return {"action": "Take umbrella"}


def wear_sunglasses(state: State):
    return {"action": "Wear sunglasses"}


# The DECIDER: looks at the backpack and returns the name of the next node.
def choose_path(state: State):
    if state["weather"] == "rain":
        return "umbrella"
    return "sunglasses"


builder = StateGraph(State)
builder.add_node("check", check_weather)
builder.add_node("umbrella", take_umbrella)
builder.add_node("sunglasses", wear_sunglasses)

builder.add_edge(START, "check")
# The fork: after "check", ask choose_path where to go next.
builder.add_conditional_edges("check", choose_path)
builder.add_edge("umbrella", END)
builder.add_edge("sunglasses", END)

graph = builder.compile()

if __name__ == "__main__":
    for _ in range(3):  # run a few times to see both paths
        print(graph.invoke({}))
