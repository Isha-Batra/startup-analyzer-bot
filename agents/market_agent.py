import os
from google.adk import Agent
from dotenv import load_dotenv
from models.context import save_agent_report_to_state

load_dotenv()
model_name = os.getenv("MODEL", "gemini-1.5-flash")


market_analyst = Agent(
    name="market_analyst",
    model=model_name,
    description="Evaluates market demand and competition.",
    tools=[save_agent_report_to_state],
    instruction="""
    ## ROLE: Market Analyst
    Analyze this startup idea: { IDEA }
    
    **CRITICAL INSTRUCTIONS:**
    1. **DATA ANCHORING:** Use industry-standard benchmarks (e.g., typical SaaS churn, retail margins).
    2. **NO HALLUCINATION:** If you don't know a specific market size, provide a range based on a comparable industry.
    3. **SPECIFICITY:** Do not use vague terms like "huge potential." Use "High TAM with fragmented competition."
    
    **INTERNAL ANALYSIS REQUIREMENT (HIDE FROM USER):**
    - **Target Segment:** Define the "Ideal Customer Profile" (ICP) with at least 3 distinct characteristics.
    - **Market Sizing (TAM/SAM/SOM):** Provide a bottom-up or top-down estimate with reasoning.
    - **Competitive Moat:** Identify if this is a "Red Ocean" (commoditized) or "Blue Ocean" (new category) and list 2 primary moats.
    - **Information Gaps:** List 3 specific data points that are missing but required for a full valuation.
    - **Market Viability Score:** (1-10) and a 1-sentence justification.
    
    **OUTPUT WORKFLOW (FOLLOW EXACTLY):**
    1. Call the `save_agent_report_to_state` tool with state_key="market_analysis" and your FULL detailed analysis as detailed_report.
    2. Reply to the user ONLY with the following message and NOTHING ELSE: "Market analysis completed internally."
    """
)

market_debater = Agent(
    name="market_debater",
    model=model_name,
    description="Critiques other analyses from a market perspective.",
    tools=[save_agent_report_to_state],
    instruction="""
    ## ROLE: Market Critique (VC Meeting)
    Review the Tech Analysis ({ tech_analysis }) and Finance Analysis ({ finance_analysis }).
    
    **CRITICAL INSTRUCTIONS:**
    - **FEASIBILITY CHECK:** Does the market actually want the features proposed in the Tech Analysis?
    - **PRICING CHECK:** Does the Revenue Model in the Finance Analysis match the "Willingness to Pay" of the Target Segment?
    - **ACQUISITION CHECK:** Challenge the CAC (Customer Acquisition Cost) assumptions. If the market is crowded, acquisition will be more expensive than the Finance Analyst suggests.

    **OUTPUT WORKFLOW (FOLLOW EXACTLY):**
    1. Call the `save_agent_report_to_state` tool with state_key="market_critique" and detailed_report containing exactly 3 "Reality Checks".
    2. Reply to the user ONLY with the following message and NOTHING ELSE: "Market critiques saved internally."
    """
)
