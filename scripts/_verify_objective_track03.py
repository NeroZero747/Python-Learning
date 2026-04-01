"""Verify #objective sections in all track_03 lesson files."""
import os, re

BASE = "pages/track_03_data_engineering"

CHECKS = {
    "section-id": r'<section id="objective">',
    "section-header": r'data-icon="fa6-solid:bullseye"',
    "header-title": r'>Lesson Objective<',
    "header-subtitle": r'>The goal and expected outcome of this lesson<',
    "4-obj-cards": None,  # special
    "amber-tip": r'class=".*?bg-amber-tip"',
    "tip-icon": r'data-icon="fa6-solid:circle-info"',
    "grid-layout": r'grid grid-cols-1 sm:grid-cols-2 gap-3',
    "card-icons": None,  # special: all 4 cards have distinct icons
    "sections-preserved-8+": None,
}

files = []
for root, dirs, fnames in os.walk(BASE):
    dirs.sort()
    for fn in sorted(fnames):
        if fn.endswith(".html"):
            files.append(os.path.join(root, fn))

pass_count = 0
fail_count = 0
for fp in files:
    content = open(fp, encoding="utf-8").read()
    rel = os.path.relpath(fp, BASE)
    issues = []

    # Extract objective section
    m = re.search(r'<section id="objective">(.*?)</section>', content, re.DOTALL)
    if not m:
        issues.append("no-objective-section")
    else:
        obj = m.group(1)

        # Check 4 obj-cards
        cards = re.findall(r'class="obj-card', obj)
        if len(cards) != 4:
            issues.append(f"obj-cards={len(cards)}")

        # Check 4 distinct icons
        icons = re.findall(r'data-icon="(fa6-solid:[^"]+)"', obj)
        # First icon is bullseye (header), rest should be 4 card icons
        card_icons = [i for i in icons if i != "fa6-solid:bullseye" and i != "fa6-solid:circle-info"]
        if len(card_icons) != 4:
            issues.append(f"card-icons={len(card_icons)}")
        elif len(set(card_icons)) != 4:
            issues.append("duplicate-icons")

    for label, pat in CHECKS.items():
        if pat is None:
            continue
        if not re.search(pat, content, re.DOTALL):
            issues.append(label)

    # Section count
    secs = re.findall(r'<section id="([^"]+)"', content)
    if len(secs) < 8:
        issues.append(f"sections={len(secs)}")

    if issues:
        print(f"  [FAIL] {rel}: {', '.join(issues)}")
        fail_count += 1
    else:
        pass_count += 1

print(f"\nVerified: {pass_count} passed, {fail_count} failed ({pass_count + fail_count} total)")
