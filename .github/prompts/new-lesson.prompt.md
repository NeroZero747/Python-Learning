---
mode: agent
description: Build a new lesson HTML file by writing and running a Python generator script that imports from scripts/lesson_builder.py
---

## Inputs

- **Source markdown:** `${input:sourceFile}`
- **Output HTML path:** `${input:outputFile}`
- **Module label:** `${input:moduleLabel}`  (e.g. `Module 2`)
- **Module full label:** `${input:moduleFullLabel}`  (e.g. `Module 2 · Lesson 2`)
- **Lesson number badge:** `${input:lessonNumber}`  (digit(s) shown in the hero, e.g. `02`)
- **Lesson title:** `${input:lessonTitle}`
- **Lesson subtitle:** `${input:lessonSubtitle}`  (one sentence shown under the hero title)
- **Difficulty:** `${input:difficulty}`  (`Beginner` / `Intermediate` / `Advanced`)
- **Progress:** `${input:progress}`  (e.g. `2/9` for lesson 2 of 9)
- **Previous lesson filename:** `${input:prevLesson}`  (`none` if first lesson of module)
- **Previous lesson title:** `${input:prevTitle}`  (`none` if first lesson)
- **Next lesson filename:** `${input:nextLesson}`  (`none` if last lesson of module)
- **Next lesson title:** `${input:nextTitle}`  (`none` if last lesson)

---

## How this works — use the pre-built builder module

`scripts/lesson_builder.py` already exists. It extracts the full CSS, JavaScript,
hero SVG, and structural chrome from `docs/new_lesson_template.html` at runtime —
**you must NOT copy-paste or reproduce the CSS/JS/SVG yourself** — the builder
handles all of that. Your only job is to write the lesson content HTML.

### Step 1 — Read the source markdown

Read `${input:sourceFile}` in full to gather:
- Lesson objectives (4 items)
- Overview concept and analogy
- 3 key ideas with keyword pills
- Key concepts (up to 5)
- 3 code examples with Python code
- 3 common mistakes with before/after code
- 3 practice exercises
- Real-world application examples
- 4 recap items
- 3 quiz questions (True/False or multiple choice)
- Next-lesson preview items

### Step 2 — Write `scripts/_gen_lesson.py`

Create the file. It must follow this exact skeleton — **do not deviate**:

```python
"""Generator for ${input:outputFile}"""
import sys
from pathlib import Path

# Make the builder importable when run from project root
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.lesson_builder import (
    cdn_head, style_block, fixed_chrome, hub_root_open, hub_root_close,
    build_hero, layout_open, layout_close, build_toc, main_open, main_close,
    section_wrap, section_header, code_block, pill_tabs, bottom_nav,
    script_block, write_lesson,
)

OUTPUT = Path("${input:outputFile}")

# ── Hero ──────────────────────────────────────────────────────────────────────
hero = build_hero(
    lesson_num="${input:lessonNumber}",
    title="${input:lessonTitle}",
    subtitle="${input:lessonSubtitle}",
    module_label="${input:moduleLabel}",
    difficulty="${input:difficulty}",
    n_goals=4, n_examples=3, n_exercises=3,
    progress="${input:progress}",
)

# ── TOC sidebar ───────────────────────────────────────────────────────────────
toc_items = [
    ("#objective",       "fa6-solid:bullseye",           "Lesson Objective"),
    ("#overview",        "fa6-solid:binoculars",         "Overview"),
    ("#key-ideas",       "fa6-solid:lightbulb",          "Key Takeaways"),
    ("#key-concepts",    "fa6-solid:book-open",          "Key Concepts"),
    ("#code-examples",   "fa6-solid:code",               "Code Examples"),
    ("#common-mistakes", "fa6-solid:triangle-exclamation","Common Mistakes"),
    ("#practice",        "fa6-solid:pencil",             "Practice Exercises"),
    ("#real-world",      "fa6-solid:briefcase",          "Real-World Use"),
    ("#recap",           "fa6-solid:list-check",         "Lesson Recap"),
    ("#knowledge-check", "fa6-solid:brain",              "Knowledge Check"),
    ("#next-lesson",     "fa6-solid:circle-arrow-right", "Next Lesson"),
]
module_lessons = [
    # (href, display_label) — list ALL lessons in the module
    ("lesson01_FILENAME.html", "1. Lesson One Title"),
    ("lesson02_FILENAME.html", "2. Lesson Two Title"),
    # … add remaining lessons …
]
toc = build_toc(toc_items, module_lessons, current_lesson_idx=1)  # 0-based

# ── Content sections — write HTML for each one ────────────────────────────────

# 1. Objective
obj_html = section_wrap("objective",
    section_header("fa6-solid:bullseye", "Lesson Objective",
                   "The goal and expected outcome of this lesson"),
    """
    <!-- 4 obj-card items in a 2-column grid, then amber tip box -->
    <!-- WRITE FULL SECTION HTML HERE following copilot-instructions.md -->
    """,
)

# 2. Overview  (hook quote → analogy paragraph → card grid → amber tip)
overview_html = section_wrap("overview",
    section_header("fa6-solid:binoculars", "Overview", "A high-level summary"),
    """<!-- WRITE FULL SECTION HTML HERE -->""",
)

# 3. Key Ideas  (brand-pink, violet, blue gradient cards + keyword pills)
key_ideas_html = section_wrap("key-ideas",
    section_header("fa6-solid:lightbulb", "Key Takeaways", "The most important concepts"),
    """<!-- WRITE FULL SECTION HTML HERE -->""",
)

# 4. Key Concepts  (kc-tab sidebar tabs, up to 5)
key_concepts_html = section_wrap("key-concepts",
    section_header("fa6-solid:book-open", "Key Concepts", "Detailed concept explanations"),
    """<!-- WRITE FULL SECTION HTML HERE -->""",
)

# 5. Code Examples  (ce-step pill tabs + Prism code blocks + copy buttons)
code_examples_html = section_wrap("code-examples",
    section_header("fa6-solid:code", "Code Examples", "Practical demonstrations"),
    """<!-- WRITE FULL SECTION HTML HERE -->""",
)

# 6. Common Mistakes  (mk-step pill tabs, minimum 3)
mistakes_html = section_wrap("common-mistakes",
    section_header("fa6-solid:triangle-exclamation", "Common Mistakes",
                   "Errors beginners often make"),
    """<!-- WRITE FULL SECTION HTML HERE -->""",
)

# 7. Practice Exercises  (pe-step pill tabs with task boxes, 3 exercises)
practice_html = section_wrap("practice",
    section_header("fa6-solid:pencil", "Practice Exercises", "Try it yourself"),
    """<!-- WRITE FULL SECTION HTML HERE -->""",
)

# 8. Real-World Use
real_world_html = section_wrap("real-world",
    section_header("fa6-solid:briefcase", "Real-World Use",
                   "How this applies in professional work"),
    """<!-- WRITE FULL SECTION HTML HERE -->""",
)

# 9. Recap  (2×2 numbered grid + pink completion banner)
recap_html = section_wrap("recap",
    section_header("fa6-solid:list-check", "Lesson Recap", "What you have learned"),
    """<!-- WRITE FULL SECTION HTML HERE -->""",
)

# 10. Knowledge Check  (qz-step pill tabs + Q1/Q2/Q3 watermark panels)
quiz_html = section_wrap("knowledge-check",
    section_header("fa6-solid:brain", "Knowledge Check", "Test your understanding"),
    """<!-- WRITE FULL SECTION HTML HERE -->""",
)

# 11. Next Lesson  (lesson badge + 3-card preview grid)
next_lesson_html = section_wrap("next-lesson",
    section_header("fa6-solid:circle-arrow-right", "Next Lesson", "Preview of what comes next"),
    """<!-- WRITE FULL SECTION HTML HERE -->""",
)

# 12. Bottom navigation
nav_html = bottom_nav(
    prev_filename="${input:prevLesson}",
    prev_title="${input:prevTitle}",
    next_filename="${input:nextLesson}",
    next_title="${input:nextTitle}",
)

# ── Assemble & write ──────────────────────────────────────────────────────────
write_lesson(OUTPUT, [
    cdn_head(),
    style_block(),
    fixed_chrome(),
    hub_root_open(),
    hero,
    layout_open(),
    toc,
    main_open(),
    obj_html,
    overview_html,
    key_ideas_html,
    key_concepts_html,
    code_examples_html,
    mistakes_html,
    practice_html,
    real_world_html,
    recap_html,
    quiz_html,
    next_lesson_html,
    nav_html,
    main_close(),
    layout_close(),
    hub_root_close(),
    script_block(),
])
```

