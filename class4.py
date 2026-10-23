"""
CLASS 4: Loops

Idea: an arrow can go BACK to an earlier node.
Like a game: "keep adding 1 until you reach 3, then stop."
"""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    count: int


def add_one(state: State):
    print("count is now", state["count"] + 1)
    return {"count": state["count"] + 1}


# Decider: go back to "add_one" (loop!) or finish with END.
def should_continue(state: State):
    if state["count"] >= 3:
        return END
    return "add_one"


builder = StateGraph(State)
builder.add_node("add_one", add_one)
builder.add_edge(START, "add_one")
builder.add_conditional_edges("add_one", should_continue)

graph = builder.compile()

if __name__ == "__main__":
    print(graph.invoke({"count": 0}))   # {'count': 3}
