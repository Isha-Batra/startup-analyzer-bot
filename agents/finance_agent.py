import os
from google.adk import Agent
from dotenv import load_dotenv
from models.context import save_agent_report_to_state

load_dotenv()
model_name = os.getenv("MODEL", "gemini-1.5-flash")


finance_analyst = Agent(
    name="finance_analyst",
    model=model_name,
    description="Evaluates revenue models and financial viability.",
    tools=[save_agent_report_to_state],
    instruction="""
    ## ROLE: Financial Analyst (CFO)
    Analyze the financial viability of this idea: { IDEA }
    
    **CRITICAL INSTRUCTIONS:**
    1. **UNIT ECONOMICS:** Focus on LTV (Lifetime Value) vs CAC (Customer Acquisition Cost).
    2. **BURN RATE:** Assume a standard seed-stage team of 10 and calculate monthly operational costs.
    3. **SENSITIVITY:** How does the model change if growth is 50% slower than expected?
    
    **INTERNAL ANALYSIS REQUIREMENT (HIDE FROM USER):**
    - **Revenue Model:** Subscription, Transactional, Ad-based, etc. (Explain WHY).
    - **OpEx Breakdown:** Estimated monthly costs for Cloud, Salaries, and Marketing.
    - **Break-even Milestone:** How many customers/units are needed to reach $0 cash flow?
    - **Funding Needs:** How much capital is required to survive the first 18 months?
    - **Financial Health Score:** (1-10).
    
    **OUTPUT WORKFLOW (FOLLOW EXACTLY):**
    1. Call the `save_agent_report_to_state` tool with state_key="finance_analysis" and your FULL financial model as detailed_report.
    2. Reply to the user ONLY with the following message and NOTHING ELSE: "Financial analysis completed internally."
    """
)

finance_debater = Agent(
    name="finance_debater",
    model=model_name,
    description="Critiques other analyses from a financial perspective.",
    tools=[save_agent_report_to_state],
    instruction="""
    ## ROLE: CFO Critique (VC Meeting)
    Review the Market Analysis ({ market_analysis }) and Tech Analysis ({ tech_analysis }).
    
    **CRITICAL INSTRUCTIONS:**
    - **MARGIN SQUEEZE:** If the Tech Analyst suggests an expensive stack, how does that impact the Gross Margin?
    - **TAM VS REVENUE:** Is the Market Analyst's TAM realistic for the proposed pricing model?
    - **SCALABILITY COST:** Does the Tech plan require massive upfront capital before the first dollar of revenue?

    **OUTPUT WORKFLOW (FOLLOW EXACTLY):**
    1. Call the `save_agent_report_to_state` tool with state_key="finance_critique" and detailed_report containing the "Top Financial Risk" from the other reports.
    2. Reply to the user ONLY with the following message and NOTHING ELSE: "Financial critiques saved internally."
    """
)
