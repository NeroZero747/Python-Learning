import os

LESSON_DIR = '/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_01_getting_started/'

BROKEN = (
    "    :root {\n"
    "      --font-body: var(--font-body);\n"
    "      --font-mono: var(--font-mono);\n"
    "    }"
)
FIXED = (
    "    :root {\n"
    "      --font-body: 'Inter', -apple-system, 'Segoe UI', Roboto, sans-serif;\n"
    "      --font-mono: 'Fira Code', monospace;\n"
    "    }"
)

for filename in sorted(os.listdir(LESSON_DIR)):
    if not filename.endswith('.html'):
        continue
    filepath = os.path.join(LESSON_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if BROKEN in content:
        content = content.replace(BROKEN, FIXED, 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("FIXED  " + filename)
    else:
        print("OK     " + filename)
