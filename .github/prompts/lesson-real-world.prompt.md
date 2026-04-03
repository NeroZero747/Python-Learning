---
mode: agent
description: "Redesign the #real-world section of a lesson. Scans all other lessons first to identify which layout types are already in use, then selects one from the catalog that has NOT been used yet. Every lesson gets a structurally unique section — same topic content, different visual presentation."
---

Redesign the `#real-world` section of `TARGET_FILE`. The layout you choose **must be different** from every other lesson's real-world section. Follow the steps below in order.

---

## Required Input

| Variable | Value |
|---|---|
| `TARGET_FILE` | Absolute path to the lesson HTML file to update |

---

## Step 1 — Audit existing layouts

Before writing anything, scan every other lesson file in the same folder as `TARGET_FILE` and identify which layout type each one uses. Map them against the **Layout Catalog** in Step 2.

Build a table like this (fill in from your scan):

| Lesson | Layout used |
|---|---|
| lesson01 | metric-cards |
| lesson02 | inbox-gotcha |
| lesson03 | ? |
| … | … |

---

## Step 2 — Layout Catalog

Each entry has a **slug** (used for tracking), a **description** of its visual identity, and the **HTML pattern** to use. Pick the first unused slug for `TARGET_FILE`.

---

### Layout A — `metric-cards`

**Visual:** 3 large centered gradient icon cards + a 2-column before/after table below.
**Best for:** concepts where you want to show the output of a function (a return value or result) across 3 scenarios.

```html
<p class="text-sm text-gray-600 leading-relaxed">INTRO</p>

<div class="grid grid-cols-1 md:grid-cols-3 gap-4">

  <!-- Card — repeat 3x, each with a different color token -->
  <div class="relative rounded-2xl overflow-hidden border BORDER bg-gradient-to-br BG px-6 py-6 text-center">
    <div class="flex flex-col items-center gap-3">
      <span class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br ICON_FROM ICON_TO shadow-lg SHADOW">
        <span class="iconify text-white text-2xl" data-icon="ICON"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-800 leading-snug">HEADLINE</h3>
      <p class="text-xs text-gray-500 leading-relaxed">BODY — mention <code class="font-mono CODE_COLOR">function()</code> inline.</p>
      <div class="flex items-center gap-1.5 mt-1 px-3 py-1.5 rounded-full PILL_BG PILL_BORDER">
        <span class="iconify PILL_TEXT text-[11px]" data-icon="fa6-solid:arrow-right-from-bracket"></span>
        <span class="text-[11px] font-semibold PILL_TEXT">returns <code class="font-mono">RETURN_VALUE</code></span>
      </div>
    </div>
  </div>

</div>

<!-- Before/after table -->
<div class="rounded-xl border border-gray-100 overflow-hidden">
  <div class="grid grid-cols-2">
    <div class="border-r border-gray-100">
      <div class="flex items-center gap-2 px-4 py-3 bg-red-50 border-b border-red-100">
        <span class="iconify text-red-400 text-sm shrink-0" data-icon="fa6-solid:circle-xmark"></span>
        <p class="text-xs font-bold text-red-500 uppercase tracking-wide">Without TOPIC</p>
      </div>
      <div class="px-4 py-4 space-y-3">
        <!-- 3 rows: flex items-start gap-2.5 + iconify xmark + text-xs text-gray-500 -->
      </div>
    </div>
    <div>
      <div class="flex items-center gap-2 px-4 py-3 bg-[#fdf0f7] border-b border-[#f5c6e0]">
        <span class="iconify text-[#CB187D] text-sm shrink-0" data-icon="fa6-solid:circle-check"></span>
        <p class="text-xs font-bold text-[#CB187D] uppercase tracking-wide">With TOPIC</p>
      </div>
      <div class="px-4 py-4 space-y-3">
        <!-- 3 rows: flex items-start gap-2.5 + iconify check emerald + text-xs text-gray-500 -->
      </div>
    </div>
  </div>
</div>
```

**Color token reference** (use a different one per card):

