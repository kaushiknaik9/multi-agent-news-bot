from tasks import research_task, write_task
from agents import researcher, writter
from crewai import Crew, Process


def resultoutput():
    crew = Crew(
        agents=[researcher, writter],
        tasks=[research_task, write_task],
        process=Process.sequential,
    )

    inp = str(input("What news are you on now: "))
    og_inp = {"topic": inp}
    result = crew.kickoff(inputs=og_inp)
    final_result = result.raw

    return final_result
