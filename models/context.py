import logging
from google.adk.tools.tool_context import ToolContext

def add_prompt_to_state(
    tool_context: ToolContext, input_text: str
) -> dict[str, str]:
    """Saves the user's input to the global state for use by downstream agents."""
    # We save to both keys to maintain backward compatibility with different agents
    tool_context.state["IDEA"] = input_text
    tool_context.state["PROMPT"] = input_text
    logging.info(f"[State updated] Input saved: {input_text}")
    return {"status": "success"}
