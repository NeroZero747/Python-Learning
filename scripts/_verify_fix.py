import re, os

LESSON_DIR = '/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_01_getting_started/'
files = sorted(f for f in os.listdir(LESSON_DIR) if f.endswith('.html'))

checks = {
    'No DOCTYPE': lambda c: '<!DOCTYPE' not in c,
    'No <html>': lambda c: '<html' not in c,
    'No <head>': lambda c: re.search(r'^<head>', c, re.MULTILINE) is None,
    'No <body>': lambda c: re.search(r'^<body>', c, re.MULTILINE) is None,
    'No </body>': lambda c: '</body>' not in c,
    'No </html>': lambda c: '</html>' not in c,
    'Has :root': lambda c: ':root {' in c,
    'Has --font-body': lambda c: '--font-body' in c,
    'Has --font-mono': lambda c: '--font-mono' in c,
    'No raw Inter stack': lambda c: "'Inter', -apple-system" not in c,
    'No raw Fira stack': lambda c: "'Fira Code', monospace" not in c,
    'TOC float:right': lambda c: 'float: right' in c,
    'layout block': lambda c: '.lesson-layout { display: block; }' in c,
    'TOC float:none mobile': lambda c: 'float: none; display: none;' in c,
}

for fname in files:
    with open(os.path.join(LESSON_DIR, fname)) as f:
        content = f.read()
    print("\n=== " + fname + " ===")
    all_ok = True
    for label, check in checks.items():
        result = check(content)
        status = 'PASS' if result else 'FAIL'
        if not result:
            all_ok = False
        print("  [" + status + "] " + label)
    if all_ok:
        print("  ALL CHECKS PASS")
