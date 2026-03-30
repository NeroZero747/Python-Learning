---
mode: "agent"
description: "Write or rewrite the #recap section for a lesson HTML file — a 2×2 grid of recap cards that exactly mirror the four lesson objectives, followed by a 'Lesson Complete!' completion banner. Each card uses the same label and icon as its corresponding objective card so the lesson comes full circle."
---

Rewrite the `#recap` section body in the target lesson file using the structure and rules below. The recap must be a direct reflection of the lesson's `#objective` section — same four labels, same four icons, one short sentence per card that summarises what the learner covered. The design stays the same every lesson; only the content changes.

---

## Writing Style — apply to all text you write

The recap is the reader's moment of "I got it". Keep sentences short, confident, and concrete.

- **State what they can now do.** Not "variables are containers" — but "you can name a value and use it throughout your script".
- **8–14 words per sentence.** Short is better. These sit under a small uppercase label, so brevity matters.
- **No jargon** unless the word was the core thing they just learned (e.g. the lesson was about `for` loops — using "loop" is fine).
- **One idea per card.** Don't cram two points into one sentence.
- **No filler.** Cut "it is important", "as you can see", "essentially".

---

## Critical rule — recap must mirror objectives

Before writing any content, read the `#objective` section of the target lesson file and extract:
- The **label** on each of the 4 objective cards (the small uppercase text)
- The **Iconify icon** used on each card
- The **core idea** stated in the card's one-line description

The 4 recap cards must use **identical labels and icons** to those 4 objective cards. This creates a deliberate "full circle" moment for the learner — they arrive at the recap and recognize exactly what they set out to learn.

---

## Inputs (fill in before running)

| Variable | Value |
|---|---|
| `TARGET_FILE` | Path to the lesson HTML file |
| `TOPIC` | The Python concept this lesson teaches (e.g. `variables`, `conditions`, `loops`, `functions`) |
| `CARD1_LABEL` | Label text from objective card 1 — copy exactly, same capitalisation |
| `CARD1_ICON` | Iconify icon from objective card 1 (e.g. `fa6-solid:list-ol`) |
| `CARD1_SENTENCE` | One short sentence (max 20 words) summarising what the learner now knows about card 1's topic. Should be concrete — state what they can *do*, not just what it *is*. Real-world examples welcome. |
| `CARD2_LABEL` | Label text from objective card 2 — copy exactly |
| `CARD2_ICON` | Iconify icon from objective card 2 |
| `CARD2_SENTENCE` | One short sentence for card 2 |
| `CARD3_LABEL` | Label text from objective card 3 — copy exactly |
| `CARD3_ICON` | Iconify icon from objective card 3 |
| `CARD3_SENTENCE` | One short sentence for card 3 |
| `CARD4_LABEL` | Label text from objective card 4 — copy exactly |
| `CARD4_ICON` | Iconify icon from objective card 4 |
| `CARD4_SENTENCE` | One short sentence for card 4 |
| `CONCEPT_COUNT` | Always `4` (matches the 4 objective cards) |

---

## Writing rules for recap sentences

- **One sentence per card.** No more. No sub-bullets.
- **Keep it short** — aim for 8–14 words. The description sits below a small uppercase label at `text-[11px]`, so brevity is critical.
- **State what the learner can now do or what the concept does**, not just what the term means. Start with an action verb, a clear subject, or the term itself used in a sentence.
- Inline `<code class="font-mono">` tags are encouraged for type names, operators, and function calls (e.g. `<code class="font-mono">type()</code>`, `<code class="font-mono">=</code>`, `<code class="font-mono">str</code>`).
- **Keep context grounded** where it fits naturally. Never force a domain reference that sounds awkward.
- **Do not repeat the label word-for-word** in the sentence — rephrase to add value.

---

## Section shell (keep unchanged)

Always preserve the outer section shell exactly — do **not** change the section `id`, the header icon (`fa6-solid:list-check`), or the header title ("Lesson Recap"). Only replace the `<div class="bg-white px-8 py-7 space-y-6">` body contents.

```html
<section id="recap">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:list-check"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Lesson Recap</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">A quick summary of what you learned</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <!-- 2×2 CARD GRID + COMPLETION BANNER GO HERE -->
    </div>
  </div>
</section>
```

---

## Card grid template (repeat for cards 01–04)

Each card uses a watermark number (`01`, `02`, `03`, `04`), the objective's icon, the objective's label as the small uppercase heading, and one recap sentence.

```html
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">

  <!-- Card 01 -->
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
      <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
      <div class="relative flex items-start gap-3">
        <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
          <span class="iconify text-sm" data-icon="CARD1_ICON"></span>
        </span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">CARD1_LABEL</p>
          <p class="text-[11px] text-gray-600 leading-snug">CARD1_SENTENCE</p>
        </div>
      </div>
    </div>
  </div>

  <!-- Card 02 — same structure, watermark "02", CARD2_* values -->
  <!-- Card 03 — same structure, watermark "03", CARD3_* values -->
  <!-- Card 04 — same structure, watermark "04", CARD4_* values -->

</div>
```

---

## Completion banner (always last inside the body div)

Always include this banner immediately after the card grid, inside the same `<div class="bg-white px-8 py-7 space-y-6">`. The text "You've covered N key concepts." uses the `CONCEPT_COUNT` value (always `4`).

```html
<div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">
  <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">&#10003;</span>
  <div class="relative flex items-center gap-4">
    <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">
      <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>
    </span>
    <div>
      <p class="text-sm font-bold text-white">Lesson Complete!</p>
      <p class="text-xs text-white/80 mt-0.5">You&#39;ve covered CONCEPT_COUNT key concepts. Ready for the knowledge check?</p>
    </div>
  </div>
</div>
```

---

## Quality checklist

Before submitting the rewritten section, verify:

- [ ] Each card label is an **exact copy** of the corresponding objective card label (same words, same capitalisation)
- [ ] Each card icon (`data-icon`) is an **exact match** to the corresponding objective card icon
- [ ] Every sentence is 8–14 words and starts with a capital letter
- [ ] No sentence repeats the label verbatim — it rephrases and adds value
- [ ] Inline `<code class="font-mono">` used for type names, operators, and function calls where appropriate
- [ ] Watermark numbers run `01` → `02` → `03` → `04` in DOM order
- [ ] Completion banner is the last element inside the body `div`, after the grid
- [ ] Section `id`, header icon, and header title are unchanged
