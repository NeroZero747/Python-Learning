"""
Reformat #practice section in lesson06_shiny_for_python.html — format only.
Preserves all existing code blocks and amber tips verbatim.
Fixes:
  - Panel headers: remove "Exercise N — " prefix, add to title only
  - Task descriptions: replace <ol> bullet lists with 2-3 prose sentences
  - Badges: add domain and concept badges (Beginner was present, others missing)
  - Tab pill row: remove double-space class, remove flex-wrap
  - Accordion button: "Show Solution" → "Show Answer"
  - Code block header: remove traffic-light dots (none present, confirming OK)
  - Terminal panes: add to all 5 panels (currently absent)
"""
from pathlib import Path
import re

TARGET = Path(__file__).parent.parent / "pages/mod_05_data_application/lesson06_shiny_for_python.html"
html = TARGET.read_text(encoding="utf-8")
original_len = len(html)

# ─── Locate the practice section ─────────────────────────────────────────────
ps = html.find('\n<section id="practice">')
pe = html.find('\n<section id="mistakes">')
if ps == -1 or pe == -1:
    print("❌ Could not find #practice or #mistakes section markers")
    raise SystemExit(1)

practice_html = html[ps:pe]

# ─── Extract the 5 code blocks ────────────────────────────────────────────────
code_blocks = re.findall(
    r'<pre class="overflow-x-auto pre-reset"><code class="language-python">(.*?)</code></pre>',
    practice_html, re.DOTALL
)

# ─── Extract the 5 amber tips ─────────────────────────────────────────────────
# Each tip sits immediately after a code block inside a <div class="mt-3">
tips = re.findall(
    r'data-icon="fa6-solid:circle-info"></span>\s*<p class="text-sm text-gray-600">(.*?)</p>',
    practice_html, re.DOTALL
)
# Strip leading/trailing whitespace from each tip
tips = [t.strip() for t in tips]

if len(code_blocks) != 5:
    print(f"❌ Expected 5 code blocks, got {len(code_blocks)}")
    raise SystemExit(1)
if len(tips) != 5:
    print(f"❌ Expected 5 tips, got {len(tips)}")
    raise SystemExit(1)

print(f"✅ Extracted {len(code_blocks)} code blocks")
print(f"✅ Extracted {len(tips)} amber tips")

