"""
Rewrite <section id="key-concepts"> for all 10 lessons in
track_02 / mod_01_data_analysis_with_pandas.

Uses the prompt spec from lesson-key-concepts.prompt.md.
Lesson 01 is already gold-standard; the script replaces it identically
so all 10 files stay consistent.
"""

import re, pathlib, html

BASE = pathlib.Path(__file__).resolve().parent.parent
MOD = BASE / "pages" / "track_02_data_analytics" / "mod_01_data_analysis_with_pandas"

SECTION_RE = re.compile(
    r'(<section id="key-concepts"[^>]*>).*?(</section>)',
    re.DOTALL,
)

# ── Color palette (sequential: pink, violet, blue, emerald, amber) ────

COLORS = {
    "pink": {
        "border": "border-pink-100",
        "topbar": "from-[#CB187D] via-pink-400 to-rose-300",
        "panelbg": "from-pink-50/60 to-white",
        "badge": "from-pink-100 to-rose-100 text-[#CB187D] border-pink-200",
        "tipbg": "bg-pink-50 border border-pink-100",
        "tipchip": "bg-[#CB187D]",
        "headchip": "from-[#CB187D] to-[#e84aad]",
        # widget header
        "wh_from": "from-pink-50", "wh_to": "to-rose-50", "wh_border": "border-pink-100", "wh_text": "text-pink-500",
        # code pills in definition/widget
        "code_bg": "bg-pink-100", "code_text": "text-pink-700", "code_border": "border-pink-200",
        # code pills in tips (-200 bg, -300 border, -800 text)
        "tip_code_bg": "bg-pink-200", "tip_code_text": "text-pink-800", "tip_code_border": "border-pink-300",
        # comparison table header pill colors
        "cola_bg": "bg-pink-100", "cola_text": "text-pink-700", "cola_border": "border-pink-200",
    },
    "violet": {
        "border": "border-violet-100",
        "topbar": "from-violet-500 via-purple-400 to-fuchsia-300",
        "panelbg": "from-violet-50/60 to-white",
        "badge": "from-violet-100 to-purple-100 text-violet-600 border-violet-200",
        "tipbg": "bg-violet-50 border border-violet-100",
        "tipchip": "bg-violet-500",
        "headchip": "from-violet-500 to-purple-600",
        "wh_from": "from-violet-50", "wh_to": "to-purple-50", "wh_border": "border-violet-100", "wh_text": "text-violet-500",
        "code_bg": "bg-violet-100", "code_text": "text-violet-700", "code_border": "border-violet-200",
        "tip_code_bg": "bg-violet-200", "tip_code_text": "text-violet-800", "tip_code_border": "border-violet-300",
        "cola_bg": "bg-violet-100", "cola_text": "text-violet-700", "cola_border": "border-violet-200",
    },
    "blue": {
        "border": "border-blue-100",
        "topbar": "from-blue-500 via-cyan-400 to-teal-300",
        "panelbg": "from-blue-50/60 to-white",
        "badge": "from-blue-100 to-indigo-100 text-blue-600 border-blue-200",
        "tipbg": "bg-blue-50 border border-blue-100",
        "tipchip": "bg-blue-500",
        "headchip": "from-blue-500 to-indigo-600",
        "wh_from": "from-blue-50", "wh_to": "to-indigo-50", "wh_border": "border-blue-100", "wh_text": "text-blue-500",
        "code_bg": "bg-blue-100", "code_text": "text-blue-700", "code_border": "border-blue-200",
        "tip_code_bg": "bg-blue-200", "tip_code_text": "text-blue-800", "tip_code_border": "border-blue-300",
        "cola_bg": "bg-blue-100", "cola_text": "text-blue-700", "cola_border": "border-blue-200",
    },
    "emerald": {
        "border": "border-emerald-100",
        "topbar": "from-emerald-500 via-teal-400 to-cyan-300",
        "panelbg": "from-emerald-50/60 to-white",
        "badge": "from-emerald-100 to-teal-100 text-emerald-600 border-emerald-200",
        "tipbg": "bg-emerald-50 border border-emerald-100",
        "tipchip": "bg-emerald-500",
        "headchip": "from-emerald-500 to-teal-600",
        "wh_from": "from-emerald-50", "wh_to": "to-teal-50", "wh_border": "border-emerald-100", "wh_text": "text-emerald-500",
        "code_bg": "bg-emerald-100", "code_text": "text-emerald-700", "code_border": "border-emerald-200",
        "tip_code_bg": "bg-emerald-200", "tip_code_text": "text-emerald-800", "tip_code_border": "border-emerald-300",
        "cola_bg": "bg-emerald-100", "cola_text": "text-emerald-700", "cola_border": "border-emerald-200",
    },
    "amber": {
        "border": "border-amber-100",
        "topbar": "from-amber-500 via-orange-400 to-red-300",
        "panelbg": "from-amber-50/60 to-white",
        "badge": "from-amber-100 to-orange-100 text-amber-600 border-amber-200",
        "tipbg": "bg-amber-50 border border-amber-100",
        "tipchip": "bg-amber-500",
        "headchip": "from-amber-500 to-orange-500",
        "wh_from": "from-amber-50", "wh_to": "to-orange-50", "wh_border": "border-amber-100", "wh_text": "text-amber-500",
        "code_bg": "bg-amber-100", "code_text": "text-amber-700", "code_border": "border-amber-200",
        "tip_code_bg": "bg-amber-200", "tip_code_text": "text-amber-800", "tip_code_border": "border-amber-300",
        "cola_bg": "bg-amber-100", "cola_text": "text-amber-700", "cola_border": "border-amber-200",
    },
}

COLOR_ORDER = ["pink", "violet", "blue", "emerald", "amber"]


# ── HTML builders ──────────────────────────────────────────────────────

def _c(idx):
    """Return color dict for tab index."""
    return COLORS[COLOR_ORDER[idx % len(COLOR_ORDER)]]


def build_sidebar(tabs: list[dict]) -> str:
    """Build the sidebar with tab buttons."""
    lines = []
    lines.append('        <!-- ── Sidebar ── -->')
    lines.append('        <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">')
    lines.append('')
    lines.append('          <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full transition-all duration-300" style="height:68px;background:#CB187D;"></div>')
    lines.append('')

    for i, tab in enumerate(tabs):
        if i == 0:
            lines.append(f'          <!-- Tab {i} — ACTIVE -->')
            lines.append(f'          <button onclick="switchKcTab({i})" class="kc-tab kc-tab-active group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">')
            lines.append(f'            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#CB187D;color:#fff;box-shadow:0 2px 8px rgba(203,24,125,0.25)"><span class="iconify text-[11px]" data-icon="{tab["icon"]}"></span></span>')
            lines.append(f'            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-900">{tab["label"]}</span>')
            lines.append('          </button>')
        else:
            lines.append(f'')
            lines.append(f'          <!-- Tab {i} — INACTIVE -->')
            lines.append(f'          <button onclick="switchKcTab({i})" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">')
            lines.append(f'            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="{tab["icon"]}"></span></span>')
            lines.append(f'            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">{tab["label"]}</span>')
            lines.append('          </button>')

    lines.append('')
    lines.append('        </div><!-- /sidebar -->')
    return "\n".join(lines)


def build_code_block(code: str, lang: str = "python") -> str:
    icon = 'logos:python' if lang == "python" else 'fa6-solid:terminal'
    label = "Python" if lang == "python" else "Bash"
    icon_class = '' if lang == "python" else ' text-gray-400'
    return f'''                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify{icon_class}" data-icon="{icon}" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">{label}</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-{lang}">{code}</code></pre>
                </div>'''


