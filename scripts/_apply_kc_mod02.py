"""
Rewrite <section id="key-concepts"> for all 6 lessons in
track_02 / mod_02_working_with_data_sources.

Uses the prompt spec from lesson-key-concepts.prompt.md.
"""

import re, pathlib, html

BASE = pathlib.Path(__file__).resolve().parent.parent
MOD = BASE / "pages" / "track_02_data_analytics" / "mod_02_working_with_data_sources"

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
        "wh_from": "from-pink-50", "wh_to": "to-rose-50", "wh_border": "border-pink-100", "wh_text": "text-pink-500",
        "code_bg": "bg-pink-100", "code_text": "text-pink-700", "code_border": "border-pink-200",
        "tip_code_bg": "bg-pink-200", "tip_code_text": "text-pink-800", "tip_code_border": "border-pink-300",
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
    return COLORS[COLOR_ORDER[idx % len(COLOR_ORDER)]]


def build_sidebar(tabs):
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
            lines.append('')
            lines.append(f'          <!-- Tab {i} — INACTIVE -->')
            lines.append(f'          <button onclick="switchKcTab({i})" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">')
            lines.append(f'            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="{tab["icon"]}"></span></span>')
            lines.append(f'            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">{tab["label"]}</span>')
            lines.append('          </button>')
    lines.append('')
    lines.append('        </div><!-- /sidebar -->')
    return "\n".join(lines)


def build_code_block(code, lang="python"):
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


def build_tip(idx, icon, text):
    c = _c(idx)
    return f'''                <div class="rounded-xl p-3 flex items-start gap-2.5 {c["tipbg"]}">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg {c["tipchip"]} shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="{icon}"></span>
                  </span>
                  <p class="text-xs text-gray-600">{text}</p>
                </div>'''


def build_header_row(idx, tab):
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


def build_rules_table(idx, title, icon, rows):
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


def build_comparison_table(idx, title, col_a, col_b, rows):
    c = _c(idx)
    lines = []
    lines.append(f'                <div class="rounded-xl overflow-hidden border {c["border"]}">')
    lines.append(f'                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r {c["wh_from"]} {c["wh_to"]} border-b {c["wh_border"]}">')
    lines.append(f'                    <span class="iconify {c["wh_text"]} text-xs" data-icon="fa6-solid:scale-balanced"></span>')
    lines.append(f'                    <p class="text-[10px] font-bold uppercase tracking-widest {c["wh_text"]}">{title}</p>')
    lines.append('                  </div>')
    lines.append('                  <table class="w-full text-xs border-collapse bg-white">')
    lines.append('                    <thead>')
    lines.append('                      <tr class="border-b border-gray-50">')
    lines.append('                        <th class="py-2 px-3 text-left font-bold text-gray-400 w-1/3"></th>')
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


def build_operators_table(idx, title, rows):
    c = _c(idx)
    lines = []
    lines.append(f'                <div class="rounded-xl overflow-hidden border {c["border"]}">')
    lines.append(f'                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r {c["wh_from"]} {c["wh_to"]} border-b {c["wh_border"]}">')
    lines.append(f'                    <span class="iconify {c["wh_text"]} text-xs" data-icon="fa6-solid:calculator"></span>')
    lines.append(f'                    <p class="text-[10px] font-bold uppercase tracking-widest {c["wh_text"]}">{title}</p>')
    lines.append('                  </div>')
    lines.append('                  <table class="w-full text-xs border-collapse bg-white">')
    lines.append('                    <thead>')
    lines.append('                      <tr class="border-b border-gray-50">')
    lines.append(f'                        <th class="py-2 px-3 text-left font-bold {c["wh_text"]} w-12">Op</th>')
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


