import os

DIR = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations"
files = [f for f in sorted(os.listdir(DIR)) if f.startswith("lesson0") and f.endswith(".html") and f != "lesson01_what_is_programming.html"]

FIND = "    .toc-link.active { color: #CB187D; font-weight: 600; border-left: 3px solid #CB187D; padding-left: 8px; }"
ADD = (
    "\n"
    "  /* \u2500\u2500 Module lessons list active link \u2500\u2500 */\n"
    "  #hub-root .mod-lesson-active {\n"
    "    background-color: #fdf0f7 !important; border-color: #CB187D !important; color: #CB187D !important;\n"
    "  }\n"
    "  #hub-root .mod-lesson-active .lesson-dot { background-color: #CB187D !important; }"
)

for f in files:
    path = os.path.join(DIR, f)
    with open(path) as fh:
        content = fh.read()
    if "#hub-root .mod-lesson-active" in content:
        print(f"already patched: {f}")
        continue
    if FIND not in content:
        print(f"ANCHOR NOT FOUND: {f}")
        continue
    content = content.replace(FIND, FIND + ADD, 1)
    with open(path, "w") as fh:
        fh.write(content)
    print(f"patched: {f}")
