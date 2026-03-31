import re
path = r'c:\Users\nightwolf\Projects\Python-Learning\pages\track_01_python_foundation\mod_04_python_best_practices\lesson04_logging_basics.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

for label in ['Goals', 'Examples', 'Exercises']:
    idx = content.find(label + '</span>')
    snippet = content[idx-200:idx+20]
    m = re.search(r'font-extrabold">(\d+)<', snippet)
    if m:
        print(f'{label}: {m.group(1)}')
    else:
        print(f'{label}: not found, snippet tail = {repr(snippet[-120:])}')

# Also check lesson label
idx = content.find('Lesson 04')
print(f'Lesson 04 label found: {idx != -1}')
idx = content.find('fa6-solid:star')
print(f'fa6-solid:star found: {idx != -1}')
idx = content.find('March 30, 2026')
print(f'March 30, 2026 found: {idx != -1}')
