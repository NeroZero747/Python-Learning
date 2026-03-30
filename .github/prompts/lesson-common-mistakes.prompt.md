---
mode: "agent"
description: "Write or rewrite the #mistakes section for a lesson HTML file — descriptive tab labels, explanation paragraph, Incorrect/Correct split-panel code comparison, and amber tip footer."
---

Rewrite the `#mistakes` section body in the target lesson file using the structure and rules below. The design — tab pills, card header, explanation paragraph, red/emerald split panel, arrow divider, and amber tip — stays the same every lesson; only the content changes.

---

## Writing Style — apply to all text you write

This content is for people who are new to programming. Write as if you're explaining a mistake to a colleague — clearly and without blame.

- **Lead with the error, not the story.** State what Python does (or what breaks) in the first sentence. Don't start with "It's easy to…" or "Many beginners…".
- **Name the exact error.** Say `SyntaxError`, `IndentationError`, or "Python prints nothing" — not "this causes a problem".
- **Explain the fix in one sentence.** Tell the reader exactly what to change.
- **Short sentences.** 15 words or fewer. One idea per sentence.
- **No jargon without definition.** If you mention a technical term, say what it means in the same sentence.
- **No filler.** Cut "it is important", "please note", "essentially", "in order to".

---

## Inputs (fill in before running)

| Variable | Value |
|---|---|
| `TARGET_FILE` | Path to the lesson HTML file |
| `TOPIC` | The Python concept the mistakes relate to (e.g. `variables`, `print statements`, `conditions`, `loops`) |
| `MK_COUNT` | Number of mistakes (typically 3; add more for advanced lessons) |
| `MK1_TAB` | Short tab pill label for mistake 1 — 2–4 words naming the error behavior (e.g. `Writing Plain English`, `Forgetting print()`, `Wrong Indentation`) |
| `MK1_TITLE` | Panel card heading — full phrase describing the mistake (e.g. `Writing Instructions in Plain English Instead of Python Syntax`) |
| `MK1_SUBTITLE` | One-sentence card subheading — state the consequence of the mistake (e.g. `Python only reads precise, structured code — natural language phrases cause a SyntaxError.`) |
| `MK1_EXPLANATION` | 1–2 sentence paragraph placed above the code panels. State the rule or error directly, name the exact consequence (error type or silent failure), and give the one-line fix. Use inline `<code>` tags for code references. |
| `MK1_WRONG_LABEL` | Short label for the red (wrong) panel, after the ✗ badge (e.g. `plain English`, `no output shown`, `result discarded`) |
| `MK1_WRONG_CODE` | Wrong code snippet. HTML-encode `<`, `>`, `&`, `"` as `&lt;`, `&gt;`, `&amp;`, `&quot;`. Use clear, meaningful variable names that match the lesson's context. |
| `MK1_CORRECT_LABEL` | Short label for the green (correct) panel, after the ✓ badge (e.g. `Python syntax`, `use print()`, `assign to a variable`) |
| `MK1_CORRECT_CODE` | Correct code snippet. Same encoding rules as wrong code. |
| `MK1_TIP` | Amber tip text — 1–2 complete sentences. Anchor the fix to a real-world analogy or a relatable workflow. Do not repeat the explanation paragraph. |
| `MK2_TAB` | Tab pill label for mistake 2 |
| `MK2_TITLE` | Card heading for mistake 2 |
| `MK2_SUBTITLE` | Card subheading for mistake 2 |
| `MK2_EXPLANATION` | 1–2 sentence explanation for mistake 2 |
| `MK2_WRONG_LABEL` | Red panel label for mistake 2 |
| `MK2_WRONG_CODE` | Wrong code for mistake 2 |
| `MK2_CORRECT_LABEL` | Green panel label for mistake 2 |
| `MK2_CORRECT_CODE` | Correct code for mistake 2 |
| `MK2_TIP` | Amber tip for mistake 2 |
| `MK3_TAB` | Tab pill label for mistake 3 |
| `MK3_TITLE` | Card heading for mistake 3 |
| `MK3_SUBTITLE` | Card subheading for mistake 3 |
| `MK3_EXPLANATION` | 1–2 sentence explanation for mistake 3 |
| `MK3_WRONG_LABEL` | Red panel label for mistake 3 |
| `MK3_WRONG_CODE` | Wrong code for mistake 3 |
| `MK3_CORRECT_LABEL` | Green panel label for mistake 3 |
| `MK3_CORRECT_CODE` | Correct code for mistake 3 |
| `MK3_TIP` | Amber tip for mistake 3 |

> For `MK_COUNT` > 3, repeat all `MK_N_*` variables and panel blocks for each additional mistake. Add its tab pill button (dark gray, no active class) and its `<div class="mk-panel mk-panel-anim hidden">` panel.

---

## When the wrong/correct comparison does NOT apply

