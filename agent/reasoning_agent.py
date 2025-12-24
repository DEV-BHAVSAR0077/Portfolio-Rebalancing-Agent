import openai
from agent.prompt_templates import (
    analysis_prompt,
    reasoning_prompt,
    explanation_prompt
)

class RebalancingAgent:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def _call_llm(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response["choices"][0]["message"]["content"]

    def run_agent(self, portfolio_df, rules_text: str):
        portfolio_summary = portfolio_df.to_string(index=False)

        # Step 1: Analysis
        analysis_output = self._call_llm(
            analysis_prompt(portfolio_summary)
        )

        # Step 2: Reasoning
        reasoning_output = self._call_llm(
            reasoning_prompt(portfolio_summary, rules_text)
        )

        # Step 3: Explanation
        explanation_output = self._call_llm(
            explanation_prompt(reasoning_output)
        )

        return {
            "analysis": analysis_output,
            "decision": reasoning_output,
            "explanation": explanation_output
        }
