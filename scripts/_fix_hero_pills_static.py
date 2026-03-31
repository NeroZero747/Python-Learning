#!/usr/bin/env python3
"""
Convert hero stat pill <a href="..."> tags to static <span> tags.
Also removes the :hover transform from .hero-pill since static pills
should not imply interactivity.
"""
import os, re

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

# Remove the :hover rule from .hero-pill
HOVER_OLD = (
    '    .hero-pill:hover {\n'
    '      transform: translateY(-1px);\n'
    '    }\n'
)
HOVER_NEW = ''

def convert_pill_links(content):
    """Replace <a href="..." class="hero-pill ...no-underline"> with <span class="hero-pill ...">"""
    # Remove href and the no-underline class, change tag to span
    def replace_a(m):
        inner = m.group(1)  # everything inside the <a ...> attributes (after tag name)
        # Remove href="..." attribute
        inner = re.sub(r'\s*href="[^"]*"', '', inner)
        # Remove no-underline from class string
        inner = re.sub(r'\s*no-underline', '', inner)
        return f'<span{inner}>'

    # Match opening <a> tag that has hero-pill class
    content = re.sub(r'<a\b([^>]*class="[^"]*hero-pill[^"]*"[^>]*)>', replace_a, content)
    # Replace corresponding </a> with </span> (only those that were hero-pill anchors)
    # Since we've already replaced the opening tags, we can safely replace all </a>
    # that immediately wrap a hero-pill — but to be safe we only need to close spans
    # that were opened. The regex above closed all hero-pill <a> → <span>, so we
    # must close them. We do this by replacing </a> inside the stat-pills container.
    # Safe approach: replace ALL </a> that appear within the hero stat pills block.
    content = re.sub(
        r'(<!-- Stat pills -->.*?</div>\s*</div>\s*<!-- RIGHT COLUMN)',
        lambda m: m.group(0).replace('</a>', '</span>'),
        content,
        flags=re.DOTALL
    )
    return content


def fix_file(path):
    name = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # 1. Remove hero-pill hover rule
    content = content.replace(HOVER_OLD, HOVER_NEW)

    # 2. Convert <a hero-pill> anchors to <span>
    content = convert_pill_links(content)

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