def build_tip(idx: int, icon: str, text: str) -> str:
    c = _c(idx)
    return f'''                <div class="rounded-xl p-3 flex items-start gap-2.5 {c["tipbg"]}">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg {c["tipchip"]} shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="{icon}"></span>
                  </span>
                  <p class="text-xs text-gray-600">{text}</p>
                </div>'''


def build_header_row(idx: int, tab: dict) -> str:
    c = _c(idx)
    return f'''                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br {c["headchip"]} shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="{tab["icon"]}"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">{tab["label"]}</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">{tab["header_subtitle"]}</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r {c["badge"]} shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> {tab["badge_label"]}
                  </span>
                </div>'''


def build_rules_table(idx: int, title: str, icon: str, rows: list[tuple]) -> str:
    """rows: list of (rule_text, result_html)"""
    c = _c(idx)
    lines = []
    lines.append(f'                <div class="rounded-xl overflow-hidden border {c["border"]}">')
    lines.append(f'                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r {c["wh_from"]} {c["wh_to"]} border-b {c["wh_border"]}">')
    lines.append(f'                    <span class="iconify {c["wh_text"]} text-xs" data-icon="{icon}"></span>')
    lines.append(f'                    <p class="text-[10px] font-bold uppercase tracking-widest {c["wh_text"]}">{title}</p>')
    lines.append('                  </div>')
    lines.append('                  <table class="w-full text-xs border-collapse bg-white">')
    lines.append('                    <tbody>')
    for ri, (rule, result) in enumerate(rows):
        shade = ' bg-gray-50/50' if ri % 2 == 1 else ''
        border = ' border-b border-gray-50' if ri < len(rows) - 1 else ''
        lines.append(f'                      <tr class="{border}{shade}">')
        lines.append(f'                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2">{rule}</td>')
        lines.append(f'                        <td class="py-2 px-3 text-gray-500">{result}</td>')
        lines.append('                      </tr>')
    lines.append('                    </tbody>')
    lines.append('                  </table>')
    lines.append('                </div>')
    return "\n".join(lines)


def build_comparison_table(idx: int, title: str, col_a: dict, col_b: dict, rows: list[dict]) -> str:
    """col_a/b: {label, color_bg, color_text, color_border}
       rows: [{label, a, b}]"""
    c = _c(idx)
    lines = []
    lines.append(f'                <div class="rounded-xl overflow-hidden border {c["border"]}">')
    lines.append(f'                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r {c["wh_from"]} {c["wh_to"]} border-b {c["wh_border"]}">')
    lines.append(f'                    <span class="iconify {c["wh_text"]} text-xs" data-icon="fa6-solid:scale-balanced"></span>')
    lines.append(f'                    <p class="text-[10px] font-bold uppercase tracking-widest {c["wh_text"]}">{title}</p>')
    lines.append('                  </div>')
    lines.append('                  <table class="w-full text-xs border-collapse bg-white">')
    lines.append('                    <thead>')
    lines.append(f'                      <tr class="border-b border-gray-50">')
    lines.append(f'                        <th class="py-2 px-3 text-left font-bold text-gray-400 w-1/3"></th>')
    lines.append(f'                        <th class="py-2 px-3 text-left"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full {col_a["color_bg"]} {col_a["color_text"]} border {col_a["color_border"]} text-[10px] font-bold">{col_a["label"]}</span></th>')
    lines.append(f'                        <th class="py-2 px-3 text-left"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full {col_b["color_bg"]} {col_b["color_text"]} border {col_b["color_border"]} text-[10px] font-bold">{col_b["label"]}</span></th>')
    lines.append('                      </tr>')
    lines.append('                    </thead>')
    lines.append('                    <tbody>')
    for ri, row in enumerate(rows):
        shade = ' bg-gray-50/40' if ri % 2 == 1 else ''
        border = ' border-b border-gray-50' if ri < len(rows) - 1 else ''
        lines.append(f'                      <tr class="{border}{shade}">')
        lines.append(f'                        <td class="py-2 px-3 font-semibold text-gray-600">{row["label"]}</td>')
        lines.append(f'                        <td class="py-2 px-3">{row["a"]}</td>')
        lines.append(f'                        <td class="py-2 px-3">{row["b"]}</td>')
        lines.append('                      </tr>')
    lines.append('                    </tbody>')
    lines.append('                  </table>')
    lines.append('                </div>')
    return "\n".join(lines)


def build_operators_table(idx: int, title: str, rows: list[dict]) -> str:
    """rows: [{op, meaning, example}]"""
    c = _c(idx)
    lines = []
    lines.append(f'                <div class="rounded-xl overflow-hidden border {c["border"]}">')
    lines.append(f'                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r {c["wh_from"]} {c["wh_to"]} border-b {c["wh_border"]}">')
    lines.append(f'                    <span class="iconify {c["wh_text"]} text-xs" data-icon="fa6-solid:calculator"></span>')
    lines.append(f'                    <p class="text-[10px] font-bold uppercase tracking-widest {c["wh_text"]}">{title}</p>')
    lines.append('                  </div>')
    lines.append('                  <table class="w-full text-xs border-collapse bg-white">')
    lines.append('                    <thead>')
    lines.append(f'                      <tr class="border-b border-gray-50">')
    lines.append(f'                        <th class="py-2 px-3 text-left font-bold {c["wh_text"].replace("text-", "text-")} w-12">Op</th>')
    lines.append(f'                        <th class="py-2 px-3 text-left font-bold {c["wh_text"]}">Meaning</th>')
    lines.append(f'                        <th class="py-2 px-3 text-left font-bold {c["wh_text"]}">Example</th>')
    lines.append('                      </tr>')
    lines.append('                    </thead>')
    lines.append('                    <tbody>')
    op_bg = c["code_bg"]
    op_text = c["code_text"].replace("-700", "-800")
    op_border = c["code_border"]
    ex_bg = c["wh_from"].replace("from-", "bg-")
    ex_text = c["code_text"]
    ex_border = c["code_border"]
    for ri, row in enumerate(rows):
        shade = ' bg-gray-50/40' if ri % 2 == 1 else ''
        border = ' border-b border-gray-50' if ri < len(rows) - 1 else ''
        lines.append(f'                      <tr class="{border}{shade}">')
        lines.append(f'                        <td class="py-2 px-3"><code class="font-mono {op_bg} {op_text} border {op_border} px-1.5 py-0.5 rounded-full text-[11px] font-bold">{row["op"]}</code></td>')
        lines.append(f'                        <td class="py-2 px-3 text-gray-500">{row["meaning"]}</td>')
        lines.append(f'                        <td class="py-2 px-3"><code class="font-mono {ex_bg} {ex_text} border {ex_border} px-1.5 py-0.5 rounded text-[10px]">{row["example"]}</code></td>')
        lines.append('                      </tr>')
    lines.append('                    </tbody>')
    lines.append('                  </table>')
    lines.append('                </div>')
    return "\n".join(lines)


def build_panel(idx: int, tab: dict) -> str:
    c = _c(idx)
    hidden = "" if idx == 0 else " hidden"
    color_name = COLOR_ORDER[idx % len(COLOR_ORDER)]

    body_parts = []
    # Header row
    body_parts.append(build_header_row(idx, tab))
    # Definition
    body_parts.append(f'                <p class="text-xs text-gray-600 leading-relaxed">{tab["definition"]}</p>')
    # Widget and code — widget before code by default, unless "code_first"
    if tab.get("code_first"):
        body_parts.append(build_code_block(tab["code"], tab.get("lang", "python")))
        body_parts.append(tab["widget_html"])
    else:
        body_parts.append(tab["widget_html"])
        body_parts.append(build_code_block(tab["code"], tab.get("lang", "python")))
    # Tip
    body_parts.append(build_tip(idx, tab.get("tip_icon", "fa6-solid:lightbulb"), tab["tip_text"]))

    body = "\n\n" + "\n\n".join(body_parts) + "\n"

    return f'''          <!-- ════ Panel {idx} — {tab["label"]} ({color_name}) ════ -->
          <div class="kc-panel kc-panel-anim{hidden}" data-color="{color_name}" role="tabpanel">
            <div class="rounded-2xl border {c["border"]} overflow-hidden">
              <div class="h-1 bg-gradient-to-r {c["topbar"]}"></div>
              <div class="bg-gradient-to-br {c["panelbg"]} p-5 space-y-4">
{body}
              </div>
            </div>
          </div>'''


