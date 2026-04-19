"""
Rewrite lesson06 #knowledge-check body:
- Q1: expand from 2→4 options (concept-identification → multiple choice)
- Q2: fix misleading "NoSQL can never join" → clear True/False about NoSQL origins
- Q3: expand from 2→4 options (concept-identification → multiple choice)
- Q4: keep content, clarify h3 as "Multiple Choice"
- All h3 headers now reflect question type
"""
import pathlib, re

FILE = pathlib.Path(
    r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_04_data_engineering"
    r"\lesson06_nosql_when_tables_arent_enough.html"
)

NEW_BODY = """\
    <div class="bg-white px-8 py-7 space-y-6">
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

<!-- ── Q1: 4 NoSQL categories — multiple choice ─────────────────── -->
<div class="qz-panel qz-panel-anim" role="tabpanel">
  <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q1</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:circle-question"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Multiple Choice</h3>
          <p class="text-xs text-gray-500 mt-0.5">Select the best answer</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="quiz-question" data-qid="quiz-q0">
        <p class="text-sm font-semibold text-gray-800 mb-4">An e-commerce site needs sub-millisecond session lookups and automatic 30-minute expiry for abandoned carts. Which NoSQL category is the best fit?</p>
        <div class="flex flex-col gap-2">
          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors text-left" onclick="checkQuiz(this, false)">
            A) Document (MongoDB) &mdash; flexible JSON schema
          </button>
          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, true)">
            B) Key-Value (Redis) &mdash; RAM-speed lookups with TTL support
          </button>
          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors text-left" onclick="checkQuiz(this, false)">
            C) Column-Family (Cassandra) &mdash; append-only wide rows
          </button>
          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors text-left" onclick="checkQuiz(this, false)">
            D) Graph (Neo4j) &mdash; multi-hop relationship traversal
          </button>
        </div>
        <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
      </div>
    </div>
  </div>
</div>

<!-- ── Q2: Define NoSQL — True / False ──────────────────────────── -->
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
        <p class="text-sm font-semibold text-gray-800 mb-4">True or False: NoSQL databases were designed primarily to solve horizontal scaling and variable-schema problems that traditional relational databases struggle with.</p>
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

<!-- ── Q3: Decision framework — multiple choice ─────────────────── -->
<div class="qz-panel qz-panel-anim hidden" role="tabpanel">
  <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q3</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:circle-question"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Multiple Choice</h3>
          <p class="text-xs text-gray-500 mt-0.5">Select the best answer</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="quiz-question" data-qid="quiz-q2">
        <p class="text-sm font-semibold text-gray-800 mb-4">Your HR system stores 5,000 employees with identical columns &mdash; ID, name, department, salary, and start date. Weekly reports JOIN employees to the payroll table. Which database is the better choice?</p>
        <div class="flex flex-col gap-2">
          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors text-left" onclick="checkQuiz(this, false)">
            A) MongoDB &mdash; document databases are always faster
          </button>
          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, true)">
            B) PostgreSQL &mdash; uniform schema, native JOINs, and ACID guarantees
          </button>
          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors text-left" onclick="checkQuiz(this, false)">
            C) Redis &mdash; HR records are frequently read
          </button>
          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors text-left" onclick="checkQuiz(this, false)">
            D) Cassandra &mdash; HR data can have high write volume
          </button>
        </div>
        <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
      </div>
    </div>
  </div>
</div>

<!-- ── Q4: Hands-on MongoDB — multiple choice ───────────────────── -->
<div class="qz-panel qz-panel-anim hidden" role="tabpanel">
  <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q4</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:circle-question"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Multiple Choice</h3>
          <p class="text-xs text-gray-500 mt-0.5">Select the correct answer</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="quiz-question" data-qid="quiz-q3">
        <p class="text-sm font-semibold text-gray-800 mb-4">You call <code class="font-mono">col.update_one({"sku": "A1"}, {"price": 9.99})</code> in pymongo. What happens?</p>
        <div class="flex flex-col gap-2">
          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors text-left" onclick="checkQuiz(this, false)">
            A) Only the <code class="font-mono">price</code> field is updated; all other fields are preserved
          </button>
          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, true)">
            B) The entire document is replaced with <code class="font-mono">{"price": 9.99}</code>, silently deleting all other fields
          </button>
          <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors text-left" onclick="checkQuiz(this, false)">
            C) MongoDB raises an error because <code class="font-mono">$set</code> is required for all updates
          </button>
        </div>
        <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
      </div>
    </div>
  </div>
</div>
"""

content = FILE.read_text(encoding="utf-8")

kc_start_tag = '<section id="knowledge-check">'
kc_start_idx = content.find(kc_start_tag)
if kc_start_idx == -1:
    print("❌ knowledge-check section not found"); raise SystemExit(1)

BODY_OPEN = '    <div class="bg-white px-8 py-7 space-y-6">\n'
SECTION_END = "    </div>\n  </div>\n</section>"

body_open_idx     = content.find(BODY_OPEN, kc_start_idx)
section_close_idx = content.find(SECTION_END, body_open_idx)

if body_open_idx == -1 or section_close_idx == -1:
    print("❌ Body delimiters not found"); raise SystemExit(1)

old_body = content[body_open_idx:section_close_idx]
new_content = content.replace(old_body, NEW_BODY, 1)

if new_content == content:
    print("⚠️  No change — identical content"); raise SystemExit(1)

FILE.write_text(new_content, encoding="utf-8")
print("✅ Knowledge check section replaced")

# ── Verify ────────────────────────────────────────────────────────────────────
import re as _re
c2 = FILE.read_text(encoding="utf-8")
lines2 = c2.split("\n")
kc_s = next(i for i,l in enumerate(lines2) if 'id="knowledge-check"' in l)
kc_e = next(i for i,l in enumerate(lines2[kc_s+1:], kc_s+1) if '<section id=' in l)
block = "\n".join(lines2[kc_s:kc_e])
print(f"div diff: {block.count('<div') - block.count('</div>')}")
tabs = [m.strip() for m in _re.findall(r'qz-step-label[^>]+>([^<]+)<', block)]
print(f"Tab count: {len(tabs)}")
qs = _re.findall(r'font-semibold text-gray-800 mb-4\">(.+?)</p>', block, _re.DOTALL)
for i,q in enumerate(qs, 1): print(f"  Q{i}: {q[:70].strip()}")
# main balance
ms = next(i for i,l in enumerate(lines2) if '<main ' in l or '<main>' in l)
me = next(i for i,l in enumerate(lines2) if '</main>' in l)
blk2 = "\n".join(lines2[ms:me+1])
print(f"main div diff: {blk2.count('<div') - blk2.count('</div>')}")
