#!/usr/bin/env python3
"""
Full CSS + HTML refactor for all lesson pages and the template.

1.  CSS: Consolidate 5× duplicate panel-anim rules → one multi-selector
2.  CSS: Consolidate 4× duplicate step-hover rules → one multi-selector
3.  CSS: Reorganise tab CSS section (move split PE rules into tab block)
4.  CSS: Add standalone active/inactive base styles for step pills
5.  CSS: Add .pill-tab base class (layout for ce/mk/pe/qz step buttons)
6.  CSS: Add .section-header / .section-icon / .section-body /
         .section-title / .section-subtitle classes
7.  CSS: Add .skill-dot / .skill-dot-active classes
8.  CSS: Add .hero-py-icon-wrap / .hero-py-icon classes
9.  CSS: Fix .bg-amber-tip — full border shorthand (not just border-color)
10. CSS: Add width:0 to .scroll-progress base rule
11. CSS: Add #hub-root overrides for every new class
12. HTML: Section header containers → .section-header
13. HTML: Section icon spans → .section-icon
14. HTML: Section body divs → .section-body
15. HTML: Section h2 titles → add .section-title (keep h2 tag)
16. HTML: Section subtitle p → add .section-subtitle (keep p tag)
17. HTML: Active step pill buttons → remove state Tailwind, add .pill-tab
18. HTML: Inactive step pill buttons → remove state Tailwind, add .pill-tab
19. HTML: Step icon spans → remove text-[13px]
20. HTML: Step label spans → remove text-xs font-bold
21. HTML: Skill-level dots → .skill-dot / .skill-dot-active classes
22. HTML: scroll-progress div → remove style="width: 0%;"
23. HTML: SVG hero → add .hero-svg class, remove style="max-height:320px;"
24. HTML: SVG foreignObject wrapper → .hero-py-icon-wrap
25. HTML: SVG Python icon span → .hero-py-icon, remove inline style
"""

import os
import re

BASE = '/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_01_getting_started'
TEMPLATE = '/Users/graywolf/Documents/Project/Python-Learning/docs/new_lesson_template.html'

LESSONS = [
    'lesson01_what_is_python.html',
    'lesson02_how_to_request_access_software.html',
    'lesson03_how_to_install_extensions_in_vs_code.html',
    'lesson04_how_to_setup_a_virtual_environment.html',
    'lesson05_how_to_install_libraries_in_a_virtual_environment.html',
    'lesson06_how_to_run_a_python_notebook_or_script.html',
]

# ──────────────────────────────────────────────────────────────────────
# SIMPLE (exact-string) REPLACEMENTS  →  (old, new)
# ──────────────────────────────────────────────────────────────────────

