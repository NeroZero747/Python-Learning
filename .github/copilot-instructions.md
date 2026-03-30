# Python Learning Hub — Copilot Instructions

This file captures all design conventions, CSS architecture decisions, and workflow rules established for the Python Learning Hub project. Follow these rules precisely when creating or editing lesson HTML files.

---

## Project Overview

**Goal:** Standalone lesson HTML pages that render correctly both in a browser AND inside Atlassian Confluence (embedded via the HTML macro).

**Master template:** `docs/new_lesson_template.html` — this is the single source of truth for all components. Clone it when creating a new lesson.

**Lesson files:** `pages/track_01/mod_01_getting_started/lesson01–06.html` (and future tracks follow the same folder structure).

**Confluence-ready format:** Lesson files do **NOT** have `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`, `</body>`, or `</html>` tags. They start directly with CDN `<link>`/`<script>` tags and end after the closing `</script>`. Paste the full file contents directly into the Confluence HTML macro — no stripping needed.

---

## Brand & Design Tokens

```
Primary pink:   #CB187D
Gradient end:   #e84aad
Dark maroon:    #7F004C
Soft pink bg:   #fdf0f7
Soft border:    #f5c6e0
Dark bg:        #111827 / #1f2937
Code bg:        #1e1e2e
```

**Brand utility classes** (defined in `<style>`, not Tailwind):
- `.text-brand` → `color: #CB187D`
- `.bg-brand` → `background: #CB187D`
- `.bg-brand-soft` → `background: #fdf0f7`
- `.brand-soft-panel` → `background: #fdf0f7; border-color: #f5c6e0`

---

## Font System

Always use CSS variables:
- `--font-body: 'Inter', -apple-system, 'Segoe UI', Roboto, sans-serif`
- `--font-mono: 'Fira Code', monospace`

Load via Google Fonts CDN `<link>` tags at the very top of the file (Inter weights 400–800, Fira Code weights 400–600). Never hard-code font-family strings inline — use the variables.

---

## File Structure

Every lesson file and the master template use this exact structure — **no `<!DOCTYPE>`, `<html>`, `<head>`, or `<body>` tags**:

```
<!-- MASTER COMMENT BLOCK (template instructions) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap">
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://code.iconify.design/3/3.1.0/iconify.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" crossorigin="anonymous">
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-sql.min.js" crossorigin="anonymous">
<style> ... </style>

<!-- Scroll progress bar -->
<div class="scroll-progress" id="scroll-progress"></div>
<!-- Back to top button -->
<button class="back-to-top" ...></button>

<div id="hub-root" class="bg-gray-50 min-h-screen">
  ... all lesson content ...
</div>

<script> ... </script>
```

The file ends immediately after `</script>` with no closing `</body>` or `</html>`.

---

## External Libraries (CDN)

Always include these at the top of every lesson file in this order:
1. **Google Fonts** (Inter + Fira Code)
2. **Tailwind CSS** — `https://cdn.tailwindcss.com`
3. **Iconify 3.1.0** — `https://code.iconify.design/3/3.1.0/iconify.min.js`
4. **Prism.js 1.29.0** — theme CSS + prism.min.js + python + bash + sql components (from cdnjs.cloudflare.com)

---

## CSS Architecture

The `<style>` block always follows this three-layer pattern:

### Layer 1 — CSS Variables & Base Resets
`:root` variables, Prism overrides, `h1–h6` resets, brand utility classes.

### Layer 2 — Component CSS (browser-only)
Standard component styles scoped with regular class selectors. Tailwind arbitrary values like `text-[#CB187D]` work here in the browser.

### Layer 3 — Confluence Hub-Root Isolation Block
**All overrides for Confluence MUST be inside `#hub-root { ... }` with `!important`.**

Confluence strips:
- Tailwind arbitrary values (`text-[#CB187D]`, `from-[#CB187D]`)
- Many background/color utilities
- Font-family declarations

The hub-root block re-applies every critical style with `!important` to survive the Confluence CSS sanitizer.

```css
/* Pattern: */
#hub-root .some-class {
  property: value !important;
}
```

---

## CSS Comment Group Headers

Every `<style>` block uses standardised section comment headers so it's easy to navigate and audit the CSS. The format is:

```css
/* ── Group name ──────────────────────────────── */
```

The headers appear in this order inside every lesson file and the master template (Layer 1 first, then Layer 2 components):

