target = r'pages\track_01_python_foundation\mod_04_python_best_practices\lesson04_logging_basics.html'
with open(target, encoding='utf-8') as fh:
    content = fh.read()

# Print key-concepts section
s = content.find('<section id="key-concepts">')
e = content.find('</section>', s) + len('</section>')
print('=== KEY-CONCEPTS SECTION ===')
print(content[s:e])
print()

# Check CSS
print('=== CSS: kc-tab rules ===')
for kw in ['kc-tab-active', 'kc-panel-anim', 'kcFadeIn']:
    idx = content.find(kw)
    print(f'  {kw}: {"FOUND at " + str(idx) if idx != -1 else "MISSING"}')

# Check JS
print()
print('=== JS: switchKcTab / kcColors ===')
for kw in ['switchKcTab', 'kcColors']:
    idx = content.find(kw)
    print(f'  {kw}: {"FOUND at " + str(idx) if idx != -1 else "MISSING"}')
