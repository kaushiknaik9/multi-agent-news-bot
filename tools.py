from crewai_tools import SerpApiGoogleSearchTool
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY", "")
tool = SerpApiGoogleSearchTool()
