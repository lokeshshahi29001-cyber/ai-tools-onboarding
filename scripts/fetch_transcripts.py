"""
fetch_transcripts.py
Fetches YouTube transcripts using youtube-transcript-api
and saves them as .md files in research/youtube-transcripts/
"""

import sys
import os
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi
import requests

# YouTube Data API v3 key (used for video metadata)
YOUTUBE_API_KEY = "YOUTUBE_API_KEY = "YOUR_YOUTUBE_API_KEY_HERE""

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "research", "youtube-transcripts")

def get_video_id(url):
    """Extract video ID from YouTube URL"""
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    else:
        raise ValueError(f"Could not extract video ID from: {url}")

def get_video_title(video_id):
    """Get video title using YouTube Data API v3"""
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "snippet",
        "id": video_id,
        "key": YOUTUBE_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data.get("items"):
        return data["items"][0]["snippet"]["title"]
    return "Untitled"

def get_transcript(video_id):
    """Fetch transcript using youtube-transcript-api"""
    transcript_list = YouTubeTranscriptApi().fetch(video_id)
    full_text = " ".join([entry.text for entry in transcript_list])
    return full_text

def save_markdown(expert_name, video_url, video_id, title, transcript):
    """Save transcript as markdown file"""
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

{transcript}
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

    print("Fetching video title...")
    title = get_video_title(video_id)
    print(f"Title: {title}")

    print("Fetching transcript...")
    transcript = get_transcript(video_id)
    print("Transcript fetched successfully!")

    filepath = save_markdown(expert_name, youtube_url, video_id, title, transcript)
    print(f"Saved to: {filepath}")

if __name__ == "__main__":
    main()