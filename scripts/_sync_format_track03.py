"""
Sync all track_03 lesson files to Confluence-ready format:
  Step 1 - Strip DOCTYPE/html/head/body shell tags
  Step 2 - Replace <style> block with reference lesson01's full block
  Step 3 - Add id="hub-root" to outer wrapper
  Step 4 - Ensure white-hover fix on KT card variants (already in reference)
"""
import os
import re

BASE = "pages/track_03_data_engineering"
REF  = "pages/track_01_python_foundation/mod_02_programming_foundations/lesson01_what_is_programming.html"

# -- Load the reference style block --
ref_lines = open(REF, encoding="utf-8").readlines()
ref_s_start = ref_s_end = None
for i, l in enumerate(ref_lines):
    if "<style>" in l and ref_s_start is None:
        ref_s_start = i
    if "</style>" in l:
        ref_s_end = i
REF_STYLE = "".join(ref_lines[ref_s_start : ref_s_end + 1])
ref_style_linecount = ref_s_end - ref_s_start + 1
print(f"Reference style block: {ref_style_linecount} lines")

# Sanity: reference already has the white-hover fix
assert "background-color: #ffffff" in REF_STYLE, "Reference missing white-hover fix!"


def sync_file(filepath):
    """Apply all 4 sync steps. Returns (ok, messages)."""
    msgs = []
    content = open(filepath, encoding="utf-8").read()

    # -- Step 1: Strip forbidden HTML shell tags --
    link_match = re.search(r'^[ \t]*<link\s+rel="preconnect"', content, re.MULTILINE)
    if link_match:
        top_removed = content[:link_match.start()]
        if any(tag in top_removed.lower() for tag in ["<!doctype", "<html", "<head", "<meta", "<title"]):
            content = content[link_match.start():]
            msgs.append("Step 1a: stripped top HTML shell")
        else:
            msgs.append("Step 1a: no top shell to strip")
    else:
        msgs.append("Step 1a: WARN no <link preconnect> found")

    # Remove </head> and <body> if still present
    content = re.sub(r'^\s*</head>\s*\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\s*<body[^>]*>\s*\n', '', content, flags=re.MULTILINE)

    # Remove trailing </body> and </html>
    content = re.sub(r'\s*</body>\s*\n?\s*</html>\s*$', '', content)
    content = content.rstrip() + "\n"
    msgs.append("Step 1b: stripped bottom HTML shell")

    # -- Step 2: Replace style block --
    style_pat = re.compile(r'<style>.*?</style>', re.DOTALL)
    if style_pat.search(content):
        content = style_pat.sub(REF_STYLE.rstrip(), content, count=1)
        msgs.append("Step 2: style block replaced")
    else:
        msgs.append("Step 2: WARN no <style> block found")

    # -- Step 3: Add id="hub-root" --
    if 'id="hub-root"' in content:
        msgs.append("Step 3: hub-root already present")
    else:
        old = '<div class="bg-gray-50 min-h-screen">'
        new = '<div id="hub-root" class="bg-gray-50 min-h-screen">'
        if old in content:
            content = content.replace(old, new, 1)
            msgs.append("Step 3: added id=hub-root")
        else:
            msgs.append("Step 3: WARN wrapper div not found")

    # -- Step 4: White-hover fix (already in reference) --
    has_kt = ".obj-card-kt:hover" in content and "background-color: #ffffff" in content
    if has_kt:
        msgs.append("Step 4: white-hover already correct")
    else:
        content = content.replace(
            ".obj-card-kt:hover { box-shadow: none; }",
            ".obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }")
        content = content.replace(
            ".obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; }",
            ".obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; background-color: #ffffff; }")
        content = content.replace(
            ".obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; }",
            ".obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; background-color: #ffffff; }")
        msgs.append("Step 4: applied white-hover fix")

    # -- Write back --
    open(filepath, "w", encoding="utf-8").write(content)
    return True, msgs


def verify_file(filepath):
    """Run the verification checklist. Returns list of failures."""
    content = open(filepath, encoding="utf-8").read()
    lines = content.split("\n")
    fails = []

    # 1: starts with <link rel="preconnect"
    first_line = lines[0].strip() if lines else ""
    if not first_line.startswith('<link rel="preconnect"'):
        fails.append("bad start: " + first_line[:60])

    # 2: ends with </script>
    last_nonblank = ""
    for l in reversed(lines):
        if l.strip():
            last_nonblank = l.strip()
            break
    if last_nonblank != "</script>":
        fails.append("bad end: " + last_nonblank[:40])

    # 3: no forbidden tags
    for tag in ["<!DOCTYPE", "<html", "</html>", "<head>", "</head>", "<body", "</body>"]:
        if tag.lower() in content.lower():
            fails.append("contains " + tag)

    # 4: hub-root present once
    count = content.count('id="hub-root"')
    if count != 1:
        fails.append("hub-root count=" + str(count))

    # 5: style block line count
    m_style = re.search(r"<style>(.*?)</style>", content, re.DOTALL)
    if m_style:
        style_lines = m_style.group(0).count("\n") + 1
        if style_lines < 400:
            fails.append("style only " + str(style_lines) + " lines")
    else:
        fails.append("no style block")

    # 6: white-hover fix
    if ".obj-card-kt:hover" in content:
        kt_match = re.search(r"\.obj-card-kt:hover\s*\{[^}]+\}", content)
        if kt_match and "background-color: #ffffff" not in kt_match.group():
            fails.append("obj-card-kt missing bg-white")

    return fails


# -- Main --
ok = 0
fail = 0
verify_fail = 0

for root, dirs, files in os.walk(BASE):
    dirs.sort()
    for f in sorted(files):
        if not f.endswith(".html"):
            continue
        fp = os.path.join(root, f)
        rel = os.path.relpath(fp, BASE)

        success, msgs = sync_file(fp)
        vfails = verify_file(fp)

        if vfails:
            print(f"  [VERIFY FAIL] {rel}: {vfails}")
            verify_fail += 1
        elif success:
            print(f"  [OK] {rel}")
            ok += 1
        else:
            print(f"  [FAIL] {rel}: {msgs}")
            fail += 1

print(f"\nDone: {ok} synced OK, {fail} failed, {verify_fail} verify failures")
