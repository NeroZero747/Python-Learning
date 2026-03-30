---
mode: "agent"
description: "Write or rewrite the #knowledge-check section for a lesson HTML file — 4 True/False questions, one per lesson objective, with beginner-friendly language and mixed True/False answers. Difficulty level is adjustable via DIFFICULTY input."
---

Rewrite the `#knowledge-check` section body in the target lesson file using the structure and rules below. There must always be exactly 4 questions — one per lesson objective — so the quiz covers the full lesson without overlap. The design stays the same every lesson; only the question content and difficulty changes.

---

## Writing Style — apply to all question statements

Quiz statements must be easy to read and understand on the first pass. If a learner has to re-read a statement to figure out what it's asking, rewrite it.

- **One clear idea per statement.** No double negatives. No compound clauses joined by "however" or "unless".
- **Plain English only.** Avoid technical terms the lesson didn't teach. Use the exact vocabulary from the lesson — no synonyms that might confuse.
- **Concrete and specific.** Anchor the statement to something the reader actually did or saw in the lesson. Vague statements are bad quiz questions.
- **The correct answer should feel obvious to an attentive reader — not a trick.** The goal is reinforcement, not a gotcha.
- **False statements should contain a believable misconception.** Something a beginner might genuinely think is true — not something obviously wrong.

---

## Critical rule — one question per objective

Before writing any questions, read the `#objective` section of the target lesson file and identify the 4 core concepts being taught. Each question must test a different objective — never write two questions on the same topic.

---

## Inputs (fill in before running)

| Variable | Value |
|---|---|
| `TARGET_FILE` | Path to the lesson HTML file |
| `TOPIC` | The Python concept this lesson teaches (e.g. `variables`, `conditions`, `loops`, `functions`) |
| `DIFFICULTY` | `beginner` / `intermediate` / `advanced` — controls question language and complexity (see Difficulty Guide below) |
| `Q1_OBJECTIVE` | The objective/concept question 1 tests (copy the label from the objective card) |
| `Q1_STATEMENT` | The True/False statement for question 1 |
| `Q1_ANSWER` | `true` or `false` |
| `Q2_OBJECTIVE` | The objective/concept question 2 tests |
| `Q2_STATEMENT` | The True/False statement for question 2 |
| `Q2_ANSWER` | `true` or `false` |
| `Q3_OBJECTIVE` | The objective/concept question 3 tests |
| `Q3_STATEMENT` | The True/False statement for question 3 |
| `Q3_ANSWER` | `true` or `false` |
| `Q4_OBJECTIVE` | The objective/concept question 4 tests |
| `Q4_STATEMENT` | The True/False statement for question 4 |
| `Q4_ANSWER` | `true` or `false` |

---

## Difficulty guide

Use this guide when writing statements. Adjust vocabulary, sentence complexity, and how direct the question is.

### `beginner` (default for Track 1 lessons)
- Write in plain, everyday English — no technical jargon unless the term was explicitly taught in the lesson.
- Start statements with "you" wherever natural ("When you write…", "Python can help you…").
- Use contractions ("don't", "it's", "you're") to keep tone conversational.
- Keep statements to one simple idea — no compound clauses.
  - Use a concrete, relatable scenario to ground the statement (e.g. "calculating a total", "checking if an item is in a list", "printing a report").
- The correct answer should feel obvious if the learner paid attention — the goal is to reinforce, not to trick.

### `intermediate`
- Introduce correct technical vocabulary that was taught in the lesson (e.g. "variable", "syntax error", "function", "loop").
- Statements may have two related clauses, but each clause should still be clear.
- Examples can be more specific (e.g. “a loop that processes 10,000 rows in a spreadsheet”).
- One or two questions may involve a small "gotcha" — a common misconception beginners have — to test real understanding.
- Avoid obscure edge cases; stick to things covered in the lesson.

### `advanced`
- Questions may reference how concepts interact (e.g. "If you define a variable inside a function, it is accessible outside that function").
- Statements can include brief inline code snippets (e.g. `print(total_price)`) where relevant to the question.
- Scenarios should be realistic, concrete, and multi-step.
- At least one question should test a common mistake or misconception that is easy to get wrong.
- Language is precise and professional; contractions are no longer required.

---

## Answer pattern rule

Always alternate True/False answers across the 4 questions so learners cannot guess by clicking the same button repeatedly. The recommended default pattern is **True / False / True / False**, but any alternating pattern is acceptable. Never make all 4 answers the same.

---

## Writing rules for statements

- Every statement must be a **single, complete sentence** — no fragments, no bullet points.
- The statement must be **clearly right or clearly wrong** — avoid statements where "it depends" is a reasonable answer.
- **Do not use the exact wording from the objective label** in the statement — rephrase to test understanding, not memory of bullet text.
- Use a relatable real-world scenario where it fits naturally. Never force a domain that sounds awkward for the concept being tested.
- False statements should assert something that is a **common beginner misconception** — not something obviously absurd.

