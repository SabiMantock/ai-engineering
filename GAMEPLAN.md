# Sabi's Game Plan — AI Engineer, Building on Existing Work

Last updated: 2026-07-19 · Pace: 1–2 hrs/day

## PIVOT (2026-07-19): back to the tutorial-era work

Phase F (Python from zero) and the Gauntlet (JS problem-solving) are removed from the active plan — full history kept in "Archived tracks" at the bottom, nothing deleted from disk (the RPG files, foundations notebooks, etc. all still exist in the repo). New starting point: the pre-existing notebooks in `custom-text-classifier/`, `nlp/`, and `llms/` (the "tutorial-era" work), with the same rule that governed everything before: **nothing advances until you can explain it back in your own words.** Predict-before-run and explain-back stay in force — only the subject matter changes, from fundamentals to what's already built.

Known trade-off, flagged and accepted: these notebooks use loops, functions, classes, imports, and library data structures that Phase F would have built up to. Expect to stop mid-notebook sometimes to learn a fundamental on demand, reactively rather than in order.

**The path:**

1. `custom-text-classifier/` — smallest, most self-contained (has its own `src/`, `tests/`, `data/`). Entry point.
2. `nlp/` notebooks — classical NLP, ~15 notebooks (tokenization, TF-IDF, LDA, POS/NER, sentiment).
3. `llms/` — BERT Q&A, XLNet classification, fine-tuning.
4. `langchain/` branch — prompt templates, few-shot, chains.
5. Rejoin the main AI-engineer roadmap below at whichever phase the skills land you (likely P1/P2 — LLM APIs and RAG).

## The deal (how tutoring works)

1. One idea per session. You predict before you run. You build before you move on. You explain it back in your own words.
1b. **Every session opens with a recap** — quick-fire recall questions on prior material, answered from memory (no notes, no running code). Spaced recall is how techniques become permanent.
1c. **Every session closes with a journal entry** in `journal/log.md` — what was learned, what broke, what surprised. Distilled into blog posts (LinkedIn + Medium/dev.to) at each week's end. Learning in public is part of the job hunt.
2. Claude never hands you finished code for something you're learning. Stuck → you get a question, not an answer.
3. Every session ends with something that runs. Every phase ends with something on GitHub. Every ⭐ phase ends with something LIVE on the internet + a CV/LinkedIn update.
4. Miss a day? Fine. Miss two? We do a 20-minute minimum session to keep the streak alive. Streaks are logged below.
5. Weekly boss fight (Fridays or last session of the week): a challenge combining everything that week, no notes.

## Timeline from here (10 hrs/week)

| Block | What | Hirable artifact |
|---|---|---|
| Tutorial-era deep dive | Rebuild real understanding of custom-text-classifier → nlp/ → llms/ → langchain/, line by line | Each notebook re-explained in your own words; refactor custom-text-classifier into a tested package |
| P0 Real engineer habits | venvs, git branches/PRs, tests, project structure | custom-text-classifier as a real installable package |
| P1 LLM APIs | Claude/GPT SDKs, streaming, structured output, tool calling, retries; context engineering; sampling params | Multi-provider LLM client (repo) |
| P2 RAG ⭐ | Embeddings, vector DBs, chunking, retrieval quality | **"Chat with your docs" — LIVE URL** + CV/LinkedIn update #1 |
| P3 Evals ⭐ (your edge) | Golden datasets, RAGAS + DeepEval, LLM-as-judge, tracing; AI safety basics | Eval suite + written "improved X from A to B" result + LinkedIn post |
| P4 Agents & MCP ⭐ | Agent loop, LangGraph, tools, MCP server & client; guardrails | Research/ops agent (repo) + CV update #2 |
| P4.5 Multimodal (side quest) | Vision APIs, Whisper, image generation | Small demo folded into agent or capstone |
| P5 Deployment | FastAPI, Docker, cloud, monitoring | Best project deployed properly, auth + dashboard |
| P6 Fine-tuning | LoRA/QLoRA, quantization, when NOT to fine-tune | Fine-tuned SLM vs prompted baseline write-up |
| P7 Capstone + job hunt | Flagship product, portfolio polish, interview prep | Capstone LIVE, CV/LinkedIn final, applications out |

North star unchanged: small task-specific language models, shipped as software, improving in a loop (deploy → feedback → evals → re-fine-tune → ship).

## Cross-checked against roadmap.sh/ai-engineer (2026-07-12)

Their structure validated ours: LLM APIs → embeddings/vector DBs → RAG → agents/MCP → evals/observability → fine-tuning. Adopted from them: explicit context engineering (P1), AI safety/guardrails (P3/P4), multimodal side quest (P4.5), sampling parameters (P1), MCP client as well as server (P4). Their prerequisite — frontend/backend — Sabi already holds as a JS developer.

## Career checkpoints (locked to phases, not dates)

- End of tutorial-era dive — GitHub profile cleaned, README on profile, notebooks re-explained honestly
- End of P2 — first LIVE project; CV rewritten around it; LinkedIn headline → "Building AI-powered applications | Python · RAG · LLM APIs"
- End of P3 — LinkedIn post: your eval results (this is the differentiator recruiters don't see often)
- End of P4 — CV v2; start following 5 AI-engineer job postings weekly to track what's asked
- P7 — applications, referrals, interview prep

## Industry pulse (so we stay current)

- Monday ritual (20 min, counts as that day's session): skim TLDR AI or Latent Space; note 1 thing relevant to current phase in `notes/industry.md`
- Every phase start: Claude re-checks what job postings ask for and adjusts the phase

## Streak & XP log

Rules: ✅ = session done (≥20 min counts). Boss fight win = 🏆.

Dashboard.html removed (2026-07-19) — visual tracker dropped, this markdown log is now the only progress record. XP so far: 65 (carried over from Phase F work — real understanding earned, kept). Current streak: 0. Longest streak: 3.

## Archived tracks (paused, not deleted — files remain in repo)

### Phase F — Python from zero (Sessions 1–3 complete, 65 qi earned)

Covered: the parse/run phase distinction, syntax vs runtime errors, variables & assignment, string indexing/slicing, f-strings, type strictness (`"10" + 5` → TypeError). Built: `foundations/hello.py`, `foundations/rpg.py` (character sheet + technique forge). Full detail in `journal/log.md`. Session 4 (lists) was queued but never run.

### The Cultivation System (gamification layer used during Phase F)

Qi = XP, realms = levels (Mortal → ... → True Immortal/Hired), tribulations = boss fights, cliffhangers, rivalry-mode prediction quizzes. Can be revived for any future track if it's still motivating — just ask.

### The Grand Artifact — Cultivation RPG

Text-based RPG built incrementally per Python concept learned. Parked mid-build (`foundations/rpg.py`). Can be resumed as a side project any time — the code is still there.

### The Gauntlet — JS problem-solving (started 2026-07-12, diagnostic in progress)

Trigger: failed technical interviews traced to no decomposition method, only recall. Method: restate → solve by hand → plan in words → code → post-mortem. Was mid-diagnostic (the "Keyhole Drill" on scanning arrays one element at a time) when the pivot happened. If interview pressure returns, this resumes exactly where it left off.