# ─── Exercise metadata ────────────────────────────────────────────────────────
exercises = [
    {
        "tab": "Build a Minimal App",
        "title": "Build a Minimal App",
        "watermark": "01",
        "difficulty": "beginner",
        "domain": "Web Apps",
        "concepts": ["App()", "@render.text"],
        "task": (
            "You are building your first Shiny app from scratch. "
            "Create a UI with a number slider (id <code>&quot;n&quot;</code>, range 1–50) "
            "and a text output placeholder called <code>&quot;greeting&quot;</code>. "
            "Write a server function with a <code>@render.text</code> function also named <code>greeting</code> "
            "that reads the slider value and returns a message — "
            "the text should update automatically each time you move the slider."
        ),
        "filename": "app.py",
        "cmd": "$ shiny run app.py",
        "output": "Listening on http://127.0.0.1:8000",
    },
    {
        "tab": "Add a Reactive Filter",
        "title": "Add a Reactive Filter",
        "watermark": "02",
        "difficulty": "beginner",
        "domain": "HR",
        "concepts": ["@reactive.calc", "@render.table"],
        "task": (
            "You have a small employee DataFrame with name, department, and salary columns. "
            "Add a department dropdown to the sidebar and write a <code>@reactive.calc</code> "
            "function called <code>filtered</code> that returns only the rows matching the selected department. "
            "Connect two outputs to the cached result: a table displaying the filtered employees "
            "and a text line showing how many rows were returned."
        ),
        "filename": "solution_2.py",
        "cmd": "$ shiny run solution_2.py",
        "output": "Listening on http://127.0.0.1:8000",
    },
    {
        "tab": "Render a Chart",
        "title": "Render a Matplotlib Chart",
        "watermark": "03",
        "difficulty": "beginner",
        "domain": "HR",
        "concepts": ["@render.plot", "matplotlib"],
        "task": (
            "Extend the employee dashboard by adding a salary bar chart. "
            "Add a <code>ui.output_plot(&quot;chart&quot;)</code> placeholder to the UI and write a "
            "<code>@render.plot</code> function named <code>chart</code> that creates a matplotlib bar chart "
            "with employee names on the x-axis and salaries on the y-axis. "
            "End the function with <code>return fig</code> instead of <code>plt.show()</code> — "
            "Shiny needs the Figure object to display the chart in the browser."
        ),
        "filename": "solution_3.py",
        "cmd": "$ shiny run solution_3.py",
        "output": "Listening on http://127.0.0.1:8000",
    },
    {
        "tab": "Create a Tabbed Layout",
        "title": "Create a Tabbed Layout",
        "watermark": "04",
        "difficulty": "beginner",
        "domain": "HR",
        "concepts": ["page_navbar", "nav_panel"],
        "task": (
            "Reorganize the employee dashboard into a two-tab layout. "
            "Replace <code>ui.page_sidebar()</code> with <code>ui.page_navbar()</code> and add two "
            "<code>ui.nav_panel()</code> tabs: a &ldquo;Chart&rdquo; tab containing the sidebar and plot, "
            "and a &ldquo;Data&rdquo; tab containing only the table. "
            "Set the <code>title=</code> argument to <code>&quot;Employee Dashboard&quot;</code> "
            "so the app name appears in the top navigation bar."
        ),
        "filename": "solution_4.py",
        "cmd": "$ shiny run solution_4.py",
        "output": "Listening on http://127.0.0.1:8000",
    },
    {
        "tab": "Add Dynamic UI",
        "title": "Add Dynamic UI",
        "watermark": "05",
        "difficulty": "intermediate",
        "domain": "HR",
        "concepts": ["@render.ui", "output_ui"],
        "task": (
            "Different departments track different metrics, so the second dropdown should change "
            "when the first one changes. "
            "Add a <code>ui.output_ui(&quot;dynamic_widget&quot;)</code> placeholder to the sidebar and write a "
            "<code>@render.ui</code> function that returns a dropdown with context-specific choices: "
            "Sales shows Revenue and Deals, Engineering shows Commits and PRs, and HR shows Headcount and Turnover. "
            "Add a <code>@render.text</code> output that confirms which department and metric are currently selected."
        ),
        "filename": "solution_5.py",
        "cmd": "$ shiny run solution_5.py",
        "output": "Listening on http://127.0.0.1:8000",
    },
]


# ─── HTML builders ────────────────────────────────────────────────────────────
def build_badges(ex):
    parts = []
    if ex["difficulty"] == "beginner":
        parts.append(
            '<span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full '
            'bg-emerald-50 text-emerald-600 border border-emerald-200">'
            '<span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner</span>'
        )
    else:
        parts.append(
            '<span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full '
            'bg-amber-50 text-amber-600 border border-amber-200">'
            '<span class="iconify text-[10px]" data-icon="fa6-solid:fire"></span> Intermediate</span>'
        )
    parts.append(
        f'<span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full '
        f'bg-gray-100 text-gray-500 font-medium">{ex["domain"]}</span>'
    )
    for concept in ex["concepts"]:
        parts.append(
            f'<span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full '
            f'bg-gray-100 text-gray-500 font-medium">{concept}</span>'
        )
    return "\n                  ".join(parts)


