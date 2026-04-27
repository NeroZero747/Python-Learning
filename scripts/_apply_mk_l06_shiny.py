"""
Reformat #mistakes section in lesson06_shiny_for_python.html — formatting only.
Preserves all existing: tab labels, titles, subtitles, code blocks, tip texts.
Fixes:
  - Tab pill row: remove flex-wrap, fix double-space on inactive classes
  - Card headers: add "Pitfall" badge
  - Add explanation paragraph (derived from subtitle, no new content)
  - Split panels: convert to canonical format (bg-red-50/30, bg-emerald-50/30, arrow divider, labelled panels)
"""
from pathlib import Path

TARGET = Path(__file__).parent.parent / "pages/mod_05_data_application/lesson06_shiny_for_python.html"
html = TARGET.read_text(encoding="utf-8")
original_len = len(html)

# ─── Section boundaries ────────────────────────────────────────────────────────
ms = html.find('\n<section id="mistakes">')
me = html.find('\n<section id="recap">')
if ms == -1 or me == -1:
    print("❌ Could not find section boundaries"); raise SystemExit(1)

# ─── Extracted code blocks (5 wrong, 5 correct) ────────────────────────────────
# These are copied verbatim from the existing file.

wrong = [
    # 1
    """# input.n without parentheses returns the reactive object
@render.text
def result():
    return f&quot;Value: {input.n}&quot;   # BUG: prints &lt;reactive object&gt;""",

    # 2
    """# UI says &quot;result&quot; but server function is named &quot;output_text&quot;
app_ui = ui.page_sidebar(
    ui.card(ui.output_text(&quot;result&quot;)),   # id = &quot;result&quot;
)

def server(input, output, session):
    @render.text
    def output_text():           # BUG: name is &quot;output_text&quot;, not &quot;result&quot;
        return &quot;Hello&quot;           # nothing appears in the UI""",

    # 3
    """@render.plot
def chart():
    fig, ax = plt.subplots()
    ax.bar([&quot;A&quot;, &quot;B&quot;], [10, 20])
    plt.show()   # BUG: shows nothing in Shiny
    # no return statement""",

    # 4
    """# Data loaded once at import time — never refreshes
df = pd.read_csv(&quot;sales.csv&quot;)

def server(input, output, session):
    @render.table
    def tbl():
        return df[df[&quot;region&quot;] == input.region()]  # stale data""",

    # 5
    """def server(input, output, session):
    # Missing @render.text decorator
    def result():
        return f&quot;Total: {input.n()}&quot;
    # Shiny never calls this function — output stays blank""",
]

correct = [
    # 1
    """# input.n() with parentheses returns the actual value
@render.text
def result():
    return f&quot;Value: {input.n()}&quot;  # Correct: returns the number""",

    # 2
    """# Server function name matches the UI output id exactly
app_ui = ui.page_sidebar(
    ui.card(ui.output_text(&quot;result&quot;)),   # id = &quot;result&quot;
)

def server(input, output, session):
    @render.text
    def result():                # Correct: matches &quot;result&quot; in UI
        return &quot;Hello&quot;           # text appears in the card""",

    # 3
    """@render.plot
def chart():
    fig, ax = plt.subplots()
    ax.bar([&quot;A&quot;, &quot;B&quot;], [10, 20])
    return fig   # Correct: Shiny embeds the Figure object""",

    # 4
    """def server(input, output, session):
    @reactive.calc
    def data():
        return pd.read_csv(&quot;sales.csv&quot;)  # re-reads when invalidated

    @render.table
    def tbl():
        return data()[data()[&quot;region&quot;] == input.region()]""",

    # 5
    """def server(input, output, session):
    @render.text              # decorator tells Shiny this is an output
    def result():
        return f&quot;Total: {input.n()}&quot;
    # Shiny calls result() whenever input.n() changes""",
]

tips = [
    # 1
    'Always call input values with parentheses — <code>input.n()</code> not <code>input.n</code>. The parentheses trigger the reactive read and return the current value.',
    # 2
    'The server function name must exactly match the <code>id</code> string you passed to the output placeholder in the UI. If nothing renders, check for typos in both places.',
    # 3
    'Replace <code>plt.show()</code> with <code>return fig</code> at the end of every <code>@render.plot</code> function. Shiny needs the Figure object to convert it into an image for the browser.',
    # 4
    'Wrap data loading inside a <code>@reactive.calc</code> if the data can change, or keep it at module level only for truly static lookup tables. For most dashboards, loading inside a reactive expression is safer.',
    # 5
    'Every output function needs a <code>@render.*</code> decorator. Without it, Shiny treats the function as a regular helper and never connects it to the UI placeholder.',
]

