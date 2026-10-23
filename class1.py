"""
CLASS 1: Your first graph (State, Node, Edge)

Idea: a graph is a MAP. We walk from START to END and visit workers (nodes).
A "backpack" (state) travels with us and the workers can change what is inside.
"""
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# 1. STATE = the backpack. It says what things we carry (here: one text called "message").
class State(TypedDict):
    message: str


# 2. NODE = a worker. It is just a normal Python function.
#    It receives the backpack and returns ONLY the things it wants to change.
def say_hello(state: State):
    return {"message": "Hello World!"}


# 3. BUILD THE MAP
builder = StateGraph(State)              # empty map that knows the backpack shape
builder.add_node("hello", say_hello)     # put a worker on the map (name, function)
builder.add_edge(START, "hello")         # arrow: START -> hello
builder.add_edge("hello", END)           # arrow: hello -> END

# 4. COMPILE = lock the map so it is ready to run
graph = builder.compile()

# 5. RUN IT. invoke() takes the starting backpack and returns the final backpack.
if __name__ == "__main__":
    print(graph.invoke({"message": ""}))   # {'message': 'Hello World!'}