| Comment label | CSS rules covered |
|---|---|
| `CSS Variables — font tokens (:root)` | `:root { --font-body; --font-mono }` |
| `Global reset — smooth scroll` | `* { scroll-behavior: smooth }` |
| `Prism.js — syntax highlighted code blocks` | `pre[class*="language-"]`, `code[class*="language-"]` |
| `Heading resets — strip Confluence default margins` | `h1, h2, h3, h4, h5, h6` |
| `Brand utility classes` | `.text-brand`, `.bg-brand`, `.bg-brand-soft`, `.brand-soft-panel`, `.bg-amber-tip`, `.bg-code`, `.border-code-sep`, `.pre-reset` |
| `Key Concepts sidebar tabs (.kc-tab / .kc-tab-active)` | `.kc-tab-active`, `.kc-tab:not(.kc-tab-active):hover`, `.kc-panel-anim`, `@keyframes kcFadeIn` |
| `Code Examples pill tabs (.ce-step / .ce-step-active)` | `.ce-step:not(.ce-step-active):hover`, `.ce-panel-anim` |
| `Common Mistakes pill tabs (.mk-step / .mk-step-active)` | `.mk-step:not(.mk-step-active):hover`, `.mk-panel-anim` |
| `Knowledge Check quiz tabs (.qz-step / .qz-step-active)` | `.qz-step:not(.qz-step-active):hover`, `.qz-panel-anim` |
| `Practice Exercise tabs (.pe-step / .pe-step-active)` | `.pe-step:not(.pe-step-active):hover`, `.pe-panel-anim`, `.task-box` |
| `Accordion — used in Overview & Key Ideas sections` | `.accordion-body`, `.accordion-toggle`, `.accordion-chevron` |
| `Hero banner — full-width gradient header` | `.hero-container`, `.hero-dots`, `.hero-glow`, `.hero-pill`, `.hero-abstract-card`, `.hero-cta`, `.stat-card` |
| `Scroll progress bar — fixed top-of-page indicator` | `.scroll-progress`, `@keyframes scrollGradient` |
| `Page layout — two-column: TOC sidebar + main content` | `.lesson-layout`, `.lesson-toc-sidebar`, `.toc-toggle-btn`, `.toc-link` |
| `Objective cards (.obj-card)` | `.obj-card` and modifier variants |
| `Generic outline tab buttons (.tab-btn / .tab-panel)` | `.tab-btn`, `.tab-panel` |
| `Code block copy button (.copy-btn)` | `.copy-btn`, `.copy-btn-light` |
| `Bottom lesson navigation — Previous / All Lessons / Next` | `.lesson-nav-link:hover` |
| `Back-to-top floating button` | `.back-to-top` |
| `Quiz answer feedback buttons (.quiz-btn.correct / .incorrect)` | `.quiz-btn.correct`, `.quiz-btn.incorrect` |
| `Card hover animations — Mistake, Flow, Recap, Overview cards` | `.mistake-card`, `.flow-stepper`, `.recap-item`, `.overview-card` |
| `Responsive — mobile breakpoint (<768px)` | `@media (max-width: 767px)` |
| `Print styles — hide interactive chrome when printing` | `@media print` |
| `Iconify icon alignment utility` | `.iconify { vertical-align: … }` |

When adding new CSS rules to a lesson file, place them under the correct group header. If a class doesn't clearly belong to an existing group, add a new `/* ── New group name ── */` header at the appropriate insertion point and document it in this table.

### TOC sidebar layout rules

The `Page layout` CSS group **must always** use a flex layout — never a float-based layout. These are the correct values:

```css
/* ── Page layout — two-column: TOC sidebar + main content ──── */
.lesson-layout { display: flex; gap: 1.75rem; align-items: flex-start; }
.lesson-toc-sidebar {
  width: 240px; flex-shrink: 0;
  position: sticky; top: 1.5rem; max-height: calc(100vh - 2rem);
  overflow-y: auto; transition: width 0.25s ease, opacity 0.25s ease;
}
```

**Mobile breakpoint** — hide sidebar and switch layout to block (no `float: none` needed):
```css
@media (max-width: 767px) {
  .lesson-toc-sidebar { display: none; }
  .lesson-layout { display: block; }
}
```

**DOM order** — `<aside class="lesson-toc-sidebar">` must appear **before** `<main>` inside the `.lesson-layout` div. This puts the TOC on the **left** column:
```html
<div class="lesson-layout">
  <aside class="lesson-toc-sidebar"> ... </aside>
  <main class="min-w-0 flex-1 space-y-10"> ... </main>
</div>
```

> **Never** use `display: block` + `float: right` on `.lesson-toc-sidebar`. That pushes the sidebar to the right side and breaks the two-column layout.

---

## Confluence-Specific Override Rules

The following rules MUST always be present in the `#hub-root` block:

### Tab pill base sizing
```css
#hub-root .ce-step, #hub-root .mk-step,
#hub-root .qz-step, #hub-root .pe-step {
  display: inline-flex !important;
  align-items: center !important;
  gap: 0.5rem !important;
  padding: 0.375rem 1rem !important;
  border-radius: 9999px !important;
  font-size: 0.75rem !important;
  font-weight: 700 !important;
  line-height: 1.2 !important;
  white-space: nowrap !important;
  border: none !important;
  cursor: pointer !important;
}
```

