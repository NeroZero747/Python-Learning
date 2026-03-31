import os, re

LESSON_DIR = '/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_01_getting_started/'
TEMPLATE   = '/Users/graywolf/Documents/Project/Python-Learning/docs/new_lesson_template.html'

# ── lesson01 uses multiline heading block ─────────────────────────────────────
OLD_MULTI = (
    "    /* Headings */\n"
    "    h1, h2, h3, h4, h5, h6 {\n"
    "      margin-top: 0;\n"
    "      margin-bottom: 0;\n"
    "      padding: 0;\n"
    "      line-height: 1.3;\n"
    "    }\n"
    "    h2 { font-size: 1.25rem; font-weight: 700; }\n"
    "    h3 { font-size: 1rem; font-weight: 600; }"
)
NEW_MULTI = (
    "    /* Headings */\n"
    "    h1, h2, h3, h4, h5, h6 {\n"
    "      font-family: var(--font-body) !important;\n"
    "      margin-top: 0;\n"
    "      margin-bottom: 0;\n"
    "      padding: 0;\n"
    "      line-height: 1.3;\n"
    "    }\n"
    "    h1 { font-weight: 800 !important; }\n"
    "    h2 { font-size: 1.25rem; font-weight: 700 !important; }\n"
    "    h3 { font-size: 1rem;   font-weight: 600 !important; }"
)

# ── lessons02-06 use an inline heading block ───────────────────────────────────
OLD_INLINE = "    h1, h2, h3, h4, h5, h6 { margin-top: 0; margin-bottom: 0; padding: 0; line-height: 1.3; }\n    h2 { font-size: 1.25rem; font-weight: 700; }\n    h3 { font-size: 1rem; font-weight: 600; }"
NEW_INLINE = "    h1, h2, h3, h4, h5, h6 { font-family: var(--font-body) !important; margin-top: 0; margin-bottom: 0; padding: 0; line-height: 1.3; }\n    h1 { font-weight: 800 !important; }\n    h2 { font-size: 1.25rem; font-weight: 700 !important; }\n    h3 { font-size: 1rem;   font-weight: 600 !important; }"

files = [os.path.join(LESSON_DIR, f) for f in sorted(os.listdir(LESSON_DIR)) if f.endswith('.html')]
files.append(TEMPLATE)

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if OLD_MULTI in content:
        content = content.replace(OLD_MULTI, NEW_MULTI, 1)
        print("MULTI  " + os.path.basename(filepath))
    elif OLD_INLINE in content:
        content = content.replace(OLD_INLINE, NEW_INLINE, 1)
        print("INLINE " + os.path.basename(filepath))
    else:
        print("SKIP   " + os.path.basename(filepath))
        continue

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
