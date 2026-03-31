"""Rewrite #comparison section in lesson04 per lesson-comparison.prompt.md."""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

# ── New section header (shell fix: title + subtitle only; keep scale-balanced icon per copilot-instructions.md) ──
OLD_HEADER = '''        <h2 class="text-xl font-bold text-gray-900 leading-tight">Comparison</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Python class vs. SQL stored procedure vs. Excel macro</p>'''
NEW_HEADER = '''        <h2 class="text-xl font-bold text-gray-900 leading-tight">SQL / Excel Comparison</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">How this topic compares across Python, SQL, and Excel</p>'''

# ── New body ───────────────────────────────────────────────────────────────────
NEW_BODY = '''\n\n      <!-- 1 · Intro paragraph -->
      <p class="text-sm text-gray-600 leading-relaxed">If you already use SQL stored procedures or Excel macros, you already know the idea behind a Python class — all three let you group a set of steps under one name and run everything with a single call.</p>

      <!-- 2 · Tool header cards -->
      <div class="grid grid-cols-3 gap-3">
        <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-indigo-600 text-white">
          <span class="iconify text-lg" data-icon="fa6-brands:python"></span> Python
        </div>
        <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-orange-600 text-white">
          <span class="iconify text-lg" data-icon="fa6-solid:database"></span> SQL
        </div>
        <div class="flex items-center gap-2 px-4 py-3 rounded-xl font-semibold text-sm bg-emerald-600 text-white">
          <span class="iconify text-lg" data-icon="fa6-solid:table"></span> Excel
        </div>
      </div>

      <!-- 3 · Concept rows -->

      <!-- Row 1 — the container -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:box"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">the container</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">class Name:</code>
            <p class="text-xs text-gray-500 leading-relaxed">You open a class block with <code class="font-mono">class</code> followed by the name — everything indented inside belongs to it.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">CREATE PROCEDURE</code>
            <p class="text-xs text-gray-500 leading-relaxed">You declare a procedure with <code class="font-mono">CREATE PROCEDURE</code> — all the SQL inside runs when you call it.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">Sub MacroName()</code>
            <p class="text-xs text-gray-500 leading-relaxed">You open a macro with <code class="font-mono">Sub</code> followed by the name — all VBA lines inside run when the macro is triggered.</p>
          </div>
        </div>
      </div>

      <!-- Row 2 — the steps inside -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:list-check"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">the steps inside</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">def method(self):</code>
            <p class="text-xs text-gray-500 leading-relaxed">Each step is a method — a function defined with <code class="font-mono">def</code> and <code class="font-mono">self</code> inside the class block.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">SQL statements</code>
            <p class="text-xs text-gray-500 leading-relaxed">Each step is a SQL statement — <code class="font-mono">SELECT</code>, <code class="font-mono">INSERT</code>, or <code class="font-mono">DELETE</code> — written inside the procedure body.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">VBA lines</code>
            <p class="text-xs text-gray-500 leading-relaxed">Each step is a VBA line — a recorded or written instruction that Excel carries out when the macro runs.</p>
          </div>
        </div>
      </div>

      <!-- Row 3 — call it once -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:play"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">call it once</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">object.run()</code>
            <p class="text-xs text-gray-500 leading-relaxed">You create one object from the class and call <code class="font-mono">run()</code> — one line triggers all the steps inside.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">EXEC proc_name</code>
            <p class="text-xs text-gray-500 leading-relaxed">You run the whole procedure with a single <code class="font-mono">EXEC</code> statement — all internal SQL steps fire in order.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">Run Macro</code>
            <p class="text-xs text-gray-500 leading-relaxed">You click the Run Macro button — Excel executes every VBA line in the <code class="font-mono">Sub</code> from top to bottom.</p>
          </div>
        </div>
      </div>

      <!-- Row 4 — reusable? -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
            <span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:arrows-rotate"></span>
          </span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">reusable?</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Python</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">yes — any script</code>
            <p class="text-xs text-gray-500 leading-relaxed">You can import the class into any other Python file and create a fresh object whenever you need it.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">SQL</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">yes — any query</code>
            <p class="text-xs text-gray-500 leading-relaxed">You can call the stored procedure from any other query in the same database — no need to rewrite the steps.</p>
          </div>
          <div class="px-4 py-4 flex flex-col gap-2">
            <span class="text-xs text-gray-400">Excel</span>
            <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">same workbook only</code>
            <p class="text-xs text-gray-500 leading-relaxed">The macro is reusable, but only within the workbook it was saved in — sharing it requires exporting the VBA module.</p>
          </div>
        </div>
      </div>

      <!-- 4 · Centered divider + 3-column code blocks -->
      <div>
        <div class="flex items-center gap-3 mb-4">
          <span class="flex-1 h-px bg-gray-100"></span>
          <div class="flex items-center gap-2 shrink-0">
            <span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-sm" data-icon="fa6-solid:code-compare"></span>
            </span>
            <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D]">Same report pipeline, three tools</p>
          </div>
          <span class="flex-1 h-px bg-gray-100"></span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 items-stretch">

          <!-- Python column -->
          <div class="flex flex-col">
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">Python code</p>
            <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">
              <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                <div class="flex items-center gap-2">
                  <span class="iconify" data-icon="logos:python" data-width="16" data-height="16"></span>
                  <span class="text-xs font-semibold text-gray-400">Python</span>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-python"># create the object, then run
report = ReportRunner()
report.run()</code></pre>
            </div>
          </div>

          <!-- SQL column -->
          <div class="flex flex-col">
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">SQL query</p>
            <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">
              <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                <div class="flex items-center gap-2">
                  <span class="iconify text-orange-400" data-icon="fa6-solid:database"></span>
                  <span class="text-xs font-semibold text-gray-400">SQL</span>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-sql">CREATE PROCEDURE RunReport AS
BEGIN
    EXEC LoadData;
    EXEC CleanData;
    EXEC SaveReport;
END;
EXEC RunReport;</code></pre>
            </div>
          </div>

          <!-- Excel column -->
          <div class="flex flex-col">
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2 flex items-center gap-1.5">Excel formula</p>
            <div class="relative rounded-xl overflow-hidden flex flex-col flex-1 bg-code">
              <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                <div class="flex items-center gap-2">
                  <span class="iconify text-green-400" data-icon="fa6-solid:table"></span>
                  <span class="text-xs font-semibold text-gray-400">Excel</span>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <pre class="overflow-x-auto flex-1 pre-reset"><code class="language-text">Sub RunReport()
    Call LoadData
    Call CleanData
    Call SaveReport
End Sub</code></pre>
            </div>
          </div>

        </div>

        <p class="text-xs text-gray-400 mt-2">All three group a set of steps under one callable name and run the full sequence with a single trigger — the same result, just written in a different tool.</p>
      </div>

      <!-- 5 · Closing amber tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">Your SQL or Excel experience gives you a head start — a Python class is just the Python way of doing what you already do with stored procedures and macros. You are not learning a new concept; you are learning a new syntax for a familiar idea.</p>
      </div>

    '''

