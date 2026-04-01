"""Audit track_03 lessons: extract titles, tab counts, lesson positions, difficulty hints."""
import os, re

BASE = "pages/track_03_data_engineering"
modules = {}

for root, dirs, files in os.walk(BASE):
    dirs.sort()
    for f in sorted(files):
        if not f.endswith(".html"):
            continue
        fp = os.path.join(root, f)
        mod = os.path.basename(root)
        rel = f"{mod}/{f}"
        c = open(fp, encoding="utf-8").read()

        # Extract lesson title from <h1>
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", c, re.DOTALL)
        title = h1.group(1).strip() if h1 else "NO H1"
        # Strip any HTML tags from title
        title = re.sub(r"<[^>]+>", "", title).strip()

        # Count ce-step tabs (code examples)
        ce_count = len(re.findall(r'class="[^"]*\bce-step\b', c))

        # Count pe-step tabs (practice exercises)
        pe_count = len(re.findall(r'class="[^"]*\bpe-step\b', c))

        # Count qz-step tabs (quiz)
        qz_count = len(re.findall(r'class="[^"]*\bqz-step\b', c))

        # Extract lesson number from filename
        ln_match = re.search(r"lesson(\d+)", f)
        lesson_num = int(ln_match.group(1)) if ln_match else 0

        # Check existing difficulty in hero
        diff_match = re.search(r"(Beginner|Intermediate|Advanced)", c[:3000])
        difficulty = diff_match.group(1) if diff_match else "?"

        # Check existing read time
        time_match = re.search(r"(\d+)\s*min\s*read", c[:3000])
        read_time = time_match.group(0) if time_match else "?"

        modules.setdefault(mod, []).append({
            "file": f,
            "lesson_num": lesson_num,
            "title": title,
            "ce": ce_count,
            "pe": pe_count,
            "qz": qz_count,
            "difficulty": difficulty,
            "read_time": read_time,
        })

for mod in sorted(modules):
    lessons = sorted(modules[mod], key=lambda x: x["lesson_num"])
    total = len(lessons)
    mod_num = re.search(r"mod_(\d+)", mod)
    mn = int(mod_num.group(1)) if mod_num else 0
    print(f"\n=== {mod} (Module {mn}, {total} lessons) ===")
    for i, l in enumerate(lessons, 1):
        print(f"  {i}/{total} {l['file']}")
        print(f"    Title: {l['title']}")
        print(f"    CE={l['ce']} PE={l['pe']} QZ={l['qz']} Diff={l['difficulty']} Time={l['read_time']}")