| Token | Border | BG | Icon from | Icon to | Shadow | Pill bg | Pill border | Pill text |
|---|---|---|---|---|---|---|---|---|
| violet | `border-violet-100` | `from-violet-50 via-white to-purple-50` | `from-violet-500` | `to-purple-600` | `shadow-violet-200` | `bg-violet-100` | `border-violet-200` | `text-violet-700` |
| pink | `border-pink-100` | `from-pink-50 via-white to-rose-50` | `from-[#CB187D]` | `to-[#e84aad]` | `shadow-pink-200` | `bg-pink-100` | `border-pink-200` | `text-[#CB187D]` |
| emerald | `border-emerald-100` | `from-emerald-50 via-white to-teal-50` | `from-emerald-500` | `to-teal-600` | `shadow-emerald-200` | `bg-emerald-100` | `border-emerald-200` | `text-emerald-700` |
| blue | `border-blue-100` | `from-blue-50 via-white to-indigo-50` | `from-blue-500` | `to-indigo-600` | `shadow-blue-200` | `bg-blue-100` | `border-blue-200` | `text-blue-700` |
| amber | `border-amber-100` | `from-amber-50 via-white to-orange-50` | `from-amber-400` | `to-orange-500` | `shadow-amber-200` | `bg-amber-100` | `border-amber-200` | `text-amber-700` |

---

### Layout B — `inbox-gotcha`

**Visual:** 3 file/ticket inbox cards with a dark IDE-style header bar per card showing a filename and type badge. Each card has a source system label, description, amber gotcha box, a "Loaded with:" code badge, and an "Unlocks:" line. Below: 2 wide numbered habit cards + amber tip.
**Best for:** lessons about loading or importing data where files have real-world quirks and silent failure modes.

```html
<p class="text-sm text-gray-600 leading-relaxed">INTRO</p>

<div>
  <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">GRID_LABEL</p>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4">

    <!-- One card per file type — repeat 3x -->
    <div class="rounded-2xl overflow-hidden border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300">
      <div class="flex items-center justify-between px-4 py-2.5 bg-[#1f2937]">
        <div class="flex items-center gap-2">
          <span class="iconify text-COLOR-400 text-xs" data-icon="ICON"></span>
          <span class="text-[10px] font-bold text-gray-300 uppercase tracking-wider">FILENAME</span>
        </div>
        <span class="text-[9px] font-bold px-1.5 py-0.5 rounded bg-COLOR-900/40 text-COLOR-300 border border-COLOR-800/40">TYPE_BADGE</span>
      </div>
      <div class="bg-white px-4 py-4 space-y-3">
        <div class="flex items-center gap-2">
          <span class="iconify text-gray-300 text-[11px]" data-icon="SYSTEM_ICON"></span>
          <span class="text-[11px] text-gray-400">From: SOURCE_SYSTEM</span>
        </div>
        <p class="text-xs text-gray-600 leading-relaxed">FILE_DESCRIPTION</p>
        <div class="rounded-lg bg-amber-50 border border-amber-100 px-3 py-2">
          <p class="text-[10px] font-semibold text-amber-700 leading-snug">&#9888; Gotcha: GOTCHA_TEXT</p>
        </div>
        <div class="flex flex-wrap items-center gap-2">
          <span class="text-[10px] text-gray-400">Loaded with:</span>
          <code class="text-[10px] font-mono font-bold px-1.5 py-0.5 rounded bg-COLOR-50 text-COLOR-700 border border-COLOR-100">FUNCTION_CALL</code>
        </div>
        <p class="text-[11px] text-gray-500 leading-snug"><span class="font-semibold text-gray-700">Unlocks:</span> UNLOCKS_TEXT</p>
      </div>
    </div>

  </div>
</div>

<!-- 2-step habit block -->
<div>
  <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">HABIT_LABEL</p>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
    <div class="flex items-start gap-4 rounded-2xl border border-gray-100 bg-gray-50 px-5 py-4 hover:border-[#f5c6e0] transition-colors">
      <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-black shadow-md shrink-0 mt-0.5">1</span>
      <div>
        <p class="text-sm font-bold text-gray-800 mb-1">STEP1_TITLE</p>
        <p class="text-xs text-gray-500 leading-relaxed">STEP1_BODY</p>
      </div>
    </div>
    <div class="flex items-start gap-4 rounded-2xl border border-gray-100 bg-gray-50 px-5 py-4 hover:border-[#f5c6e0] transition-colors">
      <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-black shadow-md shrink-0 mt-0.5">2</span>
      <div>
        <p class="text-sm font-bold text-gray-800 mb-1">STEP2_TITLE</p>
        <p class="text-xs text-gray-500 leading-relaxed">STEP2_BODY</p>
      </div>
    </div>
  </div>
  <div class="mt-4 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
    <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
    <p class="text-sm text-gray-600">TIP_TEXT</p>
  </div>
</div>
```

