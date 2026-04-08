import os
from google.adk import Agent
from dotenv import load_dotenv
from models.context import save_agent_report_to_state

load_dotenv()
model_name = os.getenv("MODEL", "gemini-1.5-flash")


tech_analyst = Agent(
    name="tech_analyst",
    model=model_name,
    description="Evaluates technical feasibility and stack.",
    tools=[save_agent_report_to_state],
    instruction="""
    ## ROLE: CTO / Technical Analyst
    Analyze the technical feasibility of this idea: { IDEA }
    
    **CRITICAL INSTRUCTIONS:**
    1. **BUILD VS BUY:** Identify which components should be built from scratch vs. using existing APIs.
    2. **TTM (TIME TO MARKET):** Estimate months to MVP based on team size assumptions (assume 3-5 engineers).
    3. **NEGATIVE CONSTRAINTS:** Do not suggest "Blockchain" or "AI" unless it is core to the value proposition.
    
    **INTERNAL ANALYSIS REQUIREMENT (HIDE FROM USER):**
    - **Core Architecture:** Describe the data flow (e.g., Event-driven, Microservices, Monolith).
    - **High-Risk Modules:** Identify the "Single Point of Failure" or most complex logic.
    - **Infrastructure Stack:** Specific recommendations for Compute (e.g., Cloud Run), Database (e.g., Postgres), and Security (e.g., OAuth2).
    - **Technical Debt Forecast:** Where will the shortcuts be taken in the first 6 months?
    - **Score:** "Feasibility Score" (1-10) and a "Risk Level" (Low/Med/High).
    
    **OUTPUT WORKFLOW (FOLLOW EXACTLY):**
    1. Call the `save_agent_report_to_state` tool with state_key="tech_analysis" and your FULL technical breakdown as detailed_report.
    2. Reply to the user ONLY with the following message and NOTHING ELSE: "Tech analysis completed internally."
    """
)

tech_debater = Agent(
    name="tech_debater",
    model=model_name,
    description="Critiques other analyses from a technical perspective.",
    tools=[save_agent_report_to_state],
    instruction="""
    ## ROLE: CTO Critique (VC Meeting)
    Review the Market Analysis ({ market_analysis }) and Finance Analysis ({ finance_analysis }).
    
    **CRITICAL INSTRUCTIONS:**
    - **COST REALITY:** Does the Tech Stack cost align with the Finance Analyst's "Cost Drivers"?
    - **FEATURE CREEP:** Did the Market Analyst suggest features that would add 6+ months to the dev cycle?
    - **SECURITY/COMPLIANCE:** Did the other agents ignore GDPR/HIPAA/SOC2 costs?

    **OUTPUT WORKFLOW (FOLLOW EXACTLY):**
    1. Call the `save_agent_report_to_state` tool with state_key="tech_critique" and detailed_report containing your "Technical Red Flag" report.
    2. Reply to the user ONLY with the following message and NOTHING ELSE: "Tech critiques saved internally."
    """
)
