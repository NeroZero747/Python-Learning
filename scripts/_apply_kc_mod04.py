"""
Rewrite <section id="key-concepts"> for all 6 lessons in
track_02 / mod_04_handling_large_data.

Uses the prompt spec from lesson-key-concepts.prompt.md.
"""

import re, pathlib, html

BASE = pathlib.Path(__file__).resolve().parent.parent
MOD = BASE / "pages" / "track_02_data_analytics" / "mod_04_handling_large_data"

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
    return f'<span class="text-green-500 font-bold">\u2713</span>{t}'

def tick_no(label=""):
    t = f' <span class="text-gray-400">{label}</span>' if label else ''
    return f'<span class="text-red-400 font-bold">\u2717</span>{t}'


# ── Lesson content ─────────────────────────────────────────────────────

# ── Lesson 02 — Memory Optimization ───────────────────────────────────

def lesson02_tabs():
    return {
        "subtitle": "memory_usage(), data types, downcasting, and the category dtype.",
        "tabs": [
            {
                "label": "memory_usage()",
                "icon": "fa6-solid:memory",
                "header_subtitle": "Check how much RAM a DataFrame uses",
                "badge_label": "method",
                "definition": f'<strong>memory_usage()</strong> shows how many bytes each column uses. Add {cp(0,"deep=True")} to count the actual memory of string columns.',
                "widget_html": build_rules_table(0, "Key Parameters", "fa6-solid:sliders", [
                    ('No arguments', 'Approximate sizes (fast)'),
                    (f'{cp(0,"deep=True")}', 'Exact sizes \u2014 counts string content'),
                    (f'{cp(0,".sum()")}', 'Total bytes across all columns'),
                    (f'{cp(0,"/ 1e6")}', 'Convert bytes to megabytes'),
                ]),
                "code": 'print(df.memory_usage(deep=True))              # bytes per column\ntotal_mb = df.memory_usage(deep=True).sum() / 1e6\nprint(f"Total: {total_mb:.1f} MB")             # human-readable',
                "tip_text": f'<strong>Always pass {tcp(0,"deep=True")} for DataFrames with text columns.</strong> Without it, pandas reports the pointer size, not the actual string content.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Data Types",
                "icon": "fa6-solid:shapes",
                "header_subtitle": "How pandas stores each column",
                "badge_label": "concept",
                "definition": f'Every column has a <strong>data type</strong> (dtype) that controls memory usage. An {cp(1,"int64")} column uses 8 bytes per value. An {cp(1,"int8")} uses only 1 byte \u2014 eight times less.',
                "widget_html": build_operators_table(1, "Common Pandas dtypes", [
                    {"op": "int64", "meaning": "Default integer \u2014 8 bytes", "example": "df[&quot;id&quot;].dtype"},
                    {"op": "int32", "meaning": "Smaller integer \u2014 4 bytes", "example": "df[&quot;age&quot;].astype(&quot;int32&quot;)"},
                    {"op": "float64", "meaning": "Default decimal \u2014 8 bytes", "example": "df[&quot;price&quot;].dtype"},
                    {"op": "category", "meaning": "Repeated strings \u2014 very compact", "example": "df[&quot;status&quot;].astype(&quot;category&quot;)"},
                ]),
                "code": 'print(df.dtypes)                               # current types\nprint(df["age"].dtype)                         # int64\ndf["age"] = df["age"].astype("int8")           # downcast to 1 byte',
                "tip_text": f'<strong>Check {tcp(1,"df.dtypes")} right after loading.</strong> Pandas often assigns int64 to columns that only hold small numbers like ages or quantities.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Downcasting",
                "icon": "fa6-solid:compress",
                "header_subtitle": "Switch to a smaller numeric type",
                "badge_label": "technique",
                "definition": f'<strong>Downcasting</strong> means converting a column from a large type like {cp(2,"int64")} to a smaller one like {cp(2,"int16")} or {cp(2,"int8")}. Use {cp(2,"pd.to_numeric()")} with downcast to let pandas pick the smallest safe type.',
                "widget_html": build_comparison_table(2, "Before vs After Downcast",
                    {"label": "int64 (before)", "color_bg": "bg-red-100", "color_text": "text-red-700", "color_border": "border-red-200"},
                    {"label": "int8 (after)", "color_bg": "bg-green-100", "color_text": "text-green-700", "color_border": "border-green-200"},
                    [
                        {"label": "Bytes per value", "a": "8", "b": "1"},
                        {"label": "Max value", "a": "9.2 quintillion", "b": "127"},
                        {"label": "1M rows", "a": "8 MB", "b": "1 MB"},
                        {"label": "When safe", "a": "Always", "b": "Values fit in range"},
                    ],
                ),
                "code": 'df["qty"] = pd.to_numeric(df["qty"], downcast="integer")\ndf["age"] = df["age"].astype("int8")           # max 127\ndf["year"] = df["year"].astype("int16")        # max 32,767',
                "tip_text": f'<strong>Check the column max value before downcasting.</strong> Run {tcp(2,"df[&quot;col&quot;].max()")} \u2014 if the maximum is 150, int8 (max 127) is too small.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "Category dtype",
                "icon": "fa6-solid:tags",
                "header_subtitle": "Efficient storage for repeated text",
                "badge_label": "dtype",
                "definition": 'The <strong>category</strong> dtype stores repeated string values as integer codes with a lookup table. A column with 1 million rows but only 5 unique values drops from hundreds of megabytes to under 1 MB.',
                "widget_html": build_comparison_table(3, "object vs category",
                    {"label": "object (string)", "color_bg": "bg-emerald-100", "color_text": "text-emerald-700", "color_border": "border-emerald-200"},
                    {"label": "category", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Storage", "a": "Full text per row", "b": "Integer code + lookup"},
                        {"label": "Memory", "a": tick_no("High for repeats"), "b": tick_yes("Very low")},
                        {"label": "Best for", "a": "Unique text (names)", "b": "Repeated labels (region)"},
                        {"label": "Convert", "a": "Default type", "b": f'{cp(3,"astype(&quot;category&quot;)")}'},
                    ],
                ),
                "code": 'print(df["region"].memory_usage(deep=True))    # before: large\ndf["region"] = df["region"].astype("category") # convert\nprint(df["region"].memory_usage(deep=True))    # after: much smaller',
                "tip_text": '<strong>Use category for columns with fewer than 50 unique values.</strong> Columns like "status", "region", or "department" are ideal candidates.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


# ── Lesson 03 — Chunk Processing ──────────────────────────────────────

def lesson03_tabs():
    return {
        "subtitle": "chunksize parameter, chunk iterators, and aggregating results.",
        "tabs": [
            {
                "label": "chunksize Parameter",
                "icon": "fa6-solid:puzzle-piece",
                "header_subtitle": "Load data in small batches",
                "badge_label": "parameter",
                "definition": f'The <strong>chunksize</strong> parameter tells {cp(0,"pd.read_csv()")} to load the file in batches instead of all at once. Each batch is a DataFrame with that many rows.',
                "widget_html": build_rules_table(0, "How chunksize Works", "fa6-solid:gears", [
                    (f'{cp(0,"chunksize=10000")}', 'Load 10,000 rows at a time'),
                    ('Returns', 'A TextFileReader iterator, not a DataFrame'),
                    ('Each chunk', 'A regular DataFrame you can process'),
                    ('Memory', 'Only one chunk lives in RAM at a time'),
                ]),
                "code": 'reader = pd.read_csv("big.csv", chunksize=10000)\nfor chunk in reader:                           # one chunk at a time\n    print(chunk.shape)                         # (10000, 8)',
                "tip_text": f'<strong>Start with {tcp(0,"chunksize=10000")} and adjust.</strong> Smaller chunks use less memory but run more loops. Larger chunks are faster but need more RAM.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Chunk Iterator",
                "icon": "fa6-solid:arrows-spin",
                "header_subtitle": "Loop through chunks one by one",
                "badge_label": "concept",
                "definition": f'A <strong>chunk iterator</strong> is the object returned by {cp(1,"read_csv(chunksize=N)")}. It yields one DataFrame per iteration. You cannot go backwards \u2014 each chunk is read once and then discarded.',
                "widget_html": build_comparison_table(1, "Full Load vs Chunk Iterator",
                    {"label": "Full load", "color_bg": "bg-violet-100", "color_text": "text-violet-700", "color_border": "border-violet-200"},
                    {"label": "Chunked", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Returns", "a": "One DataFrame", "b": "An iterator of DataFrames"},
                        {"label": "Memory", "a": tick_no("Entire file in RAM"), "b": tick_yes("One chunk in RAM")},
                        {"label": "Access", "a": "Random (any row)", "b": "Sequential (forward only)"},
                        {"label": "Best for", "a": "Small \u2013 medium files", "b": "Files larger than RAM"},
                    ],
                ),
                "code": 'reader = pd.read_csv("big.csv", chunksize=50000)\nfor i, chunk in enumerate(reader):             # numbered chunks\n    print(f"Chunk {i}: {len(chunk)} rows")     # progress',
                "tip_text": '<strong>You cannot rewind a chunk iterator.</strong> Once you loop through it, the data is gone. If you need to iterate twice, open a new reader.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "Aggregating Chunks",
                "icon": "fa6-solid:calculator",
                "header_subtitle": "Combine results from all chunks",
                "badge_label": "technique",
                "definition": '<strong>Aggregating chunks</strong> means computing a result across the entire file by accumulating values from each chunk. Collect partial results in a running total, then read the final value after the loop.',
                "widget_html": build_rules_table(2, "Aggregation Strategies", "fa6-solid:list-check", [
                    ('Sum', 'Keep a running total across chunks'),
                    ('Count', 'Increment a counter per chunk'),
                    ('Collect', 'Append filtered rows to a list'),
                    ('GroupBy', 'Concat partial results, groupby once at end'),
                ]),
                "code": 'total = 0                                      # running total\nreader = pd.read_csv("big.csv", chunksize=10000)\nfor chunk in reader:                           # loop all chunks\n    total += chunk["sales"].sum()              # accumulate\nprint(f"Grand total: {total}")                 # final result',
                "tip_text": '<strong>For grouped aggregations, collect partial results and concat at the end.</strong> Do not call groupby() inside the loop \u2014 it creates incomplete groups.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "When to Use Chunks",
                "icon": "fa6-solid:circle-question",
                "header_subtitle": "Decide whether chunking is necessary",
                "badge_label": "guideline",
                "definition": '<strong>Use chunk processing</strong> when a file is too large to fit in memory. If read_csv() raises a MemoryError or your system freezes, switch to chunked reading. For files under 500 MB, full loading is usually fine.',
                "widget_html": build_comparison_table(3, "Full Load vs Chunked",
                    {"label": "Full load", "color_bg": "bg-emerald-100", "color_text": "text-emerald-700", "color_border": "border-emerald-200"},
                    {"label": "Chunked", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "File size", "a": "Under 500 MB", "b": "Over 500 MB"},
                        {"label": "Speed", "a": tick_yes("Faster (single read)"), "b": tick_no("Slower (loop)")},
                        {"label": "Complexity", "a": tick_yes("Simple code"), "b": tick_no("More complex")},
                        {"label": "Memory safety", "a": tick_no("May crash"), "b": tick_yes("Always safe")},
                    ],
                ),
                "code": 'import os\nsize_mb = os.path.getsize("data.csv") / 1e6    # file size in MB\nif size_mb > 500:                              # large file\n    reader = pd.read_csv("data.csv", chunksize=50000)\nelse:\n    df = pd.read_csv("data.csv")               # load normally',
                "tip_text": '<strong>Check your available RAM before deciding.</strong> A 2 GB file fits in memory on a 16 GB machine but crashes on a 4 GB machine.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


# ── Lesson 04 — Processing Millions of Rows ──────────────────────────

def lesson04_tabs():
    return {
        "subtitle": "Vectorised operations, early filtering, avoiding copies, and method chaining.",
        "tabs": [
            {
                "label": "Vectorised Operations",
                "icon": "fa6-solid:bolt",
                "header_subtitle": "Apply operations to entire columns at once",
                "badge_label": "technique",
                "definition": 'A <strong>vectorised operation</strong> applies a calculation to every value in a column in one step, without a loop. Pandas does the looping internally in compiled C code, which is far faster than a Python for loop.',
                "widget_html": build_comparison_table(0, "Loop vs Vectorised",
                    {"label": "for loop", "color_bg": "bg-red-100", "color_text": "text-red-700", "color_border": "border-red-200"},
                    {"label": "Vectorised", "color_bg": "bg-green-100", "color_text": "text-green-700", "color_border": "border-green-200"},
                    [
                        {"label": "Code", "a": "for i in range(len(df)):", "b": f'{cp(0,"df[&quot;x&quot;] = df[&quot;a&quot;] * 2")}'},
                        {"label": "Speed", "a": tick_no("Seconds to minutes"), "b": tick_yes("Milliseconds")},
                        {"label": "Lines", "a": "3+ lines", "b": "1 line"},
                        {"label": "When", "a": "Complex custom logic", "b": "Standard math and comparisons"},
                    ],
                ),
                "code": '# Slow \u2014 Python loop\n# for i in range(len(df)):\n#     df.loc[i,"total"] = df.loc[i,"qty"] * df.loc[i,"price"]\n# Fast \u2014 vectorised\ndf["total"] = df["qty"] * df["price"]          # all rows at once',
                "tip_text": '<strong>If you write a for loop over DataFrame rows, stop and look for a vectorised alternative.</strong> Pandas has built-in methods for almost every common operation.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Early Filtering",
                "icon": "fa6-solid:filter",
                "header_subtitle": "Remove rows before processing",
                "badge_label": "technique",
                "definition": '<strong>Early filtering</strong> means dropping unwanted rows as soon as possible after loading. Fewer rows means every later operation \u2014 groupby, merge, export \u2014 runs faster and uses less memory.',
                "widget_html": build_rules_table(1, "Filtering Strategies", "fa6-solid:list-check", [
                    (f'{cp(1,"usecols=[...]")}', 'Skip unwanted columns at load time'),
                    (f'{cp(1,"df[condition]")}', 'Drop rows by value after loading'),
                    (f'{cp(1,"df.dropna()")}', 'Remove rows with missing values'),
                    (f'{cp(1,"df[date >= ...]")}', 'Limit to a date range'),
                ]),
                "code": 'df = pd.read_csv("orders.csv")                 # load data\ndf = df[df["status"] == "completed"]            # keep completed\ndf = df[df["date"] >= "2024-01-01"]             # recent only\nprint(f"Kept {len(df)} rows")                   # check reduction',
                "tip_text": '<strong>Filter before groupby or merge.</strong> A groupby on 1 million rows is much faster than on 10 million rows. Remove what you do not need first.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Avoiding Copies",
                "icon": "fa6-solid:clone",
                "header_subtitle": "Reduce memory by not duplicating data",
                "badge_label": "technique",
                "definition": '<strong>Avoiding copies</strong> means modifying data in place instead of creating new DataFrames. Every new assignment duplicates memory. On large datasets this can double your RAM usage.',
                "widget_html": build_comparison_table(2, "Copy vs In-Place",
                    {"label": "Creates copy", "color_bg": "bg-red-100", "color_text": "text-red-700", "color_border": "border-red-200"},
                    {"label": "In place", "color_bg": "bg-green-100", "color_text": "text-green-700", "color_border": "border-green-200"},
                    [
                        {"label": "Memory", "a": tick_no("2\u00d7 original"), "b": tick_yes("Same as original")},
                        {"label": "Original", "a": "Unchanged", "b": "Modified"},
                        {"label": "Safety", "a": tick_yes("Can undo"), "b": tick_no("Cannot undo")},
                        {"label": "When", "a": "Need both versions", "b": "Only need final result"},
                    ],
                ),
                "code": '# Creates a copy \u2014 uses extra memory\n# df_clean = df[df["status"] == "active"].copy()\n# Modifies in place \u2014 saves memory\ndf.drop(columns=["temp_col"], inplace=True)    # remove column\ndf.reset_index(drop=True, inplace=True)        # reset index',
                "tip_text": f'<strong>Use {tcp(2,"inplace=True")} only when you are certain you do not need the original data.</strong> It saves memory but the change cannot be undone.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "Method Chaining",
                "icon": "fa6-solid:link",
                "header_subtitle": "Combine operations in one statement",
                "badge_label": "pattern",
                "definition": '<strong>Method chaining</strong> connects multiple pandas operations with dots in a single statement. Each method returns a DataFrame, so you can call the next method on the result without intermediate variables.',
                "widget_html": build_comparison_table(3, "Separate Steps vs Chain",
                    {"label": "Separate variables", "color_bg": "bg-emerald-100", "color_text": "text-emerald-700", "color_border": "border-emerald-200"},
                    {"label": "Chained", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Variables", "a": "3+ temporary names", "b": "1 final name"},
                        {"label": "Memory", "a": tick_no("Stores each step"), "b": tick_yes("Only final result")},
                        {"label": "Readability", "a": "Easy to debug", "b": "Compact and clean"},
                        {"label": "Best for", "a": "Learning and debugging", "b": "Production scripts"},
                    ],
                ),
                "code": 'result = (\n    df.dropna(subset=["sales"])                 # remove nulls\n    .query("sales > 0")                         # filter positives\n    .groupby("region")["sales"].sum()           # aggregate\n    .reset_index()                               # flatten\n)',
                "tip_text": '<strong>Wrap the chain in parentheses.</strong> This lets you break it across multiple lines. Without parentheses, Python requires backslashes at the end of each line.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


# ── Lesson 05 — Columnar Storage ─────────────────────────────────────

def lesson05_tabs():
    return {
        "subtitle": "Row-based vs column-based storage, compression, and column pruning.",
        "tabs": [
            {
                "label": "Row-Based Storage",
                "icon": "fa6-solid:table-list",
                "header_subtitle": "Traditional format \u2014 one row at a time",
                "badge_label": "concept",
                "definition": '<strong>Row-based storage</strong> saves data one complete row at a time. CSV and traditional databases use this format. Reading a single row is fast, but reading a single column means scanning every row.',
                "widget_html": build_rules_table(0, "Row-Based Characteristics", "fa6-solid:list-check", [
                    ('Layout', 'All columns of row 1, then all columns of row 2\u2026'),
                    ('Read one row', tick_yes("Fast \u2014 data is contiguous")),
                    ('Read one column', tick_no("Slow \u2014 must skip every row")),
                    ('Compression', tick_no("Poor \u2014 mixed types per row")),
                ]),
                "code": '# CSV is row-based \u2014 stores one row per line\n# name,age,city\n# Alice,30,London\n# Bob,25,Paris\ndf = pd.read_csv("people.csv")                 # reads every column',
                "tip_text": '<strong>CSV is fine for small files.</strong> The performance difference only matters when files exceed hundreds of megabytes.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Column-Based Storage",
                "icon": "fa6-solid:table-columns",
                "header_subtitle": "Modern format \u2014 one column at a time",
                "badge_label": "concept",
                "definition": '<strong>Column-based storage</strong> (columnar) saves all values of one column together, then all values of the next column. Reading a single column is extremely fast because the data is contiguous on disk.',
                "widget_html": build_comparison_table(1, "Row-Based vs Columnar",
                    {"label": "Row-based (CSV)", "color_bg": "bg-violet-100", "color_text": "text-violet-700", "color_border": "border-violet-200"},
                    {"label": "Columnar (Parquet)", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Layout", "a": "Row by row", "b": "Column by column"},
                        {"label": "Read 1 column", "a": tick_no("Scans entire file"), "b": tick_yes("Reads only that column")},
                        {"label": "Compression", "a": tick_no("Low"), "b": tick_yes("High \u2014 same-type values")},
                        {"label": "Best for", "a": "Row-level lookups", "b": "Analytical queries"},
                    ],
                ),
                "code": '# Columnar layout (conceptual):\n# name: [Alice, Bob, Carol, ...]\n# age:  [30, 25, 28, ...]\n# city: [London, Paris, Berlin, ...]\ndf = pd.read_parquet("people.parquet", columns=["name"])',
                "tip_text": '<strong>Most analyst work reads a few columns from many rows.</strong> Columnar storage is built for exactly this access pattern.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Column Pruning",
                "icon": "fa6-solid:scissors",
                "header_subtitle": "Load only the columns you need",
                "badge_label": "technique",
                "definition": f'<strong>Column pruning</strong> means reading only the columns you need from a file. In columnar formats like Parquet, unselected columns are never read from disk. Use the {cp(2,"columns")} parameter.',
                "widget_html": build_comparison_table(2, "All Columns vs Pruned",
                    {"label": "All columns", "color_bg": "bg-red-100", "color_text": "text-red-700", "color_border": "border-red-200"},
                    {"label": "Pruned", "color_bg": "bg-green-100", "color_text": "text-green-700", "color_border": "border-green-200"},
                    [
                        {"label": "Disk reads", "a": tick_no("Entire file"), "b": tick_yes("Selected columns only")},
                        {"label": "Memory", "a": tick_no("All columns in RAM"), "b": tick_yes("Only needed columns")},
                        {"label": "Speed", "a": "Slower", "b": "Much faster"},
                    ],
                ),
                "code": '# Load everything \u2014 slow and wasteful\n# df = pd.read_parquet("big.parquet")\n# Prune to two columns \u2014 fast\ndf = pd.read_parquet("big.parquet", columns=["name", "sales"])',
                "tip_text": f'<strong>Always pass the {tcp(2,"columns")} parameter when reading Parquet files.</strong> If you only need 3 out of 50 columns, you skip 94% of the data.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Compression",
                "icon": "fa6-solid:file-zipper",
                "header_subtitle": "Shrink file size without losing data",
                "badge_label": "feature",
                "definition": '<strong>Compression</strong> reduces file size by encoding patterns in the data. Columnar formats compress much better than CSV because values in the same column share a type. A 3 GB CSV might shrink to 300 MB as Parquet.',
                "widget_html": build_comparison_table(3, "CSV vs Parquet Size",
                    {"label": "CSV (uncompressed)", "color_bg": "bg-emerald-100", "color_text": "text-emerald-700", "color_border": "border-emerald-200"},
                    {"label": "Parquet (snappy)", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "1M rows, 10 cols", "a": "~400 MB", "b": "~40 MB"},
                        {"label": "Compression ratio", "a": "1\u00d7", "b": "5\u201310\u00d7 smaller"},
                        {"label": "Read speed", "a": tick_no("Slower (parse text)"), "b": tick_yes("Faster (binary)")},
                    ],
                ),
                "code": 'df.to_parquet("data.parquet")                   # default snappy\ndf.to_parquet("data.gz.parquet", compression="gzip")  # max compression\nprint(os.path.getsize("data.parquet") / 1e6, "MB")    # check size',
                "tip_text": '<strong>Use the default snappy compression for most cases.</strong> It balances speed and size well. Switch to gzip only when you need the smallest possible file.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


# ── Lesson 06 — Parquet Files ────────────────────────────────────────

def lesson06_tabs():
    return {
        "subtitle": "to_parquet(), read_parquet(), column selection, and partitioning.",
        "tabs": [
            {
                "label": "to_parquet()",
                "icon": "fa6-solid:file-arrow-up",
                "header_subtitle": "Save a DataFrame as a Parquet file",
                "badge_label": "method",
                "definition": '<strong>to_parquet()</strong> writes a DataFrame to a Parquet file. It preserves column types and compresses the data automatically. The file is typically 5\u201310 times smaller than a CSV.',
                "widget_html": build_rules_table(0, "Key Parameters", "fa6-solid:sliders", [
                    (f'{cp(0,"path")}', 'Output file path (required)'),
                    (f'{cp(0,"compression")}', '"snappy" (default), "gzip", or "brotli"'),
                    (f'{cp(0,"index")}', 'Write the DataFrame index \u2014 default True'),
                    (f'{cp(0,"engine")}', '"pyarrow" (default) or "fastparquet"'),
                ]),
                "code": 'df.to_parquet("sales.parquet")                  # save with defaults\ndf.to_parquet("sales.parquet", index=False)     # skip index\ndf.to_parquet("archive.parquet", compression="gzip")',
                "tip_text": f'<strong>Install pyarrow first.</strong> Run {tcp(0,"pip install pyarrow")} \u2014 pandas needs it to read and write Parquet files.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "read_parquet()",
                "icon": "fa6-solid:file-arrow-down",
                "header_subtitle": "Load a Parquet file into a DataFrame",
                "badge_label": "function",
                "definition": f'<strong>pd.read_parquet()</strong> loads a Parquet file into a DataFrame. It reads column types automatically \u2014 no need to set {cp(1,"dtype")} or parse dates.',
                "widget_html": build_rules_table(1, "Key Parameters", "fa6-solid:sliders", [
                    (f'{cp(1,"path")}', 'File path or URL (required)'),
                    (f'{cp(1,"columns")}', 'List of column names to load'),
                    (f'{cp(1,"engine")}', '"pyarrow" (default) or "fastparquet"'),
                    (f'{cp(1,"filters")}', 'Row-level filter (partitioned files only)'),
                ]),
                "code": 'df = pd.read_parquet("sales.parquet")            # all columns\ndf = pd.read_parquet("sales.parquet", columns=["name", "total"])\nprint(df.dtypes)                                # types preserved',
                "tip_text": '<strong>Parquet preserves data types.</strong> Unlike CSV, dates load as datetime and numbers load as the correct int/float type. No manual astype() needed.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Column Selection",
                "icon": "fa6-solid:table-columns",
                "header_subtitle": "Read only the columns you need",
                "badge_label": "technique",
                "definition": f'<strong>Column selection</strong> in Parquet means the file only reads data for the columns you specify. Unselected columns are never loaded into memory. Use the {cp(2,"columns")} parameter.',
                "widget_html": build_comparison_table(2, "CSV usecols vs Parquet columns",
                    {"label": "CSV usecols", "color_bg": "bg-blue-100", "color_text": "text-blue-700", "color_border": "border-blue-200"},
                    {"label": "Parquet columns", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Reads disk", "a": tick_no("Entire file"), "b": tick_yes("Only selected columns")},
                        {"label": "Parsing", "a": "Scans all text", "b": "Skips unneeded columns"},
                        {"label": "Speed gain", "a": "Small", "b": "Large \u2014 proportional to skipped cols"},
                    ],
                ),
                "code": '# CSV \u2014 reads entire file, then drops columns\ndf = pd.read_csv("big.csv", usecols=["name", "sales"])\n# Parquet \u2014 only reads the two columns from disk\ndf = pd.read_parquet("big.parquet", columns=["name", "sales"])',
                "tip_text": f'<strong>Always pass {tcp(2,"columns=[...]")} when reading Parquet.</strong> If your table has 100 columns and you need 3, you skip 97% of the I/O.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Partitioning",
                "icon": "fa6-solid:folder-tree",
                "header_subtitle": "Split a Parquet file by column values",
                "badge_label": "feature",
                "definition": f'<strong>Partitioning</strong> splits a Parquet dataset into subfolders based on a column. Each unique value gets its own folder. When you filter by that column, pandas reads only the matching folder.',
                "widget_html": build_rules_table(3, "Partitioning Behaviour", "fa6-solid:folder-open", [
                    (f'{cp(3,"partition_cols=[&quot;year&quot;]")}', 'Creates /year=2023/, /year=2024/ folders'),
                    ('Read with filter', 'Only reads matching partitions'),
                    ('Best for', 'Date-based or category-based splits'),
                    ('Trade-off', 'Many small files instead of one large file'),
                ]),
                "code": 'df.to_parquet("data/", partition_cols=["year"]) # split by year\ndf = pd.read_parquet("data/",\n    filters=[("year", "==", 2024)])              # read only 2024',
                "tip_text": '<strong>Partition by columns you filter on most often.</strong> If every query filters by year, partition by year. Avoid partitioning by columns with thousands of unique values.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


# ── Lesson 13 — Performance Profiling ────────────────────────────────

def lesson13_tabs():
    return {
        "subtitle": "timeit, cProfile, line_profiler, and bottleneck patterns.",
        "tabs": [
            {
                "label": "timeit",
                "icon": "fa6-solid:stopwatch",
                "header_subtitle": "Measure how long code takes to run",
                "badge_label": "tool",
                "definition": f'<strong>timeit</strong> runs a code snippet many times and reports the average execution time. It is ideal for comparing two approaches. Use the {cp(0,"timeit")} module in scripts or the {cp(0,"%%timeit")} magic in Jupyter.',
                "widget_html": build_comparison_table(0, "timeit vs Manual Timing",
                    {"label": "timeit", "color_bg": "bg-pink-100", "color_text": "text-pink-700", "color_border": "border-pink-200"},
                    {"label": "time.time()", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Accuracy", "a": tick_yes("Runs many iterations"), "b": tick_no("Single measurement")},
                        {"label": "Setup", "a": "Automatic warmup", "b": "Manual start/stop"},
                        {"label": "Output", "a": "Mean \u00b1 std deviation", "b": "Single number"},
                        {"label": "Best for", "a": "Comparing two approaches", "b": "Quick checks"},
                    ],
                ),
                "code": 'import timeit\nt = timeit.timeit(\n    "df.groupby(\'region\').sum()",            # code to measure\n    globals=globals(), number=100)            # run 100 times\nprint(f"Average: {t/100:.4f}s per run")       # mean time',
                "tip_text": '<strong>Run at least 100 iterations for stable results.</strong> A single measurement changes every time due to system load.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "cProfile",
                "icon": "fa6-solid:chart-line",
                "header_subtitle": "Profile a script function by function",
                "badge_label": "module",
                "definition": '<strong>cProfile</strong> measures how many times each function is called and how long it takes. Run it on your main function to find which step consumes the most time.',
                "widget_html": build_operators_table(1, "cProfile Output Columns", [
                    {"op": "ncalls", "meaning": "Times the function was called", "example": "150"},
                    {"op": "tottime", "meaning": "Time in that function only", "example": "0.42s"},
                    {"op": "cumtime", "meaning": "Time including sub-calls", "example": "1.35s"},
                    {"op": "filename", "meaning": "Where the function is defined", "example": "script.py:12"},
                ]),
                "code": 'import cProfile\ndef process():                                  # function to profile\n    df = pd.read_csv("big.csv")                 # slow step?\n    return df.groupby("region").sum()            # or this one?\ncProfile.run("process()")                        # show breakdown',
                "tip_text": '<strong>Sort results by cumulative time.</strong> Add <em>sort="cumulative"</em> to see the slowest functions first.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "line_profiler",
                "icon": "fa6-solid:magnifying-glass",
                "header_subtitle": "Measure time spent on each line",
                "badge_label": "tool",
                "definition": '<strong>line_profiler</strong> shows how long each individual line of a function takes. It is more detailed than cProfile \u2014 you see exactly which line is the bottleneck.',
                "widget_html": build_comparison_table(2, "cProfile vs line_profiler",
                    {"label": "cProfile", "color_bg": "bg-blue-100", "color_text": "text-blue-700", "color_border": "border-blue-200"},
                    {"label": "line_profiler", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Granularity", "a": "Function level", "b": "Line level"},
                        {"label": "Built in", "a": tick_yes("Yes"), "b": tick_no("pip install line_profiler")},
                        {"label": "Use for", "a": "Finding slow functions", "b": "Finding slow lines"},
                    ],
                ),
                "code": 'from line_profiler import profile               # pip install\n@profile                                        # mark function\ndef transform(df):                              # function to profile\n    df = df.dropna()                            # how long?\n    df["total"] = df["qty"] * df["price"]       # and this?\n    return df',
                "tip_text": '<strong>Profile only the function you suspect is slow.</strong> Adding @profile to every function creates noisy output and hides the real bottleneck.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Bottleneck Patterns",
                "icon": "fa6-solid:bug",
                "header_subtitle": "Common causes of slow data scripts",
                "badge_label": "reference",
                "definition": 'A <strong>bottleneck</strong> is the single step that takes the longest. Most slow scripts have one bottleneck, not many. Fixing it often makes the entire script 10\u00d7 faster.',
                "widget_html": build_rules_table(3, "Common Bottlenecks", "fa6-solid:triangle-exclamation", [
                    ('Python for loops over rows', 'Replace with vectorised operations'),
                    ('Loading unused columns', 'Use usecols= or columns= parameters'),
                    ('String operations with apply()', 'Use the .str accessor instead'),
                    ('Repeated file reads', 'Load once and reuse the DataFrame'),
                ]),
                "code": '# Bottleneck: loop over rows\n# for i in range(len(df)): df.loc[i,"x"] = df.loc[i,"a"]*2\n# Fix: vectorised operation\ndf["x"] = df["a"] * 2                          # 100\u00d7 faster',
                "tip_text": '<strong>Fix the biggest bottleneck first.</strong> If loading takes 30 seconds and processing takes 2 seconds, optimising the processing step wastes your time.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


# ── Lesson registry ───────────────────────────────────────────────────

LESSONS = {
    "lesson02_memory_optimization.html": lesson02_tabs,
    "lesson03_chunk_processing.html": lesson03_tabs,
    "lesson04_processing_millions_of_rows.html": lesson04_tabs,
    "lesson05_columnar_storage.html": lesson05_tabs,
    "lesson06_parquet_files.html": lesson06_tabs,
    "lesson13_performance_profiling.html": lesson13_tabs,
}


# ── Apply ──────────────────────────────────────────────────────────────

def main():
    updated = 0
    for filename, builder in LESSONS.items():
        path = MOD / filename
        if not path.exists():
            print(f"  \u274c {filename} \u2014 file not found")
            continue

        data = builder()
        new_section = build_section(data["subtitle"], data["tabs"])

        html_text = path.read_text(encoding="utf-8")
        new_html, count = SECTION_RE.subn(new_section, html_text)

        if count == 0:
            print(f'  \u26a0\ufe0f  {filename} \u2014 <section id="key-concepts"> not found')
            continue

        path.write_text(new_html, encoding="utf-8")
        print(f"  \u2705 {filename} \u2014 {len(data['tabs'])} tabs")
        updated += 1

    print(f"\n  Done: {updated}/6 files updated.")


if __name__ == "__main__":
    main()
