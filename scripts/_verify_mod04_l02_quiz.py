"""Verify the rewritten #knowledge-check section in lesson02."""

from pathlib import Path

TARGET = Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices"
    "/lesson02_project_folder_structure.html"
)

html = TARGET.read_text(encoding="utf-8")

checks = [
    # --- Section shell preserved ---
    ('section id="knowledge-check"',            'section id="knowledge-check" present'),
    ('data-icon="fa6-solid:brain"',             'brain icon present'),
    ('Knowledge Check',                          'section title present'),
    ('Test your understanding before moving on', 'section subtitle present'),

    # --- 4 pill tabs ---
    ('switchQzTab(0)',     'tab 0 present'),
    ('switchQzTab(1)',     'tab 1 present'),
    ('switchQzTab(2)',     'tab 2 present'),
    ('switchQzTab(3)',     'tab 3 present'),
    ('qz-step-active',    'active tab class present'),
    ('Question 1',        'tab label Q1'),
    ('Question 2',        'tab label Q2'),
    ('Question 3',        'tab label Q3'),
    ('Question 4',        'tab label Q4'),
    ('flex-wrap',         'flex-wrap on tab row'),

    # --- 4 panels, watermarks, qids ---
    ('data-qid="quiz-q0"', 'qid quiz-q0'),
    ('data-qid="quiz-q1"', 'qid quiz-q1'),
    ('data-qid="quiz-q2"', 'qid quiz-q2'),
    ('data-qid="quiz-q3"', 'qid quiz-q3'),
    ('>Q1<',               'Q1 watermark'),
    ('>Q2<',               'Q2 watermark'),
    ('>Q3<',               'Q3 watermark'),
    ('>Q4<',               'Q4 watermark'),

    # --- First panel visible, Q2–Q4 hidden ---
    # Q1 panel should NOT have "hidden" immediately after qz-panel-anim
    # Q2–Q4 panels should have "hidden"
    ('qz-panel qz-panel-anim hidden',           'panels 2-4 have hidden class'),

    # --- Q1 content (True) — why structure matters ---
    ('Placing all your scripts, data files, and settings into a single Python file', 'Q1 statement text'),
    # Q1 correct = True: True button → checkQuiz(this, true), False button → checkQuiz(this, false)

    # --- Q2 content (False) — organizing into logical folders ---
    ("it's fine to store your raw data files and Python scripts in the same folder",  'Q2 statement text'),

    # --- Q3 content (True) — separating scripts improves maintainability ---
    ('one for cleaning data, one for calculations, and one for exports',               'Q3 statement text'),

    # --- Q4 content (False) — typical analytics project structure ---
    ('A typical analytics project only needs a single Python scripts folder',         'Q4 statement text'),

    # --- checkQuiz wiring ---
    # Q1 answer = true  → True btn: true,  False btn: false
    # Q2 answer = false → True btn: false, False btn: true
    # Q3 answer = true  → True btn: true,  False btn: false
    # Q4 answer = false → True btn: false, False btn: true
    # Count occurrences: expect 2 true-wired True buttons (Q1, Q3) and 2 false-wired True buttons (Q2, Q4)
]

passed = 0
failed = 0

for needle, label in checks:
    if needle in html:
        print(f"  ✅  {label}")
        passed += 1
    else:
        print(f"  ❌  MISSING: {label!r}  (needle: {needle!r})")
        failed += 1

# Extra structural checks
# Q1 first panel must NOT have hidden on its qz-panel-anim line
import re
panels = re.findall(r'class="qz-panel qz-panel-anim( hidden)?"', html)
q1_hidden = (panels[0] or "").strip() if panels else "MISSING"
q2_hidden = (panels[1] or "").strip() if len(panels) > 1 else "MISSING"
q3_hidden = (panels[2] or "").strip() if len(panels) > 2 else "MISSING"
q4_hidden = (panels[3] or "").strip() if len(panels) > 3 else "MISSING"

panel_count = len(panels)
if panel_count == 4:
    print(f"  ✅  exactly 4 qz-panel divs")
    passed += 1
else:
    print(f"  ❌  expected 4 qz-panel divs, found {panel_count}")
    failed += 1

if q1_hidden == "":
    print(f"  ✅  Q1 panel is visible (no hidden)")
    passed += 1
else:
    print(f"  ❌  Q1 panel should not have hidden, got: {q1_hidden!r}")
    failed += 1

for i, h in enumerate([q2_hidden, q3_hidden, q4_hidden], start=2):
    if h == "hidden":
        print(f"  ✅  Q{i} panel has hidden class")
        passed += 1
    else:
        print(f"  ❌  Q{i} panel missing hidden class, got: {h!r}")
        failed += 1

# Count qz-step buttons — should be 4
qz_buttons = re.findall(r'class="qz-step ', html)
if len(qz_buttons) == 4:
    print(f"  ✅  exactly 4 qz-step buttons")
    passed += 1
else:
    print(f"  ❌  expected 4 qz-step buttons, found {len(qz_buttons)}")
    failed += 1

total = passed + failed
print(f"\n{'='*50}")
print(f"{passed}/{total} checks — {'All checks passed.' if failed == 0 else f'{failed} FAILED.'}")
