---
mode: "agent"
description: "Write or rewrite the #comparison section for a lesson HTML file — fixed 3-column Python / SQL / Excel layout with labeled concept rows, centered divider, and side-by-side code blocks under each language column"
---

Rewrite the `#comparison` section body in the target lesson file using the structure and rules below. The three-column layout (Python / SQL / Excel), the centered divider label, and the code block grid always stay the same — only the concept rows, codes, and tip text change per lesson.

---

## Writing Style — apply to all text you write

This section bridges the gap between what the reader already knows (Excel or SQL) and what Python does. Write as if you're sitting next to them and pointing at the screen.

- **Connect before introducing.** Start from what they know (Excel formula, SQL clause) and show how Python does the same thing.
- **Short sentences.** 15 words or fewer. One idea per sentence.
- **Plain English.** No jargon. If a term is new, explain it in the same sentence. Use "you" not the passive voice.
- **Descriptions are comparisons, not definitions.** The reader wants to know "how is this the same as what I already do?" — not a textbook definition.
- **Tips remind, not teach.** The closing tip should give the reader one thing to carry away — the most important bridge between the three tools.
- **No filler.** Cut "it is important", "as you can see", "essentially", "please note".
- **American English only.** Use American spellings throughout — e.g. "optimize" not "optimise", "color" not "colour", "analyze" not "analyse".

---

## Inputs (fill in before running)

| Variable | Value |
|---|---|
| `TARGET_FILE` | Path to the lesson HTML file |
| `TOPIC` | The Python concept being taught in this lesson (e.g. `variables`, `conditions`, `loops`, `functions`) |
| `INTRO_TEXT` | One or two complete sentences introducing how SQL/Excel users will recognize this concept. Start with "If you already…" and connect it to the lesson topic. |
| `ROW_COUNT` | Number of concept comparison rows (minimum 2, maximum 4 for beginner lessons, up to 6 for advanced lessons) |
| `ROW_N_LABEL` | Lowercase label for each row — shown in the gray strip header (e.g. `one instruction`, `make a decision`, `store a value`) |
| `ROW_N_ICON` | Iconify icon `data-icon` value for the row header badge (e.g. `fa6-solid:box-archive`, `fa6-solid:font`, `fa6-solid:hashtag`, `fa6-solid:dollar-sign`, `fa6-solid:toggle-on`) |
| `ROW_N_PY_TERM` | Python term chip for row N (e.g. `statement`, `if / else`, `variable`) |
| `ROW_N_PY_DESC` | One short sentence explaining the Python term to a beginner. No jargon. |
| `ROW_N_SQL_TERM` | SQL equivalent term chip (e.g. `query clause`, `CASE WHEN`, `column value`) |
| `ROW_N_SQL_DESC` | One short sentence explaining the SQL equivalent. |
| `ROW_N_XL_TERM` | Excel equivalent term chip (e.g. `formula`, `=IF()`, `cell`) |
| `ROW_N_XL_DESC` | One short sentence explaining the Excel equivalent. |
| `DIVIDER_LABEL` | Centered divider label — describe exactly what the code blocks demonstrate, not just the concept (e.g. `Same member data, three tools`, `Same claim calculation, three tools`, `Same condition, three tools`) |
| `PY_CODE` | Python code for the side-by-side block. Use clear, descriptive variable names relevant to the lesson topic. Keep it to 1–4 lines. HTML-encode `<`, `>`, `&`, `'` as `&lt;`, `&gt;`, `&amp;`, `&apos;`. |
| `SQL_CODE` | Equivalent SQL for the side-by-side block. |
| `XL_CODE` | Equivalent Excel formula for the side-by-side block. |
| `CODE_CAPTION` | One sentence (plain text, no HTML) placed below the code grid explaining what all three versions do. |
| `TIP_TEXT` | Closing amber tip — one or two complete sentences. Remind the learner that all three tools express the same idea, just in different syntax. |

---

## Section shell (keep unchanged)

Always preserve the outer section shell exactly — do **not** change the section `id`, the header icon, the header title ("SQL / Excel Comparison"), or the subtitle. Only replace the `<div class="bg-white px-8 py-7 space-y-5">` body contents.

```html
<section id="comparison">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:table-columns"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">SQL / Excel Comparison</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">How this topic compares across Python, SQL, and Excel</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-5">
      <!-- BODY — replace everything inside here -->
    </div>
  </div>
</section>
```

---

## Body structure (replace this in order)

### 1 · Intro paragraph

```html
<p class="text-sm text-gray-600 leading-relaxed">INTRO_TEXT</p>
```

---

### 2 · Tool header cards (never change — always first)

