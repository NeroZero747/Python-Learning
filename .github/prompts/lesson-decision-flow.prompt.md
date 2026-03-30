---
mode: "agent"
description: "Rewrite the #decision-flow section for a lesson HTML file with rich content and Style A code blocks (dark-chrome, no terminal pane)"
---

<!--
FILL IN BEFORE RUNNING
───────────────────────────────────────────────────
TARGET_FILE      Path to the lesson HTML file
TOPIC            Lesson topic in plain English (e.g. "the Git workflow")

Flowchart (nodes 2–4 are variable; 1 and 5 are always the same)
FLOW_CHART_TITLE  Label above the chart (e.g. "How Git Saves Your Work — Step by Step")
FLOW_LABEL_2      Node 2 label — the core action (e.g. "Stage Changes")
FLOW_LABEL_2_SUB  Node 2 subtitle — hint or command (e.g. "git add — pick what to include")
FLOW_LABEL_2_ICON Iconify icon for node 2 (e.g. "fa6-solid:layer-group")
FLOW_LABEL_3      Node 3 label — the decision/branch (e.g. "Commit Ready?")
FLOW_LABEL_3_SUB  Node 3 subtitle (e.g. "git status — review staging")
FLOW_LABEL_3_ICON Iconify icon for node 3 (e.g. "fa6-solid:circle-question")
FLOW_LABEL_4      Node 4 label — action after the decision (e.g. "Save Snapshot")
FLOW_LABEL_4_SUB  Node 4 subtitle (e.g. "git commit -m \"message\"")
FLOW_LABEL_4_ICON Iconify icon for node 4 (e.g. "fa6-solid:bookmark")

INTRO_PARAGRAPH   1–2 sentences: name the core term in bold + an everyday analogy
SECTION_HEADING   Bold sub-heading (e.g. "The Stage → Commit → Push Cycle — Every Time, In That Order")
SECTION_BODY      2–3 complete sentences explaining the concept for a beginner

CODE_LEADUP       One sentence telling the reader what to look for in the code below
CODE_FILENAME     Filename shown in the pill (e.g. "git_workflow.sh")
CODE_LANG         Language class: "python" or "bash"
CODE_ICON         Icon for the filename pill: "logos:python" for .py, "fa6-solid:terminal" for .sh
CODE_BODY         Code with at least one inline # comment per line (use HTML entities for <>&)

CARD_LABEL        Bold section label above the grid (e.g. "The Three Commands That Drive the Git Cycle")
CARD_INTRO_SENTENCE  One sentence introducing the cards
CARD_1_TITLE / CARD_1_SUBTITLE / CARD_1_COLOR / CARD_1_ICON / CARD_1_BODY
CARD_2_TITLE / CARD_2_SUBTITLE / CARD_2_COLOR / CARD_2_ICON / CARD_2_BODY
CARD_3_TITLE / CARD_3_SUBTITLE / CARD_3_COLOR / CARD_3_ICON / CARD_3_BODY
  (colors must all differ; use blue / emerald / violet or similar)

TIP_BODY          1–2 sentences: practical "so what" — no repetition of the intro analogy
───────────────────────────────────────────────────
-->

Rewrite the `#decision-flow` section body in the target lesson file using the structure and rules below.

## Writing style

Write for a smart colleague who has never written code. Use plain English, complete sentences, and "you". Keep sentences under 15 words. No filler phrases ("it is important to note", "essentially", etc.). Introduce every technical term with a brief plain-English explanation in the same sentence.

---

## Locate the section

Find `<section id="decision-flow">` in `TARGET_FILE`. Replace only the **body div** — the `<div class="bg-white px-8 py-7 ...">` directly after the section header. Do not touch the header or anything outside the section.

Outer wrapper: `<div class="bg-white px-8 py-7 space-y-6">`

---

## Block 1 — Intro paragraph

```html
<p class="text-sm text-gray-600 leading-relaxed">INTRO_PARAGRAPH — wrap the key term in <strong class="text-gray-800">…</strong>. Do not bold the analogy words.</p>
```

---

## Block 2 — Flowchart

```html
<div class="rounded-2xl border border-gray-100 bg-gray-50 px-5 pt-4 pb-6 overflow-x-auto">
  <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-4">FLOW_CHART_TITLE</p>
  <div class="flex items-start gap-0 min-w-[640px]">
    <!-- Node 1 (fixed) · Arrow · Node 2 · Arrow · Node 3 · Arrow · Node 4 · Arrow · Node 5 (fixed) -->
  </div>
</div>
```

### Node reference

