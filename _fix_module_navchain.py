"""Repair bottom-nav prev/next links for all 16 lessons in module 5/6 SQL folder.

Strategy: for each file, locate its 'lesson-nav-link' bottom-nav block (the new-style
flex flex-col sm:flex-row block following <section id="next-lesson">) and update the
prev <a href> and next <a href> to point to the correct adjacent file.
"""

import os
import re

DIR = 'pages/mod_06a_sql_foundation/mod_05_sql_foundations'
files = sorted([f for f in os.listdir(DIR) if f.startswith('lesson') and f.endswith('.html')])
print(f"Found {len(files)} lessons.")

# Map filename → display title (taken from h1)
def get_title(content):
    m = re.search(r'<h1[^>]*tracking-tight">([^<]+)</h1>', content)
    return m.group(1).strip() if m else ''

titles = {}
for fn in files:
    with open(os.path.join(DIR, fn), 'r', encoding='utf-8') as fp:
        c = fp.read()
    titles[fn] = get_title(c)

# Iterate and rewrite the canonical bottom-nav block.
NAV_TEMPLATE_PREV = '''    <a href="{prev_href}" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{prev_title}</p>
      </div>
    </a>'''

NAV_TEMPLATE_PREV_SPACER = '    <div class="flex-1"></div>'

NAV_TEMPLATE_HUB = '''    <a href="../../hub_home_page.html" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>'''

NAV_TEMPLATE_NEXT = '''    <a href="{next_href}" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{next_title}</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>'''

NAV_TEMPLATE_NEXT_SPACER = '    <div class="flex-1"></div>'

# Pattern to find the new-style bottom-nav block: it's a <section> immediately after
# the </section> of #next-lesson, containing the flex container.
# We replace the entire <section> ... </section> at that position.

# Locate marker: '</section>\n\n<section>\n  <div class="flex flex-col sm:flex-row gap-3">'
NEW_NAV_REGEX = re.compile(
    r'<section>\s*\n\s*<div class="flex flex-col sm:flex-row gap-3">.*?</section>',
    re.DOTALL
)

# Old-style duplicate nav block (pre-existing legacy):
# '<div class="flex flex-col sm:flex-row gap-3 mt-6"><a href="..." ...>...</a></div>'
OLD_NAV_REGEX = re.compile(
    r'\s*<div class="flex flex-col sm:flex-row gap-3 mt-6">.*?</a></div>',
    re.DOTALL
)

for i, fn in enumerate(files):
    path = os.path.join(DIR, fn)
    with open(path, 'r', encoding='utf-8') as fp:
        c = fp.read()

    prev_fn = files[i - 1] if i > 0 else None
    next_fn = files[i + 1] if i < len(files) - 1 else None

    parts = []
    if prev_fn:
        parts.append(NAV_TEMPLATE_PREV.format(prev_href=prev_fn, prev_title=titles[prev_fn]))
    else:
        parts.append(NAV_TEMPLATE_PREV_SPACER)
    parts.append(NAV_TEMPLATE_HUB)
    if next_fn:
        parts.append(NAV_TEMPLATE_NEXT.format(next_href=next_fn, next_title=titles[next_fn]))
    else:
        parts.append(NAV_TEMPLATE_NEXT_SPACER)

    new_nav = '<section>\n  <div class="flex flex-col sm:flex-row gap-3">\n\n' + '\n\n'.join(parts) + '\n\n  </div>\n</section>'

    n_new = len(NEW_NAV_REGEX.findall(c))
    if n_new == 0:
        print(f"  ⚠️  {fn}: no new-style bottom nav found — skipping")
        continue
    c = NEW_NAV_REGEX.sub(new_nav, c, count=1)

    # Remove old-style duplicate nav block if present
    n_old = len(OLD_NAV_REGEX.findall(c))
    if n_old:
        c = OLD_NAV_REGEX.sub('', c, count=1)

    with open(path, 'w', encoding='utf-8') as fp:
        fp.write(c)

    prev_label = titles[prev_fn] if prev_fn else '(none)'
    next_label = titles[next_fn] if next_fn else '(none)'
    print(f"  ✅ {fn}: prev={prev_label!r}, next={next_label!r}{' (also stripped duplicate old nav)' if n_old else ''}")

print("\nDone.")
