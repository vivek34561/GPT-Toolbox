from src.states.state import ChatState
from src.llms.llm import llm, llm_with_tools
from typing import Literal


def chat_node(state: ChatState):
    """Main chat node that uses LLM with tools"""
    messages = state['messages']
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}


def route_tools(state: ChatState) -> Literal["tools", "reflect", "__end__"]:
    """Route to tools if the LLM called any, otherwise to reflection or end"""
    messages = state['messages']
    last_message = messages[-1]
    
    # Check if the LLM made tool calls
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        return "tools"
    
    # For responses without tool calls, route to reflection
    return "reflect"


def reflect_node(state: ChatState):
    """Reflection node that validates and improves response quality"""
    messages = state['messages']
    last_message = messages[-1]
    
    # Create a concise reflection prompt that returns ONLY the final response
    reflection_prompt = f"""You are a quality checker. Review the following response and either return it as-is if good, or provide an improved version. Return ONLY the final response text, nothing else.

Response to review: {last_message.content}

Final response:"""
    
    from langchain_core.messages import HumanMessage, AIMessage
    
    # Use basic LLM for reflection (without tools)
    reflection = llm.invoke([HumanMessage(content=reflection_prompt)])
    
    # Get the cleaned response content
    improved_content = reflection.content.strip()
    
    # If reflection improved it significantly, update the last message
    if improved_content and improved_content != last_message.content:
        # Remove the old message and add the improved one
        messages_without_last = messages[:-1]
        return {"messages": messages_without_last + [AIMessage(content=improved_content)]}
    
    # If no improvement needed, keep original
    return {"messages": []}
