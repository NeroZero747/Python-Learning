---
mode: "agent"
description: "Write or rewrite the #key-concepts section for a lesson HTML file"
---

<!-- ── FILL IN BEFORE RUNNING ────────────────────────────────────────────
TARGET_FILE:      /absolute/path/to/lesson.html
SECTION_SUBTITLE: One-line description, e.g. "Repository, commit, staging area, and remote."
TABS:
  0: label=…  icon=fa6-solid:…  header_subtitle="…"  badge_label=…  widget=rules-table      tip_icon=fa6-solid:lightbulb
  1: label=…  icon=fa6-solid:…  header_subtitle="…"  badge_label=…  widget=operators-table  tip_icon=fa6-solid:lightbulb
  2: label=…  icon=fa6-solid:…  header_subtitle="…"  badge_label=…  widget=comparison-table tip_icon=fa6-solid:triangle-exclamation
  3: label=…  icon=fa6-solid:…  header_subtitle="…"  badge_label=…  widget=comparison-strip tip_icon=fa6-solid:lightbulb
Colors are always sequential: tab 0 = pink, 1 = violet, 2 = blue, 3 = emerald, 4 = amber.
──────────────────────────────────────────────────────────────────────── -->

Rewrite `<section id="key-concepts">` in TARGET_FILE using the vertical sidebar tab layout below.

---

## Writing Style

This content is for people new to programming. Write like you're explaining to a smart colleague who has never coded.

- **Plain English.** Avoid "instantiate", "iterate", "invoke" unless taught in this lesson — if used, define in the same sentence.
- **15 words or fewer per sentence.** Split long ideas into two sentences.
- **One idea per sentence.** Don't chain concepts with "and" / "which".
- **Second person.** Use "you" and "your".
- **Concrete over abstract.** "You can change the value later" beats "this allows dynamic behavior".
- **No filler.** Cut "it is important to note that", "as you can see", "essentially", "in order to".

### Content rules per element

**`definition`** — 1–3 sentences. Bold the 2–4 word key phrase. Add `<code>` pills for type names. Pattern: "[Concept] is [plain-English definition]. [One sentence of practical context]."

**`code`** — 3–6 lines. Every line has an inline `#` comment. No imports. Reuse variable names from the widget where possible.

**`tip_text`** — One practical warning or "good to know". Bold the actionable phrase. Use color-matched `<code>` pills (`-200` bg, `-300` border, `-800` text — never amber).

**Widget code position** — Place the widget before the code block unless showing code first gives essential context for the widget (e.g. an operators reference table).

---

## Color Reference

Colors are always sequential: tab 0 = pink, 1 = violet, 2 = blue, 3 = emerald, 4 = amber. Copy class names exactly — do not guess.

| Color | Panel border | Top-bar gradient | Panel bg gradient | Type badge gradient | Tip bg / border | Header chip gradient | Tip chip bg |
|---|---|---|---|---|---|---|---|
| `pink` | `border-pink-100` | `from-[#CB187D] via-pink-400 to-rose-300` | `from-pink-50/60 to-white` | `from-pink-100 to-rose-100 text-[#CB187D] border-pink-200` | `bg-pink-50 border-pink-100` | `from-[#CB187D] to-[#e84aad]` | `bg-[#CB187D]` |
| `violet` | `border-violet-100` | `from-violet-500 via-purple-400 to-fuchsia-300` | `from-violet-50/60 to-white` | `from-violet-100 to-purple-100 text-violet-600 border-violet-200` | `bg-violet-50 border-violet-100` | `from-violet-500 to-purple-600` | `bg-violet-500` |
| `blue` | `border-blue-100` | `from-blue-500 via-cyan-400 to-teal-300` | `from-blue-50/60 to-white` | `from-blue-100 to-indigo-100 text-blue-600 border-blue-200` | `bg-blue-50 border-blue-100` | `from-blue-500 to-indigo-600` | `bg-blue-500` |
| `emerald` | `border-emerald-100` | `from-emerald-500 via-teal-400 to-cyan-300` | `from-emerald-50/60 to-white` | `from-emerald-100 to-teal-100 text-emerald-600 border-emerald-200` | `bg-emerald-50 border-emerald-100` | `from-emerald-500 to-teal-600` | `bg-emerald-500` |
| `amber` | `border-amber-100` | `from-amber-500 via-orange-400 to-red-300` | `from-amber-50/60 to-white` | `from-amber-100 to-orange-100 text-amber-600 border-amber-200` | `bg-amber-50 border-amber-100` | `from-amber-500 to-orange-500` | `bg-amber-500` |

