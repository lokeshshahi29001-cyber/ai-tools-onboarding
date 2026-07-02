# AI Tools Onboarding & Research Project

## Overview

This repository documents the completion of an AI Tools Onboarding portfolio assignment together with a research project on **LinkedIn Organic Content Strategy for B2B SaaS**. The project includes the setup of modern AI development tools, automation scripts for collecting YouTube transcripts, and structured research on leading B2B marketing practitioners.

---

# AI Tools Onboarding

## Tools Installed

- Cursor IDE
- Claude Code CLI
- Codex CLI
- Git
- GitHub

---

## Steps Completed

1. Installed Cursor IDE.
2. Installed Claude Code using the official installer and authenticated successfully.
3. Installed Codex CLI via npm and completed authentication.
4. Created a public GitHub repository.
5. Opened the repository in Cursor IDE.
6. Created the project folder structure and documentation.
7. Configured Git version control.
8. Committed and pushed the repository to GitHub.

---

## Issues Encountered

### Git PATH Issue

Git was already installed but was not initially recognized inside the terminal. Restarting Cursor refreshed the system PATH and resolved the issue.

### Codex CLI Authentication

The first login session expired before completion. Running the authentication command again successfully completed the authentication process.

### Supadata API – Empty Transcript Responses

The project initially used the Supadata API for YouTube transcript retrieval. Although the API connected successfully and returned valid responses, transcript content was consistently empty for the tested videos.

After evaluating alternative approaches, the implementation was migrated to the **youtube-transcript-api** library combined with the **YouTube Data API v3**, which successfully retrieved complete transcript data.

### API Key Management

During development, a YouTube Data API key was accidentally committed to the public repository. GitHub Secret Scanning immediately detected the exposed credential.

The key was revoked, regenerated, and moved into a `.env` file excluded from version control using `.gitignore`, following secure credential management best practices.

---

## Outcome

The AI development environment was successfully configured with all required tools installed, authenticated, and verified.

The completed environment was then used to build an automated research workflow for collecting YouTube transcripts, organizing research assets, and managing the project using Git and GitHub.

---

# Research Project

## Topic Chosen

**LinkedIn Organic Content Strategy for B2B SaaS**

This project researches how leading B2B practitioners and companies use LinkedIn's organic features—including posts, newsletters, comments, and thought leadership—to generate pipeline, build authority, and grow B2B SaaS businesses.

---

## Why This Topic

LinkedIn has become one of the highest-ROI organic acquisition channels for B2B SaaS companies.

Studying successful practitioners provides practical frameworks for:

- Personal branding
- Demand generation
- Content marketing
- Thought leadership
- Community building
- AI-assisted marketing

The project demonstrates both technical implementation skills and marketing domain knowledge.

---

## Tools Used

- Python 3
- Cursor IDE
- Claude Code
- Codex CLI
- Git
- GitHub
- Supadata API (initial implementation)
- youtube-transcript-api
- YouTube Data API v3

---

## Implementation Notes

The initial implementation attempted to retrieve YouTube transcripts using the **Supadata API**. Although the API connection was successful, transcript responses consistently returned empty content.

To improve reliability, the implementation was migrated to the **youtube-transcript-api** library for transcript extraction together with the **YouTube Data API v3** for retrieving video metadata.

This approach successfully generated complete transcript files and metadata for the research repository.

---

## Repository Structure

```text
ai-tools-onboarding/
│
├── docs/
│   └── project-overview.md
│
├── research/
│   ├── methodology.md
│   ├── sources.md
│   ├── linkedin-posts/
│   ├── youtube-transcripts/
│   └── articles/
│
├── scripts/
│   ├── fetch_transcripts.py
│   └── organize_linkedin.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Research Results

The completed research repository includes:

- LinkedIn post analysis for 10 B2B marketing experts
- Automated YouTube transcript collection
- Additional learning resources for every expert
- Structured Markdown documentation
- Python automation for transcript retrieval
- Organized research assets for future reference

---

## Experts Researched

| Expert | Platform | Status |
|---------|----------|--------|
| Amanda Natividad | LinkedIn / YouTube | ✅ Completed |
| Dave Gerhardt | LinkedIn / YouTube | ✅ Completed |
| Devin Reed | LinkedIn / YouTube | ✅ Completed |
| Justin Welsh | LinkedIn / YouTube | ✅ Completed |
| Kieran Flanagan | LinkedIn / YouTube | ✅ Completed |
| Kyle Coleman | LinkedIn / YouTube | ✅ Completed |
| Lara Acosta | LinkedIn / YouTube | ✅ Completed |
| Morgan J. Ingram | LinkedIn / YouTube | ✅ Completed |
| Rand Fishkin | LinkedIn / YouTube | ✅ Completed |
| Ross Simmonds | LinkedIn / YouTube | ✅ Completed |

---

## Skills Demonstrated

- Python scripting
- API integration
- AI development environment setup
- Git & GitHub workflow
- YouTube transcript automation
- Technical documentation
- Markdown documentation
- Research organization
- Prompt engineering
- Marketing research
- AI-assisted productivity

---

## Future Improvements

- Automate LinkedIn post collection
- Generate AI summaries from YouTube transcripts
- Create a searchable research index
- Build a lightweight RAG system over the research dataset
- Develop a simple web interface for browsing research

---

## Author

**Lokesh Kumar**

AI Tools Onboarding Portfolio Assignment

Developed using **Cursor IDE, Claude Code, Codex CLI, Python, Git, and GitHub**.