### Inactive tab pills (dark)
```css
#hub-root .ce-step:not(.ce-step-active),
#hub-root .mk-step:not(.mk-step-active),
#hub-root .qz-step:not(.qz-step-active),
#hub-root .pe-step:not(.pe-step-active) {
  background-color: #1f2937 !important;
  color: #ffffff !important;
  box-shadow: none !important;
}
```

### Active tab pills (pink gradient)
```css
#hub-root .ce-step-active,
#hub-root .mk-step-active,
#hub-root .qz-step-active,
#hub-root .pe-step-active {
  background: linear-gradient(to right, #CB187D, #e84aad) !important;
  color: #ffffff !important;
  box-shadow: 0 10px 25px -5px rgba(203,24,125,0.3) !important;
}
```

### Hero stat pills
```css
/* Non-clickable — no pointer cursor */
.hero-pill {
  pointer-events: none;
  cursor: default;
}
/* Confluence link color override */
#hub-root a.hero-pill { color: #CB187D !important; }
/* Label opacity — force fully visible */
#hub-root .hero-pill .opacity-55 { opacity: 1 !important; }
#hub-root .hero-pill .opacity-50 { opacity: 1 !important; }
```

### TOC active state
```css
#hub-root .toc-link:hover { color: #CB187D !important; }
#hub-root .toc-link.active {
  color: #CB187D !important;
  font-weight: 600 !important;
  border-left: 3px solid #CB187D !important;
  padding-left: 8px !important;
  background-color: #fdf0f7 !important;
}
```

### Module lessons list active link
```css
#hub-root .mod-lesson-active {
  background-color: #fdf0f7 !important;
  border-color: #CB187D !important;
  color: #CB187D !important;
}
#hub-root .mod-lesson-active .lesson-dot {
  background-color: #CB187D !important;
}
```
Stamp `mod-lesson-active` on the `<a>` element for the **current lesson's own link** in the module lessons TOC sidebar.

### Bottom nav (Previous / All Lessons / Next) hover
```css
#hub-root .lesson-nav-link:hover p,
#hub-root .lesson-nav-link:hover span,
#hub-root .lesson-nav-link:hover svg {
  color: #CB187D !important;
  transition: color 0.15s !important;
}
```
Confluence strips the Tailwind `group-hover:text-[#CB187D]` arbitrary values on these `<a>` elements. The `#hub-root` override restores the pink hover highlight for all child text and icons.

### Section header components
```css
#hub-root .section-header {
  display: flex !important; align-items: center !important;
  gap: 1rem !important; padding: 1.25rem 2rem 1.25rem 1rem !important;
  background: #ffffff !important;
  border-bottom: 1px solid #f3f4f6 !important;
  border-left: 4px solid #CB187D !important;
}
#hub-root .section-icon {
  display: inline-flex !important; align-items: center !important;
  justify-content: center !important;
  width: 2.75rem !important; height: 2.75rem !important;
  border-radius: 0.75rem !important; background: #CB187D !important;
  flex-shrink: 0 !important;
}
#hub-root .section-title {
  font-size: 1.25rem !important; font-weight: 700 !important;
  color: #111827 !important;
}
#hub-root .section-subtitle {
  font-size: 0.875rem !important; color: #9ca3af !important;
}
```

---

## HTML Component Reference

All lesson files have the same `<div id="hub-root">` wrapper as the outermost container. Everything inside is Confluence-isolated.

### Section IDs (in order)
| Section ID | Purpose |
|---|---|
| `objective` | Learning goals — 4-card grid |
| `overview` | Hook quote, analogy, and key-concept summary |
| `key-ideas` | Flow stepper / step-by-step ideas |
| `key-concepts` | `kc-tab` accordion sidebar tabs |
| `code-examples` | `ce-step` dark pill tabs + code blocks |
| `comparison` | Comparison table |
| `practice` | `pe-step` practice exercise pill tabs |
| `real-world` | Real-world application examples |
| `recap` | Summary / lesson recap |
| `knowledge-check` | `qz-step` quiz pill tabs |
| `next-lesson` | Navigation to next lesson + module list |

### Overview Section — Hook Quote + Analogy Pattern

Every `#overview` section follows a fixed four-part structure. Each part is required; do not skip any of them.

**Part 1 — Hook quote card.** Open with a single, memorable sentence that states what the lesson topic *is* in plain English. Render it inside the soft-pink gradient card so it stands out visually.

```html
<div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
  <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Py</span>
  <div class="relative flex items-start gap-4">
    <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
      <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>
    </span>
    <p class="text-base text-gray-800 leading-relaxed font-medium">ONE CLEAR SENTENCE DEFINING THE TOPIC.</p>
  </div>
</div>
```