def build_panel(ex, code, tip, hidden=False):
    hidden_cls = " hidden" if hidden else ""
    badges = build_badges(ex)
    return (
        f'      <div class="pe-panel pe-panel-anim{hidden_cls}" role="tabpanel">\n'
        f'        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">\n'
        f'          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">\n'
        f'            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{ex["watermark"]}</span>\n'
        f'            <div class="relative flex items-center gap-3">\n'
        f'              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">\n'
        f'                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>\n'
        f'              </span>\n'
        f'              <div>\n'
        f'                <h3 class="font-bold text-gray-800">{ex["title"]}</h3>\n'
        f'                <div class="flex items-center gap-2 mt-1">\n'
        f'                  {badges}\n'
        f'                </div>\n'
        f'              </div>\n'
        f'            </div>\n'
        f'          </div>\n'
        f'          <div class="px-6 py-5 space-y-4">\n'
        f'            <div class="flex items-start gap-3 rounded-xl p-4 task-box">\n'
        f'              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>\n'
        f'              <div>\n'
        f'                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>\n'
        f'                <p class="text-sm text-gray-600">{ex["task"]}</p>\n'
        f'              </div>\n'
        f'            </div>\n'
        f'            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">\n'
        f'              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer\n'
        f'              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>\n'
        f'            </button>\n'
        f'            <div class="accordion-body">\n'
        f'              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">\n'
        f'                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">\n'
        f'                  <div class="flex items-center gap-3">\n'
        f'                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">\n'
        f'                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>\n'
        f'                      <span class="text-[11px] font-semibold text-gray-400">{ex["filename"]}</span>\n'
        f'                    </div>\n'
        f'                  </div>\n'
        f'                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>\n'
        f'                </div>\n'
        f'                <div class="bg-code">\n'
        f'                  <pre class="overflow-x-auto pre-reset"><code class="language-python">{code}</code></pre>\n'
        f'                </div>\n'
        f'                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">\n'
        f'                  <div class="flex items-center gap-2 mb-1.5">\n'
        f'                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>\n'
        f'                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>\n'
        f'                    <span class="text-[10px] text-gray-600 font-mono">{ex["cmd"]}</span>\n'
        f'                  </div>\n'
        f'                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">{ex["output"]}</div>\n'
        f'                </div>\n'
        f'              </div>\n'
        f'              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">\n'
        f'                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>\n'
        f'                <p class="text-sm text-gray-600">{tip}</p>\n'
        f'              </div>\n'
        f'            </div>\n'
        f'          </div>\n'
        f'        </div>\n'
        f'      </div>'
    )


def build_tab_row(exs):
    pills = []
    for i, ex in enumerate(exs):
        if i == 0:
            pills.append(
                f'        <button onclick="switchPeTab(0)" class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">\n'
                f'          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>\n'
                f'          <span class="pe-step-label text-xs font-bold">{ex["tab"]}</span>\n'
                f'        </button>'
            )
        else:
            pills.append(
                f'        <button onclick="switchPeTab({i})" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">\n'
                f'          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>\n'
                f'          <span class="pe-step-label text-xs font-bold">{ex["tab"]}</span>\n'
                f'        </button>'
            )
    return (
        '      <div class="flex items-center gap-2 mb-6" role="tablist">\n'
        + '\n'.join(pills)
        + '\n      </div>'
    )


# ─── Assemble new section body ────────────────────────────────────────────────
panels_html = [
    build_panel(exercises[i], code_blocks[i], tips[i], hidden=(i > 0))
    for i in range(5)
]

new_body = (
    '    <div class="bg-white px-8 py-7 space-y-6">\n'
    + build_tab_row(exercises) + '\n'
    + '\n'.join(panels_html) + '\n'
    + '    </div>\n'
    + '  </div>\n'
    + '</section>'
)

# ─── Locate old body in file and replace ──────────────────────────────────────
# Find where the body div starts (after the section header) in the practice section
body_start_marker = '    <div class="bg-white px-8 py-7 space-y-6">'
body_start_pos = html.find(body_start_marker, ps)
if body_start_pos == -1 or body_start_pos > pe:
    print("❌ Could not find body div start in practice section")
    raise SystemExit(1)

# The practice section ends at pe (the \n before <section id="mistakes">)
html = html[:body_start_pos] + new_body + html[pe:]

TARGET.write_text(html, encoding="utf-8")
print(f"\n✅ Done. File: {original_len} → {len(html)} chars ({len(html) - original_len:+d})")