---

### Layout C — `day-in-the-life`

**Visual:** A horizontal (or 2×2 on mobile) timeline of 4 micro-events during a single work day. Each event is a card with a time stamp, a short task title, and 2 sentences showing exactly where the lesson concept is used. A closing amber tip wraps up the narrative.
**Best for:** lessons whose concept appears at multiple distinct points in a single analysis workflow (filtering, joining, transforming, aggregating).

```html
<p class="text-sm text-gray-600 leading-relaxed">INTRO</p>

<div>
  <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">TIMELINE_LABEL</p>
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">

    <!-- One event card per time slot — repeat 4x -->
    <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
      <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
      <div class="px-4 py-4">
        <div class="flex items-center justify-between mb-3">
          <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0">
            <span class="iconify text-white text-xs" data-icon="ICON"></span>
          </span>
          <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wider">TIME</span>
        </div>
        <p class="text-xs font-bold text-gray-800 mb-1.5">TASK_TITLE</p>
        <p class="text-xs text-gray-500 leading-relaxed mb-3">TASK_BODY — name the concept inline.</p>
        <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-bold bg-pink-50 text-[#CB187D] border border-pink-100">CONCEPT_BADGE</span>
      </div>
    </div>

  </div>
</div>

<div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">TIP_TEXT</p>
</div>
```

Use four different accent colors for the top bar across the four cards (pink → violet → blue → emerald).

---

### Layout D — `roles-board`

**Visual:** 3 role/persona cards styled like "team member profile" tiles. Each card has a job title, department tag, a description of their specific daily task, the exact code they'd run, and what it returns them. A closing "What every role shares" row below the grid ties it together.
**Best for:** lessons where different job roles on the same team use the same concept for different things (e.g. analysts, coordinators, managers all filtering or joining data differently).

```html
<p class="text-sm text-gray-600 leading-relaxed">INTRO</p>

<div>
  <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">ROLES_LABEL</p>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4">

    <!-- Role card — repeat 3x with different accent colors -->
    <div class="rounded-2xl border BORDER bg-white overflow-hidden shadow-sm hover:shadow-md transition-all duration-300">
      <div class="h-1 bg-gradient-to-r ACCENT_FROM ACCENT_TO"></div>
      <div class="px-5 py-5 space-y-3">
        <div class="flex items-center gap-3">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br ACCENT_FROM ACCENT_TO shrink-0 shadow-md">
            <span class="iconify text-white text-base" data-icon="ICON"></span>
          </span>
          <div>
            <p class="text-sm font-bold text-gray-800">JOB_TITLE</p>
            <p class="text-xs text-gray-400">DEPARTMENT</p>
          </div>
        </div>
        <p class="text-xs text-gray-600 leading-relaxed">TASK_DESCRIPTION — mention the concept and the exact call they use.</p>
        <div class="rounded-lg bg-gray-50 border border-gray-100 px-3 py-2">
          <p class="text-[10px] font-mono text-gray-500">returns <span class="RETURN_COLOR font-bold">RETURN_VAR</span></p>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- Shared insight row -->
<div class="rounded-xl border border-gray-100 bg-gray-50 px-5 py-4 flex items-start gap-4">
  <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0 mt-0.5">
    <span class="iconify text-white text-sm" data-icon="fa6-solid:users"></span>
  </span>
  <div>
    <p class="text-sm font-bold text-gray-800 mb-1">SHARED_INSIGHT_TITLE</p>
    <p class="text-xs text-gray-500 leading-relaxed">SHARED_INSIGHT_BODY</p>
  </div>
</div>
```

