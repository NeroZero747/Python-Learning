import re, os

DIRS = [
    '/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_01_getting_started/',
]
TEMPLATE = '/Users/graywolf/Documents/Project/Python-Learning/docs/new_lesson_template.html'

# --- patterns to fix ---

# 1. TOC sidebar: float:right + margin-left  →  float:left + margin-right
OLD_TOC = (
    '.lesson-toc-sidebar { float: right; width: 240px; margin-left: 1.75rem; margin-bottom: 1rem; '
    'position: sticky; top: 1.5rem; max-height: calc(100vh - 2rem); overflow-y: auto; '
    'transition: width 0.25s ease, opacity 0.25s ease; }'
)
NEW_TOC = (
    '.lesson-toc-sidebar { float: left; width: 240px; margin-right: 1.75rem; margin-bottom: 1rem; '
    'position: sticky; top: 1.5rem; max-height: calc(100vh - 2rem); overflow-y: auto; '
    'transition: width 0.25s ease, opacity 0.25s ease; }'
)

# 2. After .lesson-layout { display: block; }, inject a BFC rule for the main content
#    so it sits beside the float rather than flowing under it.
OLD_LAYOUT = '.lesson-layout { display: block; }'
NEW_LAYOUT  = (
    '.lesson-layout { display: block; }\n'
    '    .lesson-layout > main { overflow: hidden; }'   # creates BFC beside the float
)

# 3. mobile override: already has float:none, keep as-is; just ensure layout stays block
OLD_MOBILE_TOC = '.lesson-toc-sidebar { float: none; display: none; }'
NEW_MOBILE_TOC = '.lesson-toc-sidebar { float: none; display: none; }'  # no change needed

files = []
for d in DIRS:
    files += [os.path.join(d, f) for f in sorted(os.listdir(d)) if f.endswith('.html')]
files.append(TEMPLATE)

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    if OLD_TOC in content:
        content = content.replace(OLD_TOC, NEW_TOC, 1)
        changed = True

    # For the template the layout rule is multi-line; handle both inline and multiline
    if OLD_LAYOUT in content and '.lesson-layout > main' not in content:
        content = content.replace(OLD_LAYOUT, NEW_LAYOUT, 1)
        changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("FIXED  " + os.path.basename(filepath))
    else:
        print("SKIP   " + os.path.basename(filepath))