| # | Shape | Gradient | Ring | Size | Notes |
|---|---|---|---|---|---|
| 1 | `rounded-full` | `from-pink-500 to-rose-600` | `ring-pink-100` | `w-14 h-14` | Fixed — icon `fa6-solid:play`, label "Program / Starts", sub "Python begins at line 1" |
| 2 | `rounded-2xl` | `from-violet-500 to-purple-600` | `ring-violet-100` | `w-14 h-14` | FLOW_LABEL_2 / _2_SUB / _2_ICON |
| 3 | `rounded-xl rotate-45` (icon gets `-rotate-45`) | `from-blue-500 to-indigo-600` | `ring-blue-100` | `w-12 h-12` | FLOW_LABEL_3 / _3_SUB / _3_ICON · add `style="margin-top:4px;"` on the icon div · label uses `mt-3` |
| 4 | `rounded-2xl` | `from-emerald-500 to-teal-600` | `ring-emerald-100` | `w-14 h-14` | FLOW_LABEL_4 / _4_SUB / _4_ICON |
| 5 | `rounded-full` | `from-gray-400 to-gray-600` | `ring-gray-100` | `w-14 h-14` | Fixed — icon `fa6-solid:flag-checkered`, label "Program / Ends", sub "Result is shown" |

**Node wrapper** (all nodes): `<div class="flex flex-col items-center shrink-0" style="width:115px;">`

**Icon div** (non-diamond): `<div class="w-14 h-14 rounded-SHAPE bg-gradient-to-br GRADIENT flex items-center justify-center shadow-lg ring-4 RING">`

**Label**: `<p class="text-[10px] font-bold text-gray-800 mt-2 text-center leading-tight">LABEL_LINE_1<br>LABEL_LINE_2</p>`

**Subtitle**: `<p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">SUBTITLE</p>`

### Arrow template (×4, between every pair of nodes)

Arrow color sequence: pink→violet → violet→blue → blue→emerald → emerald→gray.

```html
<div class="flex-1 flex items-center" style="padding-top:28px;">
  <div class="h-0.5 flex-1 bg-gradient-to-r from-[SRC]-300 to-[DST]-300"></div>
  <span class="iconify text-[DST]-300 text-xs -ml-px" data-icon="fa6-solid:chevron-right"></span>
</div>
```

---

## Block 3 — Sub-heading + paragraph

```html
<div class="space-y-2">
  <p class="text-sm font-semibold text-gray-800">SECTION_HEADING</p>
  <p class="text-sm text-gray-600 leading-relaxed">SECTION_BODY</p>
</div>
```

---

## Block 4 — Code block (Style A, dark-chrome)

**No traffic-light dots. No terminal output pane.** The `#decision-flow` section never has a terminal pane — that is `#code-examples` only.

```html
<div class="space-y-2">
  <p class="text-sm text-gray-600 leading-relaxed">CODE_LEADUP</p>
  <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
    <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
      <div class="flex items-center gap-3">
        <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
          <span class="iconify text-yellow-400 text-xs" data-icon="CODE_ICON" data-width="12" data-height="12"></span>
          <span class="text-[11px] font-semibold text-gray-400">CODE_FILENAME</span>
        </div>
      </div>
      <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
    </div>
    <div class="bg-code">
      <pre class="overflow-x-auto pre-reset"><code class="language-CODE_LANG">CODE_BODY</code></pre>
    </div>
  </div>
</div>
```

`CODE_BODY`: use `&lt;` / `&gt;` / `&amp;` HTML entities for `<` `>` `&` inside `<code>`.

---

## Block 5 — Three concept cards

```html
<div class="space-y-3">
  <p class="text-xs font-bold uppercase tracking-widest text-brand">CARD_LABEL</p>
  <p class="text-sm text-gray-600 leading-relaxed">CARD_INTRO_SENTENCE</p>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">

    <div class="rounded-xl border border-[COLOR]-100 bg-white overflow-hidden shadow-sm hover:shadow-md hover:border-[COLOR]-200 transition-all">
      <div class="h-1 bg-gradient-to-r from-[COLOR]-500 to-[COLOR]-400"></div>
      <div class="px-4 py-4">
        <div class="flex items-center gap-2.5 mb-2.5">
          <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-[COLOR]-50 shrink-0">
            <span class="iconify text-[COLOR]-500 text-base" data-icon="ICON"></span>
          </span>
          <div>
            <p class="text-sm font-bold text-gray-800 leading-tight">TITLE</p>
            <p class="text-[10px] text-gray-400 italic leading-tight">SUBTITLE</p>
          </div>
        </div>
        <p class="text-xs text-gray-500 leading-relaxed">BODY — complete sentence, inline <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">keyword</code> for any commands</p>
      </div>
    </div>

    <!-- repeat for CARD_2 and CARD_3 — each must use a different COLOR -->

  </div>
</div>
```

---

## Block 6 — Amber tip

```html
<div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">TIP_BODY — 1–2 sentences with new practical information. Do not repeat the intro analogy.</p>
</div>
```

---

## Quality checklist

Before writing HTML, confirm:
- [ ] `INTRO_PARAGRAPH` names the key term in `<strong>` and uses an everyday analogy
- [ ] Flowchart node labels describe what is happening — never "Step 1", "Step 2"
- [ ] Block 4 has **no terminal pane** and **no traffic-light dots**
- [ ] `CODE_BODY` has at least one inline `# comment` per line
- [ ] Each card body is a complete sentence (no fragments)
- [ ] All three card colors are different
- [ ] `TIP_BODY` adds new information not covered in the intro paragraph