def build_panel(idx, tab):
    c = _c(idx)
    hidden = "" if idx == 0 else " hidden"
    color_name = COLOR_ORDER[idx % len(COLOR_ORDER)]

    body_parts = []
    body_parts.append(build_header_row(idx, tab))
    body_parts.append(f'                <p class="text-xs text-gray-600 leading-relaxed">{tab["definition"]}</p>')
    if tab.get("code_first"):
        body_parts.append(build_code_block(tab["code"], tab.get("lang", "python")))
        body_parts.append(tab["widget_html"])
    else:
        body_parts.append(tab["widget_html"])
        body_parts.append(build_code_block(tab["code"], tab.get("lang", "python")))
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


def build_section(subtitle, tabs):
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


# ── Helpers for code pills ─────────────────────────────────────────────

def cp(idx, text):
    c = _c(idx)
    return f'<code class="font-mono {c["code_bg"]} {c["code_text"]} border {c["code_border"]} px-1 rounded">{text}</code>'

def tcp(idx, text):
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
        "subtitle": "read_csv(), parameters, and encoding options.",
        "tabs": [
            {
                "label": "read_csv()",
                "icon": "fa6-solid:file-csv",
                "header_subtitle": "Load comma-separated files",
                "badge_label": "function",
                "definition": f'<strong>read_csv()</strong> loads a CSV file into a DataFrame. Pass the file path as a string. It returns a table with rows and columns ready for analysis.',
                "widget_html": build_rules_table(0, "Key Parameters", "fa6-solid:sliders", [
                    (f'{cp(0,"filepath")}', 'Path to the CSV file (required)'),
                    (f'{cp(0,"sep")}', f'Column separator — default {good(",")}'),
                    (f'{cp(0,"header")}', f'Row for column names — default {good("0")}'),
                    (f'{cp(0,"encoding")}', f'Character set — try {good("latin-1")} if garbled'),
                ]),
                "code": 'df = pd.read_csv("sales.csv")                # load with defaults\ndf = pd.read_csv("data.csv", sep=";")        # semicolon separator\ndf = pd.read_csv("eu.csv", encoding="latin-1") # fix special chars',
                "tip_text": f'<strong>Open the file in a text editor first.</strong> Check whether columns are separated by commas or semicolons, then set {tcp(0,"sep")} accordingly.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Viewing Rows",
                "icon": "fa6-solid:eye",
                "header_subtitle": "Preview the first or last rows",
                "badge_label": "methods",
                "definition": f'<strong>head()</strong> shows the first five rows. <strong>tail()</strong> shows the last five. Pass a number to change how many rows appear.',
                "widget_html": build_comparison_table(1, "head() vs tail()",
                    {"label": "head()", "color_bg": "bg-violet-100", "color_text": "text-violet-700", "color_border": "border-violet-200"},
                    {"label": "tail()", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Default rows", "a": "First 5", "b": "Last 5"},
                        {"label": "Custom count", "a": f'{cp(1,"df.head(10)")}', "b": f'<code class="font-mono bg-gray-100 text-gray-800 border border-gray-200 px-1 rounded">df.tail(10)</code>'},
                        {"label": "Use for", "a": "Check column names", "b": "Check last entries"},
                    ],
                ),
                "code": 'print(df.head())       # first five rows\nprint(df.head(3))      # first three rows\nprint(df.tail())       # last five rows',
                "tip_text": f'<strong>Run {tcp(1,"head()")} right after loading.</strong> It confirms the file loaded correctly and columns look right.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Inspecting Structure",
                "icon": "fa6-solid:magnifying-glass-chart",
                "header_subtitle": "Check shape, types, and nulls",
                "badge_label": "workflow",
                "definition": f'<strong>Inspecting</strong> means checking column types, row counts, and missing values before writing any code. Use {cp(2,"info()")} and {cp(2,"shape")} immediately after loading.',
                "widget_html": build_rules_table(2, "Inspection Checklist", "fa6-solid:list-check", [
                    (f'{cp(2,"df.shape")}', 'Row and column counts as a tuple'),
                    (f'{cp(2,"df.info()")}', 'Column names, types, non-null counts'),
                    (f'{cp(2,"df.dtypes")}', 'Data type of each column'),
                    (f'{cp(2,"df.describe()")}', 'Mean, min, max for numeric columns'),
                ]),
                "code": 'print(df.shape)        # (rows, columns)\nprint(df.info())       # types and missing counts\nprint(df.describe())   # summary statistics',
                "tip_text": f'<strong>Spend 30 seconds on {tcp(2,"info()")} before coding.</strong> It reveals wrong types and missing values in one glance.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


def lesson02_tabs():
    return {
        "subtitle": "JSON structure, json.load(), and nested data.",
        "tabs": [
            {
                "label": "JSON Structure",
                "icon": "fa6-solid:brackets-curly",
                "header_subtitle": "Key-value pairs in curly braces",
                "badge_label": "format",
                "definition": '<strong>JSON</strong> (JavaScript Object Notation) stores data as key-value pairs inside curly braces. Keys are always strings in double quotes. Values can be strings, numbers, lists, or nested objects.',
                "widget_html": build_rules_table(0, "JSON Syntax Rules", "fa6-solid:list-check", [
                    ('Keys use double quotes', good('&quot;name&quot;') + ' ✓ — ' + bad('&apos;name&apos;') + ' ✗'),
                    ('Strings use double quotes', good('&quot;London&quot;') + ' ✓ — ' + bad('&apos;London&apos;') + ' ✗'),
                    ('No trailing commas', bad('[1, 2,]') + ' ✗ → ' + good('[1, 2]') + ' ✓'),
                    ('Booleans are lowercase', good('true') + ' / ' + good('false') + ' — not True/False'),
                ]),
                "code": '# JSON looks like a Python dictionary\n# {"name": "Alice", "age": 30, "active": true}\nimport json\ndata = json.loads(&apos;{"name": "Alice", "age": 30}&apos;)\nprint(data["name"])    # Alice',
                "tip_text": '<strong>JSON keys are always double-quoted.</strong> Python dictionaries allow single quotes. JSON files do not — ' + tcp(0,'&apos;name&apos;') + ' causes a parse error.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "Loading JSON Files",
                "icon": "fa6-solid:file-import",
                "header_subtitle": "Read JSON into Python",
                "badge_label": "function",
                "definition": f'<strong>json.load()</strong> reads a JSON file and converts it into a Python dictionary or list. Open the file first with {cp(1,"open()")}, then pass the file object to {cp(1,"json.load()")}.',
                "widget_html": build_comparison_table(1, "load() vs loads()",
                    {"label": "json.load()", "color_bg": "bg-violet-100", "color_text": "text-violet-700", "color_border": "border-violet-200"},
                    {"label": "json.loads()", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Input", "a": "File object", "b": "String"},
                        {"label": "Reads from", "a": "A .json file on disk", "b": "A text string in code"},
                        {"label": "Common use", "a": "Loading saved data", "b": "Parsing API responses"},
                    ],
                ),
                "code": 'import json\nwith open("data.json", "r") as f:   # open the file\n    data = json.load(f)              # parse JSON to dict\nprint(type(data))                    # &lt;class \'dict\'&gt;',
                "tip_text": f'<strong>Use {tcp(1,"with open()")} to open files.</strong> It closes the file automatically when the block ends, even if an error occurs.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Nested JSON",
                "icon": "fa6-solid:sitemap",
                "header_subtitle": "Access data inside nested objects",
                "badge_label": "technique",
                "definition": '<strong>Nested JSON</strong> means objects inside objects. You access deeper values by chaining bracket notation — one bracket per level.',
                "widget_html": build_rules_table(2, "Accessing Nested Data", "fa6-solid:layer-group", [
                    (f'Top level: {cp(2,"data[&quot;key&quot;]")}', 'Returns the nested object'),
                    (f'Two levels: {cp(2,"data[&quot;a&quot;][&quot;b&quot;]")}', 'Returns the inner value'),
                    (f'List inside: {cp(2,"data[&quot;items&quot;][0]")}', 'First item in a nested list'),
                ]),
                "code": 'data = {"user": {"name": "Alice", "scores": [85, 92]}}\nprint(data["user"]["name"])       # Alice\nprint(data["user"]["scores"][0])  # 85',
                "tip_text": f'<strong>Chain one bracket per level.</strong> If you see a KeyError, print the parent object first with {tcp(2,"print(data[&quot;user&quot;])")} to check available keys.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


def lesson03_tabs():
    return {
        "subtitle": "Connection strings, SQLAlchemy engines, and database types.",
        "tabs": [
            {
                "label": "Connection Strings",
                "icon": "fa6-solid:link",
                "header_subtitle": "Address that locates your database",
                "badge_label": "concept",
                "definition": f'A <strong>connection string</strong> is a URL that tells Python where the database is and how to log in. It follows the pattern {cp(0,"dialect://user:password@host/dbname")}.',
                "widget_html": build_rules_table(0, "Connection String Parts", "fa6-solid:puzzle-piece", [
                    (f'{cp(0,"dialect")}', 'Database type — sqlite, postgresql, mysql'),
                    (f'{cp(0,"user:password")}', 'Login credentials (omit for SQLite)'),
                    (f'{cp(0,"host")}', 'Server address — localhost or an IP'),
                    (f'{cp(0,"dbname")}', 'Name of the database'),
                ]),
                "code": '# SQLite — local file, no server needed\nconn = "sqlite:///company.db"\n# PostgreSQL — remote server\nconn = "postgresql://admin:secret@localhost/sales"',
                "tip_text": f'<strong>SQLite uses three slashes.</strong> {tcp(0,"sqlite:///file.db")} — two from the protocol, one for the local path.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "SQLAlchemy Engine",
                "icon": "fa6-solid:gear",
                "header_subtitle": "Python object that manages the connection",
                "badge_label": "object",
                "definition": f'An <strong>engine</strong> is the object SQLAlchemy uses to talk to the database. Create it once with {cp(1,"create_engine()")}, then reuse it for every query.',
                "widget_html": build_comparison_table(1, "Engine vs Connection",
                    {"label": "Engine", "color_bg": "bg-violet-100", "color_text": "text-violet-700", "color_border": "border-violet-200"},
                    {"label": "Connection", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Created by", "a": f'{cp(1,"create_engine()")}', "b": '<code class="font-mono bg-gray-100 text-gray-800 border border-gray-200 px-1 rounded">engine.connect()</code>'},
                        {"label": "Lifetime", "a": "Whole script", "b": "One query block"},
                        {"label": "Reusable", "a": tick_yes("Yes"), "b": tick_no("Close after use")},
                    ],
                ),
                "code": 'from sqlalchemy import create_engine\nengine = create_engine("sqlite:///company.db")  # create once\nprint(engine)                                    # Engine object',
                "tip_text": f'<strong>Create the engine once at the top of your script.</strong> Pass the same {tcp(1,"engine")} variable to every {tcp(1,"pd.read_sql()")} call.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Database Types",
                "icon": "fa6-solid:database",
                "header_subtitle": "SQLite, PostgreSQL, and MySQL",
                "badge_label": "reference",
                "definition": '<strong>Database types</strong> (dialects) determine the connection string format and the pip package you need. SQLite is built in. Others need a driver.',
                "widget_html": build_operators_table(2, "Common Dialects", [
                    {"op": "sqlite", "meaning": "File-based, no server", "example": "sqlite:///data.db"},
                    {"op": "postgresql", "meaning": "Enterprise, full features", "example": "postgresql://u:p@host/db"},
                    {"op": "mysql", "meaning": "Popular web database", "example": "mysql://u:p@host/db"},
                    {"op": "mssql", "meaning": "Microsoft SQL Server", "example": "mssql://u:p@host/db"},
                ]),
                "code": '# SQLite — no install needed\nengine = create_engine("sqlite:///local.db")\n# PostgreSQL — pip install psycopg2-binary\nengine = create_engine("postgresql://admin:pw@localhost/sales")',
                "tip_text": f'<strong>Start with SQLite for learning.</strong> It needs no server, no password, and no extra install. Move to PostgreSQL when you need a shared database.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


def lesson04_tabs():
    return {
        "subtitle": "pd.read_sql(), SQL strings, and parameterised queries.",
        "tabs": [
            {
                "label": "pd.read_sql()",
                "icon": "fa6-solid:play",
                "header_subtitle": "Run SQL and get a DataFrame",
                "badge_label": "function",
                "definition": f'<strong>pd.read_sql()</strong> sends a SQL query to the database and returns the results as a DataFrame. Pass two arguments: the query string and the engine.',
                "widget_html": build_rules_table(0, "Key Parameters", "fa6-solid:sliders", [
                    (f'{cp(0,"sql")}', 'The SQL query as a string'),
                    (f'{cp(0,"con")}', 'The SQLAlchemy engine'),
                    (f'{cp(0,"params")}', 'Values for parameterised queries'),
                    (f'{cp(0,"index_col")}', 'Column to use as the DataFrame index'),
                ]),
                "code": 'df = pd.read_sql("SELECT * FROM staff", engine)  # all rows\nprint(df.shape)                                    # (rows, cols)\nprint(df.head())                                   # first five',
                "tip_text": f'<strong>Always test queries with {tcp(0,"LIMIT 5")} first.</strong> A table with millions of rows will freeze your script if you fetch everything at once.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "SQL Query Strings",
                "icon": "fa6-solid:terminal",
                "header_subtitle": "Write SQL inside Python strings",
                "badge_label": "syntax",
                "definition": f'A <strong>SQL query string</strong> is a regular Python string that contains SQL commands. Use triple quotes for multi-line queries. Pandas sends it to the database unchanged.',
                "widget_html": build_comparison_table(1, "Single-line vs Multi-line",
                    {"label": "Single line", "color_bg": "bg-violet-100", "color_text": "text-violet-700", "color_border": "border-violet-200"},
                    {"label": "Triple quotes", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Best for", "a": "Short queries", "b": "Long or complex queries"},
                        {"label": "Readability", "a": "Compact", "b": "Easier to read"},
                        {"label": "Example", "a": cp(1, "&quot;SELECT ...&quot;"), "b": '<code class="font-mono bg-gray-100 text-gray-800 border border-gray-200 px-1 rounded">&quot;&quot;&quot;SELECT ...&quot;&quot;&quot;</code>'},
                    ],
                ),
                "code": 'query = """\nSELECT name, salary\nFROM staff\nWHERE salary > 50000\n"""\ndf = pd.read_sql(query, engine)  # run multi-line query',
                "tip_text": f'<strong>Use triple quotes for anything over one line.</strong> They make SQL easier to read and you can add line breaks freely.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Parameterised Queries",
                "icon": "fa6-solid:shield-halved",
                "header_subtitle": "Safe way to pass values into SQL",
                "badge_label": "security",
                "definition": f'A <strong>parameterised query</strong> uses placeholders instead of pasting values directly into the SQL string. This prevents SQL injection — a serious security risk.',
                "widget_html": build_comparison_table(2, "String Formatting vs Parameters",
                    {"label": "f-string (unsafe)", "color_bg": "bg-red-100", "color_text": "text-red-700", "color_border": "border-red-200"},
                    {"label": "params (safe)", "color_bg": "bg-green-100", "color_text": "text-green-700", "color_border": "border-green-200"},
                    [
                        {"label": "SQL injection", "a": tick_no("Vulnerable"), "b": tick_yes("Protected")},
                        {"label": "Placeholders", "a": "None — value pasted in", "b": f'{cp(2,":name")} or {cp(2,"%s")}'},
                        {"label": "Values passed via", "a": "f-string interpolation", "b": f'{cp(2,"params={}")} dict'},
                    ],
                ),
                "code": 'from sqlalchemy import text\nquery = text("SELECT * FROM staff WHERE dept = :dept")\ndf = pd.read_sql(query, engine, params={"dept": "Sales"})',
                "tip_text": f'<strong>Never paste user input into SQL with f-strings.</strong> Use {tcp(2,"params")} to pass values safely. This stops attackers from rewriting your query.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
        ],
    }


def lesson05_tabs():
    return {
        "subtitle": "to_sql(), if_exists modes, and appending data.",
        "tabs": [
            {
                "label": "to_sql()",
                "icon": "fa6-solid:upload",
                "header_subtitle": "Write a DataFrame to a database table",
                "badge_label": "method",
                "definition": f'<strong>to_sql()</strong> writes a DataFrame to a database table. Pass the table name, the engine, and {cp(0,"if_exists")} to control what happens when the table already exists.',
                "widget_html": build_rules_table(0, "Key Parameters", "fa6-solid:sliders", [
                    (f'{cp(0,"name")}', 'Target table name (required)'),
                    (f'{cp(0,"con")}', 'SQLAlchemy engine (required)'),
                    (f'{cp(0,"if_exists")}', f'{good("replace")} / {good("append")} / {good("fail")}'),
                    (f'{cp(0,"index")}', f'Write the index — default {bad("True")} (usually set False)'),
                ]),
                "code": 'df.to_sql("staff", engine,\n         if_exists="replace",   # drop and recreate\n         index=False)            # skip row numbers',
                "tip_text": f'<strong>Always set {tcp(0,"index=False")}.</strong> Without it, Pandas adds a column of row numbers that clutters the database table.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "if_exists Modes",
                "icon": "fa6-solid:toggle-on",
                "header_subtitle": "Replace, append, or fail",
                "badge_label": "parameter",
                "definition": f'<strong>if_exists</strong> controls behaviour when the target table already exists. The three modes are {cp(1,"fail")}, {cp(1,"replace")}, and {cp(1,"append")}.',
                "code_first": True,
                "widget_html": build_operators_table(1, "if_exists Options", [
                    {"op": "fail", "meaning": "Raise an error if table exists", "example": "Safe — prevents overwrite"},
                    {"op": "replace", "meaning": "Drop table, then recreate", "example": "Full refresh each run"},
                    {"op": "append", "meaning": "Add rows to existing table", "example": "Daily new data inserts"},
                ]),
                "code": '# Replace — wipe and reload\ndf.to_sql("staff", engine, if_exists="replace", index=False)\n# Append — add new rows\nnew_rows.to_sql("staff", engine, if_exists="append", index=False)',
                "tip_text": f'<strong>{tcp(1,"replace")} deletes all existing rows first.</strong> If you only want to add new records, use {tcp(1,"append")} instead.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "Appending Data",
                "icon": "fa6-solid:plus",
                "header_subtitle": "Add new rows without deleting old ones",
                "badge_label": "technique",
                "definition": f'<strong>Appending</strong> adds new rows to the bottom of an existing table. The column names and types must match the existing table. Set {cp(2,"if_exists=&quot;append&quot;")}.',
                "widget_html": build_comparison_table(2, "Replace vs Append",
                    {"label": "replace", "color_bg": "bg-blue-100", "color_text": "text-blue-700", "color_border": "border-blue-200"},
                    {"label": "append", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Old rows", "a": tick_no("Deleted"), "b": tick_yes("Kept")},
                        {"label": "New rows", "a": tick_yes("Inserted"), "b": tick_yes("Inserted")},
                        {"label": "Risk", "a": "Data loss", "b": "Duplicates"},
                        {"label": "Best for", "a": "Full reload", "b": "Incremental updates"},
                    ],
                ),
                "code": 'new_data = pd.DataFrame({"Name": ["Eve"], "Salary": [55000]})\nnew_data.to_sql("staff", engine,\n                if_exists="append",    # keep existing rows\n                index=False)',
                "tip_text": f'<strong>Check for duplicates after appending.</strong> Run {tcp(2,"pd.read_sql()")} and inspect {tcp(2,"df.duplicated().sum()")} to catch repeated rows.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


def lesson06_tabs():
    return {
        "subtitle": "Environment variables, .env files, and python-dotenv.",
        "tabs": [
            {
                "label": "Environment Variables",
                "icon": "fa6-solid:key",
                "header_subtitle": "System-level key-value settings",
                "badge_label": "concept",
                "definition": f'An <strong>environment variable</strong> is a named value stored in your operating system. Python reads them with {cp(0,"os.getenv()")}. They keep secrets out of your code.',
                "widget_html": build_rules_table(0, "Why Use Env Vars", "fa6-solid:shield-halved", [
                    ('Passwords stay out of code', f'{good("os.getenv(&quot;DB_PASS&quot;)")} ✓'),
                    ('Different values per machine', 'Dev vs production settings'),
                    ('Not committed to Git', f'{good(".gitignore")} blocks .env files'),
                ]),
                "code": 'import os\ndb_host = os.getenv("DB_HOST")         # read from system\ndb_pass = os.getenv("DB_PASS", "")     # default if missing\nprint(db_host)                          # value or None',
                "tip_text": f'<strong>Never hard-code passwords in your script.</strong> Use {tcp(0,"os.getenv()")} so credentials stay in the environment, not in your Git history.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": ".env Files",
                "icon": "fa6-solid:file-lines",
                "header_subtitle": "Store variables in a local file",
                "badge_label": "format",
                "definition": '<strong>A .env file</strong> is a plain text file that holds environment variables as key=value pairs. Each variable goes on its own line. No quotes around values unless they contain spaces.',
                "widget_html": build_rules_table(1, ".env File Rules", "fa6-solid:list-check", [
                    ('One variable per line', f'{good("DB_HOST=localhost")}'),
                    ('No spaces around {cp(1,"=")}', f'{bad("DB_HOST = localhost")} ✗'),
                    (f'Comments start with {cp(1,"#")}', f'{good("# Database settings")}'),
                    ('Add to .gitignore', f'{good(".env")} — never commit secrets'),
                ]),
                "code": '# .env file contents:\n# DB_HOST=localhost\n# DB_USER=admin\n# DB_PASS=secret123\n# DB_NAME=sales',
                "tip_text": f'<strong>Add {tcp(1,".env")} to your {tcp(1,".gitignore")} immediately.</strong> If you commit it once, the secrets are in your Git history forever.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "python-dotenv",
                "icon": "fa6-solid:plug",
                "header_subtitle": "Load .env files into Python",
                "badge_label": "library",
                "definition": f'<strong>python-dotenv</strong> reads a .env file and loads its variables into the environment. Call {cp(2,"load_dotenv()")} once at the top of your script. After that, {cp(2,"os.getenv()")} can read every variable.',
                "widget_html": build_rules_table(2, "Setup Steps", "fa6-solid:list-ol", [
                    (f'Install: {cp(2,"pip install python-dotenv")}', 'One-time setup'),
                    (f'Import: {cp(2,"from dotenv import load_dotenv")}', 'At the top of your script'),
                    (f'Call: {cp(2,"load_dotenv()")}', 'Reads .env into the environment'),
                    (f'Read: {cp(2,"os.getenv(&quot;KEY&quot;)")}', 'Access any variable'),
                ]),
                "code": 'from dotenv import load_dotenv\nimport os\nload_dotenv()                         # read .env file\ndb_host = os.getenv("DB_HOST")        # "localhost"\ndb_pass = os.getenv("DB_PASS")        # "secret123"',
                "tip_text": f'<strong>Call {tcp(2,"load_dotenv()")} before any {tcp(2,"os.getenv()")} call.</strong> If you read a variable first, it returns None because the file has not been loaded yet.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


# ── Lesson registry ───────────────────────────────────────────────────

LESSONS = {
    "lesson01_reading_csv_files.html": lesson01_tabs,
    "lesson02_working_with_json_files.html": lesson02_tabs,
    "lesson03_connecting_to_databases.html": lesson03_tabs,
    "lesson04_running_sql_in_python.html": lesson04_tabs,
    "lesson05_writing_data_back_to_a_database.html": lesson05_tabs,
    "lesson06_managing_credentials_env.html": lesson06_tabs,
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

    print(f"\n  Done: {updated}/6 files updated.")


if __name__ == "__main__":
    main()
