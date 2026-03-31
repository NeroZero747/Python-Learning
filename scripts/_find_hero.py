path = r'c:\Users\nightwolf\Projects\Python-Learning\pages\track_01_python_foundation\mod_04_python_best_practices\lesson04_logging_basics.html'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
hero_start = None
hero_end = None
depth = 0
for i, line in enumerate(lines):
    if hero_start is None and '<section class="hero-container">' in line:
        hero_start = i + 1
        depth = 1
        continue
    if hero_start is not None:
        depth += line.count('<section') - line.count('</section')
        if depth <= 0:
            hero_end = i + 1
            break
print(f'Hero start line: {hero_start}, end line: {hero_end}')
print('End line content:', repr(lines[hero_end-1][:80]))
print('Line before end:', repr(lines[hero_end-2][:80]))
