---
mode: "agent"
description: "Write or rewrite the #real-world section for a lesson HTML file — intro paragraph, three large scenario cards, and a two-column before/after comparison table. No code blocks."
---

Rewrite the `#real-world` section body in the target lesson file using the structure and rules below. The design — intro paragraph, three large scenario cards, and a before/after comparison table — stays the same every lesson; only the content changes.

---

## Writing Style — apply to all text you write

This section shows the reader why the lesson topic matters in real work. Write like you're pointing at a real task on someone's desk and saying "this is where Python helps you."

- **Be specific.** Name real quantities, data types, and actions — not vague capabilities.
- **Human scale.** Lead with relatable numbers or situations ("500 orders", "200 products", "a 10% sale") so the reader feels the weight of the problem before seeing the solution.
- **Use "you".** "You write the function once" is clearer than "the function is written once".
- **One idea per sentence.** 15 words or fewer per sentence. No compound justifications.
- **No jargon** unless it was taught in this lesson.
- **No filler.** Cut "it is important", "essentially", "in order to", "this allows for".
- **No code blocks** anywhere in this section — all content is plain English.

---

---

## Inputs (fill in before running)

| Variable | Value |
|---|---|
| `TARGET_FILE` | Path to the lesson HTML file |
| `TOPIC` | The Python concept this lesson teaches (e.g. `variables`, `conditions`, `loops`, `functions`) |
| `DOMAIN` | The real-world setting for the three scenario cards (e.g. `an online shop`, `a data team`, `a payroll system`). Pick something universally familiar — avoid sports, music, or domain-specific jargon. |
| `INTRO_TEXT` | 2–3 sentence intro paragraph. Set the scene using `DOMAIN`, name the repeated pain the learner faces without `TOPIC`, and end with one sentence on how `TOPIC` solves it. |
| `CARD1_ICON` | Iconify icon for scenario card 1 (e.g. `fa6-solid:receipt`) |
| `CARD1_COLOR` | Tailwind color token for card 1 — one of: `violet`, `pink`, `emerald`, `blue`, `amber` |
| `CARD1_HEADLINE` | Short human-scale headline for card 1 (e.g. `Your shop gets 500 orders today`) — 6–10 words, no verb "is/are" |
| `CARD1_BODY` | 2 plain sentences. Sentence 1: the problem at scale. Sentence 2: how the function (or concept) solves it with one verb of action. |
| `CARD1_FUNCTION` | The Python function or variable name featured in card 1 (e.g. `calculate_total()`) |
| `CARD1_RETURNS` | What the function returns or produces shown in the pill (e.g. `order_total`, `True or False`) |
| `CARD2_ICON` | Iconify icon for scenario card 2 |
| `CARD2_COLOR` | Tailwind color token for card 2 |
| `CARD2_HEADLINE` | Short human-scale headline for card 2 |
| `CARD2_BODY` | 2 plain sentences matching the card 1 pattern |
| `CARD2_FUNCTION` | Python function or concept name for card 2 |
| `CARD2_RETURNS` | Return value or result for card 2 pill |
| `CARD3_ICON` | Iconify icon for scenario card 3 |
| `CARD3_COLOR` | Tailwind color token for card 3 |
| `CARD3_HEADLINE` | Short human-scale headline for card 3 |
| `CARD3_BODY` | 2 plain sentences matching the card 1 pattern |
| `CARD3_FUNCTION` | Python function or concept name for card 3 |
| `CARD3_RETURNS` | Return value or result for card 3 pill |
| `WITHOUT_ROW1` | One sentence for the "Without functions" column, row 1 — describe the manual pain at the scale stated in `CARD1_HEADLINE`. |
| `WITHOUT_ROW2` | One sentence for the "Without functions" column, row 2 — describe the error/fragility risk tied to card 2. |
| `WITHOUT_ROW3` | One sentence for the "Without functions" column, row 3 — describe the inconsistency risk tied to card 3. |
| `WITH_ROW1` | One sentence for the "With functions" column, row 1 — state how `CARD1_FUNCTION` eliminates the pain. Bold the function name using `<strong class="text-gray-700">`. |
| `WITH_ROW2` | One sentence for the "With functions" column, row 2 — state how `CARD2_FUNCTION` eliminates the error risk. Bold the function name. |
| `WITH_ROW3` | One sentence for the "With functions" column, row 3 — state how `CARD3_FUNCTION` eliminates the inconsistency. Bold the function name. |

> Card colors should visually differ from one another. A good default set is violet → pink → emerald. Never repeat the same color across cards.

---

## Section shell (keep unchanged)

Always preserve the outer section shell exactly — do **not** change the section `id`, the header icon (`fa6-solid:briefcase`), or the header title ("Real-World Use"). Only replace the `<div class="bg-white px-8 py-7 space-y-5">` body contents. Update the subtitle to match the lesson topic.

