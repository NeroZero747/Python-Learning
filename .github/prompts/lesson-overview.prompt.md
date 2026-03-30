---
mode: "agent"
description: "Write or rewrite the #overview section for a lesson HTML file"
---

Rewrite the `#overview` section body in the target lesson file using the 4-part structure below.

---

## Writing Style — apply to all text you write

This content is for people who are new to programming. Write as if you're explaining to a colleague who is smart but has never written a line of code.

- **Use plain English.** If a simpler word exists, use it. Avoid jargon unless the term was explicitly introduced in this lesson — and when you do use a new term, define it in the same sentence.
- **Short sentences win.** Aim for 15 words or fewer per sentence. Break long ideas into two sentences.
- **One idea per sentence.** Don't chain concepts with "and" or "which".
- **Address the reader.** Use "you" and "your" — it feels less intimidating than passive voice.
- **Concrete over abstract.** Compare the concept to something the learner already does (writing a list, using a formula in Excel, following a recipe).
- **No filler phrases.** Cut "it is important to note", "as you can see", "essentially", "in order to".

---

## Inputs (fill in before running)

| Variable | Value |
|---|---|
| `TARGET_FILE` | Path to the lesson HTML file |
| `TOPIC` | The lesson topic in plain English (e.g. `programming`, `variables`, `loops`) |
| `HOOK_SENTENCE` | One clear sentence defining what the topic IS — goes inside the quote banner |
| `ANALOGY_DOMAIN` | The real-world thing used as the analogy (e.g. `a chef's recipe`, `a filing cabinet`, `a toolbox`) |
| `ANALOGY_INTRO` | The full "Think of…" sentence introducing the analogy |
| `CONCEPT_1` through `CONCEPT_4` | The four sub-concepts to show as cards — each maps to a title, an analogy subtitle, and a single short analogy-anchored phrase (not a definition) |

---

## Rules

### Part 1 — Hook quote banner
- Replace only the `<p>` text inside with `HOOK_SENTENCE`
- The sentence should define the topic in plain English — no jargon
- Do **not** put the analogy here
- Use `items-center` on the flex row so the icon and text are vertically centered — do **not** use `items-start` or add `mt-0.5` to the icon

Exact wrapper to use (only `HOOK_SENTENCE` changes):

```html
<div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
  <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Py</span>
  <div class="relative flex items-center gap-4">
    <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">
      <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>
    </span>
    <p class="text-base text-gray-800 leading-relaxed font-medium">HOOK_SENTENCE</p>
  </div>
</div>
```

### Part 2 — Analogy intro paragraph
- Place immediately after the closing `</div>` of the quote banner
- Must start with "Think of…"
- Introduce `ANALOGY_DOMAIN` and map it directly to the lesson topic
- End by naming Python or the key term: "A **[term]** is that [thing], and Python is the language you use to write it."
- One paragraph only, `text-sm text-gray-600 leading-relaxed`

### Part 3 — 2-column analogy card grid
- Exactly 4 cards in a `grid grid-cols-1 sm:grid-cols-2 gap-3` wrapper
- Each card must have:
  - A unique Iconify icon from `fa6-solid:`
  - A **bold title** — the technical concept name (≤4 words)
  - An *italic analogy subtitle* — "The [thing] — [what it does in the analogy]" (≤50 chars)
  - A **single short phrase** as the description (`text-xs text-gray-500`) — see rules below
- Use a different accent color per card. Standard set: pink (`#fdf0f7` / `text-brand`), violet, blue, emerald
- Card hover uses the matching accent: `hover:border-[color]-100 hover:bg-[color]-50/30`

#### Card description rules (critical)
The card description must be **one brief phrase** that echoes the analogy — nothing more. This section is a high-level map, not a tutorial. All definitions, syntax, and detail live in later sections (Key Concepts, Code Examples, etc.).

- **Maximum length:** one sentence, ideally under 12 words
- **No definitions** — do not explain what the concept is
- **No syntax or code** — do not include `<code>` elements, variable names, or Python keywords
- **No duplication** — do not repeat anything already in the subtitle
- **Analogy-anchored** — the phrase should place the concept inside the analogy domain (e.g. "the filing cabinet", "the drawer", "the label")

