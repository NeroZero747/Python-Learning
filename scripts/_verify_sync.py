import os, re

base = "pages/track_03_data_engineering"
total = 0
issues = []
for root, dirs, files in os.walk(base):
    for f in sorted(files):
        if not f.endswith(".html"):
            continue
        total += 1
        fp = os.path.join(root, f)
        c = open(fp, encoding="utf-8").read()
        rel = os.path.relpath(fp, base)

        # 1 starts with link
        if not c.lstrip().startswith("<link rel="):
            issues.append(f"{rel}: bad start")

        # 2 no forbidden tags
        low = c.lower()
        for tag in ["<!doctype", "<html", "</html>", "<head>", "</head>", "<body", "</body>"]:
            if tag in low:
                issues.append(f"{rel}: has {tag}")

        # 3 hub-root exactly once
        hub_count = c.count('id="hub-root"')
        if hub_count != 1:
            issues.append(f"{rel}: hub-root count={hub_count}")

        # 4 ends with </script>
        stripped = c.rstrip()
        last_line = stripped.split("\n")[-1].strip()
        if last_line != "</script>":
            issues.append(f"{rel}: ends with {last_line[:30]}")

        # 5 style block size
        m = re.search(r"<style>(.*?)</style>", c, re.DOTALL)
        if m:
            sl = m.group(0).count("\n") + 1
            if sl < 400:
                issues.append(f"{rel}: style={sl} lines")
        else:
            issues.append(f"{rel}: no style block")

        # 6 white hover
        km = re.search(r"\.obj-card-kt:hover\s*\{[^}]+\}", c)
        if km and "background-color: #ffffff" not in km.group():
            issues.append(f"{rel}: kt hover missing bg-white")

if issues:
    for i in issues:
        print(f"  ISSUE: {i}")
else:
    print(f"All {total} files pass all 6 verification checks")
