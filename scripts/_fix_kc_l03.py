#!/usr/bin/env python3
"""Rewrite #knowledge-check section body in lesson03 with 4 proper questions."""

FILE = "/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations/lesson03_additional_python_data_types.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

SECTION_OPEN = '<section id="knowledge-check">'
NEXT_SECTION  = '<section id="next-lesson">'

sec_idx  = content.index(SECTION_OPEN)
next_idx = content.index(NEXT_SECTION, sec_idx)

BODY_OPEN = '    <div class="bg-white px-8 py-7 space-y-6">'
body_open_pos      = content.index(BODY_OPEN, sec_idx)
body_content_start = body_open_pos + len(BODY_OPEN)

OUTER_CLOSE = '  </div>\n</section>'
outer_close_pos = content.rindex(OUTER_CLOSE, sec_idx, next_idx)
end_pos = outer_close_pos

print(f"body_content_start = {body_content_start}")
print(f"end_pos            = {end_pos}")

# Answer pattern: True / False / True / False
# Q1 → True   (Tuples: immutability)
# Q2 → False  (Sets: uniqueness misconception)
# Q3 → True   (None: meaning of absence)
# Q4 → False  (Choosing the right type: sets preserve order — wrong)

NEW_BODY = """
      <!-- Pill tab row — 4 tabs, flex-wrap for small screens -->
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

      <!-- Q1 — Tuples (immutability) — Answer: True -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">Once you create a tuple to hold a member's name, plan type, and ID, you can't change any of those values without replacing the whole tuple.</p>
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

      <!-- Q2 — Sets (uniqueness misconception) — Answer: False -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">If you add the same diagnosis code to a set twice, Python stores both copies — the set ends up with two entries for that code.</p>
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

      <!-- Q3 — None (meaning of absence) — Answer: True -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">When a provider's specialty field hasn't been filled in yet, storing it as <code class="font-mono text-[11px] bg-gray-100 px-1 rounded">None</code> is different from storing it as <code class="font-mono text-[11px] bg-gray-100 px-1 rounded">0</code> or as an empty string.</p>
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

      <!-- Q4 — Choosing the right data type (order misconception) — Answer: False -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">A set is the best choice for storing a member's full claim history when you need to keep the claims in the exact order they were submitted.</p>
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

"""

new_content = content[:body_content_start] + NEW_BODY + "    </div>\n" + content[end_pos:]

with open(FILE, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Done — knowledge-check section rewritten successfully.")