**Part 2 — Analogy intro paragraph.** Immediately after the hook card, write a short paragraph that anchors the topic in a real-world analogy the learner already understands. Start the sentence with "Think of…" and pick a concrete object or situation (a kitchen, a toolbox, a recipe, a filing cabinet, etc.) that maps cleanly onto the concept. The analogy must be consistent — if you choose "a kitchen" here, the same kitchen vocabulary should appear on the cards below.

```html
<p class="text-sm text-gray-600 leading-relaxed">Think of [TOPIC] like [REAL-WORLD THING]: [brief mapping sentence].</p>
```

**Part 3 — Analogy card grid.** Present the key sub-concepts as a 2-column card grid. Every card must include:
- An Iconify icon representing that concept
- A **bold title** — the technical name of the concept
- An *italic analogy subtitle* — one phrase connecting it back to the Part 2 analogy (e.g. "The stove — turns ingredients into a meal")
- A short plain-English description (2–3 sentences)

```html
<div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
        <span class="iconify text-brand text-base" data-icon="ICON_NAME"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">Concept Name</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">The [thing] — [what it does in the analogy]</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">Plain-English description of what this concept actually does.</p>
  </div>
  <!-- repeat for each sub-concept -->
</div>
```

**Part 4 — Closing tip box.** End the overview with an amber `bg-amber-tip` callout that gives one concrete, memorable takeaway — typically why this topic matters for the learner's day-to-day work.

```html
<div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">ONE KEY "SO WHAT" TAKEAWAY — why this matters in practice.</p>
</div>
```

**Analogy quality checklist:**
- The analogy domain (kitchen, toolbox, etc.) is introduced in Part 2 and echoed in every Part 3 card subtitle. All four parts use the same vocabulary — never mix analogies mid-section.
- The analogy maps *directionally*: each concept card subtitle should state what the real-world item *does*, not just what it *is* (e.g. "The pantry — stocked with 500,000+ libraries" rather than just "A pantry").
- Keep the analogy subtitle short enough to fit on one line — aim for under 50 characters.
- Choose analogies that are universally familiar (kitchens, buildings, vehicles, documents). Avoid domain-specific metaphors (sports, music) that rely on background knowledge the learner may not have.

### Tab System naming conventions
| Tab type | Step class | Active class | Switch function |
|---|---|---|---|
| Code Examples | `ce-step` | `ce-step-active` | `switchCeTab(i)` |
| Common Mistakes | `mk-step` | `mk-step-active` | `switchMkTab(i)` |
| Practice Exercises | `pe-step` | `pe-step-active` | `switchPeTab(i)` |
| Knowledge Check (Quiz) | `qz-step` | `qz-step-active` | `switchQzTab(i)` |
| Key Concepts sidebar | `kc-tab` | `kc-tab-active` | `switchKcTab(i)` |

Tab panels hide via `hidden` class. Active panel gets panel animation class (e.g. `ce-panel-anim`).

### Section header pattern
```html
<div class="section-header">
  <div class="section-icon">
    <span class="iconify text-white text-xl" data-icon="ICON_NAME"></span>
  </div>
  <div class="section-body">
    <h2 class="section-title">Section Title</h2>
    <p class="section-subtitle">Brief description</p>
  </div>
</div>
```

### Skill dots (difficulty indicator)
```html
<!-- Beginner = 1 active -->
<span class="skill-dot skill-dot-active"></span>
<span class="skill-dot"></span>
<span class="skill-dot"></span>
```

### Accordion (used in overview & key ideas)
```html
<div>
  <button class="accordion-toggle w-full flex items-center justify-between ..." onclick="this.nextElementSibling.classList.toggle('open')">
    Accordion Title
    <span class="iconify accordion-chevron ..." data-icon="fa6-solid:chevron-down"></span>
  </button>
  <div class="accordion-body">
    Content here
  </div>
</div>
```
CSS: `.accordion-body { display:none !important; }` and `.accordion-body.open { display:block !important; }`

### Copy button for code blocks
```html
<button class="copy-btn" onclick="copyCode(this)">
  <span class="iconify" data-icon="fa6-regular:copy"></span>
  <span>Copy</span>
</button>
```

---

## Code Block Styles

Two canonical styles exist in the codebase. **Style A** and **Style B** are both correct — they apply to different section types. Never mix them. Every code block in the lesson must use exactly one of these two styles.

### Style A — Dark-chrome (standalone featured examples)

Used in: `#code-examples`, `#decision-flow`, `#practice` solution blocks.