---

### Layout E — `task-ticket`

**Visual:** One large "work order / task ticket" card that looks like an internal Jira/Confluence ticket, listing 4–5 sub-tasks, each with a status badge (Done ✓), the function used, and the result. A side column shows "Data Available" vs "Data Needed" as two stacked pills.
**Best for:** lessons about data transformation, aggregation, or reporting where the reader can see a realistic end-to-end mini-project being completed step by step.

```html
<p class="text-sm text-gray-600 leading-relaxed">INTRO</p>

<div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
  <!-- Ticket header -->
  <div class="flex items-center justify-between px-5 py-3 bg-gray-50 border-b border-gray-100">
    <div class="flex items-center gap-3">
      <span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-xs" data-icon="fa6-solid:ticket"></span>
      </span>
      <div>
        <p class="text-xs font-bold text-gray-800">TICKET_TITLE</p>
        <p class="text-[10px] text-gray-400">Assigned to: DATA_TEAM · Due: TODAY</p>
      </div>
    </div>
    <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-100">In Progress</span>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-3">
    <!-- Tasks column (spans 2) -->
    <div class="md:col-span-2 px-5 py-4 space-y-3 border-r border-gray-100">
      <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-2">Sub-tasks</p>

      <!-- One sub-task row — repeat 4–5x -->
      <div class="flex items-start gap-3">
        <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-50 border border-emerald-100 shrink-0 mt-0.5">
          <span class="iconify text-emerald-500 text-[10px]" data-icon="fa6-solid:check"></span>
        </span>
        <div class="flex-1 min-w-0">
          <p class="text-xs font-semibold text-gray-700">SUBTASK_TITLE</p>
          <p class="text-[11px] text-gray-400 leading-snug">SUBTASK_DETAIL — name the function/concept.</p>
        </div>
        <code class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-indigo-50 text-indigo-600 border border-indigo-100 shrink-0 whitespace-nowrap">FUNCTION</code>
      </div>

    </div>

    <!-- Side column: data availability -->
    <div class="px-4 py-4 space-y-4">
      <div>
        <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-2">Data available</p>
        <div class="space-y-1.5">
          <!-- 2–3 pills: bg-emerald-50 text-emerald-700 border-emerald-100 -->
          <span class="flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-700 border border-emerald-100">
            <span class="iconify text-[10px]" data-icon="fa6-solid:check"></span> DATA_SOURCE
          </span>
        </div>
      </div>
      <div>
        <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-2">Needed output</p>
        <div class="space-y-1.5">
          <!-- 2–3 pills: bg-pink-50 text-[#CB187D] border-pink-100 -->
          <span class="flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">
            <span class="iconify text-[10px]" data-icon="fa6-solid:arrow-right-from-bracket"></span> OUTPUT_NAME
          </span>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">TIP_TEXT</p>
</div>
```

---

### Layout F — `industry-spotlight`

**Visual:** 3 industry cards (e.g. healthcare, retail, finance) each showing a specific named dataset, the exact operation performed, and what it produces — framed as "what this means for the business". Below: a pink horizontal "shared pattern" banner that names the one common thread across all three industries.
**Best for:** lessons covering broadly applicable concepts (joins, exports, missing data, groupby) where showing diverse industries reinforces universality.

