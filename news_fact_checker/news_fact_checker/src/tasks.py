from crewai import Task
from src.agents import news_agent, social_agent, fact_checker, reporter


news_task = Task(
    description="Fetch latest news articles on {topic}",
    expected_output="Top news articles",
    agent=news_agent
)

social_task = Task(
    description="Find public sentiment and social discussions on {topic}",
    expected_output="Social sentiment report",
    agent=social_agent
)

fact_task = Task(
    description="Cross verify claims from collected news and social data",
    expected_output="Fact checked claims with confidence scores",
    agent=fact_checker
)

report_task = Task(
    description="Generate final news brief with confidence scores",
    expected_output="Professional report",
    agent=reporter
)



