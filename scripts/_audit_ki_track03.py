"""Audit all track_03 lessons for key-ideas section status."""
import os
import re

BASE = "pages/track_03_data_engineering"

files = []
for root, dirs, fnames in os.walk(BASE):
    for f in sorted(fnames):
        if f.endswith(".html"):
            files.append(os.path.join(root, f))

files.sort()

for fp in files:
    with open(fp, "r", encoding="utf-8") as fh:
        content = fh.read()

    has_ki = 'id="key-ideas"' in content
    kt_cards = len(re.findall(r"obj-card-kt|obj-card-violet|obj-card-blue", content))

    hero_match = re.search(r"<h1[^>]*>(.*?)</h1>", content, re.DOTALL)
    title = hero_match.group(1).strip() if hero_match else "NO TITLE"
    title = re.sub(r"<[^>]+>", "", title).strip()[:80]

    rel = fp.replace(BASE + os.sep, "").replace(os.sep, "/")
    if has_ki:
        status = f"{kt_cards} KT cards"
    else:
        status = "NO key-ideas"
    print(f"{rel} | {title} | {status}")
