import os
import re

DIR = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations"
files = [f for f in sorted(os.listdir(DIR)) if f.startswith("lesson0") and f.endswith(".html") and f != "lesson01_what_is_programming.html"]

for f in files:
    path = os.path.join(DIR, f)
    with open(path) as fh:
        content = fh.read()

    # Remove any leading lines that are <meta ...> tags (head-only metadata)
    # Keep stripping from the top until we hit a <link or <script line
    lines = content.split('\n')
    while lines and re.match(r'^\s*<meta\s', lines[0]):
        lines.pop(0)
    content = '\n'.join(lines)

    with open(path, "w") as fh:
        fh.write(content)
    print(f"cleaned: {f} — now starts with: {lines[0][:70]}")