```html
<div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
  <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
    <div class="flex items-center gap-3">
      <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
        <!-- Python files: -->
        <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
        <!-- Bash/shell files: -->
        <!-- <span class="iconify text-yellow-400 text-xs" data-icon="fa6-solid:terminal" data-width="12" data-height="12"></span> -->
        <span class="text-[11px] font-semibold text-gray-400">filename.py</span>
      </div>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
    </button>
  </div>
  <div class="bg-code">
    <pre class="overflow-x-auto pre-reset"><code class="language-python">CODE</code></pre>
  </div>
  <!-- Optional integrated terminal pane — only in #code-examples -->
  <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
    <div class="flex items-center gap-2 mb-1.5">
      <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
      <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
      <span class="text-[10px] text-gray-600 font-mono">$ python filename.py</span>
    </div>
    <div class="font-mono text-xs text-emerald-400 leading-relaxed">OUTPUT</div>
  </div>
</div>
```

**Style A rules:**
- Header uses `py-2.5` (not `py-2`) and `bg-[#181825]`
- Filename pill on the left inside `bg-[#1e1e2e] border border-white/5` rounded-md
- Copy button on the right with `copy-btn-light`
- **No traffic-light dots** — never add `<span class="w-2.5 h-2.5 rounded-full …">` elements
- Terminal output pane (`bg-[#11111b]`) is only in `#code-examples`; omit it in `#decision-flow` and `#practice`
- Language icon: `logos:python` for `.py` files; `fa6-solid:terminal` for `.sh` / bash files

### Style B — Simple-dark (inline snippets inside tabs and cards)

Used in: `#key-concepts` tab panels, `#comparison` code columns.

```html
<div class="rounded-xl overflow-hidden bg-code shadow-md">
  <!-- For #comparison columns, add: flex flex-col flex-1 -->
  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
    <div class="flex items-center gap-2">
      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
      <!-- or for bash: <span class="iconify text-gray-400" data-icon="fa6-solid:terminal" data-width="14" data-height="14"></span> -->
      <span class="text-[11px] font-semibold text-gray-400">Python</span>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
    </button>
  </div>
  <pre class="overflow-x-auto pre-reset"><code class="language-python">CODE</code></pre>
</div>
```

**Style B rules:**
- Outer div: `bg-code shadow-md` (not `border border-gray-800 shadow-lg`)
- Header uses `py-2` (not `py-2.5`) with `border-b border-code-sep`
- Language label text ("Python", "Bash", "SQL") next to icon — no filename pill
- Icon `data-width/height="14"` (not `12`)
- No terminal output pane
- `#comparison` adds `flex flex-col flex-1` to the outer div so columns stretch to equal height
- **No traffic-light dots**

### Style B-lite — Bare code (wrong/correct mini-blocks inside `#mistakes`)

Used in: the red/emerald split panels inside `#mistakes` mistake cards only.

```html
<div class="rounded-xl overflow-hidden bg-code">
  <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">CODE</code></pre>
</div>
```

**Style B-lite rules:**
- No `shadow-md`, no header bar, no copy button — the split panel label (✗ Wrong / ✓ Correct) provides enough context
- `px-4 py-3` goes on `<pre>`, not on the outer div
- The single-column conceptual block (non-split-panel variant) uses Style B, not Style B-lite

### Section → Style mapping

| Section | Code block style |
|---|---|
| `#code-examples` | **Style A** with integrated terminal pane |
| `#decision-flow` | **Style A** without terminal pane |
| `#practice` | **Style A** without terminal pane |
| `#key-concepts` | **Style B** |
| `#comparison` | **Style B** + `flex flex-col flex-1` on outer div |
| `#mistakes` split panel | **Style B-lite** |
| `#mistakes` single-column | **Style B** |

Every section follows the same outer shell — a `<section id="SECTION_ID">` wrapping a `rounded-2xl` card with a pink-left-border section header and a white content body. The templates below show the exact class names and structure to use for each section. Do not vary these structures when building new lessons — consistency across modules is the goal.

### Outer section shell (used by every section)

```html
<section id="SECTION_ID">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <!-- Section header — always this exact structure -->
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="ICON_NAME"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Section Title</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">One-line description of this section</p>
      </div>
    </div>

    <!-- Section body -->
    <div class="bg-white px-8 py-7 space-y-6">
      <!-- section content here -->
    </div>

  </div>
</section>
```

**Section header icons** — match these icons to their sections exactly:

| Section | `data-icon` |
|---|---|
| `objective` | `fa6-solid:bullseye` |
| `overview` | `fa6-solid:binoculars` |
| `key-ideas` | `fa6-solid:lightbulb` |
| `key-concepts` | `fa6-solid:book-open` |
| `code-examples` | `fa6-solid:code` |
| `comparison` | `fa6-solid:scale-balanced` |
| `practice` | `fa6-solid:pencil` |
| `real-world` | `fa6-solid:briefcase` |
| `recap` | `fa6-solid:list-check` |
| `knowledge-check` | `fa6-solid:brain` |
| `next-lesson` | `fa6-solid:circle-arrow-right` |

