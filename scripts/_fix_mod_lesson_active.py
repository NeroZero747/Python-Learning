#!/usr/bin/env python3
"""
Fix module lessons TOC active link in Confluence:
1. Add `mod-lesson-active` class to the currently-active lesson <a> tag
   (identified by containing `text-[#CB187D]` in its class list)
2. Add #hub-root .mod-lesson-active CSS override block
"""
import os, re

BASE = 'pages/track_01/mod_01_getting_started'
TEMPLATE = 'docs/new_lesson_template.html'

FILES = sorted(
    [os.path.join(BASE, f) for f in os.listdir(BASE) if f.endswith('.html')]
) + [TEMPLATE]

CSS_ANCHOR = '  #hub-root .toc-link.active {'
CSS_NEW = (
    '  /* -- Module lessons TOC active link -- */\n'
    '  #hub-root .mod-lesson-active {\n'
    '    background-color: #fdf0f7 !important;\n'
    '    border-color: #CB187D !important;\n'
    '    color: #CB187D !important;\n'
    '  }\n'
    '  #hub-root .mod-lesson-active .lesson-dot {\n'
    '    background-color: #CB187D !important;\n'
    '  }\n\n'
)

# Regex: <a href="..." class="... text-[#CB187D] ...">
# inside the toc-module-list section — mark it with mod-lesson-active class
ACTIVE_LINK_RE = re.compile(
    r'(<a\s[^>]*class="[^"]*text-\[#CB187D\][^"]*"[^>]*>)',
    re.DOTALL
)

def add_active_class(match):
    tag = match.group(1)
    if 'mod-lesson-active' in tag:
        return tag
    # Insert class at end of class attribute value
    tag = re.sub(
        r'(class="[^"]*)(text-\[#CB187D\][^"]*")',
        r'\1\2',
        tag
    )
    # Add mod-lesson-active to class list
    tag = re.sub(r'(class=")', r'\1mod-lesson-active ', tag)
    return tag

# Also make the dot span identifiable
DOT_IN_ACTIVE = re.compile(
    r'(mod-lesson-active[^>]*>)\s*(<span class="[^"]*bg-\[#CB187D\][^"]*")'
)

def add_dot_class(match):
    return match.group(1) + '\n                ' + match.group(2).replace('class="', 'class="lesson-dot ')


for path in FILES:
    name = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Inject CSS rule (once, before .toc-link.active block)
    if CSS_ANCHOR in content and '/* -- Module lessons TOC active link -- */' not in content:
        content = content.replace(CSS_ANCHOR, CSS_NEW + CSS_ANCHOR)

    # 2. Mark the active <a> with mod-lesson-active class
    content = ACTIVE_LINK_RE.sub(add_active_class, content)

    if content == original:
        print(f'  - no changes: {name}')
    else:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  OK: {name}')

print('\nDone.')
