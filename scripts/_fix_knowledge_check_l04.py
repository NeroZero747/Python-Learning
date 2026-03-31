"""
Rewrite the #knowledge-check section body in lesson04.
4 questions, one per objective, beginner difficulty, True/False/True/False answer pattern.
"""

TARGET = "pages/track_01/mod_02_programming_foundations/lesson04_lists_dictionaries.html"

OLD_BODY = '''    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-2 mb-6" role="tablist"><button onclick="switchQzTab(0)" class="qz-step qz-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
  <span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span>
  <span class="qz-step-label text-xs font-bold">Question 1</span>
</button>
<button onclick="switchQzTab(1)" class="qz-step  flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
  <span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span>
  <span class="qz-step-label text-xs font-bold">Question 2</span>
</button>
<button onclick="switchQzTab(2)" class="qz-step  flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
  <span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span>
  <span class="qz-step-label text-xs font-bold">Question 3</span>
</button>
</div>
      <div class="qz-panel qz-panel-anim " role="tabpanel">
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
        <p class="text-sm font-semibold text-gray-800 mb-4">lists store ordered collections of values &#8212; True or False?</p>
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
        <p class="text-sm font-semibold text-gray-800 mb-4">dictionaries store key-value pairs &#8212; True or False?</p>
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
        <p class="text-sm font-semibold text-gray-800 mb-4">lists use indexes to access data &#8212; True or False?</p>
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

    </div>
  </div>
</section>'''

NEW_BODY = '''    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Pill tab row — 4 tabs, flex-wrap for mobile -->
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

      <!-- Q1 — Lists: ordered data collections (Answer: True) -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">When you create a list in Python, the items stay in the same order you added them — so the first member you add will always be at position zero.</p>
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

      <!-- Q2 — Dictionaries: key-value pairs (Answer: False) -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">You can look up a value in a dictionary by its position number, just like you do with a list.</p>
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

      <!-- Q3 — Reading values by index or key (Answer: True) -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">If you want the last member ID in a list, you can use the index -1 to get it without knowing the total number of items.</p>
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

      <!-- Q4 — Link to SQL tables and Excel (Answer: False) -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">A Python dictionary is most similar to a column in a spreadsheet, because it holds a list of values in a fixed order.</p>
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

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

if OLD_BODY not in content:
    print("❌ OLD_BODY not found — check whitespace or content")
else:
    new_content = content.replace(OLD_BODY, NEW_BODY, 1)
    with open(TARGET, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("✅ #knowledge-check body replaced")

# --- Verify ---
with open(TARGET, 'r', encoding='utf-8') as f:
    c = f.read()

sec_start = c.index('<section id="knowledge-check">')
sec_end   = c.index('<section id="next-lesson">', sec_start)
section   = c[sec_start:sec_end]

def count(needle, hay):
    return hay.count(needle)

checks = [
    ("Section header icon unchanged (fa6-solid:brain)",    'data-icon="fa6-solid:brain"' in section),
    ("Header title unchanged (Knowledge Check)",           '>Knowledge Check<' in section),
    ("Exactly 4 pill tab buttons",                         count('switchQzTab(', section) == 4),
    ("Exactly 4 qz-panel divs",                           count('class="qz-panel', section) == 4),
    ("Tab row has flex-wrap",                              'flex-wrap' in section),
    ("Q1 panel has no hidden class",                       'class="qz-panel qz-panel-anim"' in section),
    ("Q2 panel has hidden class",                          section.count('class="qz-panel qz-panel-anim hidden"') >= 3),
    ("data-qid quiz-q0 present",                           'data-qid="quiz-q0"' in section),
    ("data-qid quiz-q1 present",                           'data-qid="quiz-q1"' in section),
    ("data-qid quiz-q2 present",                           'data-qid="quiz-q2"' in section),
    ("data-qid quiz-q3 present",                           'data-qid="quiz-q3"' in section),
    ("Watermark Q1 present",                               '>Q1<' in section),
    ("Watermark Q2 present",                               '>Q2<' in section),
    ("Watermark Q3 present",                               '>Q3<' in section),
    ("Watermark Q4 present",                               '>Q4<' in section),
    # Answer wiring: Q1=True, Q2=False, Q3=True, Q4=False
    # Q1: True btn -> checkQuiz(this, true), False btn -> checkQuiz(this, false)
    # Q2: True btn -> checkQuiz(this, false), False btn -> checkQuiz(this, true)
    # Q3: True btn -> checkQuiz(this, true), False btn -> checkQuiz(this, false)
    # Q4: True btn -> checkQuiz(this, false), False btn -> checkQuiz(this, true)
    ("Answers alternate (not all same)",                   section.count('checkQuiz(this, true)') > 0 and section.count('checkQuiz(this, false)') > 0),
    ("Q1 statement — lists ordered",                       'items stay in the same order' in section),
    ("Q2 statement — dict position misconception",         'position number' in section),
    ("Q3 statement — negative index -1",                   'index -1' in section),
    ("Q4 statement — dict vs column misconception",        'most similar to a column' in section),
    ("No statements copying objective labels verbatim",    'lists store ordered collections of values' not in section and 'dictionaries store key-value pairs' not in section),
    ("quiz-feedback elements present (4)",                 count('quiz-feedback', section) == 4),
    ("8 checkQuiz calls total (2 per question x 4)",       count('checkQuiz', section) == 8),
]

all_pass = True
for label, result in checks:
    status = "YES" if result else "NO "
    if not result:
        all_pass = False
    print(f"  {status}: {label}")

print()
print("All checks passed!" if all_pass else "Some checks FAILED — review above.")