**Inline `<code>` pills:**
- In definition / widget body → `-100` bg, `-200` border, `-700` or `-800` text
- Inside tip callout → `-200` bg, `-300` border, `-800` text (never `-50`)

---

## Section Outer Shell

```html
<section id="key-concepts" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <!-- Section header — icon is always fa6-solid:book-open, never change it -->
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:book-open"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Concepts</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">SECTION_SUBTITLE</p>
      </div>
    </div>

    <div class="bg-white px-6 py-7">
      <div class="flex flex-col md:flex-row gap-0">

        <!-- ── Sidebar ── -->
        <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">

          <!-- kc-indicator: position:absolute, right-0, syncs height to active tab via JS -->
          <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full transition-all duration-300" style="height:68px;background:#CB187D;"></div>

          <!-- Tab 0 — ACTIVE. Use inline style= on .kc-tab-num (Confluence strips Tailwind arbitrary values). -->
          <button onclick="switchKcTab(0)" class="kc-tab kc-tab-active group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#CB187D;color:#fff;box-shadow:0 2px 8px rgba(203,24,125,0.25)"><span class="iconify text-[11px]" data-icon="TAB_0_ICON"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-900">TAB_0_LABEL</span>
          </button>

          <!-- Tab 1+ — INACTIVE. All inactive tabs use style="background:#f3f4f6;color:#9ca3af" and text-gray-400 label. -->
          <button onclick="switchKcTab(1)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="TAB_1_ICON"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">TAB_1_LABEL</span>
          </button>
          <!-- Repeat inactive pattern for tabs 2, 3, 4 -->

        </div><!-- /sidebar -->

        <!-- ── Panels ── -->
        <div class="flex-1 min-w-0 md:pl-5">

          <!-- Panel 0 — ACTIVE (no "hidden"). See Widget HTML Patterns below for panel body content. -->
          <div class="kc-panel kc-panel-anim" data-color="pink" role="tabpanel">
            <div class="rounded-2xl border border-pink-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-[#CB187D] via-pink-400 to-rose-300"></div>
              <div class="bg-gradient-to-br from-pink-50/60 to-white p-5 space-y-4">
                <!-- header row, definition, widget, code block, tip — see patterns below -->
              </div>
            </div>
          </div>

          <!-- Panel 1+ — INACTIVE (add class="kc-panel kc-panel-anim hidden"). -->
          <!-- Change: border color, top-bar gradient, panel bg gradient, header chip gradient,
               type badge gradient/color, tip bg/border, tip chip color — per Color Reference. -->

        </div><!-- /panels -->
      </div>
    </div>
  </div>
</section>
```

---

## Panel Body Pattern

Every panel body (`p-5 space-y-4`) contains these four elements in order (widget and code may swap — see Writing Style):

### 1. Header row
```html
<div class="flex items-center justify-between">
  <div class="flex items-center gap-3">
    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-md shrink-0">
      <span class="iconify text-white text-sm" data-icon="TAB_ICON"></span>
    </span>
    <div>
      <h3 class="text-sm font-bold text-gray-900 leading-tight">TAB_LABEL</h3>
      <p class="text-[10px] text-gray-400 leading-none mt-0.5">HEADER_SUBTITLE</p>
    </div>
  </div>
  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-pink-100 to-rose-100 text-[#CB187D] border border-pink-200 shadow-sm">
    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> BADGE_LABEL
  </span>
</div>
```

### 2. Definition
```html
<!-- Bare <p> — no wrapper div, no border-l accent -->
<p class="text-xs text-gray-600 leading-relaxed">DEFINITION</p>
```

### 3. Widget — pick one type from Widget HTML Patterns below

### 4. Code block (Style B — always this style in #key-concepts, never the dark-chrome Style A)
```html
<div class="rounded-xl overflow-hidden bg-code shadow-md">
  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
    <div class="flex items-center gap-2">
      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
      <span class="text-[11px] font-semibold text-gray-400">Python</span>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
    </button>
  </div>
  <pre class="overflow-x-auto pre-reset"><code class="language-python">CODE</code></pre>
</div>
```
For Bash: replace `logos:python` icon with `fa6-solid:terminal` (gray-400), language label "Bash", class `language-bash`.

### 5. Tip callout (color-matched — never amber)
```html
<div class="rounded-xl p-3 flex items-start gap-2.5 bg-pink-50 border border-pink-100">
  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-[#CB187D] shrink-0 mt-0.5">
    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
  </span>
  <p class="text-xs text-gray-600">TIP_TEXT</p>
</div>
```

