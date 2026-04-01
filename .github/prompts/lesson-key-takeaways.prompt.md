---
mode: "agent"
description: "Write or rewrite the #key-ideas (Key Takeaways) section for a lesson HTML file"
---

Rewrite the `#key-ideas` section body in the target lesson file using the rules below.

---

## Writing Style — apply to all text you write

This content is for people who are new to programming. Write as if you're explaining to a colleague who is smart but has never written a line of code.

- **Use plain English.** Avoid jargon unless the term was taught in this lesson. If you use a technical term, define it in the same sentence.
- **Short sentences win.** Aim for 15 words or fewer. One idea per sentence — no chaining with "and" or "which".
- **Be direct.** Use "you" and "your". Say what a concept *does for the reader*, not what it *is* in the abstract.
- **Concrete over abstract.** Compare to something familiar: a formula in Excel, a column in a spreadsheet, copying a cell.
- **No filler.** Cut "it is important", "essentially", "in order to", "as you can see".
- **American English only.** Use American spellings throughout — e.g. "optimize" not "optimise", "color" not "colour", "analyze" not "analyse".

---

## Inputs (fill in before running)

| Variable | Value |
|---|---|
| `TARGET_FILE` | Path to the lesson HTML file |
| `OVERVIEW_TOPICS` | Comma-separated list of topics already covered in the #overview section — Key Takeaways must NOT repeat any of these |
| `TAKEAWAY_1_TITLE` | Short title for card 1 (≤5 words) |
| `TAKEAWAY_1_DESC` | One-sentence description for card 1 |
| `TAKEAWAY_1_PILLS` | 3 keyword pills for card 1 |
| `TAKEAWAY_2_TITLE` | Short title for card 2 |
| `TAKEAWAY_2_DESC` | Description for card 2 |
| `TAKEAWAY_2_PILLS` | 3 keyword pills for card 2 |
| `TAKEAWAY_3_TITLE` | Short title for card 3 |
| `TAKEAWAY_3_DESC` | Description for card 3 |
| `TAKEAWAY_3_PILLS` | 3 keyword pills for card 3 |

---

## Rules

### No repetition
Before writing any card content, review `OVERVIEW_TOPICS`. Each takeaway must cover **new ground** not already explained in #overview. The purpose of this section is to deepen understanding, not restate it.

Good progression patterns:
- Overview explained *what* something is → Takeaway explains *why it matters* or *when to use it*
- Overview used an analogy → Takeaway contrasts with a tool the learner already knows (Excel, SQL)
- Overview showed the concept at a high level → Takeaway shows the practical implication

### Card titles
- Maximum 5 words
- Phrase as a statement or verb phrase, not a question
- Examples: "Programs Are Sets of Instructions", "Programming Automates Work", "Programs Can Make Decisions"

### Card descriptions
- One complete sentence — subject, verb, object
- Target 20–30 words
- Must reference something concrete: a specific tool (Excel, SQL), a real task (copy-pasting, reformatting), or a measurable outcome
- Never use the same verb as the Overview section for the same concept

### Keyword pills
- 3 pills per card
- Short (1–3 words each)
- Match the card's accent color

### Color scheme (one per card, in order)
1. **Pink** — `obj-card-kt`, `from-[#CB187D] to-[#e84aad]`, pink pills
2. **Violet** — `obj-card-violet`, `from-violet-500 to-purple-600`, violet pills
3. **Blue** — `obj-card-blue`, `from-blue-500 to-indigo-600`, blue pills

### Card design & hover effects (CSS-driven, not Tailwind)
Do NOT add any Tailwind hover classes to the card `<div>` elements. All design and hover behavior is handled entirely by CSS. The full required CSS block is below — verify it exists in the `<style>` block of `TARGET_FILE`. If any rule is missing, add the entire block in the `Card hover animations` section of the stylesheet.

```css
/* ── Card hover animations — Key Takeaways cards ───────────────── */
.obj-card {
  transition: transform 0.22s cubic-bezier(.4,0,.2,1),
              box-shadow 0.22s cubic-bezier(.4,0,.2,1),
              border-color 0.22s ease, background-color 0.22s ease;
}
.obj-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 14px 32px -6px rgba(203,24,125,0.18), 0 6px 12px -2px rgba(203,24,125,0.1);
  border-color: #CB187D;
  background-color: #fdf0f7;
}
.obj-card .obj-icon {
  transition: transform 0.22s cubic-bezier(.4,0,.2,1), background-color 0.22s ease;
}
.obj-card:hover .obj-icon { transform: scale(1.1); background-color: #CB187D; }
.obj-card:hover .obj-icon .iconify { color: white !important; }
.obj-card-kt:hover    { box-shadow: none; background-color: #ffffff; border-color: #CB187D; }
.obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; background-color: #ffffff; }
.obj-card-blue:hover   { border-color: #3b82f6; box-shadow: none; background-color: #ffffff; }
```

**Per-color card border — resting state:**
- Pink card `obj-card-kt` → `border border-gray-100`
- Violet card `obj-card-violet` → `border border-violet-100`
- Blue card `obj-card-blue` → `border border-blue-100`

**On hover, CSS overrides the border color:**
- Pink → `#CB187D` (brand pink)
- Violet → `#8b5cf6`
- Blue → `#3b82f6`

The `box-shadow: none` on each variant suppresses the default pink glow so each color card gets a clean colored-border lift with no conflicting shadow tint.

**Important:** Each variant also sets `background-color: #ffffff` to prevent the base `.obj-card:hover` rule's pink background (`#fdf0f7`) from bleeding through. Key Takeaway cards must stay white on hover — only the border color changes.

---

## What NOT to change
- The `<section id="key-ideas">` outer wrapper and section header must stay exactly as they are
- Do not touch anything outside `<section id="key-ideas">` … `</section>`
- Do not change the section header icon (`fa6-solid:lightbulb`), title ("Key Takeaways"), or subtitle

---

## Output structure

Replace the entire `<div class="bg-white px-8 py-7 space-y-4">` … `</div>` body inside `#key-ideas` with exactly 3 cards using the structure below. Use a Python script to perform the replacement via string anchoring (not line numbers).

```html
<div class="bg-white px-8 py-7 space-y-4">

<div class="obj-card obj-card-kt rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="ICON_1"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">TITLE_1</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">DESC_1</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">PILL_1A</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">PILL_1B</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">PILL_1C</span>
    </div>
  </div>
</div>

<div class="obj-card obj-card-violet rounded-2xl border border-violet-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="ICON_2"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">TITLE_2</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">DESC_2</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">PILL_2A</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">PILL_2B</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">PILL_2C</span>
    </div>
  </div>
</div>

<div class="obj-card obj-card-blue rounded-2xl border border-blue-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="ICON_3"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">TITLE_3</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">DESC_3</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">PILL_3A</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">PILL_3B</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">PILL_3C</span>
    </div>
  </div>
</div>

</div>
```