---

### `#objective` — Learning Goals (4-card grid)

Four `obj-card` items in a 2-column grid, each with a branded icon, a bold goal title, and a one-line description. Always end the section with an amber tip box summarising what the lesson covers.

```html
<div class="bg-white px-8 py-7">
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">

    <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
      <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
        <span class="iconify text-brand text-lg" data-icon="ICON_NAME"></span>
      </span>
      <div>
        <p class="text-sm font-semibold text-gray-800">Goal title</p>
        <p class="text-xs text-gray-500 mt-0.5">One-line supporting detail</p>
      </div>
    </div>

    <!-- repeat for each of the 4 goals -->

  </div>

  <!-- Amber tip — what the lesson covers overall -->
  <div class="mt-5 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
    <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
    <p class="text-sm text-gray-600">This lesson introduces <strong>TOPIC</strong> before diving into [next concept].</p>
  </div>
</div>
```

---

### `#key-ideas` — Key Takeaways (colored gradient cards)

Each takeaway is a full-width card with a 1-pixel color-coded top bar, a gradient icon, a bold heading, a 1–2 sentence explanation, and a row of small pink/colored keyword pills. Use a different accent color per card to give each idea its own visual identity. The three standard color themes are brand-pink, violet, and blue — add more for extra cards.

```html
<div class="bg-white px-8 py-7 space-y-4">

  <!-- Brand-pink card -->
  <div class="obj-card obj-card-kt rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm">
    <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
    <div class="px-6 py-5">
      <div class="flex items-center gap-3 mb-3">
        <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
          <span class="iconify text-white text-sm" data-icon="ICON_NAME"></span>
        </span>
        <h3 class="text-sm font-bold text-gray-900">Takeaway Title</h3>
      </div>
      <p class="text-xs text-gray-600 leading-relaxed mb-4">Full-sentence explanation of this takeaway.</p>
      <div class="flex flex-wrap gap-2">
        <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Keyword</span>
        <!-- add more keywords as needed -->
      </div>
    </div>
  </div>

  <!-- Violet card -->
  <div class="obj-card obj-card-violet rounded-2xl border border-violet-100 bg-white overflow-hidden shadow-sm">
    <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
    <div class="px-6 py-5">
      <div class="flex items-center gap-3 mb-3">
        <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
          <span class="iconify text-white text-sm" data-icon="ICON_NAME"></span>
        </span>
        <h3 class="text-sm font-bold text-gray-900">Takeaway Title</h3>
      </div>
      <p class="text-xs text-gray-600 leading-relaxed mb-4">Full-sentence explanation of this takeaway.</p>
      <div class="flex flex-wrap gap-2">
        <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Keyword</span>
      </div>
    </div>
  </div>

  <!-- Blue card -->
  <div class="obj-card obj-card-blue rounded-2xl border border-blue-100 bg-white overflow-hidden shadow-sm">
    <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>
    <div class="px-6 py-5">
      <div class="flex items-center gap-3 mb-3">
        <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">
          <span class="iconify text-white text-sm" data-icon="ICON_NAME"></span>
        </span>
        <h3 class="text-sm font-bold text-gray-900">Takeaway Title</h3>
      </div>
      <p class="text-xs text-gray-600 leading-relaxed mb-4">Full-sentence explanation of this takeaway.</p>
      <div class="flex flex-wrap gap-2">
        <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Keyword</span>
      </div>
    </div>
  </div>

</div>
```

---

### `#recap` — Lesson Recap (numbered grid + completion banner)

A 2×2 grid of recap cards, each numbered with a large watermark (`01`, `02`, …) in the card background, followed by a full-width pink gradient "Lesson Complete!" banner. Always use exactly 4 recap cards — one per main concept covered in the lesson.

```html
<div class="bg-white px-8 py-7 space-y-6">

  <!-- 2×2 recap grid -->
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

    <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
      <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
        <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
        <div class="relative flex items-start gap-3">
          <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
            <span class="iconify text-sm" data-icon="fa6-solid:check"></span>
          </span>
          <p class="text-sm text-gray-700 font-medium leading-relaxed">Complete sentence summarising concept 1.</p>
        </div>
      </div>
    </div>

    <!-- repeat with 02, 03, 04 watermarks -->

  </div>

  <!-- Completion banner — always the last element in #recap -->
  <div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">
    <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">✓</span>
    <div class="relative flex items-center gap-4">
      <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">
        <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-white">Lesson Complete!</p>
        <p class="text-xs text-white/80 mt-0.5">You've covered N key concepts. Ready for the knowledge check?</p>
      </div>
    </div>
  </div>

</div>
```

---

### `#knowledge-check` — Quiz (qz-step pill tabs + question panels)