---

## Widget HTML Patterns

Insert one widget between the definition and code block (or after the code block if code context helps first).

### `rules-table` — Use for syntax / naming rules (good ✓ / bad ✗ pills)
```html
<div class="rounded-xl overflow-hidden border border-COLOR-100">
  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-COLOR-50 to-COLOR2-50 border-b border-COLOR-100">
    <span class="iconify text-COLOR-500 text-xs" data-icon="ICON"></span>
    <p class="text-[10px] font-bold uppercase tracking-widest text-COLOR-500">LABEL</p>
  </div>
  <table class="w-full text-xs border-collapse bg-white">
    <tbody>
      <tr class="border-b border-gray-50">
        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2">Rule with <code class="font-mono bg-COLOR-100 text-COLOR-700 border border-COLOR-200 px-1 rounded">keyword</code></td>
        <td class="py-2 px-3 text-gray-500">
          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">good</code> ✓
        </td>
      </tr>
      <tr class="border-b border-gray-50 bg-gray-50/50">
        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Rule</td>
        <td class="py-2 px-3 text-gray-500">
          <code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">bad</code> ✗ →
          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">good</code>
        </td>
      </tr>
      <tr class="bg-gray-50/50">
        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">Rule</td>
        <td class="py-2 px-3 text-gray-500">
          <code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">preferred</code> over
          <code class="font-mono bg-gray-200 text-gray-600 border border-gray-300 px-1.5 py-0.5 rounded-full text-[10px]">deprecated</code>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```
Row shading: alternate rows get `bg-gray-50/50`. Rule column keywords use panel color (`bg-COLOR-100 text-COLOR-700 border border-COLOR-200`).

### `comparison-strip` — Use for two equivalent forms (e.g. single vs double quotes)
```html
<div class="rounded-xl overflow-hidden border border-COLOR-100">
  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-COLOR-50 to-COLOR2-50 border-b border-COLOR-100">
    <span class="iconify text-COLOR-500 text-xs" data-icon="ICON"></span>
    <p class="text-[10px] font-bold uppercase tracking-widest text-COLOR-500">LABEL</p>
  </div>
  <div class="flex gap-0 bg-white">
    <div class="flex-1 flex flex-col items-center justify-center px-3 py-3 border-r border-COLOR-50">
      <code class="text-sm font-mono font-bold text-COLOR-700 bg-COLOR-100 border border-COLOR-200 px-2 py-0.5 rounded mb-1">ITEM_A</code>
      <span class="text-[10px] font-semibold text-COLOR-600 bg-COLOR-100 border border-COLOR-200 px-2 py-0.5 rounded-full">Label A</span>
    </div>
    <div class="flex items-center justify-center px-3 text-COLOR-300 text-base font-black">=</div>
    <div class="flex-1 flex flex-col items-center justify-center px-3 py-3 border-r border-COLOR-50">
      <code class="text-sm font-mono font-bold text-COLOR-700 bg-COLOR-100 border border-COLOR-200 px-2 py-0.5 rounded mb-1">ITEM_B</code>
      <span class="text-[10px] font-semibold text-COLOR-600 bg-COLOR-100 border border-COLOR-200 px-2 py-0.5 rounded-full">Label B</span>
    </div>
    <div class="flex items-center justify-center px-3 text-COLOR-300 text-base font-black">→</div>
    <div class="flex-1 flex flex-col items-center justify-center px-3 py-3">
      <span class="iconify text-xl text-green-500 mb-1" data-icon="fa6-solid:circle-check"></span>
      <span class="text-[10px] font-bold text-green-700 bg-green-100 border border-green-200 px-2 py-0.5 rounded-full">RESULT</span>
    </div>
  </div>
</div>
```
Separator can be `=` or `→`. Result badge is always green (`bg-green-100 text-green-700 border-green-200`).

