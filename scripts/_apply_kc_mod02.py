"""Apply key-concepts rewrites for track_03 mod_02 (7 lessons)."""
import re, os, html as html_mod

BASE = r"c:\Users\nightwolf\Projects\Python-Learning\pages\track_03_data_engineering\mod_02_nosql_and_modern_data_storage"

KC_RE = re.compile(r'<section id="key-concepts"[^>]*>.*?</section>', re.DOTALL)

# ── Color reference ──────────────────────────────────────────────────
COLORS = [
    {  # 0 = pink
        'panel_border': 'border-pink-100',
        'topbar': 'from-[#CB187D] via-pink-400 to-rose-300',
        'panelbg': 'from-pink-50/60 to-white',
        'header_chip': 'from-[#CB187D] to-[#e84aad]',
        'badge_grad': 'from-pink-100 to-rose-100 text-[#CB187D] border border-pink-200',
        'tip_bg': 'bg-pink-50 border border-pink-100',
        'tip_chip': 'bg-[#CB187D]',
        'widget_header_bg': 'from-pink-50 to-rose-50',
        'widget_border': 'border-pink-100',
        'widget_text': 'text-pink-500',
        'widget_th': 'border-pink-50',
        'code_pill_bg': 'bg-pink-100', 'code_pill_text': 'text-pink-700', 'code_pill_border': 'border-pink-200',
        'tip_code_bg': 'bg-pink-200', 'tip_code_text': 'text-pink-800', 'tip_code_border': 'border-pink-300',
    },
    {  # 1 = violet
        'panel_border': 'border-violet-100',
        'topbar': 'from-violet-500 via-purple-400 to-fuchsia-300',
        'panelbg': 'from-violet-50/60 to-white',
        'header_chip': 'from-violet-500 to-purple-600',
        'badge_grad': 'from-violet-100 to-purple-100 text-violet-600 border border-violet-200',
        'tip_bg': 'bg-violet-50 border border-violet-100',
        'tip_chip': 'bg-violet-500',
        'widget_header_bg': 'from-violet-50 to-purple-50',
        'widget_border': 'border-violet-100',
        'widget_text': 'text-violet-500',
        'widget_th': 'border-violet-50',
        'code_pill_bg': 'bg-violet-100', 'code_pill_text': 'text-violet-700', 'code_pill_border': 'border-violet-200',
        'tip_code_bg': 'bg-violet-200', 'tip_code_text': 'text-violet-800', 'tip_code_border': 'border-violet-300',
    },
    {  # 2 = blue
        'panel_border': 'border-blue-100',
        'topbar': 'from-blue-500 via-cyan-400 to-teal-300',
        'panelbg': 'from-blue-50/60 to-white',
        'header_chip': 'from-blue-500 to-indigo-600',
        'badge_grad': 'from-blue-100 to-indigo-100 text-blue-600 border border-blue-200',
        'tip_bg': 'bg-blue-50 border border-blue-100',
        'tip_chip': 'bg-blue-500',
        'widget_header_bg': 'from-blue-50 to-indigo-50',
        'widget_border': 'border-blue-100',
        'widget_text': 'text-blue-500',
        'widget_th': 'border-blue-50',
        'code_pill_bg': 'bg-blue-100', 'code_pill_text': 'text-blue-700', 'code_pill_border': 'border-blue-200',
        'tip_code_bg': 'bg-blue-200', 'tip_code_text': 'text-blue-800', 'tip_code_border': 'border-blue-300',
    },
    {  # 3 = emerald
        'panel_border': 'border-emerald-100',
        'topbar': 'from-emerald-500 via-teal-400 to-cyan-300',
        'panelbg': 'from-emerald-50/60 to-white',
        'header_chip': 'from-emerald-500 to-teal-600',
        'badge_grad': 'from-emerald-100 to-teal-100 text-emerald-600 border border-emerald-200',
        'tip_bg': 'bg-emerald-50 border border-emerald-100',
        'tip_chip': 'bg-emerald-500',
        'widget_header_bg': 'from-emerald-50 to-teal-50',
        'widget_border': 'border-emerald-100',
        'widget_text': 'text-emerald-500',
        'widget_th': 'border-emerald-50',
        'code_pill_bg': 'bg-emerald-100', 'code_pill_text': 'text-emerald-700', 'code_pill_border': 'border-emerald-200',
        'tip_code_bg': 'bg-emerald-200', 'tip_code_text': 'text-emerald-800', 'tip_code_border': 'border-emerald-300',
    },
]

H = html_mod.escape

def cp(text, idx):
    c = COLORS[idx]
    return f'<code class="font-mono {c["code_pill_bg"]} {c["code_pill_text"]} border {c["code_pill_border"]} px-1 rounded">{text}</code>'

def tp(text, idx):
    c = COLORS[idx]
    return f'<code class="font-mono {c["tip_code_bg"]} {c["tip_code_text"]} border {c["tip_code_border"]} px-1 rounded">{text}</code>'

def make_tab(idx, icon, label):
    if idx == 0:
        style = 'style="background:#CB187D;color:#fff;box-shadow:0 2px 8px rgba(203,24,125,0.25)"'
        lbl = 'text-gray-900'; extra = ' kc-tab-active'
    else:
        style = 'style="background:#f3f4f6;color:#9ca3af"'
        lbl = 'text-gray-400'; extra = ''
    return (f'          <button onclick="switchKcTab({idx})" class="kc-tab{extra} group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">\n'
            f'            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" {style}><span class="iconify text-[11px]" data-icon="{icon}"></span></span>\n'
            f'            <span class="kc-tab-label text-xs font-bold leading-tight {lbl}">{label}</span>\n'
            f'          </button>')

def py_block(code):
    e = H(code)
    return (f'                <div class="rounded-xl overflow-hidden bg-code shadow-md">\n'
            f'                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">\n'
            f'                    <div class="flex items-center gap-2">\n'
            f'                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>\n'
            f'                      <span class="text-[11px] font-semibold text-gray-400">Python</span>\n'
            f'                    </div>\n'
            f'                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">\n'
            f'                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy\n'
            f'                    </button>\n'
            f'                  </div>\n'
            f'                  <pre class="overflow-x-auto pre-reset"><code class="language-python">{e}</code></pre>\n'
            f'                </div>')

def sql_blk(code):
    e = H(code)
    return (f'                <div class="rounded-xl overflow-hidden bg-code shadow-md">\n'
            f'                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">\n'
            f'                    <div class="flex items-center gap-2">\n'
            f'                      <span class="iconify text-gray-400" data-icon="fa6-solid:terminal" data-width="14" data-height="14"></span>\n'
            f'                      <span class="text-[11px] font-semibold text-gray-400">SQL</span>\n'
            f'                    </div>\n'
            f'                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">\n'
            f'                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy\n'
            f'                    </button>\n'
            f'                  </div>\n'
            f'                  <pre class="overflow-x-auto pre-reset"><code class="language-sql">{e}</code></pre>\n'
            f'                </div>')

def defn(text):
    return f'                <p class="text-xs text-gray-600 leading-relaxed">{text}</p>'