Each question gets its own pill tab and panel. The active tab has the pink gradient; inactive tabs are dark gray. Every question panel uses the same pink gradient header card with a `Q1`/`Q2`/`Q3` watermark. Use `checkQuiz(this, CORRECT_BOOL)` on each answer button.

```html
<div class="bg-white px-8 py-7 space-y-6">

  <!-- Pill tabs -->
  <div class="flex items-center gap-2 mb-6" role="tablist">
    <button onclick="switchQzTab(0)" class="qz-step qz-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
      <span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span>
      <span class="qz-step-label text-xs font-bold">Question 1</span>
    </button>
    <button onclick="switchQzTab(1)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
      <span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span>
      <span class="qz-step-label text-xs font-bold">Question 2</span>
    </button>
    <!-- add more buttons for extra questions -->
  </div>

  <!-- Question panel (first is visible, rest get class="hidden") -->
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
          <p class="text-sm font-semibold text-gray-800 mb-4">QUESTION TEXT — True or False?</p>
          <div class="flex gap-3">
            <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors" onclick="checkQuiz(this, true)">
              <span class="iconify mr-1.5" data-icon="fa6-solid:check"></span> True
            </button>
            <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors" onclick="checkQuiz(this, false)">
              <span class="iconify mr-1.5" data-icon="fa6-solid:xmark"></span> False
            </button>
          </div>
          <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
        </div>
      </div>

    </div>
  </div>

  <!-- Hidden panels follow the same structure with class="qz-panel qz-panel-anim hidden" -->

</div>
```

---

### `#next-lesson` + Bottom Navigation

The `#next-lesson` section previews the next lesson with a lesson number badge, title, module label, and a 3-card "What You Will Learn" grid. Below it — **outside** the section card but still inside `<main>` — sits the Previous / All Lessons / Next bottom nav. These two blocks always appear together and always appear last.

**`#next-lesson` section:**

```html
<section id="next-lesson" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <!-- Section header (use fa6-solid:circle-arrow-right icon) -->
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:circle-arrow-right"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Next Lesson</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Preview of what comes next</p>
      </div>
    </div>

    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Lesson badge -->
      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
          <span class="text-white font-bold text-lg">N</span>  <!-- N = lesson number -->
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module X · Lesson N</p>
          <h3 class="text-base font-bold text-gray-800">Next Lesson Title</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>

      <!-- 3-card preview grid -->
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="ICON_NAME"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Preview item title</p>
            </div>
          </div>
          <!-- repeat for 3 items -->
        </div>
      </div>

    </div>
  </div>
</section>
```

**Bottom navigation bar** (placed immediately after `#next-lesson`, as a bare `<section>` with no card wrapper):

```html
<!-- Bottom nav — Previous / All Lessons / Next -->
<section>
  <div class="flex flex-col sm:flex-row gap-3">

    <!-- Previous lesson (omit entirely on lesson 1) -->
    <a href="PREV_LESSON.html" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Previous Lesson Title</p>
      </div>
    </a>

    <!-- Spacer (only when no Previous link) -->
    <div class="flex-1"></div>

    <!-- All Lessons hub link — always present -->
    <a href="../../../hub_home_page.html" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>

    <!-- Next lesson (omit entirely on last lesson of module) -->
    <a href="NEXT_LESSON.html" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Next Lesson Title</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>

  </div>
</section>
```

**Bottom nav rules:**
- The lesson-nav-link hover color is restored in the `#hub-root` block — do not change the hover classes.
- On the **first lesson** of a module, omit the Previous `<a>` entirely and replace it with `<div class="flex-1"></div>`.
- On the **last lesson** of a module, omit the Next `<a>` entirely.
- The hub home page path is always `../../../hub_home_page.html` (three levels up from any lesson file).

---

## Writing Style & Content Clarity

These rules apply to all body text written inside lesson files. They exist because the audience is non-programmers who are learning Python for the first time — clarity and confidence matter more than brevity.

### Sentence format

Write all explanation text as complete sentences with a subject, verb, and object. Sentence fragments, note-style bullets (e.g. "No loops needed"), and terse captions are not acceptable for body copy. Reserve bullet lists only for genuinely enumerable items (e.g. a list of steps or a list of features) — never for explanations that should read as prose.

**Correct:** "A virtual environment is a self-contained folder that holds a specific version of Python and all the packages your project needs, kept separate from every other project on your machine."

**Incorrect:** "Self-contained folder. Keeps packages separate. One per project."

### Define before demonstrating

Whenever a new term or concept appears for the first time, define it in plain English in the sentence immediately before any code example. Never show code cold. The learner needs the mental model first.

**Pattern:** "[Term] is [plain-English definition]. Here is how you write one:"

### Analogies in the overview section

