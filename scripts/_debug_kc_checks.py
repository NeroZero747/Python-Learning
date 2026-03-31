import re

TARGET = "pages/track_01_python_foundation/mod_04_python_best_practices/lesson01_creating_your_own_modules.html"
html = open(TARGET).read()
m = re.search(r'<section id="key-concepts".*?</section>', html, re.DOTALL)
sec = m.group(0) if m else ""

# kc-tab count
n1 = sec.count('class="kc-tab "')
n2 = sec.count('class="kc-tab kc-tab-active"')
n3 = sec.count('"kc-tab kc-tab-active"')
n4 = sec.count('"kc-tab"')
print(f"kc-tab counts: 'kc-tab '={n1}  'kc-tab kc-tab-active'={n2}  tab-active={n3}  tab={n4}")

# Panel 1 definition phrases
for phrase in ['statement loads', 'loads your module', 'import statement', "`import`", "the import", "The import"]:
    found = phrase in sec
    if found:
        idx = sec.find(phrase)
        print(f"FOUND {phrase!r}: ...{repr(sec[max(0,idx-20):idx+80])}...")
    else:
        print(f"NOT FOUND: {phrase!r}")

print()
# Panel 2 definition phrases
for phrase in ['pulls one function', 'from.*import.*syntax', 'from … import', 'from &hellip;', '&#8230;']:
    if '.*' in phrase:
        m2 = re.search(phrase, sec)
        if m2:
            idx = m2.start()
            print(f"FOUND regex {phrase!r}: {repr(sec[max(0,idx-20):idx+100])}")
        else:
            print(f"NOT FOUND regex: {phrase!r}")
    else:
        found = phrase in sec
        if found:
            idx = sec.find(phrase)
            print(f"FOUND {phrase!r}: ...{repr(sec[max(0,idx-20):idx+100])}...")
        else:
            print(f"NOT FOUND: {phrase!r}")
