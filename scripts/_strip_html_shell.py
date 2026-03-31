import os
import re

DIR = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations"
files = [f for f in sorted(os.listdir(DIR)) if f.startswith("lesson0") and f.endswith(".html") and f != "lesson01_what_is_programming.html"]

for f in files:
    path = os.path.join(DIR, f)
    with open(path) as fh:
        content = fh.read()

    # Check if already stripped
    if not content.startswith("<!DOCTYPE"):
        print(f"already stripped: {f}")
        continue

    # Remove opening DOCTYPE/html/head lines (keep everything from first <link> or <meta> inside head)
    # Strip: <!DOCTYPE html>\n<html lang="en">\n<head>\n
    content = re.sub(r'^<!DOCTYPE html>\s*\n<html[^>]*>\s*\n<head>\s*\n', '', content)

    # Remove </head>\n<body>\n (with optional whitespace)
    content = re.sub(r'</head>\s*\n<body>\s*\n', '', content)

    # Remove trailing </body>\n</html> at end of file
    content = re.sub(r'\s*</body>\s*\n?</html>\s*$', '\n', content)

    # Also strip leading <meta> tags that are head-only (charset, viewport, title)
    # Keep only from the first <link> or <script> tag
    content = re.sub(r'^(\s*<meta[^>]*>\s*\n)+', '', content)
    content = re.sub(r'^(\s*<title>[^<]*</title>\s*\n)', '', content)

    with open(path, "w") as fh:
        fh.write(content)
    print(f"stripped: {f}")
