---
mode: agent
description: "Lesson quality audit — checks every section of an existing lesson for completeness, consistency, and uniqueness. Ensures all objectives are reflected in Overview (with rich card content), Key Takeaways (insight-assertion cards in 2-col grid), Key Concepts (deep tabs per concept), Comparison, Recap, and banner count. Expands Code Examples, Practice, Common Mistakes, and Knowledge Check to up to 5 tabs each. Eliminates cross-section duplicate explanations so each section teaches something the others do not. Fixes duplicate KC tabs, missing icons, KC panel color consistency, and hover styles."
---

Run a full quality audit on `TARGET_FILE` and fix every issue found in place. Do not create a separate report file.

---

## Required Input

| Variable | Value |
|---|---|
| `TARGET_FILE` | Absolute path to the lesson HTML file to audit and fix |

---

## Audit Checklist

Work through each check in order. For each one: read the current HTML, identify any gap or inconsistency, fix it immediately, then confirm by re-reading the affected HTML.

---

### Check 1 — Objective cards vs lesson content

**Goal:** Every concept the lesson teaches must have its own objective card.

1. Read all objective cards (`#objective` section). Extract each card's goal title and description.
2. Read the Overview, Key Concepts, and Code Examples sections to understand every concept the lesson actually covers.
3. If a concept is covered in the lesson but has no matching objective card, **add a new `obj-card`** using this pattern:

```html
<div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
  <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
    <span class="iconify text-brand text-lg" data-icon="ICON_NAME"></span>
  </span>
  <div>
    <p class="text-sm font-semibold text-gray-800">Goal title</p>
    <p class="text-xs text-gray-500 mt-0.5">One-line supporting detail</p>
  </div>
</div>
```

