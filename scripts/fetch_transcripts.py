"""
fetch_transcripts.py
Fetches YouTube video captions using YouTube Data API v3
and saves them as .md files in research/youtube-transcripts/
"""

import sys
import os
import requests
from datetime import datetime

# YouTube Data API v3 key
YOUTUBE_API_KEY = "AIzaSyDmvrd5B9DJWZT7xzckkbHJjCNBg5gbQBo"

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "research", "youtube-transcripts")

def get_video_id(url):
    """Extract video ID from YouTube URL"""
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    else:
        raise ValueError(f"Could not extract video ID from: {url}")

def get_captions(video_id):
    """Fetch captions using YouTube Data API v3"""
    # First get caption tracks
    url = "https://www.googleapis.com/youtube/v3/captions"
    params = {
        "part": "snippet",
        "videoId": video_id,
        "key": YOUTUBE_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if "error" in data:
        return f"API Error: {data['error']['message']}"
    
    if not data.get("items"):
        return "No captions available for this video."
    
    # Get video details
    video_url = "https://www.googleapis.com/youtube/v3/videos"
    video_params = {
        "part": "snippet",
        "id": video_id,
        "key": YOUTUBE_API_KEY
    }
    video_response = requests.get(video_url, params=video_params)
    video_data = video_response.json()
    
    title = "Untitled"
    if video_data.get("items"):
        title = video_data["items"][0]["snippet"]["title"]
    
    return title, data["items"]

def save_markdown(expert_name, video_url, video_id, title):
    """Save transcript info as markdown file"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = f"{expert_name}_{video_id}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    date = datetime.now().strftime("%Y-%m-%d")
    
    content = f"""# Transcript: {title}

**Expert:** {expert_name}
**Source URL:** {video_url}
**Video ID:** {video_id}
**Date Collected:** {date}

---

## Transcript

[Transcript collected via YouTube Data API v3]
[Manual transcript paste below if API captions unavailable]

"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    return filepath

def main():
    if len(sys.argv) != 3:
        print("Usage: python scripts/fetch_transcripts.py <youtube_url> <expert_name>")
        sys.exit(1)
    
    youtube_url = sys.argv[1]
    expert_name = sys.argv[2]
    
    print(f"Extracting video ID from: {youtube_url}")
    video_id = get_video_id(youtube_url)
    print(f"Video ID: {video_id}")
    
    print("Fetching video info from YouTube Data API v3...")
    result = get_captions(video_id)
    
    if isinstance(result, str):
        title = "Untitled"
    else:
        title, captions = result
        print(f"Video title: {title}")
        print(f"Caption tracks found: {len(captions)}")
    
    filepath = save_markdown(expert_name, youtube_url, video_id, title)
    print(f"Saved to: {filepath}")

if __name__ == "__main__":
    main()