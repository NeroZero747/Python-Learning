---
mode: "agent"
description: "Write or rewrite the #code-examples section for a lesson HTML file using Style A code blocks (dark-chrome, integrated terminal pane)"
---

Rewrite the `#code-examples` section body in the target lesson file using the structure and rules below.

---

## Writing Style — apply to all text you write

This content is for people who are new to programming. Write descriptions and tips as if you're talking to a colleague who is smart but has never written code before.

- **Lead with what the code does, not what the scenario is.** The reader wants to understand Python, not read a business brief.
- **Short sentences.** 15 words or fewer per sentence. One idea per sentence.
- **No jargon.** Avoid words like "instantiate", "invoke", "populate", "downstream". If you must use a new Python term (e.g. "variable"), bold it and say what it holds in the same sentence.
- **Use "you".** "This script stores your data as a variable" is clearer than "variables are used to store data".
- **Tips should be one action.** A tip is one concrete takeaway — what to watch for, or what to try next. Not a summary of what was just shown.
- **No filler.** Cut "it is important to note", "as you can see", "essentially", "in order to".
- **American English only.** Use American spellings throughout — e.g. "optimize" not "optimise", "color" not "colour", "analyze" not "analyse".

---

## Inputs (fill in before running)

| Variable | Value |
|---|---|
| `TARGET_FILE` | Path to the lesson HTML file |
| `TOPIC` | The Python concept being taught (e.g. `variables`, `conditions`, `loops`, `functions`) |
| `EX1_TAB` | Short tab pill label for example 1 — topic title only, no "Example 1 —" prefix (e.g. `Greet a User`, `Check a Value`, `Filter a List`) |
| `EX1_DOMAIN` | The domain or subject area for example 1 — e.g. `Products`, `Orders`, `Students`, `Books`. Choose any universally understandable domain that fits the lesson's context. |
| `EX1_TITLE` | Panel heading — same as `EX1_TAB` |
| `EX1_PILLS` | Extra keyword pills after Beginner badge — comma-separated (e.g. `print(), Sequential Flow`) |
| `EX1_DESC` | "What This Does" description — **1–2 short sentences max**. Lead with what the code does (not the business process). Bold new Python terms. Keep it high-level — no jargon. |
| `EX1_FILENAME` | Python filename shown in the code tab (e.g. `greet_user.py`) |
| `EX1_CODE` | Python code — every line must have a `# inline comment`. Use clear, meaningful variable names. HTML-encode `<`, `>`, `&`, `'` as `&lt;`, `&gt;`, `&amp;`, `&apos;`. |
| `EX1_CMD` | Terminal command (e.g. `$ python greet_user.py`) |
| `EX1_OUTPUT` | Terminal output lines — use `<br>` between lines |
| `EX1_TIP` | Amber tip — **one sentence** stating why this matters in plain English. Do NOT repeat the description. No technical jargon. |
| `EX2_TAB` | Short tab pill label for example 2 |
| `EX2_DOMAIN` | The domain or subject area for example 2 |
| `EX2_TITLE` | Panel heading for example 2 |
| `EX2_PILLS` | Extra keyword pills for example 2 |
| `EX2_DESC` | "What This Does" description for example 2 — same rules as `EX1_DESC`: 1–2 sentences, code-first, no jargon |
| `EX2_FILENAME` | Python filename for example 2 |
| `EX2_CODE` | Python code for example 2 |
| `EX2_CMD` | Terminal command for example 2 |
| `EX2_OUTPUT` | Terminal output for example 2 |
| `EX2_TIP` | Amber tip for example 2 — one sentence, same rules as `EX1_TIP` |
| `EX3_TAB` | Short tab pill label for example 3 |
| `EX3_DOMAIN` | The domain or subject area for example 3 |
| `EX3_TITLE` | Panel heading for example 3 |
| `EX3_PILLS` | Extra keyword pills for example 3 |
| `EX3_DESC` | "What This Does" description for example 3 — same rules as `EX1_DESC`: 1–2 sentences, code-first, no jargon |
| `EX3_FILENAME` | Python filename for example 3 |
| `EX3_CODE` | Python code for example 3 |
| `EX3_CMD` | Terminal command for example 3 |
| `EX3_OUTPUT` | Terminal output for example 3 |
| `EX3_TIP` | Amber tip for example 3 — one sentence, same rules as `EX1_TIP` |

