# AI Tools Onboarding

## Overview
This repository documents the setup process completed as part of a portfolio assignment.

## Tools Installed
- Cursor IDE
- Claude Code CLI
- Codex CLI
- Git
- GitHub

## Steps Completed
1. Installed Cursor IDE.
2. Installed Claude Code via the official terminal installer and logged in.
3. Installed Codex CLI via npm and logged in.
4. Created a public GitHub repository.
5. Opened the repository in Cursor.
6. Created this README file.
7. Committed and pushed the repository to GitHub.

## Issues Encountered
- Git was not initially recognized in the terminal, even though it was already installed — resolved by restarting the IDE so it picked up the correct PATH.
- The Codex login session timed out on the first attempt; re-running the login command completed it successfully.

## Outcome
The development environment has been successfully configured and is ready for future portfolio projects.

---

## Research Project — LinkedIn Organic Content Strategy for B2B SaaS

### Topic Chosen
LinkedIn Organic Content Strategy for B2B SaaS — how practitioners and companies use LinkedIn's non-paid features (posts, carousels, newsletters, comments) to build pipeline and thought leadership.

### Why This Topic
LinkedIn organic content is one of the highest-ROI channels for B2B SaaS companies and a rapidly evolving space. Studying how top practitioners approach it produces immediately applicable frameworks and demonstrates domain knowledge relevant to GTM and marketing roles.

### Tools Used
- **Python 3** — scripting for transcript fetching and content organisation
- **youtube-transcript-api** – automated YouTube transcript extraction
- **YouTube Data API v3** – retrieval of video metadata (title, ID, channel information)
- **Git & GitHub** — version control and portfolio presentation
- **Claude Code** — AI-assisted research, code generation, and documentation
- **Cursor IDE** — development environment

### Implementation Notes

The project initially attempted to use the Supadata API for YouTube transcript retrieval. Although the API connected successfully, it consistently returned empty transcript content for the tested videos.

To ensure reliable transcript collection, the implementation was updated to use the `youtube-transcript-api` library for transcript extraction together with the YouTube Data API v3 for retrieving video metadata. This solution successfully generated complete transcript files for the research repository.

### Repository Structure
```
ai-tools-onboarding/
├── docs/
│   └── project-overview.md
├── research/
│   ├── methodology.md
│   ├── sources.md
│   ├── linkedin-posts/
│   ├── youtube-transcripts/
│   └── articles/
├── scripts/
│   ├── fetch_transcripts.py
│   └── organize_linkedin.py
├── .gitignore
└── requirements.txt
```

### Expert List
Experts will be added to `research/sources.md` as research progresses. Placeholders are in place — no names have been invented.

| Expert Name | Platform | Status |
|-------------|----------|--------|
| _To be added_ | LinkedIn / YouTube | Pending |