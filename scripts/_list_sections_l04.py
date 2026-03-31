target = r'pages\track_01_python_foundation\mod_04_python_best_practices\lesson04_logging_basics.html'
with open(target, encoding='utf-8') as fh:
    content = fh.read()

# Find all section IDs
import re
for m in re.finditer(r'<section id="([^"]+)"', content):
    pos = m.start()
    end = content.find('</section>', pos) + len('</section>')
    print(f'id="{m.group(1)}"  chars {pos}–{end}  ({end-pos} bytes)')
