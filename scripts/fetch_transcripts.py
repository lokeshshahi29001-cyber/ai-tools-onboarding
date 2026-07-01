"""
fetch_transcripts.py
Fetches a YouTube transcript via the Supadata API and saves it as a .md file.

Usage:
    python scripts/fetch_transcripts.py <youtube_url> <expert_name>

Example:
    python scripts/fetch_transcripts.py "https://www.youtube.com/watch?v=XXXXX" "jane-doe"
"""

import sys
import os
import re
import requests
from datetime import datetime

# ---------------------------------------------------------------------------
# Configuration — replace with your real key or load from a .env file
# ---------------------------------------------------------------------------
SUPADATA_API_KEY = "sd_02ba4147c9f540b10a8c1d37fa67c8bc"

SUPADATA_BASE_URL = "https://api.supadata.ai/v1/youtube/transcript"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "research", "youtube-transcripts")


def extract_video_id(url: str) -> str:
    """Pull the 11-character video ID out of a standard YouTube URL."""
    pattern = r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})"
    match = re.search(pattern, url)
    if not match:
        raise ValueError(f"Could not extract a video ID from URL: {url}")
    return match.group(1)


def fetch_transcript(video_id: str) -> dict:
    """Call the Supadata API and return the response JSON."""
    headers = {
        "x-api-key": SUPADATA_API_KEY,
        "Content-Type": "application/json",
    }
    params = {"videoId": video_id}

    response = requests.get(SUPADATA_BASE_URL, headers=headers, params=params, timeout=30)

    if response.status_code == 401:
        raise PermissionError("Invalid or missing Supadata API key.")
    if response.status_code == 404:
        raise FileNotFoundError(f"No transcript found for video ID: {video_id}")
    if not response.ok:
        raise RuntimeError(
            f"Supadata API error {response.status_code}: {response.text}"
        )

    return response.json()


def build_markdown(expert_name: str, video_url: str, video_id: str, data: dict) -> str:
    """Format the transcript payload as a Markdown document."""
    date_collected = datetime.utcnow().strftime("%Y-%m-%d")
    title = data.get("title", "Untitled")
    transcript_text = data.get("transcript", "")

    lines = [
        f"# Transcript: {title}",
        "",
        f"**Expert:** {expert_name}",
        f"**Source URL:** {video_url}",
        f"**Video ID:** {video_id}",
        f"**Date Collected:** {date_collected}",
        "",
        "---",
        "",
        "## Transcript",
        "",
        transcript_text,
    ]
    return "\n".join(lines)


def save_markdown(expert_name: str, video_id: str, content: str) -> str:
    """Write the Markdown content to the output directory and return the file path."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Sanitize expert name for use in a filename
    safe_name = re.sub(r"[^a-zA-Z0-9_-]", "-", expert_name).lower()
    filename = f"{safe_name}_{video_id}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


def main():
    if len(sys.argv) != 3:
        print("Usage: python scripts/fetch_transcripts.py <youtube_url> <expert_name>")
        sys.exit(1)

    youtube_url = sys.argv[1]
    expert_name = sys.argv[2]

    if SUPADATA_API_KEY == "YOUR_SUPADATA_API_KEY_HERE":
        print("Error: Please set your SUPADATA_API_KEY in fetch_transcripts.py before running.")
        sys.exit(1)

    print(f"Extracting video ID from: {youtube_url}")
    video_id = extract_video_id(youtube_url)
    print(f"Video ID: {video_id}")

    print("Fetching transcript from Supadata API...")
    data = fetch_transcript(video_id)

    print("Building Markdown document...")
    markdown = build_markdown(expert_name, youtube_url, video_id, data)

    filepath = save_markdown(expert_name, video_id, markdown)
    print(f"Transcript saved to: {filepath}")


if __name__ == "__main__":
    main()
