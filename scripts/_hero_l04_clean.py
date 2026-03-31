"""
Replace lesson04's hero section using lesson03 as the structural template,
substituting correct lesson04-specific fields.
"""
import re

PATH03 = r'c:\Users\nightwolf\Projects\Python-Learning\pages\track_01_python_foundation\mod_04_python_best_practices\lesson03_introduction_to_git_simple_workflow.html'
PATH04 = r'c:\Users\nightwolf\Projects\Python-Learning\pages\track_01_python_foundation\mod_04_python_best_practices\lesson04_logging_basics.html'
MARKER = '<section class="hero-container">'

def extract_hero(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    start = content.find(MARKER)
    if start == -1:
        raise ValueError(f'Hero not found in {path}')
    pos = start + len(MARKER)
    depth = 1
    while depth > 0 and pos < len(content):
        next_open  = content.find('<section', pos)
        next_close = content.find('</section>', pos)
        if next_close == -1:
            raise ValueError('Unmatched <section>')
        if next_open != -1 and next_open < next_close:
            depth += 1; pos = next_open + 1
        else:
            depth -= 1
            if depth == 0:
                end = next_close + len('</section>')
            pos = next_close + 1
    return content, start, end

# ── Read lesson03 hero as structural template ──────────────────────────
c03, s03, e03 = extract_hero(PATH03)
hero = c03[s03:e03]

# ── Verify lesson03 base fields ────────────────────────────────────────
print('Lesson03 hero base:')
print('  icon :', 'fa6-solid:star' in hero)
print('  dots :', 'background:#22c55e' in hero)
print('  clk  :', 'fa6-regular:clock' in hero)
print('  5min :', '5 min read' in hero)

# ── Apply lesson04 substitutions ───────────────────────────────────────

# 1. Lesson label
if 'Lesson 03</p>' in hero:
    hero = hero.replace('Lesson 03</p>', 'Lesson 04</p>')
    print('  label : OK')
else:
    print('  label : WARNING - Lesson 03 not found, current:', re.search(r'Lesson \d+</p>', hero))

# 2. Title
if 'Introduction to Git (Simple Workflow)</h1>' in hero:
    hero = hero.replace(
        'Introduction to Git (Simple Workflow)</h1>',
        'Logging Basics</h1>'
    )
    print('  title : OK')
else:
    print('  title : WARNING - not found')

# 3. Subtitle — replace whatever is in the max-w-prose or max-w-lg paragraph
old_sub = re.search(r'<p class="text-white/80[^"]*"[^>]*>.*?</p>', hero, re.DOTALL)
if old_sub:
    hero = hero[:old_sub.start()] + \
        '<p class="text-white/80 text-sm md:text-base leading-relaxed mt-4 mb-5 max-w-prose">Learn how to use Python\'s logging module to record events, track errors, and monitor your program \u2014 a professional alternative to print statements.</p>' + \
        hero[old_sub.end():]
    print('  sub   : OK')
else:
    print('  sub   : WARNING - subtitle paragraph not found')

# 4. Progress — replace the lesson position number (keep /5)
# Pattern: font-extrabold">N<span class="font-bold opacity-50">/5
hero = re.sub(
    r'(<span class="font-extrabold">)\d+(<span class="font-bold opacity-50">/5)',
    r'\g<1>4\2',
    hero
)
print('  prog  :', '">4<span class="font-bold opacity-50">/5' in hero)

# 5. Confirm stat counts already match lesson04 (4 Goals, 4 Examples, 3 Exercises)
# lesson03 and lesson04 both have 4/4/3 so no change needed
print('  goals :', '>4</span>\n            <span class="font-semibold opacity-55">Goals' in hero or '">4</span>' in hero)

# ── Write into lesson04 ────────────────────────────────────────────────
c04, s04, e04 = extract_hero(PATH04)
new_content = c04[:s04] + hero + c04[e04:]

with open(PATH04, 'w', encoding='utf-8') as f:
    f.write(new_content)
print('\nWritten successfully.')

# ── Post-write verification ────────────────────────────────────────────
c04v, s04v, e04v = extract_hero(PATH04)
h04 = c04v[s04v:e04v]

checks = [
    ('fa6-solid:star', 'fa6-solid:star' in h04),
    ('No fa6-solid:medal', 'fa6-solid:medal' not in h04),
    ('Intermediate', 'Intermediate' in h04),
    ('2 green dots', h04.count('background:#22c55e') >= 2),
    ('5 min read', '5 min read' in h04),
    ('Lesson 04 label', 'Lesson 04</p>' in h04),
    ('No Lesson 06', 'Lesson 06' not in h04),
    ('Logging Basics title', 'Logging Basics</h1>' in h04),
    ('Subtitle logging', 'logging module' in h04),
    ('Python Learning Hub', 'Python Learning Hub' in h04),
    ('Calendar icon', 'fa6-regular:calendar' in h04),
    ('March 30 2026', 'March 30, 2026' in h04),
    ('4 Goals', re.search(r'font-extrabold">\s*4\s*</span>\s*<span[^>]*>Goals', h04) is not None),
    ('4 Examples', re.search(r'font-extrabold">\s*4\s*</span>\s*<span[^>]*>Examples', h04) is not None),
    ('3 Exercises', re.search(r'font-extrabold">\s*3\s*</span>\s*<span[^>]*>Exercises', h04) is not None),
    ('Progress 4/5', '">4<span class="font-bold opacity-50">/5' in h04),
    ('No 6/5', '6/5' not in h04),
    ('SVG hex', 'viewBox="0 0 280 324"' in h04),
    ('hero-abstract-card opacity', 'padding:0.25rem;opacity:0.75;' in h04),
    ('2-space child indent', h04.split('\n')[1].startswith('  <div')),
]

print('\nVerification:')
all_ok = True
for label, ok in checks:
    print(f'  {"OK  " if ok else "FAIL"}: {label}')
    if not ok:
        all_ok = False

print('\n' + ('All checks passed.' if all_ok else 'Some checks FAILED.'))
