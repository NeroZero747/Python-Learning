"""
Replace <section id="knowledge-check"> in lesson04.
4 T/F quiz questions (T/F/T/F pattern).
Q1 True:  Refactoring changes structure but keeps output the same.
Q2 False: When moving a function into a class, you can remove self.
Q3 True:  A run() method can call other methods using self.method_name().
Q4 False: You should always refactor into a class, even for one or two small functions.
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_SECTION = '''<section id="knowledge-check" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:brain"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Knowledge Check</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Four True or False questions — check your understanding</p>
      </div>
    </div>

    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Pill tabs -->
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        <button onclick="switchQzTab(0)" class="qz-step qz-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span>
          <span class="qz-step-label text-xs font-bold">Question 1</span>
        </button>
        <button onclick="switchQzTab(1)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span>
          <span class="qz-step-label text-xs font-bold">Question 2</span>
        </button>
        <button onclick="switchQzTab(2)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span>
          <span class="qz-step-label text-xs font-bold">Question 3</span>
        </button>
        <button onclick="switchQzTab(3)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span>
          <span class="qz-step-label text-xs font-bold">Question 4</span>
        </button>
      </div>

      <!-- ══════════════════════════════════════════════ -->
      <!-- Panel Q1 — True                               -->
      <!-- ══════════════════════════════════════════════ -->
      <div class="qz-panel qz-panel-anim" role="tabpanel">
        <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q1</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:circle-question"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">True or False</h3>
                <p class="text-xs text-gray-500 mt-0.5">Select the correct answer</p>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <div class="quiz-question" data-qid="quiz-q0">
              <p class="text-sm font-semibold text-gray-800 mb-4">Refactoring changes the structure of your code but keeps the output exactly the same.</p>
              <div class="flex gap-3">
                <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors" onclick="checkQuiz(this, true)">
                  <span class="iconify mr-1.5" data-icon="fa6-solid:check"></span> True
                </button>
                <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors" onclick="checkQuiz(this, false)">
                  <span class="iconify mr-1.5" data-icon="fa6-solid:xmark"></span> False
                </button>
              </div>
              <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
            </div>
          </div>

        </div>
      </div>

      <!-- ══════════════════════════════════════════════ -->
      <!-- Panel Q2 — False                              -->
      <!-- ══════════════════════════════════════════════ -->
      <div class="qz-panel qz-panel-anim hidden" role="tabpanel">
        <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q2</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:circle-question"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">True or False</h3>
                <p class="text-xs text-gray-500 mt-0.5">Select the correct answer</p>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <div class="quiz-question" data-qid="quiz-q1">
              <p class="text-sm font-semibold text-gray-800 mb-4">When you move a function into a class, you can remove the <code class="font-mono text-xs bg-gray-100 px-1 py-0.5 rounded border border-gray-200">self</code> parameter to keep the code shorter.</p>
              <div class="flex gap-3">
                <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors" onclick="checkQuiz(this, false)">
                  <span class="iconify mr-1.5" data-icon="fa6-solid:check"></span> True
                </button>
                <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors" onclick="checkQuiz(this, true)">
                  <span class="iconify mr-1.5" data-icon="fa6-solid:xmark"></span> False
                </button>
              </div>
              <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
            </div>
          </div>

        </div>
      </div>

      <!-- ══════════════════════════════════════════════ -->
      <!-- Panel Q3 — True                               -->
      <!-- ══════════════════════════════════════════════ -->
      <div class="qz-panel qz-panel-anim hidden" role="tabpanel">
        <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q3</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:circle-question"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">True or False</h3>
                <p class="text-xs text-gray-500 mt-0.5">Select the correct answer</p>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <div class="quiz-question" data-qid="quiz-q2">
              <p class="text-sm font-semibold text-gray-800 mb-4">A <code class="font-mono text-xs bg-gray-100 px-1 py-0.5 rounded border border-gray-200">run()</code> method can call other methods inside the same class using <code class="font-mono text-xs bg-gray-100 px-1 py-0.5 rounded border border-gray-200">self.method_name()</code>.</p>
              <div class="flex gap-3">
                <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors" onclick="checkQuiz(this, true)">
                  <span class="iconify mr-1.5" data-icon="fa6-solid:check"></span> True
                </button>
                <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors" onclick="checkQuiz(this, false)">
                  <span class="iconify mr-1.5" data-icon="fa6-solid:xmark"></span> False
                </button>
              </div>
              <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
            </div>
          </div>

        </div>
      </div>

      <!-- ══════════════════════════════════════════════ -->
      <!-- Panel Q4 — False                              -->
      <!-- ══════════════════════════════════════════════ -->
      <div class="qz-panel qz-panel-anim hidden" role="tabpanel">
        <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q4</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:circle-question"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">True or False</h3>
                <p class="text-xs text-gray-500 mt-0.5">Select the correct answer</p>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">
            <div class="quiz-question" data-qid="quiz-q3">
              <p class="text-sm font-semibold text-gray-800 mb-4">You should always refactor a script into a class, even if it only has one or two small functions.</p>
              <div class="flex gap-3">
                <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors" onclick="checkQuiz(this, false)">
                  <span class="iconify mr-1.5" data-icon="fa6-solid:check"></span> True
                </button>
                <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors" onclick="checkQuiz(this, true)">
                  <span class="iconify mr-1.5" data-icon="fa6-solid:xmark"></span> False
                </button>
              </div>
              <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
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
html, ok = replace_section(html, 'knowledge-check', NEW_SECTION)
if not ok: sys.exit(1)
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# --- Verification ---
result = TARGET.read_text(encoding='utf-8')
se_start = result.find('<section id="knowledge-check"')
nx_start = result.find('<section id="next-lesson"')
s = result[se_start:nx_start] if se_start != -1 and nx_start != -1 else result

checks = [
    ("scroll-mt-24",                        'class="scroll-mt-24"'),
    ("Icon fa6-solid:brain",                'data-icon="fa6-solid:brain"'),
    ("Header: Knowledge Check",             ">Knowledge Check<"),
    ("4 qz-step tabs",                      4),
    ("qz-step-active on tab 0",             "qz-step-active"),
    ("Q1 label",                            ">Question 1<"),
    ("Q2 label",                            ">Question 2<"),
    ("Q3 label",                            ">Question 3<"),
    ("Q4 label",                            ">Question 4<"),
    ("4 qz-panel divs",                     4),
    ("Q1 watermark",                        ">Q1<"),
    ("Q2 watermark",                        ">Q2<"),
    ("Q3 watermark",                        ">Q3<"),
    ("Q4 watermark",                        ">Q4<"),
    ("Q1 statement: Refactoring changes",   "Refactoring changes the structure"),
    ("Q2 statement: remove self",           "can remove the"),
    ("Q3 statement: run() calls others",    "self.method_name()"),
    ("Q4 statement: always refactor",       "always refactor a script"),
    ("Q1 True answer: checkQuiz(this,true)",  "checkQuiz(this, true)"),
    ("Q2 False: True btn is wrong",         "checkQuiz(this, false)"),
    ("8 quiz-feedback elements",            8),
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
        if "qz-step tabs" in label:
            count = s.count('<button onclick="switchQzTab(')
        elif "qz-panel" in label:
            count = s.count('class="qz-panel')
        elif "quiz-feedback" in label:
            count = s.count('class="quiz-feedback')
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
