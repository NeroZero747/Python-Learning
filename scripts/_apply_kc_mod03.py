"""
Rewrite <section id="key-concepts"> for all 6 lessons in
track_02 / mod_03_python_for_analysts.

Uses the prompt spec from lesson-key-concepts.prompt.md.
"""

import re, pathlib, html

BASE = pathlib.Path(__file__).resolve().parent.parent
MOD = BASE / "pages" / "track_02_data_analytics" / "mod_03_python_for_analysts"

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

# ── Lesson 01 — Why Analysts Use Python ────────────────────────────────

def lesson01_tabs():
    return {
        "subtitle": "Automation, reproducibility, scalability, and the library ecosystem.",
        "tabs": [
            {
                "label": "Automation",
                "icon": "fa6-solid:robot",
                "header_subtitle": "Let code do the repetitive work",
                "badge_label": "concept",
                "definition": '<strong>Automation</strong> means writing a script that performs a task for you. You run it once, and it processes hundreds of files or rows without manual clicks.',
                "widget_html": build_comparison_table(0, "Manual vs Automated",
                    {"label": "Manual", "color_bg": "bg-red-100", "color_text": "text-red-700", "color_border": "border-red-200"},
                    {"label": "Automated", "color_bg": "bg-green-100", "color_text": "text-green-700", "color_border": "border-green-200"},
                    [
                        {"label": "Speed", "a": tick_no("Minutes per file"), "b": tick_yes("Seconds per file")},
                        {"label": "Errors", "a": tick_no("Risk of typos"), "b": tick_yes("Consistent every run")},
                        {"label": "Effort", "a": tick_no("Redo each time"), "b": tick_yes("Write once, rerun forever")},
                    ],
                ),
                "code": 'files = ["jan.csv", "feb.csv", "mar.csv"]  # list of reports\nfor f in files:                             # loop through each\n    df = pd.read_csv(f)                     # load the file\n    print(f, df.shape)                      # show row count',
                "tip_text": '<strong>Start with the task you repeat most often.</strong> If you copy-paste the same Excel steps every week, that task is your first automation candidate.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Reproducibility",
                "icon": "fa6-solid:rotate",
                "header_subtitle": "Rerun the same steps every time",
                "badge_label": "concept",
                "definition": '<strong>Reproducibility</strong> means anyone can rerun your script and get the same result. A Python script records every step. Manual Excel work cannot be replayed or audited.',
                "widget_html": build_comparison_table(1, "Excel vs Python Script",
                    {"label": "Excel workflow", "color_bg": "bg-red-100", "color_text": "text-red-700", "color_border": "border-red-200"},
                    {"label": "Python script", "color_bg": "bg-green-100", "color_text": "text-green-700", "color_border": "border-green-200"},
                    [
                        {"label": "Steps visible", "a": tick_no("Hidden in clicks"), "b": tick_yes("Written in code")},
                        {"label": "Rerun", "a": tick_no("Start over manually"), "b": tick_yes("Run the script again")},
                        {"label": "Audit trail", "a": tick_no("None"), "b": tick_yes("Full script history")},
                    ],
                ),
                "code": 'df = pd.read_csv("sales.csv")              # step 1: load data\ndf = df[df["amount"] > 0]                   # step 2: filter rows\ndf.to_csv("cleaned.csv", index=False)        # step 3: save result',
                "tip_text": '<strong>Save your script with a descriptive name.</strong> A file called <em>clean_sales_data.py</em> tells your future self exactly what it does.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Scalability",
                "icon": "fa6-solid:arrow-up-right-dots",
                "header_subtitle": "Handle millions of rows without crashing",
                "badge_label": "concept",
                "definition": '<strong>Scalability</strong> means your code handles large datasets the same way it handles small ones. Excel slows down above one million rows. Python processes tens of millions without crashing.',
                "widget_html": build_comparison_table(2, "Excel vs Python",
                    {"label": "Excel", "color_bg": "bg-red-100", "color_text": "text-red-700", "color_border": "border-red-200"},
                    {"label": "Python", "color_bg": "bg-green-100", "color_text": "text-green-700", "color_border": "border-green-200"},
                    [
                        {"label": "Max rows", "a": tick_no("~1,048,576"), "b": tick_yes("Limited by RAM only")},
                        {"label": "Speed", "a": tick_no("Freezes on large data"), "b": tick_yes("Optimised for speed")},
                        {"label": "Multiple files", "a": tick_no("Open each manually"), "b": tick_yes("Loop and combine")},
                    ],
                ),
                "code": 'df = pd.read_csv("big_data.csv")            # 5 million rows\nprint(df.shape)                              # (5000000, 12)\ntotal = df.memory_usage().sum() / 1e6        # memory in MB\nprint(f"Total: {total:.1f} MB")              # readable size',
                "tip_text": '<strong>If your spreadsheet takes more than 30 seconds to open,</strong> it is a sign that you need Python instead.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Library Ecosystem",
                "icon": "fa6-solid:cubes",
                "header_subtitle": "Pre-built tools for every analyst task",
                "badge_label": "concept",
                "definition": 'A <strong>library</strong> is a package of pre-built code you install and import. Python has thousands of libraries. Analysts use a small core set for data, charts, and automation.',
                "widget_html": build_operators_table(3, "Common Analyst Libraries", [
                    {"op": "pandas", "meaning": "Data loading and manipulation", "example": "import pandas as pd"},
                    {"op": "matplotlib", "meaning": "Charts and visualisations", "example": "import matplotlib.pyplot as plt"},
                    {"op": "openpyxl", "meaning": "Read and write Excel files", "example": "pip install openpyxl"},
                    {"op": "glob", "meaning": "Find files by name pattern", "example": "import glob"},
                ]),
                "code": 'df = pd.read_csv("data.csv")                # pandas: load data\ndf["total"] = df["qty"] * df["price"]       # pandas: calculate\ndf.to_excel("report.xlsx", index=False)      # openpyxl: save Excel',
                "tip_text": '<strong>Start with pandas.</strong> It covers 80% of analyst tasks. The other libraries become useful once you have your data loaded and cleaned.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


# ── Lesson 02 — Replacing Excel Workflows with Python ──────────────────

def lesson02_tabs():
    return {
        "subtitle": "read_excel(), filtering, calculations, and exporting results.",
        "tabs": [
            {
                "label": "pd.read_excel()",
                "icon": "fa6-solid:file-excel",
                "header_subtitle": "Load Excel files into a DataFrame",
                "badge_label": "function",
                "definition": f'<strong>pd.read_excel()</strong> loads an Excel workbook into a DataFrame. Pass the file path as a string. Set {cp(0,"sheet_name")} to choose which sheet to load.',
                "widget_html": build_rules_table(0, "Key Parameters", "fa6-solid:sliders", [
                    (f'{cp(0,"filepath")}', 'Path to the .xlsx file (required)'),
                    (f'{cp(0,"sheet_name")}', 'Sheet to read — default 0 (first)'),
                    (f'{cp(0,"header")}', 'Row for column names — default 0'),
                    (f'{cp(0,"usecols")}', 'Columns to load — e.g. "A:D"'),
                ]),
                "code": 'df = pd.read_excel("sales.xlsx")                 # first sheet\ndf = pd.read_excel("sales.xlsx", sheet_name=1)    # second sheet\ndf = pd.read_excel("sales.xlsx", usecols="A:D")   # columns A\u2013D',
                "tip_text": f'<strong>Install openpyxl first.</strong> Run {tcp(0,"pip install openpyxl")} before using read_excel \u2014 pandas needs it to read .xlsx files.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "Boolean Indexing",
                "icon": "fa6-solid:filter",
                "header_subtitle": "Filter rows with conditions",
                "badge_label": "technique",
                "definition": '<strong>Boolean indexing</strong> filters a DataFrame by passing a condition inside square brackets. It replaces Excel AutoFilter. The condition returns True or False for each row.',
                "widget_html": build_comparison_table(1, "Excel Filter vs Python",
                    {"label": "Excel AutoFilter", "color_bg": "bg-violet-100", "color_text": "text-violet-700", "color_border": "border-violet-200"},
                    {"label": "Python boolean index", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Filter method", "a": "Menu dropdowns", "b": f'{cp(1,"df[df[&quot;col&quot;] > val]")}'},
                        {"label": "Multiple filters", "a": "One at a time", "b": f'Combine with {cp(1,"&amp;")} or {cp(1,"|")}'},
                        {"label": "Result", "a": "Hides rows in place", "b": "Returns a new DataFrame"},
                    ],
                ),
                "code": 'big = df[df["Sales"] > 1000]                     # rows above 1000\neast = df[df["Region"] == "East"]                # exact match\nboth = df[(df["Sales"] > 1000) &amp; (df["Region"] == "East")]',
                "tip_text": '<strong>Wrap each condition in parentheses when combining.</strong> Python needs <em>(A) &amp; (B)</em>, not <em>A &amp; B</em>, or you get an operator error.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "Calculated Columns",
                "icon": "fa6-solid:calculator",
                "header_subtitle": "Add formula columns to a DataFrame",
                "badge_label": "technique",
                "definition": 'A <strong>calculated column</strong> is a new column created from existing ones. Assign a formula to a new column name. It replaces typing formulas row by row in Excel.',
                "widget_html": build_comparison_table(2, "Excel Formula vs Python",
                    {"label": "Excel", "color_bg": "bg-blue-100", "color_text": "text-blue-700", "color_border": "border-blue-200"},
                    {"label": "Python", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Where", "a": "Cell by cell", "b": "Entire column at once"},
                        {"label": "Syntax", "a": "=B2\u2013C2", "b": f'{cp(2,"df[&quot;profit&quot;] = df[&quot;rev&quot;] - df[&quot;cost&quot;]")}'},
                        {"label": "Copies down", "a": "Drag fill handle", "b": "Automatic \u2014 one line"},
                    ],
                ),
                "code": 'df["profit"] = df["revenue"] - df["cost"]        # subtract columns\ndf["margin"] = df["profit"] / df["revenue"]       # divide columns\ndf["label"]  = "Q1"                                # constant value',
                "tip_text": '<strong>Python applies the formula to every row at once.</strong> You never need to drag a formula down \u2014 one line of code handles the entire column.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "to_excel()",
                "icon": "fa6-solid:file-export",
                "header_subtitle": "Save a DataFrame as an Excel file",
                "badge_label": "method",
                "definition": f'<strong>to_excel()</strong> writes a DataFrame to an .xlsx file. Pass the file path and set {cp(3,"index=False")} to skip row numbers.',
                "widget_html": build_rules_table(3, "Key Parameters", "fa6-solid:sliders", [
                    (f'{cp(3,"filepath")}', 'Output file path (required)'),
                    (f'{cp(3,"sheet_name")}', 'Sheet tab name \u2014 default "Sheet1"'),
                    (f'{cp(3,"index")}', f'Write row numbers \u2014 set {good("False")}'),
                    (f'{cp(3,"columns")}', 'List of columns to include'),
                ]),
                "code": 'df.to_excel("output.xlsx", index=False)              # basic save\ndf.to_excel("report.xlsx", sheet_name="Summary")     # named tab\ndf[["Name","Sales"]].to_excel("slim.xlsx", index=False)',
                "tip_text": f'<strong>Always set {tcp(3,"index=False")} when saving.</strong> Without it, pandas adds a column of row numbers that confuses Excel users.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
        ],
    }


# ── Lesson 03 — Using Python with SQL Queries ─────────────────────────

def lesson03_tabs():
    return {
        "subtitle": "SELECT, WHERE, GROUP BY, JOINs, and the SQL-plus-pandas workflow.",
        "tabs": [
            {
                "label": "SELECT and WHERE",
                "icon": "fa6-solid:magnifying-glass",
                "header_subtitle": "Fetch and filter rows from a table",
                "badge_label": "SQL clauses",
                "definition": '<strong>SELECT</strong> picks which columns to return. <strong>WHERE</strong> filters rows by a condition. Together they pull exactly the data you need from a database table.',
                "widget_html": build_operators_table(0, "Common SQL Clauses", [
                    {"op": "SELECT", "meaning": "Pick columns to return", "example": "SELECT name, salary"},
                    {"op": "WHERE", "meaning": "Filter rows by condition", "example": "WHERE salary &gt; 50000"},
                    {"op": "ORDER BY", "meaning": "Sort the result set", "example": "ORDER BY salary DESC"},
                    {"op": "LIMIT", "meaning": "Cap the row count", "example": "LIMIT 100"},
                ]),
                "code": 'query = "SELECT name, salary FROM staff WHERE salary > 50000"\ndf = pd.read_sql(query, engine)              # returns filtered rows\nprint(len(df), "rows matched")               # count results',
                "tip_text": '<strong>Always add a WHERE clause for large tables.</strong> Fetching every row wastes time and memory when you only need a subset.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "GROUP BY",
                "icon": "fa6-solid:layer-group",
                "header_subtitle": "Aggregate rows into summaries",
                "badge_label": "SQL clause",
                "definition": f'<strong>GROUP BY</strong> groups rows that share a value and applies an aggregate function like {cp(1,"SUM")}, {cp(1,"COUNT")}, or {cp(1,"AVG")}. It does in SQL what {cp(1,"groupby()")} does in pandas.',
                "widget_html": build_operators_table(1, "Aggregate Functions", [
                    {"op": "COUNT(*)", "meaning": "Count rows per group", "example": "SELECT dept, COUNT(*)"},
                    {"op": "SUM(col)", "meaning": "Total values in group", "example": "SUM(salary)"},
                    {"op": "AVG(col)", "meaning": "Mean value in group", "example": "AVG(salary)"},
                    {"op": "MAX(col)", "meaning": "Largest value in group", "example": "MAX(salary)"},
                ]),
                "code": 'query = """\nSELECT department, COUNT(*) AS n, AVG(salary) AS avg_pay\nFROM staff GROUP BY department\n"""\ndf = pd.read_sql(query, engine)              # one row per dept',
                "tip_text": '<strong>Every column in SELECT must appear in GROUP BY or inside an aggregate.</strong> Adding a bare column without SUM/COUNT/AVG causes an error.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "JOIN Queries",
                "icon": "fa6-solid:link",
                "header_subtitle": "Combine rows from two tables",
                "badge_label": "SQL clause",
                "definition": 'A <strong>JOIN</strong> combines rows from two tables using a shared column. The most common type is INNER JOIN, which returns only rows that match in both tables.',
                "widget_html": build_rules_table(2, "Join Types", "fa6-solid:diagram-project", [
                    ('INNER JOIN', 'Rows that match in both tables'),
                    ('LEFT JOIN', 'All left-table rows plus matches'),
                    ('RIGHT JOIN', 'All right-table rows plus matches'),
                    ('FULL JOIN', 'All rows from both tables'),
                ]),
                "code": 'query = """\nSELECT s.name, d.dept_name\nFROM staff s INNER JOIN departments d ON s.dept_id = d.id\n"""\ndf = pd.read_sql(query, engine)              # combined result',
                "tip_text": '<strong>Use table aliases to keep queries short.</strong> Write <em>FROM staff s</em> instead of repeating the full table name in every column reference.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "SQL + Pandas Workflow",
                "icon": "fa6-solid:shuffle",
                "header_subtitle": "Filter in SQL, transform in pandas",
                "badge_label": "workflow",
                "definition": 'The best approach is to <strong>filter and aggregate in SQL</strong>, then do final transformations in pandas. SQL is faster for filtering millions of rows. Pandas is better for reshaping and custom logic.',
                "widget_html": build_comparison_table(3, "SQL vs Pandas",
                    {"label": "SQL", "color_bg": "bg-emerald-100", "color_text": "text-emerald-700", "color_border": "border-emerald-200"},
                    {"label": "Pandas", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Filter rows", "a": tick_yes("Fast for millions"), "b": tick_yes("Flexible syntax")},
                        {"label": "Aggregate", "a": tick_yes("GROUP BY"), "b": tick_yes("groupby()")},
                        {"label": "Reshape", "a": tick_no("Limited"), "b": tick_yes("pivot, melt, stack")},
                        {"label": "Custom logic", "a": tick_no("Difficult"), "b": tick_yes("apply(), lambda")},
                    ],
                ),
                "code": 'df = pd.read_sql("SELECT * FROM sales WHERE year=2024", engine)\nsummary = df.groupby("region")["amount"].sum()  # pandas aggregate\nsummary = summary.reset_index()                  # flatten result',
                "tip_text": '<strong>Move heavy filtering to SQL.</strong> Loading 10 million rows into pandas and then filtering wastes memory. Let the database do it first.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


# ── Lesson 04 — Automating Repetitive Data Tasks ──────────────────────

def lesson04_tabs():
    return {
        "subtitle": "glob(), file loops, pd.concat(), and reusable functions.",
        "tabs": [
            {
                "label": "glob()",
                "icon": "fa6-solid:folder-open",
                "header_subtitle": "Find files by name pattern",
                "badge_label": "function",
                "definition": f'<strong>glob()</strong> searches a folder for files matching a pattern. Use {cp(0,"*")} to match any characters. It returns a list of file paths you can loop through.',
                "widget_html": build_rules_table(0, "Common Glob Patterns", "fa6-solid:asterisk", [
                    (f'{cp(0,"*.csv")}', 'All CSV files in the folder'),
                    (f'{cp(0,"data_*.xlsx")}', 'Excel files starting with data_'),
                    (f'{cp(0,"**/*.csv")}', 'CSV files in all subfolders'),
                    (f'{cp(0,"sales_202?.csv")}', 'sales_2020 through sales_2029'),
                ]),
                "code": 'files = glob.glob("data/*.csv")              # all CSVs in data/\nprint(len(files))                             # how many found\nprint(files[0])                               # first file path',
                "tip_text": f'<strong>Add {tcp(0,"recursive=True")} to search subfolders.</strong> Without it, the {tcp(0,"**")} pattern does not descend into nested directories.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "File Loops",
                "icon": "fa6-solid:arrows-spin",
                "header_subtitle": "Process every file in a list",
                "badge_label": "pattern",
                "definition": 'A <strong>file loop</strong> iterates over a list of file paths and runs the same code on each one. Combine glob() with a for loop to process an entire folder automatically.',
                "widget_html": build_rules_table(1, "Loop Pattern Steps", "fa6-solid:list-ol", [
                    ('Step 1', 'Find files with glob()'),
                    ('Step 2', 'Create an empty list for results'),
                    ('Step 3', 'Loop and read each file'),
                    ('Step 4', 'Append each DataFrame to the list'),
                ]),
                "code": 'files = glob.glob("reports/*.csv")            # find all CSVs\nframes = []                                   # empty collector\nfor f in files:                               # loop each file\n    frames.append(pd.read_csv(f))             # load and collect',
                "tip_text": '<strong>Print the file name inside the loop while developing.</strong> A quick <em>print(f)</em> shows which file caused an error if something fails.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "pd.concat()",
                "icon": "fa6-solid:object-group",
                "header_subtitle": "Stack multiple DataFrames into one",
                "badge_label": "function",
                "definition": f'<strong>pd.concat()</strong> joins a list of DataFrames into one. By default it stacks them vertically. All frames must share the same column names.',
                "widget_html": build_comparison_table(2, "concat() vs merge()",
                    {"label": "concat()", "color_bg": "bg-blue-100", "color_text": "text-blue-700", "color_border": "border-blue-200"},
                    {"label": "merge()", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Direction", "a": "Vertical \u2014 stack rows", "b": "Horizontal \u2014 add columns"},
                        {"label": "Input", "a": "List of DataFrames", "b": "Two DataFrames"},
                        {"label": "Match on", "a": "Same column names", "b": "A shared key column"},
                        {"label": "Use for", "a": "Combining monthly files", "b": "Joining related tables"},
                    ],
                ),
                "code": 'all_data = pd.concat(frames)                  # stack all frames\nall_data = pd.concat(frames, ignore_index=True)  # reset index\nprint(all_data.shape)                         # total rows and cols',
                "tip_text": f'<strong>Add {tcp(2,"ignore_index=True")} to reset row numbers.</strong> Without it, row numbers from each file overlap (0, 1, 2, 0, 1, 2\u2026).',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Reusable Functions",
                "icon": "fa6-solid:cube",
                "header_subtitle": "Wrap logic in a function for reuse",
                "badge_label": "pattern",
                "definition": 'A <strong>reusable function</strong> wraps your automation logic so you can call it with different inputs. Write the steps once inside <em>def</em>, then call the function with any folder or pattern.',
                "widget_html": build_rules_table(3, "Function Benefits", "fa6-solid:star", [
                    ('Write once', 'Define the logic a single time'),
                    ('Call many times', 'process_folder("jan/"), process_folder("feb/")'),
                    ('Easy to test', 'Run with a single test file first'),
                    ('Easy to read', 'A function name describes the intent'),
                ]),
                "code": 'def process_folder(pattern):                  # define once\n    files = glob.glob(pattern)                # find matching files\n    frames = [pd.read_csv(f) for f in files]  # load each one\n    return pd.concat(frames, ignore_index=True)  # combine',
                "tip_text": '<strong>Name functions after what they do, not how they do it.</strong> Use <em>process_monthly_sales()</em> instead of <em>loop_and_concat()</em>.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


# ── Lesson 05 — Building a Simple Reporting Script ────────────────────

def lesson05_tabs():
    return {
        "subtitle": "Extract, transform, summarise, and export in one script.",
        "tabs": [
            {
                "label": "Extract",
                "icon": "fa6-solid:download",
                "header_subtitle": "Load raw data from a source",
                "badge_label": "pipeline step",
                "definition": '<strong>Extract</strong> is the first step in a reporting pipeline. You load raw data from a file or database into a DataFrame. The goal is one clean load with no transformations yet.',
                "widget_html": build_rules_table(0, "Common Sources", "fa6-solid:database", [
                    (f'{cp(0,"pd.read_csv()")}', 'Load a CSV file'),
                    (f'{cp(0,"pd.read_excel()")}', 'Load an Excel workbook'),
                    (f'{cp(0,"pd.read_sql()")}', 'Query a database'),
                    (f'{cp(0,"pd.concat()")}', 'Combine multiple files'),
                ]),
                "code": 'df = pd.read_csv("sales_2024.csv")            # load source data\nprint(df.shape)                               # check row count\nprint(df.head())                              # preview first rows',
                "tip_text": f'<strong>Always check {tcp(0,"df.shape")} and {tcp(0,"df.head()")} after loading.</strong> This catches empty files, wrong separators, and missing columns before you continue.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Transform",
                "icon": "fa6-solid:wand-magic-sparkles",
                "header_subtitle": "Clean and reshape raw data",
                "badge_label": "pipeline step",
                "definition": '<strong>Transform</strong> is the second step. You clean the data by dropping nulls, fixing types, renaming columns, and filtering out rows you do not need.',
                "widget_html": build_rules_table(1, "Common Transforms", "fa6-solid:list-check", [
                    (f'{cp(1,"df.dropna()")}', 'Remove rows with missing values'),
                    (f'{cp(1,"df.rename()")}', 'Rename columns for clarity'),
                    (f'{cp(1,"pd.to_datetime()")}', 'Convert strings to date type'),
                    (f'{cp(1,"df[condition]")}', 'Filter rows by condition'),
                ]),
                "code": 'df = df.dropna(subset=["sales"])               # drop missing sales\ndf["date"] = pd.to_datetime(df["date"])        # fix date type\ndf = df[df["sales"] > 0]                       # remove zero sales',
                "tip_text": '<strong>Transform in order: drop nulls first, then fix types, then filter.</strong> Fixing types on null values causes errors.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "Summarise",
                "icon": "fa6-solid:chart-bar",
                "header_subtitle": "Aggregate data into a summary table",
                "badge_label": "pipeline step",
                "definition": f'<strong>Summarise</strong> means grouping rows and calculating totals or averages. Use {cp(2,"groupby()")} with an aggregate function. The result is a smaller table ready for the report.',
                "widget_html": build_operators_table(2, "Aggregate Functions", [
                    {"op": "sum()", "meaning": "Total of values", "example": 'df.groupby("region")["sales"].sum()'},
                    {"op": "mean()", "meaning": "Average value", "example": 'df.groupby("region")["sales"].mean()'},
                    {"op": "count()", "meaning": "Number of rows", "example": 'df.groupby("region")["sales"].count()'},
                    {"op": "max()", "meaning": "Largest value", "example": 'df.groupby("region")["sales"].max()'},
                ]),
                "code": 'summary = df.groupby("region")["sales"].sum()  # total per region\nsummary = summary.reset_index()                # flatten columns\nsummary.columns = ["Region", "Total Sales"]     # rename headers',
                "tip_text": f'<strong>Call {tcp(2,"reset_index()")} after groupby.</strong> Without it, the group column becomes the index, which makes exporting and merging harder.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Export",
                "icon": "fa6-solid:file-arrow-down",
                "header_subtitle": "Save the report to a file",
                "badge_label": "pipeline step",
                "definition": '<strong>Export</strong> is the final step. You save the summary table to a CSV or Excel file that stakeholders can open.',
                "widget_html": build_comparison_table(3, "CSV vs Excel Output",
                    {"label": "CSV", "color_bg": "bg-emerald-100", "color_text": "text-emerald-700", "color_border": "border-emerald-200"},
                    {"label": "Excel", "color_bg": "bg-gray-100", "color_text": "text-gray-700", "color_border": "border-gray-200"},
                    [
                        {"label": "Format", "a": "Plain text", "b": "Formatted workbook"},
                        {"label": "Method", "a": f'{cp(3,"to_csv()")}', "b": '<code class="font-mono bg-gray-100 text-gray-800 border border-gray-200 px-1 rounded">to_excel()</code>'},
                        {"label": "File size", "a": "Smaller", "b": "Larger"},
                        {"label": "Best for", "a": "Further processing", "b": "Sharing with people"},
                    ],
                ),
                "code": 'summary.to_csv("report.csv", index=False)      # CSV output\nsummary.to_excel("report.xlsx", index=False)    # Excel output\nprint("Report saved:", summary.shape[0], "rows") # confirm',
                "tip_text": '<strong>Add a print statement at the end of your script.</strong> A simple message like <em>"Report saved: 12 rows"</em> confirms the script ran successfully.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


# ── Lesson 06 — Automating Reports End to End ─────────────────────────

def lesson06_tabs():
    return {
        "subtitle": "Pipeline functions, logging, error handling, and the main() pattern.",
        "tabs": [
            {
                "label": "Pipeline Functions",
                "icon": "fa6-solid:diagram-project",
                "header_subtitle": "Organise code into extract, transform, load",
                "badge_label": "pattern",
                "definition": 'A <strong>pipeline function</strong> handles one step of the process. Split your script into extract(), transform(), and load(). Each function does one job and returns its result to the next step.',
                "widget_html": build_rules_table(0, "Pipeline Structure", "fa6-solid:list-ol", [
                    (f'{cp(0,"extract()")}', 'Load raw data from source \u2192 returns DataFrame'),
                    (f'{cp(0,"transform(df)")}', 'Clean and reshape \u2192 returns cleaned DataFrame'),
                    (f'{cp(0,"load(df)")}', 'Save the final output \u2192 writes file'),
                    (f'{cp(0,"main()")}', 'Calls all three in order'),
                ]),
                "code": 'def extract():                                 # step 1: load\n    return pd.read_csv("sales.csv")\ndef transform(df):                             # step 2: clean\n    return df.dropna().reset_index(drop=True)\ndef load(df):                                  # step 3: save\n    df.to_csv("report.csv", index=False)',
                "tip_text": '<strong>Each function should do one thing.</strong> If a function loads data AND cleans it, split it into two separate functions.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Logging",
                "icon": "fa6-solid:clipboard-list",
                "header_subtitle": "Track what your script does",
                "badge_label": "module",
                "definition": f'The <strong>logging</strong> module records messages as your script runs. Use it instead of {cp(1,"print()")}. Log messages include timestamps and severity levels.',
                "widget_html": build_operators_table(1, "Log Levels", [
                    {"op": "DEBUG", "meaning": "Detailed technical info", "example": 'logging.debug("Loading file")'},
                    {"op": "INFO", "meaning": "Normal operation", "example": 'logging.info("Loaded 500 rows")'},
                    {"op": "WARNING", "meaning": "Something unexpected", "example": 'logging.warning("Empty file")'},
                    {"op": "ERROR", "meaning": "Something failed", "example": 'logging.error("File not found")'},
                ]),
                "code": 'import logging\nlogging.basicConfig(level=logging.INFO)        # show INFO and above\nlogging.info("Script started")                 # log a message\nlogging.warning("No data for March")           # log a warning',
                "tip_text": f'<strong>Use {tcp(1,"logging.info()")} instead of {tcp(1,"print()")} in automated scripts.</strong> Log messages include timestamps and can be saved to a file for later review.',
                "tip_icon": "fa6-solid:lightbulb",
            },
            {
                "label": "Error Handling",
                "icon": "fa6-solid:triangle-exclamation",
                "header_subtitle": "Catch problems without crashing",
                "badge_label": "pattern",
                "definition": f'<strong>Error handling</strong> uses {cp(2,"try")} and {cp(2,"except")} to catch problems. If a file is missing or data is corrupt, the script logs the error and continues instead of crashing.',
                "widget_html": build_comparison_table(2, "Without vs With Error Handling",
                    {"label": "No try/except", "color_bg": "bg-red-100", "color_text": "text-red-700", "color_border": "border-red-200"},
                    {"label": "With try/except", "color_bg": "bg-green-100", "color_text": "text-green-700", "color_border": "border-green-200"},
                    [
                        {"label": "Missing file", "a": tick_no("Script crashes"), "b": tick_yes("Logs error, continues")},
                        {"label": "Bad data", "a": tick_no("Traceback printed"), "b": tick_yes("Handled gracefully")},
                        {"label": "Recovery", "a": tick_no("Restart manually"), "b": tick_yes("Skips and moves on")},
                    ],
                ),
                "code": 'try:                                           # protect this block\n    df = pd.read_csv("sales.csv")              # may fail\n    logging.info("Loaded %d rows", len(df))    # log success\nexcept FileNotFoundError:                      # catch missing file\n    logging.error("sales.csv not found")       # log the error',
                "tip_text": '<strong>Catch specific exceptions, not all exceptions.</strong> Writing <em>except Exception</em> hides bugs. Use specific types like <em>FileNotFoundError</em> or <em>ValueError</em>.',
                "tip_icon": "fa6-solid:triangle-exclamation",
            },
            {
                "label": "main() Pattern",
                "icon": "fa6-solid:play",
                "header_subtitle": "Run the full pipeline in one call",
                "badge_label": "pattern",
                "definition": 'The <strong>main() pattern</strong> wraps your entire pipeline in a single function. Call it at the bottom of the script with the name guard. This makes your script importable and testable.',
                "widget_html": build_rules_table(3, "main() Benefits", "fa6-solid:star", [
                    ('Single entry point', 'Run the whole pipeline with main()'),
                    ('Importable', 'Other scripts can import your functions'),
                    ('Testable', 'Call extract() or transform() separately'),
                    ('Clear flow', 'Read main() to see the full pipeline'),
                ]),
                "code": 'def main():                                    # entry point\n    df = extract()                             # step 1: load\n    df = transform(df)                         # step 2: clean\n    load(df)                                   # step 3: save\n    logging.info("Pipeline complete")          # confirm\nif __name__ == "__main__":                     # guard\n    main()                                     # run it',
                "tip_text": '<strong>The name guard prevents the pipeline from running when imported.</strong> Without it, importing your script in another file triggers the entire pipeline.',
                "tip_icon": "fa6-solid:lightbulb",
            },
        ],
    }


# ── Lesson registry ───────────────────────────────────────────────────

LESSONS = {
    "lesson01_why_analysts_use_python.html": lesson01_tabs,
    "lesson02_replacing_excel_workflows_with_python.html": lesson02_tabs,
    "lesson03_using_python_with_sql_queries.html": lesson03_tabs,
    "lesson04_automating_repetitive_data_tasks.html": lesson04_tabs,
    "lesson05_building_a_simple_reporting_script.html": lesson05_tabs,
    "lesson06_automating_reports_end_to_end.html": lesson06_tabs,
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
