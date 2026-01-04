from typing import List

from agno.agent import Agent
from agno.models.openai import OpenAIChat


class QuestionGeneratorAgent:
    """
    Agent responsible for converting a research topic into
    structured market research questions.
    """

    def __init__(self) -> None:
        self.agent = Agent(
            name="Question Generator",
            model=OpenAIChat(
                
                temperature=0.3,
            ),
            instructions=[
                "You are a senior market research analyst.",
                "Your task is to generate high-quality research questions.",
                "Questions must help understand market size, trends, players, risks, and opportunities.",
                "Do NOT answer the questions.",
                "Output ONLY a numbered list of questions.",
                "Limit the output to 5–8 questions.",
            ],
        )

    def generate(self, topic: str, domain: str) -> List[str]:
        """
        Generate research questions for a given topic and domain.
        """
        prompt = (
            f"Research Topic: {topic}\n"
            f"Industry / Domain: {domain}\n\n"
            "Generate market research questions."
        )

        response = self.agent.run(prompt)

        questions = [
            line.strip()
            for line in response.content.split("\n")
            if line.strip()
        ]

        return questions
from typing import List

from agno.agent import Agent
from agno.models.openai import OpenAIChat


class QuestionGeneratorAgent:
    """
    Agent responsible for converting a research topic into
    structured market research questions.
    """

    def __init__(self) -> None:
        self.agent = Agent(
            name="Question Generator",
            model=OpenAIChat(
                
                temperature=0.3,
            ),
            instructions=[
                "You are a senior market research analyst.",
                "Your task is to generate high-quality research questions.",
                "Questions must help understand market size, trends, players, risks, and opportunities.",
                "Do NOT answer the questions.",
                "Output ONLY a numbered list of questions.",
                "Limit the output to 5–8 questions.",
            ],
        )

    def generate(self, topic: str, domain: str) -> List[str]:
        """
        Generate research questions for a given topic and domain.
        """
        prompt = (
            f"Research Topic: {topic}\n"
            f"Industry / Domain: {domain}\n\n"
            "Generate market research questions."
        )

        response = self.agent.run(prompt)

        questions = [
            line.strip()
            for line in response.content.split("\n")
            if line.strip()
        ]

        return questions