```html
<section id="real-world">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:briefcase"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Real-World Use</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">How TOPIC is used across real-world workflows</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-5">
      <!-- INTRO + SCENARIO CARDS + BEFORE/AFTER TABLE GO HERE -->
    </div>
  </div>
</section>
```

---

## Intro paragraph

A single `<p>` tag. 2–3 sentences maximum. Set the scene, name the scale of the problem, end with how the lesson concept solves it.

```html
<p class="text-sm text-gray-600 leading-relaxed">INTRO_TEXT</p>
```

---

## Three scenario cards

A 3-column grid of centered cards. Each card has a large gradient icon badge, a human-scale headline, 2 plain sentences, and a "returns" pill at the bottom. Use a different color per card.

**Color token reference** — drives gradient, border, background, and pill classes:

| Token | Card border | Card background | Icon gradient from | Icon gradient to | Icon shadow | Pill bg | Pill border | Pill text |
|---|---|---|---|---|---|---|---|---|
| `violet` | `border-violet-100` | `from-violet-50 via-white to-purple-50` | `from-violet-500` | `to-purple-600` | `shadow-violet-200` | `bg-violet-100` | `border-violet-200` | `text-violet-700` |
| `pink` (brand) | `border-pink-100` | `from-pink-50 via-white to-rose-50` | `from-[#CB187D]` | `to-[#e84aad]` | `shadow-pink-200` | `bg-pink-100` | `border-pink-200` | `text-[#CB187D]` |
| `emerald` | `border-emerald-100` | `from-emerald-50 via-white to-teal-50` | `from-emerald-500` | `to-teal-600` | `shadow-emerald-200` | `bg-emerald-100` | `border-emerald-200` | `text-emerald-700` |
| `blue` | `border-blue-100` | `from-blue-50 via-white to-indigo-50` | `from-blue-500` | `to-indigo-600` | `shadow-blue-200` | `bg-blue-100` | `border-blue-200` | `text-blue-700` |
| `amber` | `border-amber-100` | `from-amber-50 via-white to-orange-50` | `from-amber-400` | `to-orange-500` | `shadow-amber-200` | `bg-amber-100` | `border-amber-200` | `text-amber-700` |

```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-4">

  <!-- Card 1 — CARD1_COLOR -->
  <div class="relative rounded-2xl overflow-hidden border CARD1_BORDER bg-gradient-to-br CARD1_BG px-6 py-6 text-center">
    <div class="flex flex-col items-center gap-3">
      <span class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br CARD1_ICON_FROM CARD1_ICON_TO shadow-lg CARD1_SHADOW">
        <span class="iconify text-white text-2xl" data-icon="CARD1_ICON"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-800 leading-snug">CARD1_HEADLINE</h3>
      <p class="text-xs text-gray-500 leading-relaxed">CARD1_BODY — use inline <code class="font-mono CARD1_CODE_COLOR">CARD1_FUNCTION</code> in the text.</p>
      <div class="flex items-center gap-1.5 mt-1 px-3 py-1.5 rounded-full CARD1_PILL_BG CARD1_PILL_BORDER">
        <span class="iconify CARD1_PILL_TEXT text-[11px]" data-icon="fa6-solid:arrow-right-from-bracket"></span>
        <span class="text-[11px] font-semibold CARD1_PILL_TEXT">returns <code class="font-mono">CARD1_RETURNS</code></span>
      </div>
    </div>
  </div>

  <!-- Card 2 — CARD2_COLOR (repeat structure above) -->

  <!-- Card 3 — CARD3_COLOR (repeat structure above) -->

</div>
```

**Headline rules:**
- Use a real number or quantity ("500 orders", "200 products") to communicate scale.
- Write it as two short lines — break after the scale number using `<br>` so the card stays balanced.
- Never start with "You" — lead with the situation, not the person.

**Body text rules:**
- Sentence 1: state the problem at scale (what would have to happen manually or repeatedly).
- Sentence 2: state how writing the function once solves it — name the function in `<code>` inline.

**Pill rules:**
- The `returns` pill shows what the function produces — use the actual Python value or variable name (`order_total`, `True` or `False`, `sale_price`).
- Use `<code class="font-mono">` around the return value inside the pill span.

---

## Before/After comparison table

A two-column grid inside a `rounded-xl` border container. Left column = "Without [TOPIC]" (red header, ✗ bullets). Right column = "With [TOPIC]" (pink header, ✓ bullets). Each column has exactly 3 rows — one per scenario card above.

