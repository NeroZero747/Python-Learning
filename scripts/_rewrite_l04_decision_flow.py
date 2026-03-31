"""Rewrite #decision-flow section body in lesson04 per lesson-decision-flow.prompt.md."""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_BODY = '''\n\n      <!-- Block 1 — Intro paragraph -->
      <p class="text-sm text-gray-600 leading-relaxed">When you refactor a script, you follow a repeatable sequence called <strong class="text-gray-800">structured reorganisation</strong> — each step reshapes the code without ever changing what it outputs.</p>

      <!-- Block 2 — Flowchart -->
      <div class="rounded-2xl border border-gray-100 bg-gray-50 px-5 pt-4 pb-6 overflow-x-auto">
        <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-4">How Python Reads Your Program — Top to Bottom</p>
        <div class="flex items-start gap-0 min-w-[640px]">

          <!-- Node 1 — Program Starts (circle, pink) -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-14 h-14 rounded-full bg-gradient-to-br from-pink-500 to-rose-600 flex items-center justify-center shadow-lg ring-4 ring-pink-100">
              <span class="iconify text-white text-lg" data-icon="fa6-solid:play"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-2 text-center leading-tight">Program<br>Starts</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">Python begins at line 1</p>
          </div>

          <!-- Arrow 1 — pink→violet -->
          <div class="flex-1 flex items-center" style="padding-top:28px;">
            <div class="h-0.5 flex-1 bg-gradient-to-r from-pink-300 to-violet-300"></div>
            <span class="iconify text-violet-300 text-xs -ml-px" data-icon="fa6-solid:chevron-right"></span>
          </div>

          <!-- Node 2 — Identify Functions (rounded square, violet) -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-violet-500 to-purple-600 flex items-center justify-center shadow-lg ring-4 ring-violet-100">
              <span class="iconify text-white text-lg" data-icon="fa6-solid:magnifying-glass"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-2 text-center leading-tight">Identify<br>Functions</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">Find functions that share one job</p>
          </div>

          <!-- Arrow 2 — violet→blue -->
          <div class="flex-1 flex items-center" style="padding-top:28px;">
            <div class="h-0.5 flex-1 bg-gradient-to-r from-violet-300 to-blue-300"></div>
            <span class="iconify text-blue-300 text-xs -ml-px" data-icon="fa6-solid:chevron-right"></span>
          </div>

          <!-- Node 3 — Group into Class (diamond, blue) -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-12 h-12 rounded-xl rotate-45 bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center shadow-lg ring-4 ring-blue-100" style="margin-top:4px;">
              <span class="iconify text-white text-lg -rotate-45" data-icon="fa6-solid:cube"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-3 text-center leading-tight">Group into<br>Class</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">Write class Name: in Python</p>
          </div>

          <!-- Arrow 3 — blue→emerald -->
          <div class="flex-1 flex items-center" style="padding-top:28px;">
            <div class="h-0.5 flex-1 bg-gradient-to-r from-blue-300 to-emerald-300"></div>
            <span class="iconify text-emerald-300 text-xs -ml-px" data-icon="fa6-solid:chevron-right"></span>
          </div>

          <!-- Node 4 — Add run() Method (rounded square, emerald) -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-emerald-500 to-teal-600 flex items-center justify-center shadow-lg ring-4 ring-emerald-100">
              <span class="iconify text-white text-lg" data-icon="fa6-solid:play"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-2 text-center leading-tight">Add run()<br>Method</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">Call all steps in one go</p>
          </div>

          <!-- Arrow 4 — emerald→gray -->
          <div class="flex-1 flex items-center" style="padding-top:28px;">
            <div class="h-0.5 flex-1 bg-gradient-to-r from-emerald-300 to-gray-300"></div>
            <span class="iconify text-gray-300 text-xs -ml-px" data-icon="fa6-solid:chevron-right"></span>
          </div>

          <!-- Node 5 — Program Ends (circle, gray) -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-14 h-14 rounded-full bg-gradient-to-br from-gray-400 to-gray-600 flex items-center justify-center shadow-lg ring-4 ring-gray-100">
              <span class="iconify text-white text-lg" data-icon="fa6-solid:flag-checkered"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-2 text-center leading-tight">Program<br>Ends</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">Result is shown</p>
          </div>

        </div>
      </div>

      <!-- Block 3 — Sub-heading + paragraph -->
      <div class="space-y-2">
        <p class="text-sm font-semibold text-gray-800">Refactoring Step by Step — the Default Pattern</p>
        <p class="text-sm text-gray-600 leading-relaxed">You start by finding functions that work together — like <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">load_data</code>, <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">clean_data</code>, and <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">save_report</code>. You then write a class, indent those functions inside it, and add <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">self</code> as the first parameter to each. Finally, you add a <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">run()</code> method that calls all of them in order. Every time you follow this pattern, the script produces exactly the same output as before.</p>
      </div>

      <!-- Block 4 — Code block with combined terminal output -->
      <div class="space-y-2">
        <p class="text-sm text-gray-600 leading-relaxed">Here is the refactored <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">ReportRunner</code> — notice how each method has <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">self</code> as its first parameter and <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">run()</code> calls all three steps in order:</p>
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">report_runner.py</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code">
            <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:              # Step 1 — create the class container
    def load_data(self):         # Step 2 — move load_data in as a method
        print("Loading data...")

    def clean_data(self):        # Step 3 — move clean_data in as a method
        print("Cleaning data...")

    def save_report(self):       # Step 4 — move save_report in as a method
        print("Report saved!")

    def run(self):               # Step 5 — add run() to call all steps
        self.load_data()
        self.clean_data()
        self.save_report()

report = ReportRunner()          # create one object from the class
report.run()                     # one line triggers the full pipeline</code></pre>
          </div>
          <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
            <div class="flex items-center gap-2 mb-1.5">
              <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
              <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
              <span class="text-[10px] text-gray-600 font-mono">$ python report_runner.py</span>
            </div>
            <div class="font-mono text-xs text-emerald-400 leading-relaxed">Loading data...<br>Cleaning data...<br>Report saved!</div>
          </div>
        </div>
      </div>

      <!-- Block 5 — Three concept cards -->
      <div class="space-y-3">
        <p class="text-xs font-bold uppercase tracking-widest text-brand">The Three Concepts in Any Refactoring</p>
        <p class="text-sm text-gray-600 leading-relaxed">Every refactoring you ever do in Python uses these three building blocks — master them once and you can restructure any script.</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">

          <!-- Card 1 — blue -->
          <div class="rounded-xl border border-blue-100 bg-white overflow-hidden shadow-sm hover:shadow-md hover:border-blue-200 transition-all">
            <div class="h-1 bg-gradient-to-r from-blue-500 to-blue-400"></div>
            <div class="px-4 py-4">
              <div class="flex items-center gap-2.5 mb-2.5">
                <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-blue-50 shrink-0">
                  <span class="iconify text-blue-500 text-base" data-icon="fa6-solid:arrows-rotate"></span>
                </span>
                <div>
                  <p class="text-sm font-bold text-gray-800 leading-tight">Refactoring</p>
                  <p class="text-[10px] text-gray-400 italic leading-tight">Same output — cleaner shape</p>
                </div>
              </div>
              <p class="text-xs text-gray-500 leading-relaxed">Refactoring only changes how your code is organised, never what it returns or prints.</p>
            </div>
          </div>

          <!-- Card 2 — emerald -->
          <div class="rounded-xl border border-emerald-100 bg-white overflow-hidden shadow-sm hover:shadow-md hover:border-emerald-200 transition-all">
            <div class="h-1 bg-gradient-to-r from-emerald-500 to-emerald-400"></div>
            <div class="px-4 py-4">
              <div class="flex items-center gap-2.5 mb-2.5">
                <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-emerald-50 shrink-0">
                  <span class="iconify text-emerald-500 text-base" data-icon="fa6-solid:cube"></span>
                </span>
                <div>
                  <p class="text-sm font-bold text-gray-800 leading-tight">The Class</p>
                  <p class="text-[10px] text-gray-400 italic leading-tight">Your labelled container</p>
                </div>
              </div>
              <p class="text-xs text-gray-500 leading-relaxed">Writing <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">class ReportRunner:</code> creates a named container that holds all related methods together.</p>
            </div>
          </div>

          <!-- Card 3 — violet -->
          <div class="rounded-xl border border-violet-100 bg-white overflow-hidden shadow-sm hover:shadow-md hover:border-violet-200 transition-all">
            <div class="h-1 bg-gradient-to-r from-violet-500 to-violet-400"></div>
            <div class="px-4 py-4">
              <div class="flex items-center gap-2.5 mb-2.5">
                <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-violet-50 shrink-0">
                  <span class="iconify text-violet-500 text-base" data-icon="fa6-solid:play"></span>
                </span>
                <div>
                  <p class="text-sm font-bold text-gray-800 leading-tight">The run() Method</p>
                  <p class="text-[10px] text-gray-400 italic leading-tight">One call, all steps</p>
                </div>
              </div>
              <p class="text-xs text-gray-500 leading-relaxed">Adding a <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">run()</code> method means the rest of your program only ever needs to call one line to run the whole workflow.</p>
            </div>
          </div>

        </div>
      </div>

      <!-- Block 6 — Closing amber tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">Once you have refactored a script, you can reuse it anywhere in your project with just two lines — one to create the object and one to call <code class="text-[11px] bg-orange-50 px-1.5 py-0.5 rounded font-mono border border-orange-100">run()</code>. That same two-line pattern works whether your class has three methods or thirty.</p>
      </div>

    '''

