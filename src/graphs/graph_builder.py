from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import ToolNode

from src.states.state import ChatState
from src.nodes.node import chat_node, route_tools, reflect_node
from src.llms.llm import tools


def build_graph():
    """Build and compile the chatbot graph with conditional routing and reflection"""
    tool_node = ToolNode(tools)
    
    # Checkpointer
    checkpointer = InMemorySaver()
    
    graph = StateGraph(ChatState)
    
    # Add nodes
    graph.add_node("chat_node", chat_node)
    graph.add_node("tools", tool_node)
    graph.add_node("reflect", reflect_node)
    
    # Add edges
    graph.add_edge(START, "chat_node")
    
    # Conditional routing: check if tools are needed
    graph.add_conditional_edges(
        "chat_node",
        route_tools,
        {
            "tools": "tools",      # If tools called, go to tools
            "reflect": "reflect",  # If no tools, go to reflection
            "__end__": END         # Direct end if needed
        }
    )
    
    # After tools execute, go back to chat for response
    graph.add_edge("tools", "chat_node")
    
    # After reflection, end the conversation
    graph.add_edge("reflect", END)
    
    chatbot = graph.compile(checkpointer=checkpointer)
    return chatbot, checkpointer
