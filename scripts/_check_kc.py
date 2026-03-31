import os, re

root = r'C:/Users/nightwolf/Projects/Python-Learning/pages/track_02_data_analytics'
f = root + '/mod_01_data_analysis_with_pandas/lesson01_introduction_to_pandas.html'
html = open(f, encoding='utf-8').read()

# Check section
tag = '<section id="key-concepts"'
idx = html.find(tag)
end = html.find('</section>', idx) + 10
print('=== KEY-CONCEPTS SECTION (first 800 chars) ===')
print(html[idx:idx+800])
print()

# Check CSS
print('kc-tab-active CSS present:', 'kc-tab-active' in html)
print('kc-panel-anim CSS present:', '.kc-panel-anim' in html)
print()

# Check JS
print('kcColors JS present:', 'kcColors' in html)
print('switchKcTab JS present:', 'switchKcTab' in html)
print()

# Check body class
body_tag = '<div class="bg-white px-6 py-7">'
print('px-6 py-7 body present:', body_tag in html)
