from dotenv import load_dotenv
from langchain.tools import tool
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from typing import Annotated
from typing_extensions import TypedDict

load_dotenv()

@tool
def assistance_with_cooking(dish: str) -> str:
    """Assist the user with cooking a specific dish."""
    return f"I'm glad to help you cook {dish}!"

@tool
def get_ingredients(dish_name: str) -> str:
    """Get the ingredients needed for a specific dish."""
    return f"The ingredients for {dish_name} are ..."

persona = """ 
You are an experienced chef and you are helping the user with their cooking needs.
You are capable of providing recipes, cooking tips, and ingredient substitutions. 
"""

agent = create_react_agent(
        model="groq:llama-3.3-70b-versatile",
        tools=[assistance_with_cooking, get_ingredients],
        prompt=persona
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

memory = MemorySaver()

def cookbot_node(state: State):
    messages = state["messages"]
    output = agent.invoke({"messages": messages})
    # append latest assistant message to messages list and return new state
    return {"messages": messages + [output["messages"][-1]]}

graph_builder = StateGraph(State)
graph_builder.add_node("CookBot", cookbot_node)
graph_builder.add_edge(START, "CookBot")
graph_builder.add_edge("CookBot", END)

graph = graph_builder.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "chef_thread"}}


def get_bot_response(chat_history):
    events = graph.stream(
        {"messages": chat_history},
        config=config,
        stream_mode="values",
    )
    assistant_reply = ""
    for event in events:
        assistant_reply = event["messages"][-1].content
    return assistant_reply