**Icon rules:** Use an icon that matches the concept — `ph:brackets-curly` for JSON, `fa6-solid:file-lines` for Excel/files, `fa6-solid:file-arrow-down` for CSV/loading, `fa6-solid:eye` for preview/inspect, `fa6-solid:triangle-exclamation` for errors/warnings. Verify the icon exists on [Iconify](https://iconify.design) before using it.

---

### Check 2 — Hero "Learning Goals" pill count

**Goal:** The hero stat pill that shows the number of learning goals must match the actual objective card count.

1. Count the objective cards from Check 1 (after any additions).
2. Search the hero section for the pill that contains "Learning Goals" or "Goals".
3. If the number in the pill does not match the card count, update it.

The pill text typically looks like: `<span>N</span><span class="...">Learning Goals</span>`

---

### Check 3 — Overview cards — presence and depth

**Goal:** Every objective must have a concept card in the `#overview` section, and every card must be rich enough to genuinely help a beginner understand the concept before seeing code.

#### 3a — Card presence
1. List all objective titles (from Check 1).
2. List all overview analogy cards (the `rounded-xl border border-gray-100 bg-gray-50` cards in the overview grid).
3. For every objective that has no matching overview card, add one following the template pattern from `copilot-instructions.md` (Part 3 — Analogy card grid). Match the analogy domain already used in the section.

#### 3b — Card content depth
For **every existing overview card**, check all content requirements below. If any are missing or thin, rewrite that part of the card in place:

1. **Icon** — A `data-icon` attribute is present and references a real Iconify icon that visually represents the concept.
2. **Bold title** — The card has a `text-sm font-bold` title that states the concept name clearly (e.g. `read_csv()`, `DataFrame`, `Series`).
3. **Italic analogy subtitle** — A `text-[10px] text-gray-400 italic` line connects the concept to the analogy introduced in the overview intro paragraph. The subtitle must say what the real-world item *does*, not just name it (e.g. `"The pantry — stocked with 500,000+ libraries"`).
4. **Explanation paragraph** — A `text-xs text-gray-500 leading-relaxed` paragraph containing ** a single complete sentence** that:
   - Define the concept in plain English (what it is)
   - Explain what a learner uses it *for* in practice (why it matters)
   - Give one concrete detail — a parameter name, a return type, a common pattern, or a comparison to something familiar (Excel/SQL) that makes the concept tangible

**Content quality rules:**
- Write in second person ("you", "your"). Never use sentence fragments or note-style bullets in the explanation paragraph.
- Do not repeat the analogy subtitle word for word inside the explanation — the subtitle teases, the paragraph teaches.
- If the existing explanation has only one sentence, expand it to a maximum of two sentences.
- If the explanation is vague (e.g. "This is useful for data analysis.") rewrite it with specific, concrete detail.

**Example of a complete, high-quality overview card:**
```html
<div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
  <div class="flex items-center gap-3 mb-2.5">
    <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
      <span class="iconify text-brand text-base" data-icon="fa6-solid:file-arrow-down"></span>
    </span>
    <div>
      <p class="text-sm font-bold text-gray-800 leading-tight">read_csv()</p>
      <p class="text-[10px] text-gray-400 italic leading-tight">The fork-lift — moves raw files straight to your desk</p>
    </div>
  </div>
  <p class="text-xs text-gray-500 leading-relaxed">pd.read_csv() reads a CSV (comma-separated values) file from your disk and returns it as a pandas DataFrame — a table of rows and columns you can immediately query and transform. You pass it a file path as a string and pandas handles all the parsing for you. It also accepts optional parameters like sep= to handle tab-delimited files, encoding= for files with special characters, and header= if your file has no column names on the first row.</p>
</div>
```

---

### Check 4 — Key Takeaways (`#key-ideas`) — presence, format, and content

**Goal:** The `#key-ideas` section must have one card per lesson objective. Each card states a single memorable insight about that concept — not an action label (that belongs in `#objective`) and not a definition (that belongs in `#key-concepts`). The format must match the canonical 2-column grid used across all lessons in the track.

#### 4a — Card presence and count

1. Count the `#key-ideas` takeaway cards (every `obj-card rounded-2xl` div inside the `#key-ideas` section body).
2. Cross-check against the objective list from Check 1. If any objective has no matching takeaway card, add one using the template in 4b below.
3. If there are more takeaway cards than objectives, evaluate whether the extras cover genuinely distinct insights. Remove any card whose insight duplicates another — do not pad the count.

#### 4b — Grid layout and card template

The `#key-ideas` section body wrapper must use this exact structure:

```html
<div class="bg-white px-8 py-7">
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
    <!-- cards -->
  </div>
</div>
```

Each card follows this pattern:

```html
<div class="obj-card rounded-2xl border border-[COLOR]-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-[COLOR]-500 to-[SHADE]-400"></div>
  <div class="px-5 py-5 space-y-3">
    <div class="flex items-center gap-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[COLOR]-500 to-[SHADE]-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="ICON_NAME"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Insight assertion heading</h3>
    </div>
    <p class="text-sm text-gray-600 leading-relaxed">a single complete sentence...</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-[COLOR]-50 text-[COLOR]-600 border border-[COLOR]-100">Keyword</span>
    </div>
  </div>
</div>
```

Assign colors in this order (card 0 = first card):

| Index | Family | `h-1` bar | Icon gradient | Pill classes |
|---|---|---|---|---|
| 0 | pink | `from-[#CB187D] to-[#e84aad]` | `from-[#CB187D] to-[#e84aad]` | `bg-pink-50 text-[#CB187D] border border-pink-100` |
| 1 | violet | `from-violet-500 to-purple-400` | `from-violet-500 to-purple-600` | `bg-violet-50 text-violet-600 border border-violet-100` |
| 2 | blue | `from-blue-500 to-indigo-400` | `from-blue-500 to-indigo-600` | `bg-blue-50 text-blue-600 border border-blue-100` |
| 3 | emerald | `from-emerald-500 to-teal-400` | `from-emerald-500 to-teal-600` | `bg-emerald-50 text-emerald-600 border border-emerald-100` |
| 4 | amber | `from-amber-500 to-orange-400` | `from-amber-500 to-orange-600` | `bg-amber-50 text-amber-600 border border-amber-100` |
| 5 | teal | `from-teal-500 to-cyan-400` | `from-teal-500 to-cyan-600` | `bg-teal-50 text-teal-600 border border-teal-100` |
| 6 | cyan | `from-cyan-500 to-sky-400` | `from-cyan-500 to-sky-600` | `bg-cyan-50 text-cyan-600 border border-cyan-100` |
| 7 | orange | `from-orange-500 to-red-400` | `from-orange-500 to-red-600` | `bg-orange-50 text-orange-600 border border-orange-100` |

**Fixing the old single-column format:** If the current file uses `<div class="bg-white px-8 py-7 space-y-4">` as the body wrapper (cards with `px-6 py-5` inner padding and `text-xs text-gray-600` explanation text), convert it:

1. Replace the body wrapper from `px-8 py-7 space-y-4` to `px-8 py-7`, and wrap all cards in `<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">...</div>`.
2. Change each card's inner body from `<div class="px-6 py-5">` to `<div class="px-5 py-5 space-y-3">`.
3. Remove `mb-3` from the icon header `<div>` and `mb-4` from the explanation `<p>` — `space-y-3` handles all vertical spacing automatically.
4. Change every `text-xs text-gray-600 leading-relaxed` explanation paragraph to `text-sm text-gray-600 leading-relaxed`.

#### 4c — Card content quality

For **every card**, check and fix all of the following:

1. **Heading is an insight assertion** — The heading must not be an action-verb label ("Select a column") nor a plain concept title ("Boolean Mask"). It must state *why the concept matters* or *what it enables* using a noun phrase or short assertion: e.g. "Boolean Masks Leave the Original Data Untouched" or "isin() Replaces Long OR Chains".
2. **Explanation has 2+ complete sentences in `text-sm`** — Write in second person ("you", "your"). Sentence 1 explains what the concept does or why the insight is true. Sentence 2 gives a concrete consequence — what goes wrong without it, an Excel/SQL parallel, or a real-world scenario where it saves time.
3. **2–4 keyword pills per card** — Each pill is a short code token, technique name, or outcome keyword specific to this card. Pill colors must match the card's color family from the table above.
4. **No duplication with other sections** — The heading and explanation must not copy the objective card title, the overview analogy subtitle, or the KC panel intro sentence word for word. If the current heading matches an objective card title exactly, rewrite it as a consequence statement. If the explanation matches KC panel prose, rewrite it to focus on the practical implication or the "gotcha" rather than the definition.

#### 4d — Key Takeaway card hover CSS

**Goal:** Key Takeaway cards in `#key-ideas` must have a distinct hover style — neutral border, white background, and a plain gray shadow — that is visually separate from the pink hover used on objective cards elsewhere. Without this fix the cards flash pink on hover, the icon gradient is overwritten with brand pink, and the shadow is too deep and tinted.

**Step 1 — Inner content div background**

Every card's inner content div must have `bg-white` to block the outer wrapper's hover background from bleeding through:

```html
<div class="px-5 py-5 space-y-3 bg-white">
```

If any card is missing `bg-white` on that div, add it.

**Step 2 — Plain CSS override (inside `<style>`)**

Verify the `<style>` block contains these two rules immediately after the `.obj-card-blue:hover` line:

```css
#key-ideas .obj-card:hover { border-color: #f3f4f6; background-color: #ffffff; box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08); }
#key-ideas .obj-card:hover .obj-icon { transform: scale(1.1); background-color: revert; }
```

The `border-color: #f3f4f6` keeps the border invisible on hover (same as the resting gray-100 tone). `background-color: revert` on `.obj-icon` cancels the forced `#CB187D` override so each card's icon keeps its own gradient color. If these rules are missing or different, add or correct them.

**Step 3 — Hub-root Confluence override**

Verify the `#hub-root` block contains these rules after the standard `.obj-card:hover` override group:

```css
/* ── Key Takeaway cards — keep border gray and icon gradient on hover ── */
#hub-root #key-ideas .obj-card:hover {
  border-color: #f3f4f6 !important;
  background-color: #ffffff !important;
  box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08) !important;
}
#hub-root #key-ideas .obj-card:hover .obj-icon {
  background: revert !important;
}
```

If these rules are missing or different, add or correct them.

#### 4e — Overview vs Key Takeaways deduplication

**Goal:** Every overview card and its matching takeaway card must teach the reader something different. The overview answers "What is this, in plain English?" using an analogy. The takeaway answers "What must I remember?" using a consequence, gotcha, or real-world implication. When both cards say the same facts in different words, the reader gains nothing from reading the second one.

**How to check:**

For every concept that has both an overview card and a takeaway card, compare the two explanations directly:

1. **Extract the core claim** from each card — strip out code, analogies, and qualifiers; boil each explanation down to the single main fact it asserts (e.g. "returns a Series", "original DataFrame is unchanged", "use list() to convert").
2. **Flag any pair** where both cards assert the same main fact, even if the wording differs. Common overlap patterns:
   - Overview says "not a method, no parentheses, returns an Index listing column names" and takeaway says the same.
   - Overview closes with "original DataFrame is never modified" and takeaway opens with the same statement.
   - Overview explains "by default returns a new DataFrame so you must assign the result" and takeaway repeats the assignment requirement.
3. **For every flagged takeaway card**, rewrite it to carry information the overview card does not:
   - If the overview defines the concept → the takeaway should state the consequence of getting it wrong (the bug, the error, the silent failure).
   - If the overview explains the mechanism → the takeaway should explain the real-world scenario where knowing this saves time.
   - If the overview gives the syntax rule → the takeaway should give the debugging technique or the "gotcha" edge case.

**Rewrite rule:** The heading and both sentences of a takeaway card must be true statements that would still make sense if the overview card did not exist. If you find yourself writing the same sentence that's already in the overview, it belongs in the overview — rewrite the takeaway around what happens *next*, or what goes wrong without it.

**Max 2 sentences per takeaway card explanation** — do not expand to 3 sentences to accommodate both the definition and the insight. Cut the definition (it lives in the overview) and keep only the insight.

---

### Check 5 — Key Concepts tabs — deduplication, coverage, and depth

**Goal:** No duplicate KC tabs. Every major concept must have its own KC tab with genuinely educational content.

#### 5a — Deduplication
1. List all KC tab labels.
2. If two or more tabs cover the same concept or very closely related sub-topics, merge them into a single tab with consolidated content. Update all `switchKcTab(i)` index numbers after any removal.

#### 5b — Coverage
3. Cross-check the remaining tabs against the objective list. Every objective must map to at least one KC tab. If a tab is missing, add it.

#### 5c — Tab depth (apply to every tab, new and existing)
For **every KC panel**, check and fix all the following. A panel that fails any item must be rewritten:

1. **Concept intro sentence** — The panel opens with a `text-sm` paragraph that defines the concept in one clear sentence. Format: `"[ConceptName] is [plain-English definition]."`
2. **Code block** — A Style B code block follows, containing a minimal but complete working example (enough lines to show the concept in a realistic context — not just a one-liner unless the concept genuinely is one line).
3. **Code annotations** — Every non-trivial line in the code example has an inline `# comment` that explains what that line does. Do not leave uncommented code.
4. **Parameter table or detail list** — If the concept has key parameters or variants a reader needs to know, include a small table or a `brand-soft-panel` rounded box listing them with a one-line description each.
5. **Tip callout** — End every panel with a `bg-amber-tip` callout containing a practical, specific tip — not a generic statement like "This is useful." The tip should warn about a common mistake OR give a shortcut the reader will actually use.

**Content quality rules for KC panels:**
- Write all prose in complete sentences. No bullet-point fragments.
- Do not pad the explanation — every sentence must add information the previous sentence did not.
- If the existing panel has only a code block and no explanation prose, add the intro sentence, annotations, and tip.
- If the existing panel explanation is one sentence, expand it to cover "what it is", "what you use it for", and "one concrete detail (parameter, return type, or gotcha)".

**Tab count guidance:** There is no fixed maximum for KC tabs — add as many tabs as the topic genuinely requires. If covering a concept properly needs 8 tabs, use 8. Prioritise depth and completeness over a round number.

#### 5d — KC panel color & structure consistency

**Goal:** Every KC tab's HTML color classes must match its assigned `kcColors` JavaScript entry, and every panel must use the canonical `h-1` accent-bar structure. Without this check, panels built at different times cycle between only 3 colors (pink → violet → blue → pink → …) regardless of how many tabs exist, making the UI look inconsistent.

**Step 1 — Verify `kcColors` array length matches tab count**

1. Count the KC tab buttons (`.kc-tab` elements).
2. Find the `kcColors` array in the `<script>` block near the bottom of the file.
3. If `kcColors.length` is less than the tab count, the JS uses `idx % kcColors.length` and **cycles colors** — tabs beyond the array boundary reuse colors from the start. Add one missing entry per extra tab. Choose a color not already used in the array. Standard recommended sequence:

| Index | Hex | Tailwind family | `activeBg` |
|---|---|---|---|
| 0 | `#CB187D` | pink | `#fdf0f7` |
| 1 | `#7c3aed` | violet | `#f5f3ff` |
| 2 | `#2563eb` | blue | `#eff6ff` |
| 3 | `#059669` | emerald | `#ecfdf5` |
| 4 | `#c74905` | orange | `#ffddb3` |
| 5+ | pick an unused hue | — | matching light bg |

Each entry shape:
```js
{ num: '#HEXVALUE', numShadow: 'rgba(R,G,B,0.25)', activeBg: '#HEXBG' }
```

**Step 2 — Map each tab index to its color family**

Build a reference list: for tab index 0 the color is `kcColors[0].num`, for index 1 it is `kcColors[1].num`, and so on. Note the Tailwind color family name (pink, violet, blue, emerald, amber, cyan, teal, orange…) for each index — you will need this to check the HTML in Step 3.

**Step 3 — Verify every KC panel's HTML color tokens**

For **each** KC panel (index 0 to N−1), check that the following elements use color tokens matching the panel's assigned color family from Step 2:

| HTML element | Expected class pattern |
|---|---|
| Outer wrapper | `border border-[COLOR]-100 overflow-hidden` |
| `h-1` accent bar | `bg-gradient-to-r from-[COLOR]-500 via-... to-...` |
| Body gradient div | `bg-gradient-to-br from-[COLOR]-50/60 to-white` |
| Icon span | `bg-gradient-to-br from-[COLOR]-500 to-[SHADE]-...` |
| Badge pill | `from-[COLOR]-100 to-[SHADE]-100 text-[COLOR]-600` |
| Table header (if present) | `bg-[COLOR]-50 text-[COLOR]-600` |
| Inline code tokens (if present) | `bg-[COLOR]-50 text-[COLOR]-700` |

If any panel has mismatched color tokens, rewrite all of them to the correct color family in a single multi-replace operation.

**Step 4 — Verify `h-1` accent bar structure in every panel**

Every KC panel must open with this exact three-level structure:

```html
<div class="rounded-2xl border border-[COLOR]-100 overflow-hidden">
  <div class="h-1 bg-gradient-to-r from-[COLOR]-500 via-... to-..."></div>
  <div class="bg-gradient-to-br from-[COLOR]-50/60 to-white p-5 space-y-4">
    <div class="flex items-center justify-between">
      <!-- left: icon w-9 h-9 rounded-xl + title h3 + subtitle p -->
      <!-- right: badge pill span -->
    </div>
    <!-- body: paragraph, optional table, Style B code block, amber tip -->
  </div>
</div>
```

If a panel uses the **old flat-header style** — a `flex items-center gap-3 px-5 py-4 bg-gradient-to-r` header div followed by a separate `<div class="px-5 py-5 space-y-4 bg-white">` body wrapper — replace it with the canonical structure above. After the replacement, verify the closing `</div>` count still balances (the panel's outer div should close at depth 0). Each panel should have exactly 4 closing `</div>` tags at the end: one for the inner content, one for the body gradient div, one for the outer rounded card, and one for the `kc-panel` wrapper.

---

### Check 6 — Common Mistakes tabs — coverage and depth

**Goal:** Every major concept that beginners commonly get wrong should have a mistakes tab. Target **up to 5 tabs** — one per common beginner mistake tied to this lesson's objectives.

1. List all existing mistakes tab labels.
2. Cross-check against the objective list. Identify up to 5 of the most impactful beginner mistakes — prioritise mistakes that are silent (no error, wrong result) over ones that throw obvious exceptions.
3. For every missing mistake (up to the 5-tab maximum), add a tab button and a panel.

**Each mistake panel must contain:**
- A `text-sm font-semibold` heading that names the mistake in plain English (e.g. "Using the wrong separator")
- A one-sentence explanation of *why* this mistake happens (what the learner incorrectly assumes)
- A side-by-side split using Style B-lite: red panel (✗ Wrong) on the left, emerald panel (✓ Correct) on the right
- Below the split, a `bg-amber-tip` callout explaining the fix and how to remember it

**Tab count:** Do not exceed 5 tabs. If the lesson already has 5, do not add more — instead, improve the depth of existing tabs.

---

### Check 7 — Comparison section — all concepts covered

**Goal:** The SQL/Excel Comparison section must have a row for every concept that maps meaningfully to SQL or Excel.

1. List all existing comparison row labels (`text-xs font-bold uppercase tracking-widest text-gray-400` spans).
2. Cross-check against objectives. For every missing concept, add a new row block using this pattern:

```html
<div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
  <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
    <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
      <span class="iconify text-indigo-400 text-[11px]" data-icon="ICON_NAME"></span>
    </span>
    <span class="text-xs font-bold uppercase tracking-widest text-gray-400">CONCEPT LABEL</span>
  </div>
  <div class="grid grid-cols-3 divide-x divide-gray-100">
    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">Python</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">PYTHON_SYNTAX</code>
      <p class="text-xs text-gray-500 leading-relaxed">What the Python approach does.</p>
    </div>
    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">SQL</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">SQL_EQUIVALENT or n/a</code>
      <p class="text-xs text-gray-500 leading-relaxed">SQL equivalent or why it doesn't apply.</p>
    </div>
    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">Excel</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">EXCEL_EQUIVALENT or n/a</code>
      <p class="text-xs text-gray-500 leading-relaxed">Excel equivalent or why it doesn't apply.</p>
    </div>
  </div>
</div>
```

Insert the new row in a logical order (e.g. group file-reading rows together, group inspection rows together).

---

### Check 8 — Lesson Recap cards match objectives

**Goal:** Every objective must have a corresponding recap card. The recap summarises what was learned, so it needs one card per concept.

1. List recap card labels (`text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1` elements inside `#recap`).
2. Cross-check against objectives. For each missing objective, add a recap card using this pattern (increment the watermark number):

```html
<!-- Card NN -->
<div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
  <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
    <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">NN</span>
    <div class="relative flex items-start gap-3">
      <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
        <span class="iconify text-sm" data-icon="ICON_NAME"></span>
      </span>
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">CARD TITLE</p>
        <p class="text-[11px] text-gray-600 leading-snug">One-sentence summary using <code class="font-mono">key_syntax()</code> if applicable.</p>
      </div>
    </div>
  </div>
</div>
```

---

### Check 9 — Completion banner count

**Goal:** The "Lesson Complete!" banner inside `#recap` must say "You've covered N key concepts" where N equals the total number of recap cards.

1. Count the recap cards (after any additions from Check 7).
2. Find the banner text: `You&#39;ve covered N key concepts.`
3. If the number is wrong, update it.

---

### Check 10 — All icons render correctly

**Goal:** Every `data-icon` attribute references a real Iconify icon.

1. Extract all unique `data-icon` values from the file.
2. For any icon that uses a prefix other than `fa6-solid:`, `fa6-brands:`, `fa6-regular:`, `logos:`, or `ph:` — verify it exists. If it doesn't, replace it with the nearest equivalent from a confirmed set.
3. Common safe substitutions:
   - JSON concepts → `ph:brackets-curly`
   - File loading → `fa6-solid:file-arrow-down`
   - Excel files → `fa6-solid:file-lines`
   - Inspection/preview → `fa6-solid:eye`
   - Errors → `fa6-solid:triangle-exclamation`
   - Columns/series → `fa6-solid:bars`
   - Tables → `fa6-solid:table`
   - Settings/parameters → `fa6-solid:sliders`

---

### Check 11 — Obj-card hover style consistency

**Goal:** All objective cards must have a stationary hover effect — soft pink border, subtle gray shadow, white background, and icon fill. Cards must not lift, shift, or change size on hover.

Verify the `<style>` block contains these exact rules under the `Objective cards (.obj-card)` CSS group:

```css
.obj-card {
  transition: box-shadow 0.22s cubic-bezier(.4,0,.2,1),
              border-color 0.22s ease, background-color 0.22s ease;
}
.obj-card:hover {
  box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08);
  border-color: #f5c6e0; background-color: #ffffff;
}
.obj-card .obj-icon { transition: transform 0.22s cubic-bezier(.4,0,.2,1), background-color 0.22s ease; }
.obj-card:hover .obj-icon { transform: scale(1.1); background-color: #CB187D; }
.obj-card:hover .obj-icon .iconify { color: white !important; }
```

**Rules:**
- No `transform: translateY()` on `.obj-card:hover` — cards must stay stationary
- No `border-width` change on hover — keep border at 1px to avoid layout shift
- Shadow is neutral gray `rgba(0,0,0,0.08)`, not pink-tinted
- Background stays white `#ffffff` — no soft-pink tint
- Icon still scales to pink `#CB187D` with white icon (intentional for objective cards)

Apply the same fix to the `#hub-root` block:

```css
#hub-root .obj-card:hover {
  border-color: #f5c6e0 !important;
  box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08) !important;
  background-color: #ffffff !important;
}
#hub-root .obj-card:hover .obj-icon {
  background: #CB187D !important;
}
#hub-root .obj-card:hover .obj-icon .iconify {
  color: #ffffff !important;
}
```

---

## Completion Checklist

After all 11 checks, confirm the following counts are consistent:

| Item | Should equal |
|---|---|
| Objective cards | Number of distinct concepts the lesson teaches |
| Hero "Learning Goals" number | Objective card count |
| Overview concept cards | Objective card count |
| Key Takeaway cards | Objective card count |
| KC tabs | At least one per objective; add as many sub-concept tabs as the topic needs |
| Comparison rows | One per objective that has an SQL/Excel equivalent |
| Recap cards | Objective card count |
| Banner "N key concepts" | Recap card count |
| Code Examples tabs | Up to 5 — one per objective or key scenario |
| Practice Exercise tabs | Up to 5 — one per objective |
| Knowledge Check tabs | Up to 5 — one per objective |
| Cross-section uniqueness | No two sections repeat the same sentence or explanation; each section stays within its intended role |

Do not close the task until all counts are consistent.

---

### Check 12 — Code Examples, Practice, Knowledge Check — up to 5 tabs each

**Goal:** The Code Examples, Practice Exercises, and Knowledge Check sections should each have **up to 5 tabs** — one per major concept or scenario the lesson covers. This gives the reader a hands-on example and a quiz question for every objective, not just the first one or two.

Work through each section in order:

#### 12a — Code Examples (`#code-examples`, `ce-step` tabs)
1. Count the existing `ce-step` tab buttons.
2. Cross-check tab titles against the objective list. If there are fewer than 5 tabs, and the lesson has objectives not yet illustrated with a code example, add new tabs (up to 5 total).
3. Each new tab panel must use **Style A** (dark-chrome with integrated terminal pane) and include:
   - A realistic, runnable code snippet (not toy data) using the same dataset name as the rest of the lesson where possible
   - Every non-trivial line annotated with an inline `# comment`
   - A terminal output pane showing what the code prints
   - A `bg-amber-tip` callout below the code block explaining what to notice in the output

#### 12b — Practice Exercises (`#practice`, `pe-step` tabs)
1. Count the existing `pe-step` tab buttons.
2. If there are fewer than 5 tabs, add tasks (up to 5 total) — one per objective.
3. Each practice tab must include:
   - A `task-box` block listing 2–4 numbered sub-tasks that build on each other (not isolated one-liners)
   - A "Show Solution" toggle using the accordion pattern that reveals a **Style A** code block (without the terminal pane)
   - A brief "Why this matters" sentence after the solution explaining the real-world relevance

#### 12c — Knowledge Check (`#knowledge-check`, `qz-step` tabs)
1. Count the existing `qz-step` tab buttons.
2. If there are fewer than 5 tabs, add quiz questions (up to 5 total) — one per objective.
3. Each quiz panel must have:
   - A question header card with a `Q1`/`Q2`/… watermark
   - Either a True/False or a 4-option multiple-choice question (prefer multiple-choice for concept identification; True/False for common-mistake scenarios)
   - `checkQuiz(this, BOOL)` on each answer button, where `true` marks the correct answer
   - A hidden `quiz-feedback` paragraph that appears on selection

**Tab count rule for all three sections:** The maximum is 5. If a section already has 5 tabs, do not add more — instead, review the existing tabs for content depth and fix any that are thin.

---

### Check 13 — Cross-section content uniqueness

**Goal:** Each section of the lesson must serve a distinct purpose for the reader. No two sections should explain the same concept in the same way or repeat the same sentences. A reader who reads every section front-to-back should feel like they are learning something new at each stop — not re-reading the same paragraph with a different heading.

#### The intended role of each section

Use this table as the reference for what each section is *allowed* to do. If content in a section overlaps with another section's role, rewrite it to fit the correct role instead.

| Section | Unique role | What it must NOT do |
|---|---|---|
| `#objective` | Names the skills the reader will have after this lesson. One action-verb phrase per card (e.g. "Load a CSV file"). | Must not explain *how* to do anything — no code, no prose explanation. |
| `#overview` | Connects concepts to something the reader already knows via an analogy. Answers: "What is this, in plain English?" | Must not show syntax or copy definitions from Key Concepts. |
| `#key-ideas` | States the most important take-home facts as bold assertions. Answers: "What must I remember?" | Must not be a repeat of objective card titles or overview card titles. Each takeaway should be a statement of *insight*, not a label. |
| `#key-concepts` | Teaches the mechanics — syntax, parameters, return types, and edge cases. Answers: "How does this actually work?" | Must not re-tell the analogy from Overview. Definition prose must be more technical and detailed than the Overview plain-English intro. |
| `#code-examples` | Shows the concept running on realistic data with annotated code and actual output. Answers: "What does this look like in practice?" | Must not explain what the function is (that belongs in Key Concepts). Comments annotate *what a specific line does in this example*, not what the function does in general. |
| `#mistakes` | Diagnoses the exact wrong-code pattern a beginner writes, and contrasts it with the correct pattern. Answers: "What will I get wrong?" | Must not define the concept. Must not repeat an explanation already in Key Concepts. |
| `#comparison` | Maps the Python concept to its SQL or Excel equivalent so the reader anchors it in a tool they already know. | Must not explain the Python concept from scratch — assume the reader has read Key Concepts. |
| `#practice` | Challenges the reader to write code themselves with a scaffolded task. Answers: "Can I do this?" | Must not give away the solution before the reader attempts it. Tasks must be distinct from Code Examples — not just a re-run of the same snippet. |
| `#recap` | Confirms what was learned in one short sentence per concept. Answers: "What did I just learn?" | Must not introduce new information. Must not copy the objective card description word for word — rephrase it as a past-tense achievement. |
| `#knowledge-check` | Tests understanding with a question that requires the reader to *apply* their knowledge, not just recall a label. | Must not ask "What is X called?" style questions. At least half the questions should test application (e.g. "Which code snippet would correctly load a tab-delimited file?"). |

#### How to apply this check

1. **Read every section in order** and build a mental map of what each concept explanation says.
2. **Flag any sentence or paragraph** that appears (verbatim or near-verbatim) in more than one section.
3. **Flag any section** whose prose falls outside its intended role (e.g. an Overview card that explains syntax, or a Recap card that introduces a new concept).
4. **For each flag**, apply the correct fix:
   - If the same sentence appears in Overview *and* Key Concepts: keep the version in Key Concepts (more detailed), and rewrite the Overview version to use the analogy frame instead.
   - If the same sentence appears in Key Concepts *and* Code Examples comments: the comment is correct — rewrite the Key Concepts prose to be more detailed/technical so it adds value beyond the comment.
   - If a Recap card copies an Objective card description word for word: rewrite the recap as a past-tense achievement sentence (e.g. "You learned that `pd.read_csv()` loads any CSV file into a DataFrame in one line.").
   - If a Knowledge Check question only tests recall ("What does `pd.read_csv()` do?"): replace it with an application question ("Your CSV uses tabs as separators. Which call loads it correctly?").
5. **Do not remove correct, non-duplicate content** just because the same *topic* appears in multiple sections — the goal is unique *framing*, not unique *topics*. Every section can reference `pd.read_csv()` as long as each section says something different about it.
