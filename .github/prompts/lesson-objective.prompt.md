---
mode: "agent"
description: "Write or rewrite the #objective section for a lesson HTML file"
---

Rewrite the `#objective` section in the target lesson file using the rules below.

---

## Writing Style — apply to all text you write

Objective cards are the first thing the reader sees. They need to be instantly clear.

- **Card titles:** Short, action-oriented, plain English — what they will be able to *do* after this lesson. No jargon.
- **Card descriptions:** One sentence only. Say what the learner will be able to do or understand — make it concrete. 12–18 words is the sweet spot.
- **Amber tip:** One sentence. Tell the reader why this lesson matters — connect it to a real task or outcome, not an abstract concept.
- **No filler.** Cut "it is important", "you will learn about", "this section covers".
- **American English only.** Use American spellings throughout — e.g. "optimize" not "optimise", "color" not "colour", "analyze" not "analyse".

---

## Inputs (fill in before running)

| Variable | Value |
|---|---|
| `TARGET_FILE` | Path to the lesson HTML file (e.g. `pages/track_01/mod_02_programming_foundations/lesson01_what_is_programming.html`) |
| `TOPIC` | Short lesson topic name used in the amber tip (e.g. `programming`, `variables`, `loops`) |
| `GOAL_1` through `GOAL_4` | The four learning goals for this lesson |

---

## Rules

### Card titles
- Maximum 5 words
- Start with a verb or noun — no "How a …", "What the …" padding
- Examples: "What programming is", "How computers run instructions", "Automating repetitive work", "Where Python fits in"

### Card descriptions
- One complete sentence only — subject, verb, object
- Target length: 12–18 words
- No em-dashes, no nested lists, no fragments
- Make it concrete: name a real task or outcome the learner recognizes

### Icons
- Choose a relevant Iconify icon from the `fa6-solid:` set for each card
- Each card must have a different icon

### Amber tip box
- One sentence starting with "This lesson …"
- Explain the *purpose* of the lesson, not a repeat of the goals

---

## Output

Replace the entire content of `<section id="objective">` … `</section>` in `TARGET_FILE` with the following structure. Do **not** change anything outside that section.

```html
<section id="objective">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:bullseye"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Lesson Objective</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">The goal and expected outcome of this lesson</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">

        <!-- Card 1 -->
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="ICON_1"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">TITLE_1</p>
            <p class="text-xs text-gray-500 mt-0.5">DESC_1</p>
          </div>
        </div>

        <!-- Card 2 -->
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="ICON_2"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">TITLE_2</p>
            <p class="text-xs text-gray-500 mt-0.5">DESC_2</p>
          </div>
        </div>

        <!-- Card 3 -->
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="ICON_3"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">TITLE_3</p>
            <p class="text-xs text-gray-500 mt-0.5">DESC_3</p>
          </div>
        </div>

        <!-- Card 4 -->
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="ICON_4"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">TITLE_4</p>
            <p class="text-xs text-gray-500 mt-0.5">DESC_4</p>
          </div>
        </div>

      </div>
      <div class="mt-5">
        <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">AMBER_TIP</p>
        </div>
      </div>
    </div>
  </div>
</section>
```