```html
<div class="rounded-xl border border-gray-100 overflow-hidden">
  <div class="grid grid-cols-2">

    <!-- Without column -->
    <div class="border-r border-gray-100">
      <div class="flex items-center gap-2 px-4 py-3 bg-red-50 border-b border-red-100">
        <span class="iconify text-red-400 text-sm shrink-0" data-icon="fa6-solid:circle-xmark"></span>
        <p class="text-xs font-bold text-red-500 uppercase tracking-wide">Without TOPIC</p>
      </div>
      <div class="px-4 py-4 space-y-3">
        <div class="flex items-start gap-2.5">
          <span class="iconify text-red-300 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>
          <p class="text-xs text-gray-500 leading-relaxed">WITHOUT_ROW1</p>
        </div>
        <div class="flex items-start gap-2.5">
          <span class="iconify text-red-300 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>
          <p class="text-xs text-gray-500 leading-relaxed">WITHOUT_ROW2</p>
        </div>
        <div class="flex items-start gap-2.5">
          <span class="iconify text-red-300 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>
          <p class="text-xs text-gray-500 leading-relaxed">WITHOUT_ROW3</p>
        </div>
      </div>
    </div>

    <!-- With column -->
    <div>
      <div class="flex items-center gap-2 px-4 py-3 bg-[#fdf0f7] border-b border-[#f5c6e0]">
        <span class="iconify text-[#CB187D] text-sm shrink-0" data-icon="fa6-solid:circle-check"></span>
        <p class="text-xs font-bold text-[#CB187D] uppercase tracking-wide">With TOPIC</p>
      </div>
      <div class="px-4 py-4 space-y-3">
        <div class="flex items-start gap-2.5">
          <span class="iconify text-emerald-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>
          <p class="text-xs text-gray-500 leading-relaxed">WITH_ROW1</p>
        </div>
        <div class="flex items-start gap-2.5">
          <span class="iconify text-emerald-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>
          <p class="text-xs text-gray-500 leading-relaxed">WITH_ROW2</p>
        </div>
        <div class="flex items-start gap-2.5">
          <span class="iconify text-emerald-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>
          <p class="text-xs text-gray-500 leading-relaxed">WITH_ROW3</p>
        </div>
      </div>
    </div>

  </div>
</div>
```

**Before/after content rules:**
- Row N in the "Without" column must pair directly with row N in the "With" column — same card, same concept, flipped perspective.
- "Without" rows describe the manual burden, fragility, or inconsistency at scale.
- "With" rows describe the single action that eliminates it — always bold (`<strong class="text-gray-700">`) the function or concept name.
- Each row is one sentence only. No trailing justifications or compound clauses.
- The "Without TOPIC" header label uses the plain English name of the concept (e.g. `Without functions`, `Without loops`, `Without conditions`).
- Same rule for the "With TOPIC" header.

---

## Completion checklist

- [ ] Outer section shell (`id="real-world"`, briefcase header icon, title) is unchanged
- [ ] Body wrapper uses `space-y-5`
- [ ] Intro paragraph is 2–3 sentences, no code, names the `DOMAIN` and the scale
- [ ] Three scenario cards — different color each, centered layout, `w-14 h-14` icon badge, headline has `<br>` between scale and situation, body names the function in `<code>`
- [ ] Returns pill at the bottom of each card with `fa6-solid:arrow-right-from-bracket` icon
- [ ] Before/after table has exactly 3 rows each side, rows pair 1:1 with the cards above
- [ ] "Without" header is red (`bg-red-50`, `text-red-500`), "With" header is pink (`bg-[#fdf0f7]`, `text-[#CB187D]`)
- [ ] Function names bolded with `<strong class="text-gray-700">` in the "With" column
- [ ] No code blocks anywhere in the section

---

## Reference example (lesson08_functions.html)

**TOPIC:** `functions`  
**DOMAIN:** `an online shop`

**Intro:** "Imagine you run an online shop. Every day you need to calculate totals, apply discounts, and check what's in stock. A function lets you write that rule once and reuse it for every single product or order — no copy-pasting, no mistakes."

**Card 1 (violet) — `fa6-solid:receipt`**
- Headline: "Your shop gets / 500 orders today"
- Body: "You write `calculate_total()` once, pass in the quantity and price, and call it for every order — done in seconds."
- Returns pill: `order_total`

**Card 2 (pink) — `fa6-solid:tag`**
- Headline: "A 10% sale / starts tonight"
- Body: "You write `apply_discount()` once. Every product's sale price is calculated the same way — no editing each row by hand."
- Returns pill: `sale_price`

**Card 3 (emerald) — `fa6-solid:boxes-stacked`**
- Headline: "200 products, / one stock check"
- Body: "You write `is_in_stock()` once. It checks each product's stock level and tells you yes or no — for all 200 products at once."
- Returns pill: `True or False`

**Before/After rows:**
| Row | Without functions | With functions |
|---|---|---|
| 1 | You manually calculate the total for every single order — 500 orders means 500 calculations done by hand. | Write **calculate_total()** once. Call it for every order — all 500 are processed the same way in seconds. |
| 2 | One typo in the discount formula means every price on the site is wrong — and you have to fix each one separately. | Fix the discount logic in one place inside **apply_discount()** and every price on the site updates instantly. |
| 3 | Checking 200 products for stock means repeating the same logic 200 times with no guarantee it's consistent. | **is_in_stock()** runs the exact same check every time — no inconsistency, no guesswork, no repeated logic. |
