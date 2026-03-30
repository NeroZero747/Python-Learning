---
mode: agent
description: "Full lesson build — Phase 1 compiles a lesson brief from all section inputs upfront; Phase 2 builds each section sequentially using that brief."
promptFiles:
  - .github/prompts/lesson-sync-format.prompt.md
  - .github/prompts/lesson-objective.prompt.md
  - .github/prompts/lesson-hero.prompt.md
  - .github/prompts/lesson-overview.prompt.md
  - .github/prompts/lesson-key-takeaways.prompt.md
  - .github/prompts/lesson-key-concepts.prompt.md
  - .github/prompts/lesson-decision-flow.prompt.md
  - .github/prompts/lesson-code-examples.prompt.md
  - .github/prompts/lesson-comparison.prompt.md
  - .github/prompts/lesson-practice-exercises.prompt.md
  - .github/prompts/lesson-common-mistakes.prompt.md
  - .github/prompts/lesson-real-world.prompt.md
  - .github/prompts/lesson-recap.prompt.md
  - .github/prompts/lesson-knowledge-check.prompt.md
  - .github/prompts/lesson-next-lesson.prompt.md
---

## Required Inputs

| Variable | Value |
|---|---|
| `TARGET_FILE` | Absolute path to the lesson HTML file |
| `LESSON_TOPIC` | The lesson topic in plain English (e.g. `functions`, `loops`, `variables`) |

---

## Phase 1 — Lesson Brief

**Complete this phase in full before writing any HTML.**

Read `TARGET_FILE` once to understand the existing structure. Then read any relevant reference docs about the lesson topic. Produce the Lesson Brief below — a single structured planning document covering every input required by every section prompt.

Output the brief as a code block so it is easy to scan:

```
LESSON BRIEF
============
TARGET_FILE: ...
TOPIC: ...
MODULE: ...   LESSON NUM: ...   DIFFICULTY: Beginner / Intermediate / Advanced
PUB_DATE: ...

── SECTION PLAN ──────────────────────────────────────────

[0] sync-format      → no content inputs; run first, fixes CSS/format only
[1] objective        → 4 goal cards (define FIRST — recap + quiz reference these verbatim)
[2] hero             → derives GOALS_COUNT=4, EXAMPLES_COUNT, EXERCISES_COUNT from objectives
[3] overview         → hook sentence + analogy; list topics covered here (key-takeaways must not repeat)
[4] key-takeaways    → 3 cards; each covers NEW ground not in overview
[5] key-concepts     → 1 sidebar tab per major syntax element / type
[6] decision-flow    → CONDITIONAL — include if topic has branching/looping/flow control logic;
                        skip if topic is purely declarative (e.g. imports, print statements, data types)
[7] code-examples    → 3 tabs with descriptive labels; confirm EXAMPLES_COUNT here
[8] comparison       → Python vs SQL vs Excel; 2–4 concept rows
[9] practice         → 3 exercises; confirm EXERCISES_COUNT here
[10] common-mistakes → 3 mistakes; lead with the exact error
[11] real-world      → 3 scenario cards + before/after table; no code blocks
[12] recap           → 2×2 grid; MUST use identical labels + icons to #objective cards
[13] knowledge-check → 4 True/False questions; one per objective
[14] next-lesson     → lesson badge + 3 preview cards + bottom nav

── OBJECTIVE CARDS (defined here, copied verbatim into recap + quiz) ──

GOAL_1_LABEL: ...   GOAL_1_ICON: fa6-solid:...
GOAL_2_LABEL: ...   GOAL_2_ICON: fa6-solid:...
GOAL_3_LABEL: ...   GOAL_3_ICON: fa6-solid:...
GOAL_4_LABEL: ...   GOAL_4_ICON: fa6-solid:...

── INTER-SECTION DEPENDENCIES ─────────────────────────────

DECISION-FLOW: include / skip
  Reason: ...

OVERVIEW ANALOGY DOMAIN: ...
OVERVIEW TOPICS COVERED (key-takeaways must NOT touch these): ...

EXAMPLES_COUNT (code-examples tabs → hero pill): ...
EXERCISES_COUNT (practice tabs → hero pill): ...

── HERO VARIABLES ─────────────────────────────────────────
(Fill these in Phase 1 so Phase 2 can use them without guessing)

LESSON_TITLE: ...            ← exact title as it appears in the <h1>
LESSON_NUM_LABEL: ...        ← zero-padded: "Lesson 01", "Lesson 02", etc.
SUBTITLE: ...                ← 15–25 words; starts with action word; beginner-safe
MODULE_ICON: fa6-solid:...  ← rocket=mod1, cubes=mod2, diagram-project=mod3, star=mod4+
READ_TIME: ...               ← e.g. "15 min read"; estimate from section count
LESSON_POSITION: ...         ← this lesson's number within the module (e.g. 3)
TOTAL_LESSONS: ...           ← total lessons in the module (e.g. 5)

── NEXT LESSON INFO ───────────────────────────────────────

NEXT_LESSON_NUM: ...
NEXT_LESSON_TITLE: ...
NEXT_LESSON_FILE: ...
PREV_LESSON_FILE: ...   (NONE if first lesson of module)
PREV_LESSON_TITLE: ...
```

