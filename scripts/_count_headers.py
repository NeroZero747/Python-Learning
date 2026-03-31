target = r'pages\track_01_python_foundation\mod_04_python_best_practices\lesson04_logging_basics.html'
with open(target, encoding='utf-8') as fh:
    content = fh.read()
s = content.find('<section id="key-concepts"')
e = content.find('</section>', s) + len('</section>')
sec = content[s:e]

panel_headers = sec.count('flex items-center justify-between">')
code_headers  = sec.count('flex items-center justify-between px-4')
print(f'Panel header divs (no px-4):  {panel_headers}')
print(f'Code block header divs (px-4): {code_headers}')
print(f'Total justify-between:          {sec.count("flex items-center justify-between")}')
