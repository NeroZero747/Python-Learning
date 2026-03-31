"""Verify the #key-concepts section of lesson02_project_folder_structure.html."""

from pathlib import Path

TARGET = Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices"
    "/lesson02_project_folder_structure.html"
)

html = TARGET.read_text(encoding="utf-8")

# Extract the key-concepts section only
kc_start = html.index('id="key-concepts"')
# Back up to the opening <section tag
kc_start = html.rindex("<section", 0, kc_start)
kc_end   = html.index("</section>", kc_start) + len("</section>")
kc = html[kc_start:kc_end]

checks = []

def chk(label, cond):
    status = "✅" if cond else "❌"
    checks.append((status, label))
    return cond

# ── Section shell ──────────────────────────────────────────────────────────
chk("section id='key-concepts' present", 'id="key-concepts"' in kc)
chk("section header icon fa6-solid:book-open unchanged", 'data-icon="fa6-solid:book-open"' in kc)
chk("section title 'Key Concepts'", "Key Concepts" in kc)
chk("section subtitle updated (Project root, modules...)", "Project root, modules" in kc)
chk("section body uses px-6 py-7 (not px-8)", 'class="bg-white px-6 py-7"' in kc)

# ── Sidebar layout ─────────────────────────────────────────────────────────
chk("sidebar md:w-52", "md:w-52" in kc)
chk("kc-indicator present", "kc-indicator" in kc)
chk("kc-indicator uses inline style background (not Tailwind class)", 'style="height:68px;background:#CB187D;"' in kc)
chk("4 kc-tab buttons", kc.count('class="kc-tab') == 4 or "kc-tab kc-tab-active" in kc)

# ── Tab 0 — Project Root (pink) ────────────────────────────────────────────
chk("tab 0 label: Project Root", "Project Root" in kc)
chk("tab 0 icon fa6-solid:folder-open (sidebar)", 'data-icon="fa6-solid:folder-open"' in kc)
chk("tab 0 kc-tab-num uses inline style pink", "background:#CB187D;color:#fff;box-shadow:0 2px 8px rgba(203,24,125,0.25)" in kc)
chk("tab 0 kc-tab-active class", "kc-tab kc-tab-active" in kc)

# ── Tab 1 — Module (violet) ────────────────────────────────────────────────
chk("tab 1 label: Module", ">Module<" in kc)
chk("tab 1 icon fa6-solid:file-code (sidebar)", 'data-icon="fa6-solid:file-code"' in kc)
chk("tab 1 inactive style gray", 'style="background:#f3f4f6;color:#9ca3af"' in kc)

# ── Tab 2 — Data Folder (blue) ─────────────────────────────────────────────
chk("tab 2 label: Data Folder", "Data Folder" in kc)
chk("tab 2 icon fa6-solid:database", 'data-icon="fa6-solid:database"' in kc)

# ── Tab 3 — Entry Point (emerald) ─────────────────────────────────────────
chk("tab 3 label: Entry Point", "Entry Point" in kc)
chk("tab 3 icon fa6-solid:play (sidebar)", 'data-icon="fa6-solid:play"' in kc)

# ── Panel 0 — pink ────────────────────────────────────────────────────────
chk("panel 0 no 'hidden' class (active)", 'class="kc-panel kc-panel-anim"' in kc)
chk("panel 0 border-pink-100", "border border-pink-100" in kc)
chk("panel 0 pink gradient bar", 'from-[#CB187D] via-pink-400 to-rose-300' in kc)
chk("panel 0 from-pink-50/60 bg", "from-pink-50/60 to-white" in kc)
chk("panel 0 uses p-5 space-y-4", "p-5 space-y-4" in kc)
chk("panel 0 header chip gradient from-[#CB187D] to-[#e84aad]", "from-[#CB187D] to-[#e84aad]" in kc)
chk("panel 0 definition mentions 'project root'", "project root is the single top-level folder" in kc)
chk("panel 0 rules-table widget", "Folder Naming Rules" in kc)
chk("panel 0 code block has logos:python data-width='14'", 'data-icon="logos:python" data-width="14" data-height="14"' in kc)
chk("panel 0 tip bg-pink-50 border-pink-100", "bg-pink-50 border border-pink-100" in kc)
chk("panel 0 tip chip bg-[#CB187D]", "bg-[#CB187D] shrink-0 mt-0.5" in kc)
chk("panel 0 tip code pill uses bg-pink-200 border-pink-300", "bg-pink-200 text-pink-800 border border-pink-300" in kc)

