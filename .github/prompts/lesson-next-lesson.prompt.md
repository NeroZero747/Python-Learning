---
mode: "agent"
description: "Write or rewrite the #next-lesson section and bottom navigation bar for a lesson HTML file — a lesson badge, a 3-card 'What You Will Learn' preview grid, and a Previous / All Lessons / Next bottom nav. Matches the mod_01/lesson01 design standard."
---

Rewrite the `#next-lesson` section and the bottom navigation bar in the target lesson file using the structure and rules below. The section previews the next lesson at a high level so the learner knows what's coming. The bottom nav links to the previous lesson, the hub home page, and the next lesson. The design stays the same every lesson; only the content and links change.

---

## Inputs (fill in before running)

| Variable | Value |
|---|---|
| `TARGET_FILE` | Path to the lesson HTML file |
| `CURRENT_MODULE` | Module number (e.g. `2`) |
| `NEXT_LESSON_NUM` | Lesson number of the next lesson (e.g. `2`) |
| `NEXT_LESSON_TITLE` | Full title of the next lesson (e.g. `Variables & Data Types`) — use `&amp;` for `&` in HTML |
| `NEXT_LESSON_FILE` | Filename of the next lesson HTML (e.g. `lesson02_variables_data_types.html`) |
| `CARD1_ICON` | Iconify icon for preview card 1 (e.g. `fa6-solid:box`) |
| `CARD1_TEXT` | Short title for card 1 — what the learner will cover, written as a noun phrase (e.g. `What a Variable Is and How to Create One`) |
| `CARD2_ICON` | Iconify icon for preview card 2 |
| `CARD2_TEXT` | Short title for card 2 |
| `CARD3_ICON` | Iconify icon for preview card 3 |
| `CARD3_TEXT` | Short title for card 3 |
| `PREV_LESSON_FILE` | Relative path to the previous lesson HTML (e.g. `../mod_01_getting_started/lesson06_how_to_run_a_python_notebook_or_script.html`). Set to `NONE` if this is the first lesson of the track. |
| `PREV_LESSON_TITLE` | Display title of the previous lesson (e.g. `How to Run a Python Notebook or Script`). Ignored if `PREV_LESSON_FILE` is `NONE`. |
| `HUB_PATH` | Relative path to the hub home page from the lesson file (always `../../../hub_home_page.html`) |

---

## Writing rules for preview card text

- Each card title is a **noun phrase**, not a full sentence — it names what the learner will encounter, not what they will do.
- Write at a beginner level: avoid jargon the learner hasn't seen yet. Favor plain English ("What a Variable Is") over technical shorthand ("Variable declaration").
- Three cards is the standard — if the next lesson only has two strong topics, combine two related ideas into one card rather than padding with a weak third.
- Use `&amp;` instead of `&` in all card text inside HTML attributes and body text.
- Keep each card title under 60 characters so it fits cleanly on two lines at most.

---

## Section shell (keep unchanged)

Always preserve the outer section shell — do **not** change the section `id` (`next-lesson`), the `scroll-mt-24` class, the header icon (`fa6-solid:circle-arrow-right`), or the header title ("Next Lesson"). Only replace the `<div class="bg-white px-8 py-7 space-y-6">` body contents.

```html
<section id="next-lesson" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
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
      <!-- LESSON BADGE + CARD GRID GO HERE -->
    </div>
  </div>
</section>
```

---

## Lesson badge template

The badge shows the lesson number, module + lesson label, next lesson title, and a short "Next you will learn:" line.

```html
<div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
  <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
    <span class="text-white font-bold text-lg">NEXT_LESSON_NUM</span>
  </span>
  <div class="min-w-0">
    <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module CURRENT_MODULE · Lesson NEXT_LESSON_NUM</p>
    <h3 class="text-base font-bold text-gray-800">NEXT_LESSON_TITLE</h3>
    <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
  </div>
</div>
```

---

## Preview card grid template

Always 3 cards in a responsive `sm:grid-cols-3` grid. Each card has a pink icon square and a bold title.

```html
<div>
  <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">

    <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-sm" data-icon="CARD1_ICON"></span>
      </span>
      <div>
        <p class="text-sm font-semibold text-gray-700">CARD1_TEXT</p>
      </div>
    </div>

    <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-sm" data-icon="CARD2_ICON"></span>
      </span>
      <div>
        <p class="text-sm font-semibold text-gray-700">CARD2_TEXT</p>
      </div>
    </div>

    <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-sm" data-icon="CARD3_ICON"></span>
      </span>
      <div>
        <p class="text-sm font-semibold text-gray-700">CARD3_TEXT</p>
      </div>
    </div>

  </div>
</div>
```

---

## Bottom navigation bar template

The bottom nav goes **immediately after** the closing `</section>` of `#next-lesson`, as a bare `<section>` with no card wrapper. It always has three slots: Previous (left), All Lessons (center), Next (right).

- If `PREV_LESSON_FILE` is `NONE` (first lesson of the track), replace the Previous `<a>` with `<div class="flex-1"></div>`.
- If there is no next lesson (last lesson of the module), omit the Next `<a>` entirely.
- Hub path is always `HUB_PATH` — do not hardcode `../../../hub_home_page.html` unless that's the correct relative path.

```html
<section>
  <div class="flex flex-col sm:flex-row gap-3">

    <!-- Previous lesson (omit and use <div class="flex-1"></div> if first lesson) -->
    <a href="PREV_LESSON_FILE" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">PREV_LESSON_TITLE</p>
      </div>
    </a>

    <!-- All Lessons — always present -->
    <a href="HUB_PATH" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>

    <!-- Next lesson (omit entirely if last lesson of the module) -->
    <a href="NEXT_LESSON_FILE" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">NEXT_LESSON_TITLE</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>

  </div>
</section>
```

---

## Quality checklist

Before submitting, verify:

- [ ] Section `id` is `next-lesson` and `scroll-mt-24` class is present
- [ ] Lesson badge shows the correct module number, lesson number, and next lesson title
- [ ] All three preview cards have a unique icon and clear noun-phrase title
- [ ] Card text uses `&amp;` for any ampersands
- [ ] Bottom nav has all three slots: Previous (left), All Lessons (center), Next (right)
- [ ] If first lesson: Previous slot is `<div class="flex-1"></div>`, not an `<a>`
- [ ] If last lesson: Next `<a>` is omitted entirely
- [ ] All file paths are relative to the current lesson file — not absolute
- [ ] Section header icon, title, and subtitle are unchanged
