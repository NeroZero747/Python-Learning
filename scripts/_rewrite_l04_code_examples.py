"""Rewrite #code-examples section body in lesson04 per lesson-code-examples.prompt.md."""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_BODY = '''\n\n      <!-- Tab pill row -->
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">

        <button onclick="switchCeTab(0)" class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Loose Script</span>
        </button>

        <button onclick="switchCeTab(1)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Refactored Class</span>
        </button>

        <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Adding run()</span>
        </button>

      </div>

      <!-- ═══════════════════════════════════════ -->
      <!-- Panel 0 — Loose Script                 -->
      <!-- ═══════════════════════════════════════ -->
      <div class="ce-panel ce-panel-anim" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Loose Script</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Reports</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Functions</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Sequential</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">

            <!-- What This Does -->
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This script defines three separate <strong class="text-gray-800">functions</strong> and calls them one by one at the bottom. It works, but every new step must be added manually in the correct order.</p>
              </div>
            </div>

            <!-- Code block -->
            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">report_script.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python"># Loose script — three functions with no grouping

def load_data():                # defines the first step
    print("Loading data...")

def clean_data():               # defines the second step
    print("Cleaning data...")

def save_report():              # defines the third step
    print("Report saved!")

# call each function manually, in the correct order
load_data()                     # step 1
clean_data()                    # step 2
save_report()                   # step 3</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python report_script.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">Loading data...<br>Cleaning data...<br>Report saved!</div>
              </div>
            </div>

            <!-- Amber tip -->
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">As your script grows, tracking down the call section at the bottom to add each new step becomes error-prone and easy to miss.</p>
            </div>

          </div>
        </div>
      </div>

      <!-- ═══════════════════════════════════════ -->
      <!-- Panel 1 — Refactored Class             -->
      <!-- ═══════════════════════════════════════ -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Refactored Class</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Reports</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">class</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">self</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">

            <!-- What This Does -->
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This script moves the three functions inside a <strong class="text-gray-800">class</strong> as methods. The only change to each function is adding <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">self</code> as its first parameter — the logic inside every function stays exactly the same.</p>
              </div>
            </div>

            <!-- Code block -->
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
                <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:                  # class header — groups all three methods

    def load_data(self):             # same logic, self added as first param
        print("Loading data...")

    def clean_data(self):            # same logic, self added as first param
        print("Cleaning data...")

    def save_report(self):           # same logic, self added as first param
        print("Report saved!")

report = ReportRunner()              # create one object from the class
report.load_data()                   # call step 1 via the object
report.clean_data()                  # call step 2 via the object
report.save_report()                 # call step 3 via the object</code></pre>
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

            <!-- Amber tip -->
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">The output never changes when you refactor — that is the signal that tells you the restructuring worked correctly.</p>
            </div>

          </div>
        </div>
      </div>

      <!-- ═══════════════════════════════════════ -->
      <!-- Panel 2 — Adding run()                 -->
      <!-- ═══════════════════════════════════════ -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Adding run()</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Reports</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">run()</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Methods</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">

            <!-- What This Does -->
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This script adds a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">run()</code> method that calls all three steps in order from inside the class. Your main script shrinks to two lines, and you never need to remember which steps exist or what order they run in.</p>
              </div>
            </div>

            <!-- Code block -->
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
                <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:                  # the container that holds all methods

    def load_data(self):             # step 1 — load the data
        print("Loading data...")

    def clean_data(self):            # step 2 — clean the data
        print("Cleaning data...")

    def save_report(self):           # step 3 — save the report
        print("Report saved!")

    def run(self):                   # calls all three steps in order
        self.load_data()             # runs step 1
        self.clean_data()            # runs step 2
        self.save_report()           # runs step 3

report = ReportRunner()              # create the object
report.run()                         # one line triggers everything</code></pre>
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

            <!-- Amber tip -->
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Once a class has a <code class="text-[11px] bg-orange-50 px-1.5 py-0.5 rounded font-mono border border-orange-100">run()</code> method, you can drop it into any other script and trigger the whole pipeline with just one line.</p>
            </div>

          </div>
        </div>
      </div>

    '''