# ── Panel 1 — violet ──────────────────────────────────────────────────────
chk("panel 1 has 'hidden' class", 'kc-panel kc-panel-anim hidden" data-color="violet"' in kc)
chk("panel 1 border-violet-100", "border border-violet-100" in kc)
chk("panel 1 violet gradient bar", "from-violet-500 via-purple-400 to-fuchsia-300" in kc)
chk("panel 1 definition mentions 'single Python file'", "single Python file that handles one specific task" in kc)
chk("panel 1 rules-table widget", "Module Naming Rules" in kc)
chk("panel 1 tip bg-violet-50", "bg-violet-50 border border-violet-100" in kc)
chk("panel 1 tip chip bg-violet-500", "bg-violet-500 shrink-0 mt-0.5" in kc)
chk("panel 1 tip code pill bg-violet-200", "bg-violet-200 text-violet-800 border border-violet-300" in kc)

# ── Panel 2 — blue ────────────────────────────────────────────────────────
chk("panel 2 has 'hidden' class", 'kc-panel kc-panel-anim hidden" data-color="blue"' in kc)
chk("panel 2 border-blue-100", "border border-blue-100" in kc)
chk("panel 2 blue gradient bar", "from-blue-500 via-cyan-400 to-teal-300" in kc)
chk("panel 2 definition mentions 'data folder'", "data folder keeps all your CSV" in kc)
chk("panel 2 comparison-table raw/ vs processed/", "raw/ vs processed/" in kc)
chk("panel 2 tip bg-blue-50", "bg-blue-50 border border-blue-100" in kc)
chk("panel 2 tip chip bg-blue-500", "bg-blue-500 shrink-0 mt-0.5" in kc)
chk("panel 2 tip code pill bg-blue-200", "bg-blue-200 text-blue-800 border border-blue-300" in kc)

# ── Panel 3 — emerald ─────────────────────────────────────────────────────
chk("panel 3 has 'hidden' class", 'kc-panel kc-panel-anim hidden" data-color="emerald"' in kc)
chk("panel 3 border-emerald-100", "border border-emerald-100" in kc)
chk("panel 3 emerald gradient bar", "from-emerald-500 via-teal-400 to-cyan-300" in kc)
chk("panel 3 definition mentions 'entry point'", "entry point is the single script you run" in kc)
chk("panel 3 comparison-table main.py vs modules/", "main.py vs modules/" in kc)
chk("panel 3 tip bg-emerald-50", "bg-emerald-50 border border-emerald-100" in kc)
chk("panel 3 tip chip bg-emerald-500", "bg-emerald-500 shrink-0 mt-0.5" in kc)

# ── Panels correct count ────────────────────────────────────────────────────
chk("exactly 4 kc-panel divs", kc.count('class="kc-panel') == 4)
chk("exactly 3 hidden panels", kc.count('kc-panel kc-panel-anim hidden"') == 3)

# ── No old content ──────────────────────────────────────────────────────────
chk("old 'Core terms and definitions' subtitle removed", "Core terms and definitions" not in kc)
chk("old simple panel body (no p-5 space-y-4) removed", 'class="bg-gradient-to-br from-pink-50/60 to-white p-5">' not in kc)
chk("no British spellings", "organised" not in kc and "colour" not in kc)

# ── CSS rules (full file scope) ─────────────────────────────────────────────
chk("CSS: .kc-tab-active { background: #fdf0f7; }", ".kc-tab-active { background: #fdf0f7; }" in html)
chk("CSS: .kc-tab:not(...):hover", ".kc-tab:not(.kc-tab-active):hover" in html)
chk("CSS: .kc-panel-anim animation", ".kc-panel-anim" in html and "kcFadeIn" in html)

# ── JS (full file scope) ────────────────────────────────────────────────────
chk("JS: kcColors array present", "const kcColors = [" in html)
chk("JS: switchKcTab function present", "function switchKcTab(idx)" in html)
chk("JS: Prism.highlightAllUnder in switchKcTab", "Prism.highlightAllUnder(visible)" in html)

# ── Summary ─────────────────────────────────────────────────────────────────
passed = sum(1 for s, _ in checks if s == "✅")
total  = len(checks)
print(f"\n{'='*59}")
print(f"  #key-concepts verify — {passed}/{total} checks passed")
print(f"{'='*59}")
for s, label in checks:
    print(f"  {s}  {label}")

if passed < total:
    print(f"\n❌  {total - passed} check(s) failed.")
else:
    print(f"\n🎉  All {total} checks passed.")
