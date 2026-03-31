"""
Replace <section id="practice"> in lesson04.
3 exercises (all Beginner) using ReportRunner domain.
Ex1: Wrap 3 loose functions into class ReportRunner
Ex2: Add self to each method in an incomplete class
Ex3: Add a run() method that calls all three steps
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_SECTION = '''<section id="practice" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:pencil"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Practice Exercises</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Three hands-on exercises — refactoring a script into a class step by step</p>
      </div>
    </div>

    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Pill tabs -->
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        <button onclick="switchPeTab(0)" class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:circle-1"></span>
          <span class="pe-step-label text-xs font-bold">Exercise 1</span>
        </button>
        <button onclick="switchPeTab(1)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:circle-2"></span>
          <span class="pe-step-label text-xs font-bold">Exercise 2</span>
        </button>
        <button onclick="switchPeTab(2)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:circle-3"></span>
          <span class="pe-step-label text-xs font-bold">Exercise 3</span>
        </button>
      </div>

      <!-- ══════════════════════════════════════════════ -->
      <!-- Panel 0 — Exercise 1                          -->
      <!-- ══════════════════════════════════════════════ -->
      <div class="pe-panel pe-panel-anim" role="tabpanel">
        <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <div class="flex items-center gap-2 mb-1">
                  <h3 class="font-bold text-gray-800">Wrap functions inside a class</h3>
                  <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-50 text-emerald-600 border border-emerald-100">Beginner</span>
                </div>
                <div class="flex flex-wrap gap-1.5">
                  <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Classes</span>
                  <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Refactoring</span>
                  <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Functions</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Body -->
          <div class="px-6 py-5 space-y-4">

            <!-- Task box -->
            <div class="task-box rounded-xl border border-[#f5c6e0] bg-[#fdf0f7] px-5 py-4">
              <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-2">Your Task</p>
              <p class="text-sm text-gray-700 leading-relaxed">The script below has three loose functions. Refactor it into a class called <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-pink-100">ReportRunner</code> so that each function becomes a method. Remember to add <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-pink-100">self</code> as the first parameter of each method.</p>
            </div>

            <!-- Starter code -->
            <div>
              <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2">Starter code</p>
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center gap-3 px-4 py-2.5 bg-[#181825]">
                  <div class="flex gap-1.5">
                    <span class="w-2.5 h-2.5 rounded-full bg-red-400/80"></span>
                    <span class="w-2.5 h-2.5 rounded-full bg-amber-400/80"></span>
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400/80"></span>
                  </div>
                  <span class="text-[11px] font-semibold text-gray-400">report_script.py — refactor this</span>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">def load_data():
    print("Loading data...")

def clean_data():
    print("Cleaning data...")

def save_report():
    print("Report saved!")</code></pre>
                </div>
              </div>
            </div>

            <!-- Solution (hidden by default) -->
            <details class="group rounded-xl border border-gray-200 overflow-hidden">
              <summary class="flex items-center justify-between px-5 py-3 bg-gray-50 cursor-pointer select-none">
                <div class="flex items-center gap-2">
                  <span class="iconify text-[#CB187D] text-sm" data-icon="fa6-solid:key"></span>
                  <span class="text-sm font-semibold text-gray-700">Show solution</span>
                </div>
                <span class="iconify text-gray-400 group-open:rotate-180 transition-transform" data-icon="fa6-solid:chevron-down"></span>
              </summary>
              <div class="border-t border-gray-100">
                <div class="rounded-none overflow-hidden">
                  <div class="flex items-center gap-3 px-4 py-2.5 bg-[#181825]">
                    <div class="flex gap-1.5">
                      <span class="w-2.5 h-2.5 rounded-full bg-red-400/80"></span>
                      <span class="w-2.5 h-2.5 rounded-full bg-amber-400/80"></span>
                      <span class="w-2.5 h-2.5 rounded-full bg-emerald-400/80"></span>
                    </div>
                    <span class="text-[11px] font-semibold text-gray-400">solution</span>
                  </div>
                  <div class="bg-code">
                    <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:          # wrap everything inside a class

    def load_data(self):     # same function, plus self
        print("Loading data...")

    def clean_data(self):    # same function, plus self
        print("Cleaning data...")

    def save_report(self):   # same function, plus self
        print("Report saved!")</code></pre>
                  </div>
                </div>
                <div class="px-5 py-3 bg-white border-t border-gray-100">
                  <p class="text-xs text-gray-500 leading-relaxed">The logic inside each function does not change at all. The only two changes are: indent each function under the class, and add <code class="font-mono">self</code> as the first parameter.</p>
                </div>
              </div>
            </details>

          </div>
        </div>
      </div>

      <!-- ══════════════════════════════════════════════ -->
      <!-- Panel 1 — Exercise 2                          -->
      <!-- ══════════════════════════════════════════════ -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <div class="flex items-center gap-2 mb-1">
                  <h3 class="font-bold text-gray-800">Fix the missing self parameter</h3>
                  <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-50 text-emerald-600 border border-emerald-100">Beginner</span>
                </div>
                <div class="flex flex-wrap gap-1.5">
                  <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">self</span>
                  <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Methods</span>
                  <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Classes</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Body -->
          <div class="px-6 py-5 space-y-4">

            <!-- Task box -->
            <div class="task-box rounded-xl border border-[#f5c6e0] bg-[#fdf0f7] px-5 py-4">
              <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-2">Your Task</p>
              <p class="text-sm text-gray-700 leading-relaxed">The class below is incomplete — the developer forgot to add <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-pink-100">self</code> to each method. Fix every method definition so that the class will run without a <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-pink-100">TypeError</code>.</p>
            </div>

            <!-- Starter code -->
            <div>
              <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2">Broken code — find and fix the errors</p>
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center gap-3 px-4 py-2.5 bg-[#181825]">
                  <div class="flex gap-1.5">
                    <span class="w-2.5 h-2.5 rounded-full bg-red-400/80"></span>
                    <span class="w-2.5 h-2.5 rounded-full bg-amber-400/80"></span>
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400/80"></span>
                  </div>
                  <span class="text-[11px] font-semibold text-gray-400">report_runner.py — fix this</span>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:

    def load_data():        # ❌ missing self
        print("Loading data...")

    def clean_data():       # ❌ missing self
        print("Cleaning data...")

    def save_report():      # ❌ missing self
        print("Report saved!")

report = ReportRunner()
report.load_data()          # this will raise TypeError without self</code></pre>
                </div>
              </div>
            </div>

            <!-- Solution -->
            <details class="group rounded-xl border border-gray-200 overflow-hidden">
              <summary class="flex items-center justify-between px-5 py-3 bg-gray-50 cursor-pointer select-none">
                <div class="flex items-center gap-2">
                  <span class="iconify text-[#CB187D] text-sm" data-icon="fa6-solid:key"></span>
                  <span class="text-sm font-semibold text-gray-700">Show solution</span>
                </div>
                <span class="iconify text-gray-400 group-open:rotate-180 transition-transform" data-icon="fa6-solid:chevron-down"></span>
              </summary>
              <div class="border-t border-gray-100">
                <div class="rounded-none overflow-hidden">
                  <div class="flex items-center gap-3 px-4 py-2.5 bg-[#181825]">
                    <div class="flex gap-1.5">
                      <span class="w-2.5 h-2.5 rounded-full bg-red-400/80"></span>
                      <span class="w-2.5 h-2.5 rounded-full bg-amber-400/80"></span>
                      <span class="w-2.5 h-2.5 rounded-full bg-emerald-400/80"></span>
                    </div>
                    <span class="text-[11px] font-semibold text-gray-400">solution</span>
                  </div>
                  <div class="bg-code">
                    <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:

    def load_data(self):    # ✅ self added
        print("Loading data...")

    def clean_data(self):   # ✅ self added
        print("Cleaning data...")

    def save_report(self):  # ✅ self added
        print("Report saved!")

report = ReportRunner()
report.load_data()          # now works correctly</code></pre>
                  </div>
                </div>
                <div class="px-5 py-3 bg-white border-t border-gray-100">
                  <p class="text-xs text-gray-500 leading-relaxed">Python passes the object itself as the first argument every time you call a method. If <code class="font-mono">self</code> is missing, Python raises a <code class="font-mono">TypeError: load_data() takes 0 positional arguments but 1 was given</code>.</p>
                </div>
              </div>
            </details>

          </div>
        </div>
      </div>

      <!-- ══════════════════════════════════════════════ -->
      <!-- Panel 2 — Exercise 3                          -->
      <!-- ══════════════════════════════════════════════ -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <div class="flex items-center gap-2 mb-1">
                  <h3 class="font-bold text-gray-800">Add a run() method</h3>
                  <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-50 text-emerald-600 border border-emerald-100">Beginner</span>
                </div>
                <div class="flex flex-wrap gap-1.5">
                  <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">run()</span>
                  <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">self</span>
                  <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Methods</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Body -->
          <div class="px-6 py-5 space-y-4">

            <!-- Task box -->
            <div class="task-box rounded-xl border border-[#f5c6e0] bg-[#fdf0f7] px-5 py-4">
              <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-2">Your Task</p>
              <p class="text-sm text-gray-700 leading-relaxed">The class below is almost complete, but it is missing a <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-pink-100">run()</code> method. Add one that calls all three methods in the correct order: <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-pink-100">load_data</code>, then <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-pink-100">clean_data</code>, then <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-pink-100">save_report</code>. Use <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-pink-100">self.</code> to call each one.</p>
            </div>

            <!-- Starter code -->
            <div>
              <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-2">Starter code — add the missing method</p>
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center gap-3 px-4 py-2.5 bg-[#181825]">
                  <div class="flex gap-1.5">
                    <span class="w-2.5 h-2.5 rounded-full bg-red-400/80"></span>
                    <span class="w-2.5 h-2.5 rounded-full bg-amber-400/80"></span>
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400/80"></span>
                  </div>
                  <span class="text-[11px] font-semibold text-gray-400">report_runner.py — add run()</span>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:

    def load_data(self):
        print("Loading data...")

    def clean_data(self):
        print("Cleaning data...")

    def save_report(self):
        print("Report saved!")

    # TODO: add a run() method here

report = ReportRunner()
report.run()    # should print all three lines</code></pre>
                </div>
              </div>
            </div>

            <!-- Solution -->
            <details class="group rounded-xl border border-gray-200 overflow-hidden">
              <summary class="flex items-center justify-between px-5 py-3 bg-gray-50 cursor-pointer select-none">
                <div class="flex items-center gap-2">
                  <span class="iconify text-[#CB187D] text-sm" data-icon="fa6-solid:key"></span>
                  <span class="text-sm font-semibold text-gray-700">Show solution</span>
                </div>
                <span class="iconify text-gray-400 group-open:rotate-180 transition-transform" data-icon="fa6-solid:chevron-down"></span>
              </summary>
              <div class="border-t border-gray-100">
                <div class="rounded-none overflow-hidden">
                  <div class="flex items-center gap-3 px-4 py-2.5 bg-[#181825]">
                    <div class="flex gap-1.5">
                      <span class="w-2.5 h-2.5 rounded-full bg-red-400/80"></span>
                      <span class="w-2.5 h-2.5 rounded-full bg-amber-400/80"></span>
                      <span class="w-2.5 h-2.5 rounded-full bg-emerald-400/80"></span>
                    </div>
                    <span class="text-[11px] font-semibold text-gray-400">solution</span>
                  </div>
                  <div class="bg-code">
                    <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:

    def load_data(self):
        print("Loading data...")

    def clean_data(self):
        print("Cleaning data...")

    def save_report(self):
        print("Report saved!")

    def run(self):              # orchestrates all steps
        self.load_data()        # calls step 1
        self.clean_data()       # calls step 2
        self.save_report()      # calls step 3

report = ReportRunner()
report.run()                    # prints all three lines</code></pre>
                  </div>
                </div>
                <div class="px-5 py-3 bg-white border-t border-gray-100">
                  <p class="text-xs text-gray-500 leading-relaxed">Inside any method, use <code class="font-mono">self.method_name()</code> to call another method in the same class. The <code class="font-mono">run()</code> method is the entry point — it knows the right order so the calling code does not have to.</p>
                </div>
              </div>
            </details>

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
        elif search[i:].startswith('</section>'):
            depth -= 1
            if depth == 0:
                end = start + i + len('</section>'); break
            i += len('</section>')
        else:
            i += 1
    if end == -1:
        print(f'❌ No closing </section> for #{section_id}'); return html, False
    old = html[start:end]
    print(f'  Old #{section_id}: {len(old):,} chars')
    print(f'  New #{section_id}: {len(new_html):,} chars')
    return html[:start] + new_html + html[end:], True

html = TARGET.read_text(encoding='utf-8')
html, ok = replace_section(html, 'practice', NEW_SECTION)
if not ok: sys.exit(1)
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# --- Verification ---
result = TARGET.read_text(encoding='utf-8')
se_start = result.find('<section id="practice"')
nx_start = result.find('<section id="mistakes"')
if nx_start == -1:
    nx_start = result.find('<section id="real-world"')
s = result[se_start:nx_start] if se_start != -1 and nx_start != -1 else result

checks = [
    ("scroll-mt-24",                        'class="scroll-mt-24"'),
    ("Icon fa6-solid:pencil",               'data-icon="fa6-solid:pencil"'),
    ("Header: Practice Exercises",          ">Practice Exercises<"),
    ("3 pe-step tabs",                      3),
    ("pe-step-active on tab 0",             "pe-step-active"),
    ("Exercise 1 label",                    ">Exercise 1<"),
    ("Exercise 2 label",                    ">Exercise 2<"),
    ("Exercise 3 label",                    ">Exercise 3<"),
    ("3 pe-panel divs",                     3),
    ("Ex1 task: class ReportRunner",        "class ReportRunner"),
    ("Ex1 starter: def load_data():",       "def load_data():\n"),
    ("Ex2 task: missing self",              "missing self"),
    ("Ex2 starter: ❌ missing self",        "❌ missing self"),
    ("Ex3 task: run() method",              "run()"),
    ("Ex3 starter: # TODO: add a run()",    "# TODO: add a run()"),
    ("Solutions use self.load_data()",      "self.load_data()"),
    ("Solutions use self.clean_data()",     "self.clean_data()"),
    ("Solutions use self.save_report()",    "self.save_report()"),
    ("No DataPipeline refs",                True),
    ("No AnalysisPipeline refs",            True),
    ("No CI/CD tag",                        True),
    ("3 Beginner badges",                   3),
]

passed, failed = 0, 0
for label, needle in checks:
    if needle is True:
        label_map = {
            "No DataPipeline refs": "DataPipeline",
            "No AnalysisPipeline refs": "AnalysisPipeline",
            "No CI/CD tag": "CI/CD",
        }
        term = label_map.get(label, "")
        ok2 = term not in s
        print(f'  {"✅" if ok2 else "❌"} {label}')
        if ok2: passed += 1
        else: failed += 1
    elif isinstance(needle, int):
        if "pe-step tabs" in label:
            count = s.count('<button onclick="switchPeTab(')
        elif "pe-panel" in label:
            count = s.count('class="pe-panel')
        elif "Beginner badges" in label:
            count = s.count(">Beginner<")
        else:
            count = 0
        ok3 = count >= needle
        print(f'  {"✅" if ok3 else "❌"} {label} (found {count})')
        if ok3: passed += 1
        else: failed += 1
    elif needle in s:
        print(f'  ✅ {label}'); passed += 1
    else:
        print(f'  ❌ {label} — not found'); failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
