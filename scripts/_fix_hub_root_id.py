import os

DIR = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations"
files = [f for f in sorted(os.listdir(DIR)) if f.startswith("lesson0") and f.endswith(".html") and f != "lesson01_what_is_programming.html"]

FIND = '<div class="bg-gray-50 min-h-screen">'
REPLACE = '<div id="hub-root" class="bg-gray-50 min-h-screen">'

for f in files:
    path = os.path.join(DIR, f)
    with open(path) as fh:
        content = fh.read()
    if 'id="hub-root"' in content:
        print(f"already patched: {f}")
        continue
    if FIND not in content:
        print(f"ANCHOR NOT FOUND: {f}")
        continue
    content = content.replace(FIND, REPLACE, 1)
    with open(path, "w") as fh:
        fh.write(content)
    print(f"patched: {f}")
