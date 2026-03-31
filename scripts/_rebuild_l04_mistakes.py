"""
Replace <section id="mistakes"> in lesson04.
3 mistakes using ReportRunner domain.
Mk1: Moving Functions Without Adding self
Mk2: Forgetting to Create an Object (DataPipeline → ReportRunner)
Mk3: Refactoring Too Early — fix duplicate tip text
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_SECTION = '''<section id="mistakes" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:triangle-exclamation"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Common Mistakes</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Three mistakes beginners make when refactoring scripts into classes</p>
      </div>
    </div>

    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Pill tabs -->
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        <button onclick="switchMkTab(0)" class="mk-step mk-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:circle-1"></span>
          <span class="mk-step-label text-xs font-bold">No self</span>
        </button>
        <button onclick="switchMkTab(1)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:circle-2"></span>
          <span class="mk-step-label text-xs font-bold">No object</span>
        </button>
        <button onclick="switchMkTab(2)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:circle-3"></span>
          <span class="mk-step-label text-xs font-bold">Too early</span>
        </button>
      </div>

      <!-- ══════════════════════════════════════════════ -->
      <!-- Panel 0 — No self                             -->
      <!-- ══════════════════════════════════════════════ -->
      <div class="mk-panel mk-panel-anim" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-red-100 transition-all duration-300">

          <div class="relative bg-gradient-to-br from-red-50 via-white to-rose-50 px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-red-400/[0.06] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-red-500 to-rose-500 text-white shadow-md shrink-0">
                <span class="iconify text-base" data-icon="fa6-solid:triangle-exclamation"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Moving Functions Without Adding <code class="text-sm font-mono">self</code></h3>
                <p class="text-xs text-gray-500 mt-0.5">The most common refactoring mistake — a TypeError at runtime</p>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <p class="text-sm text-gray-600 leading-relaxed">When you move a function inside a class, Python automatically passes the object as the first argument every time you call the method. If your method definition does not have <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">self</code> as its first parameter, Python has nowhere to put that argument and raises a <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">TypeError</code>.</p>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- ❌ Wrong -->
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-red-500 mb-2">❌ Mistake</p>
                <div class="rounded-xl overflow-hidden border border-red-900/30 shadow-lg">
                  <div class="px-3 py-2 bg-[#181825]">
                    <span class="text-[11px] font-semibold text-red-400">forgot self</span>
                  </div>
                  <div class="bg-code">
                    <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:

    def load_data():       # ❌ no self
        print("Loading data...")</code></pre>
                  </div>
                </div>
              </div>
              <!-- ✅ Correct -->
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-emerald-600 mb-2">✅ Fix</p>
                <div class="rounded-xl overflow-hidden border border-emerald-900/30 shadow-lg">
                  <div class="px-3 py-2 bg-[#181825]">
                    <span class="text-[11px] font-semibold text-emerald-400">self added</span>
                  </div>
                  <div class="bg-code">
                    <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:

    def load_data(self):   # ✅ self is first
        print("Loading data...")</code></pre>
                  </div>
                </div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">You never write <code class="text-[11px] bg-white px-1 py-0.5 rounded font-mono border border-gray-100">self</code> yourself when you call the method — Python inserts it automatically. Your job is just to make sure there is a slot for it in the method's parameter list.</p>
            </div>
          </div>

        </div>
      </div>

      <!-- ══════════════════════════════════════════════ -->
      <!-- Panel 1 — No object                           -->
      <!-- ══════════════════════════════════════════════ -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-red-100 transition-all duration-300">

          <div class="relative bg-gradient-to-br from-red-50 via-white to-rose-50 px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-red-400/[0.06] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-red-500 to-rose-500 text-white shadow-md shrink-0">
                <span class="iconify text-base" data-icon="fa6-solid:triangle-exclamation"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Forgetting to Create an Object First</h3>
                <p class="text-xs text-gray-500 mt-0.5">Calling a method directly on the class name instead of an instance</p>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <p class="text-sm text-gray-600 leading-relaxed">A class is a <em>blueprint</em>, not a ready-to-use object. Before you can call any of its methods, you must create an instance by calling the class like a function — <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">ReportRunner()</code>. If you try to call a method directly on the class name without creating an instance first, Python raises a <code class="text-[11px] bg-gray-100 px-1.5 py-0.5 rounded font-mono border border-gray-200">TypeError</code> about a missing argument.</p>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- ❌ Wrong -->
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-red-500 mb-2">❌ Mistake</p>
                <div class="rounded-xl overflow-hidden border border-red-900/30 shadow-lg">
                  <div class="px-3 py-2 bg-[#181825]">
                    <span class="text-[11px] font-semibold text-red-400">calling the class, not an instance</span>
                  </div>
                  <div class="bg-code">
                    <pre class="overflow-x-auto pre-reset"><code class="language-python"># ❌ calling run() on the class itself
ReportRunner.run()    # raises TypeError</code></pre>
                  </div>
                </div>
              </div>
              <!-- ✅ Correct -->
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-emerald-600 mb-2">✅ Fix</p>
                <div class="rounded-xl overflow-hidden border border-emerald-900/30 shadow-lg">
                  <div class="px-3 py-2 bg-[#181825]">
                    <span class="text-[11px] font-semibold text-emerald-400">create an instance first</span>
                  </div>
                  <div class="bg-code">
                    <pre class="overflow-x-auto pre-reset"><code class="language-python"># ✅ create an object, then call the method
report = ReportRunner()
report.run()          # works correctly</code></pre>
                  </div>
                </div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Think of the class as a cookie cutter and the object as the cookie. You cannot eat the cutter — you need to press it into dough first. <code class="text-[11px] bg-white px-1 py-0.5 rounded font-mono border border-gray-100">report = ReportRunner()</code> is the step that makes the cookie.</p>
            </div>
          </div>

        </div>
      </div>

      <!-- ══════════════════════════════════════════════ -->
      <!-- Panel 2 — Too early                           -->
      <!-- ══════════════════════════════════════════════ -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-amber-100 transition-all duration-300">

          <div class="relative bg-gradient-to-br from-amber-50 via-white to-yellow-50 px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-amber-400/[0.08] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-amber-500 to-orange-500 text-white shadow-md shrink-0">
                <span class="iconify text-base" data-icon="fa6-solid:clock"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Refactoring Too Early</h3>
                <p class="text-xs text-gray-500 mt-0.5">Creating a class when a simple script would be cleaner</p>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <p class="text-sm text-gray-600 leading-relaxed">A class adds structure — but structure adds complexity. If your script only has one or two small functions that will never grow, adding a class makes your code harder to read, not easier. Refactoring is worth doing when the script has several related steps that you want to keep together, reuse, or test independently.</p>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- ❌ Over-engineered -->
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-red-500 mb-2">❌ Over-engineered</p>
                <div class="rounded-xl overflow-hidden border border-red-900/30 shadow-lg">
                  <div class="px-3 py-2 bg-[#181825]">
                    <span class="text-[11px] font-semibold text-red-400">class for a one-liner</span>
                  </div>
                  <div class="bg-code">
                    <pre class="overflow-x-auto pre-reset"><code class="language-python">class Greeter:          # unnecessary — one tiny function

    def run(self):
        print("Hello!")</code></pre>
                  </div>
                </div>
              </div>
              <!-- ✅ Appropriate -->
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-emerald-600 mb-2">✅ Appropriate</p>
                <div class="rounded-xl overflow-hidden border border-emerald-900/30 shadow-lg">
                  <div class="px-3 py-2 bg-[#181825]">
                    <span class="text-[11px] font-semibold text-emerald-400">keep it simple</span>
                  </div>
                  <div class="bg-code">
                    <pre class="overflow-x-auto pre-reset"><code class="language-python">def greet():            # plain function is fine here
    print("Hello!")</code></pre>
                  </div>
                </div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">A good rule of thumb: reach for a class when you have three or more related functions that belong together, or when you expect the script to keep growing. A script that loads data, cleans it, and saves a report is a natural fit. A script that prints one message is not.</p>
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
html, ok = replace_section(html, 'mistakes', NEW_SECTION)
if not ok: sys.exit(1)
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# --- Verification ---
result = TARGET.read_text(encoding='utf-8')
se_start = result.find('<section id="mistakes"')
nx_start = result.find('<section id="real-world"')
s = result[se_start:nx_start] if se_start != -1 and nx_start != -1 else result

checks = [
    ("scroll-mt-24",                        'class="scroll-mt-24"'),
    ("Icon fa6-solid:triangle-exclamation", 'data-icon="fa6-solid:triangle-exclamation"'),
    ("Header: Common Mistakes",             ">Common Mistakes<"),
    ("3 mk-step tabs",                      3),
    ("mk-step-active on tab 0",             "mk-step-active"),
    ("No self label",                       ">No self<"),
    ("No object label",                     ">No object<"),
    ("Too early label",                     ">Too early<"),
    ("3 mk-panel divs",                     3),
    ("Mk1: class ReportRunner in code",     "class ReportRunner:"),
    ("Mk1: def load_data(self)",            "def load_data(self):"),
    ("Mk2: ReportRunner.run()",             "ReportRunner.run()"),
    ("Mk2: report = ReportRunner()",        "report = ReportRunner()"),
    ("Mk3: cookie cutter analogy",          "cookie cutter"),
    ("Mk3: three or more related",          "three or more related"),
    ("3 amber tips",                        3),
    ("No DataPipeline refs",                True),
]

passed, failed = 0, 0
for label, needle in checks:
    if needle is True:
        ok2 = "DataPipeline" not in s
        print(f'  {"✅" if ok2 else "❌"} {label}')
        if ok2: passed += 1
        else: failed += 1
    elif isinstance(needle, int):
        if "mk-step tabs" in label:
            count = s.count('<button onclick="switchMkTab(')
        elif "mk-panel" in label:
            count = s.count('class="mk-panel')
        elif "amber tips" in label:
            count = s.count("bg-amber-tip")
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
