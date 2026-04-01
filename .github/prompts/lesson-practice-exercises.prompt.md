---
mode: "agent"
description: "Write or rewrite the #practice section for a lesson HTML file — descriptive tab names, relatable tasks, show-answer accordion, and mod_01-style code blocks with terminal output pane"
---

Rewrite the `#practice` section body in the target lesson file using the structure and rules below. The design — tab pills, panel header, task box, accordion, code block, terminal pane, and tip — stays the same every lesson; only the content changes.

---

## Writing Style — apply to all text you write

This content is for people who are new to programming. Write task descriptions and tips as if you're giving instructions to a colleague who has never coded before.

- **Task descriptions must be clear enough to act on.** The reader should know exactly what to type after reading one time. State what data to use, what to write, and what the output should look like.
- **Short sentences.** 15 words or fewer. One idea per sentence — no chaining with "and" or "which".
- **Use "you".** "Create a variable called `name`" is clearer than "a variable should be created".
- **No jargon without explanation.** If you use a Python term (e.g. "accumulator"), explain it in a bracket or the next sentence.
- **Tips should be one practical takeaway.** Tell the reader what to remember or what to try — not a repeat of the task.
- **No filler.** Cut "it is important", "please note", "essentially", "in order to".
- **American English only.** Use American spellings throughout — e.g. "optimize" not "optimise", "color" not "colour", "analyze" not "analyse".

---

## Inputs (fill in before running)

| Variable | Value |
|---|---|
| `TARGET_FILE` | Path to the lesson HTML file |
| `TOPIC` | The Python concept being practiced (e.g. `print statements`, `variables`, `conditions`, `loops`, `functions`) |
| `EX_COUNT` | Number of exercises (typically 3; add more for advanced lessons) |
| `EX1_TAB` | Short tab pill label for exercise 1 — describe the task, not a number (e.g. `Print a Report`, `Check a Value`, `Filter a List`) |
| `EX1_TITLE` | Panel heading — same as `EX1_TAB` |
| `EX1_DOMAIN` | Subject area label for example 1 (e.g. `Products`, `Orders`, `Students`, `Books`). Choose any simple, universally understandable domain that fits the lesson's context. |
| `EX1_BADGES` | Extra badge pill labels after the Beginner badge — comma-separated (e.g. `print()`, `Sequential Flow`) |
| `EX1_TASK` | Full-sentence task description. Set the scenario first (who, what data), then state exactly what the learner must write. End with what the output should show. Keep to 2–3 sentences. |
| `EX1_FILENAME` | Solution filename shown in the code tab (e.g. `member_report.py`) |
| `EX1_CODE` | Solution code — every line must have a `# inline comment`. Use meaningful, descriptive variable names that fit the scenario. HTML-encode `<`, `>`, `&`, `'` as `&lt;`, `&gt;`, `&amp;`, `&apos;`. |
| `EX1_CMD` | Terminal command shown in the output pane (e.g. `$ python member_report.py`) |
| `EX1_OUTPUT` | Terminal output lines — use `<br>` between lines |
| `EX1_TIP` | Amber tip text — one or two complete sentences. Explain *why* the pattern matters in context. Do not repeat the task description. |
| `EX2_TAB` | Short tab pill label for exercise 2 |
| `EX2_TITLE` | Panel heading for exercise 2 |
| `EX2_DOMAIN` | Subject area label for example 2 |
| `EX2_BADGES` | Extra badge pills for exercise 2 |
| `EX2_TASK` | Task description for exercise 2 |
| `EX2_FILENAME` | Solution filename for exercise 2 |
| `EX2_CODE` | Solution code for exercise 2 |
| `EX2_CMD` | Terminal command for exercise 2 |
| `EX2_OUTPUT` | Terminal output for exercise 2 |
| `EX2_TIP` | Amber tip for exercise 2 |
| `EX3_TAB` | Short tab pill label for exercise 3 |
| `EX3_TITLE` | Panel heading for exercise 3 |
| `EX3_DOMAIN` | Subject area label for example 3 |
| `EX3_BADGES` | Extra badge pills for exercise 3 |
| `EX3_TASK` | Task description for exercise 3 |
| `EX3_FILENAME` | Solution filename for exercise 3 |
| `EX3_CODE` | Solution code for exercise 3 |
| `EX3_CMD` | Terminal command for exercise 3 |
| `EX3_OUTPUT` | Terminal output for exercise 3 |
| `EX3_TIP` | Amber tip for exercise 3 |

> For `EX_COUNT` > 3, repeat all `EX_N_*` variables and panel blocks for each additional exercise.

---

## Section shell (keep unchanged)

Always preserve the outer section shell exactly — do **not** change the section `id`, the header icon, the header title ("Practice Exercises"), or the subtitle. Only replace the `<div class="bg-white px-8 py-7 space-y-6">` body contents.

