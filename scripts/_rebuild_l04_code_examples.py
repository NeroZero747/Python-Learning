"""
Replace <section id="code-examples"> in lesson04.
3 descriptive tabs: Loose Script | Refactored Class | Adding run()
Domain: ReportRunner — load_data / clean_data / save_report
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_SECTION = '''<section id="code-examples" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:code"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Code Examples</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">From loose script to a clean refactored class — three stages</p>
      </div>
    </div>

    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Pill tabs -->
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        <button onclick="switchCeTab(0)" class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:file-lines"></span>
          <span class="ce-step-label text-xs font-bold">Loose Script</span>
        </button>
        <button onclick="switchCeTab(1)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:cube"></span>
          <span class="ce-step-label text-xs font-bold">Refactored Class</span>
        </button>
        <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:play"></span>
          <span class="ce-step-label text-xs font-bold">Adding run()</span>
        </button>
      </div>

      <!-- ══════════════════════════════════════════════ -->
      <!-- Panel 0 — Loose Script                        -->
      <!-- ══════════════════════════════════════════════ -->
      <div class="ce-panel ce-panel-anim" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:file-lines"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Loose Script</h3>
                <p class="text-xs text-gray-500 mt-0.5">Three functions defined and called separately — no grouping</p>
              </div>
            </div>
          </div>

          <!-- Body -->
          <div class="px-6 py-5 space-y-4">
            <p class="text-sm text-gray-600 leading-relaxed">This is the starting point — three functions that all belong together but live as separate, ungrouped definitions. The script works, but anyone reading it has to scan all the way to the bottom call section to understand what order the steps run in.</p>

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
                    <span class="text-[11px] font-semibold text-gray-400">report_script.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python"># Loose script — functions defined separately, no grouping

def load_data():
    print("Loading data...")    # step 1

def clean_data():
    print("Cleaning data...")   # step 2

def save_report():
    print("Report saved!")      # step 3

# must call each function manually in the right order
load_data()
clean_data()
save_report()</code></pre>
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
                <p><span class="text-gray-500">$</span> python report_script.py</p>
                <p>Loading data...</p>
                <p>Cleaning data...</p>
                <p>Report saved!</p>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">The output is correct — but if you added a fourth step, you would need to find the call section at the bottom of the file and add another line there. As scripts grow, this becomes fragile and easy to get wrong.</p>
            </div>
          </div>

        </div>
      </div>

      <!-- ══════════════════════════════════════════════ -->
      <!-- Panel 1 — Refactored Class                    -->
      <!-- ══════════════════════════════════════════════ -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:cube"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Refactored Class</h3>
                <p class="text-xs text-gray-500 mt-0.5">The same three functions moved inside a class as methods</p>
              </div>
            </div>
          </div>

          <!-- Body -->
          <div class="px-6 py-5 space-y-4">
            <p class="text-sm text-gray-600 leading-relaxed">Moving the functions inside a <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">class</code> block is the core refactoring step. Each function becomes a method — the only change you make to each one is adding <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">self</code> as the first parameter. The logic inside every function stays exactly the same.</p>

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
                <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:                  # class header — groups everything together

    def load_data(self):             # was: def load_data()  → added self
        print("Loading data...")

    def clean_data(self):            # was: def clean_data() → added self
        print("Cleaning data...")

    def save_report(self):           # was: def save_report() → added self
        print("Report saved!")

# create an object, then call each method manually
report = ReportRunner()
report.load_data()
report.clean_data()
report.save_report()</code></pre>
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

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">The output is identical to the loose script. The only differences visible in the calling code are: the methods are now prefixed with <code class="text-[11px] bg-white px-1 py-0.5 rounded font-mono border border-gray-100">report.</code> and the object must be created first. Everything else is the same.</p>
            </div>
          </div>

        </div>
      </div>

      <!-- ══════════════════════════════════════════════ -->
      <!-- Panel 2 — Adding run()                        -->
      <!-- ══════════════════════════════════════════════ -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:play"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Adding run()</h3>
                <p class="text-xs text-gray-500 mt-0.5">One method that orchestrates all the steps — the finished class</p>
              </div>
            </div>
          </div>

          <!-- Body -->
          <div class="px-6 py-5 space-y-4">
            <p class="text-sm text-gray-600 leading-relaxed">Adding a <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">run()</code> method is the finishing touch. It calls all the other methods in the right order from inside the class — so your main script shrinks to just two lines and you never have to remember which steps exist or what sequence they run in.</p>

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

    def load_data(self):
        print("Loading data...")

    def clean_data(self):
        print("Cleaning data...")

    def save_report(self):
        print("Report saved!")

    def run(self):                   # new method — chains all the steps
        self.load_data()             # calls step 1
        self.clean_data()            # calls step 2
        self.save_report()           # calls step 3

# main script — clean, just two lines
report = ReportRunner()
report.run()                         # everything runs automatically</code></pre>
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

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">The same three lines of output — but now the calling code is just <code class="text-[11px] bg-white px-1 py-0.5 rounded font-mono border border-gray-100">report = ReportRunner()</code> and <code class="text-[11px] bg-white px-1 py-0.5 rounded font-mono border border-gray-100">report.run()</code>. That is the complete benefit of refactoring into a class with a <code class="text-[11px] bg-white px-1 py-0.5 rounded font-mono border border-gray-100">run()</code> method.</p>
            </div>
          </div>

        </div>
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
html, ok = replace_section(html, 'code-examples', NEW_SECTION)
if not ok: sys.exit(1)
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# --- Verification ---
result = TARGET.read_text(encoding='utf-8')
ce_start = result.find('<section id="code-examples"')
cp_start = result.find('<section id="comparison"')
slice_   = result[ce_start:cp_start] if ce_start != -1 and cp_start != -1 else result

checks = [
    ("scroll-mt-24",                        'class="scroll-mt-24"'),
    ("Icon fa6-solid:code",                 'data-icon="fa6-solid:code"'),
    ("Header title Code Examples",          ">Code Examples<"),
    ("3 ce-step pill tabs",                 3),
    ("Tab 0 active",                        "ce-step-active"),
    ("Tab 0: Loose Script label",           ">Loose Script<"),
    ("Tab 0: file-lines icon",              'data-icon="fa6-solid:file-lines"'),
    ("Tab 1: Refactored Class label",       ">Refactored Class<"),
    ("Tab 1: cube icon",                    'data-icon="fa6-solid:cube"'),
    ("Tab 2: Adding run() label",           ">Adding run()<"),
    ("Tab 2: play icon on tab",             'data-icon="fa6-solid:play"'),
    ("3 ce-panel divs",                     3),
    ("Panel 0: report_script.py",           "report_script.py"),
    ("Panel 0: def load_data() no self",    "def load_data():\n"),
    ("Panel 0: call load_data() global",    "\nload_data()"),
    ("Panel 1: report_runner.py",           "report_runner.py"),
    ("Panel 1: class ReportRunner",         "class ReportRunner:"),
    ("Panel 1: load_data(self)",            "def load_data(self):"),
    ("Panel 1: report = ReportRunner()",    "report = ReportRunner()"),
    ("Panel 2: def run(self)",              "def run(self):"),
    ("Panel 2: self.load_data()",           "self.load_data()"),
    ("Panel 2: report.run()",              "report.run()"),
    ("All 3 terminals: Loading data",       3),
    ("All 3 terminals: Cleaning data",      3),
    ("All 3 terminals: Report saved!",      3),
    ("No DataPipeline refs",                True),
]

passed, failed = 0, 0
for label, needle in checks:
    if needle is True:
        ok2 = "DataPipeline" not in slice_
        print(f'  {"✅" if ok2 else "❌"} {label}')
        if ok2: passed += 1
        else: failed += 1
    elif isinstance(needle, int):
        if "ce-step pill" in label:
            count = slice_.count('<button onclick="switchCeTab(')
        elif "ce-panel" in label:
            count = slice_.count('class="ce-panel')
        elif "terminals: Loading" in label:
            count = slice_.count("Loading data...")
        elif "terminals: Cleaning" in label:
            count = slice_.count("Cleaning data...")
        elif "terminals: Report" in label:
            count = slice_.count("Report saved!")
        else:
            count = 0
        ok3 = count >= needle
        print(f'  {"✅" if ok3 else "❌"} {label} (found {count})')
        if ok3: passed += 1
        else: failed += 1
    elif needle in slice_:
        print(f'  ✅ {label}'); passed += 1
    else:
        print(f'  ❌ {label} — not found'); failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