# ── Apply changes ──────────────────────────────────────────────────────────────
html = TARGET.read_text(encoding='utf-8')

# 1. Fix section header title + subtitle
if OLD_HEADER not in html:
    print('❌ Old header not found'); sys.exit(1)
html = html.replace(OLD_HEADER, NEW_HEADER, 1)

# 2. Fix body space-y-6 → space-y-5 inside comparison section only
comp_idx = html.find('id="comparison"')
body_marker = '<div class="bg-white px-8 py-7 space-y-6">'
body_pos = html.find(body_marker, comp_idx)
if body_pos != -1 and body_pos < comp_idx + 5000:
    html = html[:body_pos] + '<div class="bg-white px-8 py-7 space-y-5">' + html[body_pos + len(body_marker):]
    print('  ✅ space-y-6 → space-y-5')
else:
    print('  ℹ️  body already uses space-y-5 or not found within section')

# 3. Replace body content
comp_idx2 = html.find('id="comparison"')
BODY_OPEN = '<div class="bg-white px-8 py-7 space-y-5">'
body_start = html.find(BODY_OPEN, comp_idx2)
if body_start == -1:
    print('❌ body div not found after header fix'); sys.exit(1)

content_start = body_start + len(BODY_OPEN)
search = html[content_start:]
depth, body_end, i = 1, -1, 0
while i < len(search):
    if search[i:].startswith('<div'):
        depth += 1; i += 4
    elif search[i:].startswith('</div>'):
        depth -= 1
        if depth == 0:
            body_end = content_start + i; break
        i += 6
    else:
        i += 1

if body_end == -1:
    print('❌ Closing </div> not found'); sys.exit(1)

