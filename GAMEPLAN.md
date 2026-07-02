# Sabi's Game Plan — The Path to Immortality (AI Engineer from True Zero)

Last updated: 2026-07-02 · Pace: 1–2 hrs/day · Realistic horizon: 9–12 months to ascension (job-ready)

## The Cultivation System

Learning is cultivation: a mortal gathers qi daily, refines techniques until flawless, survives tribulations, and breaks through realms. No skipped foundations — cultivators with unstable cores explode at higher realms (so do engineers).

- **Qi** = XP. Every session gathers qi. 100 qi = one realm breakthrough.
- **Realms**: Mortal → Qi Condensation → Foundation Establishment → Core Formation → Nascent Soul → Soul Transformation → Void Refinement → Body Integration → Grand Ascension → True Immortal (Hired).
- **Tribulations** = weekly boss fights. Survive = 🏆 + bonus qi. Fail = retry after more refinement; no shame, all cultivators fail tribulations.
- **Techniques** = badges/skills mastered. A technique isn't yours until you can explain it back.
- **Cliffhangers**: every session ends with a fragment of mysterious code or an unanswered question — the next session's revelation.
- **Magic first**: each week opens with a demonstration of "high-realm power" (an impressive result in few lines) that the week's training earns the understanding of.
- **Rivalry mode**: Claude sets bars ("most disciples need 3 attempts"); Sabi beats them.

## The Grand Artifact: your own Cultivation RPG

Sabi once wanted to build a gaming universe. So the Phase F project thread IS one: a text-based cultivation RPG, built incrementally as each concept is learned — variables (character sheet) → conditionals (breakthrough checks) → loops (training cycles) → dicts (inventory & technique scrolls) → functions (combat system) → files (save games). By end of F.1: playable, on GitHub, every line understood. Money/investing side quests arrive in P1–P2 with real APIs and data.

## The deal (how tutoring works)

1. One idea per session. You predict before you run. You build before you move on. You explain it back in your own words.
2. Claude never hands you finished code for something you're learning. Stuck → you get a question, not an answer.
3. Every session ends with something that runs. Every phase ends with something on GitHub. Every ⭐ phase ends with something LIVE on the internet + a CV/LinkedIn update.
4. Miss a day? Fine. Miss two? We do a 20-minute minimum session to keep the streak alive. Streaks are logged below.
5. Weekly boss fight (Fridays or last session of the week): a challenge combining everything that week, no notes.

## Recalibrated timeline (10 hrs/week)

| Block | Weeks | What | Hirable artifact |
|---|---|---|---|
| F.1 Python from zero | 1–5 | Feedback loop, variables, strings, lists/dicts, conditionals, loops, functions, files | Word-counter CLI you can explain line by line (GitHub repo #1) |
| F.2 How machines learn from text | 6–8 | Data/labels, bag-of-words, train vs predict | Rebuilt sentiment classifier, understood fully (repo #2) |
| P0 Real engineer habits | 9–10 | venvs, git branches/PRs, tests, project structure | custom-text-classifier refactored into a real package |
| P1 LLM APIs | 11–13 | Claude/GPT SDKs, streaming, structured output, tool calling, retries | Multi-provider LLM client (repo #3) |
| P2 RAG ⭐ | 14–18 | Embeddings, vector DBs, chunking, retrieval quality | **"Chat with your docs" — LIVE URL** + CV/LinkedIn update #1 |
| P3 Evals ⭐ (your edge) | 19–21 | Golden datasets, RAGAS, LLM-as-judge, tracing | Eval suite + written "improved X from A to B" result + LinkedIn post |
| P4 Agents & MCP ⭐ | 22–26 | Agent loop, LangGraph, tools, MCP server | Research/ops agent (repo #4) + CV update #2 |
| P5 Deployment | 27–29 | FastAPI, Docker, cloud, monitoring | Best project deployed properly, auth + dashboard |
| P6 Fine-tuning | 30–33 | LoRA/QLoRA, quantization, when NOT to fine-tune | Fine-tuned SLM vs prompted baseline write-up |
| P7 Capstone + job hunt | 34–42 | Flagship product, portfolio polish, interview prep | Capstone LIVE, CV/LinkedIn final, applications out |

North star unchanged: small task-specific language models, shipped as software, improving in a loop (deploy → feedback → evals → re-fine-tune → ship).

## Career checkpoints (locked to phases, not dates)

- End of F.2 — GitHub profile cleaned, README on profile, 2 repos with honest READMEs
- End of P2 — first LIVE project; CV rewritten around it; LinkedIn headline → "Building AI-powered applications | Python · RAG · LLM APIs"
- End of P3 — LinkedIn post #1: your eval results (this is the differentiator recruiters don't see often)
- End of P4 — CV v2; start following 5 AI-engineer job postings weekly to track what's asked
- P7 — applications, referrals, interview prep

## Industry pulse (so we stay current)

- Monday ritual (20 min, counts as that day's session): skim TLDR AI or Latent Space; note 1 thing relevant to current phase in `notes/industry.md`
- Every phase start: Claude re-checks what job postings ask for and adjusts the phase

## Streak & XP log

Rules: ✅ = session done (≥20 min counts). Boss fight win = 🏆.

| Week | Mon | Tue | Wed | Thu | Fri | Sat | Sun | Boss fight |
|---|---|---|---|---|---|---|---|---|
| W1 (Jun 30–Jul 6) | – | – | · | · | · | · | · | pending |

XP: 0 · Current streak: 0 · Longest streak: 0

## F.1 week-by-week (current block)

- **W1: The feedback loop + variables.** Run code, read errors without fear, variables & types. Mini-build: mad-libs generator.
- **W2: Strings & lists.** Slicing, methods, loops over lists. Mini-build: password strength checker.
- **W3: Dicts + conditionals.** Mini-build: quiz game with score tracking.
- **W4: Loops + functions.** Mini-build: number-guessing game, then refactor quiz game into functions.
- **W5: Files + checkpoint.** Read real text files. **Boss project: word-counter CLI** — counts words in any text file, top-10 most frequent, you explain every line. Push to GitHub with README.
