from agents import researcher, writter
from crewai import Task
from tools import tool

research_task = Task(
    description=(
        "identify the next big trends in {topic}."
        "Focus on identifying pros cosn and the overall narrative."
        "your final report should clearly articulate the key points,"
        "its market opportunities, and potential risks."
    ),
    expected_output="A comprehensive 3 parahgraph long report on the latest AI trends.",
    tools=[tool],
    agent=researcher,
)

write_task = Task(
    description=(
        "Compose an insightful article on {topic}."
        "Focus on the latest trends and how it's impacting the industry."
        "this article should be easy to understand, engaging and positive."
    ),
    expected_output="A 4 full parah article on {topic}  advancements formatted as markdown.",
    tools=[tool],
    agent=writter,
    context=[research_task],
    async_execution=False,
    output_file="result.md",
)
