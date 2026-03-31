target = r'pages\track_01_python_foundation\mod_04_python_best_practices\lesson04_logging_basics.html'
with open(target, encoding='utf-8') as fh:
    content = fh.read()

import re

def remove_section(html, section_id):
    """Remove a <section id="...">...</section> block plus the surrounding newline."""
    pattern = rf'\n[ \t]*<section id="{re.escape(section_id)}"[\s\S]*?</section>'
    m = re.search(pattern, html)
    if not m:
        print(f'ERROR: section id="{section_id}" not found')
        return html, False
    html = html[:m.start()] + html[m.end():]
    print(f'Removed: id="{section_id}"  ({len(m.group())} chars)')
    return html, True

content, ok1 = remove_section(content, 'decision-flow')
content, ok2 = remove_section(content, 'comparison')

if ok1 and ok2:
    with open(target, 'w', encoding='utf-8') as fh:
        fh.write(content)
    print('File saved.')

# Verify
import re as re2
ids = re2.findall(r'<section id="([^"]+)"', content)
print('Remaining sections:', ids)
assert 'decision-flow' not in ids, 'decision-flow still present'
assert 'comparison' not in ids,    'comparison still present'
print('All checks passed.')