```html
<p class="text-sm text-gray-600 leading-relaxed">INTRO</p>

<div>
  <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">SPOTLIGHT_LABEL</p>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4">

    <!-- Industry card — repeat 3x -->
    <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md transition-all duration-300">
      <div class="flex items-center gap-3 px-4 py-3 bg-gray-50 border-b border-gray-100">
        <span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-gradient-to-br ACCENT_FROM ACCENT_TO shrink-0">
          <span class="iconify text-white text-xs" data-icon="INDUSTRY_ICON"></span>
        </span>
        <div>
          <p class="text-xs font-bold text-gray-800">INDUSTRY_NAME</p>
          <p class="text-[10px] text-gray-400">DATASET_NAME</p>
        </div>
      </div>
      <div class="px-4 py-4 space-y-2.5">
        <p class="text-xs text-gray-600 leading-relaxed">SCENARIO — what the analyst does with the concept on this dataset.</p>
        <div class="flex items-center gap-2">
          <code class="text-[10px] font-mono font-bold px-1.5 py-0.5 rounded bg-indigo-50 text-indigo-700 border border-indigo-100">FUNCTION_CALL</code>
        </div>
        <p class="text-[11px] text-emerald-600 font-semibold leading-snug">&#x2192; BUSINESS_OUTCOME</p>
      </div>
    </div>

  </div>
</div>

<!-- Shared pattern banner -->
<div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-4">
  <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[3rem] font-black text-white/10 leading-none select-none pointer-events-none">&#x221E;</span>
  <div class="relative flex items-center gap-4">
    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">
      <span class="iconify text-white text-base" data-icon="fa6-solid:share-nodes"></span>
    </span>
    <div>
      <p class="text-xs font-bold text-white uppercase tracking-widest mb-0.5">The common thread</p>
      <p class="text-sm text-white/90">SHARED_PATTERN_TEXT</p>
    </div>
  </div>
</div>
```

---

### Layout G — `checklist-scenario`

**Visual:** A single realistic analysis task shown as a numbered checklist of 5 steps. Each step has a checkbox (always ticked ✓), the exact line of Python used, and one sentence of plain English explaining what that line produces. Below: a 2-column "what you needed" vs "what you got" mini summary grid.
**Best for:** lessons that are naturally sequential (handling missing data, exporting, writing to databases) where the steps must be done in order.

```html
<p class="text-sm text-gray-600 leading-relaxed">INTRO</p>

<div>
  <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">CHECKLIST_LABEL</p>
  <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm divide-y divide-gray-100">

    <!-- One checklist row — repeat 5x, alternating bg-white and bg-gray-50/50 -->
    <div class="flex items-start gap-4 px-5 py-4 bg-white hover:bg-[#fdf0f7]/30 transition-colors">
      <span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-emerald-50 border border-emerald-100 shrink-0 mt-0.5">
        <span class="iconify text-emerald-500 text-[11px]" data-icon="fa6-solid:check"></span>
      </span>
      <div class="flex-1 min-w-0">
        <div class="flex items-center gap-2 mb-1">
          <p class="text-xs font-bold text-gray-800">STEP_TITLE</p>
          <code class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-indigo-50 text-indigo-600 border border-indigo-100">FUNCTION</code>
        </div>
        <p class="text-[11px] text-gray-500 leading-snug">STEP_RESULT — one plain sentence.</p>
      </div>
    </div>

  </div>
</div>

<!-- Summary grid -->
<div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
  <div class="rounded-xl border border-red-100 bg-red-50 px-4 py-3">
    <p class="text-[10px] font-bold uppercase tracking-widest text-red-400 mb-2">You started with</p>
    <!-- 2–3 items: flex items-center gap-2 + iconify xmark red + text-xs text-gray-600 -->
  </div>
  <div class="rounded-xl border border-emerald-100 bg-emerald-50 px-4 py-3">
    <p class="text-[10px] font-bold uppercase tracking-widest text-emerald-600 mb-2">You ended with</p>
    <!-- 2–3 items: flex items-center gap-2 + iconify check emerald + text-xs text-gray-600 -->
  </div>
</div>
```

---

### Layout H — `data-before-after`

**Visual:** Two wide panels side by side — left panel shows a mocked "before" DataFrame (a simple 4-row HTML table with a raw/messy/incomplete state), right panel shows the "after" DataFrame (cleaned, transformed, or enriched). Annotations beside each panel call out the specific change made. Below: a single amber tip.
**Best for:** lessons where the transformation of data is the point and a visual table diff makes it instantly obvious what changed (transforming data, handling missing data, parquet/performance).

