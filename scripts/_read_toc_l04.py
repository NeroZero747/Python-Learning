target = r'pages\track_01_python_foundation\mod_04_python_best_practices\lesson04_logging_basics.html'
with open(target, encoding='utf-8') as fh:
    content = fh.read()
s = content.find('class="lesson-toc-sidebar"')
e = content.find('</aside>', s) + len('</aside>')
print(content[s:e])
