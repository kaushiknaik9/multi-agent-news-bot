from crewai import Agent, LLM
import os
from dotenv import load_dotenv
from tools import tool

load_dotenv()

llm = LLM(
    model="gemini/gemini-2.5-flash",  # or your exact deployed model id
    api_key=os.getenv("GOOGLE_API_KEY"),
    verbose=True,
    temperature=0.5,
)

researcher = Agent(
    role="Senior Researcher",
    goal="Uncover ground breaking technologies in {topic}",
    verbose=True,
    memory=False,
    llm=llm,
    tools=[tool],
    backstory=(
        "Driven by curiosity, you're at the forefront of innovation, eager to "
        "explore and share knowledge that could change the world."
    ),
    allow_delegation=True,
)

writter = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=False,
    llm=llm,
    tools=[tool],
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging "
        "narratives that captivate and educate."
    ),
    allow_delegation=False,
)