### `operators-table` — Use for arithmetic / comparison / logical operators
```html
<div class="rounded-xl overflow-hidden border border-COLOR-100">
  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-COLOR-50 to-COLOR2-50 border-b border-COLOR-100">
    <span class="iconify text-COLOR-500 text-xs" data-icon="fa6-solid:calculator"></span>
    <p class="text-[10px] font-bold uppercase tracking-widest text-COLOR-500">LABEL</p>
  </div>
  <table class="w-full text-xs border-collapse bg-white">
    <thead>
      <tr class="border-b border-COLOR-50">
        <th class="py-2 px-3 text-left font-bold text-COLOR-600 w-12">Op</th>
        <th class="py-2 px-3 text-left font-bold text-COLOR-600">Meaning</th>
        <th class="py-2 px-3 text-left font-bold text-COLOR-600">Example</th>
      </tr>
    </thead>
    <tbody>
      <tr class="border-b border-gray-50">
        <td class="py-2 px-3"><code class="font-mono bg-COLOR-100 text-COLOR-800 border border-COLOR-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">+</code></td>
        <td class="py-2 px-3 text-gray-500">Add</td>
        <td class="py-2 px-3"><code class="font-mono bg-COLOR-50 text-COLOR-700 border border-COLOR-200 px-1.5 py-0.5 rounded text-[10px]">3 + 4 → 7</code></td>
      </tr>
      <tr class="border-b border-gray-50 bg-gray-50/40"><!-- alternate rows get bg-gray-50/40 -->
        <!-- repeat rows ... -->
      </tr>
    </tbody>
  </table>
</div>
```
Example column uses `bg-COLOR-50` (not `-100`) — intentional subtle distinction from the operator pill.

### `comparison-table` — Use to compare two related types side by side
```html
<div class="rounded-xl overflow-hidden border border-COLOR-100">
  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-COLOR-50 to-COLOR2-50 border-b border-COLOR-100">
    <span class="iconify text-COLOR-500 text-xs" data-icon="fa6-solid:scale-balanced"></span>
    <p class="text-[10px] font-bold uppercase tracking-widest text-COLOR-500">TYPE_A vs TYPE_B</p>
  </div>
  <table class="w-full text-xs border-collapse bg-white">
    <thead>
      <tr class="border-b border-COLOR-50">
        <th class="py-2 px-3 text-left font-bold text-gray-400 w-1/3"></th>
        <th class="py-2 px-3 text-left"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-COLA-100 text-COLA-700 border border-COLA-200 text-[10px] font-bold">TYPE_A</span></th>
        <th class="py-2 px-3 text-left"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-COLB-100 text-COLB-700 border border-COLB-200 text-[10px] font-bold">TYPE_B</span></th>
      </tr>
    </thead>
    <tbody>
      <tr class="border-b border-gray-50">
        <td class="py-2 px-3 font-semibold text-gray-600">Example</td>
        <td class="py-2 px-3"><code class="font-mono bg-COLA-100 text-COLA-700 border border-COLA-200 px-1 rounded">VALUE_A</code></td>
        <td class="py-2 px-3"><code class="font-mono bg-COLB-100 text-COLB-800 border border-COLB-200 px-1 rounded">VALUE_B</code></td>
      </tr>
      <tr class="border-b border-gray-50 bg-gray-50/40">
        <td class="py-2 px-3 font-semibold text-gray-600">Row label</td>
        <td class="py-2 px-3"><span class="text-red-400 font-bold">✗</span> <span class="text-gray-400">No</span></td>
        <td class="py-2 px-3"><span class="text-green-500 font-bold">✓</span> <span class="text-gray-400">Yes</span></td>
      </tr>
      <tr>
        <td class="py-2 px-3 font-semibold text-gray-600">Use for</td>
        <td class="py-2 px-3 text-gray-500">…</td>
        <td class="py-2 px-3 text-gray-500">…</td>
      </tr>
    </tbody>
  </table>
</div>
```
Column A and B each get their own color (`COLA`, `COLB`). Text-only rows use plain `text-gray-500`.

### `true-false-cards` — Use only for boolean concepts
```html
<div class="grid grid-cols-2 gap-3">
  <div class="rounded-xl border border-green-200 overflow-hidden shadow-sm">
    <div class="bg-gradient-to-br from-green-400 to-emerald-500 px-3 py-2 flex items-center gap-2">
      <span class="iconify text-white text-base" data-icon="fa6-solid:circle-check"></span>
      <span class="text-sm font-black text-white">True</span>
    </div>
    <div class="bg-green-50 px-3 py-2">
      <code class="text-[11px] font-mono text-green-700">is_active = True</code>
      <p class="text-[10px] text-gray-500 mt-1">Condition is met / yes</p>
    </div>
  </div>
  <div class="rounded-xl border border-red-200 overflow-hidden shadow-sm">
    <div class="bg-gradient-to-br from-red-400 to-rose-500 px-3 py-2 flex items-center gap-2">
      <span class="iconify text-white text-base" data-icon="fa6-solid:circle-xmark"></span>
      <span class="text-sm font-black text-white">False</span>
    </div>
    <div class="bg-red-50 px-3 py-2">
      <code class="text-[11px] font-mono text-red-600">is_active = False</code>
      <p class="text-[10px] text-gray-500 mt-1">Condition not met / no</p>
    </div>
  </div>
</div>
```

