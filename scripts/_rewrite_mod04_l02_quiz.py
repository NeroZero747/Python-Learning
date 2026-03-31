"""Rewrite #knowledge-check section in lesson02_project_folder_structure.html.

4 True/False questions — one per objective — alternating True/False/True/False.
Q1 (True)  — why project folder structure matters
Q2 (False) — how to organize Python projects into logical folders
Q3 (True)  — how separating scripts improves maintainability
Q4 (False) — what a typical analytics project structure looks like
"""

import re
from pathlib import Path

TARGET = Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices"
    "/lesson02_project_folder_structure.html"
)

NEW_BODY = """\
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

      <!-- Q1 — why project folder structure matters — ANSWER: True -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">Placing all your scripts, data files, and settings into a single Python file becomes harder to manage as your project grows.</p>
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

      <!-- Q2 — how to organize Python projects into logical folders — ANSWER: False -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">In a well-organised Python project, it's fine to store your raw data files and Python scripts in the same folder because Python can find them automatically regardless of where they are.</p>
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

      <!-- Q3 — how separating scripts improves maintainability — ANSWER: True -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">When you split your project into separate files — one for cleaning data, one for calculations, and one for exports — you can update one step without having to change the others.</p>
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

      <!-- Q4 — what a typical analytics project structure looks like — ANSWER: False -->
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
              <p class="text-sm font-semibold text-gray-800 mb-4">A typical analytics project only needs a single Python scripts folder — separate folders for raw data and configuration files are advanced extras that most beginners don't need.</p>
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

def main():
    html = TARGET.read_text(encoding="utf-8")
    original_len = len(html)

    # Find the #knowledge-check section body div and replace its contents.
    # We locate the body div open tag and replace everything up to its closing `</div></div></section>`
    # The section ends just before <section id="next-lesson">.

    # Strategy: replace from the opening of the body div (inside knowledge-check)
    # to its closing tags, preserving the outer shell.

    BODY_OPEN = '    <div class="bg-white px-8 py-7 space-y-6">'
    # We need the one inside #knowledge-check. Find its position.
    kc_start = html.index('<section id="knowledge-check">')
    body_start = html.index(BODY_OPEN, kc_start)

    # The body div closes just before </section> of knowledge-check.
    # Find the </section> that follows knowledge-check (the next-lesson section follows).
    kc_section_end = html.index('\n<section id="next-lesson">', body_start)

    # Extract what's between body_start + len(BODY_OPEN) and the closing tags.
    # The closing structure is:
    #   \n    </div>\n  </div>\n</section>
    # We want to preserve that outer closing.
    # Find it by looking backward from kc_section_end.
    closing = '\n    </div>\n  </div>\n</section>'
    closing_start = html.rindex(closing, body_start, kc_section_end + len(closing))

    old_body_content = html[body_start + len(BODY_OPEN): closing_start]
    old_len = len(old_body_content)

    html = (
        html[:body_start + len(BODY_OPEN)]
        + "\n"
        + NEW_BODY
        + html[closing_start:]
    )

    TARGET.write_text(html, encoding="utf-8")
    new_len = len(html)
    print(f"✅  #knowledge-check body replaced  ({old_len:,} chars → {len(NEW_BODY):,} chars)")
    print(f"File size: {new_len:,} chars")


if __name__ == "__main__":
    main()
