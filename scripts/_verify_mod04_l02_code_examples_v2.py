"""Verify KC __init__.py tab + new Code Examples section in lesson02."""

from pathlib import Path

TARGET = Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices"
    "/lesson02_project_folder_structure.html"
)

html = TARGET.read_text(encoding="utf-8")

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

# ── Isolate Key Concepts section ──────────────────────────────────
kc_start = html.rindex("<section", 0, html.index('id="key-concepts"'))
kc_end   = html.index("</section>", kc_start) + len("</section>")
kc       = html[kc_start:kc_end]

# ── Isolate Code Examples section ─────────────────────────────────
ce_start = html.rindex("<section", 0, html.index('id="code-examples"'))
ce_end   = html.index("</section>", ce_start) + len("</section>")
ce       = html[ce_start:ce_end]

print("\n── Key Concepts: __init__.py tab ───────────────────────────")
check("5 kc-tab buttons total",              kc.count("switchKcTab(") == 5)
check("5th tab: switchKcTab(4)",             "switchKcTab(4)" in kc)
check("5th tab label: __init__.py",          ">__init__.py<" in kc)
check("5 kc-panel divs",                     kc.count("kc-panel kc-panel-anim") == 5)
check("Panel 4 is hidden",                   'data-color="amber"' in kc)
check("__init__.py concept explained",       "ModuleNotFoundError" in kc)
check("With/Without comparison present",     "Without __init__.py" in kc and "With __init__.py" in kc)
check("open __init__.py creation line",      'open("modules/__init__.py", "w").close()' in kc)
check("Namespace packages tip present",      "namespace packages" in kc)

print("\n── Code Examples: structure ────────────────────────────────")
check("Exactly 3 ce-step buttons",           ce.count('class="ce-step ') == 3)
check("Panel 1 visible",                     'ce-panel ce-panel-anim"' in ce or 'ce-panel ce-panel-anim ' in ce)
check("Panels 2 & 3 hidden (×2)",            ce.count("ce-panel ce-panel-anim hidden") == 2)
check("Intro connector callout present",     "These three examples form one project" in ce)

print("\n── Code Examples: tab labels ───────────────────────────────")
check("Tab 1: 'Set Up the Project'",         "1 · Set Up the Project" in ce)
check("Tab 2: 'Write the Module'",           "2 · Write the Module" in ce)
check("Tab 3: 'Run the Pipeline'",           "3 · Run the Pipeline" in ce)
check("No generic 'Example 1/2/3/4'",        "Example 1" not in ce and "Example 4" not in ce)

print("\n── Code Examples: watermarks ───────────────────────────────")
check("Watermark 01", ">01<" in ce)
check("Watermark 02", ">02<" in ce)
check("Watermark 03", ">03<" in ce)
check("No watermark 04", ">04<" not in ce)

print("\n── Code Examples: no forbidden patterns ────────────────────")
check("No traffic-light dots (bg-red-400)",    "bg-red-400"    not in ce)
check("No traffic-light dots (bg-yellow-400)", "bg-yellow-400" not in ce)
check("No traffic-light dots (bg-green-400)",  "bg-green-400"  not in ce)

print("\n── Code Examples: code content ─────────────────────────────")
check("Panel 1: os.makedirs",                "os.makedirs" in ce)
check("Panel 1: __init__.py creation",       'open("modules/__init__.py", "w").close()' in ce)
check("Panel 1: exist_ok=True",              "exist_ok=True" in ce)
check("Panel 1: output: Folders created",    "Folders created!" in ce)
check("Panel 2: def remove_blanks",          "def remove_blanks" in ce)
check("Panel 2: no if __name__ guard",       '__name__ == "__main__"' not in ce)
check("Panel 2: no callout box",             "bg-violet-50" not in ce)
check("Panel 3: remove_blanks import",       "from modules.cleaning import remove_blanks" in ce)
check("Panel 3: output: Clean list",         "Clean list:" in ce)
check("Panel 3: no SALES REPORT",           "SALES REPORT" not in ce)

print("\n── Code Examples: filenames ────────────────────────────────")
check("setup_project.py",    "setup_project.py" in ce)
check("modules/cleaning.py", "modules/cleaning.py" in ce)
check("main.py filename",    ">main.py<" in ce)

print("\n── Code Examples: components ───────────────────────────────")
check("3 task-box divs",                     ce.count("task-box") == 3)
check("3 terminal panes (bg-[#11111b])",     ce.count("bg-[#11111b]") == 3)
check("3 amber tip boxes",                   ce.count("bg-amber-tip") == 3)
check("3 copy buttons",                      ce.count("copyCode(this)") == 3)
check("3 'What This Does' labels",           ce.count(">What This Does<") == 3)

print(f"\n{'='*52}")
print(f"  TOTAL: {pass_count} passed, {fail_count} failed  ({pass_count}/{pass_count + fail_count})")
print(f"{'='*52}\n")
