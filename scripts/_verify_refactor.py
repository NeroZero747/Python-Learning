import os

BASE    = 'pages/track_01/mod_01_getting_started/lesson01_what_is_python.html'
content = open(BASE).read()

checks = [
    ('hero-abstract-card CSS has padding:0.25rem',  'padding: 0.25rem;' in content),
    ('hero-abstract-card CSS has opacity:0.75',     'opacity: 0.75;' in content),
    ('hero-abstract-card CSS removed padding:1rem', 'padding: 1rem;' not in content),
    ('kc-indicator default height in CSS',          '.kc-indicator { height: 68px; }' in content),
    ('hero-pill iconify opacity 0.5',               'hero-pill .iconify { opacity: 0.5 !important; }' in content),
    ('inactive step has box-shadow:none',           'box-shadow: none !important;' in content),
    ('active step has gradient background',         'background: linear-gradient(to right, #CB187D, #e84aad) !important;' in content),
    ('active step has box-shadow',                  'box-shadow: 0 10px 25px -5px rgba(203,24,125,0.3) !important;' in content),
    ('no style=opacity:0.5 in HTML',                'style="opacity:0.5;"' not in content),
    ('no inline style on hero-abstract-card HTML',  'style="padding:0.25rem;opacity:0.75;"' not in content),
    ('no inline height on kc-indicator HTML',       'style="height:68px;"' not in content),
    ('no s.style.background gradient in JS',        "s.style.background = 'linear-gradient" not in content),
    ('no s.style.color = fff in JS',                "s.style.color = '#fff'" not in content),
    ('no s.style.boxShadow in JS',                  "s.style.boxShadow = '0 10px" not in content),
    ('no s.style.background inactive in JS',        "s.style.background = '#1f2937'" not in content),
]

all_pass = True
for label, result in checks:
    icon = 'OK' if result else 'FAIL'
    if not result:
        all_pass = False
    print(f'  [{icon}] {label}')

print()
print('All checks passed!' if all_pass else 'SOME CHECKS FAILED')