---

## Section shell (keep unchanged)

Always preserve the outer section shell exactly — do **not** change the section `id`, the header icon (`fa6-solid:brain`), or the header title ("Knowledge Check"). Only replace the `<div class="bg-white px-8 py-7 space-y-6">` body contents.

```html
<section id="knowledge-check">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:brain"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Knowledge Check</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5">Test your understanding before moving on</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <!-- PILL TABS + QUESTION PANELS GO HERE -->
    </div>
  </div>
</section>
```

---

## Pill tab row template

Always render all 4 pill tabs. The first tab gets the active pink gradient; the other three get the dark inactive style. Use `flex-wrap` so the row wraps on small screens.

```html
<div class="flex items-center gap-2 flex-wrap" role="tablist">
  <button onclick="switchQzTab(0)" class="qz-step qz-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span>
    <span class="qz-step-label text-xs font-bold">Question 1</span>
  </button>
  <button onclick="switchQzTab(1)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span>
    <span class="qz-step-label text-xs font-bold">Question 2</span>
  </button>
  <button onclick="switchQzTab(2)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span>
    <span class="qz-step-label text-xs font-bold">Question 3</span>
  </button>
  <button onclick="switchQzTab(3)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span>
    <span class="qz-step-label text-xs font-bold">Question 4</span>
  </button>
</div>
```

---

## Question panel template (repeat for Q1–Q4)

The first panel has no `hidden` class. Panels Q2–Q4 get `class="qz-panel qz-panel-anim hidden"`.

The `data-qid` attribute increments: `quiz-q0`, `quiz-q1`, `quiz-q2`, `quiz-q3`.

The watermark text increments: `Q1`, `Q2`, `Q3`, `Q4`.

For each question, the `onclick` on the **True** button gets `checkQuiz(this, QN_ANSWER)` and the **False** button gets the opposite boolean. Wire both buttons correctly — the checkQuiz boolean must match the actual correct answer.

```html
<!-- Q1 panel — no "hidden" class -->
<div class="qz-panel qz-panel-anim" role="tabpanel">
  <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

    <!-- Question header -->
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q1</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:circle-question"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">True or False</h3>
          <p class="text-xs text-gray-500 mt-0.5">Select the correct answer</p>
        </div>
      </div>
    </div>

    <!-- Question body -->
    <div class="px-6 py-5 space-y-4">
      <div class="quiz-question" data-qid="quiz-q0">
        <p class="text-sm font-semibold text-gray-800 mb-4">Q1_STATEMENT</p>
        <div class="flex gap-3">
          <!-- If Q1_ANSWER is true: True button gets checkQuiz(this, true), False button gets checkQuiz(this, false) -->
          <!-- If Q1_ANSWER is false: True button gets checkQuiz(this, false), False button gets checkQuiz(this, true) -->
          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors" onclick="checkQuiz(this, TRUE_IF_CORRECT)">
            <span class="iconify mr-1.5" data-icon="fa6-solid:check"></span> True
          </button>
          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors" onclick="checkQuiz(this, FALSE_IF_CORRECT)">
            <span class="iconify mr-1.5" data-icon="fa6-solid:xmark"></span> False
          </button>
        </div>
        <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
      </div>
    </div>

  </div>
</div>

<!-- Q2–Q4: same structure with class="qz-panel qz-panel-anim hidden" and incremented qid/watermark -->
```

> **Important — `checkQuiz` wiring:** The boolean passed to `checkQuiz(this, BOOL)` means "is clicking THIS button the correct action?" So:
> - If the correct answer is **True**: True button → `checkQuiz(this, true)`, False button → `checkQuiz(this, false)`
> - If the correct answer is **False**: True button → `checkQuiz(this, false)`, False button → `checkQuiz(this, true)`

---

## Quality checklist

Before submitting the rewritten section, verify:

- [ ] There are exactly **4 pill tabs** and exactly **4 question panels**
- [ ] Each question tests a **different lesson objective** — no topic is repeated
- [ ] Answers alternate (e.g. True / False / True / False) — not all the same
- [ ] `checkQuiz` booleans are wired correctly on both buttons for every question
- [ ] `data-qid` values run `quiz-q0` → `quiz-q1` → `quiz-q2` → `quiz-q3`
- [ ] Watermarks run `Q1` → `Q2` → `Q3` → `Q4`
- [ ] First panel has no `hidden` class; panels 2–4 have `hidden`
- [ ] All statements match the chosen `DIFFICULTY` level guidelines
- [ ] False statements test a **real beginner misconception**, not something obviously wrong
- [ ] Section `id`, header icon, and header title are unchanged