html = TARGET.read_text(encoding='utf-8')

# Locate the code-examples section body div
ce_start = html.find('id="code-examples"')
if ce_start == -1:
    print('❌ id="code-examples" not found'); sys.exit(1)

BODY_OPEN = '<div class="bg-white px-8 py-7 space-y-6">'
body_start = html.find(BODY_OPEN, ce_start)
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

# ── Verification ──────────────────────────────────────────────────────────────
result = TARGET.read_text(encoding='utf-8')
ce2 = result.find('id="code-examples"')
sec_s = result.rfind('<section', 0, ce2)
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
    # Tab pills — all fa6-solid:code
    ('Tab 1 active: Loose Script',              '>Loose Script<'),
    ('Tab 2: Refactored Class',                 '>Refactored Class<'),
    ('Tab 3: Adding run()',                      '>Adding run()<'),
    ('All tabs use fa6-solid:code (3 occurrences)', s.count('data-icon="fa6-solid:code"') >= 6),  # 3 tabs + 3 header icons
    # Panel headers — badges row
    ('Panel 1 watermark: 01',                   '>01<'),
    ('Panel 2 watermark: 02',                   '>02<'),
    ('Panel 3 watermark: 03',                   '>03<'),
    ('All 3 Beginner badges',                   s.count('fa6-solid:leaf') == 3),
    ('Panel 1 domain pill: Reports (×3)',       s.count('>Reports<') >= 3),
    ('Panel 1 keyword: Functions',              '>Functions<'),
    ('Panel 1 keyword: Sequential',             '>Sequential<'),
    ('Panel 2 keyword: class',                  '>class<'),
    ('Panel 2 keyword: self',                   '>self<'),
    ('Panel 3 keyword: run()',                   s.count('>run()<') >= 1),
    ('Panel 3 keyword: Methods',                '>Methods<'),
    # task-box / What This Does (3 panels)
    ('3× task-box containers',                  s.count('task-box') == 3),
    ('3× clipboard-list icons',                 s.count('fa6-solid:clipboard-list') == 3),
    ('3× What This Does headings',              s.count('What This Does') == 3),
    # Code blocks — no traffic-light dots
    ('No traffic-light dots anywhere',          'bg-red-400/80' not in s),
    # Combined terminal panes (3 total)
    ('3× combined terminal panes bg-[#11111b]', s.count('bg-[#11111b]') == 3),
    ('No separate terminal output blocks',      'Terminal output' not in s),
    # Filenames
    ('Panel 1 filename: report_script.py',      'report_script.py'),
    ('Panel 2 filename: report_runner.py',      s.count('report_runner.py') >= 2),
    # Terminal commands
    ('Panel 1 cmd: $ python report_script.py',  '$ python report_script.py'),
    ('Panel 2/3 cmd: $ python report_runner.py', '$ python report_runner.py'),
    # Output lines in combined panes
    ('Loading data... in pane',                 'Loading data...<br>Cleaning data...<br>Report saved!'),
    # Tips — one sentence each
    ('Panel 1 tip: error-prone',                'error-prone'),
    ('Panel 2 tip: output never changes',       'output never changes'),
    ('Panel 3 tip: one line triggers',          'trigger the whole pipeline with just one line'),
    # All 3 amber tips use circle-info
    ('3× circle-info icons',                    s.count('fa6-solid:circle-info') == 3),
    # Panel 2/3 hidden class
    ('Panel 2 hidden',                          'ce-panel ce-panel-anim hidden'),
    # Section structure unchanged
    ('Section header: fa6-solid:code',          'data-icon="fa6-solid:code"'),
    ('space-y-6 preserved',                     'space-y-6'),
]

passed, failed = 0, 0
for label, check in checks:
    if isinstance(check, bool):
        ok = check
    else:
        ok = check in s
    print(f'  {"✅" if ok else "❌"} {label}')
    if ok: passed += 1
    else: failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
