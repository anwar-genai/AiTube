from typing import List, Optional
import os
import requests
from datetime import datetime, timedelta


YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "")
YOUTUBE_API_BASE = "https://www.googleapis.com/youtube/v3"


def list_channel_uploads(channel_id: str, max_results: int = 10) -> List[dict]:
    """Fetch recent videos from a YouTube channel"""
    if not YOUTUBE_API_KEY:
        print("⚠️  YOUTUBE_API_KEY not set - using mock data")
        return get_mock_videos()
    
    try:
        # Get channel's uploads playlist
        channel_url = f"{YOUTUBE_API_BASE}/channels"
        channel_params = {
            "part": "contentDetails",
            "id": channel_id,
            "key": YOUTUBE_API_KEY
        }
        
        response = requests.get(channel_url, params=channel_params)
        response.raise_for_status()
        channel_data = response.json()
        
        if not channel_data.get("items"):
            return []
        
        uploads_playlist_id = channel_data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
        
        # Get videos from uploads playlist
        playlist_url = f"{YOUTUBE_API_BASE}/playlistItems"
        playlist_params = {
            "part": "snippet",
            "playlistId": uploads_playlist_id,
            "maxResults": max_results,
            "key": YOUTUBE_API_KEY
        }
        
        response = requests.get(playlist_url, params=playlist_params)
        response.raise_for_status()
        playlist_data = response.json()
        
        videos = []
        for item in playlist_data.get("items", []):
            video_info = item["snippet"]
            videos.append({
                "video_id": video_info["resourceId"]["videoId"],
                "title": video_info["title"],
                "description": video_info["description"],
                "published_at": video_info["publishedAt"],
                "thumbnail": video_info["thumbnails"]["default"]["url"]
            })
        
        return videos
        
    except Exception as e:
        print(f"❌ Error fetching channel videos: {e}")
        return get_mock_videos()


def fetch_captions(video_id: str) -> Optional[str]:
    """Fetch captions/subtitles for a video"""
    if not YOUTUBE_API_KEY:
        print("⚠️  YOUTUBE_API_KEY not set - using mock captions")
        return get_mock_captions()
    
    try:
        # Get captions list
        captions_url = f"{YOUTUBE_API_BASE}/captions"
        captions_params = {
            "part": "snippet",
            "videoId": video_id,
            "key": YOUTUBE_API_KEY
        }
        
        response = requests.get(captions_url, params=captions_params)
        response.raise_for_status()
        captions_data = response.json()
        
        if not captions_data.get("items"):
            return None
        
        # For now, return a placeholder - real implementation would download captions
        return "Mock captions: This is a sample transcript of the video content..."
        
    except Exception as e:
        print(f"❌ Error fetching captions: {e}")
        return None


def get_mock_videos() -> List[dict]:
    """Return mock video data for testing"""
    return [
        {
            "video_id": "dQw4w9WgXcQ",
            "title": "Sample Video 1 - Introduction to Programming",
            "description": "Learn the basics of programming in this comprehensive tutorial",
            "published_at": (datetime.now() - timedelta(days=1)).isoformat() + "Z",
            "thumbnail": "https://img.youtube.com/vi/dQw4w9WgXcQ/default.jpg"
        },
        {
            "video_id": "jNQXAC9IVRw",
            "title": "Sample Video 2 - Advanced Concepts",
            "description": "Dive deeper into advanced programming concepts",
            "published_at": (datetime.now() - timedelta(days=2)).isoformat() + "Z",
            "thumbnail": "https://img.youtube.com/vi/jNQXAC9IVRw/default.jpg"
        }
    ]


def get_mock_captions() -> str:
    """Return mock captions for testing"""
    return """
    Welcome to this programming tutorial. In this video, we'll cover the fundamentals of 
    software development. We'll start with basic concepts and gradually move to more 
    advanced topics. This comprehensive guide will help you understand the core principles 
    of programming and give you a solid foundation to build upon.
    """