```html
<section id="practice">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:pencil"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Practice Exercises</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Guided exercises to reinforce your learning</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <!-- BODY — replace everything inside here -->
    </div>
  </div>
</section>
```

---

## Body structure (replace this in order)

### 1 · Tab pill row

The first tab is always active (pink gradient). All other tabs are dark gray. The icon is always `fa6-solid:pencil`. Match the number of `<button>` elements to `EX_COUNT`.

```html
<div class="flex items-center gap-2 mb-6" role="tablist">

  <button onclick="switchPeTab(0)" class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
    <span class="pe-step-label text-xs font-bold">EX1_TAB</span>
  </button>

  <button onclick="switchPeTab(1)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
    <span class="pe-step-label text-xs font-bold">EX2_TAB</span>
  </button>

  <!-- Repeat for each additional tab, incrementing switchPeTab(N) -->

</div>
```

---

### 2 · Exercise panel (repeat for each exercise, N = 1 to EX_COUNT)

The first panel has no `hidden` class. All subsequent panels have `class="pe-panel pe-panel-anim hidden"`.

```html
<div class="pe-panel pe-panel-anim [hidden if not first]" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

    <!-- Panel header -->
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">0N</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">EXN_TITLE</h3>
          <div class="flex items-center gap-2 mt-1">
            <!-- Beginner badge — always first -->
            <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
              <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
            </span>
            <!-- Domain badge (label set by EX_N_DOMAIN) -->
            <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">EXN_DOMAIN</span>
            <!-- Additional concept badges from EXN_BADGES -->
            <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">BADGE</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Panel body -->
    <div class="px-6 py-5 space-y-4">

      <!-- Task description box -->
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
          <p class="text-sm text-gray-600">EXN_TASK</p>
        </div>
      </div>

      <!-- Show Answer accordion toggle -->
      <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
        <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
        <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
      </button>

      <!-- Accordion body (hidden by default) -->
      <div class="accordion-body">

        <!-- Code block — Style A (dark-chrome, no traffic-light dots, filename pill only, no terminal pane) -->
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">EXN_FILENAME</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code">
            <pre class="overflow-x-auto pre-reset"><code class="language-python">EXN_CODE</code></pre>
          </div>
          <!-- Terminal output pane -->
          <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
            <div class="flex items-center gap-2 mb-1.5">
              <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
              <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
              <span class="text-[10px] text-gray-600 font-mono">EXN_CMD</span>
            </div>
            <div class="font-mono text-xs text-emerald-400 leading-relaxed">EXN_OUTPUT</div>
          </div>
        </div>

        <!-- Amber tip -->
        <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">EXN_TIP</p>
        </div>

      </div>
    </div>

  </div>
</div>
```

---

## Content rules

### Tab labels
- Short, action-oriented, and descriptive — read like a task title, not a number (e.g. `Print a Label`, `Calculate a Discount`, `Total Item Prices`).
- Never use "Exercise N" as the label.
- Three words maximum per tab label.

### Panel headers
- The `0N` watermark in the top-right corner must match the exercise number: `01`, `02`, `03`, etc.
- The `EXN_TITLE` matches `EXN_TAB` exactly.
- Badge order: **Beginner** badge always first, then **domain badge** (the label from `EXN_DOMAIN`), then any concept badges from `EXN_BADGES`.
- Each exercise uses a different domain so the three exercises each cover a distinct, easy-to-understand subject area.

### Task description (`EXN_TASK`)
- Write 2–3 complete sentences. No bullet fragments.
- **Sentence 1**: Set the scenario — who or what is involved, and what data you have (e.g. “A customer bought three books priced at $12, $8, and $20.”).
- **Sentence 2**: State the concrete task — what variables to create, what calculation to perform, or what to print.
- **Sentence 3** (optional but recommended): Tell the learner what correct output looks like, or what they should verify.

### Code blocks
- **No traffic-light dots** — the block header contains the filename pill only. Never add `<span class="w-2.5 h-2.5 rounded-full ...">` traffic-light elements.
- Use `class="language-python"` on the `<code>` element — always.
- **8 lines maximum per code block.** Count every line including blank separator lines and imports. Simplify the example if you exceed this limit — cut a step, not a comment.
- **No step-header comment dividers.** Never use `# ── Step 1: …` or `# === Section ===` style headers inside solution code.
- **No `if __name__ == "__main__"` guard.** Solution code runs at the top level.
- Every line of code **must** have a `# inline comment` explaining what it does.
- Variable names must be descriptive and match the scenario: `item_price`, `discount_rate`, `total_cost`, `student_score`, `book_title`, `order_count`, etc. Never use generic names like `a`, `b`, `x`, or `value`.
- HTML-encode special characters inside `<code>` blocks: `<` → `&lt;`, `>` → `&gt;`, `&` → `&amp;`, `'` → `&apos;`.

