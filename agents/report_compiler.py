from typing import List, Dict

from agno.agent import Agent
from agno.models.openai import OpenAIChat


class ReportCompilerAgent:
    """
    Agent responsible for compiling multiple research findings
    into a professional market research report.
    """

    def __init__(self) -> None:
        self.agent = Agent(
            name="Report Compiler",
            model=OpenAIChat(
                
                temperature=0.3,
            ),
            instructions=[
                "You are a senior market research consultant.",
                "Your task is to compile a professional research report.",
                "Use the provided research findings as source material.",
                "Write in a clear, structured, and executive-friendly tone.",
                "Do not invent facts beyond the provided findings.",
                "Structure the report with clear section headers.",
            ],
        )

    def compile(self, findings: List[Dict[str, object]]) -> str:
        """
        Compile research findings into a structured report.
        """
        formatted_findings = "\n\n".join(
            f"Question: {item['question']}\n"
            f"Answer: {item['answer']}\n"
            f"Sources: {', '.join(item['sources'])}"
            for item in findings
        )

        prompt = (
            "Using the following research findings, generate a market research report.\n\n"
            "The report must include:\n"
            "1. Executive Summary\n"
            "2. Market Overview\n"
            "3. Key Trends and Insights\n"
            "4. Risks and Opportunities\n"
            "5. Conclusion / Recommendations\n\n"
            f"Research Findings:\n{formatted_findings}"
        )

        response = self.agent.run(prompt)
        return response.content
