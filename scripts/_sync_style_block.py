import os
import re

DIR = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations"

# --- Extract lesson01's style block (everything from <style> to </style> inclusive) ---
with open(os.path.join(DIR, "lesson01_what_is_programming.html")) as fh:
    l01 = fh.read()

style_match = re.search(r'(  <style>.*?  </style>)', l01, re.DOTALL)
if not style_match:
    print("ERROR: could not find style block in lesson01")
    exit(1)

L01_STYLE = style_match.group(1)
print(f"Extracted lesson01 style block: {len(L01_STYLE.splitlines())} lines")

# --- Apply to lessons 02-06 ---
TARGET_FILES = [
    "lesson02_variables_data_types.html",
    "lesson03_additional_python_data_types.html",
    "lesson04_lists_dictionaries.html",
    "lesson05_operators.html",
    "lesson06_if_statements.html",
    "lesson07_loops.html",
    "lesson08_functions.html",
    "lesson09_reading_understanding_errors.html",
]

for f in TARGET_FILES:
    path = os.path.join(DIR, f)
    with open(path) as fh:
        content = fh.read()

    # Find and replace the existing style block
    new_content = re.sub(r'  <style>.*?  </style>', L01_STYLE, content, count=1, flags=re.DOTALL)

    if new_content == content:
        print(f"NO CHANGE: {f} — style block not found or already matches")
        continue

    with open(path, "w") as fh:
        fh.write(new_content)
    print(f"updated: {f}")
