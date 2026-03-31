"""
Fix lesson04's hero indentation by using lesson03's hero as the template,
substituting only the lesson04-specific content fields.
"""

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
            depth += 1
            pos = next_open + 1
        else:
            depth -= 1
            if depth == 0:
                end = next_close + len('</section>')
            pos = next_close + 1
    return content, start, end

# Extract lesson03 hero as the indentation-correct template
c03, s03, e03 = extract_hero(PATH03)
hero03 = c03[s03:e03]

# Check what lesson03 progress position shows
import re
prog_m = re.search(r'font-extrabold">(\d+)<span class="font-bold opacity-50">/5', hero03)
print(f'Lesson03 progress position: {prog_m.group(1) if prog_m else "NOT FOUND"}')

# Lesson03 subtitle
sub_m = re.search(r'max-w-prose">(.*?)</p>', hero03, re.DOTALL)
print(f'Lesson03 subtitle: {sub_m.group(1).strip()[:80] if sub_m else "NOT FOUND"}')

# Build lesson04 hero from lesson03 template
hero04 = hero03

# 1. Lesson label: Lesson 03 → Lesson 04
hero04 = hero04.replace(
    '>Lesson 03</p>',
    '>Lesson 04</p>'
)

# 2. Title
hero04 = hero04.replace(
    '>Introduction to Git (Simple Workflow)</h1>',
    '>Logging Basics</h1>'
)

# 3. Subtitle
old_subtitle = sub_m.group(0)  # full <p ...>..text..</p> match
new_subtitle = 'max-w-prose">Learn how to use Python\u2019s logging module to track errors, record events, and monitor your program \u2014 the professional alternative to print statements.</p>'
hero04 = hero04.replace(old_subtitle, new_subtitle)

# 4. Progress position: lesson03 position → 4
old_pos = prog_m.group(1)
hero04 = re.sub(
    r'(font-extrabold">)' + re.escape(old_pos) + r'(<span class="font-bold opacity-50">/5</span></span>)',
    r'\g<1>4\2',
    hero04
)

print('\nVerification of substitutions:')
print('  Lesson 04 label:', 'Lesson 04</p>' in hero04)
print('  Logging Basics title:', 'Logging Basics</h1>' in hero04)
print('  Correct subtitle:', 'professional alternative to print statements.' in hero04)
print('  Progress 4/5:', 'font-extrabold">4<span class="font-bold opacity-50">/5' in hero04)
print('  Old lesson03 title absent:', 'Introduction to Git' not in hero04)
print('  Old lesson03 label absent:', '>Lesson 03</p>' not in hero04)

# Write into lesson04
c04, s04, e04 = extract_hero(PATH04)

# Preserve the original section's surrounding indentation prefix
line_start = c04.rfind('\n', 0, s04) + 1
outer_indent = c04[line_start:s04]
print(f'\nLesson04 outer indent before section: {repr(outer_indent)}')
print(f'First 80 chars of hero03: {repr(hero03[:80])}')

# hero03 already starts with <section (no leading spaces), so just use it directly
new_content = c04[:s04] + hero04 + c04[e04:]

with open(PATH04, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('\nWritten successfully.')

# Final check: compare indentation of first child in both heroes
def first_child_indent(hero_text):
    lines = hero_text.split('\n')
    for line in lines[1:]:  # skip section opening tag
        if line.strip():
            return len(line) - len(line.lstrip())
    return -1

c04_new, s04_new, e04_new = extract_hero(PATH04)
hero04_new = c04_new[s04_new:e04_new]

print(f'\nLesson03 first child indent: {first_child_indent(hero03)} spaces')
print(f'Lesson04 first child indent: {first_child_indent(hero04_new)} spaces')
print('Match:', first_child_indent(hero03) == first_child_indent(hero04_new))
