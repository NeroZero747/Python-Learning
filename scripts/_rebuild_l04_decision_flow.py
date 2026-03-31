"""
Replace <section id="decision-flow"> in lesson04.
Keep the 5-node flowchart structure. Replace DataPipeline with ReportRunner.
Add proper explanation text + full terminal output block.
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_SECTION = '''<section id="decision-flow" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:route"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Decision Flow</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">How to move a script into a class — step by step</p>
      </div>
    </div>

    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Intro paragraph -->
      <p class="text-sm text-gray-600 leading-relaxed">Every refactoring job follows the same five steps. You identify which functions belong together, create a class to hold them, move each function in as a method, then create an object and call <strong class="text-gray-800">run()</strong> to trigger everything in one go.</p>

      <!-- Flowchart -->
      <div class="rounded-2xl border border-gray-100 bg-gray-50 px-5 pt-4 pb-6 overflow-x-auto">
        <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-4">The Refactoring Process — Five Steps</p>
        <div class="flex items-start gap-0 min-w-[640px]">

          <!-- Node 1 — Program Starts (circle, pink) -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-16 h-16 rounded-full bg-gradient-to-br from-pink-500 to-rose-600 flex items-center justify-center shadow-lg ring-4 ring-pink-100">
              <span class="iconify text-white text-xl" data-icon="fa6-solid:play"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-2 text-center leading-tight">Identify<br>functions</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">Find related functions in your script</p>
          </div>

          <!-- Arrow 1 -->
          <div class="flex items-center flex-1" style="padding-top:28px;">
            <div class="h-0.5 flex-1 bg-gradient-to-r from-pink-300 to-violet-300"></div>
            <span class="iconify text-gray-400 text-sm -ml-1" data-icon="fa6-solid:chevron-right"></span>
          </div>

          <!-- Node 2 — Create a class (rounded square, violet) -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-violet-500 to-purple-600 flex items-center justify-center shadow-lg ring-4 ring-violet-100">
              <span class="iconify text-white text-xl" data-icon="fa6-solid:cube"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-2 text-center leading-tight">Create<br>class</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">Write class Name: at the top</p>
          </div>

          <!-- Arrow 2 -->
          <div class="flex items-center flex-1" style="padding-top:28px;">
            <div class="h-0.5 flex-1 bg-gradient-to-r from-violet-300 to-blue-300"></div>
            <span class="iconify text-gray-400 text-sm -ml-1" data-icon="fa6-solid:chevron-right"></span>
          </div>

          <!-- Node 3 — Move functions (diamond, blue) -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-12 h-12 rounded-xl rotate-45 bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center shadow-lg ring-4 ring-blue-100" style="margin-top:4px;">
              <span class="iconify text-white text-xl -rotate-45" data-icon="fa6-solid:code-branch"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-3 text-center leading-tight">Move into<br>methods</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">Add def &amp; self to each function</p>
          </div>

          <!-- Arrow 3 -->
          <div class="flex items-center flex-1" style="padding-top:28px;">
            <div class="h-0.5 flex-1 bg-gradient-to-r from-blue-300 to-emerald-300"></div>
            <span class="iconify text-gray-400 text-sm -ml-1" data-icon="fa6-solid:chevron-right"></span>
          </div>

          <!-- Node 4 — Create object (rounded square, emerald) -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-emerald-500 to-teal-600 flex items-center justify-center shadow-lg ring-4 ring-emerald-100">
              <span class="iconify text-white text-xl" data-icon="fa6-solid:rotate-right"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-2 text-center leading-tight">Create<br>object</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">report = ReportRunner()</p>
          </div>

          <!-- Arrow 4 -->
          <div class="flex items-center flex-1" style="padding-top:28px;">
            <div class="h-0.5 flex-1 bg-gradient-to-r from-emerald-300 to-gray-300"></div>
            <span class="iconify text-gray-400 text-sm -ml-1" data-icon="fa6-solid:chevron-right"></span>
          </div>

          <!-- Node 5 — Run methods (circle, gray) -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-16 h-16 rounded-full bg-gradient-to-br from-gray-400 to-gray-600 flex items-center justify-center shadow-lg ring-4 ring-gray-100">
              <span class="iconify text-white text-xl" data-icon="fa6-solid:flag-checkered"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-2 text-center leading-tight">Run<br>methods</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">report.run() does everything</p>
          </div>

        </div>
      </div>

      <!-- Explanation block -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="flex items-center gap-3 px-5 py-3.5 bg-gray-50 border-b border-gray-100">
          <span class="iconify text-[#CB187D] text-base" data-icon="fa6-solid:circle-info"></span>
          <p class="text-xs font-bold text-gray-700">Following the five steps with ReportRunner</p>
        </div>
        <div class="px-5 py-4 space-y-2">
          <p class="text-sm text-gray-600 leading-relaxed">Start by looking at your script and spotting functions that all belong to the same job — for example, <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">load_data</code>, <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">clean_data</code>, and <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">save_report</code> all belong to the same report-generation task.</p>
          <p class="text-sm text-gray-600 leading-relaxed">Once you have moved all three into a class as methods, your main script becomes just two lines: one to create the object and one to call <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">run()</code>.</p>
        </div>
      </div>

      <!-- Code example -->
      <div>
        <p class="text-sm text-gray-600 leading-relaxed mb-3">Here is the complete refactored class — notice how calling <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">report.run()</code> triggers all three steps automatically:</p>
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex gap-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-red-400/80"></span>
                <span class="w-2.5 h-2.5 rounded-full bg-amber-400/80"></span>
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-400/80"></span>
              </div>
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">report_runner.py</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code">
            <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:
    def load_data(self):             # Step 1 — moved inside the class
        print("Loading data...")

    def clean_data(self):            # Step 2 — moved inside the class
        print("Cleaning data...")

    def save_report(self):           # Step 3 — moved inside the class
        print("Report saved!")

    def run(self):                   # orchestrates all three steps
        self.load_data()
        self.clean_data()
        self.save_report()

report = ReportRunner()              # create the object
report.run()                         # trigger all three steps</code></pre>
          </div>
        </div>
      </div>

      <!-- Terminal output -->
      <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
        <div class="flex items-center gap-3 px-4 py-2.5 bg-[#181825]">
          <div class="flex gap-1.5">
            <span class="w-2.5 h-2.5 rounded-full bg-red-400/80"></span>
            <span class="w-2.5 h-2.5 rounded-full bg-amber-400/80"></span>
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400/80"></span>
          </div>
          <span class="iconify text-gray-400 text-xs" data-icon="fa6-solid:terminal"></span>
          <span class="text-[11px] font-semibold text-gray-400">Terminal output</span>
        </div>
        <div class="bg-[#0d1117] px-4 py-3 font-mono text-xs text-emerald-400 leading-relaxed space-y-0.5">
          <p><span class="text-gray-500">$</span> python report_runner.py</p>
          <p>Loading data...</p>
          <p>Cleaning data...</p>
          <p>Report saved!</p>
        </div>
      </div>

      <!-- Concept cards grid -->
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">

        <div class="rounded-xl border border-blue-100 bg-blue-50/40 px-4 py-4">
          <div class="flex items-center gap-2.5 mb-2">
            <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-blue-500 shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:arrows-rotate"></span>
            </span>
            <div>
              <p class="text-xs font-bold text-gray-800 leading-tight">Refactoring</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">Same result, cleaner shape</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">The output of your script never changes — only the internal structure improves when you refactor.</p>
        </div>

        <div class="rounded-xl border border-emerald-100 bg-emerald-50/40 px-4 py-4">
          <div class="flex items-center gap-2.5 mb-2">
            <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-emerald-500 shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:cube"></span>
            </span>
            <div>
              <p class="text-xs font-bold text-gray-800 leading-tight">class keyword</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The labelled folder</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">Writing <code class="font-mono">class ReportRunner:</code> creates the container that holds all related methods under one name.</p>
        </div>

        <div class="rounded-xl border border-violet-100 bg-violet-50/40 px-4 py-4">
          <div class="flex items-center gap-2.5 mb-2">
            <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-violet-500 shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:play"></span>
            </span>
            <div>
              <p class="text-xs font-bold text-gray-800 leading-tight">run() method</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">One trigger for all steps</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">Adding a <code class="font-mono">run()</code> method means the caller never needs to know which steps exist or what order to run them in.</p>
        </div>

      </div>

      <!-- Amber tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">Once you have defined <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">run()</code>, your whole main script collapses to two lines — the object creation and the single method call — which makes the script dramatically easier to read and test.</p>
      </div>

    </div>
  </div>
</section>'''

def replace_section(html, section_id, new_html):
    marker = f'<section id="{section_id}"'
    start = html.find(marker)
    if start == -1:
        print(f'❌ Could not find <section id="{section_id}">'); return html, False
    search = html[start:]
    depth, end, i = 0, -1, 0
    while i < len(search):
        if search[i:].startswith('<section'):
            depth += 1; i += len('<section')
        elif search[i:].startswith('</section'):
            depth -= 1
            if depth == 0:
                end = start + i + len('</section>'); break
            i += len('</section')
        else:
            i += 1
    if end == -1:
        print(f'❌ No closing </section> for #{section_id}'); return html, False
    old = html[start:end]
    print(f'  Old #{section_id}: {len(old):,} chars')
    print(f'  New #{section_id}: {len(new_html):,} chars')
    return html[:start] + new_html + html[end:], True

html = TARGET.read_text(encoding='utf-8')
html, ok = replace_section(html, 'decision-flow', NEW_SECTION)
if not ok: sys.exit(1)
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# --- Verification ---
result = TARGET.read_text(encoding='utf-8')
df_start = result.find('<section id="decision-flow"')
ce_start = result.find('<section id="code-examples"')
slice_   = result[df_start:ce_start] if df_start != -1 and ce_start != -1 else result

checks = [
    ("scroll-mt-24",                           'class="scroll-mt-24"'),
    ("Header icon route",                      'data-icon="fa6-solid:route"'),
    ("Header title Decision Flow",             ">Decision Flow<"),
    ("Intro: refactoring paragraph",           "Every refactoring job follows the same five steps"),
    ("Flowchart: min-w-[640px]",               'min-w-[640px]'),
    ("Node 1: fa6-solid:play",                 'data-icon="fa6-solid:play"'),
    ("Node 1: Identify functions",             "Identify<br>functions"),
    ("Node 2: fa6-solid:cube",                 'data-icon="fa6-solid:cube"'),
    ("Node 2: Create class",                   "Create<br>class"),
    ("Node 3: fa6-solid:code-branch",          'data-icon="fa6-solid:code-branch"'),
    ("Node 3: Move into methods",              "Move into<br>methods"),
    ("Node 4: fa6-solid:rotate-right",         'data-icon="fa6-solid:rotate-right"'),
    ("Node 4: report = ReportRunner()",        "report = ReportRunner()"),
    ("Node 5: fa6-solid:flag-checkered",       'data-icon="fa6-solid:flag-checkered"'),
    ("Node 5: Run methods",                    "Run<br>methods"),
    ("Code: report_runner.py filename",        "report_runner.py"),
    ("Code: class ReportRunner",               "class ReportRunner:"),
    ("Code: def run(self)",                    "def run(self):"),
    ("Code: report.run()",                     "report.run()"),
    ("Terminal: Loading data...",              "Loading data..."),
    ("Terminal: Cleaning data...",             "Cleaning data..."),
    ("Terminal: Report saved!",                "Report saved!"),
    ("Concept cards grid",                     "sm:grid-cols-3"),
    ("Amber tip: two lines",                   "two lines"),
    ("No DataPipeline refs",                   True),
]

passed, failed = 0, 0
for label, needle in checks:
    if needle is True:
        ok2 = "DataPipeline" not in slice_
        print(f'  {"✅" if ok2 else "❌"} {label}')
        if ok2: passed += 1
        else: failed += 1
    elif needle in slice_:
        print(f'  ✅ {label}'); passed += 1
    else:
        print(f'  ❌ {label} — not found'); failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
