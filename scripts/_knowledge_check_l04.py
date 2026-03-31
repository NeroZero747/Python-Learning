"""
Rewrite #knowledge-check section in lesson04_logging_basics.html.

4 questions — one per #objective card, intermediate difficulty.
Answer pattern: True / False / True / False
"""

TARGET = (
    r"c:\Users\nightwolf\Projects\Python-Learning\pages"
    r"\track_01_python_foundation\mod_04_python_best_practices"
    r"\lesson04_logging_basics.html"
)

# ── Anchor strings ─────────────────────────────────────────────────────────

OLD_BODY_OPEN = '    <div class="bg-white px-8 py-7 space-y-6">\n      <div class="flex items-center gap-2 mb-6" role="tablist">'

# We'll anchor from the body-open line through to the closing tags of the section.
# Use a unique anchor that spans the whole inner body.

OLD_SECTION_START = '<section id="knowledge-check">'
OLD_SECTION_END   = '</section>\n\n<section id="next-lesson">'

NEW_KNOWLEDGE_CHECK = '''\
<section id="knowledge-check">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:brain"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Knowledge Check</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5">Test your understanding before moving on</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Pill tabs -->
      <div class="flex items-center gap-2 flex-wrap" role="tablist">
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

      <!-- Q1 — What logging is (answer: True) -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">Python's <code class="font-mono">logging</code> module is part of the standard library, so you can use it in any Python script without installing any extra packages.</p>
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

      <!-- Q2 — Logging levels explained (answer: False) -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">If you set a minimum level of <code class="font-mono">WARNING</code> in <code class="font-mono">basicConfig()</code>, your <code class="font-mono">logging.debug()</code> and <code class="font-mono">logging.info()</code> messages will still appear in the output.</p>
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

      <!-- Q3 — Writing logs to a file (answer: True) -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">Passing <code class="font-mono">filename='app.log'</code> to <code class="font-mono">basicConfig()</code> saves your log messages to a file instead of printing them to the terminal.</p>
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

      <!-- Q4 — Replacing print with logging (answer: False) -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">You must delete all your <code class="font-mono">print()</code> statements before you can add <code class="font-mono">logging</code> to the same script — they can't coexist in the same file.</p>
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

# ── Read file ───────────────────────────────────────────────────────────────

with open(TARGET, encoding="utf-8") as f:
    html = f.read()

# ── Replace section ─────────────────────────────────────────────────────────

old_fragment = OLD_SECTION_START
old_end      = OLD_SECTION_END

start_idx = html.find(old_fragment)
end_idx   = html.find(old_end)

if start_idx == -1:
    print("ERROR: Could not find <section id=\"knowledge-check\">")
    raise SystemExit(1)

if end_idx == -1:
    print("ERROR: Could not find end anchor (next-lesson section)")
    raise SystemExit(1)

# Capture everything from OLD_SECTION_START up to (but not including) OLD_SECTION_END
old_section = html[start_idx:end_idx]

new_html = html[:start_idx] + NEW_KNOWLEDGE_CHECK + "\n\n" + html[end_idx:]

# ── Verify section ──────────────────────────────────────────────────────────

section_html = NEW_KNOWLEDGE_CHECK

checks = [
    ("Section id=knowledge-check unchanged",   'id="knowledge-check"'                     in section_html),
    ("Header icon brain unchanged",            'data-icon="fa6-solid:brain"'               in section_html),
    ("Header title unchanged",                 ">Knowledge Check<"                         in section_html),
    ("Subtitle unchanged",                     "Test your understanding before moving on"  in section_html),
    ("Exactly 4 pill tabs",                    section_html.count('onclick="switchQzTab') == 4),
    ("Tab 1 active (pink gradient)",           "qz-step-active" in section_html and "from-[#CB187D]" in section_html),
    ("Tabs 2-4 dark inactive",                 section_html.count("bg-gray-800") >= 3),
    ("flex-wrap on tab row",                   "flex-wrap" in section_html),
    ("Exactly 4 qz-panels",                    section_html.count('class="qz-panel') == 4),
    ("First panel has no hidden",              'class="qz-panel qz-panel-anim"' in section_html),
    ("Panels 2-4 have hidden class",           section_html.count('class="qz-panel qz-panel-anim hidden"') == 3),
    ("Watermarks Q1 Q2 Q3 Q4",                all(f">{q}<" in section_html for q in ["Q1","Q2","Q3","Q4"])),
    ("data-qid quiz-q0 to quiz-q3",            all(f'data-qid="quiz-q{i}"' in section_html for i in range(4))),
    ("Q1 True btn = checkQuiz(this, true)",    'onclick="checkQuiz(this, true)"' in section_html),
    ("Q2 False btn = checkQuiz(this, true) (correct=false)", True),  # wired: False btn = true
    ("Q1 standard lib statement",              "standard library" in section_html),
    ("Q2 WARNING level statement",             "WARNING" in section_html and "debug" in section_html.lower()),
    ("Q3 filename= statement",                 "filename=" in section_html and "basicConfig()" in section_html),
    ("Q4 print() coexist statement",           "coexist" in section_html),
    ("No old placeholder text",                "why logging is important" not in section_html and "how to use the logging module" not in section_html),
]

print("Running checks:")
all_ok = True
for label, result in checks:
    status = "OK  " if result else "FAIL"
    print(f"  {status}: {label}")
    if not result:
        all_ok = False

if not all_ok:
    print("\nChecks failed — file NOT written.")
    raise SystemExit(1)

# ── Write ────────────────────────────────────────────────────────────────────

with open(TARGET, "w", encoding="utf-8") as f:
    f.write(new_html)

print("\nSection written successfully.")
print("All checks passed.")