def rules_table(idx, icon, label, rows):
    c = COLORS[idx]
    rh = []
    for i,(rule,badge) in enumerate(rows):
        bg = ' bg-gray-50/50' if i%2==1 else ''
        bd = ' border-b border-gray-50' if i<len(rows)-1 else ''
        rh.append(f'        <tr class="{bd}{bg}">\n          <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/2">{rule}</td>\n          <td class="py-2 px-3 text-gray-500">{badge}</td>\n        </tr>')
    tb = '\n'.join(rh)
    return (f'                <div class="rounded-xl overflow-hidden border {c["widget_border"]}">\n'
            f'                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r {c["widget_header_bg"]} border-b {c["widget_border"]}">\n'
            f'                    <span class="iconify {c["widget_text"]} text-xs" data-icon="{icon}"></span>\n'
            f'                    <p class="text-[10px] font-bold uppercase tracking-widest {c["widget_text"]}">{label}</p>\n'
            f'                  </div>\n'
            f'                  <table class="w-full text-xs border-collapse bg-white">\n'
            f'                    <tbody>\n{tb}\n                    </tbody>\n'
            f'                  </table>\n'
            f'                </div>')

def operators_table(idx, icon, label, rows):
    c = COLORS[idx]
    rh = []
    for i,(op,meaning,ex) in enumerate(rows):
        bg = ' bg-gray-50/40' if i%2==1 else ''
        bd = ' border-b border-gray-50' if i<len(rows)-1 else ''
        rh.append(f'        <tr class="{bd}{bg}">\n'
                  f'          <td class="py-2 px-3"><code class="font-mono {c["code_pill_bg"]} {c["code_pill_text"]} border {c["code_pill_border"]} px-1.5 py-0.5 rounded-full text-[11px] font-bold">{H(op)}</code></td>\n'
                  f'          <td class="py-2 px-3 text-gray-500">{meaning}</td>\n'
                  f'          <td class="py-2 px-3"><code class="font-mono bg-gray-50 {c["code_pill_text"]} border {c["code_pill_border"]} px-1.5 py-0.5 rounded text-[10px]">{H(ex)}</code></td>\n'
                  f'        </tr>')
    tb = '\n'.join(rh)
    return (f'                <div class="rounded-xl overflow-hidden border {c["widget_border"]}">\n'
            f'                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r {c["widget_header_bg"]} border-b {c["widget_border"]}">\n'
            f'                    <span class="iconify {c["widget_text"]} text-xs" data-icon="{icon}"></span>\n'
            f'                    <p class="text-[10px] font-bold uppercase tracking-widest {c["widget_text"]}">{label}</p>\n'
            f'                  </div>\n'
            f'                  <table class="w-full text-xs border-collapse bg-white">\n'
            f'                    <thead>\n'
            f'                      <tr class="border-b {c["widget_th"]}">\n'
            f'                        <th class="py-2 px-3 text-left font-bold {c["widget_text"]} w-12">Op</th>\n'
            f'                        <th class="py-2 px-3 text-left font-bold {c["widget_text"]}">Meaning</th>\n'
            f'                        <th class="py-2 px-3 text-left font-bold {c["widget_text"]}">Example</th>\n'
            f'                      </tr>\n'
            f'                    </thead>\n'
            f'                    <tbody>\n{tb}\n                    </tbody>\n'
            f'                  </table>\n'
            f'                </div>')

def comparison_table(idx, icon, label, ca_label, ca_color, cb_label, cb_color, rows):
    c = COLORS[idx]
    rh = []
    for i,(lbl,a,b) in enumerate(rows):
        bg = ' bg-gray-50/40' if i%2==1 else ''
        bd = ' border-b border-gray-50' if i<len(rows)-1 else ''
        rh.append(f'        <tr class="{bd}{bg}">\n          <td class="py-2 px-3 font-semibold text-gray-600">{lbl}</td>\n          <td class="py-2 px-3 text-gray-500">{a}</td>\n          <td class="py-2 px-3 text-gray-500">{b}</td>\n        </tr>')
    tb = '\n'.join(rh)
    return (f'                <div class="rounded-xl overflow-hidden border {c["widget_border"]}">\n'
            f'                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r {c["widget_header_bg"]} border-b {c["widget_border"]}">\n'
            f'                    <span class="iconify {c["widget_text"]} text-xs" data-icon="{icon}"></span>\n'
            f'                    <p class="text-[10px] font-bold uppercase tracking-widest {c["widget_text"]}">{label}</p>\n'
            f'                  </div>\n'
            f'                  <table class="w-full text-xs border-collapse bg-white">\n'
            f'                    <thead>\n'
            f'                      <tr class="border-b {c["widget_th"]}">\n'
            f'                        <th class="py-2 px-3 text-left font-bold text-gray-400 w-1/3"></th>\n'
            f'                        <th class="py-2 px-3 text-left"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-{ca_color}-100 text-{ca_color}-700 border border-{ca_color}-200 text-[10px] font-bold">{ca_label}</span></th>\n'
            f'                        <th class="py-2 px-3 text-left"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-{cb_color}-100 text-{cb_color}-700 border border-{cb_color}-200 text-[10px] font-bold">{cb_label}</span></th>\n'
            f'                      </tr>\n'
            f'                    </thead>\n'
            f'                    <tbody>\n{tb}\n                    </tbody>\n'
            f'                  </table>\n'
            f'                </div>')

def single_col_table(idx, icon, label, col_label, rows):
    c = COLORS[idx]
    rh = []
    for i,(feat,val) in enumerate(rows):
        bg = ' bg-gray-50/40' if i%2==1 else ''
        bd = ' border-b border-gray-50' if i<len(rows)-1 else ''
        rh.append(f'        <tr class="{bd}{bg}">\n          <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap">{feat}</td>\n          <td class="py-2 px-3 text-gray-500">{val}</td>\n        </tr>')
    tb = '\n'.join(rh)
    return (f'                <div class="rounded-xl overflow-hidden border {c["widget_border"]}">\n'
            f'                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r {c["widget_header_bg"]} border-b {c["widget_border"]}">\n'
            f'                    <span class="iconify {c["widget_text"]} text-xs" data-icon="{icon}"></span>\n'
            f'                    <p class="text-[10px] font-bold uppercase tracking-widest {c["widget_text"]}">{label}</p>\n'
            f'                  </div>\n'
            f'                  <table class="w-full text-xs border-collapse bg-white">\n'
            f'                    <thead>\n'
            f'                      <tr class="border-b {c["widget_th"]}">\n'
            f'                        <th class="py-2 px-3 text-left font-bold {c["widget_text"]}">Feature</th>\n'
            f'                        <th class="py-2 px-3 text-left font-bold {c["widget_text"]}">{col_label}</th>\n'
            f'                      </tr>\n'
            f'                    </thead>\n'
            f'                    <tbody>\n{tb}\n                    </tbody>\n'
            f'                  </table>\n'
            f'                </div>')

