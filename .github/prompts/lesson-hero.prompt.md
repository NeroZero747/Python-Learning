---
mode: "agent"
description: "Write or rewrite the hero banner section for a lesson HTML file — badge row, lesson number, title, subtitle, author/date row, stat pills, and the right-column hex SVG graphic. Matches the mod_02/lesson01 design standard exactly."
---

Rewrite the `<section class="hero-container">` block in the target lesson file using the structure and rules below. The hero is the full-width gradient header at the very top of the lesson. The visual design (background layers, SVG hex, color palette) is locked and must never change — only the text content and stat numbers are updated per lesson.

---

## Inputs (fill in before running)

| Variable | Value |
|---|---|
| `TARGET_FILE` | Path to the lesson HTML file |
| `MODULE_NUM` | Module number shown in the first badge pill (e.g. `2`) |
| `MODULE_ICON` | Iconify icon for the module badge (e.g. `fa6-solid:cubes`). Use `fa6-solid:rocket` for Module 1, `fa6-solid:cubes` for Module 2, `fa6-solid:diagram-project` for Module 3, `fa6-solid:star` for Module 4+. |
| `DIFFICULTY` | Skill level shown in the second badge pill — `Beginner`, `Intermediate`, or `Advanced` |
| `READ_TIME` | Estimated read time shown in the third badge pill (e.g. `5 min read`) |
| `LESSON_NUM_LABEL` | Lesson number label above the title (e.g. `Lesson 01`, `Lesson 02`) |
| `LESSON_TITLE` | Full lesson title displayed as the `<h1>` (e.g. `What Is Programming?`) |
| `SUBTITLE` | One-sentence subtitle under the title — 15–25 words, written for a beginner. Start with a verb or "Discover…" / "Learn…" / "Understand…". No jargon the learner hasn't seen yet. |
| `PUB_DATE` | Publication date in the format `Month DD, YYYY` (e.g. `March 24, 2026`) |
| `GOALS_COUNT` | Number shown on the Goals stat pill — matches the number of objective cards (always `4`) |
| `EXAMPLES_COUNT` | Number shown on the Examples stat pill — matches the number of code example tabs |
| `EXERCISES_COUNT` | Number shown on the Exercises stat pill — matches the number of practice exercise tabs |
| `LESSON_POSITION` | Current lesson number within the module (e.g. `1`) |
| `TOTAL_LESSONS` | Total number of lessons in the module (e.g. `9`) |

---

## Difficulty dot colors

The second badge pill uses three colored inline dots to indicate difficulty. Do **not** use Tailwind classes for these — use the exact inline `style` attributes below so they survive Confluence CSS sanitization:

| Level | Dot 1 | Dot 2 | Dot 3 |
|---|---|---|---|
| `Beginner` | `#22c55e` (green) | `#d1d5db` (gray) | `#d1d5db` (gray) |
| `Intermediate` | `#22c55e` (green) | `#22c55e` (green) | `#d1d5db` (gray) |
| `Advanced` | `#22c55e` (green) | `#22c55e` (green) | `#22c55e` (green) |

Each dot: `style="width:6px;height:6px;border-radius:50%;background:COLOR;display:inline-block;"`

---

## Writing rules for subtitle

- One sentence only — no full paragraph.
- Start with an action word or "Discover…" / "Learn…" / "Understand…" / "See how…"
- Mention the lesson topic by name and give a hint of why it matters in practice.
- Keep it between 15 and 25 words.
- Avoid technical jargon the learner hasn't encountered yet in the course.

**Good example:** "Discover how programming works — writing step-by-step instructions that tell a computer exactly what to do, and why Python makes that process simple and readable."

**Bad example:** "An introduction to imperative programming paradigms, sequential execution models, and the Python runtime environment."

---

## Locked elements (do not change)

The following elements are identical across every lesson and must be copied verbatim — never modified:

- All background layers: `.hero-dots`, `.hero-glow-1`, `.hero-glow-2`, `.hero-glow-line`
- The author name: `Python Learning Hub`
- The author icon: `fa6-solid:user`
- The date icon: `fa6-regular:calendar`
- The separator: `<span class="text-white/30">|</span>`
- The stat pill icons and `href` anchors (`#objective`, `#code-examples`, `#practice`)
- The entire right-column `<svg>` hex graphic — copy it exactly as shown in the template below
- The `hero-abstract-card` wrapper: `style="padding:0.25rem;opacity:0.75;"`

---

## Full section template

Replace the complete `<section class="hero-container">…</section>` block with the following, substituting all `VARIABLE_NAME` placeholders:

```html
<section class="hero-container">
  <div class="hero-dots"></div>
  <div class="hero-glow hero-glow-1"></div>
  <div class="hero-glow hero-glow-2"></div>
  <div class="hero-glow-line"></div>
  <div class="relative z-10 px-8 py-8 md:px-12 md:py-10">
    <div class="hero-split flex flex-col md:flex-row items-center gap-6 md:gap-10">

      <!-- LEFT COLUMN — Lesson info -->
      <div class="flex-1 min-w-0">

        <!-- Badge row -->
        <div class="flex flex-wrap items-center gap-2 mb-4">
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="iconify text-[10px]" data-icon="MODULE_ICON"></span> Module MODULE_NUM
          </span>
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="inline-flex items-center gap-1">
              <span style="width:6px;height:6px;border-radius:50%;background:DOT1_COLOR;display:inline-block;"></span>
              <span style="width:6px;height:6px;border-radius:50%;background:DOT2_COLOR;display:inline-block;"></span>
              <span style="width:6px;height:6px;border-radius:50%;background:DOT3_COLOR;display:inline-block;"></span>
            </span>
            DIFFICULTY
          </span>
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="iconify text-[10px]" data-icon="fa6-regular:clock"></span> READ_TIME
          </span>
        </div>

        <!-- Lesson number label -->
        <p class="text-xs font-bold uppercase tracking-[0.2em] text-white/90 mb-2">LESSON_NUM_LABEL</p>

        <!-- Title -->
        <h1 class="text-3xl md:text-4xl font-extrabold text-white mb-3 leading-[1.15] tracking-tight">LESSON_TITLE</h1>

        <!-- Subtitle -->
        <p class="text-white/80 text-sm md:text-base leading-relaxed mt-4 mb-5 max-w-prose">SUBTITLE</p>

        <!-- Author & Date -->
        <div class="flex items-center gap-4 mb-5 text-sm">
          <div class="flex items-center gap-2">
            <span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-white/15">
              <span class="iconify text-white text-[10px]" data-icon="fa6-solid:user"></span>
            </span>
            <span class="text-white/85 font-medium text-xs">Python Learning Hub</span>
          </div>
          <span class="text-white/30">|</span>
          <div class="flex items-center gap-2">
            <span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-white/15">
              <span class="iconify text-white text-[10px]" data-icon="fa6-regular:calendar"></span>
            </span>
            <span class="text-white/85 font-medium text-xs">PUB_DATE</span>
          </div>
        </div>

        <!-- Stat pills -->
        <div class="flex items-center gap-2 flex-wrap">
          <a href="#objective" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline">
            <span class="iconify text-[10px]" data-icon="fa6-solid:bullseye" style="opacity:0.5;"></span>
            <span class="font-extrabold">GOALS_COUNT</span>
            <span class="font-semibold opacity-55">Goals</span>
          </a>
          <a href="#code-examples" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline">
            <span class="iconify text-[10px]" data-icon="fa6-solid:code" style="opacity:0.5;"></span>
            <span class="font-extrabold">EXAMPLES_COUNT</span>
            <span class="font-semibold opacity-55">Examples</span>
          </a>
          <a href="#practice" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline">
            <span class="iconify text-[10px]" data-icon="fa6-solid:dumbbell" style="opacity:0.5;"></span>
            <span class="font-extrabold">EXERCISES_COUNT</span>
            <span class="font-semibold opacity-55">Exercises</span>
          </a>
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="iconify text-[10px]" data-icon="fa6-solid:layer-group" style="opacity:0.5;"></span>
            <span class="font-extrabold">LESSON_POSITION<span class="font-bold opacity-50">/TOTAL_LESSONS</span></span>
            <span class="font-semibold opacity-55">Progress</span>
          </span>
        </div>

      </div>

      <!-- RIGHT COLUMN — Hex graphic (locked — never edit) -->
      <div class="w-full md:w-[300px] lg:w-[320px] shrink-0 self-center">
        <div class="hero-abstract-card" style="padding:0.25rem;opacity:0.75;">
          <svg viewBox="0 0 280 324" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-auto" style="max-height:320px;" aria-hidden="true">
            <defs>
              <linearGradient id="hexFill" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1a0a12"/><stop offset="45%" stop-color="#2d0a1e"/><stop offset="100%" stop-color="#0d0610"/></linearGradient>
              <linearGradient id="hexBorder" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#CB187D"/><stop offset="50%" stop-color="#e84aad"/><stop offset="100%" stop-color="#CB187D"/></linearGradient>
              <radialGradient id="hexGlow" cx="50%" cy="38%" r="45%"><stop offset="0%" stop-color="#CB187D" stop-opacity="0.18"/><stop offset="100%" stop-color="#CB187D" stop-opacity="0"/></radialGradient>
              <radialGradient id="pyGlow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#FFD43B" stop-opacity="0.12"/><stop offset="100%" stop-color="#FFD43B" stop-opacity="0"/></radialGradient>
              <clipPath id="hexClip"><polygon points="140,14 268,88 268,236 140,310 12,236 12,88"/></clipPath>
            </defs>
            <polygon points="140,14 268,88 268,236 140,310 12,236 12,88" fill="url(#hexFill)"/>
            <polygon points="140,14 268,88 268,236 140,310 12,236 12,88" fill="url(#hexGlow)"/>
            <g clip-path="url(#hexClip)" opacity="1">
              <g opacity="0.06"><circle cx="40" cy="100" r="1.2" fill="white"/><circle cx="60" cy="100" r="1.2" fill="white"/><circle cx="80" cy="100" r="1.2" fill="white"/><circle cx="100" cy="100" r="1.2" fill="white"/><circle cx="120" cy="100" r="1.2" fill="white"/><circle cx="160" cy="100" r="1.2" fill="white"/><circle cx="180" cy="100" r="1.2" fill="white"/><circle cx="200" cy="100" r="1.2" fill="white"/><circle cx="220" cy="100" r="1.2" fill="white"/><circle cx="240" cy="100" r="1.2" fill="white"/><circle cx="50" cy="120" r="1.2" fill="white"/><circle cx="70" cy="120" r="1.2" fill="white"/><circle cx="90" cy="120" r="1.2" fill="white"/><circle cx="110" cy="120" r="1.2" fill="white"/><circle cx="170" cy="120" r="1.2" fill="white"/><circle cx="190" cy="120" r="1.2" fill="white"/><circle cx="210" cy="120" r="1.2" fill="white"/><circle cx="230" cy="120" r="1.2" fill="white"/><circle cx="40" cy="200" r="1.2" fill="white"/><circle cx="60" cy="200" r="1.2" fill="white"/><circle cx="80" cy="200" r="1.2" fill="white"/><circle cx="100" cy="200" r="1.2" fill="white"/><circle cx="120" cy="200" r="1.2" fill="white"/><circle cx="160" cy="200" r="1.2" fill="white"/><circle cx="180" cy="200" r="1.2" fill="white"/><circle cx="200" cy="200" r="1.2" fill="white"/><circle cx="220" cy="200" r="1.2" fill="white"/><circle cx="240" cy="200" r="1.2" fill="white"/><circle cx="50" cy="220" r="1.2" fill="white"/><circle cx="70" cy="220" r="1.2" fill="white"/><circle cx="90" cy="220" r="1.2" fill="white"/><circle cx="110" cy="220" r="1.2" fill="white"/><circle cx="170" cy="220" r="1.2" fill="white"/><circle cx="190" cy="220" r="1.2" fill="white"/><circle cx="210" cy="220" r="1.2" fill="white"/><circle cx="230" cy="220" r="1.2" fill="white"/></g>
              <g opacity="0.12" stroke="#CB187D" stroke-width="1" fill="none"><path d="M30,95 L55,95 L55,115 L80,115"/><path d="M35,110 L60,110 L60,130"/><circle cx="80" cy="115" r="2.5" fill="#CB187D" opacity="0.4"/><circle cx="55" cy="95" r="2" fill="#CB187D" opacity="0.35"/><circle cx="60" cy="130" r="2" fill="#CB187D" opacity="0.3"/></g>
              <g opacity="0.12" stroke="#e84aad" stroke-width="1" fill="none"><path d="M250,95 L225,95 L225,115 L200,115"/><path d="M245,110 L220,110 L220,130"/><circle cx="200" cy="115" r="2.5" fill="#e84aad" opacity="0.4"/><circle cx="225" cy="95" r="2" fill="#e84aad" opacity="0.35"/><circle cx="220" cy="130" r="2" fill="#e84aad" opacity="0.3"/></g>
              <g opacity="0.1" stroke="#CB187D" stroke-width="1" fill="none"><path d="M35,210 L60,210 L60,230 L85,230"/><path d="M40,225 L65,225 L65,240"/><circle cx="85" cy="230" r="2.5" fill="#CB187D" opacity="0.35"/><circle cx="65" cy="240" r="2" fill="#CB187D" opacity="0.3"/></g>
              <g opacity="0.1" stroke="#e84aad" stroke-width="1" fill="none"><path d="M245,210 L220,210 L220,230 L195,230"/><path d="M240,225 L215,225 L215,240"/><circle cx="195" cy="230" r="2.5" fill="#e84aad" opacity="0.35"/><circle cx="215" cy="240" r="2" fill="#e84aad" opacity="0.3"/></g>
              <g opacity="0.08" fill="white" font-family="'Fira Code',monospace" font-size="7"><text x="42" y="145">&gt;&gt;&gt; import pandas</text><text x="185" y="92">def main():</text><text x="38" y="92">class Data:</text></g>
              <g opacity="0.07" fill="white" font-family="'Fira Code',monospace" font-size="7"><text x="160" y="255">return result</text><text x="42" y="260">for i in range:</text><text x="175" y="275">print("done")</text></g>
              <g opacity="0.15" stroke="#FFD43B" stroke-width="1.5" fill="none" stroke-linecap="round"><polyline points="52,72 42,72 42,85"/><polyline points="228,72 238,72 238,85"/><polyline points="52,252 42,252 42,239"/><polyline points="228,252 238,252 238,239"/></g>
              <g opacity="0.04" stroke="white" stroke-width="1" fill="none"><polygon points="70,155 85,146 100,155 100,173 85,182 70,173"/><polygon points="180,155 195,146 210,155 210,173 195,182 180,173"/><polygon points="125,260 140,251 155,260 155,278 140,287 125,278"/><polygon points="125,40 140,31 155,40 155,58 140,67 125,58"/></g>
              <g opacity="0.08" stroke="white" stroke-width="0.8" fill="none" stroke-dasharray="4,4"><path d="M25,160 Q60,140 60,162 Q60,185 95,165"/><path d="M25,180 Q55,195 75,180"/></g>
              <g opacity="0.08" stroke="white" stroke-width="0.8" fill="none" stroke-dasharray="4,4"><path d="M255,160 Q220,140 220,162 Q220,185 185,165"/><path d="M255,180 Q225,195 205,180"/></g>
              <circle cx="140" cy="145" r="55" fill="url(#pyGlow)"/>
            </g>
            <polygon points="140,14 268,88 268,236 140,310 12,236 12,88" fill="none" stroke="url(#hexBorder)" stroke-width="4" stroke-linejoin="round"/>
            <polygon points="140,24 258,93 258,231 140,300 22,231 22,93" fill="none" stroke="#CB187D" stroke-width="0.8" stroke-linejoin="round" stroke-opacity="0.25"/>
            <foreignObject x="95" y="85" width="90" height="90"><div xmlns="http://www.w3.org/1999/xhtml" style="display:flex;align-items:center;justify-content:center;width:100%;height:100%;"><span class="iconify" data-icon="logos:python" style="font-size:70px;filter:drop-shadow(0 0 14px rgba(255,212,59,0.25));"></span></div></foreignObject>
            <text x="140" y="205" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-weight="800" font-size="30" letter-spacing="4" opacity="0.95">PYTHON</text>
            <text x="140" y="230" text-anchor="middle" fill="#f5c6e0" font-family="Inter,sans-serif" font-weight="600" font-size="14" letter-spacing="5" opacity="0.8">LEARNING HUB</text>
            <line x1="85" y1="185" x2="195" y2="185" stroke="#CB187D" stroke-width="1" stroke-opacity="0.35" stroke-linecap="round"/>
            <line x1="100" y1="248" x2="180" y2="248" stroke="#FFD43B" stroke-width="1.2" stroke-opacity="0.25" stroke-linecap="round"/>
            <g opacity="0.5"><rect x="113" y="255" width="54" height="16" rx="8" fill="#CB187D" opacity="0.2"/><rect x="113" y="255" width="54" height="16" rx="8" fill="none" stroke="#CB187D" stroke-width="0.6" opacity="0.35"/><text x="140" y="266.5" text-anchor="middle" fill="#f5c6e0" font-family="'Fira Code',monospace" font-weight="600" font-size="8" opacity="0.8">v1.0</text></g>
          </svg>
        </div>
      </div>

    </div>
  </div>
</section>
```

---

## Quality checklist

Before submitting the rewritten hero, verify:

- [ ] Module number and icon are correct for this lesson's module
- [ ] Difficulty dot colors match the level (beginner = 1 green dot, intermediate = 2, advanced = 3)
- [ ] `LESSON_NUM_LABEL` uses two-digit zero-padding (e.g. `Lesson 01`, not `Lesson 1`)
- [ ] Subtitle is 15–25 words and starts with an action word or "Discover…" / "Learn…"
- [ ] Author name is exactly `Python Learning Hub` — never changed
- [ ] Date format is `Month DD, YYYY` with full month name
- [ ] Stat pill numbers (`GOALS_COUNT`, `EXAMPLES_COUNT`, `EXERCISES_COUNT`) match the actual section tab counts in the file
- [ ] Progress fraction (`LESSON_POSITION/TOTAL_LESSONS`) matches the lesson's position in its module
- [ ] The SVG hex graphic is copied verbatim — no modifications
- [ ] `hero-abstract-card` wrapper has `style="padding:0.25rem;opacity:0.75;"` — not changed