Every `#overview` section must contain an analogy. Refer to the "Overview Section — Hook Quote + Analogy Pattern" section above for the exact HTML structure. The analogy must:

1. Be introduced as a "Think of…" sentence in the analogy intro paragraph.
2. Be echoed consistently in every analogy card subtitle in the card grid.
3. Use a domain the learner already knows — everyday objects (kitchens, buildings, vehicles, documents) rather than technical or sports metaphors.
4. Map directionally: each card subtitle must say what the real-world item *does*, not just name it.

When the analogy is strong, leave it out of the tip box — the tip box should add new information (the "so what" for the learner's job), not repeat the analogy.

### Explaining potentially unclear concepts

When a concept is likely to confuse beginners, apply these techniques in order:

1. **Name the confusion directly.** Start a sentence with "You might wonder why…" or "This can seem confusing at first because…" — naming the sticking point reduces anxiety.
2. **Use an everyday comparison.** Connect the concept to something the learner already does with Excel, email, or file folders.
3. **Show a minimal working example.** Use the smallest possible code snippet that demonstrates the idea. Every line of example code should have an inline comment explaining it.
4. **Add a tip or warning callout.** Use the amber `bg-amber-tip` box for important caveats and the soft-pink `brand-soft-panel` box for helpful tips. Never bury a warning inside a paragraph.

### Tone

Write in second person ("you", "your"). Address the learner directly and use an encouraging, professional tone — not casual slang, but also not academic jargon. Contractions are fine (e.g. "you'll", "it's", "don't").

---

## JavaScript Patterns

All JS is inline at the bottom of each file in a `<script>` tag.

### Required functions
- `switchCeTab(i)` — Code Examples tab switcher
- `switchMkTab(i)` — Common Mistakes tab switcher
- `switchPeTab(i)` — Practice Exercises tab switcher
- `switchQzTab(i)` — Knowledge Check tab switcher
- `switchKcTab(i)` — Key Concepts sidebar tab switcher
- `toggleToc()` — Mobile TOC show/hide
- `copyCode(btn)` — Copy code block contents to clipboard
- TOC scroll spy (`IntersectionObserver` watching all `[data-section]` elements)
- Scroll progress bar update
- Back-to-top button visibility

### Tab switcher generic pattern
```javascript
function switchCeTab(i) {
  document.querySelectorAll('.ce-step').forEach((b,j) => {
    b.classList.toggle('ce-step-active', i===j);
    b.classList.toggle('ce-panel-anim', false);
  });
  document.querySelectorAll('.ce-panel').forEach((p,j) => {
    p.classList.toggle('hidden', i!==j);
    if(i===j) { p.classList.remove('ce-panel-anim'); void p.offsetWidth; p.classList.add('ce-panel-anim'); }
  });
}
```

---

## File Update Workflow

### Rule: Always update ALL lesson files + template together
When making a CSS change or structural fix, apply it to:
1. All 6 lesson files in `pages/track_01/mod_01_getting_started/`
2. `docs/new_lesson_template.html`

Never manually edit one file at a time. Use Python scripts to apply changes across all files simultaneously.

### Script naming convention
`_fix_DESCRIPTION.py` in the project root (e.g. `_fix_tab_active_bg.py`, `_fix_confluence_overrides.py`).

Each script should:
- Define a `TARGET_FILES` list with paths to all 6 lessons + template
- Apply the change by string replacement or regex
- Print a per-file status (✅ patched / ⚠️ already patched / ❌ not found)

---

## Key Design Decisions

| Decision | Rationale |
|---|---|
| `#hub-root` + `!important` overrides | Confluence HTML macro strips almost all Tailwind arbitrary values and many utility colors; `!important` under a specific ID beat Confluence's global styles |
| Hero pills: `pointer-events: none` | Pills are decorative stat displays, not navigation links |
| Prism.js theme `prism-tomorrow` | Dark code blocks on dark bg (`#1e1e2e`) match the design system |
| Tailwind CDN (not built) | Avoids build toolchain for a docs-first project; arbitrary values work in browser, only Confluence needs hub-root fallbacks |
| `mod-lesson-active` CSS class on `<a>` | Confluence strips inline `style=` attributes and Tailwind arbitrary color classes; a semantic CSS class + hub-root override survives the sanitizer |
| `#hub-root .lesson-nav-link:hover` override | Confluence strips `group-hover:text-[#CB187D]` Tailwind arbitrary hover values on nav `<a>` elements; the hub-root rule restores the pink hover on Previous / All Lessons / Next |
| Single `<style>` block per file | Keeps each lesson self-contained for Confluence embedding (no linked stylesheets) |
| No `<html>`/`<head>`/`<body>` shell | Confluence HTML macro embeds fragment HTML; outer document tags are injected by Confluence itself and cause conflicts if duplicated |
