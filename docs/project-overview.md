# # Project Overview — LinkedIn Organic Content Strategy for B2B SaaS

## Purpose

This project was developed as part of an AI Tools Onboarding portfolio assignment. It demonstrates the use of AI-assisted research workflows, Python automation, external APIs, Git, and GitHub to systematically collect, organize, and document knowledge from leading B2B SaaS marketing practitioners.

The repository combines automated transcript collection with structured research documentation to create a reusable knowledge base for LinkedIn organic content strategy.

---

## Topic

**LinkedIn Organic Content Strategy for B2B SaaS**

The research explores how leading B2B SaaS marketers use LinkedIn's organic features—including posts, newsletters, videos, comments, and thought leadership—to build brand awareness, generate demand, grow professional audiences, and establish industry authority.

---

## Repository Structure

```text

ai-tools-onboarding/

│

├── docs/

│   └── [project-overview.md](http://project-overview.md)

│

├── research/

│   ├── [methodology.md](http://methodology.md)

│   ├── [sources.md](http://sources.md)

│   ├── articles/

│   ├── linkedin-posts/

│   └── youtube-transcripts/

│

├── scripts/

│   ├── fetch_[transcripts.py](http://transcripts.py)

│   └── organize_[linkedin.py](http://linkedin.py)

│

├── .env

├── .gitignore

├── requirements.txt

└── [README.md](http://README.md)

```

---

## Tools Used

| Tool | Purpose |

|------|---------|

| Python 3 | Automation scripts and research workflows |

| youtube-transcript-api | Automated YouTube transcript retrieval |

| YouTube Data API v3 | Retrieval of video metadata |

| Git | Version control |

| GitHub | Repository hosting and portfolio presentation |

| Claude Code | AI-assisted research, documentation, and code generation |

| Cursor IDE | Development environment |

---

## Research Workflow

The project follows a structured workflow:

1. Select a recognized B2B marketing expert.

2. Collect recent LinkedIn posts.

3. Retrieve YouTube transcripts using Python automation.

4. Research additional resources such as blogs, newsletters, and websites.

5. Summarize findings into standardized Markdown documents.

6. Organize all research using Git version control.

---

## Running the Scripts

### Install dependencies

```bash

pip install -r requirements.txt

```

### Fetch a YouTube transcript

```bash

python scripts/fetch_[transcripts.py](http://transcripts.py) "<youtube_url>" "<expert_name>"

```

### Organize a LinkedIn post

```bash

python scripts/organize_[linkedin.py](http://linkedin.py) "<expert_name>" "<YYYY-MM-DD>" "<post_content>"

```

---

## Project Status

**Completed**

The repository contains research on ten leading B2B SaaS marketing practitioners, including LinkedIn post analysis, YouTube transcripts, curated learning resources, and structured research documentation.

