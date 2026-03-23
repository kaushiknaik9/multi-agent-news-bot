# Multi-Agent AI News Researcher (CrewAI + Gemini + SerpAPI)

This project is a multi‑agent news researcher built with **CrewAI**, **Google Gemini**, and the **SerpApi Google Search Tool**. It lets you enter a news topic and get:

- A research report on current trends and key points.
- A readable, blog‑style article based on that research.

---

## Features

- Two cooperative agents:
  - **Senior Researcher** – uses SerpAPI to gather and analyze information about `{topic}`.
  - **Writer** – converts the research into an engaging article.
- Sequential task flow (research → write).
- Google Gemini as the LLM backend.
- SerpAPI for web/news search.

---

## Project Structure

```text
multiagentcrewainews/
├─ crew.py          # Crew setup and kickoff (entry point)
├─ agents.py        # Agent definitions (researcher, writter)
├─ tasks.py         # Task definitions (research_task, write_task)
├─ tools.py         # SerpApiGoogleSearchTool wrapper (tool)
├─ .env             # API keys (not committed)
├─ requirements.txt # Python dependencies
└─ result.md        # Generated article output (created at runtime)
```
