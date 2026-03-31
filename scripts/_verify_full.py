"""
Verify all refactor changes applied correctly in lesson01.
"""
import os, re

path = 'pages/track_01/mod_01_getting_started/lesson01_what_is_python.html'
content = open(path).read()

checks = [
    # ── CSS: Duplicate removal ────────────────────────────────────────
    ('panel-anim: only ONE rule block (multi-selector)',
        content.count('animation: kcFadeIn 0.25s ease-out; }') == 1),
    ('panel-anim: kc-panel-anim still present',
        '.kc-panel-anim,' in content),
    ('panel-anim: ce-panel-anim still present',
        '.ce-panel-anim,' in content),
    ('panel-anim: pe-panel-anim still present',
        '.pe-panel-anim { animation: kcFadeIn' in content),
    ('hover: only ONE ce-step:not(:hover) CSS rule',
        content.count('.ce-step:not(.ce-step-active):hover') == 1),
    ('hover: all 4 step types in one rule block',
        '.ce-step:not(.ce-step-active):hover,\n    .mk-step:not(.mk-step-active):hover,' in content),
    ('PE tab CSS NOT split (practice exercise tab pills comment gone)',
        '/* Practice exercise tab pills */' not in content),

    # ── CSS: New rules added ──────────────────────────────────────────
    ('has .pill-tab base class',          '.pill-tab {' in content),
    ('pill-tab has border-radius:9999px', 'border-radius: 9999px;' in content),
    ('pill-tab has .iconify rule',        '.pill-tab .iconify { font-size: 13px; }' in content),
    ('has active step base CSS (no hub-root)',
        '.ce-step-active,\n    .mk-step-active,' in content),
    ('has inactive step base CSS',
        '.ce-step:not(.ce-step-active),\n    .mk-step:not(.mk-step-active),' in content),
    ('has .section-header CSS',           '.section-header {' in content),
    ('has .section-icon CSS',             '.section-icon {' in content),
    ('has .section-body CSS',             '.section-body { min-width: 0; }' in content),
    ('has .section-title CSS',            '.section-title {' in content),
    ('has .section-subtitle CSS',         '.section-subtitle {' in content),
    ('has .skill-dot CSS',                '.skill-dot {' in content),
    ('has .skill-dot-active CSS',         '.skill-dot-active { background: #22c55e; }' in content),
    ('has .hero-svg CSS',                 '.hero-svg { max-height: 320px; }' in content),
    ('has .hero-py-icon CSS',             '.hero-py-icon {' in content),
    ('has .hero-py-icon-wrap CSS',        '.hero-py-icon-wrap {' in content),
    ('scroll-progress has width: 0',      'width: 0;\n      height: 3px;' in content),
    ('bg-amber-tip has full border',      '.bg-amber-tip    { background: #fff7ed; border: 1px solid #fed7aa; }' in content),
    ('bg-amber-tip no border-color only', 'border-color: #fed7aa' not in content),

    # ── CSS: hub-root overrides ───────────────────────────────────────
    ('hub-root has .section-header override',  '#hub-root .section-header {' in content),
    ('hub-root has .section-icon override',    '#hub-root .section-icon {' in content),
    ('hub-root has .section-title override',   '#hub-root .section-title {' in content),
    ('hub-root has .pill-tab override',        '#hub-root .pill-tab {' in content),
    ('hub-root has .skill-dot override',       '#hub-root .skill-dot {' in content),
    ('hub-root has .hero-py-icon override',    '#hub-root .hero-py-icon {' in content),
    ('hub-root has .bg-amber-tip override',    '#hub-root .bg-amber-tip {' in content),
    ('old h2.text-xl hub-root rule removed',   '#hub-root h2.text-xl { font-size' not in content),

    # ── HTML: Section headers ─────────────────────────────────────────
    ('section-header class in HTML',      'class="section-header"' in content),
    ('section-icon class in HTML',        'class="section-icon"' in content),
    ('section-body class in HTML',        'class="section-body"' in content),
    ('section-title h2 in HTML',          'class="section-title"' in content),
    ('section-subtitle p in HTML',        'class="section-subtitle"' in content),
    ('old section header Tailwind gone',
        'class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]"' not in content),
    ('old w-11 h-11 icon span gone',
        'class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0"' not in content),

    # ── HTML: Pill tab buttons ────────────────────────────────────────
    ('pill-tab class on step buttons',
        'class="ce-step ce-step-active pill-tab"' in content),
    ('inactive ce-step uses pill-tab',
        'class="ce-step pill-tab"' in content),
    ('no old active button Tailwind soup',
        'bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50' not in content),
    ('no old inactive button bg-gray-800',
        'class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400' not in content),
    ('no text-[13px] on iconify in pill tabs',
        'class="iconify text-[13px]"' not in content),
    ('no text-xs font-bold on step labels',
        'class="ce-step-label text-xs font-bold"' not in content),

    # ── HTML: Misc inline styles ──────────────────────────────────────
    ('skill-dot classes in HTML',         'class="skill-dot skill-dot-active"' in content),
    ('no inline style on skill dot green',
        'style="width:6px;height:6px;border-radius:50%;background:#22c55e' not in content),
    ('scroll-progress no inline style',
        'id="scroll-progress" style=' not in content),
    ('hero-svg class in HTML',            'class="w-full h-auto hero-svg"' in content),
    ('no max-height inline on SVG',       'style="max-height:320px;"' not in content),
    ('hero-py-icon-wrap class in HTML',   'class="hero-py-icon-wrap"' in content),
    ('hero-py-icon class in HTML',        'class="iconify hero-py-icon"' in content),
    ('no font-size:70px inline',          'style="font-size:70px;' not in content),
]

all_pass = True
for label, result in checks:
    icon = 'OK  ' if result else 'FAIL'
    if not result:
        all_pass = False
    print(f'  [{icon}] {label}')

print()
print('✅ All checks passed!' if all_pass else '❌ SOME CHECKS FAILED — review above')
