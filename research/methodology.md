# Research Methodology

## Topic

LinkedIn Organic Content Strategy for B2B SaaS

---

## 1. Expert Selection Criteria

Experts are selected based on the following criteria:

- **Relevance** — The expert actively publishes content specifically about LinkedIn strategy, B2B SaaS marketing, or organic growth.

- **Audience size** — A minimum established following on LinkedIn or YouTube that indicates credibility and reach.

- **Recency** — Content published within the last 12 months is prioritised to ensure the advice reflects current platform behaviour.

- **Depth** — Preference for practitioners who share original frameworks or data rather than purely opinion-based content.

- **Diversity** — The expert list represents a range of company sizes, geographies, and roles (founders, CMOs, content strategists).

---

## 2. Transcript Collection — YouTube Data API v3

YouTube transcripts are collected using the `youtube-transcript-api` Python library combined with the YouTube Data API v3 for video metadata retrieval.

> **Note:** The project initially attempted to use the Supadata API for transcript collection. Although the API connected successfully, transcript responses were consistently empty for all tested videos. After evaluating alternatives, the implementation was migrated to `youtube-transcript-api`, which successfully retrieved complete transcripts.

### Process

1. Identify a relevant YouTube video by the selected expert.

2. Copy the full video URL.

3. Run `scripts/fetch_transcripts.py` with the URL and expert name as arguments:

python scripts/fetch_[transcripts.py](http://transcripts.py) "<youtube_url>" "<expert_name>"

4. The script extracts the video ID, fetches the full transcript using `youtube-transcript-api`, retrieves video metadata (title, video ID) via YouTube Data API v3, and saves everything as a `.md` file in `research/youtube-transcripts/`.

5. The saved file includes the video title, source URL, video ID, date collected, and full transcript text.

### API Key Management

The `YOUTUBE_API_KEY` variable is stored in a `.env` file that is excluded from version control via `.gitignore`. The key is never committed to the public repository.

> **Note:** During development, the YouTube API key was accidentally committed to the public repository. GitHub Secret Scanning detected the exposed credential immediately. The key was revoked, a new key was generated, and secure credential management via `.env` was implemented.

---

## 3. LinkedIn Content Organisation

LinkedIn posts are saved using `scripts/organize_linkedin.py`.

### Process

1. Identify a post by a selected expert on LinkedIn.

2. Copy the post text manually from LinkedIn.

3. Run the script with the expert name, post date, and post content:

python scripts/organize_[linkedin.py](http://linkedin.py) "<expert_name>" "<YYYY-MM-DD>" "<post_content>"

4. The script generates a `.md` file in `research/linkedin-posts/` using a standard template: Expert, Date, Source, Summary, Key Takeaways, and Original Post Content.

5. The Summary and Key Takeaways sections are filled in manually after reviewing the post.

> **Note:** LinkedIn does not provide a public API for post collection. All LinkedIn posts in this project were manually collected directly from each expert's LinkedIn profile.

---

## 4. Version Control Workflow

This project follows a simple trunk-based workflow:

1. All work is committed to the `main` branch.

2. Each logical unit of work (adding an expert, collecting a transcript, updating sources) is a separate commit with a descriptive message.

3. Commit messages follow the format: `Add <expert name> LinkedIn posts and YouTube transcript`.

4. The `research/sources.md` table is updated whenever new content is collected.

5. Sensitive values (API keys) are never committed — `.gitignore` excludes `.env` files.

---

## 5. Tools Used

| Tool | Purpose |

|------|---------|

| Python 3 | Scripting for transcript fetching and content organisation |

| youtube-transcript-api | Automated YouTube transcript extraction |

| YouTube Data API v3 | Video metadata retrieval (title, ID, channel) |

| Supadata API | Initial transcript attempt (returned empty responses) |

| Cursor IDE | Development environment |

| Claude Code | AI-assisted code generation and documentation |

| Codex CLI | AI-assisted code suggestions |

| Git & GitHub | Version control and portfolio presentation |