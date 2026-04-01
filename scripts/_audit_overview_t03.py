"""Audit overview sections in all Track 03 lesson files."""
import os
import re
import html

base = r"c:\Users\nightwolf\Projects\Python-Learning\pages\track_03_data_engineering"
modules = sorted(os.listdir(base))

total_files = 0
complete_count = 0
partial_count = 0
missing_count = 0

for mod in modules:
    mod_path = os.path.join(base, mod)
    if not os.path.isdir(mod_path):
        continue
    files = sorted([f for f in os.listdir(mod_path) if f.endswith(".html")])
    print(f"\n{'='*80}")
    print(f"  {mod} ({len(files)} files)")
    print(f"{'='*80}")

    for fname in files:
        total_files += 1
        fpath = os.path.join(mod_path, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract h1 title
        h1_match = re.search(r"<h1[^>]*>(.+?)</h1>", content, re.DOTALL)
        title = html.unescape(h1_match.group(1).strip()) if h1_match else "NO TITLE"

        # Find overview section - get content between <section id="overview"> and next </section>
        ov_start = content.find('<section id="overview">')
        if ov_start == -1:
            print(f"\n  [{total_files:02d}] {fname}")
            print(f"       Title: {title}")
            print(f"       Status: MISSING SECTION")
            missing_count += 1
            continue

        # Find the closing </section> - need to handle nested sections
        depth = 0
        pos = ov_start
        ov_end = -1
        while pos < len(content):
            next_open = content.find("<section", pos + 1)
            next_close = content.find("</section>", pos + 1)
            if next_close == -1:
                break
            if next_open != -1 and next_open < next_close:
                depth += 1
                pos = next_open
            else:
                if depth == 0:
                    ov_end = next_close + len("</section>")
                    break
                depth -= 1
                pos = next_close

        if ov_end == -1:
            ov = content[ov_start:ov_start + 5000]
        else:
            ov = content[ov_start:ov_end]

        # Check 4 parts
        has_hook = "quote-left" in ov
        has_analogy_intro = "Think of" in ov or "think of" in ov
        has_card_grid = "grid grid-cols" in ov and ("grid-cols-2" in ov or "sm:grid-cols-2" in ov)
        has_tip = "bg-amber-tip" in ov

        parts_found = []
        parts_missing = []

        if has_hook:
            parts_found.append("Hook")
        else:
            parts_missing.append("Hook")

        if has_analogy_intro:
            parts_found.append("Analogy")
        else:
            parts_missing.append("Analogy")

        if has_card_grid:
            parts_found.append("CardGrid")
        else:
            parts_missing.append("CardGrid")

        if has_tip:
            parts_found.append("Tip")
        else:
            parts_missing.append("Tip")

        count = len(parts_found)

        if count == 4:
            status = "COMPLETE"
            complete_count += 1
        else:
            status = f"PARTIAL ({count}/4)"
            partial_count += 1

        # Check section header icon
        has_binoculars = "fa6-solid:binoculars" in ov

        print(f"\n  [{total_files:02d}] {fname}")
        print(f"       Title: {title}")
        print(f"       Status: {status}")
        if parts_found:
            print(f"       Has: {', '.join(parts_found)}")
        if parts_missing:
            print(f"       Missing: {', '.join(parts_missing)}")
        if not has_binoculars:
            print(f"       WARNING: No binoculars icon in section header")

print(f"\n{'='*80}")
print(f"  SUMMARY")
print(f"{'='*80}")
print(f"  Total files:    {total_files}")
print(f"  Complete (4/4): {complete_count}")
print(f"  Partial:        {partial_count}")
print(f"  Missing:        {missing_count}")
print(f"{'='*80}")
