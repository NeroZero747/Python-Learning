import os

root = r'C:/Users/nightwolf/Projects/Python-Learning/pages/track_02_data_analytics'
f = root + '/mod_01_data_analysis_with_pandas/lesson01_introduction_to_pandas.html'
html = open(f, encoding='utf-8').read()

# Check CSS block
idx = html.find('obj-card-kt:hover')
print('CSS block (obj-card-kt:hover) found:', idx != -1)

# Check section header
tag = '<section id="key-ideas">'
idx2 = html.find(tag)
print('--- Section header START ---')
print(html[idx2:idx2+600])

# Check where the section ends
end_idx = html.find('</section>', idx2)
body_start = html.find('<div class="bg-white px-8 py-7 space-y-4">', idx2)
print('Body div starts at offset from section:', body_start - idx2)
