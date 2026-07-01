# Project Overview — LinkedIn Organic Content Strategy for B2B SaaS

## Purpose

This project is a research repository built as part of a portfolio hiring assignment. It demonstrates the ability to use AI-assisted research workflows, Python scripting, external APIs, and version control to collect and organise domain knowledge systematically.

---

## Topic

**LinkedIn Organic Content Strategy for B2B SaaS**

The research focuses on how B2B SaaS companies and practitioners use LinkedIn's organic (non-paid) features — posts, carousels, newsletters, comments — to build pipeline, grow audiences, and establish thought leadership.

---

## Repository Structure

```
ai-tools-onboarding/
├── docs/
│   └── project-overview.md       # This file
├── research/
│   ├── methodology.md            # How research is collected and organised
│   ├── sources.md                # Tracker table of all experts and content
│   ├── linkedin-posts/           # Saved LinkedIn posts (.md files)
│   ├── youtube-transcripts/      # Saved YouTube transcripts (.md files)
│   └── articles/                 # Saved articles and blog posts (.md files)
├── scripts/
│   ├── fetch_transcripts.py      # Fetches YouTube transcripts via Supadata API
│   └── organize_linkedin.py      # Saves LinkedIn posts as formatted .md files
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Python 3 | Scripting — transcript fetching and content organisation |
| Supadata API | Fetching YouTube video transcripts programmatically |
| Git | Version control for all research files and scripts |
| GitHub | Remote repository and portfolio presentation |
| Claude Code | AI-assisted research, code generation, and documentation |
| Cursor IDE | Code editing environment |

---

## How to Run the Scripts

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Fetch a YouTube transcript:**
```bash
python scripts/fetch_transcripts.py "https://www.youtube.com/watch?v=XXXXX" "expert-name"
```

**Save a LinkedIn post:**
```bash
python scripts/organize_linkedin.py "expert-name" "2026-06-15" "Post content goes here..."
```

---

## Status

Research in progress. See `research/sources.md` for the current collection tracker.