---

## Rules

### Locate the section

Find `<section id="code-examples">` in `TARGET_FILE`. Replace only the **body div** — the `<div class="bg-white px-8 py-7 ...">` that sits directly after the section header. Do **not** touch the section header or anything outside the section.

The outer body wrapper must use `space-y-6`:
```html
<div class="bg-white px-8 py-7 space-y-6">
```

---

### Tab pill row

One active pill (pink gradient) and two inactive pills (dark gray). Always use the topic title as the label — never "Example 1", "Example 2", "Example 3".

```html
<div class="flex items-center gap-2 mb-6" role="tablist">

  <button onclick="switchCeTab(0)" class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
    <span class="ce-step-label text-xs font-bold">EX1_TAB</span>
  </button>

  <button onclick="switchCeTab(1)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
    <span class="ce-step-label text-xs font-bold">EX2_TAB</span>
  </button>

  <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
    <span class="ce-step-label text-xs font-bold">EX3_TAB</span>
  </button>

</div>
```

---

### Panel structure (repeat for all three examples)

The first panel has no `hidden` class. The second and third panels have `class="ce-panel ce-panel-anim hidden"`.

```html
<div class="ce-panel ce-panel-anim" role="tabpanel">        <!-- panel 1 — visible -->
<div class="ce-panel ce-panel-anim hidden" role="tabpanel"> <!-- panels 2 & 3 — hidden -->
```

Each panel follows this exact inner structure:

```html
<div class="ce-panel ce-panel-anim[hidden]" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

    <!-- Panel header -->
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:code"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">EX1_TITLE</h3>
          <div class="flex items-center gap-2 mt-1">

            <!-- Always first: Beginner badge -->
            <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
              <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
            </span>

            <!-- Domain pill — always second -->
            <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">EX1_DOMAIN</span>

            <!-- Additional keyword pills from EX1_PILLS -->
            <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">KEYWORD</span>

          </div>
        </div>
      </div>
    </div>

    <!-- Panel body -->
    <div class="px-6 py-5 space-y-4">

      <!-- "What This Does" description box -->
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
          <p class="text-sm text-gray-600">EX1_DESC</p>
        </div>
      </div>

      <!-- Code block — Style A (dark-chrome, no traffic-light dots, filename pill only) -->
      <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
        <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
          <div class="flex items-center gap-3">
            <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
              <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
              <span class="text-[11px] font-semibold text-gray-400">EX1_FILENAME</span>
            </div>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-python">EX1_CODE</code></pre>
        </div>
        <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
          <div class="flex items-center gap-2 mb-1.5">
            <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
            <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
            <span class="text-[10px] text-gray-600 font-mono">EX1_CMD</span>
          </div>
          <div class="font-mono text-xs text-emerald-400 leading-relaxed">EX1_OUTPUT</div>
        </div>
      </div>

      <!-- Amber tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">EX1_TIP</p>
      </div>

    </div>
  </div>
</div>
```

The watermark number in the panel header (`01`, `02`, `03`) must match the panel position.

---

## Code block rules (critical)

### No traffic-light dots
The header bar must **never** contain the three colored dot spans. Only the filename pill appears on the left:

**Correct:**
```html
<div class="flex items-center gap-3">
  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" ...></span>
    <span class="text-[11px] font-semibold text-gray-400">filename.py</span>
  </div>
</div>
```

**Wrong (do not use):**
```html
<div class="flex gap-1.5">
  <span class="w-2.5 h-2.5 rounded-full bg-red-400/80"></span>
  <span class="w-2.5 h-2.5 rounded-full bg-amber-400/80"></span>
  <span class="w-2.5 h-2.5 rounded-full bg-emerald-400/80"></span>
</div>
```

### Terminal output pane
Every code block must have the dark terminal output pane at the bottom (`bg-[#11111b]`). Use `<br>` to separate multiple output lines within the `leading-relaxed` div.

### Inline comments
Every meaningful line of code must have a `# comment` explaining what it does in plain English. Blank separator lines between logical blocks do not need comments.

### HTML entities
Inside `<code class="language-python">` elements, always encode:
- `<` → `&lt;`
- `>` → `&gt;`
- `&` → `&amp;`
- `'` → `&apos;`
- `"` → `&quot;`

---

## Example content guidelines

