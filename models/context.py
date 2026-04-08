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

def save_agent_report_to_state(
    tool_context: ToolContext, state_key: str, detailed_report: str
) -> dict[str, str]:
    """Saves a detailed analysis report to the global state so other agents can read it without it being displayed to the user."""
    tool_context.state[state_key] = detailed_report
    logging.info(f"[State updated] Internal report saved for key: {state_key}")
    return {"status": "success"}
