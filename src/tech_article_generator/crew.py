from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tech_article_generator.llm.llm_config import llm
from tech_article_generator.tools.topic_tools import TopicTools

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class TechArticleGenerator():
    """TechArticleGenerator crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def chief_topic_strategist(self) -> Agent:
        topic_tools = TopicTools()
        return Agent(
            llm=llm,
            config=self.agents_config['chief_topic_strategist'],
            tools=topic_tools.get_all_tools,
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def topic_selection_task(self) -> Task:
        return Task(
            config=self.tasks_config['topic_selection_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TechArticleGenerator crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            llm=llm,  # Use the LLM defined in llm_config.py
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
