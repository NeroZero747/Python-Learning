"""
Replace the #practice section body in lesson01_creating_your_own_modules.html
following the lesson-practice-exercises prompt rules.
"""
import re

TARGET = "pages/track_01_python_foundation/mod_04_python_best_practices/lesson01_creating_your_own_modules.html"

NEW_BODY = '''\
      <!-- ── Tab pill row ──────────────────────────────────────── -->
      <div class="flex items-center gap-2 mb-6" role="tablist">

        <button onclick="switchPeTab(0)" class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Build a Module</span>
        </button>

        <button onclick="switchPeTab(1)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Import and Use</span>
        </button>

        <button onclick="switchPeTab(2)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Pick One Function</span>
        </button>

      </div>

      <!-- ── Panel 1 — Build a Module ───────────────────────────── -->
      <div class="pe-panel pe-panel-anim" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Build a Module</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">School</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">def</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">.py file</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">

            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">You are building a helper file for a school grading system. Create a Python file called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">grade_utils.py</code> that contains two functions: one that converts a raw score to a percentage, and one that returns a letter grade (Pass or Fail) based on that percentage. Run the file directly to test that both functions work correctly.</p>
              </div>
            </div>

            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>

            <div class="accordion-body">
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">grade_utils.py</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python"># grade_utils.py — reusable grading functions

def to_percentage(score, total):         # convert a raw score to a percentage
    return round((score / total) * 100)  # divide, multiply by 100, round

def get_grade(percentage):               # decide Pass or Fail from a percentage
    if percentage &gt;= 50:                 # 50 or above is a pass
        return &quot;Pass&quot;                    # return the pass label
    return &quot;Fail&quot;                        # anything below 50 is a fail

pct = to_percentage(38, 50)             # test: 38 out of 50
print(pct)                              # should print 76
print(get_grade(pct))                   # should print Pass</code></pre>
                </div>
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ python grade_utils.py</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">76<br>Pass</div>
                </div>
              </div>
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">Adding a quick test at the bottom of the module file is a common habit — it lets you run the file directly to check your functions work before importing them anywhere else.</p>
              </div>
            </div>

          </div>
        </div>
      </div>

      <!-- ── Panel 2 — Import and Use ──────────────────────────── -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Import and Use</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">School</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">import</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">dot notation</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">

            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">Using the <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">grade_utils.py</code> module from exercise 1, create a separate file called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">report.py</code>. Import the whole module using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">import grade_utils</code>, then use dot notation to process scores for three students and print each result on its own line. Each output line should show the student&apos;s name, percentage, and grade.</p>
              </div>
            </div>

            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>

            <div class="accordion-body">
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">report.py</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">import grade_utils                              # load every function from grade_utils.py

alice_pct = grade_utils.to_percentage(45, 50)  # Alice scored 45 out of 50
alice_grade = grade_utils.get_grade(alice_pct) # decide Pass or Fail for Alice
print(&quot;Alice:&quot;, alice_pct, &quot;%&quot;, alice_grade)  # print Alice&apos;s result

bob_pct = grade_utils.to_percentage(22, 50)    # Bob scored 22 out of 50
bob_grade = grade_utils.get_grade(bob_pct)     # decide Pass or Fail for Bob
print(&quot;Bob:&quot;, bob_pct, &quot;%&quot;, bob_grade)        # print Bob&apos;s result

cara_pct = grade_utils.to_percentage(31, 50)   # Cara scored 31 out of 50
cara_grade = grade_utils.get_grade(cara_pct)   # decide Pass or Fail for Cara
print(&quot;Cara:&quot;, cara_pct, &quot;%&quot;, cara_grade)     # print Cara&apos;s result</code></pre>
                </div>
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ python report.py</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">Alice: 90 % Pass<br>Bob: 44 % Fail<br>Cara: 62 % Pass</div>
                </div>
              </div>
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">Notice that <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">report.py</code> contains no calculation logic at all — it just calls functions from the module. This is the core benefit of modules: your main script stays short and readable.</p>
              </div>
            </div>

          </div>
        </div>
      </div>

      <!-- ── Panel 3 — Pick One Function ───────────────────────── -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Pick One Function</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">School</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">from … import</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">

            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">Create a file called <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">quick_check.py</code> that imports only the <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">to_percentage</code> function from <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">grade_utils</code> using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">from grade_utils import to_percentage</code>. Use it to check the percentage for five exam scores (all out of 60) and print each result. You should be able to call <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">to_percentage()</code> directly without any module prefix.</p>
              </div>
            </div>

            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>

            <div class="accordion-body">
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">quick_check.py</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">from grade_utils import to_percentage   # import only the one function needed

scores = [54, 30, 42, 58, 21]          # five exam scores, all out of 60

for raw_score in scores:               # loop through each score
    pct = to_percentage(raw_score, 60) # convert to percentage — no prefix needed
    print(raw_score, &quot;→&quot;, pct, &quot;%&quot;)  # print the raw score and its percentage</code></pre>
                </div>
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ python quick_check.py</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">54 → 90 %<br>30 → 50 %<br>42 → 70 %<br>58 → 97 %<br>21 → 35 %</div>
                </div>
              </div>
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">When you only need one function from a module, <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">from … import</code> keeps the code tidier — you skip the module name every time you call it.</p>
              </div>
            </div>

          </div>
        </div>
      </div>
'''

html = open(TARGET, encoding="utf-8").read()

# Match the body div of the practice section
pattern = re.compile(
    r'(<section id="practice">.*?<div class="bg-white px-8 py-7 space-y-6">)'
    r'.*?'
    r'(</div>\s*</div>\s*</section>\s*<section id="mistakes">)',
    re.DOTALL
)

m = pattern.search(html)
if not m:
    print("❌  Could not find #practice body")
    raise SystemExit(1)

old_len = len(m.group(0))
new_section = m.group(1) + '\n' + NEW_BODY + '\n    ' + m.group(2)
html_new = html[:m.start()] + new_section + html[m.end():]

open(TARGET, "w", encoding="utf-8").write(html_new)
print(f"✅  #practice body replaced  ({old_len:,} chars → {len(new_section):,} chars)")
print(f"   File size: {len(html_new):,} chars")
