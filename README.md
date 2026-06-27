# AI Tools Onboarding

## Tools Installed
- Cursor IDE
- Claude Code CLI (Anthropic)
- Codex CLI (OpenAI)
- Git / GitHub

## Steps Completed
1. Installed Cursor IDE
2. Created a public GitHub repository and cloned it locally
3. Installed Claude Code via PowerShell (`irm https://claude.ai/install.ps1 | iex`) and logged in with a Claude account
4. Installed Codex CLI via npm and logged in with a ChatGPT account
5. Verified both tools were authenticated using `claude` and `codex login status`
6. Documented the process in this README
7. Committed and pushed changes to GitHub

## Issues Encountered
- Claude Code and Codex are not regular Cursor "Extensions" — they had to be installed and run via the terminal (PowerShell/npm) rather than through the Extensions or Plugins marketplace.
- The first Codex login attempt timed out before browser authentication completed; retried `codex login` and it succeeded.

## Notes
This repository was completed as a portfolio/screening task as part of a hiring process.