mistakes = [
    {
        "tab": "Forgetting Parentheses on Input Reads",
        "title": "Forgetting Parentheses on Input Reads",
        "subtitle": "Beginners treat <code class=\"font-mono bg-gray-100 px-1 rounded text-[11px]\">input.n</code> as a regular variable instead of a reactive signal that must be called.",
        "explanation": "Writing <code class=\"font-mono bg-gray-100 px-1 rounded text-[11px]\">input.n</code> without parentheses returns the reactive signal object, not the value — the output displays something like <code class=\"font-mono bg-gray-100 px-1 rounded text-[11px]\">&lt;reactive.Value object&gt;</code> instead of a number. Add parentheses: <code class=\"font-mono bg-gray-100 px-1 rounded text-[11px]\">input.n()</code> reads and returns the current value.",
        "wrong_label": "no parentheses",
        "correct_label": "with parentheses",
    },
    {
        "tab": "Output Name Mismatch",
        "title": "Output Name Mismatch Between UI and Server",
        "subtitle": "The output id in the UI does not match the function name in the server, so Shiny silently ignores the function.",
        "explanation": "Shiny connects a server function to a UI placeholder by matching the function name to the output id string — if they differ, the placeholder stays blank with no error message. Make sure the function name inside <code class=\"font-mono bg-gray-100 px-1 rounded text-[11px]\">server()</code> is identical to the id you passed to the output widget.",
        "wrong_label": "mismatched names",
        "correct_label": "matching names",
    },
    {
        "tab": "plt.show() in a Render Function",
        "title": "Calling plt.show() Instead of Returning the Figure",
        "subtitle": "In Jupyter notebooks, <code class=\"font-mono bg-gray-100 px-1 rounded text-[11px]\">plt.show()</code> displays the chart — but inside Shiny, there is no interactive matplotlib window.",
        "explanation": "Calling <code class=\"font-mono bg-gray-100 px-1 rounded text-[11px]\">plt.show()</code> in a <code class=\"font-mono bg-gray-100 px-1 rounded text-[11px]\">@render.plot</code> function tries to open a desktop window, which fails silently in a web app. End the function with <code class=\"font-mono bg-gray-100 px-1 rounded text-[11px]\">return fig</code> so Shiny can convert the Figure object into a browser image.",
        "wrong_label": "plt.show() called",
        "correct_label": "return fig",
    },
    {
        "tab": "Computation Outside Reactive Context",
        "title": "Expensive Computation Outside a Reactive Context",
        "subtitle": "Placing <code class=\"font-mono bg-gray-100 px-1 rounded text-[11px]\">pd.read_csv()</code> or a database query at the module level means it runs once at startup and never updates when inputs change.",
        "explanation": "Code at the module level runs once when the app starts — it is not part of the reactive graph and will not re-run when a user changes an input. Wrap data loading in a <code class=\"font-mono bg-gray-100 px-1 rounded text-[11px]\">@reactive.calc</code> function so Shiny re-runs it whenever its dependencies change.",
        "wrong_label": "module-level load",
        "correct_label": "inside @reactive.calc",
    },
    {
        "tab": "Missing @render Decorator",
        "title": "Forgetting the @render Decorator",
        "subtitle": "The function looks correct but Shiny never registers it as an output because the decorator is missing.",
        "explanation": "Without a <code class=\"font-mono bg-gray-100 px-1 rounded text-[11px]\">@render.*</code> decorator, the function is a plain Python function — Shiny does not know it should be treated as an output. Add the matching decorator (<code class=\"font-mono bg-gray-100 px-1 rounded text-[11px]\">@render.text</code>, <code class=\"font-mono bg-gray-100 px-1 rounded text-[11px]\">@render.plot</code>, etc.) on the line immediately above the function definition.",
        "wrong_label": "decorator missing",
        "correct_label": "decorator added",
    },
]


# ─── HTML builders ─────────────────────────────────────────────────────────────

def build_tab_row(ms_list):
    pills = []
    for i, m in enumerate(ms_list):
        if i == 0:
            pills.append(
                f'        <button onclick="switchMkTab(0)" class="mk-step mk-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">\n'
                f'          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>\n'
                f'          <span class="mk-step-label text-xs font-bold">{m["tab"]}</span>\n'
                f'        </button>'
            )
        else:
            pills.append(
                f'        <button onclick="switchMkTab({i})" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">\n'
                f'          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>\n'
                f'          <span class="mk-step-label text-xs font-bold">{m["tab"]}</span>\n'
                f'        </button>'
            )
    return (
        '      <div class="flex items-center gap-2 mb-6" role="tablist">\n'
        + '\n'.join(pills) + '\n'
        + '      </div>'
    )


def build_panel(m, wcode, ccode, tip, hidden=False):
    hidden_cls = " hidden" if hidden else ""
    return f"""\
      <div class="mk-panel mk-panel-anim{hidden_cls}" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">{m["title"]}</h4>
              <p class="text-xs text-gray-500 mt-0.5">{m["subtitle"]}</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">{m["explanation"]}</p>
          </div>

          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong &mdash; {m["wrong_label"]}
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">{wcode}</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct &mdash; {m["correct_label"]}
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">{ccode}</code></pre>
              </div>
            </div>
          </div>

          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">{tip}</p>
          </div>

        </div>
      </div>"""


# ─── Build full new section ────────────────────────────────────────────────────
panels = [
    build_panel(mistakes[i], wrong[i], correct[i], tips[i], hidden=(i > 0))
    for i in range(5)
]

new_section = """\n<section id="mistakes">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:triangle-exclamation"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Common Mistakes</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Pitfalls beginners hit when working with Shiny for Python</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
""" + build_tab_row(mistakes) + "\n" + "\n".join(panels) + """
    </div>
  </div>
</section>"""

# ─── Splice into file ──────────────────────────────────────────────────────────
html = html[:ms] + new_section + html[me:]
TARGET.write_text(html, encoding="utf-8")
print(f"✅ Done. File: {original_len} → {len(html)} chars ({len(html) - original_len:+d})")
