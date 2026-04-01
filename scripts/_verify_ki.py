import os, re

base = "pages/track_03_data_engineering"
bad = []
total = 0
for root, dirs, files in os.walk(base):
    for f in sorted(files):
        if not f.endswith(".html"):
            continue
        total += 1
        fp = os.path.join(root, f)
        content = open(fp, encoding="utf-8").read()
        sections = re.findall(r'<section id="([^"]+)"', content)
        if len(sections) < 8:
            bad.append((fp, len(sections), sections))

if bad:
    for fp, n, ss in bad:
        print(f"  LOW ({n}): {fp}")
        print(f"       {ss}")
else:
    print(f"All {total} files have 8+ sections - OK")

# Spot-check one file
fp2 = os.path.join(base, "mod_03_api_data_integration", "lesson01_what_is_an_api.html")
content = open(fp2, encoding="utf-8").read()
sections = re.findall(r'<section id="([^"]+)"', content)
print(f"Spot check: {len(sections)} sections: {sections}")
print(f"  pink={('obj-card-kt' in content)}, violet={('obj-card-violet' in content)}, blue={('obj-card-blue' in content)}")
print(f"  Title ok: {'APIs Connect Separate Systems' in content}")
