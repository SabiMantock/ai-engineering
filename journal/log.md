# Journey Log — raw material for blog posts

One entry per session. Captured while fresh: what I learned, what broke, what surprised me. Distilled into posts periodically.

---

## Session 1 — 2026-07-01/02 · The feedback loop (~45 min)

- First program: 3 print lines. Then broke it on purpose (deleted a quote).
- **Surprise:** put the broken line LAST and the working lines still didn't run. I assumed Python executed top-to-bottom like a script — turns out it READS the whole file first (parse phase), then runs it. A syntax error means nothing runs at all.
- `print(1/0)` proved the other side: grammatically fine, crashes mid-run. Lines above it DO print.
- Mental model corrected: syntax error = caught while reading. Runtime error = caught while running.
- Coming from JavaScript assumptions and being wrong was the best part.

## Session 2 — 2026-07-02 · Variables (~90 min)

- `qi = qi + 10` looked like impossible math. It's not math — `=` assigns. Read right-to-left: compute right side, store under the name.
- Prediction quiz 2/3. The miss: I predicted `"10" + 5` → `"105"` (JavaScript brain again). Python threw TypeError instead — it never looks INSIDE a string, it only cares about types. `"10"` and `"abc"` fail identically.
- Discovered f-strings, used them before being taught — then had to prove I understood them (what happens without the `f`: prints `{qi}` literally).
- Built: my RPG character sheet (name, realm, qi, technique, spirit stones), with reassignment for a training day.
- Habit learned: dead variables are clutter. Every name must earn its place.

## Session 3 — 2026-07-03 · Strings (~60 min)

- Recap quiz 5/5 (recaps before every session now — retrieval, not re-reading).
- Strings are sequences: indexing from 0, negatives from the end, `len()`.
- Slicing rule, finally precise: **start included, end excluded.** Got `[6:10]` wrong by ignoring the end bound; got `[-5:]` wrong by missing the colon. Both misses taught more than the hits.
- `scroll[17]` on a 17-char string = IndexError (runtime — parser can't know lengths).
- Built: technique forge — `.title()`, `.upper()`, `.replace()`, indexing for a sigil. "Dark Fire Palm" / "DARK-FIRE-PALM!!!" / "D.F.P"
- Mentor called me out: I kept answering conceptual questions with code. New rule — words questions get word answers. Interviews don't have keyboards.

<!-- Next entry: Session 4 — lists -->