Some mistakes are conceptual rather than syntactic — for example, misunderstanding order of execution, or confusing data types. For those, replace the split panel with a single-column explanation block:

```html
<div class="px-6 pb-5">
  <div class="rounded-xl overflow-hidden bg-code">
    <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
      <div class="flex items-center gap-2">
        <span class="iconify text-gray-400" data-icon="fa6-solid:terminal" data-width="12" data-height="12"></span>
        <span class="text-[11px] font-semibold text-gray-400">FILENAME.py</span>
      </div>
      <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
    </div>
    <pre class="overflow-x-auto pre-reset"><code class="language-python">CODE_HERE</code></pre>
  </div>
</div>
```

Use this single-column block when the mistake is about *what happens at runtime* rather than *what was typed incorrectly*. Prefer the split panel whenever a direct wrong/correct comparison is possible — which is the case for most beginner mistakes.

---

## Section shell (keep unchanged)

Always preserve the outer section shell exactly — do **not** change the section `id`, the header icon (`fa6-solid:triangle-exclamation`), the header title ("Common Mistakes"), or the subtitle. Only replace the `<div class="bg-white px-8 py-7 space-y-6">` body contents.

```html
<section id="mistakes">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:triangle-exclamation"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Common Mistakes</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Pitfalls beginners hit when working with TOPIC</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <!-- TAB ROW + PANELS GO HERE -->
    </div>
  </div>
</section>
```

---

## Tab pill row

The first tab is active (pink gradient). All other tabs start dark gray. Tab labels use `MK_N_TAB` values — never "Mistake 1", "Mistake 2", etc.

```html
<div class="flex items-center gap-2 mb-6" role="tablist">
  <button onclick="switchMkTab(0)" class="mk-step mk-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
    <span class="mk-step-label text-xs font-bold">MK1_TAB</span>
  </button>
  <button onclick="switchMkTab(1)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
    <span class="mk-step-label text-xs font-bold">MK2_TAB</span>
  </button>
  <button onclick="switchMkTab(2)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
    <span class="mk-step-label text-xs font-bold">MK3_TAB</span>
  </button>
</div>
```

---

## Mistake panel template (repeat for each mistake)

The first panel has no `hidden` class. All subsequent panels have `class="mk-panel mk-panel-anim hidden"`.

```html
<div class="mk-panel mk-panel-anim [hidden for panels 2+]" role="tabpanel">
  <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

    <!-- Card header -->
    <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
        <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
      </span>
      <div class="min-w-0 flex-1">
        <h4 class="font-bold text-gray-800 text-sm">MK_N_TITLE</h4>
        <p class="text-xs text-gray-500 mt-0.5">MK_N_SUBTITLE</p>
      </div>
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
        <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
      </span>
    </div>

    <!-- Explanation paragraph -->
    <div class="px-6 py-5">
      <p class="text-sm text-gray-600 leading-relaxed">MK_N_EXPLANATION</p>
    </div>

    <!-- Wrong / Correct split panel -->
    <div class="relative grid grid-cols-1 sm:grid-cols-2">
      <div class="p-5 bg-red-50/30">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — MK_N_WRONG_LABEL
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">MK_N_WRONG_CODE</code></pre>
        </div>
      </div>
      <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
        <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
          <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
        </span>
      </div>
      <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — MK_N_CORRECT_LABEL
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">MK_N_CORRECT_CODE</code></pre>
        </div>
      </div>
    </div>

    <!-- Amber tip footer -->
    <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
      <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
      <p class="text-xs text-gray-600 leading-relaxed">MK_N_TIP</p>
    </div>

  </div>
</div>
```

---

## Content rules

### Tab labels
- Always descriptive: name the *behavior* the learner got wrong (e.g. `Writing Plain English`, `Forgetting print()`, `Losing the Result`).
- Never use "Mistake 1", "Mistake 2", "Mistake N".
- Keep to 2–4 words so the pill doesn't wrap.

### Card subtitle
- One sentence stating the direct consequence of the mistake (what Python does, what error is thrown, what goes missing). Start with a capital letter, end with a period.

