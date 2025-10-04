"""Sample LangGraph flow demonstrating branching:
caption available -> summarizer
no caption -> whisper(transcribe) -> summarizer

This is a minimal, non-executing stub to show structure.
"""

from typing import Dict, Any
from langgraph.graph import Graph


def node_fetch_caption(state: Dict[str, Any]) -> Dict[str, Any]:
    # pretend we checked for captions
    state["has_captions"] = bool(state.get("transcript"))
    return state


def node_whisper(state: Dict[str, Any]) -> Dict[str, Any]:
    # whisper transcription stub
    state["transcript"] = state.get("transcript") or "(transcript from whisper)"
    return state


def node_summarize(state: Dict[str, Any]) -> Dict[str, Any]:
    # summarization stub
    state["summary"] = {
        "summary_text": "",
        "hashtags": "",
        "keywords": "",
    }
    return state


def build_sample_graph() -> Graph:
    g = Graph()
    g.add_node("fetch_caption", node_fetch_caption)
    g.add_node("whisper", node_whisper)
    g.add_node("summarize", node_summarize)

    # Branch: if has_captions -> summarize, else -> whisper -> summarize
    g.add_edge("fetch_caption", "summarize", condition=lambda s: s.get("has_captions", False))
    g.add_edge("fetch_caption", "whisper", condition=lambda s: not s.get("has_captions", False))
    g.add_edge("whisper", "summarize")
    g.set_entry_point("fetch_caption")
    return g


