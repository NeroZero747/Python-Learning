import re

TARGET = r'c:\Users\nightwolf\Projects\Python-Learning\pages\track_01_python_foundation\mod_04_python_best_practices\lesson04_logging_basics.html'

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

# Count ce-step tabs (switchCeTab calls)
ce_tabs = len(re.findall(r'switchCeTab\(\d+\)', content))
# Count pe-step tabs (switchPeTab calls)
pe_tabs = len(re.findall(r'switchPeTab\(\d+\)', content))

print(f'Code Example tabs (ce): {ce_tabs}')
print(f'Practice Exercise tabs (pe): {pe_tabs}')

# Show current hero lesson-specific fields
MARKER = '<section class="hero-container">'
start = content.find(MARKER)
pos = start + len(MARKER)
depth = 1
while depth > 0 and pos < len(content):
    next_open  = content.find('<section', pos)
    next_close = content.find('</section>', pos)
    if next_close == -1: break
    if next_open != -1 and next_open < next_close:
        depth += 1; pos = next_open + 1
    else:
        depth -= 1
        if depth == 0: end = next_close + len('</section>')
        pos = next_close + 1

hero = content[start:end]

# Extract key fields
for pattern, label in [
    (r'data-icon="(fa6-solid:[^"]+)".*?Module (\d+)', 'Module icon + num'),
    (r'Lesson \d+</p>', 'Lesson label'),
    (r'<h1[^>]+>([^<]+)</h1>', 'Title'),
    (r'max-w-(?:prose|lg)">(.*?)</p>', 'Subtitle'),
    (r'<span class="text-white/85 font-medium text-xs">([^<]+)</span>\s*</div>\s*</div>\s*<div', 'Date'),
    (r'"font-extrabold">(\d+)</span>\s*<span class="font-semibold opacity-55">Goals', 'Goals'),
    (r'"font-extrabold">(\d+)</span>\s*<span class="font-semibold opacity-55">Examples', 'Examples'),
    (r'"font-extrabold">(\d+)</span>\s*<span class="font-semibold opacity-55">Exercises', 'Exercises'),
    (r'font-extrabold">(\d+)<span class="font-bold opacity-50">/(\d+)', 'Progress'),
]:
    m = re.search(pattern, hero, re.DOTALL)
    if m:
        print(f'{label}: {m.group(0)[:80].strip()}')
    else:
        print(f'{label}: NOT FOUND')