```html
<div class="grid grid-cols-3 gap-3">
  <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-indigo-600 text-white">
    <span class="iconify text-lg" data-icon="fa6-brands:python"></span> Python
  </div>
  <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-orange-600 text-white">
    <span class="iconify text-lg" data-icon="fa6-solid:database"></span> SQL
  </div>
  <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-emerald-600 text-white">
    <span class="iconify text-lg" data-icon="fa6-solid:table"></span> Excel
  </div>
</div>
```

---

### 3 · Concept rows (repeat for each row, N = 1 to ROW_COUNT)

Each row has a gray label strip with an icon badge + 3 cells. Each cell has:
- A `text-xs text-gray-400` language label
- A colored term chip (indigo for Python, orange for SQL, emerald for Excel)
- A one-sentence description in `text-xs text-gray-500 leading-relaxed`
- Inline `<code class="font-mono">` snippets inside the description are encouraged for short examples

```html
<div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
  <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
    <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
      <span class="iconify text-indigo-400 text-[11px]" data-icon="ROW_N_ICON"></span>
    </span>
    <span class="text-xs font-bold uppercase tracking-widest text-gray-400">ROW_N_LABEL</span>
  </div>
  <div class="grid grid-cols-3 divide-x divide-gray-100">

    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">Python</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">ROW_N_PY_TERM</code>
      <p class="text-xs text-gray-500 leading-relaxed">ROW_N_PY_DESC</p>
    </div>

    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">SQL</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">ROW_N_SQL_TERM</code>
      <p class="text-xs text-gray-500 leading-relaxed">ROW_N_SQL_DESC</p>
    </div>

    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">Excel</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">ROW_N_XL_TERM</code>
      <p class="text-xs text-gray-500 leading-relaxed">ROW_N_XL_DESC</p>
    </div>

  </div>
</div>
```

> **Row count guidance:**
> - Beginner lessons (mod_01, mod_02): use one row per concept variant — e.g. for variables/data types, split into individual type rows (`str`, `int`, `float`, `bool`) rather than grouping them. Aim for 3–5 rows.
> - Intermediate lessons (mod_03–04): 3–4 rows matching the concept complexity
> - Advanced lessons (mod_05+): up to 5–6 rows

---

### 4 · Centered divider + side-by-side code blocks

The divider label is **always centered** with equal hairlines on both sides. The code grid is always 3 columns — Python / SQL / Excel — each column has its language label above and a dark code block below. Column labels and code block icons are fixed; only the code inside `<code>` changes.

```html
<div>
  <!-- Centered divider label -->
  <div class="flex items-center gap-3 mb-4">
    <span class="flex-1 h-px bg-gray-100"></span>
    <div class="flex items-center gap-2 shrink-0">
      <span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#fdf0f7] shrink-0">
        <span class="iconify text-brand text-sm" data-icon="fa6-solid:code-compare"></span>
      </span>
      <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D]">DIVIDER_LABEL</p>
    </div>
    <span class="flex-1 h-px bg-gray-100"></span>
  </div>

  <!-- 3-column code block grid -->
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 items-stretch">

    <!-- Python column -->
    <div class="flex flex-col">
      <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">Python code</p>
      <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">
        <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
          <div class="flex items-center gap-2">
            <span class="iconify" data-icon="logos:python" data-width="16" data-height="16"></span>
            <span class="text-xs font-semibold text-gray-400">Python</span>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-python">PY_CODE</code></pre>
      </div>
    </div>

    <!-- SQL column -->
    <div class="flex flex-col">
      <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">SQL query</p>
      <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">
        <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
          <div class="flex items-center gap-2">
            <span class="iconify text-orange-400" data-icon="fa6-solid:database"></span>
            <span class="text-xs font-semibold text-gray-400">SQL</span>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-sql">SQL_CODE</code></pre>
      </div>
    </div>

    <!-- Excel column -->
    <div class="flex flex-col">
      <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">Excel formula</p>
      <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">
        <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
          <div class="flex items-center gap-2">
            <span class="iconify text-green-400" data-icon="fa6-solid:table"></span>
            <span class="text-xs font-semibold text-gray-400">Excel</span>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-text">XL_CODE</code></pre>
      </div>
    </div>

  </div>

  <!-- Caption below the grid -->
  <p class="text-xs text-gray-400 mt-2">CODE_CAPTION</p>
</div>
```

---

### 5 · Closing amber tip (always last)

```html
<div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">TIP_TEXT</p>
</div>
```

---

## Content rules

