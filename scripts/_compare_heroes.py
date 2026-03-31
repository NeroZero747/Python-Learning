import sys

def extract_hero(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    MARKER = '<section class="hero-container">'
    start = content.find(MARKER)
    if start == -1:
        return None, None, None
    pos = start + len(MARKER)
    depth = 1
    while depth > 0 and pos < len(content):
        next_open  = content.find('<section', pos)
        next_close = content.find('</section>', pos)
        if next_close == -1:
            break
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 1
        else:
            depth -= 1
            if depth == 0:
                end = next_close + len('</section>')
            pos = next_close + 1
    return content, start, end

path03 = r'c:\Users\nightwolf\Projects\Python-Learning\pages\track_01_python_foundation\mod_04_python_best_practices\lesson03_introduction_to_git_simple_workflow.html'
path04 = r'c:\Users\nightwolf\Projects\Python-Learning\pages\track_01_python_foundation\mod_04_python_best_practices\lesson04_logging_basics.html'

_, s3, e3 = extract_hero(path03)
c4, s4, e4 = extract_hero(path04)

with open(path03, 'r', encoding='utf-8') as f:
    hero03 = f.read()[s3:e3]
hero04 = c4[s4:e4]

print('=== LESSON 03 HERO ===')
print(hero03)
print()
print('=== LESSON 04 HERO ===')
print(hero04)
