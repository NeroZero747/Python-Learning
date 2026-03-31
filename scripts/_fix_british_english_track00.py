import os

TARGET_DIR = "pages/track_00_getting_started/mod_01_getting_started"
files = [os.path.join(TARGET_DIR, f) for f in os.listdir(TARGET_DIR) if f.endswith(".html")]

replacements = [
    ("/* \u2500\u2500 Text colours \u2500\u2500 */", "/* \u2500\u2500 Text colors \u2500\u2500 */"),
    ("/* \u2500\u2500 Background-colour utilities \u2500\u2500 */", "/* \u2500\u2500 Background-color utilities \u2500\u2500 */"),
    ("token colours (mirrors", "token colors (mirrors"),
    ("organised.", "organized."),
    ("organised ", "organized "),
    ("organised,", "organized,"),
]

for path in sorted(files):
    with open(path, "r", encoding="utf-8") as fh:
        original = fh.read()
    updated = original
    for old, new in replacements:
        updated = updated.replace(old, new)
    if updated != original:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(updated)
        print("patched: " + os.path.basename(path))
    else:
        print("no change: " + os.path.basename(path))
