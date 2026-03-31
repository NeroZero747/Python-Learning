L03 = 'pages/track_01_python_foundation/mod_04_python_best_practices/lesson03_introduction_to_git_simple_workflow.html'
L05 = 'pages/track_01_python_foundation/mod_04_python_best_practices/lesson05_logging_basics.html'

with open(L03) as f: h = f.read()
with open(L05) as f: l5 = f.read()

checks = [
  ('KC switchKcTab (5 buttons + fn = 6)', h.count('switchKcTab') == 6),
  ('KC VS Code panel (sky color)', 'data-color="sky"' in h),
  ('CE switchCeTab (5 buttons + fn = 6)', h.count('switchCeTab') == 6),
  ('CE vs_code_workflow.sh', 'vs_code_workflow.sh' in h),
  ('PE switchPeTab (4 buttons + fn = 5)', h.count('switchPeTab') == 5),
  ('PE open_vs_code.sh', 'open_vs_code.sh' in h),
  ('MK switchMkTab (4 buttons + fn = 5)', h.count('switchMkTab') == 5),
  ('MK Ignoring VS Code Indicators (button+panel = 2)', h.count('Ignoring VS Code Indicators') == 2),
  ('Recap watermark 05', '>05<' in h),
  ('Recap 5 key concepts', 'covered 5 key concepts' in h),
  ('Hero 3/4 Progress', '3<span class="font-bold opacity-50">/4</span>' in h),
  ('Next-lesson Logging Basics title', 'Logging Basics' in h),
  ('Bottom nav lesson05', 'href="lesson05_logging_basics.html"' in h),
  ('No lesson04 in lesson03', 'lesson04_git_in_vs_code.html' not in h),
  ('L05 no lesson04 entry', 'lesson04_git_in_vs_code.html' not in l5),
  ('L05 shows 4. Logging Basics', '4. Logging Basics' in l5),
]

for label, ok in checks:
    print(f'  {"OK" if ok else "FAIL"} {label}')
passed = sum(1 for _,ok in checks if ok)
print(f'\n{passed}/{len(checks)} passed')
