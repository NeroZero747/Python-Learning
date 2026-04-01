"""Extract overview topics + current key-ideas card titles from all track_03 lessons."""
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

    rel = fp.replace(BASE + os.sep, "").replace(os.sep, "/")

    # Hero title
    hero_match = re.search(r"<h1[^>]*>(.*?)</h1>", content, re.DOTALL)
    title = re.sub(r"<[^>]+>", "", hero_match.group(1)).strip() if hero_match else "?"

    # Overview card titles (inside #overview section)
    ov_section = re.search(r'<section id="overview"[^>]*>(.*?)</section>', content, re.DOTALL)
    ov_titles = []
    if ov_section:
        # Look for bold titles in the overview card grid
        ov_titles = re.findall(r'<p class="text-sm font-bold text-gray-800[^"]*"[^>]*>(.*?)</p>', ov_section.group(1))
        if not ov_titles:
            ov_titles = re.findall(r'<p class="text-sm font-bold[^"]*"[^>]*>(.*?)</p>', ov_section.group(1))

    # Key-ideas card titles
    ki_section = re.search(r'<section id="key-ideas"[^>]*>(.*?)</section>', content, re.DOTALL)
    ki_titles = []
    if ki_section:
        ki_titles = re.findall(r'<h3 class="text-sm font-bold text-gray-900">(.*?)</h3>', ki_section.group(1))

    print(f"\n=== {rel} ===")
    print(f"  Title: {title}")
    print(f"  Overview: {', '.join(ov_titles) if ov_titles else 'NONE'}")
    print(f"  Key-Ideas: {', '.join(ki_titles) if ki_titles else 'NONE'}")
