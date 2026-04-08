from google.adk.tools.tool_context import ToolContext

class BaseAgent:
    """
    Note: This base class is currently optional as you are using 
    google.adk.Agent directly in your agent files.
    """
    def __init__(self, name: str):
        self.name = name