def build_section(subtitle: str, tabs: list[dict]) -> str:
    sidebar = build_sidebar(tabs)
    panels = "\n\n".join(build_panel(i, tab) for i, tab in enumerate(tabs))

    return f'''<section id="key-concepts" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <!-- Section header -->
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:book-open"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Concepts</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">{subtitle}</p>
      </div>
    </div>

    <div class="bg-white px-6 py-7">
      <div class="flex flex-col md:flex-row gap-0">

{sidebar}

        <!-- ── Panels ── -->
        <div class="flex-1 min-w-0 md:pl-5">

{panels}

        </div><!-- /panels -->
      </div>
    </div>
  </div>
</section>'''


# ── Helper: quickly make code pills for definitions/widgets ──────────

def cp(idx, text):
    """Code pill for definition/widget body (uses -100/-200/-700 colors)."""
    c = _c(idx)
    return f'<code class="font-mono {c["code_bg"]} {c["code_text"]} border {c["code_border"]} px-1 rounded">{text}</code>'


def tcp(idx, text):
    """Code pill for tip callout (uses -200/-300/-800 colors)."""
    c = _c(idx)
    return f'<code class="font-mono {c["tip_code_bg"]} {c["tip_code_text"]} border {c["tip_code_border"]} px-1 rounded">{text}</code>'


def good(text):
    return f'<code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">{text}</code>'


def bad(text):
    return f'<code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">{text}</code>'


def tick_yes(label=""):
    t = f' <span class="text-gray-400">{label}</span>' if label else ''
    return f'<span class="text-green-500 font-bold">✓</span>{t}'


def tick_no(label=""):
    t = f' <span class="text-gray-400">{label}</span>' if label else ''
    return f'<span class="text-red-400 font-bold">✗</span>{t}'


# ── Lesson content ─────────────────────────────────────────────────────

