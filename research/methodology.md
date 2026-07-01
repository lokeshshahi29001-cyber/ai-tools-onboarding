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
- **Diversity** — The expert list should represent a range of company sizes, geographies, and roles (founders, CMOs, content strategists).

---

## 2. Transcript Collection — Supadata API

YouTube transcripts are collected using the [Supadata API](https://supadata.ai).

**Process:**

1. Identify a relevant YouTube video by the selected expert.
2. Copy the full video URL.
3. Run `scripts/fetch_transcripts.py` with the URL and expert name as arguments:
   ```
   python scripts/fetch_transcripts.py "<youtube_url>" "<expert_name>"
   ```
4. The script extracts the video ID, calls the Supadata `/v1/youtube/transcript` endpoint with the API key, and saves the response as a `.md` file in `research/youtube-transcripts/`.
5. The saved file includes the video title, source URL, date collected, and full transcript text.

**API key management:**  
The `SUPADATA_API_KEY` variable is defined at the top of `scripts/fetch_transcripts.py`. The key itself is never committed to Git — it should be replaced locally or loaded from a `.env` file (excluded via `.gitignore`).

---

## 3. LinkedIn Content Organisation

LinkedIn posts are saved using `scripts/organize_linkedin.py`.

**Process:**

1. Identify a post by a selected expert on LinkedIn.
2. Copy the post text.
3. Run the script with the expert name, post date, and post content:
   ```
   python scripts/organize_linkedin.py "<expert_name>" "<YYYY-MM-DD>" "<post_content>"
   ```
4. The script generates a `.md` file in `research/linkedin-posts/` using a standard template: Expert, Date, Source, Summary, Key Takeaways, and Original Post Content.
5. The Summary and Key Takeaways sections are filled in manually after reviewing the post.

---

## 4. Version Control Workflow

This project follows a simple trunk-based workflow:

1. All work is committed to the `main` branch.
2. Each logical unit of work (adding an expert, collecting a transcript, updating sources) is a separate commit with a descriptive message.
3. Commit messages follow the format: `<action>: <short description>` (e.g., `add: transcript for Jane Doe — LinkedIn strategy video`).
4. The `research/sources.md` table is updated whenever new content is collected.
5. Sensitive values (API keys) are never committed — `.gitignore` excludes `.env` files.
