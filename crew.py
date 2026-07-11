from tasks import research_task, write_task
from agents import researcher, writter
from crewai import Crew, Process


def resultoutput(topic):
    crew = Crew(
        agents=[researcher, writter],
        tasks=[research_task, write_task],
        process=Process.sequential,
    )

    result = crew.kickoff(inputs={"topic": topic})

    return str(result)
