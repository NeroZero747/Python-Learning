TARGET = '/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations/lesson04_lists_dictionaries.html'
with open(TARGET, 'r', encoding='utf-8') as f:
    check = f.read()

kc_s = check.index('id="key-concepts"')
kc_e = check.index('id="decision-flow"', kc_s)
section = check[kc_s:kc_e]

tests = [
    ('4 sidebar tabs',             section.count('<button onclick="switchKcTab(') == 4),
    ('Tab 0 List active',          'kc-tab kc-tab-active' in section and 'fa6-solid:list' in section),
    ('Tab 1 Index hashtag',        'fa6-solid:hashtag' in section),
    ('Tab 2 Dictionary book-open', 'fa6-solid:book-open' in section),
    ('Tab 3 Key-Value link',       'fa6-solid:link' in section),
    ('4 kc-panels',                section.count('class="kc-panel kc-panel-anim') == 4),
    ('Pink panel active',          'data-color="pink"' in section),
    ('Violet panel',               'data-color="violet"' in section),
    ('Blue panel',                 'data-color="blue"' in section),
    ('Emerald panel',              'data-color="emerald"' in section),
    ('Panel 0 no hidden',         'class="kc-panel kc-panel-anim"' in section),
    ('Panels 1-3 hidden x3',      section.count('class="kc-panel kc-panel-anim hidden"') == 3),
    ('List Rules widget',          'List Rules' in section),
    ('Index Quick Reference',      'Index Quick Reference' in section),
    ('List vs Dictionary table',   'List vs Dictionary' in section),
    ('Anatomy of a Pair strip',    'Anatomy of a Pair' in section),
    ('Type badge list',            '> list' in section),
    ('Type badge dict',            '> dict' in section),
    ('Inline kc-tab-num style',    'style="background:#CB187D' in section),
    ('decision-flow intact',       check.count('id="decision-flow"') >= 1),
    ('code-examples intact',       check.count('id="code-examples"') >= 1),
]

all_ok = True
for label, passed in tests:
    mark = 'YES' if passed else 'NO'
    if not passed:
        all_ok = False
    print(f'{mark}: {label}')

print()
print('All checks passed!' if all_ok else 'Some checks FAILED.')
