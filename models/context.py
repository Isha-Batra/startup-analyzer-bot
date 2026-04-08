import logging
from google.adk.tools.tool_context import ToolContext

def add_prompt_to_state(
    tool_context: ToolContext, idea: str
) -> dict[str, str]:
    """Saves the user's startup idea to the global state for use by downstream agents."""
    tool_context.state["IDEA"] = idea
    tool_context.state["PROMPT"] = idea
    logging.info(f"[State updated] Input saved: {idea}")
    return {"status": "success"}