```html
<p class="text-sm text-gray-600 leading-relaxed">INTRO</p>

<div>
  <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">BEFORE_AFTER_LABEL</p>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

    <!-- Before panel -->
    <div class="rounded-2xl border border-red-100 overflow-hidden shadow-sm">
      <div class="flex items-center gap-2 px-4 py-2.5 bg-red-50 border-b border-red-100">
        <span class="iconify text-red-400 text-sm" data-icon="fa6-solid:circle-xmark"></span>
        <p class="text-xs font-bold text-red-500">Before: BEFORE_LABEL</p>
      </div>
      <div class="px-4 py-3 overflow-x-auto">
        <table class="w-full text-[11px] font-mono border-collapse">
          <thead>
            <tr class="border-b border-gray-100">
              <!-- TH: px-2 py-1 text-left text-[10px] font-bold text-gray-400 uppercase -->
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-50">
            <!-- 4 rows: TD px-2 py-1.5 text-gray-500 — mark bad cells with text-red-400 -->
          </tbody>
        </table>
      </div>
      <div class="px-4 pb-3 space-y-1.5">
        <!-- 2 annotations: flex items-start gap-2 + iconify xmark red text-[11px] + text-[11px] text-red-500 -->
      </div>
    </div>

    <!-- After panel -->
    <div class="rounded-2xl border border-emerald-100 overflow-hidden shadow-sm">
      <div class="flex items-center gap-2 px-4 py-2.5 bg-emerald-50 border-b border-emerald-100">
        <span class="iconify text-emerald-500 text-sm" data-icon="fa6-solid:circle-check"></span>
        <p class="text-xs font-bold text-emerald-600">After: AFTER_LABEL</p>
      </div>
      <div class="px-4 py-3 overflow-x-auto">
        <table class="w-full text-[11px] font-mono border-collapse">
          <thead>
            <tr class="border-b border-gray-100">
              <!-- same TH structure -->
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-50">
            <!-- 4 rows — mark fixed cells with text-emerald-600 font-semibold -->
          </tbody>
        </table>
      </div>
      <div class="px-4 pb-3 space-y-1.5">
        <!-- 2 annotations: iconify check emerald + text-[11px] text-emerald-600 -->
      </div>
    </div>

  </div>
</div>

<div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">TIP_TEXT</p>
</div>
```

---

## Step 3 — Selection rules

1. Build the audit table from Step 1.
2. Find the **first layout slug in the catalog** (A → B → C → D → E → F → G → H) that is **not already used** by another lesson.
3. Use that layout for `TARGET_FILE`. Do not use a layout marked as already in use, even if you think it would suit the topic better.
4. If all 8 layouts are already used, cycle back to A and pick the one used least frequently.

---

## Step 4 — Write the content

Fill every placeholder in the chosen layout template with content specific to `TARGET_FILE`'s lesson topic. Follow these writing rules for all text:

- **Be specific.** Name real quantities, data types, and actions — not vague capabilities.
- **Human scale.** Lead with relatable numbers ("500 orders", "12 regional offices") so the reader feels the weight of the problem before seeing the solution.
- **Use "you".** "You write the function once" is clearer than "the function is written once".
- **One idea per sentence.** Keep prose sentences under 20 words.
- **No jargon** unless it was taught in this lesson.
- **American English only.** "optimize" not "optimise", "color" not "colour", "analyze" not "analyse".
- **No code blocks** in prose — all syntax appears only in `<code class="font-mono">` inline spans or in the explicit code areas defined by the chosen layout.

---

## Step 5 — Apply the change

1. Read `TARGET_FILE`.
2. Locate the `#real-world` section. Find the opening `<div class="bg-white px-8 py-7` and its matching closing `</div>` just before `</section>`.
3. Replace the entire body contents (everything inside `<div class="bg-white px-8 py-7 space-y-N">`) with the new layout HTML.
4. Keep the outer section shell unchanged — the section `id`, the header icon (`fa6-solid:briefcase`), and the "Real-World Use" title must not change. Update only the subtitle `line-clamp-1` text to match the lesson topic.
5. Write the file and verify the change by re-reading the section to confirm it starts and ends correctly.

