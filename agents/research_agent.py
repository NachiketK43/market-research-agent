import os
from typing import Dict, List

import httpx
from agno.agent import Agent
from agno.models.openai import OpenAIChat


class ResearchAgent:
    """
    Agent responsible for researching a single question
    using real-world search data and synthesizing insights.
    """

    def __init__(self) -> None:
        self.serpapi_key = os.getenv("SERPAPI_API_KEY")
        if not self.serpapi_key:
            raise ValueError("SERPAPI_API_KEY not found in environment variables")

        self.agent = Agent(
            name="Research Agent",
            model=OpenAIChat(
                
                temperature=0.2,
            ),
            instructions=[
                "You are a market research analyst.",
                "Use the provided search results to answer the question.",
                "Be factual and concise.",
                "Cite sources by referencing their URLs.",
                "If information is insufficient, say so clearly.",
            ],
        )

    async def _search(self, query: str) -> List[Dict[str, str]]:
        """
        Perform an async Google search using SerpAPI.
        """
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(
                "https://serpapi.com/search",
                params={
                    "q": query,
                    "api_key": self.serpapi_key,
                    "engine": "google",
                    "num": 5,
                },
            )
            response.raise_for_status()
            data = response.json()

        results = []
        for item in data.get("organic_results", []):
            results.append(
                {
                    "title": item.get("title", ""),
                    "snippet": item.get("snippet", ""),
                    "link": item.get("link", ""),
                }
            )

        return results

    async def research(self, question: str) -> Dict[str, object]:
        """
        Async research for a single question.
        """
        search_results = await self._search(question)

        context = "\n\n".join(
            f"Title: {r['title']}\nSnippet: {r['snippet']}\nURL: {r['link']}"
            for r in search_results
        )

        prompt = (
            f"Question:\n{question}\n\n"
            f"Search Results:\n{context}\n\n"
            "Provide a synthesized answer with citations."
        )

        response = await self.agent.arun(prompt)

        sources = [r["link"] for r in search_results if r["link"]]

        return {
            "question": question,
            "answer": response.content,
            "sources": sources,
        }
