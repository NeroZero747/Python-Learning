"""Verify the #overview section of lesson02_project_folder_structure.html."""

from pathlib import Path
import re

TARGET = Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices"
    "/lesson02_project_folder_structure.html"
)

html = TARGET.read_text(encoding="utf-8")

# Extract the overview section only
ov_start = html.index('<section id="overview">')
ov_end = html.index("</section>", ov_start) + len("</section>")
ov = html[ov_start:ov_end]

checks = []

def chk(label, cond):
    status = "✅" if cond else "❌"
    checks.append((status, label))
    return cond

# 1. Section wrapper intact
chk("section id='overview' present", 'id="overview"' in ov)

# 2. Body div preserved
chk("body div has space-y-5", 'class="bg-white px-8 py-7 space-y-5"' in ov)

# 3. Hook banner — key structural requirement
chk("hook banner uses flex items-center gap-4 (not items-start)", "flex items-center gap-4" in ov)
chk("hook banner does NOT use items-start", "flex items-start gap-4" not in ov)
chk("no mt-0.5 on icon span inside hook banner", 'from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">' in ov)
chk("hook quote icon present", 'data-icon="fa6-solid:quote-left"' in ov)
chk("hook sentence: 'A project folder structure'", "A project folder structure is the system of subfolders" in ov)

# 4. Analogy paragraph
chk("analogy starts with 'Think of'", "Think of your Python project like a filing cabinet" in ov)
chk("analogy paragraph present", "project folder" in ov and "filing cabinet" in ov)

# 5. Cards — all 4 icons must be present
chk("card 1 icon fa6-solid:folder-open", 'data-icon="fa6-solid:folder-open"' in ov)
chk("card 2 icon fa6-solid:folder-tree", 'data-icon="fa6-solid:folder-tree"' in ov)
chk("card 3 icon fa6-solid:file-code", 'data-icon="fa6-solid:file-code"' in ov)
chk("card 4 icon fa6-solid:layer-group", 'data-icon="fa6-solid:layer-group"' in ov)

# 6. Card titles
chk("card 1 title: Why structure matters", "Why structure matters" in ov)
chk("card 2 title: Organizing into folders", "Organizing into folders" in ov)
chk("card 3 title: One script, one job", "One script, one job" in ov)
chk("card 4 title: The standard layout", "The standard layout" in ov)

# 7. Card subtitles (analogy echoes)
chk("card 1 subtitle mentions cabinet", "cabinet itself" in ov)
chk("card 2 subtitle mentions labeled drawers", "labeled drawers" in ov)
chk("card 3 subtitle mentions drawer",  "drawer" in ov)
chk("card 4 subtitle mentions cabinet model", "cabinet model" in ov)

# 8. Color accents — 4 distinct colors
chk("pink accent on card 1 (text-brand / [#fdf0f7])", "text-brand" in ov and "bg-[#fdf0f7]" in ov)
chk("violet accent on card 2", "text-violet-500" in ov)
chk("blue accent on card 3", "text-blue-500" in ov)
chk("emerald accent on card 4", "text-emerald-500" in ov)

# 9. Amber tip
chk("amber tip uses bg-amber-tip", "bg-amber-tip" in ov)
chk("amber tip icon fa6-solid:circle-info", 'data-icon="fa6-solid:circle-info"' in ov)
chk("amber tip mentions folders/desktop", "folders on your desktop" in ov)

# 10. No old content
chk("old pill chip 'analysis.py' removed", "analysis.py" not in ov)
chk("old 'Inside this file' text removed", "Inside this file might be" not in ov)
chk("no British spelling 'organised'", "organised" not in ov)

# 11. 2-column grid present
chk("card grid class sm:grid-cols-2", "sm:grid-cols-2 gap-3" in ov)

# Summary
passed = sum(1 for s, _ in checks if s == "✅")
total = len(checks)
print(f"\n{'='*55}")
print(f"  #overview verify — {passed}/{total} checks passed")
print(f"{'='*55}")
for s, label in checks:
    print(f"  {s}  {label}")

if passed < total:
    print(f"\n❌  {total - passed} check(s) failed.")
else:
    print(f"\n🎉  All {total} checks passed.")
