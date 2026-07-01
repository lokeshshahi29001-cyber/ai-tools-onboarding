"""
organize_linkedin.py
Saves a LinkedIn post as a formatted .md file in research/linkedin-posts/.

Usage:
    python scripts/organize_linkedin.py <expert_name> <post_date> <post_content>

Example:
    python scripts/organize_linkedin.py "jane-doe" "2026-06-15" "Your post text here..."

Note: For post_content that contains spaces, wrap the argument in quotes.
"""

import sys
import os
import re
from datetime import datetime

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "research", "linkedin-posts")


def build_markdown(expert_name: str, post_date: str, post_content: str) -> str:
    """Format the LinkedIn post using the standard research template."""
    date_collected = datetime.utcnow().strftime("%Y-%m-%d")

    lines = [
        f"# LinkedIn Post — {expert_name}",
        "",
        f"**Expert:** {expert_name}",
        f"**Date:** {post_date}",
        f"**Source:** LinkedIn",
        f"**Date Collected:** {date_collected}",
        "",
        "---",
        "",
        "## Summary",
        "",
        "_Add a 1–2 sentence summary of the post here._",
        "",
        "## Key Takeaways",
        "",
        "- _Takeaway 1_",
        "- _Takeaway 2_",
        "- _Takeaway 3_",
        "",
        "---",
        "",
        "## Original Post Content",
        "",
        post_content,
    ]
    return "\n".join(lines)


def save_markdown(expert_name: str, post_date: str, content: str) -> str:
    """Write the Markdown content to the output directory and return the file path."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Sanitize inputs for use in a filename
    safe_name = re.sub(r"[^a-zA-Z0-9_-]", "-", expert_name).lower()
    safe_date = re.sub(r"[^0-9-]", "", post_date)
    filename = f"{safe_name}_{safe_date}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


def main():
    if len(sys.argv) != 4:
        print(
            "Usage: python scripts/organize_linkedin.py "
            "<expert_name> <post_date> <post_content>"
        )
        sys.exit(1)

    expert_name = sys.argv[1]
    post_date = sys.argv[2]
    post_content = sys.argv[3]

    print(f"Building Markdown for: {expert_name} ({post_date})")
    markdown = build_markdown(expert_name, post_date, post_content)

    filepath = save_markdown(expert_name, post_date, markdown)
    print(f"Post saved to: {filepath}")


if __name__ == "__main__":
    main()
