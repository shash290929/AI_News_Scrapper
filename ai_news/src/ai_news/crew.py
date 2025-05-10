from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileWriterTool
from typing import List
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class AiNews():
    """AiNews crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def retrieve_news(self) -> Agent:
        return Agent(
            config=self.agents_config['retrieve_news'],
            tools=[SerperDevTool()],
            verbose=True,
            # llm=self.ollama_llm
        )

    @agent
    def website_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['website_scraper'],
            tools=[ScrapeWebsiteTool()],
            verbose=True,
            # llm=self.ollama_llm
        )

    @agent
    def ai_news_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_news_writer'],
            tools=[],
            verbose=True,
            # llm=self.ollama_llm
        )

    @agent
    def file_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['file_writer'],
            tools=[FileWriterTool()],
            verbose=True,
            # llm=self.ollama_llm
        )

    @task
    def retrieve_news_task(self) -> Task:
        return Task(
            config=self.tasks_config['retrieve_news_task']
        )

    @task
    def website_scraper_task(self) -> Task:
        return Task(
            config=self.tasks_config['website_scraper_task']
        )

    @task
    def ai_news_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['ai_news_writer_task']
        )

    @task
    def file_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['file_writer_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AiNews crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