SIMPLE = [

    # ──────────────────────────────────────────────────────────────────
    # 1-3: CSS — Consolidate duplicated tab CSS into one clean block
    # ──────────────────────────────────────────────────────────────────

    # Replace the fragmented tab CSS (KC, CE, MK, QZ, PE interleaved with
    # accordion) with one organised section. The old block spans from the
    # KC comment to the PE practice exercises section. We replace it with:
    #   • one multi-selector panel-anim rule
    #   • one multi-selector hover rule
    #   • base state rules for step pills (so standalone browser works)
    #   • .pill-tab base class
    #   • individual KC, task-box rules
    (
        '    /* Key Concepts vertical tabs */\n'
        '    .kc-tab-active { background: #fdf0f7; }\n'
        '    .kc-indicator { height: 68px; }\n'
        '    .kc-tab:not(.kc-tab-active):hover { background: #f9fafb; }\n'
        '    .kc-panel-anim { animation: kcFadeIn 0.25s ease-out; }\n'
        '    @keyframes kcFadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }\n'
        '\n'
        '    /* Code Examples */\n'
        '    .ce-step:not(.ce-step-active):hover { background: #374151; color: #ffffff; }\n'
        '    .ce-panel-anim { animation: kcFadeIn 0.25s ease-out; }\n'
        '\n'
        '    /* Common Mistakes */\n'
        '    .mk-step:not(.mk-step-active):hover { background: #374151; color: #ffffff; }\n'
        '    .mk-panel-anim { animation: kcFadeIn 0.25s ease-out; }\n'
        '\n'
        '    /* Knowledge Check */\n'
        '    .qz-step:not(.qz-step-active):hover { background: #374151; color: #ffffff; }\n'
        '    .qz-panel-anim { animation: kcFadeIn 0.25s ease-out; }\n'
        '\n'
        '    /* Practice Exercises */\n'
        '    .task-box { background: #fdf0f7; border: 1px solid #f5c6e0; }',

        '    /* ─── Tab Systems ──────────────────────────────────────────── */\n'
        '\n'
        '    /* Keyframe used by all tab panel fade-in animations */\n'
        '    @keyframes kcFadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }\n'
        '\n'
        '    /* All panel animations share one keyframe */\n'
        '    .kc-panel-anim,\n'
        '    .ce-panel-anim,\n'
        '    .mk-panel-anim,\n'
        '    .qz-panel-anim,\n'
        '    .pe-panel-anim { animation: kcFadeIn 0.25s ease-out; }\n'
        '\n'
        '    /* Inactive pill tab hover (shared across all step types) */\n'
        '    .ce-step:not(.ce-step-active):hover,\n'
        '    .mk-step:not(.mk-step-active):hover,\n'
        '    .qz-step:not(.qz-step-active):hover,\n'
        '    .pe-step:not(.pe-step-active):hover { background: #374151; color: #ffffff; }\n'
        '\n'
        '    /* Inactive pill tab base state (standalone browser without Tailwind) */\n'
        '    .ce-step:not(.ce-step-active),\n'
        '    .mk-step:not(.mk-step-active),\n'
        '    .qz-step:not(.qz-step-active),\n'
        '    .pe-step:not(.pe-step-active) { background: #1f2937; color: #ffffff; box-shadow: none; }\n'
        '\n'
        '    /* Active pill tab base state */\n'
        '    .ce-step-active,\n'
        '    .mk-step-active,\n'
        '    .qz-step-active,\n'
        '    .pe-step-active {\n'
        '      background: linear-gradient(to right, #CB187D, #e84aad);\n'
        '      color: #ffffff;\n'
        '      box-shadow: 0 10px 25px -5px rgba(203, 24, 125, 0.3);\n'
        '    }\n'
        '\n'
        '    /* Pill tab base layout (shared by all step tab buttons) */\n'
        '    .pill-tab {\n'
        '      display: inline-flex;\n'
        '      align-items: center;\n'
        '      gap: 0.5rem;\n'
        '      padding: 0.5rem 1rem;\n'
        '      border-radius: 9999px;\n'
        '      border: none;\n'
        '      cursor: pointer;\n'
        '      font-size: 0.75rem;\n'
        '      font-weight: 700;\n'
        '      line-height: 1.2;\n'
        '      transition: all 0.25s;\n'
        '    }\n'
        '    .pill-tab .iconify { font-size: 13px; }\n'
        '\n'
        '    /* Key Concepts sidebar tabs */\n'
        '    .kc-tab-active { background: #fdf0f7; }\n'
        '    .kc-indicator { height: 68px; }\n'
        '    .kc-tab:not(.kc-tab-active):hover { background: #f9fafb; }\n'
        '\n'
        '    /* Task description box inside practice/example panels */\n'
        '    .task-box { background: #fdf0f7; border: 1px solid #f5c6e0; }',
    ),

    # Remove the now-redundant dangling PE tab CSS (split from above)
    (
        '    /* Practice exercise tab pills */\n'
        '    .pe-step:not(.pe-step-active):hover { background: #374151; color: #ffffff; }\n'
        '    .pe-panel-anim { animation: kcFadeIn 0.25s ease-out; }\n',
        '',
    ),

    # ──────────────────────────────────────────────────────────────────
    # 5-6: CSS — Add section-header classes (injected after .obj-card block)
    # ──────────────────────────────────────────────────────────────────
    (
        '    /* Tabs */\n'
        '    .tab-btn {',

        '    /* ─── Section Headers ──────────────────────────────────────── */\n'
        '    .section-header {\n'
        '      display: flex;\n'
        '      align-items: center;\n'
        '      gap: 1rem;\n'
        '      padding: 1.25rem 2rem 1.25rem 1rem;\n'
        '      background: #ffffff;\n'
        '      border-bottom: 1px solid #f3f4f6;\n'
        '      border-left: 4px solid #CB187D;\n'
        '    }\n'
        '    .section-icon {\n'
        '      display: inline-flex;\n'
        '      align-items: center;\n'
        '      justify-content: center;\n'
        '      width: 2.75rem;\n'
        '      height: 2.75rem;\n'
        '      border-radius: 0.75rem;\n'
        '      background: #CB187D;\n'
        '      flex-shrink: 0;\n'
        '    }\n'
        '    .section-body { min-width: 0; }\n'
        '    .section-title {\n'
        '      font-size: 1.25rem;\n'
        '      font-weight: 700;\n'
        '      color: #111827;\n'
        '      line-height: 1.3;\n'
        '      margin: 0;\n'
        '    }\n'
        '    .section-subtitle {\n'
        '      font-size: 0.875rem;\n'
        '      color: #9ca3af;\n'
        '      line-height: 1.4;\n'
        '      margin-top: 0.125rem;\n'
        '      margin-bottom: 0;\n'
        '    }\n'
        '\n'
        '    /* ─── Skill-level indicator dots ──────────────────────────── */\n'
        '    .skill-dot {\n'
        '      width: 6px;\n'
        '      height: 6px;\n'
        '      border-radius: 50%;\n'
        '      background: #d1d5db;\n'
        '      display: inline-block;\n'
        '    }\n'
        '    .skill-dot-active { background: #22c55e; }\n'
        '\n'
        '    /* ─── Hero SVG illustration ────────────────────────────────── */\n'
        '    .hero-svg { max-height: 320px; }\n'
        '    .hero-py-icon-wrap {\n'
        '      display: flex;\n'
        '      align-items: center;\n'
        '      justify-content: center;\n'
        '      width: 100%;\n'
        '      height: 100%;\n'
        '    }\n'
        '    .hero-py-icon {\n'
        '      font-size: 70px;\n'
        '      filter: drop-shadow(0 0 14px rgba(255, 212, 59, 0.25));\n'
        '    }\n'
        '\n'
        '    /* ─── Generic Tabs ─────────────────────────────────────────── */\n'
        '    .tab-btn {',
    ),

    # ──────────────────────────────────────────────────────────────────
    # 9: CSS — Fix .bg-amber-tip to have complete border shorthand
    # ──────────────────────────────────────────────────────────────────
    (
        '    .bg-amber-tip    { background: #fff7ed; border-color: #fed7aa; }',
        '    .bg-amber-tip    { background: #fff7ed; border: 1px solid #fed7aa; }',
    ),

    # ──────────────────────────────────────────────────────────────────
    # 10: CSS — Add width: 0 to .scroll-progress base rule
    # ──────────────────────────────────────────────────────────────────
    (
        '    .scroll-progress {\n'
        '      position: fixed;\n'
        '      top: 0;\n'
        '      left: 0;\n'
        '      height: 3px;\n',

        '    .scroll-progress {\n'
        '      position: fixed;\n'
        '      top: 0;\n'
        '      left: 0;\n'
        '      width: 0;\n'
        '      height: 3px;\n',
    ),

    # ──────────────────────────────────────────────────────────────────
    # 11: CSS — hub-root overrides for new classes
    # ──────────────────────────────────────────────────────────────────
    # Insert new hub-root rules before the dark pill tabs section
    (
        '  /* ── Dark pill tabs — inactive (dark bg) ── */\n'
        '  #hub-root .ce-step:not(.ce-step-active),',

        '  /* ── Section header components ── */\n'
        '  #hub-root .section-header {\n'
        '    display: flex !important;\n'
        '    align-items: center !important;\n'
        '    gap: 1rem !important;\n'
        '    padding: 1.25rem 2rem 1.25rem 1rem !important;\n'
        '    background: #ffffff !important;\n'
        '    border-bottom: 1px solid #f3f4f6 !important;\n'
        '    border-left: 4px solid #CB187D !important;\n'
        '  }\n'
        '  #hub-root .section-icon {\n'
        '    display: inline-flex !important;\n'
        '    align-items: center !important;\n'
        '    justify-content: center !important;\n'
        '    width: 2.75rem !important;\n'
        '    height: 2.75rem !important;\n'
        '    border-radius: 0.75rem !important;\n'
        '    background: #CB187D !important;\n'
        '    flex-shrink: 0 !important;\n'
        '  }\n'
        '  #hub-root .section-body { min-width: 0 !important; }\n'
        '  #hub-root .section-title {\n'
        '    font-size: 1.25rem !important;\n'
        '    font-weight: 700 !important;\n'
        '    color: #111827 !important;\n'
        '    line-height: 1.3 !important;\n'
        '    margin: 0 !important;\n'
        '  }\n'
        '  #hub-root .section-subtitle {\n'
        '    font-size: 0.875rem !important;\n'
        '    color: #9ca3af !important;\n'
        '    line-height: 1.4 !important;\n'
        '    margin-top: 0.125rem !important;\n'
        '    margin-bottom: 0 !important;\n'
        '  }\n'
        '\n'
        '  /* ── Pill tab base layout ── */\n'
        '  #hub-root .pill-tab {\n'
        '    display: inline-flex !important;\n'
        '    align-items: center !important;\n'
        '    gap: 0.5rem !important;\n'
        '    padding: 0.5rem 1rem !important;\n'
        '    border-radius: 9999px !important;\n'
        '    border: none !important;\n'
        '    cursor: pointer !important;\n'
        '    font-size: 0.75rem !important;\n'
        '    font-weight: 700 !important;\n'
        '    line-height: 1.2 !important;\n'
        '    transition: all 0.25s !important;\n'
        '  }\n'
        '  #hub-root .pill-tab .iconify { font-size: 13px !important; }\n'
        '\n'
        '  /* ── Skill dots ── */\n'
        '  #hub-root .skill-dot {\n'
        '    width: 6px !important;\n'
        '    height: 6px !important;\n'
        '    border-radius: 50% !important;\n'
        '    background: #d1d5db !important;\n'
        '    display: inline-block !important;\n'
        '  }\n'
        '  #hub-root .skill-dot-active { background: #22c55e !important; }\n'
        '\n'
        '  /* ── Hero SVG / Python icon ── */\n'
        '  #hub-root .hero-svg { max-height: 320px !important; }\n'
        '  #hub-root .hero-py-icon-wrap {\n'
        '    display: flex !important;\n'
        '    align-items: center !important;\n'
        '    justify-content: center !important;\n'
        '    width: 100% !important;\n'
        '    height: 100% !important;\n'
        '  }\n'
        '  #hub-root .hero-py-icon {\n'
        '    font-size: 70px !important;\n'
        '    filter: drop-shadow(0 0 14px rgba(255, 212, 59, 0.25)) !important;\n'
        '  }\n'
        '\n'
        '  /* ── Tip / info boxes ── */\n'
        '  #hub-root .bg-amber-tip { background: #fff7ed !important; border: 1px solid #fed7aa !important; }\n'
        '\n'
        '  /* ── Dark pill tabs — inactive (dark bg) ── */\n'
        '  #hub-root .ce-step:not(.ce-step-active),',
    ),

    # Remove the now-redundant hub-root h2.text-xl rule (handled by .section-title)
    (
        '  /* ── Section header card titles ── */\n'
        '  #hub-root .text-xl.font-bold,\n'
        '  #hub-root h2.text-xl { font-size: 1.25rem !important; font-weight: 700 !important; }\n',
        '',
    ),

    # ──────────────────────────────────────────────────────────────────
    # 12-16: HTML — Section headers
    # Replace the long Tailwind class string with .section-header
    # ──────────────────────────────────────────────────────────────────
    (
        'class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]"',
        'class="section-header"',
    ),
    # Section icon spans
    (
        'class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0"',
        'class="section-icon"',
    ),
    # Section body divs (standalone class="min-w-0", not "flex-1 min-w-0")
    (
        '              <div class="min-w-0">\n'
        '                <h2 class="text-xl font-bold text-gray-900 leading-tight">',
        '              <div class="section-body">\n'
        '                <h2 class="section-title">',
    ),
    # Section subtitle paragraphs (immediately after section title)
    (
        '                <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">',
        '                <p class="section-subtitle">',
    ),

    # ──────────────────────────────────────────────────────────────────
    # 17-20: HTML — Step pill tab buttons
    # Active buttons: remove Tailwind state classes, keep .pill-tab
    # ──────────────────────────────────────────────────────────────────
    # ce-step active
    (
        'class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250"',
        'class="ce-step ce-step-active pill-tab"',
    ),
    # ce-step inactive
    (
        'class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250"',
        'class="ce-step pill-tab"',
    ),
    # mk-step active
    (
        'class="mk-step mk-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250"',
        'class="mk-step mk-step-active pill-tab"',
    ),
    # mk-step inactive
    (
        'class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250"',
        'class="mk-step pill-tab"',
    ),
    # pe-step active
    (
        'class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250"',
        'class="pe-step pe-step-active pill-tab"',
    ),
    # pe-step inactive
    (
        'class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250"',
        'class="pe-step pill-tab"',
    ),
    # qz-step active
    (
        'class="qz-step qz-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250"',
        'class="qz-step qz-step-active pill-tab"',
    ),
    # qz-step inactive
    (
        'class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250"',
        'class="qz-step pill-tab"',
    ),

    # 19: Remove text-[13px] from iconify spans inside pill tabs
    (
        '<span class="iconify text-[13px]"',
        '<span class="iconify"',
    ),

    # 20: Remove text-xs font-bold from step label spans (now in .pill-tab CSS)
    (
        '<span class="ce-step-label text-xs font-bold">',
        '<span class="ce-step-label">',
    ),
    (
        '<span class="mk-step-label text-xs font-bold">',
        '<span class="mk-step-label">',
    ),
    (
        '<span class="pe-step-label text-xs font-bold">',
        '<span class="pe-step-label">',
    ),
    (
        '<span class="qz-step-label text-xs font-bold">',
        '<span class="qz-step-label">',
    ),

    # ──────────────────────────────────────────────────────────────────
    # 21: HTML — Skill-level dots (green active + gray inactive)
    # ──────────────────────────────────────────────────────────────────
    (
        '<span class="inline-flex items-center gap-1">\n'
        '                  <span style="width:6px;height:6px;border-radius:50%;background:#22c55e;display:inline-block;"></span>\n'
        '                  <span style="width:6px;height:6px;border-radius:50%;background:#d1d5db;display:inline-block;"></span>\n'
        '                  <span style="width:6px;height:6px;border-radius:50%;background:#d1d5db;display:inline-block;"></span>\n'
        '                </span>',

        '<span class="inline-flex items-center gap-1">\n'
        '                  <span class="skill-dot skill-dot-active"></span>\n'
        '                  <span class="skill-dot"></span>\n'
        '                  <span class="skill-dot"></span>\n'
        '                </span>',
    ),

    # ──────────────────────────────────────────────────────────────────
    # 22: HTML — Remove scroll-progress inline style
    # ──────────────────────────────────────────────────────────────────
    (
        '<div class="scroll-progress" id="scroll-progress" style="width: 0%;">',
        '<div class="scroll-progress" id="scroll-progress">',
    ),

    # ──────────────────────────────────────────────────────────────────
    # 23: HTML — SVG hero: add .hero-svg class, remove inline style
    # ──────────────────────────────────────────────────────────────────
    (
        'class="w-full h-auto" style="max-height:320px;" aria-hidden="true">',
        'class="w-full h-auto hero-svg" aria-hidden="true">',
    ),

    # ──────────────────────────────────────────────────────────────────
    # 24: HTML — foreignObject wrapper div → .hero-py-icon-wrap
    # ──────────────────────────────────────────────────────────────────
    (
        '<div xmlns="http://www.w3.org/1999/xhtml" style="display:flex;align-items:center;justify-content:center;width:100%;height:100%;">',
        '<div xmlns="http://www.w3.org/1999/xhtml" class="hero-py-icon-wrap">',
    ),

    # ──────────────────────────────────────────────────────────────────
    # 25: HTML — Python icon span → .hero-py-icon, remove inline style
    # ──────────────────────────────────────────────────────────────────
    (
        '<span class="iconify" data-icon="logos:python" style="font-size:70px;filter:drop-shadow(0 0 14px rgba(255,212,59,0.25));"></span>',
        '<span class="iconify hero-py-icon" data-icon="logos:python"></span>',
    ),
]


# ──────────────────────────────────────────────────────────────────────
# REGEX REPLACEMENTS  →  (pattern, replacement, flags)
# ──────────────────────────────────────────────────────────────────────

# (none needed beyond the simple replacements above)
REGEX = []


def fix_file(path):
    name = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    for old, new in SIMPLE:
        content = content.replace(old, new)

    for pattern, replacement, flags in REGEX:
        content = re.sub(pattern, replacement, content, flags=flags)

    if content == original:
        print(f'  — No changes: {name}')
        return

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  ✅ Updated: {name}')


for lesson in LESSONS:
    fix_file(os.path.join(BASE, lesson))

fix_file(TEMPLATE)
print('\nDone.')
