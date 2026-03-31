"""
Replace <section class="hero-container"> in lesson04.
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_HERO = '''<section class="hero-container">
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
            <span class="iconify text-[10px]" data-icon="fa6-solid:diagram-project"></span> Module 3
          </span>
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="inline-flex items-center gap-1">
              <span style="width:6px;height:6px;border-radius:50%;background:#22c55e;display:inline-block;"></span>
              <span style="width:6px;height:6px;border-radius:50%;background:#d1d5db;display:inline-block;"></span>
              <span style="width:6px;height:6px;border-radius:50%;background:#d1d5db;display:inline-block;"></span>
            </span>
            Beginner
          </span>
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="iconify text-[10px]" data-icon="fa6-regular:clock"></span> 25 min read
          </span>
        </div>

        <!-- Lesson number label -->
        <p class="text-xs font-bold uppercase tracking-[0.2em] text-white/90 mb-2">Lesson 04</p>

        <!-- Title -->
        <h1 class="text-3xl md:text-4xl font-extrabold text-white mb-3 leading-[1.15] tracking-tight">Refactoring a Script into a Class</h1>

        <!-- Subtitle -->
        <p class="text-white/80 text-sm md:text-base leading-relaxed mt-4 mb-5 max-w-prose">Learn how to reorganise a working Python script into a clean class — giving your code structure that is easier to read, reuse, and grow.</p>

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
            <span class="text-white/85 font-medium text-xs">March 29, 2026</span>
          </div>
        </div>

        <!-- Stat pills -->
        <div class="flex items-center gap-2 flex-wrap">
          <a href="#objective" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline">
            <span class="iconify text-[10px]" data-icon="fa6-solid:bullseye" style="opacity:0.5;"></span>
            <span class="font-extrabold">4</span>
            <span class="font-semibold opacity-55">Goals</span>
          </a>
          <a href="#code-examples" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline">
            <span class="iconify text-[10px]" data-icon="fa6-solid:code" style="opacity:0.5;"></span>
            <span class="font-extrabold">3</span>
            <span class="font-semibold opacity-55">Examples</span>
          </a>
          <a href="#practice" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline">
            <span class="iconify text-[10px]" data-icon="fa6-solid:dumbbell" style="opacity:0.5;"></span>
            <span class="font-extrabold">3</span>
            <span class="font-semibold opacity-55">Exercises</span>
          </a>
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="iconify text-[10px]" data-icon="fa6-solid:layer-group" style="opacity:0.5;"></span>
            <span class="font-extrabold">4<span class="font-bold opacity-50">/4</span></span>
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
</section>'''

html = TARGET.read_text(encoding='utf-8')

# Find and replace the hero section
start = html.find('<section class="hero-container">')
if start == -1:
    print('❌ hero-container not found'); sys.exit(1)

search = html[start:]
depth, end, i = 0, -1, 0
while i < len(search):
    if search[i:].startswith('<section'):
        depth += 1; i += len('<section')
    elif search[i:].startswith('</section>'):
        depth -= 1
        if depth == 0:
            end = start + i + len('</section>'); break
        i += len('</section>')
    else:
        i += 1

if end == -1:
    print('❌ Closing </section> not found'); sys.exit(1)

old = html[start:end]
print(f'  Old hero: {len(old):,} chars')
print(f'  New hero: {len(NEW_HERO):,} chars')

html = html[:start] + NEW_HERO + html[end:]
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# --- Verification ---
result = TARGET.read_text(encoding='utf-8')
s = result[result.find('<section class="hero-container">'):]
s = s[:s.find('</section>') + len('</section>')]

checks = [
    ("hero-container class",                'class="hero-container"'),
    ("hero-dots",                           'class="hero-dots"'),
    ("Module 3 badge",                      "> Module 3"),
    ("Module icon: diagram-project",        'data-icon="fa6-solid:diagram-project"'),
    ("Beginner label",                      "Beginner"),
    ("Green dot (beginner)",                "background:#22c55e"),
    ("Gray dot 2",                          "#d1d5db"),
    ("25 min read",                         "25 min read"),
    ("Lesson 04 label",                     ">Lesson 04<"),
    ("Title: Refactoring a Script",         "Refactoring a Script into a Class"),
    ("Subtitle starts with Learn",          "Learn how to reorganise"),
    ("Author: Python Learning Hub",         "Python Learning Hub"),
    ("Date: March 29, 2026",               "March 29, 2026"),
    ("4 Goals stat",                        ">4<"),
    ("3 Examples stat",                     ">3<"),
    ("3 Exercises stat — dumbbell icon",    'data-icon="fa6-solid:dumbbell"'),
    ("Progress 4/4",                        ">4<"),
    ("href #objective",                     'href="#objective"'),
    ("href #code-examples",                 'href="#code-examples"'),
    ("href #practice",                      'href="#practice"'),
    ("SVG hexFill gradient",                'id="hexFill"'),
    ("SVG hexClip",                         'id="hexClip"'),
    ("hero-abstract-card padding",          'style="padding:0.25rem;opacity:0.75;"'),
    ("PYTHON text in SVG",                  ">PYTHON<"),
    ("LEARNING HUB text in SVG",            ">LEARNING HUB<"),
    ("logos:python icon",                   'data-icon="logos:python"'),
    ("fa6-solid:user author icon",          'data-icon="fa6-solid:user"'),
    ("fa6-regular:calendar date icon",      'data-icon="fa6-regular:calendar"'),
]

passed, failed = 0, 0
for label, needle in checks:
    ok = needle in s
    print(f'  {"✅" if ok else "❌"} {label}')
    if ok: passed += 1
    else: failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