old = html[content_start:body_end]
print(f'  Old body: {len(old):,} chars')
print(f'  New body: {len(NEW_BODY):,} chars')

html = html[:content_start] + NEW_BODY + html[body_end:]
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# ── Verification ──────────────────────────────────────────────────────────────
result = TARGET.read_text(encoding='utf-8')
idx = result.find('id="comparison"')
sec_s = result.rfind('<section', 0, idx)
search2 = result[sec_s:]
depth2, sec_e, i = 0, -1, 0
while i < len(search2):
    if search2[i:].startswith('<section'): depth2 += 1; i += len('<section')
    elif search2[i:].startswith('</section>'):
        depth2 -= 1
        if depth2 == 0: sec_e = sec_s + i + len('</section>'); break
        i += len('</section>')
    else: i += 1
s = result[sec_s:sec_e]

checks = [
    # Header
    ('Header: SQL / Excel Comparison',          '>SQL / Excel Comparison<'),
    ('Header subtitle correct',                 'How this topic compares across Python, SQL, and Excel'),
    ('Header icon: scale-balanced preserved',   'fa6-solid:scale-balanced'),
    # Body wrapper
    ('Body: space-y-5',                         'space-y-5'),
    # Intro
    ('Intro: If you already',                   'If you already use SQL stored procedures'),
    # Tool header cards
    ('Tool card: Python indigo',                'bg-indigo-600 text-white'),
    ('Tool card: SQL orange',                   'bg-orange-600 text-white'),
    ('Tool card: Excel emerald',                'bg-emerald-600 text-white'),
    ('Tool card: fa6-brands:python',            'fa6-brands:python'),
    # Concept rows — labels
    ('Row 1 label: the container',              'the container'),
    ('Row 2 label: the steps inside',           'the steps inside'),
    ('Row 3 label: call it once',               'call it once'),
    ('Row 4 label: reusable?',                  'reusable?'),
    # Row icons
    ('Row 1 icon: fa6-solid:box',               'data-icon="fa6-solid:box"'),
    ('Row 2 icon: fa6-solid:list-check',        'data-icon="fa6-solid:list-check"'),
    ('Row 3 icon: fa6-solid:play',              'data-icon="fa6-solid:play"'),
    ('Row 4 icon: fa6-solid:arrows-rotate',     'data-icon="fa6-solid:arrows-rotate"'),
    # Term chips — indigo/orange/emerald
    ('Row 1 Py chip: class Name:',              'bg-indigo-50 text-indigo-700'),
    ('Row 1 SQL chip: CREATE PROCEDURE',        'bg-orange-50 text-orange-700'),
    ('Row 1 XL chip: Sub MacroName()',          'bg-emerald-50 text-emerald-700'),
    # Divider
    ('Divider: code-compare icon',              'fa6-solid:code-compare'),
    ('Divider: Same report pipeline',           'Same report pipeline, three tools'),
    ('Divider: centered hairlines',             'flex-1 h-px bg-gray-100'),
    # Code blocks — no traffic-light dots
    ('No traffic-light dots',                   'bg-red-400/80' not in s),
    # Column labels
    ('Python code column label',                '>Python code<'),
    ('SQL query column label',                  '>SQL query<'),
    ('Excel formula column label',              '>Excel formula<'),
    # Language classes
    ('Python: language-python',                 'language-python'),
    ('SQL: language-sql',                       'language-sql'),
    ('Excel: language-text',                    'language-text'),
    # Code content
    ('Python code: ReportRunner()',             'report = ReportRunner()'),
    ('Python code: report.run()',               'report.run()'),
    ('SQL code: CREATE PROCEDURE RunReport',    'CREATE PROCEDURE RunReport AS'),
    ('SQL code: EXEC RunReport',                'EXEC RunReport;'),
    ('Excel code: Sub RunReport()',             'Sub RunReport()'),
    ('Excel code: Call LoadData',               'Call LoadData'),
    # Caption
    ('Caption: All three…',                     'All three group'),
    ('Caption: same result',                    'same result, just written in a different tool'),
    # Amber tip
    ('Amber tip: circle-info',                  'fa6-solid:circle-info'),
    ('Amber tip: head start bridge',            'gives you a head start'),
]

passed, failed = 0, 0
for label, check in checks:
    ok = check if isinstance(check, bool) else (check in s)
    print(f'  {"✅" if ok else "❌"} {label}')
    if ok: passed += 1
    else: failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
