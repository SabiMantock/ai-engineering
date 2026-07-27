# Post #1 — draft (publish at end of Week 1, after the boss fight)

---

## LinkedIn version (short)

I'm a JavaScript developer. I also have folders full of Python NLP notebooks — fine-tuned BERT models, LangChain experiments — all built by following tutorials on my way toward AI engineering.

This week I admitted something uncomfortable: I couldn't explain most of that Python line by line. It ran, but it wasn't *mine*.

So I restarted Python from zero. Not "watch another tutorial" zero — actual zero. Three lines of print statements, run from a terminal.

Day 1, I broke my own code on purpose and learned Python reads your ENTIRE file before running any of it.

Day 2, my JavaScript instincts predicted "10" + 5 would give "105". Python threw a TypeError instead. Turns out my new language has stricter standards than my old one — and that one error taught me more about Python's type system than a month of tutorials.

Day 3, I got string slicing wrong twice, and the wrong answers taught me more than the right ones.

The method: predict before you run, build before you move on, explain it back in your own words. No copy-paste. An AI mentor that answers my questions with questions.

The goal: AI engineer, on foundations that are actually mine. Documenting the whole path — misses included, because that's where the learning lives.

Day 3. Streak intact. More soon.

#learninpublic #python #javascript #aiengineering

---

## Medium/dev.to version (long)

# I'm a JavaScript Developer with Fine-Tuned BERT Models. I Restarted Python from Print Statements.

**Why I threw out my tutorial-built AI knowledge and started from absolute zero — and what three days of real fundamentals taught me.**

There's a specific kind of shame in having a GitHub full of machine learning notebooks you can't explain. I'm a JavaScript developer by background, and somewhere along the way toward "AI engineer" I accumulated a pile of Python: tokenization pipelines, fine-tuned transformers, LangChain chains. All of it assembled from tutorials, adjusted until the errors went away.

It ran. But ask me what any of it did line by line, and I'd have talked around the question. I had tutorial Python, not *my* Python.

This week I stopped pretending. New branch, empty folder, one rule: nothing advances until I can explain it back in my own words.

### Day 1: The thing tutorials never taught me

My first exercise was three print statements. Then my mentor had me break the file on purpose — delete a closing quote — and predict what would happen. Easy, I thought: the lines before the broken one run, the rest don't. Scripts run top to bottom, right?

Wrong. I moved the broken line to the END of the file and *nothing* printed. The perfectly valid lines above it never ran.

Python reads your entire file before running any of it. A syntax error is caught in that reading phase, before a single line executes. A runtime error — like `1/0` — is different: grammatically fine, so the file runs and crashes mid-execution, output of earlier lines already on screen.

All those notebooks, and I didn't know this.

### Day 2: JavaScript instincts meet a language that refuses to guess

Prediction quiz: what does `"10" + 5` produce? My JS brain answered instantly: `"105"`. That's what JavaScript does — it guesses what you meant and glues them together.

Python threw a `TypeError` instead. It doesn't peek inside strings and "notice" digits — `"10"` and `"abc"` fail identically, because Python judges the type of the box, never its contents. Want the math? Say so explicitly: `int("10") + 5`.

That's the personality difference between my old language and my new one: JavaScript guesses, Python makes you say what you mean. Coming from JS, being wrong like this is the fastest way to learn where the languages actually differ.

I scored 2/3 on that quiz. The miss was worth more than both hits.

### Day 3: Wrong twice about slicing, better for it

`scroll[6:10]` — I read it as "from 6 to 10" and included too much. The rule, precisely: **start is included, end is excluded.** Then `scroll[-5:]` — I missed the colon entirely and answered with one character instead of five.

My mentor also caught me doing something sneaky: answering conceptual questions with code snippets. New rule — concept questions get answered in words. Interviews don't come with keyboards.

### The method

What's different this time isn't effort. It's structure:

**Predict before running.** Committing to a prediction makes being wrong informative. Passive tutorial-following never exposed my broken mental models; predictions do — especially the JavaScript-shaped ones.

**Build immediately.** Every concept goes straight into a project (I'm building a text-based RPG — variables became the character sheet, string methods became a technique-name forge).

**Explain it back.** If I can't say it in my own words, I don't own it.

**Track it visibly.** A progress dashboard with streaks and XP. Day 3, streak intact.

### Where this goes

The destination is AI engineering — RAG systems, agents, evaluation pipelines. My old notebooks will get revisited eventually, and this time I'll be able to read them like plain English.

I'm documenting the whole path, misses included. If you're a developer whose "AI knowledge" is a tower of tutorials balanced on sand — you're who I'm writing for.

*Day 3 of ~300. Follow along.*
