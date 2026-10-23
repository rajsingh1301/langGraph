"""
CLASS 2: Many nodes in a row

Idea: each worker gets the backpack the LAST worker left behind.
Workers only return what they change; everything else stays in the backpack.
"""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    name: str
    greeting: str
    shout: str


def make_greeting(state: State):
    # reads "name" from the backpack, writes "greeting"
    return {"greeting": f"Hello, {state['name']}!"}


def make_shout(state: State):
    # reads "greeting" (written by the previous worker), writes "shout"
    return {"shout": state["greeting"].upper()}


builder = StateGraph(State)
builder.add_node("greet", make_greeting)
builder.add_node("shout", make_shout)

# START -> greet -> shout -> END   (a straight line)
builder.add_edge(START, "greet")
builder.add_edge("greet", "shout")
builder.add_edge("shout", END)

graph = builder.compile()

if __name__ == "__main__":
    # We only fill "name". The other boxes in the backpack start empty.
    result = graph.invoke({"name": "Mayank"})
    print(result)
    # {'name': 'Mayank', 'greeting': 'Hello, Mayank!', 'shout': 'HELLO, MAYANK!'}
