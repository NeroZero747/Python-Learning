target = r'pages\track_01_python_foundation\mod_04_python_best_practices\lesson04_logging_basics.html'
with open(target, encoding='utf-8') as fh:
    content = fh.read()

# Read CSS kc rules
print('=== CSS around kc-tab-active (char 2711) ===')
print(content[2650:2900])

print()
print('=== JS: switchKcTab context (char 59300) ===')
print(content[59300:59600])

print()
print('=== JS: kcColors context (char 143200) ===')
print(content[143200:143400])