---

## CSS Requirements

Check the `<style>` block. If these four rules are missing under `Key Concepts sidebar tabs (.kc-tab / .kc-tab-active)`, add them:

```css
.kc-tab-active { background: #fdf0f7; }
.kc-tab:not(.kc-tab-active):hover { background: #f9fafb; }
.kc-panel-anim { animation: kcFadeIn 0.25s ease-out; }
@keyframes kcFadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
```

## Required JavaScript

Check the `<script>` block. If `kcColors` and `switchKcTab` are missing, add them:

```javascript
const kcColors = [
  { num: '#CB187D', numShadow: 'rgba(203,24,125,0.25)', activeBg: '#fdf0f7' },  // pink
  { num: '#7c3aed', numShadow: 'rgba(124,58,237,0.25)', activeBg: '#f5f3ff' },  // violet
  { num: '#2563eb', numShadow: 'rgba(37,99,235,0.25)',  activeBg: '#eff6ff' },  // blue
  { num: '#059669', numShadow: 'rgba(5,150,105,0.25)',  activeBg: '#ecfdf5' },  // emerald
  { num: '#d97706', numShadow: 'rgba(217,119,6,0.25)',  activeBg: '#fffbeb' },  // amber
];
function switchKcTab(idx) {
  const c = kcColors[idx % kcColors.length];
  const tabs = document.querySelectorAll('.kc-tab');
  const panels = document.querySelectorAll('.kc-panel');
  const indicator = document.querySelector('.kc-indicator');
  tabs.forEach((t, i) => {
    const num = t.querySelector('.kc-tab-num');
    const label = t.querySelector('.kc-tab-label');
    if (i === idx) {
      t.classList.add('kc-tab-active'); t.style.background = c.activeBg;
      if (num) { num.style.background = c.num; num.style.color = '#fff'; num.style.boxShadow = '0 2px 8px ' + c.numShadow; }
      if (label) { label.style.color = '#111827'; }
    } else {
      t.classList.remove('kc-tab-active'); t.style.background = '';
      if (num) { num.style.background = '#f3f4f6'; num.style.color = '#9ca3af'; num.style.boxShadow = 'none'; }
      if (label) { label.style.color = '#9ca3af'; }
    }
  });
  if (indicator && tabs[idx]) { indicator.style.top = tabs[idx].offsetTop + 'px'; indicator.style.height = tabs[idx].offsetHeight + 'px'; indicator.style.background = c.num; }
  panels.forEach((p, i) => { if (i === idx) { p.classList.remove('hidden'); p.classList.remove('kc-panel-anim'); void p.offsetWidth; p.classList.add('kc-panel-anim'); } else { p.classList.add('hidden'); } });
  const visible = panels[idx]; if (visible && window.Prism) Prism.highlightAllUnder(visible);
}
```

---

## What NOT to Change

- Never modify anything outside `<section id="key-concepts">` … `</section>`
- Section header icon is always `fa6-solid:book-open`
- Section body: `px-6 py-7` (not `px-8`)
- Panel body: `p-5 space-y-4` (not `px-6 py-6`)
- Panel right column: `md:pl-5` (not `md:pl-6`)
- Body text: `text-xs text-gray-600 leading-relaxed` (not `text-sm`)
- Code block icon: `data-width="14" data-height="14"` (not `16`)
- Gradient top bar: `h-1` (not `h-1.5`)
- `.kc-tab-num` circle: `rounded-full` (not `rounded-lg`)
- Tip callout always matches panel color — never amber
- `<code>` pills in tip: `-200` bg + `-300` border (never `-50` or `-100`)
- `<code>` pills in definition/widget: `-100` bg + `-200` border (never `-50`)
- No wrapper div around the definition `<p>` (no `border-l-2` accent bar)
- Use `.kc-tab` / `.kc-panel` — never `.tab-btn` / `.tab-panel`
- Code blocks use Style B (`bg-code shadow-md`) — never Style A (`border-gray-800 bg-[#181825]`)
- No traffic-light dots in code block headers

## Output

1. Replace `<section id="key-concepts">` … `</section>` with the rendered HTML.
2. Add `kcColors` + `switchKcTab` to the `<script>` block if missing.
3. Add the four CSS rules to the `<style>` block if missing.
4. Confirm no syntax errors.