### Explanation paragraph
- **1–2 sentences maximum.** Front-load the rule or error: state what Python does (or doesn't do), name the exact error raised or silent failure, then give the one-line fix.
- Pattern: *"[What Python does / rule broken] — `wrong_code` [does X], so [consequence]. [Fix sentence]"*
- Do **not** open with scene-setting or empathy phrases like "It is natural to…" or "After fixing…" — get straight to the error.
- The card subtitle above already names the consequence; the explanation adds the *why* and the *fix*, not a restatement.
- Use `<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">VALUE</code>` for inline code references.
- Write in second person ("you", "your") only when needed — impersonal phrasing ("Python treats…", "writing X raises…") is preferred for brevity.

### Wrong / Correct code panels
- Code blocks use **Style B-lite**: outer div is `rounded-xl overflow-hidden bg-code` (no `shadow-md`, no header bar). Code appears directly with `<pre class="overflow-x-auto pre-reset px-4 py-3">` — **never** add a `border-b border-code-sep` header inside the split panels.
- For the single-column conceptual block (when no split panel applies), use `rounded-xl overflow-hidden bg-code` with the `border-b border-code-sep` header — but **no traffic-light dots** (`w-2.5 h-2.5 rounded-full` elements) anywhere in that header.
- **Never** use `border border-gray-800 shadow-lg` or `bg-[#181825]` — those are the `#code-examples` dark-chrome style and do not belong here.
- Use `language-python` for Python samples and `language-bash` for terminal commands. Change the class if the lesson's examples are SQL or bash.
- Keep each code snippet to **1–5 lines** — just enough to show the mistake and its fix clearly. Don't add unrelated lines.
- **No step-header comment dividers.** Never use `# ── Step 1: …` style headers inside snippets.
- **No `if __name__ == "__main__"` guard** — snippets are always top-level code fragments.
- Every line in the **correct** panel should have a `# inline comment` explaining what it does.
- Use meaningful, descriptive snake_case variable names: `item_price`, `discount_rate`, `total_cost`, `student_name`, `order_count`, etc. Never use generic names like `a`, `b`, `x`, `result`.
- HTML-encode these characters inside `<code>` blocks: `<` → `&lt;`, `>` → `&gt;`, `&` → `&amp;`, `"` → `&quot;`.

### Amber tip
- 1–2 complete sentences only.
- Give a concrete analogy or a real-world connection the reader will recognize — don't repeat the explanation.
- Inline `<code>` tags may be used: `<code class="font-mono bg-amber-100 px-1 rounded text-[11px]">VALUE</code>`.

### Progression across mistakes
- Mistake 1 should be the most common beginner error for the topic (conceptual or syntactic).
- Mistake 2 should be a follow-on consequence that often appears after fixing Mistake 1.
- Mistake 3 should be a subtler, easy-to-miss error that even slightly experienced beginners hit.

---

## Quality checklist

Before finalising the section, verify:

- [ ] All tab labels are descriptive — no "Mistake N" labels anywhere
- [ ] Explanation paragraph appears above the split panel in every card
- [ ] Split panels use `bg-red-50/30` (wrong) and `bg-emerald-50/30` (correct)
- [ ] Pink arrow circle divider (`fa6-solid:arrow-right`) is between the two panels
- [ ] Panel 1 has no `hidden` class; panels 2+ each have `hidden`
- [ ] All code uses meaningful, descriptive variable names — no `a`, `b`, `x`, `result`
- [ ] Each wrong and correct snippet is **5 lines or fewer**
- [ ] No step-header comment dividers (`# ── Step 1:` etc.) inside any snippet
- [ ] No `if __name__ == "__main__"` guard in any snippet
- [ ] `<`, `>`, `&`, `"` are HTML-encoded inside all `<code>` blocks
- [ ] No traffic-light dots in any code block header (no `<span class="w-2.5 h-2.5 rounded-full …">` elements)
- [ ] Wrong/correct mini-blocks have **no** `border-b border-code-sep` header bar — code sits directly inside `bg-code` with `px-4 py-3` on `<pre>`
- [ ] Every correct code panel has inline `# comments`
- [ ] Amber tip does not repeat the explanation paragraph
- [ ] `switchMkTab(i)` index matches the panel order (0, 1, 2, …)
- [ ] Outer section shell (`id="mistakes"`, header icon, title) is unchanged

---

## Reference example (lesson01_what_is_programming.html)

**TOPIC:** `variables and print statements`  
**MK_COUNT:** 3

| # | `MK_N_TAB` | `MK_N_TITLE` |
|---|---|---|
| 1 | Writing Plain English | Writing Instructions in Plain English Instead of Python Syntax |
| 2 | Forgetting print() | Assigning a Value Without Displaying It |
| 3 | Losing the Result | Calculating Without Storing the Result |

**Mistake 1**
- Wrong: `Calculate 10% discount on the price` (plain English → SyntaxError)
- Correct: `discount = item_price * 0.10`
- Tip: "Think of Python as a very literal assistant — it does exactly what you type, nothing more."

**Mistake 2**
- Wrong: `item_price = 80` / `discount = item_price * 0.10` with no `print()` — runs silently, no output
- Correct: same two lines + `print(discount)  # Displays: 8.0`
- Tip: "`print()` is the 'publish' button — the variable is calculated silently, and `print()` sends the result to your screen."

**Mistake 3**
- Wrong: `item_price * 0.10  # Calculated, then lost` (no assignment → answer discarded)
- Correct: `discount = item_price * 0.10  # Saved for later`
- Tip: "Every result you'll need later must be saved to a variable — like writing on a whiteboard instead of immediately erasing it."
