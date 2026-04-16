from crewai import Crew, Process
from src.agents import news_agent, social_agent, fact_checker, reporter
from src.tasks import news_task, social_task, fact_task, report_task


collection_crew = Crew(
    agents=[news_agent, social_agent],
    tasks=[news_task, social_task],
    process=Process.sequential,
    verbose=True
)

verification_crew = Crew(
    agents=[fact_checker, reporter],
    tasks=[fact_task, report_task],
    process=Process.sequential,
    verbose=True
)
