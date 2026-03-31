"""Verify the #key-ideas section of lesson02_project_folder_structure.html."""

from pathlib import Path

TARGET = Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices"
    "/lesson02_project_folder_structure.html"
)

html = TARGET.read_text(encoding="utf-8")

# Extract the key-ideas section only
ki_start = html.index('<section id="key-ideas">')
ki_end   = html.index("</section>", ki_start) + len("</section>")
ki = html[ki_start:ki_end]

checks = []

def chk(label, cond):
    status = "✅" if cond else "❌"
    checks.append((status, label))
    return cond

# ── Section shell ──────────────────────────────────────────────────────────
chk("section id='key-ideas' present", 'id="key-ideas"' in ki)
chk("section header icon fa6-solid:lightbulb unchanged", 'data-icon="fa6-solid:lightbulb"' in ki)
chk("section title 'Key Takeaways' unchanged", "Key Takeaways" in ki)
chk("section subtitle unchanged", "The most important ideas to remember" in ki)
chk("body div has space-y-4", 'class="bg-white px-8 py-7 space-y-4"' in ki)

# ── Card 1 — Pink ──────────────────────────────────────────────────────────
chk("card 1 class obj-card-kt", "obj-card-kt" in ki)
chk("card 1 pink gradient bar", 'from-[#CB187D] to-[#e84aad]' in ki)
chk("card 1 icon fa6-solid:triangle-exclamation", 'data-icon="fa6-solid:triangle-exclamation"' in ki)
chk("card 1 title: Version Chaos Costs Real Time", "Version Chaos Costs Real Time" in ki)
chk("card 1 desc mentions report_v3_FINAL_final.py", "report_v3_FINAL_final.py" in ki)
chk("card 1 pill: Version creep", "Version creep" in ki)
chk("card 1 pill: File naming", "File naming" in ki)
chk("card 1 pill: Maintainability", "Maintainability" in ki)
chk("card 1 pills are pink (bg-pink-50 text-[#CB187D])", "bg-pink-50 text-[#CB187D]" in ki)

# ── Card 2 — Violet ────────────────────────────────────────────────────────
chk("card 2 class obj-card-violet", "obj-card-violet" in ki)
chk("card 2 violet gradient bar", "from-violet-500 to-purple-400" in ki)
chk("card 2 icon fa6-solid:scissors", 'data-icon="fa6-solid:scissors"' in ki)
chk("card 2 title: Fix One File, Break Nothing", "Fix One File, Break Nothing" in ki)
chk("card 2 desc mentions Excel", "Excel" in ki)
chk("card 2 pill: Isolation", "Isolation" in ki)
chk("card 2 pill: Safe edits", "Safe edits" in ki)
chk("card 2 pill: Single responsibility", "Single responsibility" in ki)
chk("card 2 pills are violet (bg-violet-50 text-violet-600)", "bg-violet-50 text-violet-600" in ki)

# ── Card 3 — Blue ──────────────────────────────────────────────────────────
chk("card 3 class obj-card-blue", "obj-card-blue" in ki)
chk("card 3 blue gradient bar", "from-blue-500 to-indigo-400" in ki)
chk("card 3 icon fa6-solid:users", 'data-icon="fa6-solid:users"' in ki)
chk("card 3 title: Structure Lets Others Navigate Fast", "Structure Lets Others Navigate Fast" in ki)
chk("card 3 desc mentions under a minute", "under a minute" in ki)
chk("card 3 pill: Collaboration", "Collaboration" in ki)
chk("card 3 pill: Onboarding", "Onboarding" in ki)
chk("card 3 pill: Readability", "Readability" in ki)
chk("card 3 pills are blue (bg-blue-50 text-blue-600)", "bg-blue-50 text-blue-600" in ki)

# ── No old content ──────────────────────────────────────────────────────────
chk("old split card (md:w-1/2) removed", "md:w-1/2" not in ki)
chk("old fa6-solid:terminal removed", 'data-icon="fa6-solid:terminal"' not in ki)
chk("old fa6-solid:glasses removed", 'data-icon="fa6-solid:glasses"' not in ki)
chk("old pre block with analysis_script_final removed", "analysis_script_final_v3" not in ki)

# ── CSS checks (full file scope) ───────────────────────────────────────────
chk("CSS: obj-card-kt:hover has border-color: #CB187D", "background-color: #ffffff; border-color: #CB187D;" in html)
chk("CSS: obj-card-violet:hover has border-color: #8b5cf6", "border-color: #8b5cf6" in html)
chk("CSS: obj-card-blue:hover has border-color: #3b82f6", "border-color: #3b82f6" in html)

# ── No British spellings ────────────────────────────────────────────────────
chk("no British spelling in section", "organised" not in ki and "colour" not in ki)

# ── Summary ─────────────────────────────────────────────────────────────────
passed = sum(1 for s, _ in checks if s == "✅")
total  = len(checks)
print(f"\n{'='*57}")
print(f"  #key-ideas verify — {passed}/{total} checks passed")
print(f"{'='*57}")
for s, label in checks:
    print(f"  {s}  {label}")

if passed < total:
    print(f"\n❌  {total - passed} check(s) failed.")
else:
    print(f"\n🎉  All {total} checks passed.")
