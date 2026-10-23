"""
CLASS 5: Reducers (how to ADD to a list instead of REPLACING it)

Problem: normally, when a worker returns {"x": value}, the old x is thrown away.
Fix: tell LangGraph HOW to combine old + new. That rule is called a "reducer".
Annotated[list, operator.add] means: "when new items come, ADD them to the old list."
This is exactly how chat history works (messages keep piling up).
"""
import operator
from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    # Without Annotated: new list would REPLACE the old list.
    # With operator.add: new list is ADDED to the old list.
    steps: Annotated[list[str], operator.add]


def first(state: State):
    return {"steps": ["woke up"]}


def second(state: State):
    return {"steps": ["brushed teeth"]}


def third(state: State):
    return {"steps": ["went to school"]}


builder = StateGraph(State)
builder.add_node("first", first)
builder.add_node("second", second)
builder.add_node("third", third)
builder.add_edge(START, "first")
builder.add_edge("first", "second")
builder.add_edge("second", "third")
builder.add_edge("third", END)

graph = builder.compile()

if __name__ == "__main__":
    print(graph.invoke({"steps": []}))
    # {'steps': ['woke up', 'brushed teeth', 'went to school']}