Replace every `"""<!-- WRITE FULL SECTION HTML HERE -->"""` with full, correct
HTML following ALL rules in `.github/copilot-instructions.md`. The skeleton shows
*what* to write, not a placeholder to leave empty.

### Step 3 — Run the script

```
python3 scripts/_gen_lesson.py
```

Confirm the output file exists and contains valid HTML.

---

## Section content rules (enforced by copilot-instructions.md)

Follow ALL rules in `.github/copilot-instructions.md`. Key requirements per section:

1. **`#objective`** — 4 `obj-card` items (icon + bold title + one-line description) in a 2-column grid, closed with an amber `bg-amber-tip` box.
2. **`#overview`** — Hook quote card → "Think of…" analogy paragraph → 2-column analogy card grid (each card: bold title + *italic analogy subtitle* + plain-English description) → amber closing tip. Analogy domain must be consistent across all four parts.
3. **`#key-ideas`** — Brand-pink, violet, and blue gradient cards. Each has a top color bar, gradient icon, bold heading, full-sentence explanation, and keyword pills.
4. **`#key-concepts`** — `kc-tab` sidebar tabs with concept panels. Each panel has definition, example code, and usage notes.
5. **`#code-examples`** — `ce-step` pill tabs. Each panel has: brief intro, Prism code block with copy button, and output/explanation.
6. **`#common-mistakes`** — `mk-step` pill tabs (3 minimum). Each shows incorrect → correct code with explanation.
7. **`#practice`** — `pe-step` pill tabs with `task-box` callout, 3 exercises with solution code.
8. **`#real-world`** — Cards showing professional use cases with concrete Python examples.
9. **`#recap`** — 2×2 grid of numbered recap cards (watermarks 01–04) + pink "Lesson Complete!" banner.
10. **`#knowledge-check`** — `qz-step` pill tabs. Each panel has a `Q1`/`Q2`/`Q3` watermark header and True/False or multiple-choice buttons wired to `checkQuiz(this, bool)`.
11. **`#next-lesson`** — Lesson number badge, module label, 3-card "What You Will Learn" preview grid.
12. **Bottom nav** — `bottom_nav()` handles this automatically — just pass the filenames.

## Writing style rules

- All explanation text must be **complete sentences**. No terse bullet fragments.
- Define every new term in plain English **before** showing any code.
- Write in **second person** ("you", "your"). Encouraging, professional tone.
- **American English only.** Use American spellings throughout — e.g. "optimize" not "optimise", "color" not "colour", "analyze" not "analyse".

## Script quality rules

- Import only from `scripts.lesson_builder` — do not reproduce CSS, JS, or SVG inline.
- Use `python3 scripts/_gen_lesson.py` (macOS uses `python3`).