html = TARGET.read_text(encoding='utf-8')

# Locate the decision-flow section body div
df_start = html.find('id="decision-flow"')
if df_start == -1:
    print('❌ id="decision-flow" not found'); sys.exit(1)

BODY_OPEN = '<div class="bg-white px-8 py-7 space-y-6">'
body_start = html.find(BODY_OPEN, df_start)
if body_start == -1:
    print('❌ body div not found'); sys.exit(1)

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
    print('❌ Closing </div> of body not found'); sys.exit(1)

old = html[content_start:body_end]
print(f'  Old body: {len(old):,} chars')
print(f'  New body: {len(NEW_BODY):,} chars')

html = html[:content_start] + NEW_BODY + html[body_end:]
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# Verification
result = TARGET.read_text(encoding='utf-8')
df2 = result.find('id="decision-flow"')
sec_s = result.rfind('<section', 0, df2)
search2 = result[sec_s:]
depth2, sec_e, i = 0, -1, 0
while i < len(search2):
    if search2[i:].startswith('<section'):
        depth2 += 1; i += len('<section')
    elif search2[i:].startswith('</section>'):
        depth2 -= 1
        if depth2 == 0:
            sec_e = sec_s + i + len('</section>'); break
        i += len('</section>')
    else:
        i += 1
