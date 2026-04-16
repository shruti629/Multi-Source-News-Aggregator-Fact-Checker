from crewai import Agent, LLM
from src.tools import NewsSearchTool, SocialSearchTool
import os
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("google_api_key")
)

news_agent = Agent(
    role="News Aggregator",
    goal="Fetch latest news",
    backstory="Expert journalist",
    tools=[NewsSearchTool()],
    llm=llm,
    verbose=True
)

social_agent = Agent(
    role="Social Analyst",
    goal="Track social discussions",
    backstory="Expert in trend detection",
    tools=[SocialSearchTool()],
    llm=llm,
    verbose=True
)

fact_checker = Agent(
    role="Fact Checker",
    goal="Cross verify news claims",
    backstory="Expert fact checking analyst",
    llm=llm,
    verbose=True
)

reporter = Agent(
    role="Reporter",
    goal="Generate final fact checked report",
    backstory="Professional newsroom editor",
    llm=llm,
    verbose=True
)

