#!/usr/bin/env python3
"""Extract objective card labels + icons from all track_03 lessons."""
import re, pathlib, json

ROOT = pathlib.Path(r"c:\Users\nightwolf\Projects\Python-Learning\pages\track_03_data_engineering")
files = sorted(ROOT.rglob("*.html"))

pat_card = re.compile(
    r'<div class="obj-card.*?data-icon="([^"]+)".*?'
    r'<p class="text-sm font-semibold text-gray-800">(.*?)</p>',
    re.DOTALL
)

results = {}
for f in files:
    text = f.read_text(encoding="utf-8")
    obj_match = re.search(r'<section id="objective">(.*?)</section>', text, re.DOTALL)
    if not obj_match:
        print(f"NO OBJ: {f.relative_to(ROOT)}")
        continue
    obj_html = obj_match.group(1)
    cards = pat_card.findall(obj_html)
    rel = str(f.relative_to(ROOT)).replace("\\", "/")
    if len(cards) != 4:
        print(f"CARDS={len(cards)}: {rel}")
    results[rel] = [(icon, label) for icon, label in cards]

print(json.dumps(results, indent=2))