def lesson01_tabs():
    return {
        "subtitle": "Pandas library, DataFrame, and Series.",
        "tabs": [
            {
                "label": "Pandas Library",
                "icon": "fa6-solid:box-open",
                "header_subtitle": "The data analysis toolkit",
                "badge_label": "library",
                "definition": '<strong>Pandas</strong> is a Python library for working with tabular data. You can load, clean, filter, and summarise data in a few lines of code.',
                "widget_html": build_rules_table(0, "Import Conventions", "fa6-solid:list-check", [
                    (f'Always alias as {cp(0,"pd")}', f'{good("import pandas as pd")} ✓'),
                    ('Full name works but avoid it', f'{bad("import pandas")} ✗ → {good("import pandas as pd")}'),
                    (f'Spell it {cp(0,"pandas")} (plural)', f'{bad("panda")} ✗ → {good("pandas")}'),
                ]),
                "code": 'import pandas as pd            # load the library\ndf = pd.read_csv("sales.csv")  # read a CSV into a table\nprint(df.head())               # show the first five rows',
                "tip_text": f'<strong>Always use {tcp(0,"pd")} as the alias.</strong> Every tutorial and colleague expects {tcp(0,"import pandas as pd")}.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "DataFrame",
                "icon": "fa6-solid:table",
                "header_subtitle": "A table of rows and columns",
                "badge_label": "structure",
                "definition": 'A <strong>DataFrame</strong> is a two-dimensional table with labelled columns. Think of it as a spreadsheet inside Python.',
                "widget_html": build_comparison_table(1, "DataFrame vs Spreadsheet",
                    {"label": "DataFrame", "color_bg": "bg-violet-100", "color_text": "text-violet-700", "color_border": "border-violet-200"},
                    {"label": "Spreadsheet", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Row numbering", "a": f'{cp(1,"0, 1, 2…")}', "b": '<code class="font-mono bg-gray-100 text-gray-800 border border-gray-200 px-1 rounded">1, 2, 3…</code>'},
                        {"label": "Columns", "a": "Named labels", "b": "Letters A, B, C…"},
                        {"label": "Row limit", "a": "Millions of rows", "b": "~1 million rows"},
                        {"label": "Automation", "a": tick_yes("Full scripting"), "b": tick_no("Limited macros")},
                    ],
                ),
                "code": 'data = {"Name": ["Alice", "Bob"], "Age": [30, 28]}  # dictionary of lists\ndf = pd.DataFrame(data)     # convert to a DataFrame\nprint(df.shape)              # (2, 2) — two rows, two columns\nprint(df.columns.tolist())   # [\'Name\', \'Age\']',
                "tip_text": f'<strong>Check your shape first.</strong> Run {tcp(1,"df.shape")} after loading data to confirm row and column counts.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Series",
                "icon": "fa6-solid:list-ol",
                "header_subtitle": "One column of data",
                "badge_label": "type",
                "definition": f'A <strong>Series</strong> is a single column of data with an index. Each column you pull from a {cp(2,"DataFrame")} becomes a Series.',
                "widget_html": build_comparison_table(2, "Series vs DataFrame",
                    {"label": "Series", "color_bg": "bg-blue-100", "color_text": "text-blue-700", "color_border": "border-blue-200"},
                    {"label": "DataFrame", "color_bg": "bg-violet-100", "color_text": "text-violet-700", "color_border": "border-violet-200"},
                    [
                        {"label": "Dimensions", "a": "1-D (one column)", "b": "2-D (rows + columns)"},
                        {"label": "Access with", "a": f'{cp(2,"df[&quot;col&quot;]")}', "b": '<code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1 rounded">df[["a","b"]]</code>'},
                        {"label": "Use for", "a": "One-column maths", "b": "Multi-column tables"},
                    ],
                ),
                "code": 'ages = df["Age"]       # select one column — returns a Series\nprint(type(ages))      # &lt;class \'pandas...Series\'&gt;\nprint(ages.mean())     # average of the column\nprint(ages.max())      # largest value in the column',
                "tip_text": f'<strong>Single brackets return a Series; double brackets return a DataFrame.</strong> Use {tcp(2,"df[&quot;Age&quot;]")} for a Series and {tcp(2,"df[[&quot;Age&quot;]]")} for a one-column DataFrame.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


def lesson02_tabs():
    return {
        "subtitle": "DataFrame structure, dtypes, and inspection methods.",
        "tabs": [
            {
                "label": "DataFrame Structure",
                "icon": "fa6-solid:table-cells",
                "header_subtitle": "Rows, columns, and the index",
                "badge_label": "anatomy",
                "definition": 'A <strong>DataFrame</strong> has three parts: an index (row labels), column headers, and the data cells. Every row has a numbered index starting from zero.',
                "widget_html": build_rules_table(0, "Anatomy of a DataFrame", "fa6-solid:table-cells", [
                    (f'Index = {cp(0,"row labels")}', f'{good("0, 1, 2…")} by default'),
                    (f'Columns = {cp(0,"header names")}', f'{good("df.columns")} lists them'),
                    (f'Shape = {cp(0,"(rows, cols)")}', f'{good("df.shape")} returns a tuple'),
                ]),
                "code": 'df = pd.read_csv("staff.csv")   # load data\nprint(df.index)                 # RangeIndex(start=0, stop=50)\nprint(df.columns.tolist())      # [\'Name\', \'Role\', \'Salary\']\nprint(df.shape)                 # (50, 3)',
                "tip_text": f'<strong>Row numbering starts at zero.</strong> The first row is index {tcp(0,"0")}, not {tcp(0,"1")}. Keep this in mind when slicing.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Data Types (dtypes)",
                "icon": "fa6-solid:tags",
                "header_subtitle": "How Pandas stores each column",
                "badge_label": "dtypes",
                "definition": f'Each column has a <strong>dtype</strong> — the data type Pandas uses to store its values. Common types include {cp(1,"int64")} for whole numbers, {cp(1,"float64")} for decimals, and {cp(1,"object")} for text.',
                "widget_html": build_operators_table(1, "Common Data Types", [
                    {"op": "int64", "meaning": "Whole numbers", "example": "1, 42, -7"},
                    {"op": "float64", "meaning": "Decimal numbers", "example": "3.14, 0.5"},
                    {"op": "object", "meaning": "Text (strings)", "example": "'Sales', 'UK'"},
                    {"op": "bool", "meaning": "True / False", "example": "True, False"},
                    {"op": "datetime64", "meaning": "Dates and times", "example": "2026-01-15"},
                ]),
                "code": 'print(df.dtypes)        # show every column\'s type\nprint(df["Salary"].dtype)  # int64\nprint(df["Name"].dtype)    # object (text)',
                "tip_text": f'<strong>If a number column shows {tcp(1,"object")}, it is stored as text.</strong> Convert it with {tcp(1,"pd.to_numeric()")} before doing maths.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "Inspection Methods",
                "icon": "fa6-solid:magnifying-glass",
                "header_subtitle": "Quick ways to explore your data",
                "badge_label": "methods",
                "definition": f'Pandas provides shortcut methods to inspect a DataFrame. Use {cp(2,"head()")}, {cp(2,"info()")}, and {cp(2,"describe()")} to understand your data before writing any transformation code.',
                "widget_html": build_rules_table(2, "Key Inspection Methods", "fa6-solid:magnifying-glass", [
                    (f'{cp(2,"df.head()")}', 'First 5 rows'),
                    (f'{cp(2,"df.tail()")}', 'Last 5 rows'),
                    (f'{cp(2,"df.info()")}', 'Column names, types, and non-null counts'),
                    (f'{cp(2,"df.describe()")}', 'Stats: mean, min, max for numbers'),
                    (f'{cp(2,"df.shape")}', 'Row and column counts'),
                ]),
                "code": 'print(df.head())       # first five rows\nprint(df.info())       # types and missing values\nprint(df.describe())   # summary statistics',
                "tip_text": f'<strong>Run {tcp(2,"df.info()")} before anything else.</strong> It reveals missing values and wrong dtypes in one glance.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


def lesson03_tabs():
    return {
        "subtitle": "read_csv(), read_excel(), and dataset inspection.",
        "tabs": [
            {
                "label": "read_csv()",
                "icon": "fa6-solid:file-csv",
                "header_subtitle": "Load comma-separated files",
                "badge_label": "function",
                "definition": f'<strong>read_csv()</strong> loads a CSV file into a DataFrame. Pass the file path as a string. Pandas assumes a comma separator unless you set {cp(0,"sep")}.',
                "widget_html": build_rules_table(0, "Key Parameters", "fa6-solid:sliders", [
                    (f'{cp(0,"filepath")}', 'Path to the CSV file (required)'),
                    (f'{cp(0,"sep")}', f'Delimiter — default is {good(",")}'),
                    (f'{cp(0,"encoding")}', f'Character set — try {good("latin-1")} if garbled'),
                    (f'{cp(0,"header")}', f'Row number for column names — default {good("0")}'),
                ]),
                "code": 'df = pd.read_csv("sales.csv")               # comma separated\ndf2 = pd.read_csv("report.csv", sep=";")    # semicolon separated\ndf3 = pd.read_csv("data.csv", encoding="latin-1")  # fix encoding',
                "tip_text": f'<strong>Open the file in a text editor first.</strong> Check whether values are separated by commas or semicolons, then set {tcp(0,"sep")} accordingly.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "read_excel()",
                "icon": "fa6-solid:file-excel",
                "header_subtitle": "Load Excel workbooks",
                "badge_label": "function",
                "definition": f'<strong>read_excel()</strong> loads an Excel file into a DataFrame. It reads the first sheet by default. Use {cp(1,"sheet_name")} to pick a different sheet.',
                "widget_html": build_rules_table(1, "Key Parameters", "fa6-solid:sliders", [
                    (f'{cp(1,"filepath")}', 'Path to the .xlsx or .xls file'),
                    (f'{cp(1,"sheet_name")}', f'Sheet name or index — default {good("0")} (first sheet)'),
                    (f'{cp(1,"header")}', f'Row for column names — default {good("0")}'),
                    (f'{cp(1,"usecols")}', 'List of columns to load (saves memory)'),
                ]),
                "code": 'df = pd.read_excel("report.xlsx")                 # first sheet\ndf2 = pd.read_excel("report.xlsx", sheet_name="Q1") # named sheet\ndf3 = pd.read_excel("report.xlsx", usecols=["Name", "Total"])',
                "tip_text": f'<strong>Install {tcp(1,"openpyxl")} first.</strong> Run {tcp(1,"pip install openpyxl")} — Pandas needs it to read .xlsx files.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "Inspecting Data",
                "icon": "fa6-solid:magnifying-glass-chart",
                "header_subtitle": "Explore after loading",
                "badge_label": "workflow",
                "definition": '<strong>Inspecting a dataset</strong> means checking its size, column types, and first few rows. Always inspect before writing any transformation code.',
                "widget_html": build_comparison_table(2, "Inspection Methods at a Glance",
                    {"label": "Method", "color_bg": "bg-blue-100", "color_text": "text-blue-700", "color_border": "border-blue-200"},
                    {"label": "Returns", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Preview rows", "a": f'{cp(2,"df.head()")}', "b": "First 5 rows"},
                        {"label": "Shape", "a": f'{cp(2,"df.shape")}', "b": "(rows, columns) tuple"},
                        {"label": "Types + nulls", "a": f'{cp(2,"df.info()")}', "b": "Column names, dtypes, non-null counts"},
                        {"label": "Statistics", "a": f'{cp(2,"df.describe()")}', "b": "Mean, min, max for numeric columns"},
                    ],
                ),
                "code": 'df = pd.read_csv("data.csv")  # load the file\nprint(df.shape)               # (rows, columns)\nprint(df.head())              # first five rows\nprint(df.dtypes)              # column types',
                "tip_text": f'<strong>Spend 60 seconds on {tcp(2,"info()")} and {tcp(2,"describe()")} before coding.</strong> They reveal missing values and wrong types before you hit an error.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


def lesson04_tabs():
    return {
        "subtitle": "Single column, multiple columns, and DataFrame subsets.",
        "tabs": [
            {
                "label": "Single Column",
                "icon": "fa6-solid:grip-lines-vertical",
                "header_subtitle": "Select one column by name",
                "badge_label": "syntax",
                "definition": f'<strong>Single-column selection</strong> uses square brackets with the column name as a string. The result is a {cp(0,"Series")} — a one-dimensional array with an index.',
                "widget_html": build_rules_table(0, "Bracket Rules", "fa6-solid:list-check", [
                    (f'Single brackets {cp(0,"df[&quot;col&quot;]")}', f'Returns a {good("Series")}'),
                    ('Name must match exactly', f'{bad("df[&quot;sales&quot;]")} ✗ if column is "Sales"'),
                    (f'Dot notation {cp(0,"df.col")}', f'{bad("df.col")} ✗ avoid — breaks on spaces'),
                ]),
                "code": 'names = df["Name"]      # returns a Series\nprint(type(names))      # &lt;class \'pandas...Series\'&gt;\nprint(names.head())     # first five values',
                "tip_text": f'<strong>Column names are case-sensitive.</strong> {tcp(0,"df[&quot;Name&quot;]")} works but {tcp(0,"df[&quot;name&quot;]")} raises a KeyError.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "Multiple Columns",
                "icon": "fa6-solid:table-columns",
                "header_subtitle": "Select two or more columns",
                "badge_label": "syntax",
                "definition": f'<strong>Multi-column selection</strong> uses double brackets with a list of names. The result is a {cp(1,"DataFrame")} — a smaller table with just those columns.',
                "widget_html": build_comparison_table(1, "Single vs Double Brackets",
                    {"label": "df[\"col\"]", "color_bg": "bg-violet-100", "color_text": "text-violet-700", "color_border": "border-violet-200"},
                    {"label": "df[[\"a\",\"b\"]]", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Returns", "a": "Series", "b": "DataFrame"},
                        {"label": "Dimensions", "a": "1-D", "b": "2-D"},
                        {"label": "Columns", "a": "One", "b": "Two or more"},
                    ],
                ),
                "code": 'subset = df[["Name", "Salary"]]  # returns a DataFrame\nprint(type(subset))               # &lt;class \'pandas...DataFrame\'&gt;\nprint(subset.shape)                # (rows, 2)',
                "tip_text": f'<strong>Double brackets = list inside brackets.</strong> {tcp(1,"df[[&quot;A&quot;, &quot;B&quot;]]")} is really {tcp(1,"df[ [&quot;A&quot;, &quot;B&quot;] ]")} — a list passed to the accessor.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Column Subset",
                "icon": "fa6-solid:scissors",
                "header_subtitle": "Create a smaller working table",
                "badge_label": "technique",
                "definition": '<strong>Creating a subset</strong> means selecting only the columns you need and storing the result in a new variable. This keeps your workspace tidy and uses less memory.',
                "widget_html": build_rules_table(2, "Subset Best Practices", "fa6-solid:list-check", [
                    ('Name columns explicitly', f'{good("df[[&quot;A&quot;, &quot;B&quot;]]")} ✓'),
                    ('Avoid modifying the original', f'Store in a {good("new variable")}'),
                    ('Check shape after subsetting', f'{good("subset.shape")}'),
                ]),
                "code": 'cols = ["Name", "Role", "Salary"]  # list of column names\nsubset = df[cols]                   # select those columns\nprint(subset.shape)                  # confirm column count\nprint(subset.head())                 # preview the subset',
                "tip_text": f'<strong>Store column lists in a variable.</strong> Writing {tcp(2,"cols = [...]")} once lets you reuse the same selection everywhere.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


def lesson05_tabs():
    return {
        "subtitle": "Boolean masks, comparison operators, and combining filters.",
        "tabs": [
            {
                "label": "Boolean Masks",
                "icon": "fa6-solid:filter",
                "header_subtitle": "True/False for every row",
                "badge_label": "concept",
                "definition": f'A <strong>boolean mask</strong> is a Series of {cp(0,"True")} and {cp(0,"False")} values — one per row. When you pass it inside brackets, Pandas keeps only the rows marked True.',
                "widget_html": build_rules_table(0, "How Filtering Works", "fa6-solid:filter", [
                    ('Write a condition', f'{good("df[&quot;Age&quot;] &gt; 30")} → True/False series'),
                    ('Pass it to brackets', f'{good("df[mask]")} → filtered rows'),
                    ('Assign to a variable', f'{good("result = df[mask]")}'),
                ]),
                "code": 'mask = df["Age"] > 30         # True where Age > 30\nprint(mask.head())             # shows True/False per row\nolder = df[mask]               # keep only True rows\nprint(older.shape)             # fewer rows than original',
                "tip_text": f'<strong>A mask does not change the original DataFrame.</strong> It returns a new, smaller DataFrame. The original {tcp(0,"df")} stays intact.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Comparison Operators",
                "icon": "fa6-solid:not-equal",
                "header_subtitle": "Build conditions for filtering",
                "badge_label": "operators",
                "definition": '<strong>Comparison operators</strong> compare each value in a column against a target. The result is a boolean mask you can pass to the bracket accessor.',
                "code_first": True,
                "widget_html": build_operators_table(1, "Comparison Operators", [
                    {"op": "==", "meaning": "Equal to", "example": 'df["Region"] == "UK"'},
                    {"op": "!=", "meaning": "Not equal", "example": 'df["Status"] != "Closed"'},
                    {"op": "&gt;", "meaning": "Greater than", "example": "df[\"Sales\"] &gt; 1000"},
                    {"op": "&lt;", "meaning": "Less than", "example": "df[\"Age\"] &lt; 25"},
                    {"op": "&gt;=", "meaning": "Greater or equal", "example": "df[\"Score\"] &gt;= 90"},
                    {"op": "&lt;=", "meaning": "Less or equal", "example": "df[\"Qty\"] &lt;= 5"},
                ]),
                "code": 'big = df[df["Sales"] > 1000]        # rows where Sales > 1000\nuk = df[df["Region"] == "UK"]       # rows where Region is UK\nprint(big.shape)                     # count of matching rows',
                "tip_text": f'<strong>Use {tcp(1,"==")} for comparison, not {tcp(1,"=")}.</strong> A single equals sign assigns a value. A double equals sign checks equality.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "Combining Filters",
                "icon": "fa6-solid:code-merge",
                "header_subtitle": "AND, OR, and NOT conditions",
                "badge_label": "logic",
                "definition": f'You can <strong>combine filters</strong> with {cp(2,"&amp;")} (and), {cp(2,"|")} (or), and {cp(2,"~")} (not). Wrap each condition in parentheses.',
                "widget_html": build_operators_table(2, "Logical Operators", [
                    {"op": "&amp;", "meaning": "Both true (AND)", "example": "(A) &amp; (B)"},
                    {"op": "|", "meaning": "Either true (OR)", "example": "(A) | (B)"},
                    {"op": "~", "meaning": "Opposite (NOT)", "example": "~(A)"},
                ]),
                "code": 'both = df[(df["Age"] > 30) &amp; (df["Region"] == "UK")]   # AND\neither = df[(df["Age"] > 30) | (df["Region"] == "UK")]  # OR\nnot_uk = df[~(df["Region"] == "UK")]                     # NOT',
                "tip_text": f'<strong>Always wrap each condition in parentheses.</strong> Without them, Python reads the operators in the wrong order and raises an error.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
        ],
    }


def lesson06_tabs():
    return {
        "subtitle": "Column assignment, vectorised maths, and transformations.",
        "tabs": [
            {
                "label": "Column Assignment",
                "icon": "fa6-solid:pen-to-square",
                "header_subtitle": "Create a new column",
                "badge_label": "syntax",
                "definition": f'<strong>Column assignment</strong> creates a new column by writing {cp(0,"df[&quot;new&quot;] = value")}. If the column already exists, it overwrites it.',
                "widget_html": build_rules_table(0, "Assignment Rules", "fa6-solid:list-check", [
                    (f'New column with {cp(0,"df[&quot;col&quot;] = ...")}', f'{good("creates")} or {bad("overwrites")}'),
                    ('Right side must match row count', f'{good("scalar or Series of same length")}'),
                    ('Name must be a string', f'{bad("df[Total]")} ✗ → {good("df[&quot;Total&quot;]")}'),
                ]),
                "code": 'df["Bonus"] = 500                          # constant for every row\ndf["Total"] = df["Salary"] + df["Bonus"]   # column maths\nprint(df[["Salary", "Bonus", "Total"]].head())',
                "tip_text": f'<strong>Put the new column name in quotes.</strong> {tcp(0,"df[&quot;Total&quot;]")} works. {tcp(0,"df[Total]")} looks for a variable named Total.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "Vectorised Maths",
                "icon": "fa6-solid:calculator",
                "header_subtitle": "Operate on entire columns at once",
                "badge_label": "concept",
                "definition": '<strong>Vectorised operations</strong> apply a calculation to every row in one go. They are much faster than looping row by row.',
                "widget_html": build_operators_table(1, "Common Column Operations", [
                    {"op": "+", "meaning": "Add columns or values", "example": 'df["A"] + df["B"]'},
                    {"op": "-", "meaning": "Subtract", "example": 'df["Revenue"] - df["Cost"]'},
                    {"op": "*", "meaning": "Multiply", "example": "df[\"Qty\"] * df[\"Price\"]"},
                    {"op": "/", "meaning": "Divide", "example": "df[\"Total\"] / 100"},
                    {"op": "**", "meaning": "Power", "example": "df[\"Base\"] ** 2"},
                ]),
                "code": 'df["Revenue"] = df["Qty"] * df["Price"]    # multiply two columns\ndf["Margin"]  = df["Revenue"] - df["Cost"]  # subtract columns\ndf["Tax"]     = df["Revenue"] * 0.2          # multiply by a scalar',
                "tip_text": f'<strong>Avoid loops for column maths.</strong> A single line like {tcp(1,"df[&quot;A&quot;] * df[&quot;B&quot;]")} runs in milliseconds on millions of rows.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Transformations",
                "icon": "fa6-solid:wand-magic-sparkles",
                "header_subtitle": "Change existing column values",
                "badge_label": "methods",
                "definition": f'<strong>Transformations</strong> change the values in a column. Use built-in methods like {cp(2,".round()")}, {cp(2,".str.upper()")}, or {cp(2,".clip()")} instead of writing loops.',
                "widget_html": build_rules_table(2, "Useful Transform Methods", "fa6-solid:wand-magic-sparkles", [
                    (f'{cp(2,".round(2)")}', 'Round to 2 decimal places'),
                    (f'{cp(2,".str.upper()")}', 'Convert text to uppercase'),
                    (f'{cp(2,".str.strip()")}', 'Remove leading/trailing spaces'),
                    (f'{cp(2,".clip(lower, upper)")}', 'Cap values within a range'),
                    (f'{cp(2,".replace(old, new)")}', 'Swap specific values'),
                ]),
                "code": 'df["Margin"] = df["Margin"].round(2)         # round to 2 decimals\ndf["Name"]   = df["Name"].str.strip()        # trim whitespace\ndf["Region"] = df["Region"].str.upper()      # UPPERCASE text',
                "tip_text": f'<strong>Chain transforms on the same line.</strong> {tcp(2,"df[&quot;Name&quot;].str.strip().str.upper()")} trims then uppercases in one expression.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


def lesson07_tabs():
    return {
        "subtitle": "groupby(), aggregation functions, and agg().",
        "tabs": [
            {
                "label": "groupby()",
                "icon": "fa6-solid:layer-group",
                "header_subtitle": "Split data into groups",
                "badge_label": "method",
                "definition": f'<strong>groupby()</strong> splits a DataFrame into groups based on one or more columns. After grouping, you apply an aggregation like {cp(0,".sum()")} or {cp(0,".mean()")} to summarise each group.',
                "widget_html": build_rules_table(0, "groupby() Steps", "fa6-solid:layer-group", [
                    ('1. Split', f'{good("df.groupby(&quot;Region&quot;)")} — create groups'),
                    ('2. Apply', f'{good(".sum()")} — run a function per group'),
                    ('3. Combine', 'Pandas merges results into one table'),
                ]),
                "code": 'grouped = df.groupby("Region")           # split by Region\ntotals = grouped["Sales"].sum()           # sum Sales per group\nprint(totals)                              # one row per region',
                "tip_text": f'<strong>You can chain it in one line.</strong> {tcp(0,"df.groupby(&quot;Region&quot;)[&quot;Sales&quot;].sum()")} does split, apply, and combine in one expression.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Aggregation Functions",
                "icon": "fa6-solid:calculator",
                "header_subtitle": "Summarise each group",
                "badge_label": "methods",
                "definition": '<strong>Aggregation functions</strong> reduce a group of values to a single number. Pandas provides built-in methods for the most common calculations.',
                "code_first": True,
                "widget_html": build_operators_table(1, "Built-in Aggregations", [
                    {"op": ".sum()", "meaning": "Total", "example": "Sales per region"},
                    {"op": ".mean()", "meaning": "Average", "example": "Average salary"},
                    {"op": ".count()", "meaning": "Number of rows", "example": "Orders per customer"},
                    {"op": ".min()", "meaning": "Smallest value", "example": "Lowest price"},
                    {"op": ".max()", "meaning": "Largest value", "example": "Highest score"},
                    {"op": ".median()", "meaning": "Middle value", "example": "Median age"},
                ]),
                "code": 'df.groupby("Team")["Revenue"].sum()     # total revenue per team\ndf.groupby("Team")["Revenue"].mean()    # average revenue per team\ndf.groupby("Team")["Name"].count()      # headcount per team',
                "tip_text": f'<strong>Only numeric columns work with {tcp(1,".sum()")} and {tcp(1,".mean()")}.</strong> Calling them on text columns gives unexpected results or errors.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "Multiple Aggregations",
                "icon": "fa6-solid:bars-staggered",
                "header_subtitle": "Several stats in one call",
                "badge_label": "agg()",
                "definition": f'<strong>agg()</strong> lets you apply more than one function at a time. Pass a dictionary mapping column names to a list of functions.',
                "widget_html": build_comparison_table(2, "Single vs Multiple Aggregations",
                    {"label": ".sum()", "color_bg": "bg-blue-100", "color_text": "text-blue-700", "color_border": "border-blue-200"},
                    {"label": ".agg()", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Functions", "a": "One", "b": "Multiple"},
                        {"label": "Result columns", "a": "One", "b": "One per function"},
                        {"label": "Flexibility", "a": "Basic", "b": "Full control"},
                    ],
                ),
                "code": 'summary = df.groupby("Region").agg(\n    total_sales=("Sales", "sum"),       # sum of Sales\n    avg_sales=("Sales", "mean"),        # average of Sales\n    order_count=("OrderID", "count")    # count of orders\n)\nprint(summary.head())',
                "tip_text": f'<strong>Named aggregations make columns readable.</strong> {tcp(2,"total_sales=(&quot;Sales&quot;, &quot;sum&quot;)")} creates a column called {tcp(2,"total_sales")} instead of a cryptic multi-index.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


def lesson08_tabs():
    return {
        "subtitle": "merge(), join types, and key columns.",
        "tabs": [
            {
                "label": "merge()",
                "icon": "fa6-solid:code-merge",
                "header_subtitle": "Combine two DataFrames",
                "badge_label": "method",
                "definition": f'<strong>merge()</strong> joins two DataFrames on a shared column — like a VLOOKUP across two tables. Set {cp(0,"on")} to the column name they share.',
                "widget_html": build_rules_table(0, "Key Parameters", "fa6-solid:sliders", [
                    (f'{cp(0,"on")}', 'Column name shared by both tables'),
                    (f'{cp(0,"how")}', f'Join type — {good("inner")}, left, right, outer'),
                    (f'{cp(0,"left_on")} / {cp(0,"right_on")}', 'When column names differ'),
                    (f'{cp(0,"suffixes")}', 'Labels for duplicate column names'),
                ]),
                "code": 'merged = pd.merge(orders, customers, on="CustomerID")  # inner join\nprint(merged.shape)              # combined table\nprint(merged.columns.tolist())   # columns from both tables',
                "tip_text": f'<strong>Check for duplicates before merging.</strong> If one table has repeated keys, {tcp(0,"merge()")} multiplies rows. Run {tcp(0,"df.duplicated()")} first.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "Inner Join",
                "icon": "fa6-solid:circle-dot",
                "header_subtitle": "Keep only matching rows",
                "badge_label": "how",
                "definition": f'An <strong>inner join</strong> keeps only rows that appear in both tables. Rows with no match in the other table are dropped. This is the default {cp(1,"how")} setting.',
                "widget_html": build_comparison_table(1, "Inner Join Behaviour",
                    {"label": "Left table", "color_bg": "bg-violet-100", "color_text": "text-violet-700", "color_border": "border-violet-200"},
                    {"label": "Right table", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Key in both", "a": tick_yes("Kept"), "b": tick_yes("Kept")},
                        {"label": "Key in left only", "a": tick_no("Dropped"), "b": "—"},
                        {"label": "Key in right only", "a": "—", "b": tick_no("Dropped")},
                    ],
                ),
                "code": 'inner = pd.merge(orders, customers,\n                 on="CustomerID",\n                 how="inner")         # only matching rows\nprint(inner.shape)                     # fewer rows than either table',
                "tip_text": f'<strong>Inner join is the default.</strong> If you omit {tcp(1,"how")}, Pandas uses {tcp(1,"inner")} automatically.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Left Join",
                "icon": "fa6-solid:arrow-right-to-bracket",
                "header_subtitle": "Keep all rows from the left table",
                "badge_label": "how",
                "definition": '<strong>Left join</strong> keeps every row from the left table. If a row has no match in the right table, the right-side columns are filled with NaN.',
                "widget_html": build_comparison_table(2, "Left Join Behaviour",
                    {"label": "Left table", "color_bg": "bg-blue-100", "color_text": "text-blue-700", "color_border": "border-blue-200"},
                    {"label": "Right table", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Key in both", "a": tick_yes("Kept"), "b": tick_yes("Kept")},
                        {"label": "Key in left only", "a": tick_yes("Kept"), "b": "NaN"},
                        {"label": "Key in right only", "a": "—", "b": tick_no("Dropped")},
                    ],
                ),
                "code": 'left = pd.merge(orders, customers,\n                on="CustomerID",\n                how="left")           # keep all orders\nprint(left.shape)                      # same row count as orders',
                "tip_text": f'<strong>Left join is the most common choice.</strong> Use it when you want to keep every row from your main table and add extra columns from a lookup table.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Right / Outer Join",
                "icon": "fa6-solid:arrows-left-right",
                "header_subtitle": "Other join options",
                "badge_label": "how",
                "definition": f'A <strong>right join</strong> keeps all rows from the right table. An <strong>outer join</strong> keeps all rows from both tables, filling gaps with {cp(3,"NaN")}.',
                "widget_html": build_comparison_table(3, "Right vs Outer",
                    {"label": "Right join", "color_bg": "bg-emerald-100", "color_text": "text-emerald-700", "color_border": "border-emerald-200"},
                    {"label": "Outer join", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Left-only rows", "a": tick_no("Dropped"), "b": tick_yes("Kept + NaN")},
                        {"label": "Right-only rows", "a": tick_yes("Kept"), "b": tick_yes("Kept + NaN")},
                        {"label": "Both matched", "a": tick_yes("Kept"), "b": tick_yes("Kept")},
                    ],
                ),
                "code": 'right = pd.merge(orders, customers,\n                 on="CustomerID",\n                 how="right")          # keep all customers\nouter = pd.merge(orders, customers,\n                 on="CustomerID",\n                 how="outer")          # keep everything',
                "tip_text": f'<strong>Outer joins can create many NaN values.</strong> Run {tcp(3,"df.isna().sum()")} after an outer join to see how many gaps appeared.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
        ],
    }


def lesson09_tabs():
    return {
        "subtitle": "isna(), dropna(), fillna(), and missing-data strategy.",
        "tabs": [
            {
                "label": "Detecting Missing Data",
                "icon": "fa6-solid:circle-question",
                "header_subtitle": "Find NaN values",
                "badge_label": "detection",
                "definition": f'Pandas represents missing values as {cp(0,"NaN")} (Not a Number). Use {cp(0,"isna()")} to create a boolean mask that is True wherever a value is missing.',
                "widget_html": build_rules_table(0, "Detection Methods", "fa6-solid:magnifying-glass", [
                    (f'{cp(0,"df.isna()")}', 'True/False mask for every cell'),
                    (f'{cp(0,"df.isna().sum()")}', 'Count of missing per column'),
                    (f'{cp(0,"df.notna()")}', 'Opposite — True where not missing'),
                ]),
                "code": 'print(df.isna().sum())        # missing count per column\nprint(df["Age"].isna().sum()) # missing in one column\nprint(df.isna().any())        # True if column has any NaN',
                "tip_text": f'<strong>Never use {tcp(0,"== None")} or {tcp(0,"== NaN")}.</strong> They do not detect Pandas missing values. Always use {tcp(0,"isna()")}.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "Removing Missing Data",
                "icon": "fa6-solid:trash-can",
                "header_subtitle": "Drop rows or columns with NaN",
                "badge_label": "method",
                "definition": f'<strong>dropna()</strong> removes rows (or columns) that contain missing values. By default it drops any row with at least one NaN.',
                "widget_html": build_rules_table(1, "dropna() Parameters", "fa6-solid:sliders", [
                    (f'{cp(1,"axis=0")}', 'Drop rows (default)'),
                    (f'{cp(1,"axis=1")}', 'Drop columns'),
                    (f'{cp(1,"how=&quot;all&quot;")}', 'Drop only if every value is NaN'),
                    (f'{cp(1,"subset=[&quot;col&quot;]")}', 'Check only specific columns'),
                ]),
                "code": 'clean = df.dropna()                     # drop any row with NaN\nclean2 = df.dropna(subset=["Email"])    # drop only if Email is NaN\nprint(clean.shape)                       # fewer rows',
                "tip_text": f'<strong>dropna() returns a new DataFrame.</strong> The original is unchanged unless you add {tcp(1,"inplace=True")} or reassign: {tcp(1,"df = df.dropna()")}.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Filling Missing Data",
                "icon": "fa6-solid:fill-drip",
                "header_subtitle": "Replace NaN with a value",
                "badge_label": "method",
                "definition": f'<strong>fillna()</strong> replaces every NaN with a value you choose. Pass a number, a string, or even a column\'s {cp(2,"mean()")}.',
                "widget_html": build_rules_table(2, "fillna() Options", "fa6-solid:sliders", [
                    (f'{cp(2,"df.fillna(0)")}', 'Replace NaN with zero'),
                    (f'{cp(2,"df.fillna(&quot;Unknown&quot;)")}', 'Replace NaN with text'),
                    (f'{cp(2,"df.fillna(df.mean())")}', 'Replace with column averages'),
                    (f'{cp(2,"df.fillna(method=&quot;ffill&quot;)")}', 'Forward-fill from previous row'),
                ]),
                "code": 'df["Age"] = df["Age"].fillna(df["Age"].mean())  # fill with average\ndf["City"] = df["City"].fillna("Unknown")       # fill with text\nprint(df.isna().sum())                            # confirm zero NaN',
                "tip_text": f'<strong>Save the result.</strong> {tcp(2,"df.fillna(0)")} alone does nothing. Write {tcp(2,"df[&quot;col&quot;] = df[&quot;col&quot;].fillna(0)")} to keep the change.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "Choosing a Strategy",
                "icon": "fa6-solid:route",
                "header_subtitle": "Drop or fill — when to use each",
                "badge_label": "decision",
                "definition": '<strong>Choosing a strategy</strong> depends on why the data is missing and how much of it is gone. Dropping works when very few rows are affected. Filling works when you have a sensible replacement value.',
                "widget_html": build_comparison_table(3, "Drop vs Fill",
                    {"label": "dropna()", "color_bg": "bg-emerald-100", "color_text": "text-emerald-700", "color_border": "border-emerald-200"},
                    {"label": "fillna()", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Best when", "a": "Few rows missing", "b": "Many rows missing"},
                        {"label": "Risk", "a": "Lose too much data", "b": "Introduce fake values"},
                        {"label": "Speed", "a": "Very fast", "b": "Very fast"},
                        {"label": "Common fill", "a": "—", "b": "Mean, median, \"Unknown\""},
                    ],
                ),
                "code": 'pct = df.isna().mean() * 100       # % missing per column\nprint(pct)                          # decide based on percentage\n# < 5% missing → dropna() is safe\n# > 5% missing → fillna() is safer',
                "tip_text": f'<strong>Check the percentage first.</strong> If a column is 40% empty, dropping rows throws away nearly half your data. Use {tcp(3,"fillna()")} instead.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


def lesson10_tabs():
    return {
        "subtitle": "to_csv(), to_excel(), index control, and column selection.",
        "tabs": [
            {
                "label": "Exporting to CSV",
                "icon": "fa6-solid:file-csv",
                "header_subtitle": "Save a DataFrame as a CSV file",
                "badge_label": "method",
                "definition": f'<strong>to_csv()</strong> writes a DataFrame to a comma-separated text file. Pass the output filename as a string.',
                "widget_html": build_rules_table(0, "Key Parameters", "fa6-solid:sliders", [
                    (f'{cp(0,"path")}', 'Output filename (required)'),
                    (f'{cp(0,"index=False")}', 'Exclude the row numbers'),
                    (f'{cp(0,"sep")}', f'Delimiter — default {good(",")}'),
                    (f'{cp(0,"encoding")}', f'Character set — default {good("utf-8")}'),
                ]),
                "code": 'df.to_csv("output.csv", index=False)   # save without row numbers\ndf.to_csv("euro.csv", sep=";")          # semicolon-separated\nprint("CSV saved")',
                "tip_text": f'<strong>Always pass {tcp(0,"index=False")}.</strong> Without it, Pandas adds a column of row numbers that clutters the output file.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Exporting to Excel",
                "icon": "fa6-solid:file-excel",
                "header_subtitle": "Save as an .xlsx workbook",
                "badge_label": "method",
                "definition": f'<strong>to_excel()</strong> writes a DataFrame to an Excel file. Use {cp(1,"sheet_name")} to name the sheet.',
                "widget_html": build_rules_table(1, "Key Parameters", "fa6-solid:sliders", [
                    (f'{cp(1,"path")}', 'Output filename (required, .xlsx)'),
                    (f'{cp(1,"index=False")}', 'Exclude row numbers'),
                    (f'{cp(1,"sheet_name")}', f'Tab name — default {good("Sheet1")}'),
                    (f'{cp(1,"float_format")}', 'Number format — e.g. "%.2f"'),
                ]),
                "code": 'df.to_excel("report.xlsx", index=False)  # save to Excel\ndf.to_excel("report.xlsx",\n            sheet_name="Sales",           # custom sheet name\n            index=False)',
                "tip_text": f'<strong>Install {tcp(1,"openpyxl")} first.</strong> Run {tcp(1,"pip install openpyxl")} — Pandas needs it to write .xlsx files.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "Index Control",
                "icon": "fa6-solid:hashtag",
                "header_subtitle": "Include or exclude the index",
                "badge_label": "parameter",
                "definition": f'The <strong>index</strong> is the row label column. By default, {cp(2,"to_csv()")} and {cp(2,"to_excel()")} include it. Set {cp(2,"index=False")} to exclude it.',
                "widget_html": build_comparison_table(2, "With vs Without Index",
                    {"label": "index=True", "color_bg": "bg-blue-100", "color_text": "text-blue-700", "color_border": "border-blue-200"},
                    {"label": "index=False", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Extra column", "a": tick_yes("0, 1, 2…"), "b": tick_no("None")},
                        {"label": "File size", "a": "Slightly larger", "b": "Slightly smaller"},
                        {"label": "Best for", "a": "Time-series index", "b": "Most exports"},
                    ],
                ),
                "code": 'df.to_csv("with_index.csv")             # includes 0, 1, 2…\ndf.to_csv("clean.csv", index=False)     # no extra column\nprint("Both files saved")',
                "tip_text": f'<strong>The extra column looks like unnamed data.</strong> Recipients of your file may not know what the index column means. Use {tcp(2,"index=False")} unless the index carries meaning.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Exporting Columns",
                "icon": "fa6-solid:table-columns",
                "header_subtitle": "Export only selected columns",
                "badge_label": "technique",
                "definition": '<strong>Exporting specific columns</strong> means selecting a subset of columns before calling the export method. This keeps the output file tidy and focused.',
                "widget_html": build_rules_table(3, "Column Selection Patterns", "fa6-solid:list-check", [
                    (f'{cp(3,"df[[&quot;A&quot;,&quot;B&quot;]].to_csv(...)")}', 'Select then export'),
                    (f'{cp(3,"usecols")} on re-import', 'Load only needed columns'),
                    ('Store column list in a variable', f'{good("cols = [&quot;A&quot;, &quot;B&quot;]")}'),
                ]),
                "code": 'cols = ["Name", "Region", "Sales"]         # columns to export\ndf[cols].to_csv("subset.csv", index=False) # export only those\nprint(df[cols].shape)                       # confirm column count',
                "tip_text": f'<strong>Export only what the recipient needs.</strong> A 50-column file is overwhelming. Select the relevant columns with {tcp(3,"df[cols]")} before exporting.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


# ── Lesson registry ───────────────────────────────────────────────────

LESSONS = {
    "lesson01_introduction_to_pandas.html": lesson01_tabs,
    "lesson02_dataframes_explained.html": lesson02_tabs,
    "lesson03_reading_data_csv_excel.html": lesson03_tabs,
    "lesson04_selecting_columns.html": lesson04_tabs,
    "lesson05_filtering_rows.html": lesson05_tabs,
    "lesson06_creating_calculated_columns.html": lesson06_tabs,
    "lesson07_aggregations_group_by.html": lesson07_tabs,
    "lesson08_joining_data_merge.html": lesson08_tabs,
    "lesson09_handling_missing_data.html": lesson09_tabs,
    "lesson10_exporting_data.html": lesson10_tabs,
}


# ── Apply ──────────────────────────────────────────────────────────────

def main():
    updated = 0
    for filename, builder in LESSONS.items():
        path = MOD / filename
        if not path.exists():
            print(f"  ❌ {filename} — file not found")
            continue

        data = builder()
        new_section = build_section(data["subtitle"], data["tabs"])

        html_text = path.read_text(encoding="utf-8")
        new_html, count = SECTION_RE.subn(new_section, html_text)

        if count == 0:
            print(f'  ⚠️  {filename} — <section id="key-concepts"> not found')
            continue

        path.write_text(new_html, encoding="utf-8")
        print(f"  ✅ {filename} — {len(data['tabs'])} tabs")
        updated += 1

    print(f"\n  Done: {updated}/10 files updated.")


if __name__ == "__main__":
    main()
