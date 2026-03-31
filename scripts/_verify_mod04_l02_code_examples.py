"""Verify the #code-examples section in lesson02_project_folder_structure.html."""

from pathlib import Path

TARGET = Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices"
    "/lesson02_project_folder_structure.html"
)

html = TARGET.read_text(encoding="utf-8")

# --- isolate the section ---
ce_start = html.index('id="code-examples"')
ce_start = html.rindex("<section", 0, ce_start)
ce_end   = html.index("</section>", ce_start) + len("</section>")
sec      = html[ce_start:ce_end]

pass_count = 0
fail_count = 0

def check(label, condition):
    global pass_count, fail_count
    if condition:
        print(f"  ✅  {label}")
        pass_count += 1
    else:
        print(f"  ❌  FAIL — {label}")
        fail_count += 1

print("\n── Structure ───────────────────────────────────────────")
check("Exactly 3 ce-step buttons", sec.count('class="ce-step ') == 3)
check("Exactly 3 ce-panel divs",   sec.count('class="ce-panel ') + sec.count("ce-step-active") >= 1)
check("Panel 1 visible (no hidden on first)",             'ce-panel ce-panel-anim"' in sec or 'ce-panel ce-panel-anim ' in sec)
check("Panels 2 & 3 have hidden class (×2)",             sec.count('ce-panel ce-panel-anim hidden') == 2)

print("\n── Tab labels ──────────────────────────────────────────")
check("Tab 1: 'Create Project Folders'", "Create Project Folders" in sec)
check("Tab 2: 'Write a Module'",         "Write a Module" in sec)
check("Tab 3: 'Connect with main.py'",   "Connect with main.py" in sec)
check("No generic 'Example 1/2/3/4'",   "Example 1" not in sec and "Example 2" not in sec)

print("\n── Watermarks ──────────────────────────────────────────")
check("Watermark 01 present", ">01<" in sec)
check("Watermark 02 present", ">02<" in sec)
check("Watermark 03 present", ">03<" in sec)
check("No watermark 04",      ">04<" not in sec)

print("\n── No forbidden patterns ───────────────────────────────")
check("No traffic-light dots (bg-red-400)",    "bg-red-400"    not in sec)
check("No traffic-light dots (bg-yellow-400)", "bg-yellow-400" not in sec)
check("No traffic-light dots (bg-green-400)",  "bg-green-400"  not in sec)

print("\n── Code content ────────────────────────────────────────")
check("os.makedirs in panel 1",      "os.makedirs" in sec)
check("os.listdir in panel 1",       "os.listdir"  in sec)
check("exist_ok=True in panel 1",    "exist_ok=True" in sec)
check("def remove_blanks in panel 2","remove_blanks" in sec)
check("modules.cleaning import in panel 3", "modules.cleaning import remove_blanks" in sec)
check("Filenames: setup_project.py", "setup_project.py" in sec)
check("Filenames: modules/cleaning.py", "modules/cleaning.py" in sec)
check("Filenames: main.py",          ">main.py<" in sec or "main.py\"" in sec)

print("\n── Components ──────────────────────────────────────────")
check("3 task-box divs",             sec.count("task-box") == 3)
check("3 terminal panes (bg-[#11111b])", sec.count("bg-[#11111b]") == 3)
check("3 amber tip boxes",           sec.count("bg-amber-tip") == 3)
check("3 copy buttons",              sec.count("copyCode(this)") == 3)
check("3 'What This Does' labels",   sec.count("What This Does") == 3)

print("\n── Domain pills ────────────────────────────────────────")
check("Reports pill (panel 1)", "Reports" in sec)
check("Sales pill (panel 2)",   "Sales"   in sec)
check("Products pill (panel 3)","Products" in sec)

print("\n── Beginner badges ─────────────────────────────────────")
check("3 Beginner badges", sec.count("Beginner") == 3)

print(f"\n{'='*52}")
print(f"  TOTAL: {pass_count} passed, {fail_count} failed  ({pass_count}/{pass_count + fail_count})")
print(f"{'='*52}\n")