s = result[sec_s:sec_e]

checks = [
    # Block 1
    ('Intro: structured reorganisation bold',    '<strong class="text-gray-800">structured reorganisation</strong>'),
    # Block 2 — flowchart
    ('Chart title: How Python Reads',            'How Python Reads Your Program — Top to Bottom'),
    ('Node 1: Program Starts',                   '>Program<br>Starts<'),
    ('Node 1: Python begins at line 1',          'Python begins at line 1'),
    ('Node 1: play icon',                        'data-icon="fa6-solid:play"'),
    ('Node 1: w-14 h-14',                        'w-14 h-14 rounded-full bg-gradient-to-br from-pink-500'),
    ('Node 2: Identify Functions label',         '>Identify<br>Functions<'),
    ('Node 2: magnifying-glass icon',            'data-icon="fa6-solid:magnifying-glass"'),
    ('Node 3: Group into Class label',           '>Group into<br>Class<'),
    ('Node 3: diamond (rotate-45)',              'rotate-45 bg-gradient-to-br from-blue-500'),
    ('Node 4: Add run() Method label',           '>Add run()<br>Method<'),
    ('Node 5: Program Ends',                     '>Program<br>Ends<'),
    ('Node 5: Result is shown',                  'Result is shown'),
    ('Node 5: flag-checkered icon',              'data-icon="fa6-solid:flag-checkered"'),
    ('Arrow chevrons match dest colour',         'text-violet-300 text-xs'),
    ('Arrow 2 blue chevron',                     'text-blue-300 text-xs'),
    ('Arrow 3 emerald chevron',                  'text-emerald-300 text-xs'),
    ('Arrow 4 gray chevron',                     'text-gray-300 text-xs'),
    # Block 3
    ('Sub-heading: Refactoring Step by Step',    '>Refactoring Step by Step — the Default Pattern<'),
    # Block 4 — code block
    ('Code: no traffic-light dots',              'bg-red-400/80'),   # must be ABSENT
    ('Code: combined terminal pane',             'bg-[#11111b]'),
    ('Code: no separate terminal block',         'Terminal output'),  # must be ABSENT (separate block removed)
    ('Code: filename report_runner.py',          'report_runner.py'),
    ('Code: $ python terminal cmd',              '$ python report_runner.py'),
    ('Code: emerald output text',                'text-emerald-400 leading-relaxed'),
    ('Code: Loading data output',                'Loading data...'),
    ('Code: Report saved output',                'Report saved!'),
    # Block 5 — cards
    ('Cards label: Three Concepts',              'The Three Concepts in Any Refactoring'),
    ('Card 1 blue top bar',                      'from-blue-500 to-blue-400'),
    ('Card 2 emerald top bar',                   'from-emerald-500 to-emerald-400'),
    ('Card 3 violet top bar',                    'from-violet-500 to-violet-400'),
    ('Card 1 arrows-rotate icon',                'fa6-solid:arrows-rotate'),
    ('Card 2 cube icon',                         'fa6-solid:cube'),
    ('Card 2 code element: class ReportRunner',  'class ReportRunner:'),
    ('Card 3 run() code element',                'run()'),
    # Block 6
    ('Amber tip: circle-info',                   'fa6-solid:circle-info'),
    ('Amber tip: two lines content',             'That same two-line pattern'),
    # Structure
    ('Section header unchanged',                 'fa6-solid:route'),
    ('space-y-6 preserved',                      'space-y-6'),
]

must_absent = {'Code: no traffic-light dots', 'Code: no separate terminal block'}

passed, failed = 0, 0
for label, needle in checks:
    if label in must_absent:
        ok = needle not in s
        note = ' (absent ✓)' if ok else ' (FOUND — should be absent ❌)'
    else:
        ok = needle in s
        note = ''
    print(f'  {"✅" if ok else "❌"} {label}{note}')
    if ok: passed += 1
    else: failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
