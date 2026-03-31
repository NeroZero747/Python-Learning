import pathlib

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")
html = TARGET.read_text(encoding="utf-8")

idx = html.find('id="knowledge-check"')
end_idx = html.find("</section>", idx) + len("</section>")
s = html[idx:end_idx]

checks = [
    # Shell
    ("Shell: id=knowledge-check",           'id="knowledge-check"'),
    ("Shell: fa6-solid:brain",              'data-icon="fa6-solid:brain"'),
    ("Shell: Knowledge Check title",        ">Knowledge Check<"),
    ("Shell: subtitle preserved",           "Test your understanding before moving on"),
    # Pill tabs
    ("4 pill tabs",                         s.count("qz-step-label text-xs font-bold") == 4),
    ("Tab 1 active (pink gradient)",        "qz-step-active" in s and "from-[#CB187D]" in s),
    ("Tabs 2-3-4 dark bg-gray-800",         s.count("bg-gray-800 text-gray-400") == 3),
    # Panels
    ("4 panels total",                      s.count("qz-panel qz-panel-anim") == 4),
    ("Panel 1 no hidden",                   'class="qz-panel qz-panel-anim"' in s),
    ("Panels 2-3-4 hidden (3×)",            s.count('class="qz-panel qz-panel-anim hidden"') == 3),
    # Watermarks
    ("Watermark Q1",                        ">Q1<"),
    ("Watermark Q2",                        ">Q2<"),
    ("Watermark Q3",                        ">Q3<"),
    ("Watermark Q4",                        ">Q4<"),
    # data-qid
    ('data-qid quiz-q0',                    'data-qid="quiz-q0"'),
    ('data-qid quiz-q1',                    'data-qid="quiz-q1"'),
    ('data-qid quiz-q2',                    'data-qid="quiz-q2"'),
    ('data-qid quiz-q3',                    'data-qid="quiz-q3"'),
    # Q1 — What Refactoring Means (True)
    ("Q1 statement: same output",           "keeps the output exactly the same"),
    # Q2 — Why Scripts Grow Messy (False)
    ("Q2 statement: messy functions",       "easy to maintain as long as each function works correctly"),
    # Q3 — Converting Scripts to Classes (True)
    ("Q3 statement: self as first param",   "self</code> as its first parameter"),
    # Q4 — Benefits of a Class Structure (False)
    ("Q4 statement: run() misconception",   "Creating an object from your class runs all the steps automatically"),
    # Old statements gone
    ("Old Q2 gone (remove self)",           "remove the" not in s),
    ("Old Q3 gone (run can call)",          "can call other methods inside the same class" not in s),
    ("Old Q4 gone (always refactor)",       "always refactor a script into a class" not in s),
    # checkQuiz wiring — 8 total calls
    ("8 checkQuiz calls total",             s.count("checkQuiz(this,") == 8),
    # True/False/True/False pattern:
    # Q1 True → True btn = true, False btn = false
    # Q2 False → True btn = false, False btn = true
    # Q3 True → True btn = true, False btn = false
    # Q4 False → True btn = false, False btn = true
    # Each panel's True button: Q1=true, Q2=false, Q3=true, Q4=false
    # Total checkQuiz(this, true): Q1-True + Q2-False_btn + Q3-True + Q4-False_btn = 4
    ("4× checkQuiz true",                   s.count("checkQuiz(this, true)") == 4),
    ("4× checkQuiz false",                  s.count("checkQuiz(this, false)") == 4),
    # No inline code in Q2 (plain English)
    ("Q2 no stray code tags",               s.count("quiz-q1") == 1),
]

passed = failed = 0
for label, check in checks:
    ok = check if isinstance(check, bool) else (check in s)
    print(f'  {"✅" if ok else "❌"} {label}')
    if ok: passed += 1
    else: failed += 1

print(f"\n{passed}/{passed+failed} checks passed")
print(f"File size: {len(html):,} chars")
