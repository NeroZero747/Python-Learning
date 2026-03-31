content = open('pages/track_01/mod_01_getting_started/lesson01_what_is_python.html').read()
checks = [
    ('base CSS: .ce-step sizing rule added', '.ce-step, .mk-step, .qz-step, .pe-step {\n      display: inline-flex;' in content),
    ('base CSS: white-space:nowrap in ce-step rule', 'white-space: nowrap;\n    }\n' in content),
    ('base CSS: .pill-tab still present', '.pill-tab {' in content),
    ('hub-root: #hub-root .ce-step sizing rule', '#hub-root .ce-step,\n  #hub-root .mk-step,\n  #hub-root .qz-step,\n  #hub-root .pe-step {' in content),
    ('hub-root: white-space nowrap important', 'white-space: nowrap !important;' in content),
    ('hub-root: #hub-root .pill-tab still present', '#hub-root .pill-tab {' in content),
    ('HTML: active button has pill-tab', 'class="ce-step ce-step-active pill-tab"' in content),
    ('HTML: inactive button has pill-tab', 'class="ce-step pill-tab"' in content),
    ('sizing rule before skill-dots in file', content.index('#hub-root .ce-step,\n  #hub-root .mk-step') < content.index('Skill dots')),
    ('sizing rule after pill-tab iconify', content.index('#hub-root .pill-tab .iconify') < content.index('#hub-root .ce-step,\n  #hub-root .mk-step')),
]
all_ok = True
for label, result in checks:
    icon = 'OK  ' if result else 'FAIL'
    if not result:
        all_ok = False
    print(f'  [{icon}] {label}')
print()
print('All passed!' if all_ok else 'SOME FAILED')
