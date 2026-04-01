#!/usr/bin/env python3
"""Extract objective card icons and labels from all track_03 lessons."""
import re, pathlib

root = pathlib.Path(r"c:\Users\nightwolf\Projects\Python-Learning\pages\track_03_data_engineering")
files = sorted(root.rglob("*.html"))

sec_pat = re.compile(r'<section id="objective">.*?</section>', re.DOTALL)
card_pat = re.compile(
    r'data-icon="([^"]+)">\s*</span>\s*</span>\s*<div>\s*<p class="text-sm font-semibold text-gray-800">([^<]+)</p>',
    re.DOTALL,
)

total = 0
for f in files:
    text = f.read_text(encoding="utf-8")
    m = sec_pat.search(text)
    if not m:
        print(f"NO_OBJ: {f.relative_to(root)}")
        continue
    cards = card_pat.findall(m.group(0))
    rel = str(f.relative_to(root)).replace("\\", "/")
    if len(cards) != 4:
        print(f"CARDS={len(cards)}: {rel}")
    else:
        total += 1
        for i, (icon, label) in enumerate(cards):
            print(f"{rel}|{i+1}|{icon}|{label.strip()}")

print(f"\nTotal with 4 cards: {total}")