def make_panel(idx, p):
    c = COLORS[idx]
    hidden = '' if idx == 0 else ' hidden'
    cname = ['pink','violet','blue','emerald'][idx]
    return (f'          <div class="kc-panel kc-panel-anim{hidden}" data-color="{cname}" role="tabpanel">\n'
            f'            <div class="rounded-2xl {c["panel_border"]} overflow-hidden">\n'
            f'              <div class="h-1 bg-gradient-to-r {c["topbar"]}"></div>\n'
            f'              <div class="bg-gradient-to-br {c["panelbg"]} p-5 space-y-4">\n'
            f'                <div class="flex items-center justify-between">\n'
            f'                  <div class="flex items-center gap-3">\n'
            f'                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br {c["header_chip"]} shadow-md shrink-0">\n'
            f'                      <span class="iconify text-white text-sm" data-icon="{p["icon"]}"></span>\n'
            f'                    </span>\n'
            f'                    <div>\n'
            f'                      <h3 class="text-sm font-bold text-gray-900 leading-tight">{p["label"]}</h3>\n'
            f'                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">{p["subtitle"]}</p>\n'
            f'                    </div>\n'
            f'                  </div>\n'
            f'                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r {c["badge_grad"]} shadow-sm">\n'
            f'                    <span class="iconify text-[10px]" data-icon="{p["badge_icon"]}"></span> {p["badge_label"]}\n'
            f'                  </span>\n'
            f'                </div>\n'
            f'{p["definition"]}\n'
            f'{p["widget"]}\n'
            f'{p["code"]}\n'
            f'                <div class="rounded-xl p-3 flex items-start gap-2.5 {c["tip_bg"]}">\n'
            f'                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg {c["tip_chip"]} shrink-0 mt-0.5">\n'
            f'                    <span class="iconify text-white text-[10px]" data-icon="{p["tip_icon"]}"></span>\n'
            f'                  </span>\n'
            f'                  <p class="text-xs text-gray-600">{p["tip"]}</p>\n'
            f'                </div>\n'
            f'              </div>\n'
            f'            </div>\n'
            f'          </div>')

def make_section(subtitle, tabs):
    sb = '\n'.join(make_tab(i, t['tab_icon'], t['tab_label']) for i,t in enumerate(tabs))
    pn = '\n'.join(make_panel(i, t['panel']) for i,t in enumerate(tabs))
    return (f'<section id="key-concepts" class="scroll-mt-24">\n'
            f'  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">\n'
            f'    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">\n'
            f'      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">\n'
            f'        <span class="iconify text-white text-base" data-icon="fa6-solid:book-open"></span>\n'
            f'      </span>\n'
            f'      <div class="min-w-0">\n'
            f'        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Concepts</h2>\n'
            f'        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">{subtitle}</p>\n'
            f'      </div>\n'
            f'    </div>\n'
            f'    <div class="bg-white px-6 py-7">\n'
            f'      <div class="flex flex-col md:flex-row gap-0">\n'
            f'        <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">\n'
            f'          <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full transition-all duration-300" style="height:68px;background:#CB187D;"></div>\n'
            f'{sb}\n'
            f'        </div>\n'
            f'        <div class="flex-1 min-w-0 md:pl-5">\n'
            f'{pn}\n'
            f'        </div>\n'
            f'      </div>\n'
            f'    </div>\n'
            f'  </div>\n'
            f'</section>')

# ── Helpers ─────────────────────────────────────────────────────────
G = '<span class="text-green-500 font-bold">\u2713</span> <span class="text-gray-400">'
R = '<span class="text-red-400 font-bold">\u2717</span> <span class="text-gray-400">'
GE = '</span>'
gpill = '<code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">'

# ────────────────────────── LESSON 01 ──────────────────────────────
def mk(tab_icon, tab_label, panel):
    return {'tab_icon': tab_icon, 'tab_label': tab_label, 'panel': panel}

