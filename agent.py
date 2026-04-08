import os
import sys

# Ensure the root directory is on the Python path for Cloud Run and local ADK runs
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dotenv import load_dotenv

from google.adk import Agent

from models.context import add_prompt_to_state
from orchestrator.pipeline import validator_workflow

# Setup Environment
load_dotenv()
model_name = os.getenv("MODEL", "gemini-1.5-flash")

# Root Agent (Entry Point)
root_agent = Agent(
    name="validator_entrypoint",
    model=model_name,
    description="Main entry point for the Startup Validator.",
    instruction="""
    ## ROLE: System Concierge

    - Greet the user professionally.
    - Ask for the startup idea.
    - Store the idea using 'add_prompt_to_state'.
    - Immediately trigger 'startup_validator_workflow'.

    Be crisp and do not add unnecessary text.
    """,
    tools=[add_prompt_to_state],
    sub_agents=[validator_workflow]
)
