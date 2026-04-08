import os
from dotenv import load_dotenv

from google.adk import Agent, Runner
from google.adk.sessions import InMemorySessionService
from google.adk.runners import RunRequest

from models.context import add_prompt_to_state
from orchestrator.pipeline import validator_workflow

# Load environment variables
load_dotenv()
model_name = os.getenv("MODEL")


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
    - Immediately trigger 'validator_workflow'.

    Be crisp and do not add unnecessary text.
    """,
    tools=[add_prompt_to_state],
    sub_agents=[validator_workflow]
)


def main():
    print("🚀 Starting Multi-Agent Startup Validator Local CLI...\n")

    # Initialize session service
    session_service = InMemorySessionService()

    # Initialize runner
    runner = Runner(
        agent=root_agent,
        app_name="startup_validator",
        session_service=session_service
    )

    # CLI loop
    while True:
        user_input = input("\n💡 Enter your startup idea (or type 'exit'): \n> ")

        if user_input.lower() in ["exit", "quit"]:
            print("👋 Exiting... Good luck building!")
            break

        try:
            # Create request object
            request = RunRequest(input=user_input)

            # Run agent system
            response = runner.run(request)

            print("\n📊 FINAL OUTPUT:\n")
            if hasattr(response, "output"):
                print(response.output)
            else:
                print(response)

        except Exception as e:
            print("\n❌ Error occurred:")
            print(str(e))


if __name__ == "__main__":
    main()