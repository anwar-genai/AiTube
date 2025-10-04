#!/usr/bin/env python3
"""
Script to add popular programming channels to AITube
"""
import requests
import json

# Popular programming channels
POPULAR_CHANNELS = [
    {
        "owner_id": 1,
        "external_id": "UC8butISFwT-Wl7EV0hUK0BQ",
        "platform": "youtube",
        "title": "freeCodeCamp.org"
    },
    {
        "owner_id": 1,
        "external_id": "UCBJycsmduvYEL83R_U4JriQ",
        "platform": "youtube", 
        "title": "Marques Brownlee"
    },
    {
        "owner_id": 1,
        "external_id": "UCuAXFkgsw1L7xaCfnd5JJOw",
        "platform": "youtube",
        "title": "Traversy Media"
    },
    {
        "owner_id": 1,
        "external_id": "UCW5YeuERMmlnqo4oq8vwUpg",
        "platform": "youtube",
        "title": "The Net Ninja"
    },
    {
        "owner_id": 1,
        "external_id": "UC29ju8bIPH5as8OGNQhyg",
        "platform": "youtube",
        "title": "Programming with Mosh"
    }
]

def add_channels():
    """Add popular channels to the system"""
    base_url = "http://localhost:8001"
    
    print("🚀 Adding popular programming channels...")
    
    for channel in POPULAR_CHANNELS:
        try:
            response = requests.post(
                f"{base_url}/channels/",
                json=channel,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                print(f"✅ Added: {channel['title']}")
            elif response.status_code == 400:
                print(f"⚠️  Already exists: {channel['title']}")
            else:
                print(f"❌ Error adding {channel['title']}: {response.text}")
                
        except Exception as e:
            print(f"❌ Error adding {channel['title']}: {e}")
    
    print("\n🎯 Now you can:")
    print("1. Visit http://localhost:8001/docs")
    print("2. Try POST /monitor/start to process all channels")
    print("3. Check GET /videos/ to see processed videos")

if __name__ == "__main__":
    add_channels()
