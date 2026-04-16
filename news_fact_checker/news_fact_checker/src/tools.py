import os
from dotenv import load_dotenv
from crewai.tools import BaseTool
from newsapi import NewsApiClient
from exa_py import Exa
from pydantic import BaseModel, Field

load_dotenv()


# ------------------------------
# NEWS TOOL
# ------------------------------

class NewsSearchInput(BaseModel):
    query: str = Field(..., description="News search query")


class NewsSearchTool(BaseTool):
    name: str = "News Search Tool"
    description: str = "Searches recent news articles from trusted sources"
    args_schema: type[BaseModel] = NewsSearchInput

    def _run(self, query: str) -> str:
        """
        Fetch latest news articles using NewsAPI
        """
        newsapi = NewsApiClient(
            api_key=os.getenv("NEWS_API_KEY")
        )

        results = newsapi.get_everything(
            q=query,
            language="en",
            sort_by="publishedAt",
            page_size=5
        )

        articles = results.get("articles", [])

        if not articles:
            return "No news articles found."

        output = []

        for article in articles:
            output.append(
                f"""
Source: {article['source']['name']}
Title: {article['title']}
Description: {article['description']}
URL: {article['url']}
"""
            )

        return "\n".join(output)


# ------------------------------
# EXA SOCIAL TOOL
# ------------------------------

class SocialSearchInput(BaseModel):
    query: str = Field(..., description="Social trend query")


class SocialSearchTool(BaseTool):
    name: str = "Social Trend Tool"
    description: str = "Searches social discussions and public sentiment"
    args_schema: type[BaseModel] = SocialSearchInput

    def _run(self, query: str) -> str:
        """
        Fetch social discussions using Exa
        """
        exa = Exa(api_key=os.getenv("EXA_API_KEY"))

        results = exa.search_and_contents(
            query,
            num_results=5
        )

        output = []

        for result in results.results:
            output.append(
                f"""
Title: {result.title}
URL: {result.url}
Snippet: {result.text[:300]}
"""
            )

        return "\n".join(output)

