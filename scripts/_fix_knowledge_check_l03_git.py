"""Replace the #knowledge-check section body in lesson03 with 4 proper Git quiz questions."""

TARGET = (
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson03_introduction_to_git_simple_workflow.html"
)

# Objectives → Questions (True/False alternating: T / F / T / F)
#
# Q1 — "What version control is"    → ANSWER: True
#   Statement: "Git keeps a history of every change you make to your project files,
#               so you can go back to an earlier version at any time."
#
# Q2 — "Save and undo code changes" → ANSWER: False
#   Statement: "Running git commit on its own is all you need to save a snapshot —
#               you don't have to run git add first."
#   (Misconception: beginners often think commit stages and saves in one step)
#
# Q3 — "Push work to GitLab"        → ANSWER: True
#   Statement: "After you run git push, your commits are uploaded to GitLab so
#               your teammates can see and download your latest changes."
#
# Q4 — "The full Git loop"          → ANSWER: False
#   Statement: "Once you run git commit, your teammates on GitLab can immediately
#               see the changes you made."
#   (Misconception: commit alone doesn't share — you still need git push)

NEW_BODY = '''\
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

      <!-- Q1 — What version control is → ANSWER: True -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">Git keeps a history of every change you make to your project files, so you can go back to an earlier version at any time.</p>
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

      <!-- Q2 — Save and undo code changes → ANSWER: False -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">Running <code class="font-mono bg-gray-100 px-1 rounded text-[12px]">git commit</code> on its own is all you need to save a snapshot — you don't have to run <code class="font-mono bg-gray-100 px-1 rounded text-[12px]">git add</code> first.</p>
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

      <!-- Q3 — Push work to GitLab → ANSWER: True -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">After you run <code class="font-mono bg-gray-100 px-1 rounded text-[12px]">git push</code>, your commits are uploaded to GitLab so your teammates can see and download your latest changes.</p>
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

      <!-- Q4 — The full Git loop → ANSWER: False -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">Once you run <code class="font-mono bg-gray-100 px-1 rounded text-[12px]">git commit</code>, your teammates on GitLab can immediately see the changes you made.</p>
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
'''


def find_kc_body(html: str):
    """Find start/end indices of the content inside the #knowledge-check body div."""
    section_pos = html.find('<section id="knowledge-check">')
    if section_pos == -1:
        return None, None

    marker = '<div class="bg-white px-8 py-7 space-y-6">'
    body_start = html.find(marker, section_pos)
    if body_start == -1:
        return None, None

    content_start = body_start + len(marker)
    depth = 1
    pos = content_start
    while pos < len(html) and depth > 0:
        next_open = html.find('<div', pos)
        next_close = html.find('</div>', pos)
        if next_close == -1:
            break
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            if depth == 0:
                return content_start, next_close
            pos = next_close + 6
    return None, None


def main():
    with open(TARGET, encoding="utf-8") as f:
        html = f.read()

    start, end = find_kc_body(html)
    if start is None:
        print("❌ Could not locate #knowledge-check body div")
        return

    new_html = html[:start] + "\n" + NEW_BODY + "    " + html[end:]

    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(new_html)

    print("✅ #knowledge-check body replaced")

    # ── Verification ──────────────────────────────────────────────
    kc = new_html[new_html.find('<section id="knowledge-check">'):
                  new_html.find('<section id="next-lesson">')]

    checks = [
        # Section shell
        ("Section id unchanged",                   'id="knowledge-check"' in kc),
        ("Header icon unchanged",                  "fa6-solid:brain" in kc),
        ("Header title unchanged",                 "Knowledge Check" in kc),
        # 4 pill tabs
        ("4 switchQzTab calls (one per tab)",      kc.count("switchQzTab") == 4),
        ("switchQzTab(0) present",                 "switchQzTab(0)" in kc),
        ("switchQzTab(1) present",                 "switchQzTab(1)" in kc),
        ("switchQzTab(2) present",                 "switchQzTab(2)" in kc),
        ("switchQzTab(3) present",                 "switchQzTab(3)" in kc),
        # 4 question panels
        ("1 visible panel (no hidden class)",      'class="qz-panel qz-panel-anim"' in kc),
        ("3 hidden panels",                        kc.count('class="qz-panel qz-panel-anim hidden"') == 3),
        # data-qid sequence
        ('data-qid="quiz-q0"',                    'data-qid="quiz-q0"' in kc),
        ('data-qid="quiz-q1"',                    'data-qid="quiz-q1"' in kc),
        ('data-qid="quiz-q2"',                    'data-qid="quiz-q2"' in kc),
        ('data-qid="quiz-q3"',                    'data-qid="quiz-q3"' in kc),
        # Watermarks
        ("Q1 watermark",                           ">Q1<" in kc),
        ("Q2 watermark",                           ">Q2<" in kc),
        ("Q3 watermark",                           ">Q3<" in kc),
        ("Q4 watermark",                           ">Q4<" in kc),
        # Statements contain real content
        ("Q1 — history of every change",           "history of every change" in kc),
        ("Q2 — git add not required misconception","don't have to run" in kc),
        ("Q3 — uploaded to GitLab",                "uploaded to GitLab" in kc),
        ("Q4 — immediately see misconception",     "immediately see" in kc),
        # No stale placeholder text
        ("No old placeholder fragment text",       "True or False?" not in kc),
        # flex-wrap on tab row
        ("flex-wrap on tab row",                   "flex-wrap" in kc),
    ]

    passed = sum(1 for _, ok in checks if ok)
    for label, ok in checks:
        print(f"  {'✅' if ok else '❌'} {label}")
    print(f"\n{'✅' if passed == len(checks) else '⚠️'} {passed}/{len(checks)} checks passed")


if __name__ == "__main__":
    main()
