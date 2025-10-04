from typing import List, Optional
import os
import requests


YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "")


def list_channel_uploads(channel_id: str) -> List[dict]:
    # Minimal stub; replace with real YouTube Data API calls
    return []


def fetch_captions(video_id: str) -> Optional[str]:
    # Stub: would call YouTube Captions API
    return None


