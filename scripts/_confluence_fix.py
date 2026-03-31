import re, os

LESSON_DIR = '/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_01_getting_started/'

ROOT_VARS = (
    "    :root {\n"
    "      --font-body: 'Inter', -apple-system, 'Segoe UI', Roboto, sans-serif;\n"
    "      --font-mono: 'Fira Code', monospace;\n"
    "    }\n\n"
)

for filename in sorted(os.listdir(LESSON_DIR)):
    if not filename.endswith('.html'):
        continue

    filepath = os.path.join(LESSON_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # ── 1. REMOVE STRUCTURAL HTML TAGS (keep inner content) ──────────────────
    content = re.sub(r'^<!DOCTYPE html>\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^<html[^>]*>\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^<head>\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\s*<meta charset="[^"]*">\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\s*<meta name="viewport"[^>]*>\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\s*<title>[^<]*</title>\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\s*<meta name="description"[^>]*>\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^</head>\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^<body>\n', '', content, flags=re.MULTILINE)
    # Remove </body></html> at end of file
    content = re.sub(r'\n</body>\n</html>\s*$', '', content)

    # ── 2. FONT CONSISTENCY: :root CSS custom properties ──────────────────────
    if ':root {' not in content:
        content = content.replace('  <style>\n', '  <style>\n' + ROOT_VARS, 1)

    # Replace concrete font stacks with CSS variables
    content = content.replace(
        "'Inter', -apple-system, 'Segoe UI', Roboto, sans-serif",
        "var(--font-body)"
    )
    content = content.replace(
        "'Fira Code', monospace",
        "var(--font-mono)"
    )

    # ── 3. TOC: float right instead of flex-left ──────────────────────────────
    # .lesson-layout  – drop flex (inline AND multiline variants)
    content = re.sub(
        r'\.lesson-layout\s*\{[^}]*display:\s*flex;[^}]*\}',
        '.lesson-layout { display: block; }',
        content,
        flags=re.DOTALL
    )

    # .lesson-toc-sidebar base rule – add float:right, drop flex-shrink
    content = re.sub(
        r'\.lesson-toc-sidebar\s*\{[^}]*flex-shrink[^}]*\}',
        (
            '.lesson-toc-sidebar { float: right; width: 240px; margin-left: 1.75rem; '
            'margin-bottom: 1rem; position: sticky; top: 1.5rem; '
            'max-height: calc(100vh - 2rem); overflow-y: auto; '
            'transition: width 0.25s ease, opacity 0.25s ease; }'
        ),
        content,
        flags=re.DOTALL
    )

    # Mobile override – clear the float too
    content = re.sub(
        r'(\.lesson-toc-sidebar\s*\{)\s*display:\s*none;\s*(\})',
        r'\1 float: none; display: none; \2',
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print("OK  " + filename)

print("\nDone – all lesson files updated.")
