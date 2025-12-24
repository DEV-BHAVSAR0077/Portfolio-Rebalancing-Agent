def analysis_prompt(portfolio_summary: str) -> str:
    return f"""
You are a financial portfolio analysis agent.

Analyze the following portfolio allocation and identify:
- Overweight assets
- Underweight assets
- Allocation drift

Portfolio Data:
{portfolio_summary}
"""


def reasoning_prompt(portfolio_summary: str, rules: str) -> str:
    return f"""
You are an expert financial advisor.

Using the following rebalancing rules:
{rules}

Analyze the portfolio and decide:
- Which assets to reduce
- Which assets to increase
- Why rebalancing is required

Portfolio:
{portfolio_summary}
"""


def explanation_prompt(decision_text: str) -> str:
    return f"""
Explain the following rebalancing decision in simple, investor-friendly language.

Decision:
{decision_text}
"""
