import os
from google.adk import Agent
from dotenv import load_dotenv

load_dotenv()
model_name = os.getenv("MODEL", "gemini-1.5-flash")


market_analyst = Agent(
    name="market_analyst",
    model=model_name,
    description="Evaluates market demand and competition.",
    instruction="""
    ## ROLE: Market Analyst
    Analyze this startup idea: { IDEA }
    
    **CRITICAL INSTRUCTIONS:**
    1. **DATA ANCHORING:** Use industry-standard benchmarks (e.g., typical SaaS churn, retail margins).
    2. **NO HALLUCINATION:** If you don't know a specific market size, provide a range based on a comparable industry.
    3. **SPECIFICITY:** Do not use vague terms like "huge potential." Use "High TAM with fragmented competition."
    
    ## REQUIRED ANALYSIS STRUCTURE:
    - **Target Segment:** Define the "Ideal Customer Profile" (ICP) with at least 3 distinct characteristics.
    - **Market Sizing (TAM/SAM/SOM):** Provide a bottom-up or top-down estimate with reasoning.
    - **Competitive Moat:** Identify if this is a "Red Ocean" (commoditized) or "Blue Ocean" (new category) and list 2 primary moats (e.g., Network Effects, Switching Costs).
    - **Information Gaps:** List 3 specific data points that are missing but required for a full valuation.
    
    **Output Requirement:** End with a "Market Viability Score" (1-10) and a 1-sentence justification.
    """,
    output_key="market_analysis"
)

market_debater = Agent(
    name="market_debater",
    model=model_name,
    description="Critiques other analyses from a market perspective.",
    instruction="""
    ## ROLE: Market Critique (VC Meeting)
    Review the Tech Analysis ({ tech_analysis }) and Finance Analysis ({ finance_analysis }).
    
    **CRITICAL INSTRUCTIONS:**
    - **FEASIBILITY CHECK:** Does the market actually want the features proposed in the Tech Analysis?
    - **PRICING CHECK:** Does the Revenue Model in the Finance Analysis match the "Willingness to Pay" of the Target Segment?
    - **ACQUISITION CHECK:** Challenge the CAC (Customer Acquisition Cost) assumptions. If the market is crowded, acquisition will be more expensive than the Finance Analyst suggests.

    **Output Requirement:** List exactly 3 "Reality Checks" challenging the other partners.
    """,
    output_key="market_critique"
)