### Domain assignment
Each of the three examples should cover a different subject area if possible — for example Products, Orders, and Customers; or Books, Students, and Scores; or any other simple, everyday domain the reader will recognize instantly. Choose domains that are universally understandable — everyday objects (shops, schools, trips, recipes) rather than specialist industries. If no specific domain is given, use the simplest possible real-world scenario (e.g. a name, a price, a list of items).

### Difficulty progression
The three examples must get progressively more complex, matching the concept being taught:
- **Example 1** — the simplest possible use of the concept, using `print()` or a single variable
- **Example 2** — introduces one new idea (a calculation, a second variable, a comparison)
- **Example 3** — combines two ideas from examples 1 and 2, or introduces a small collection (list) and a built-in function

### Code quality rules
- **8 lines maximum per code block.** Count every line including blank separator lines and import lines. If you need more, simplify the example — cut a step, not a comment.
- **No step-header comment dividers.** Never use `# ── Step 1: …` or `# === Section ===` style headers inside example code. Use a single inline comment on the relevant line instead.
- **No `if __name__ == "__main__"` guard.** Example code runs at the top level. Never wrap output or function calls inside this pattern.
- **Terminal output: 1–2 lines of plain text.** No ASCII tables, no tree diagrams, no formatted banners or headers. One short `print()` result per line.
- Variable names must be clear and descriptive — never `x`, `y`, `a`, `val`, or vague names
- Use snake_case for all variable names (e.g. `product_name`, `order_total`, `item_count`)
- Keep code simple enough for a beginner — no classes, no comprehensions, no f-strings unless the lesson specifically covers them
- Each example should take no longer than 30 seconds to read and understand

### "What This Does" description rules
- **Length:** 1–2 sentences maximum. No long paragraphs.
- **Lead with the code**, not the business scenario. Tell the learner what the script does, then why it matters.
- Bold new Python terms using `<strong class="text-gray-800">term</strong>`.
- Use inline `<code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">fn()</code>` for Python keywords or function names.
- **No jargon** — write as if explaining to someone who has never programmed before.

**Good example:** "This script stores four pieces of information as **variables** — one for each data type — then prints them. Each variable holds a different kind of value: text, a whole number, a decimal, or true/false."

**Bad example:** "When a member calls the helpline, the service representative's screen populates with key details pulled from the system. This script creates four variables…"

### Tip rules
- **One sentence only.** State the plain "why this matters" or "what to watch out for".
- Do NOT repeat what the description already said.
- No jargon, no multi-step technical explanations.
- Prefer actionable or cautionary statements (e.g. "Change the number at the top and Python recalculates everything below automatically.")

---

## Content quality checklist

Before writing the HTML, verify:

- [ ] All three examples cover different domains or subject areas
- [ ] Tab labels are descriptive topic titles, not "Example 1 / 2 / 3"
- [ ] Panel headings match the tab labels exactly
- [ ] Watermark numbers are `01`, `02`, `03` matching panel order
- [ ] No traffic-light dots in any code block header
- [ ] Every code block has a terminal output pane
- [ ] Every code block is **8 lines or fewer** (including blank lines and imports)
- [ ] No step-header comment dividers (`# ── Step 1:` etc.) inside any code block
- [ ] No `if __name__ == "__main__"` guard in any example
- [ ] Terminal output is **1–2 lines of plain text** — no ASCII tables, trees, or formatted headers
- [ ] Every meaningful code line has a `# comment`
- [ ] HTML entities are correctly encoded inside `<code>` elements
- [ ] All variable names are clear, descriptive, and in snake_case
- [ ] "What This Does" descriptions are 1–2 short sentences, lead with what the code does (not the business scenario), contain no jargon
- [ ] Tips are a single sentence — no jargon, no repetition of the description
- [ ] Difficulty increases across the three examples

---

## Example — completed Code Examples for “What is Programming?”

Target file: `pages/track_01/mod_02_programming_foundations/lesson01_what_is_programming.html`

The section was rewritten with:

| # | Tab | Domain | Title | Key concept shown |
|---|---|---|---|---|
| 1 | Greet a User | Products | Greet a User | `print()` + sequential execution |
| 2 | Calculate a Discount | Orders | Calculate a Discount | Variables + arithmetic (`*`) to show two values |
| 3 | Total Item Prices | Customers | Total Item Prices | List + `sum()` to total a set of values |

Code filenames: `greet_user.py`, `discount_calc.py`, `item_total.py`