**Pattern:** "The [analogy object] — [one thing it does in the analogy]."

**Good example (filing cabinet analogy):**
- Variable → *"The label on the drawer — gives any value a name your script can refer back to."*
- String → *"Text documents in the cabinet — anything you read rather than calculate."*
- int & float → *"Number sheets in the cabinet — whole counts or decimals, depending on your data."*
- Boolean → *"The checkbox on the drawer — ticked or unticked, nothing in between."*

**Bad example (too much detail — belongs in Key Concepts):**
- ~~"A string is any piece of text wrapped in quotes, such as `"Hello"`. Python uses strings whenever you work with names, messages, or any value that cannot be calculated as a number."~~

### Part 4 — Amber tip box
- One sentence starting with a concrete benefit or bridge to what the learner already knows
- Use the `bg-amber-tip` class and `fa6-solid:circle-info` icon
- Do **not** repeat the analogy — add new information (e.g. connect to Excel/SQL/existing knowledge)

---

## What NOT to change
- The `<section id="overview">` outer wrapper and section header must stay exactly as they are
- Do not touch anything outside `<section id="overview">` … `</section>`
- Do not remove the `space-y-5` class on the section body `<div>`

---

## Output structure

Use a Python script to perform the replacement (string search between unique anchor markers, not fragile line-number edits). The script should:
1. Read `TARGET_FILE`
2. Find the old body content between the end of the hook quote banner and the closing `</div></div></section>` of the overview section
3. Replace it with the 4-part HTML below
4. Write the file and print a ✅ / ❌ status

```html
<!-- Part 2 — Analogy intro paragraph -->
<p class="text-sm text-gray-600 leading-relaxed">ANALOGY_INTRO</p>

<!-- Part 3 — Analogy card grid -->
<div class="grid grid-cols-1 sm:grid-cols-2 gap-3">

  <!-- Card 1 — pink accent -->
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
        <span class="iconify text-brand text-base" data-icon="ICON_1"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">TITLE_1</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">SUBTITLE_1</p>
      </div>
    </div>
    <!-- DESC_1 = one short analogy-anchored phrase, ≤12 words, no definitions, no code -->
    <p class="text-xs text-gray-500 leading-relaxed">DESC_1</p>
  </div>

  <!-- Card 2 — violet accent -->
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-violet-100 hover:bg-violet-50/30 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-violet-50 shrink-0">
        <span class="iconify text-violet-500 text-base" data-icon="ICON_2"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">TITLE_2</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">SUBTITLE_2</p>
      </div>
    </div>
    <!-- DESC_2 = one short analogy-anchored phrase, ≤12 words, no definitions, no code -->
    <p class="text-xs text-gray-500 leading-relaxed">DESC_2</p>
  </div>

  <!-- Card 3 — blue accent -->
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-blue-100 hover:bg-blue-50/30 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-blue-50 shrink-0">
        <span class="iconify text-blue-500 text-base" data-icon="ICON_3"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">TITLE_3</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">SUBTITLE_3</p>
      </div>
    </div>
    <!-- DESC_3 = one short analogy-anchored phrase, ≤12 words, no definitions, no code -->
    <p class="text-xs text-gray-500 leading-relaxed">DESC_3</p>
  </div>

  <!-- Card 4 — emerald accent -->
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-emerald-100 hover:bg-emerald-50/30 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-emerald-50 shrink-0">
        <span class="iconify text-emerald-500 text-base" data-icon="ICON_4"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">TITLE_4</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">SUBTITLE_4</p>
      </div>
    </div>
    <!-- DESC_4 = one short analogy-anchored phrase, ≤12 words, no definitions, no code -->
    <p class="text-xs text-gray-500 leading-relaxed">DESC_4</p>
  </div>

</div>

<!-- Part 4 — Amber tip -->
<div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">AMBER_TIP</p>
</div>
```
