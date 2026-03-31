import re

TARGET = r'c:\Users\nightwolf\Projects\Python-Learning\pages\track_01_python_foundation\mod_04_python_best_practices\lesson04_logging_basics.html'

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('<section id="objective">')
end   = content.find('</section>', start) + len('</section>')
print(content[start:end])
