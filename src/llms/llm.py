import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Use a model that supports tool calling well
llm = ChatGroq(model="openai/gpt-oss-120b")

# Search tool
search_tool = DuckDuckGoSearchRun(region="us-en")

# Calculator tool for mathematical operations
@tool
def calculator(expression: str) -> str:
    """Useful for performing mathematical calculations. 
    Input should be a valid mathematical expression as a string.
    Example: '2 + 2', '10 * 5', '(100 - 20) / 4'
    """
    try:
        # Safe evaluation of mathematical expressions
        result = eval(expression, {"__builtins__": {}}, {})
        return f"The result is: {result}"
    except Exception as e:
        return f"Error calculating: {str(e)}"

tools = [search_tool, calculator]
llm_with_tools = llm.bind_tools(tools)