### Concept rows
- Row labels must be **lowercase** (e.g. `store a value`, not `Store a Value`).
- Each description is **one sentence** — no semicolons, no bullet fragments.
- Python chip: `bg-indigo-50 text-indigo-700` — never change the colors.
- SQL chip: `bg-orange-50 text-orange-700` — never change.
- Excel chip: `bg-emerald-50 text-emerald-700` — never change.
- Keep cell content proportional — if the Python description is one sentence, the SQL and Excel descriptions must also be one sentence.

### Code blocks
- **No traffic-light dots** in any code block header — the column label (`Python code`, `SQL query`, `Excel formula`) above each block is sufficient.
- Python block: `class="language-python"` — always.
- SQL block: `class="language-sql"` — always.
- Excel block: `class="language-text"` — always (Prism doesn't highlight Excel formulas).
- Use clear, descriptive variable names in Python code (`item_price`, `discount_rate`, `total_cost`, `student_name`, etc.) that match the lesson's topic and are easy for a beginner to understand.
- Keep Python code short (1–4 lines) so all three columns align visually.
- HTML-encode special characters inside `<code>` blocks: `<` → `&lt;`, `>` → `&gt;`, `&` → `&amp;`, `'` → `&apos;`.

### Divider label
- The `DIVIDER_LABEL` text should **describe what the code actually shows**, not just repeat the concept name (e.g. `Same member data, three tools` rather than `Same variable, three tools`).
- Follow the pattern: **"Same [specific thing the code demonstrates], three tools"** (e.g. `Same claim calculation, three tools`, `Same eligibility check, three tools`).
- Always center it with a `flex-1 h-px bg-gray-100` hairline on both sides.
- Always use the `fa6-solid:code-compare` icon in the soft-pink circle.
- Never put a period at the end of the label.

### Caption
- Write as a complete sentence.
- Start with "All three…" and describe what the code accomplishes, then add "— the same result, just written in a different tool."

### Closing tip
- One to two sentences only.
- Reinforce that the same idea works across tools — help the learner feel confident that SQL/Excel knowledge transfers.
- Never repeat the intro paragraph word-for-word.

---

## Quality checklist

Before finalising, verify:

- [ ] Intro paragraph uses "If you already…" and connects to the lesson topic
- [ ] Tool header cards are unchanged (indigo / orange / emerald)
- [ ] Every row label strip has an icon badge (`w-5 h-5 rounded bg-indigo-50` + indigo Iconify icon)
- [ ] Every row has a lowercase gray-strip label
- [ ] Every cell has term chip + one-sentence description
- [ ] Chip colors match: indigo = Python, orange = SQL, emerald = Excel
- [ ] Divider label is centered with equal hairlines on both sides
- [ ] Divider label describes what the code actually shows (not just the concept name), follows "Same [specific thing], three tools" pattern
- [ ] No traffic-light dots in any code block header
- [ ] Python code uses `language-python`, SQL uses `language-sql`, Excel uses `language-text`
- [ ] Python, SQL, and Excel code blocks are aligned — similar line counts
- [ ] Caption below grid starts with "All three…"
- [ ] Closing amber tip is 1–2 sentences and does not repeat the intro

---

## Reference example — lesson01_what_is_programming.html

**Inputs used:**
```
TOPIC          = what is programming
INTRO_TEXT     = If you already use SQL or Excel, you already know how to give a computer instructions. Python works the same way — it just gives you more control over what those instructions can do.
ROW_COUNT      = 2
ROW_1_LABEL    = one instruction
ROW_1_PY_TERM  = statement
ROW_1_PY_DESC  = One line of code that does one thing.
ROW_1_SQL_TERM = query clause
ROW_1_SQL_DESC = A keyword like SELECT or WHERE that tells the database what to do.
ROW_1_XL_TERM  = formula
ROW_1_XL_DESC  = A cell expression starting with = that computes a result.
ROW_2_LABEL    = a full program
ROW_2_PY_TERM  = script
ROW_2_PY_DESC  = A file that runs many statements from top to bottom.
ROW_2_SQL_TERM = stored procedure
ROW_2_SQL_DESC = A saved collection of queries you can run together by name.
ROW_2_XL_TERM  = macro
ROW_2_XL_DESC  = A recorded set of steps Excel can replay on demand.
DIVIDER_LABEL  = Same calculation, three tools
PY_CODE        = discount = item_price * 0.25
SQL_CODE       = SELECT item_price * 0.25\n  AS discount\nFROM orders;
XL_CODE        = =A2 * 0.25
CODE_CAPTION   = All three calculate a 25% discount from an item price — the same result, just written in a different tool.
TIP_TEXT       = The concepts are the same across all three tools. Once you understand what a program is, switching between Python, SQL, and Excel just means learning a different syntax for the same ideas.
```
