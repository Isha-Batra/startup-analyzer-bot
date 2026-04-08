from google.adk.agents import SequentialAgent
from agents.market_agent import market_analyst, market_debater
from agents.tech_agent import tech_analyst, tech_debater
from agents.finance_agent import finance_analyst, finance_debater
from agents.investor_agent import investor_decision_maker

validator_workflow = SequentialAgent(
    name="startup_validator_workflow",
    description="Sequential workflow for validating startup ideas.",
    sub_agents=[
        # Phase 1: Initial Analysis
        market_analyst,
        tech_analyst,
        finance_analyst,
        
        # Phase 2: Discussion / Critique Layer
        market_debater,
        tech_debater,
        finance_debater,
        
        # Phase 3: Final Verdict
        investor_decision_maker
    ]
)