### Terminal output pane
- Always present — even for `print()` exercises with a single output line.
- **1–2 lines of plain text maximum.** No ASCII tables, tree diagrams, or formatted headers. One short `print()` result per line.
- `EXN_CMD` format: `$ python FILENAME` (no path prefix).
- `EXN_OUTPUT` uses `<br>` between multiple output lines.
- Output text color is always `text-emerald-400` — never change it.

### Amber tip (`EXN_TIP`)
- 1–2 complete sentences.
- Explain **why** the pattern or concept matters in everyday terms — connect it to something the reader might actually do (calculating a total, updating a record, checking a value).
- Do not repeat the task description word-for-word.
- Do not start with "Note:" or "Remember:".

### Difficulty progression
- All three exercises in a beginner lesson use the **Beginner** badge.
- For intermediate/advanced lessons, exercise 3 may use an **Intermediate** badge:
  ```html
  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-amber-50 text-amber-600 border border-amber-200">
    <span class="iconify text-[10px]" data-icon="fa6-solid:fire"></span> Intermediate
  </span>
  ```

---

## Quality checklist

Before finalising, verify:

- [ ] Tab labels are descriptive, action-oriented, and match panel titles exactly
- [ ] No exercise tab is labelled "Exercise N"
- [ ] Panel watermarks (`01`, `02`, `03`) match exercise order
- [ ] Badges: Beginner first, then domain label, then concept badges
- [ ] All three exercises use different, easy-to-understand domains
- [ ] Each task description is 2–3 complete sentences — no bullet fragments or tag strings
- [ ] No traffic-light dots in any code block header
- [ ] Every code block is **8 lines or fewer** (including blank lines and imports)
- [ ] No step-header comment dividers (`# ── Step 1:` etc.) inside any code block
- [ ] No `if __name__ == "__main__"` guard in any solution
- [ ] Every code line has a `# inline comment`
- [ ] All variable names are descriptive and match the scenario
- [ ] Special characters in `<code>` are HTML-encoded
- [ ] Terminal output pane is present in every exercise
- [ ] Amber tip connects the exercise to a real-world context the reader will recognize
- [ ] First panel has no `hidden` class; panels 2+ have `class="pe-panel pe-panel-anim hidden"`

---

## Reference example — lesson01_what_is_programming.html

**Inputs used:**
```
TOPIC    = print statements and basic arithmetic
EX_COUNT = 3

EX1_TAB      = Print a Product Label
EX1_TITLE    = Print a Product Label
EX1_DOMAIN   = Products
EX1_BADGES   = print(), Sequential Flow
EX1_TASK     = Write a Python program that prints three lines about a product in a shop: its name, its price, and how many are in stock. Each piece of information should appear on its own line, in the exact order you write the code.
EX1_FILENAME = product_label.py
EX1_CODE     = print("Product: Wireless Mouse")  # print the product name
               print("Price: $29.99")             # print the price
               print("In stock: 42")              # print the stock count
EX1_CMD      = $ python product_label.py
EX1_OUTPUT   = Product: Wireless Mouse<br>Price: $29.99<br>In stock: 42
EX1_TIP      = Notice the output appears in exactly the same order as the three print() lines — Python always runs statements from top to bottom, one at a time.

EX2_TAB      = Calculate a Discount
EX2_TITLE    = Calculate a Discount
EX2_DOMAIN   = Orders
EX2_BADGES   = Arithmetic, print()
EX2_TASK     = A customer is buying a jacket that costs $80. The shop is running a 25% discount. Write a Python program that stores the original price and the discount rate as variables, calculates the final price, and prints the result.
EX2_FILENAME = discount_calc.py
EX2_CODE     = original_price = 80             # full price of the jacket
               discount_rate = 0.25            # 25% off
               discounted_price = original_price * (1 - discount_rate)  # calculate final price
               print("Final price:", discounted_price)                   # display the result
EX2_CMD      = $ python discount_calc.py
EX2_OUTPUT   = Final price: 60.0
EX2_TIP      = Python evaluates the right side of the = first, stores the result in discounted_price, and then uses that value when printing — this same sequence happens every time a checkout system applies a discount.

EX3_TAB      = Total Item Prices
EX3_TITLE    = Total Item Prices
EX3_DOMAIN   = Customers
EX3_BADGES   = Arithmetic, print()
EX3_TASK     = A customer bought three books priced at $12, $25, and $8. Write a Python program that stores each price in its own variable, adds them together to get the total, and prints the final amount.
EX3_FILENAME = basket_total.py
EX3_CODE     = book_1 = 12                             # price of the first book
               book_2 = 25                             # price of the second book
               book_3 = 8                              # price of the third book
               basket_total = book_1 + book_2 + book_3 # add all three prices
               print("Total:", basket_total)           # display the result
EX3_CMD      = $ python basket_total.py
EX3_OUTPUT   = Total: 45
EX3_TIP      = Storing each price in its own variable makes the program easy to read and update — if a price changes, you only need to edit one number and the total recalculates automatically.
```