Do not proceed to Phase 2 until this brief is complete.

---

## Phase 2 — Build Each Section

Apply the full instructions from each section's loaded prompt file, working through sections **in the order shown in the brief**, one at a time. Complete each section fully — write and save the HTML — before moving to the next.

### Rules for every section

1. **One section at a time.** Do not start the next section until the current one is written and saved to `TARGET_FILE`.

2. **Use the brief for values, use the sub-prompt for structure.** Before writing each section, re-read the full instructions from that section's loaded prompt file — the focus checklist below is a reminder only, not a substitute. The sub-prompt contains the exact HTML template, quality checklist, and content rules that define what the output must look like. Follow the sub-prompt template verbatim; use the brief for the content values (labels, numbers, icons).

   Only read the specific `<section id="...">` block in `TARGET_FILE` that you are about to replace — do not re-read the whole file.

3. **Carry forward these values explicitly** — state them in a one-line note after saving each section:

   | After writing… | Carry forward… | Used by… |
   |---|---|---|
   | `#objective` | Exact card labels + icons (copy from brief) | `#recap`, `#knowledge-check` |
   | `#overview` | List of topics covered + analogy domain | `#key-takeaways` (must not repeat) |
   | `#code-examples` | Actual tab count → EXAMPLES_COUNT | `#hero` stat pill |
   | `#practice` | Actual tab count → EXERCISES_COUNT | `#hero` stat pill |

   Build `#hero` **after** `#code-examples` and `#practice` so the stat counts are confirmed.

4. **Decision-flow gate:** If the brief says `skip`, do not run the `lesson-decision-flow` prompt. If `include`, run it after `#key-concepts`.

5. **Focus checklist — these are reminders of the most critical constraint per section. They do NOT replace reading the full sub-prompt template before writing each section:**

   **Code block style quick reference** (full spec in `copilot-instructions.md` § Code Block Styles):

   | Section | Style to use |
   |---|---|
   | `#code-examples` | Style A — dark chrome, `border border-gray-800 shadow-lg`, with terminal pane |
   | `#decision-flow` | Style A — dark chrome, **no** terminal pane |
   | `#practice` | Style A — dark chrome, **no** terminal pane |
   | `#key-concepts` | Style B — `bg-code shadow-md` + `border-b border-code-sep`, language label |
   | `#comparison` | Style B + `flex flex-col flex-1` on outer div |
   | `#mistakes` split panels | Style B-lite — bare `bg-code`, `px-4 py-3` on `<pre>`, no header |
   | `#mistakes` single-column | Style B |

   Never use `bg-gray-800` or traffic-light dots (`w-2.5 h-2.5 rounded-full`) in any code block.

   - **sync-format** → strip HTML shell tags; sync style block; confirm `id="hub-root"`; apply hover fix
   - **objective** → 4 goal cards; unique Fa6 icon per card; one-sentence concrete description; amber tip
   - **hero** → all locked elements verbatim; only update text, lesson number, date, stat counts
   - **overview** → 4-part: hook banner → "Think of…" analogy intro → 2-col card grid → amber tip
   - **key-takeaways** → 3 cards (pink / violet / blue); each deepens understanding, never restates overview
   - **key-concepts** → sidebar tabs; define the concept BEFORE showing code; widget + code + color tip per tab
   - **decision-flow** → 4 flowchart nodes + 3 concept cards; match the topic's actual flow logic
   - **code-examples** → 3 tabs with descriptive pill labels; every code line has an inline comment
   - **comparison** → Python / SQL / Excel columns; 2–4 concept rows; side-by-side code blocks
   - **practice** → 3 exercises; task description must be clear enough to act on without re-reading
   - **common-mistakes** → 3 mistakes; lead with the exact error type or what breaks; wrong then correct code
   - **real-world** → 3 scenario cards + before/after table; no code blocks; human-scale numbers
   - **recap** → 2×2 grid; labels + icons MUST match #objective exactly; short action-verb sentences (8–14 words)
   - **knowledge-check** → 4 True/False questions (one per objective); reinforce, never trick; mix true + false answers
   - **next-lesson** → lesson badge + 3 preview cards + bottom nav; omit Previous link if first lesson of module

---

## Phase 3 — Quality Gate

After all sections are saved, run this checklist against `TARGET_FILE`:

- [ ] All 4 objective card labels appear **verbatim** in both `#recap` and `#knowledge-check`
- [ ] `#key-takeaways` has zero topics that overlap with the overview topics listed in the brief
- [ ] `#decision-flow` is either fully present (4 flow nodes + 3 concept cards) or fully absent — never partial
- [ ] Hero stat pills (`EXAMPLES_COUNT`, `EXERCISES_COUNT`) match the actual tab count in `#code-examples` and `#practice`
- [ ] All JS tab switcher functions (`switchCeTab`, `switchMkTab`, `switchPeTab`, `switchQzTab`, `switchKcTab`) call the correct number of panels
- [ ] `mod-lesson-active` class is on the current lesson's `<a>` in the module TOC sidebar
- [ ] No `<!DOCTYPE>`, `<html>`, `<head>`, or `<body>` tags anywhere in the file
