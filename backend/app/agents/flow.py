from typing import Optional

# Placeholder for LangGraph flow orchestration


class WatcherAgent:
    def run(self) -> list[dict]:
        return []


class TranscriptAgent:
    def run(self, video: dict) -> str:
        return ""


class SummarizerAgent:
    def run(self, transcript: str) -> dict:
        return {"summary_text": "", "hashtags": "", "keywords": ""}


class PublisherAgent:
    def run(self, video: dict, summary: dict) -> None:
        pass


def orchestrate(video: dict) -> Optional[dict]:
    transcript_agent = TranscriptAgent()
    summarizer_agent = SummarizerAgent()
    publisher_agent = PublisherAgent()

    transcript = transcript_agent.run(video)
    if transcript is None:
        return None
    summary = summarizer_agent.run(transcript)
    publisher_agent.run(video, summary)
    return summary