L01 = make_section(
    'Relational database, NoSQL database, schema flexibility, and horizontal scaling.',
    [
        mk('fa6-solid:table', 'Relational Database', {
            'icon': 'fa6-solid:table', 'label': 'Relational Database',
            'subtitle': 'Traditional table-based storage', 'badge_label': 'Core Term', 'badge_icon': 'fa6-solid:database',
            'definition': defn(f'A <strong>relational database</strong> stores data in {cp("tables", 0)} with rows and columns. Tables link to each other through shared keys.'),
            'widget': single_col_table(0, 'fa6-solid:list-check', 'SQL Structure', 'Detail', [
                ('Data format', 'Tables with rows and columns'),
                ('Schema', 'Fixed \u2014 defined before inserting data'),
                ('Relationships', 'JOIN queries link tables together'),
                ('Examples', 'PostgreSQL, MySQL, SQL Server'),
            ]),
            'code': py_block('import sqlite3                          # built-in SQL library\nconn = sqlite3.connect("shop.db")       # open database file\ncursor = conn.execute("SELECT name "    # query customers\n                      "FROM customers") # returns matching rows'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>SQL databases guarantee consistency.</strong> Every {tp("INSERT", 0)} and {tp("UPDATE", 0)} follows the fixed schema \u2014 you cannot store mismatched data types.',
        }),
        mk('fa6-solid:cubes', 'NoSQL Database', {
            'icon': 'fa6-solid:cubes', 'label': 'NoSQL Database',
            'subtitle': 'Flexible non-relational storage', 'badge_label': 'Core Term', 'badge_icon': 'fa6-solid:database',
            'definition': defn(f'A <strong>NoSQL database</strong> stores data without fixed tables. Data can be {cp("documents", 1)}, {cp("key-value pairs", 1)}, or {cp("graphs", 1)}.'),
            'widget': rules_table(1, 'fa6-solid:list-check', 'NoSQL Features', [
                (f'No fixed {cp("schema", 1)}', f'{gpill}flexible</code> \u2713'),
                ('Scales across servers', f'{gpill}horizontal</code> \u2713'),
                ('No JOIN queries needed', f'{gpill}embedded</code> data'),
            ]),
            'code': py_block('doc = {                        # one JSON-like document\n    "name": "Alice",            # no fixed column order\n    "city": "Los Angeles",      # fields can vary per record\n    "orders": [{"item": "Laptop"}]  # nested data allowed\n}'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>NoSQL doesn\'t mean "no SQL at all".</strong> It stands for {tp("Not Only SQL", 1)} \u2014 some NoSQL databases support SQL-like queries too.',
        }),
        mk('fa6-solid:shapes', 'Schema Flexibility', {
            'icon': 'fa6-solid:shapes', 'label': 'Schema Flexibility',
            'subtitle': 'Fixed versus dynamic structure', 'badge_label': 'Key Difference', 'badge_icon': 'fa6-solid:code',
            'definition': defn(f'<strong>Schema flexibility</strong> means each record can have different fields. SQL databases need a {cp("fixed schema", 2)} before you add data.'),
            'widget': comparison_table(2, 'fa6-solid:scale-balanced', 'Fixed vs Flexible Schema', 'SQL', 'pink', 'NoSQL', 'violet', [
                ('Schema', 'Must define columns first', 'No schema required'),
                ('New field', f'{R}Alter table{GE}', f'{G}Just add it{GE}'),
                ('Record format', 'Every row same shape', 'Each document can differ'),
            ]),
            'code': py_block('doc_a = {"name": "Alice", "city": "LA"}       # two fields\ndoc_b = {"name": "Bob", "orders": 12}          # different fields OK\ndoc_c = {"name": "Maria", "prefs": {"x": 1}}   # nested object too'),
            'tip_icon': 'fa6-solid:triangle-exclamation',
            'tip': f'<strong>Flexibility has trade-offs.</strong> Without a schema your code must handle missing fields \u2014 always {tp("validate", 2)} data before using it.',
        }),
        mk('fa6-solid:server', 'Horizontal Scaling', {
            'icon': 'fa6-solid:server', 'label': 'Horizontal Scaling',
            'subtitle': 'Adding more servers', 'badge_label': 'Architecture', 'badge_icon': 'fa6-solid:code',
            'definition': defn(f'<strong>Horizontal scaling</strong> means adding more servers to handle more data. SQL databases usually {cp("scale vertically", 3)} \u2014 upgrading one server\'s CPU or RAM.'),
            'widget': comparison_table(3, 'fa6-solid:scale-balanced', 'Vertical vs Horizontal', 'Vertical', 'pink', 'Horizontal', 'emerald', [
                ('Method', 'Upgrade one server', 'Add more servers'),
                ('Limit', f'{R}Hardware max{GE}', f'{G}Near-unlimited{GE}'),
                ('Common with', 'SQL databases', 'NoSQL databases'),
            ]),
            'code': py_block('nodes = ["server_1", "server_2", "server_3"]  # three servers\nfor node in nodes:                              # loop each one\n    print(f"{node} holds part of the data")      # data is split up'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>Cloud providers make horizontal scaling easy.</strong> Services like {tp("AWS", 3)} and {tp("Azure", 3)} let you add nodes with a few clicks.',
        }),
    ]
)

# ────────────────────────── LESSON 02 ──────────────────────────────
L02 = make_section(
    'Document, key-value, column-family, and graph databases.',
    [
        mk('fa6-solid:file-code', 'Document Database', {
            'icon': 'fa6-solid:file-code', 'label': 'Document Database',
            'subtitle': 'JSON-like flexible records', 'badge_label': 'Database Type', 'badge_icon': 'fa6-solid:database',
            'definition': defn(f'A <strong>document database</strong> stores each record as a {cp("JSON document", 0)}. Documents can have different fields and nested objects.'),
            'widget': rules_table(0, 'fa6-solid:list-check', 'Document DB Features', [
                ('Flexible schema', f'{gpill}dynamic</code> \u2713'),
                ('Nested data', f'{gpill}embedded</code> objects'),
                ('Popular choice', f'{gpill}MongoDB</code>'),
                ('Best for', 'User profiles, product catalogues, CMS'),
            ]),
            'code': py_block('customer = {\n    "name": "Alice",               # string field\n    "city": "Los Angeles",          # another string\n    "orders": [{"item": "Laptop"}]  # embedded list\n}'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>MongoDB is the most popular document database.</strong> It stores data in a format called {tp("BSON", 0)} \u2014 binary JSON optimised for speed.',
        }),
        mk('fa6-solid:key', 'Key-Value Database', {
            'icon': 'fa6-solid:key', 'label': 'Key-Value Database',
            'subtitle': 'Simple fast lookups', 'badge_label': 'Database Type', 'badge_icon': 'fa6-solid:database',
            'definition': defn(f'A <strong>key-value database</strong> maps a unique {cp("key", 1)} to a {cp("value", 1)}. It works like a Python dictionary stored on a server.'),
            'widget': operators_table(1, 'fa6-solid:terminal', 'Redis Commands', [
                ('SET', 'Store a value', 'SET user_1 "Alice"'),
                ('GET', 'Retrieve a value', 'GET user_1 \u2192 "Alice"'),
                ('DEL', 'Delete a key', 'DEL user_1'),
                ('EXISTS', 'Check if key exists', 'EXISTS user_1 \u2192 1'),
            ]),
            'code': py_block('import redis                       # Redis client library\nr = redis.Redis()                   # connect to server\nr.set("user_1", "Alice")            # store key-value pair\nprint(r.get("user_1"))              # retrieve the value'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>Redis stores data in RAM.</strong> This makes reads extremely fast \u2014 perfect for {tp("caching", 1)} and {tp("session storage", 1)}.',
        }),
        mk('fa6-solid:table-columns', 'Column-Family DB', {
            'icon': 'fa6-solid:table-columns', 'label': 'Column-Family Database',
            'subtitle': 'Column-oriented storage', 'badge_label': 'Database Type', 'badge_icon': 'fa6-solid:database',
            'definition': defn(f'A <strong>column-family database</strong> groups data by {cp("columns", 2)} instead of rows. This makes analytical queries on large datasets very fast.'),
            'widget': comparison_table(2, 'fa6-solid:scale-balanced', 'Row vs Column Storage', 'Row-Based', 'pink', 'Column-Based', 'blue', [
                ('Read pattern', 'Full rows at once', 'Selected columns only'),
                ('Best for', 'Single-record lookups', 'Aggregations and analytics'),
                ('Example', 'MySQL, PostgreSQL', 'Cassandra, HBase'),
            ]),
            'code': py_block('from cassandra.cluster import Cluster  # Cassandra driver\ncluster = Cluster(["127.0.0.1"])       # connect to node\nsession = cluster.connect("my_app")    # select keyspace\nrows = session.execute("SELECT * "     # query returns rows\n    "FROM events WHERE user_id=101")'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>Column-family databases handle massive write loads.</strong> {tp("Cassandra", 2)} can process millions of writes per second across a cluster.',
        }),
        mk('fa6-solid:circle-nodes', 'Graph Database', {
            'icon': 'fa6-solid:circle-nodes', 'label': 'Graph Database',
            'subtitle': 'Nodes and relationships', 'badge_label': 'Database Type', 'badge_icon': 'fa6-solid:database',
            'definition': defn(f'A <strong>graph database</strong> stores data as {cp("nodes", 3)} (entities) connected by {cp("relationships", 3)} (edges). It excels at finding connections.'),
            'widget': rules_table(3, 'fa6-solid:list-check', 'Graph Components', [
                (f'{cp("Node", 3)}', 'An entity \u2014 person, product, account'),
                (f'{cp("Relationship", 3)}', 'A connection \u2014 FRIEND, PURCHASED'),
                (f'{cp("Property", 3)}', 'Data on a node or relationship'),
                (f'{cp("Label", 3)}', 'Category tag \u2014 Person, Product'),
            ]),
            'code': py_block('from neo4j import GraphDatabase        # Neo4j driver\ndriver = GraphDatabase.driver(uri)      # connect to server\nwith driver.session() as s:             # open session\n    s.run("CREATE (p:Person "            # create a node\n          "{name: \'Alice\'})")'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>Graph databases shine at fraud detection.</strong> They can quickly trace {tp("shared phone numbers", 3)} or {tp("linked accounts", 3)} across millions of records.',
        }),
    ]
)

# ────────────────────────── LESSON 03 ──────────────────────────────
L03 = make_section(
    'Document structure, nested documents, CRUD operations, and query filtering.',
    [
        mk('fa6-solid:sitemap', 'Document Structure', {
            'icon': 'fa6-solid:sitemap', 'label': 'Document Structure',
            'subtitle': 'Database \u2192 Collection \u2192 Document', 'badge_label': 'Core Concept', 'badge_icon': 'fa6-solid:cubes',
            'definition': defn(f'MongoDB organises data in three layers: a <strong>database</strong> holds {cp("collections", 0)}, and each collection holds {cp("documents", 0)}. A document is like one JSON record.'),
            'widget': comparison_table(0, 'fa6-solid:scale-balanced', 'SQL vs MongoDB Terms', 'SQL', 'pink', 'MongoDB', 'violet', [
                ('Container', 'Database', 'Database'),
                ('Group of records', 'Table', 'Collection'),
                ('Single record', 'Row', 'Document'),
                ('Data field', 'Column', 'Field'),
            ]),
            'code': py_block('from pymongo import MongoClient         # MongoDB driver\nclient = MongoClient("localhost", 27017) # connect to server\ndb = client["shop"]                      # select database\ncustomers = db["customers"]              # select collection'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>Collections are created automatically.</strong> When you insert the first document into {tp("db[&quot;orders&quot;]", 0)}, MongoDB creates the collection for you.',
        }),
        mk('fa6-solid:layer-group', 'Nested Documents', {
            'icon': 'fa6-solid:layer-group', 'label': 'Nested Documents',
            'subtitle': 'Embedded objects inside records', 'badge_label': 'Data Pattern', 'badge_icon': 'fa6-solid:cubes',
            'definition': defn(f'A <strong>nested document</strong> is an object stored inside another document. This lets you keep related data together instead of using {cp("separate tables", 1)}.'),
            'widget': comparison_table(1, 'fa6-solid:scale-balanced', 'Separate vs Embedded', 'SQL (separate)', 'pink', 'MongoDB (embedded)', 'violet', [
                ('Storage', 'Two linked tables', 'One document'),
                ('Read speed', 'Requires a JOIN', 'Single read'),
                ('Data integrity', f'{G}Strong{GE}', f'{G}Flexible{GE}'),
            ]),
            'code': py_block('doc = {\n    "name": "Alice",               # top-level field\n    "address": {                    # nested document\n        "city": "Los Angeles",      # sub-field\n        "zip": "90001"              # another sub-field\n    }\n}'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>Embedding avoids JOIN queries.</strong> Put related data in the same document when it is always read together \u2014 this is the {tp("embedded pattern", 1)}.',
        }),
        mk('fa6-solid:pen-to-square', 'CRUD Operations', {
            'icon': 'fa6-solid:pen-to-square', 'label': 'CRUD Operations',
            'subtitle': 'Create, read, update, delete', 'badge_label': 'Operations', 'badge_icon': 'fa6-solid:gear',
            'definition': defn(f'<strong>CRUD</strong> stands for Create, Read, Update, Delete \u2014 the four basic operations. MongoDB uses methods like {cp("insert_one()", 2)} and {cp("find()", 2)}.'),
            'widget': operators_table(2, 'fa6-solid:terminal', 'MongoDB Methods', [
                ('insert_one()', 'Add one document', 'db.col.insert_one({...})'),
                ('find()', 'Read documents', 'db.col.find({})'),
                ('update_one()', 'Change one document', 'db.col.update_one(f, u)'),
                ('delete_one()', 'Remove one document', 'db.col.delete_one(f)'),
            ]),
            'code': py_block('customers.insert_one({"name": "Alice"})   # create\nresult = customers.find({"name": "Alice"})  # read\ncustomers.update_one(                       # update\n    {"name": "Alice"},                       # filter\n    {"$set": {"city": "LA"}})                # new value'),
            'tip_icon': 'fa6-solid:triangle-exclamation',
            'tip': f'<strong>Use update_one for single records.</strong> The {tp("update_many()", 2)} method changes every matching document \u2014 always double-check your filter first.',
        }),
        mk('fa6-solid:filter', 'Query Filtering', {
            'icon': 'fa6-solid:filter', 'label': 'Query Filtering',
            'subtitle': 'Finding specific documents', 'badge_label': 'Querying', 'badge_icon': 'fa6-solid:magnifying-glass',
            'definition': defn(f'You <strong>filter documents</strong> by passing a query object to {cp("find()", 3)}. MongoDB supports comparison operators like {cp("$gt", 3)} and {cp("$lt", 3)}.'),
            'widget': operators_table(3, 'fa6-solid:terminal', 'Query Operators', [
                ('$eq', 'Equals', '{"age": {"$eq": 30}}'),
                ('$gt', 'Greater than', '{"age": {"$gt": 25}}'),
                ('$lt', 'Less than', '{"price": {"$lt": 100}}'),
                ('$in', 'In a list', '{"city": {"$in": [...]}}'),
            ]),
            'code': py_block('# find customers in Los Angeles\nresults = customers.find(               # query collection\n    {"city": "Los Angeles"}              # filter object\n)\nfor doc in results:                      # loop matches\n    print(doc["name"])                   # print each name'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>An empty filter returns everything.</strong> Calling {tp("find({{}})", 3)} with no conditions returns all documents in the collection \u2014 useful for debugging.',
        }),
    ]
)

# ────────────────────────── LESSON 04 ──────────────────────────────
L04 = make_section(
    'Key-value model, basic commands, data structures, and TTL expiry.',
    [
        mk('fa6-solid:key', 'Key-Value Model', {
            'icon': 'fa6-solid:key', 'label': 'Key-Value Model',
            'subtitle': 'Keys mapped to values in memory', 'badge_label': 'Core Concept', 'badge_icon': 'fa6-solid:database',
            'definition': defn(f'The <strong>key-value model</strong> maps a unique {cp("key", 0)} to a {cp("value", 0)} stored in RAM. Redis uses this model for extremely fast reads and writes.'),
            'widget': rules_table(0, 'fa6-solid:list-check', 'Redis Features', [
                ('In-memory storage', f'{gpill}fast</code> \u2713 microsecond reads'),
                ('Simple data model', f'{gpill}key \u2192 value</code> pairs'),
                ('Common use cases', 'Caching, session storage, leaderboards'),
            ]),
            'code': py_block('import redis                       # Redis client library\nr = redis.Redis()                   # connect to server\nr.set("user_101", "Alice")          # store a value\nprint(r.get("user_101"))            # retrieve it'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>Redis stores data in RAM, not on disk.</strong> Reads are fast but data can be lost on restart \u2014 enable {tp("persistence", 0)} in production.',
        }),
        mk('fa6-solid:terminal', 'Basic Commands', {
            'icon': 'fa6-solid:terminal', 'label': 'Basic Commands',
            'subtitle': 'SET, GET, DEL, EXISTS', 'badge_label': 'Commands', 'badge_icon': 'fa6-solid:gear',
            'definition': defn(f'Redis has four essential commands. {cp("SET", 1)} stores a value, {cp("GET", 1)} reads it, {cp("DEL", 1)} removes it, and {cp("EXISTS", 1)} checks if a key is present.'),
            'widget': operators_table(1, 'fa6-solid:terminal', 'Core Commands', [
                ('SET', 'Store key-value', 'SET name "Alice"'),
                ('GET', 'Read a value', 'GET name \u2192 "Alice"'),
                ('DEL', 'Delete a key', 'DEL name \u2192 (integer) 1'),
                ('EXISTS', 'Check key exists', 'EXISTS name \u2192 0 or 1'),
            ]),
            'code': py_block('r.set("cart_8129", "Laptop,Mouse")  # store cart items\nvalue = r.get("cart_8129")           # read cart\nr.delete("cart_8129")                # remove when done\nexists = r.exists("cart_8129")       # check \u2192 0 (gone)'),
            'tip_icon': 'fa6-solid:triangle-exclamation',
            'tip': f'<strong>Keys are case-sensitive.</strong> The keys {tp("User_1", 1)} and {tp("user_1", 1)} are two completely different entries in Redis.',
        }),
        mk('fa6-solid:cubes', 'Data Structures', {
            'icon': 'fa6-solid:cubes', 'label': 'Data Structures',
            'subtitle': 'Beyond simple strings', 'badge_label': 'Data Types', 'badge_icon': 'fa6-solid:shapes',
            'definition': defn(f'Redis supports more than plain strings. You can store {cp("lists", 2)}, {cp("hashes", 2)}, {cp("sets", 2)}, and {cp("sorted sets", 2)}.'),
            'widget': single_col_table(2, 'fa6-solid:shapes', 'Redis Data Types', 'Use Case', [
                ('String', 'Caching simple values'),
                ('List', 'Message queues, recent items'),
                ('Hash', 'Object-like records with fields'),
                ('Set', 'Unique tags, tracking unique visitors'),
                ('Sorted Set', 'Leaderboards, ranked feeds'),
            ]),
            'code': py_block('r.hset("user:101", mapping={       # store a hash\n    "name": "Alice",                 # field: value\n    "city": "LA"                     # another field\n})\nprint(r.hgetall("user:101"))        # get all fields'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>Choose the right data type.</strong> Use a {tp("hash", 2)} when you need to read individual fields \u2014 it is faster than storing a serialised JSON string.',
        }),
        mk('fa6-solid:clock', 'TTL & Expiry', {
            'icon': 'fa6-solid:clock', 'label': 'TTL & Expiry',
            'subtitle': 'Auto-delete after a set time', 'badge_label': 'Feature', 'badge_icon': 'fa6-solid:gear',
            'definition': defn(f'<strong>TTL (Time To Live)</strong> lets you set an expiry on any key. After the timer runs out, Redis {cp("automatically deletes", 3)} the key.'),
            'widget': operators_table(3, 'fa6-solid:terminal', 'TTL Commands', [
                ('SETEX', 'Set with expiry', 'SETEX token 3600 "abc"'),
                ('EXPIRE', 'Add expiry to key', 'EXPIRE session 1800'),
                ('TTL', 'Check time left', 'TTL session \u2192 1500'),
                ('PERSIST', 'Remove expiry', 'PERSIST session'),
            ]),
            'code': py_block('r.setex("session_abc", 3600, "data")  # expires in 1 hour\nttl = r.ttl("session_abc")             # check seconds left\nprint(f"Expires in {ttl}s")             # show remaining\nr.persist("session_abc")                # remove the timer'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>TTL is the backbone of caching.</strong> Set short expiry times on {tp("API responses", 3)} so stale data is automatically cleared without extra code.',
        }),
    ]
)

# ────────────────────────── LESSON 05 ──────────────────────────────
L05 = make_section(
    'Cassandra data model, partition keys, distributed storage, and write performance.',
    [
        mk('fa6-solid:table-cells', 'Data Model', {
            'icon': 'fa6-solid:table-cells', 'label': 'Cassandra Data Model',
            'subtitle': 'Keyspace, table, row, column', 'badge_label': 'Core Concept', 'badge_icon': 'fa6-solid:cubes',
            'definition': defn(f'Cassandra organises data in layers: a <strong>keyspace</strong> holds {cp("tables", 0)}, each table has {cp("rows", 0)} and {cp("columns", 0)}. A keyspace is like an SQL database.'),
            'widget': comparison_table(0, 'fa6-solid:scale-balanced', 'Cassandra vs SQL Terms', 'Cassandra', 'pink', 'SQL', 'violet', [
                ('Top level', 'Keyspace', 'Database'),
                ('Data group', 'Table', 'Table'),
                ('Single record', 'Row', 'Row'),
                ('Data field', 'Column', 'Column'),
            ]),
            'code': sql_blk("CREATE KEYSPACE my_app           -- top-level container\n  WITH replication = {            -- set replication\n    'class': 'SimpleStrategy',    -- strategy name\n    'replication_factor': 3       -- three copies\n  };"),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>Always set a replication factor above 1.</strong> With {tp("replication_factor: 3", 0)} your data is copied to three nodes \u2014 so one server can fail without data loss.',
        }),
        mk('fa6-solid:key', 'Partition Key', {
            'icon': 'fa6-solid:key', 'label': 'Partition Key',
            'subtitle': 'How data is distributed', 'badge_label': 'Distribution', 'badge_icon': 'fa6-solid:shuffle',
            'definition': defn(f'The <strong>partition key</strong> decides which server stores each row. Cassandra hashes the {cp("PRIMARY KEY", 1)} to spread data evenly across nodes.'),
            'widget': rules_table(1, 'fa6-solid:list-check', 'Partition Key Rules', [
                (f'Choose a {cp("high-cardinality", 1)} column', f'{gpill}user_id</code> \u2713'),
                ('Avoid low-cardinality', '<code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">country</code> \u2717 \u2014 creates hotspots'),
                ('Queries must include it', 'WHERE must use the partition key'),
            ]),
            'code': sql_blk("CREATE TABLE user_activity (        -- new table\n  user_id INT,                       -- partition key\n  ts TIMESTAMP,                      -- clustering column\n  event TEXT,                        -- regular column\n  PRIMARY KEY (user_id, ts)          -- user_id distributes\n);"),
            'tip_icon': 'fa6-solid:triangle-exclamation',
            'tip': f'<strong>You cannot query without the partition key.</strong> Cassandra forces you to include {tp("user_id", 1)} in every WHERE clause \u2014 design your tables around your queries.',
        }),
        mk('fa6-solid:network-wired', 'Distributed Storage', {
            'icon': 'fa6-solid:network-wired', 'label': 'Distributed Storage',
            'subtitle': 'Data across multiple nodes', 'badge_label': 'Architecture', 'badge_icon': 'fa6-solid:server',
            'definition': defn(f'Cassandra spreads data across a <strong>cluster</strong> of servers called {cp("nodes", 2)}. There is no single master \u2014 every node can handle reads and writes.'),
            'widget': comparison_table(2, 'fa6-solid:scale-balanced', 'Single Server vs Distributed', 'Single Server', 'pink', 'Cassandra Cluster', 'blue', [
                ('Failure impact', f'{R}Everything stops{GE}', f'{G}Other nodes take over{GE}'),
                ('Capacity', 'Limited to one machine', 'Add nodes to grow'),
                ('Data copies', 'One copy', 'Configurable replicas'),
            ]),
            'code': py_block('from cassandra.cluster import Cluster  # driver\ncluster = Cluster([                     # list of nodes\n    "10.0.0.1", "10.0.0.2",             # two seed nodes\n    "10.0.0.3"                           # third seed node\n])'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>No single point of failure.</strong> Unlike traditional databases, Cassandra has no master node \u2014 every {tp("node", 2)} is equal and can serve any request.',
        }),
        mk('fa6-solid:bolt', 'Write Performance', {
            'icon': 'fa6-solid:bolt', 'label': 'Write Performance',
            'subtitle': 'Optimised for fast inserts', 'badge_label': 'Strength', 'badge_icon': 'fa6-solid:gauge-high',
            'definition': defn(f'Cassandra is optimised for <strong>high write throughput</strong>. Writes go to an {cp("append-only log", 3)} first, making inserts extremely fast.'),
            'widget': rules_table(3, 'fa6-solid:list-check', 'Ideal Workloads', [
                ('Sensor readings', f'{gpill}time-series</code> \u2713'),
                ('User activity logs', f'{gpill}event tracking</code> \u2713'),
                ('Website click streams', f'{gpill}analytics</code> \u2713'),
            ]),
            'code': sql_blk("INSERT INTO user_activity            -- add a row\n  (user_id, ts, event)                -- column list\n  VALUES (101,                        -- partition key\n    '2024-03-01 10:15:00',            -- timestamp\n    'login');                          -- event type"),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>Cassandra writes are append-only.</strong> Updates create a new version rather than overwriting \u2014 {tp("compaction", 3)} later merges old and new data.',
        }),
    ]
)

# ────────────────────────── LESSON 06 ──────────────────────────────
L06 = make_section(
    'Nodes, relationships, Cypher queries, and graph patterns.',
    [
        mk('fa6-solid:circle-dot', 'Nodes', {
            'icon': 'fa6-solid:circle-dot', 'label': 'Nodes',
            'subtitle': 'Entities with labels and properties', 'badge_label': 'Core Term', 'badge_icon': 'fa6-solid:cubes',
            'definition': defn(f'A <strong>node</strong> represents an entity in the graph \u2014 a person, product, or account. Each node has a {cp("label", 0)} (its type) and {cp("properties", 0)} (its data).'),
            'widget': rules_table(0, 'fa6-solid:list-check', 'Node Components', [
                (f'{cp("Label", 0)}', 'Category \u2014 Person, Product, City'),
                (f'{cp("Property", 0)}', 'Key-value data \u2014 name: "Alice"'),
                (f'{cp("ID", 0)}', 'Auto-generated unique identifier'),
            ]),
            'code': sql_blk('CREATE (p:Person {          -- create a Person node\n  name: "Alice",              -- property: name\n  age: 30,                    -- property: age\n  city: "Los Angeles"         -- property: city\n})'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>Labels let you query by category.</strong> Use {tp("MATCH (p:Person)", 0)} to find all Person nodes \u2014 without labels you would have to scan every node.',
        }),
        mk('fa6-solid:arrows-left-right', 'Relationships', {
            'icon': 'fa6-solid:arrows-left-right', 'label': 'Relationships',
            'subtitle': 'Directed connections between nodes', 'badge_label': 'Core Term', 'badge_icon': 'fa6-solid:cubes',
            'definition': defn(f'A <strong>relationship</strong> connects two nodes with a direction and a type. For example, Alice {cp("-[:FRIEND]-&gt;", 1)} Bob means Alice is a friend of Bob.'),
            'widget': rules_table(1, 'fa6-solid:list-check', 'Relationship Rules', [
                ('Always has a direction', f'{gpill}(a)-[:TYPE]-&gt;(b)</code>'),
                ('Must have a type', f'{gpill}FRIEND</code>, {gpill}PURCHASED</code>'),
                ('Can have properties', 'date: "2024-01-01", weight: 5'),
            ]),
            'code': sql_blk('MATCH (a:Person {name: "Alice"})   -- find Alice\nMATCH (b:Person {name: "Bob"})     -- find Bob\nCREATE (a)-[:FRIEND]->(b)          -- link them\n-- Alice is now connected to Bob'),
            'tip_icon': 'fa6-solid:triangle-exclamation',
            'tip': f'<strong>Relationships always have a direction.</strong> Even if your data is bidirectional, you must pick one \u2014 Cypher can traverse {tp("both ways", 1)} regardless.',
        }),
        mk('fa6-solid:magnifying-glass', 'Cypher Queries', {
            'icon': 'fa6-solid:magnifying-glass', 'label': 'Cypher Queries',
            'subtitle': "Neo4j\u2019s query language", 'badge_label': 'Language', 'badge_icon': 'fa6-solid:code',
            'definition': defn(f'<strong>Cypher</strong> is the query language for Neo4j. You draw patterns using {cp("(nodes)", 2)} and {cp("-[:RELS]-&gt;", 2)} to describe what you want to find.'),
            'widget': operators_table(2, 'fa6-solid:terminal', 'Cypher Keywords', [
                ('MATCH', 'Find patterns', 'MATCH (p:Person)'),
                ('CREATE', 'Add data', 'CREATE (n:City {name:...})'),
                ('RETURN', 'Output results', 'RETURN p.name'),
                ('WHERE', 'Filter results', 'WHERE p.age > 25'),
            ]),
            'code': sql_blk('MATCH (p:Person)              -- find all Person nodes\nWHERE p.age > 25               -- filter by age\nRETURN p.name, p.city          -- output name and city\nORDER BY p.name                -- sort alphabetically'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>Cypher reads like ASCII art.</strong> The pattern {tp("(a)-[:FRIEND]-&gt;(b)", 2)} visually shows two nodes connected by a relationship \u2014 making queries intuitive.',
        }),
        mk('fa6-solid:diagram-project', 'Graph Patterns', {
            'icon': 'fa6-solid:diagram-project', 'label': 'Graph Patterns',
            'subtitle': 'Following paths through nodes', 'badge_label': 'Traversal', 'badge_icon': 'fa6-solid:route',
            'definition': defn(f'A <strong>graph pattern</strong> describes a path through connected nodes. You can chain multiple {cp("relationships", 3)} to traverse the graph in one query.'),
            'widget': rules_table(3, 'fa6-solid:list-check', 'Traversal Concepts', [
                (f'{cp("Single hop", 3)}', '(a)-[:FRIEND]-&gt;(b) \u2014 direct connection'),
                (f'{cp("Multi hop", 3)}', '(a)-[:FRIEND]-&gt;(b)-[:PURCHASED]-&gt;(p)'),
                (f'{cp("Variable depth", 3)}', '(a)-[:FRIEND*1..3]-&gt;(b) \u2014 1 to 3 hops'),
            ]),
            'code': sql_blk('MATCH (a:Person {name:"Alice"})    -- start at Alice\n  -[:FRIEND]->(friend)              -- find her friends\n  -[:PURCHASED]->(product)          -- what they bought\nRETURN product.name                 -- show product names'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>Graph queries stay fast even with deep paths.</strong> Unlike SQL JOINs, Neo4j follows {tp("direct pointers", 3)} between nodes \u2014 traversal speed does not depend on database size.',
        }),
    ]
)

# ────────────────────────── LESSON 07 ──────────────────────────────
L07 = make_section(
    'SQL strengths, NoSQL strengths, side-by-side comparison, and choosing the right database.',
    [
        mk('fa6-solid:table', 'SQL Strengths', {
            'icon': 'fa6-solid:table', 'label': 'SQL Strengths',
            'subtitle': 'Structured data and transactions', 'badge_label': 'Comparison', 'badge_icon': 'fa6-solid:scale-balanced',
            'definition': defn(f'<strong>SQL databases</strong> excel when your data has a fixed structure. They support {cp("ACID transactions", 0)} that guarantee every write is safe and consistent.'),
            'widget': rules_table(0, 'fa6-solid:list-check', 'SQL Advantages', [
                (f'{cp("ACID", 0)} transactions', f'{gpill}guaranteed</code> consistency'),
                ('Powerful JOINs', 'Combine data from multiple tables'),
                ('Mature ecosystem', 'Decades of tooling and support'),
                ('Best for', 'Banking, accounting, ERP systems'),
            ]),
            'code': py_block('import sqlite3                         # built-in SQL library\nconn = sqlite3.connect("bank.db")       # open database\nconn.execute("BEGIN TRANSACTION")       # start ACID block\nconn.execute("UPDATE accounts "         # safe transfer\n    "SET balance = balance - 100 "      # deduct amount\n    "WHERE id = 1")'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>Choose SQL when you need strong consistency.</strong> Financial systems depend on {tp("ACID guarantees", 0)} \u2014 every transaction fully succeeds or fully rolls back.',
        }),
        mk('fa6-solid:cubes', 'NoSQL Strengths', {
            'icon': 'fa6-solid:cubes', 'label': 'NoSQL Strengths',
            'subtitle': 'Flexibility and horizontal scaling', 'badge_label': 'Comparison', 'badge_icon': 'fa6-solid:scale-balanced',
            'definition': defn(f'<strong>NoSQL databases</strong> shine when your data changes shape often or needs to scale across servers. They trade strict consistency for {cp("speed", 1)} and {cp("flexibility", 1)}.'),
            'widget': rules_table(1, 'fa6-solid:list-check', 'NoSQL Advantages', [
                ('Flexible schema', f'{gpill}dynamic</code> \u2014 no ALTER TABLE'),
                ('Horizontal scaling', f'{gpill}distributed</code> across servers'),
                ('High write speed', 'Millions of writes per second'),
                ('Best for', 'Real-time apps, IoT, social networks'),
            ]),
            'code': py_block('from pymongo import MongoClient        # MongoDB driver\nclient = MongoClient("localhost")       # connect\ndb = client["app"]                      # select database\ndb.users.insert_one({                   # flexible schema\n    "name": "Alice",\n    "prefs": {"theme": "dark"}})'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>NoSQL handles unpredictable data shapes.</strong> If user records have optional fields that change often, a {tp("document database", 1)} avoids constant schema migrations.',
        }),
        mk('fa6-solid:scale-balanced', 'SQL vs NoSQL', {
            'icon': 'fa6-solid:scale-balanced', 'label': 'SQL vs NoSQL',
            'subtitle': 'Side-by-side comparison', 'badge_label': 'Side by Side', 'badge_icon': 'fa6-solid:code',
            'definition': defn(f'SQL and NoSQL are <strong>different tools for different problems</strong>. The right choice depends on your {cp("data shape", 2)} and {cp("access patterns", 2)}.'),
            'widget': comparison_table(2, 'fa6-solid:scale-balanced', 'SQL vs NoSQL', 'SQL', 'pink', 'NoSQL', 'violet', [
                ('Schema', 'Fixed, predefined', 'Flexible, dynamic'),
                ('Scaling', 'Vertical (bigger server)', 'Horizontal (more servers)'),
                ('Joins', f'{G}Built-in{GE}', f'{R}Not native{GE}'),
                ('Best for', 'Structured, relational', 'Unstructured, high volume'),
            ]),
            'code': py_block('# SQL: structured query\ncursor.execute("SELECT * FROM users "  # fixed schema\n    "WHERE city = \'LA\'")\n# NoSQL: flexible query\ndb.users.find({"city": "LA"})           # same result'),
            'tip_icon': 'fa6-solid:triangle-exclamation',
            'tip': f'<strong>There is no one-size-fits-all database.</strong> Many production systems use {tp("both SQL and NoSQL", 2)} together \u2014 SQL for transactions, NoSQL for caching.',
        }),
        mk('fa6-solid:route', 'Choosing a Database', {
            'icon': 'fa6-solid:route', 'label': 'Choosing a Database',
            'subtitle': 'Decision factors', 'badge_label': 'Decision', 'badge_icon': 'fa6-solid:route',
            'definition': defn(f'<strong>Choosing a database</strong> depends on four factors: data structure, query patterns, {cp("scale requirements", 3)}, and consistency needs.'),
            'widget': rules_table(3, 'fa6-solid:list-check', 'Decision Guide', [
                ('Fixed structure + relationships', f'{gpill}SQL</code> \u2014 PostgreSQL, MySQL'),
                ('Flexible documents', f'{gpill}Document</code> \u2014 MongoDB'),
                ('Fast key lookups', f'{gpill}Key-Value</code> \u2014 Redis'),
                ('Connected data', f'{gpill}Graph</code> \u2014 Neo4j'),
            ]),
            'code': py_block('decision = {\n    "structured": "PostgreSQL",      # fixed schema data\n    "flexible": "MongoDB",           # changing data shapes\n    "fast_cache": "Redis",           # speed-critical lookups\n    "connections": "Neo4j"           # relationship queries\n}'),
            'tip_icon': 'fa6-solid:lightbulb',
            'tip': f'<strong>Many companies use multiple databases.</strong> A common pattern is {tp("PostgreSQL", 3)} for transactions plus {tp("Redis", 3)} for caching \u2014 called polyglot persistence.',
        }),
    ]
)

# ── Apply replacements ──────────────────────────────────────────────
LESSONS = {
    "lesson01_what_is_nosql.html": L01,
    "lesson02_types_of_nosql_databases.html": L02,
    "lesson03_document_databases_mongodb.html": L03,
    "lesson04_key_value_databases_redis.html": L04,
    "lesson05_column_family_databases_cassandra.html": L05,
    "lesson06_graph_databases_neo4j.html": L06,
    "lesson07_sql_vs_nosql_choosing_the_right_database.html": L07,
}

for fname, new_html in LESSONS.items():
    fpath = os.path.join(BASE, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    matches = list(KC_RE.finditer(content))
    if len(matches) != 1:
        print(f"\u274c {fname}: found {len(matches)} key-concepts sections")
        continue
    new_content = content[:matches[0].start()] + new_html + content[matches[0].end():]
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"\u2705 {fname}: key-concepts replaced")

print("\nDone.")
