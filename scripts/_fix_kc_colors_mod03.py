import re, os, sys

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

folder = 'c:/Users/nightwolf/Projects/Python-Learning/pages/mod_03_python_for_data_analysts'

# ── Color conversion rules (ordered: most-specific first) ────────────────────

def rules_pink_to_emerald():
    return [
        ('from-[#CB187D] via-pink-400 to-rose-300',  'from-emerald-500 via-teal-400 to-cyan-300'),
        ('from-[#CB187D] to-[#e84aad]',               'from-emerald-500 to-teal-600'),
        ('from-pink-100 to-rose-100',                  'from-emerald-100 to-teal-100'),
        ('from-pink-50 to-rose-50',                    'from-emerald-50 to-teal-50'),
        ('from-pink-50/60',                            'from-emerald-50/60'),
        ('bg-pink-100 text-pink-700 border border-pink-200', 'bg-emerald-100 text-emerald-700 border border-emerald-200'),
        ('data-color="pink"',                          'data-color="emerald"'),
        ('border border-pink-100',                     'border border-emerald-100'),
        ('text-[#CB187D]',                             'text-emerald-600'),
        ('text-pink-500',                              'text-emerald-500'),
        ('text-pink-600',                              'text-emerald-600'),
        ('text-pink-700',                              'text-emerald-700'),
        ('border-pink-200',                            'border-emerald-200'),
        ('border-pink-100',                            'border-emerald-100'),
        ('bg-pink-100',                                'bg-emerald-100'),
        ('bg-pink-50',                                 'bg-emerald-50'),
        ('from-pink-',                                 'from-emerald-'),
        ('to-rose-',                                   'to-teal-'),
        ('via-pink-',                                  'via-teal-'),
    ]

def rules_pink_to_amber():
    return [
        ('from-[#CB187D] via-pink-400 to-rose-300',  'from-amber-500 via-amber-400 to-orange-300'),
        ('from-[#CB187D] to-[#e84aad]',               'from-amber-500 to-orange-600'),
        ('from-pink-100 to-rose-100',                  'from-amber-100 to-orange-100'),
        ('from-pink-50 to-rose-50',                    'from-amber-50 to-orange-50'),
        ('from-pink-50/60',                            'from-amber-50/60'),
        ('bg-pink-100 text-pink-700 border border-pink-200', 'bg-amber-100 text-amber-700 border border-amber-200'),
        ('data-color="pink"',                          'data-color="amber"'),
        ('border border-pink-100',                     'border border-amber-100'),
        ('text-[#CB187D]',                             'text-amber-600'),
        ('text-pink-500',                              'text-amber-500'),
        ('text-pink-600',                              'text-amber-600'),
        ('text-pink-700',                              'text-amber-700'),
        ('border-pink-200',                            'border-amber-200'),
        ('border-pink-100',                            'border-amber-100'),
        ('bg-pink-100',                                'bg-amber-100'),
        ('bg-pink-50',                                 'bg-amber-50'),
        ('from-pink-',                                 'from-amber-'),
        ('to-rose-',                                   'to-orange-'),
        ('via-pink-',                                  'via-amber-'),
    ]

def rules_violet_to_amber():
    return [
        ('from-violet-500 via-purple-400 to-fuchsia-300', 'from-amber-500 via-amber-400 to-orange-300'),
        ('from-violet-500 to-purple-600',              'from-amber-500 to-orange-600'),
        ('from-violet-100 to-purple-100',              'from-amber-100 to-orange-100'),
        ('from-violet-50 to-purple-50',                'from-amber-50 to-orange-50'),
        ('from-violet-50/60',                          'from-amber-50/60'),
        ('bg-violet-100 text-violet-700 border border-violet-200', 'bg-amber-100 text-amber-700 border border-amber-200'),
        ('data-color="violet"',                        'data-color="amber"'),
        ('border border-violet-100',                   'border border-amber-100'),
        ('text-violet-600',                            'text-amber-600'),
        ('text-violet-500',                            'text-amber-500'),
        ('text-violet-700',                            'text-amber-700'),
        ('border-violet-200',                          'border-amber-200'),
        ('border-violet-100',                          'border-amber-100'),
        ('bg-violet-100',                              'bg-amber-100'),
        ('bg-violet-50',                               'bg-amber-50'),
        ('from-violet-',                               'from-amber-'),
        ('to-purple-',                                 'to-orange-'),
        ('to-fuchsia-',                                'to-orange-'),
        ('via-purple-',                                'via-amber-'),
    ]

def rules_violet_to_cyan():
    return [
        ('from-violet-500 via-purple-400 to-fuchsia-300', 'from-cyan-500 via-cyan-400 to-sky-300'),
        ('from-violet-500 to-purple-600',              'from-cyan-500 to-sky-600'),
        ('from-violet-100 to-purple-100',              'from-cyan-100 to-sky-100'),
        ('from-violet-50 to-purple-50',                'from-cyan-50 to-sky-50'),
        ('from-violet-50/60',                          'from-cyan-50/60'),
        ('bg-violet-100 text-violet-700 border border-violet-200', 'bg-cyan-100 text-cyan-700 border border-cyan-200'),
        ('data-color="violet"',                        'data-color="cyan"'),
        ('border border-violet-100',                   'border border-cyan-100'),
        ('text-violet-600',                            'text-cyan-600'),
        ('text-violet-500',                            'text-cyan-500'),
        ('text-violet-700',                            'text-cyan-700'),
        ('border-violet-200',                          'border-cyan-200'),
        ('border-violet-100',                          'border-cyan-100'),
        ('bg-violet-100',                              'bg-cyan-100'),
        ('bg-violet-50',                               'bg-cyan-50'),
        ('from-violet-',                               'from-cyan-'),
        ('to-purple-',                                 'to-sky-'),
        ('to-fuchsia-',                                'to-sky-'),
        ('via-purple-',                                'via-cyan-'),
    ]

def rules_blue_to_cyan():
    return [
        ('from-blue-500 via-cyan-400 to-teal-300',    'from-cyan-500 via-cyan-400 to-sky-300'),
        ('from-blue-500 to-indigo-600',                'from-cyan-500 to-sky-600'),
        ('from-blue-100 to-indigo-100',                'from-cyan-100 to-sky-100'),
        ('from-blue-50 to-indigo-50',                  'from-cyan-50 to-sky-50'),
        ('from-blue-50/60',                            'from-cyan-50/60'),
        ('bg-blue-100 text-blue-700 border border-blue-200', 'bg-cyan-100 text-cyan-700 border border-cyan-200'),
        ('data-color="blue"',                          'data-color="cyan"'),
        ('border border-blue-100',                     'border border-cyan-100'),
        ('text-blue-600',                              'text-cyan-600'),
        ('text-blue-500',                              'text-cyan-500'),
        ('text-blue-700',                              'text-cyan-700'),
        ('border-blue-200',                            'border-cyan-200'),
        ('border-blue-100',                            'border-cyan-100'),
        ('bg-blue-100',                                'bg-cyan-100'),
        ('bg-blue-50',                                 'bg-cyan-50'),
        ('from-blue-',                                 'from-cyan-'),
        ('to-indigo-',                                 'to-sky-'),
        ('via-indigo-',                                'via-cyan-'),
    ]

def rules_blue_to_pink():
    return [
        ('from-blue-500 via-cyan-400 to-teal-300',    'from-[#CB187D] via-pink-400 to-rose-300'),
        ('from-blue-500 to-indigo-600',                'from-[#CB187D] to-[#e84aad]'),
        ('from-blue-100 to-indigo-100',                'from-pink-100 to-rose-100'),
        ('from-blue-50 to-indigo-50',                  'from-pink-50 to-rose-50'),
        ('from-blue-50/60',                            'from-pink-50/60'),
        ('bg-blue-100 text-blue-700 border border-blue-200', 'bg-pink-100 text-pink-700 border border-pink-200'),
        ('data-color="blue"',                          'data-color="pink"'),
        ('border border-blue-100',                     'border border-pink-100'),
        ('text-blue-600',                              'text-[#CB187D]'),
        ('text-blue-500',                              'text-pink-500'),
        ('text-blue-700',                              'text-pink-700'),
        ('border-blue-200',                            'border-pink-200'),
        ('border-blue-100',                            'border-pink-100'),
        ('bg-blue-100',                                'bg-pink-100'),
        ('bg-blue-50',                                 'bg-pink-50'),
        ('from-blue-',                                 'from-pink-'),
        ('to-indigo-',                                 'to-rose-'),
        ('via-indigo-',                                'via-pink-'),
        ('via-cyan-',                                  'via-pink-'),
    ]

def rules_emerald_to_pink():
    return [
        (r'from-emerald-500 via-(?:teal|green|emerald)-\d+ to-(?:teal|cyan|green)-\d+', 'from-[#CB187D] via-pink-400 to-rose-300'),
        (r'from-emerald-500 to-(?:teal|green)-\d+',   'from-[#CB187D] to-[#e84aad]'),
        ('from-emerald-100 to-teal-100',               'from-pink-100 to-rose-100'),
        ('from-emerald-50 to-teal-50',                 'from-pink-50 to-rose-50'),
        ('from-emerald-50/60',                         'from-pink-50/60'),
        ('bg-emerald-100 text-emerald-700 border border-emerald-200', 'bg-pink-100 text-pink-700 border border-pink-200'),
        ('data-color="emerald"',                       'data-color="pink"'),
        ('border border-emerald-100',                  'border border-pink-100'),
        ('text-emerald-600',                           'text-[#CB187D]'),
        ('text-emerald-500',                           'text-pink-500'),
        ('text-emerald-700',                           'text-pink-700'),
        ('border-emerald-200',                         'border-pink-200'),
        ('border-emerald-100',                         'border-pink-100'),
        ('bg-emerald-100',                             'bg-pink-100'),
        ('bg-emerald-50',                              'bg-pink-50'),
        ('from-emerald-',                              'from-pink-'),
        ('to-teal-',                                   'to-rose-'),
        ('to-green-',                                  'to-rose-'),
        ('via-teal-',                                  'via-pink-'),
        ('via-green-',                                 'via-pink-'),
        ('via-emerald-',                               'via-pink-'),
    ]

def rules_emerald_to_violet():
    return [
        (r'from-emerald-500 via-(?:teal|green|emerald)-\d+ to-(?:teal|cyan|green)-\d+', 'from-violet-500 via-purple-400 to-fuchsia-300'),
        (r'from-emerald-500 to-(?:teal|green)-\d+',   'from-violet-500 to-purple-600'),
        ('from-emerald-100 to-teal-100',               'from-violet-100 to-purple-100'),
        ('from-emerald-50 to-teal-50',                 'from-violet-50 to-purple-50'),
        ('from-emerald-50/60',                         'from-violet-50/60'),
        ('bg-emerald-100 text-emerald-700 border border-emerald-200', 'bg-violet-100 text-violet-700 border border-violet-200'),
        ('data-color="emerald"',                       'data-color="violet"'),
        ('border border-emerald-100',                  'border border-violet-100'),
        ('text-emerald-600',                           'text-violet-600'),
        ('text-emerald-500',                           'text-violet-500'),
        ('text-emerald-700',                           'text-violet-700'),
        ('border-emerald-200',                         'border-violet-200'),
        ('border-emerald-100',                         'border-violet-100'),
        ('bg-emerald-100',                             'bg-violet-100'),
        ('bg-emerald-50',                              'bg-violet-50'),
        ('from-emerald-',                              'from-violet-'),
        ('to-teal-',                                   'to-purple-'),
        ('to-green-',                                  'to-purple-'),
        ('via-teal-',                                  'via-purple-'),
        ('via-green-',                                 'via-purple-'),
        ('via-emerald-',                               'via-purple-'),
    ]

def rules_orange_to_amber():
    return [
        (r'from-orange-500 via-(?:orange|amber)-\d+ to-(?:yellow|red|orange)-\d+', 'from-amber-500 via-amber-400 to-orange-300'),
        (r'from-orange-500 to-(?:red|orange)-\d+',    'from-amber-500 to-orange-600'),
        ('from-orange-100 to-red-100',                 'from-amber-100 to-orange-100'),
        ('from-orange-100 to-yellow-100',              'from-amber-100 to-orange-100'),
        ('from-orange-50 to-red-50',                   'from-amber-50 to-orange-50'),
        ('from-orange-50 to-yellow-50',                'from-amber-50 to-orange-50'),
        ('from-orange-50/60',                          'from-amber-50/60'),
        ('data-color="orange"',                        'data-color="amber"'),
        ('border border-orange-100',                   'border border-amber-100'),
        ('text-orange-600',                            'text-amber-600'),
        ('text-orange-500',                            'text-amber-500'),
        ('text-orange-700',                            'text-amber-700'),
        ('border-orange-200',                          'border-amber-200'),
        ('border-orange-100',                          'border-amber-100'),
        ('bg-orange-100',                              'bg-amber-100'),
        ('bg-orange-50',                               'bg-amber-50'),
        ('from-orange-',                               'from-amber-'),
        ('to-red-',                                    'to-orange-'),
        ('to-yellow-',                                 'to-orange-'),
        ('via-orange-',                                'via-amber-'),
        ('via-amber-',                                 'via-amber-'),
    ]

def rules_orange_to_violet():
    return [
        (r'from-orange-500 via-(?:orange|amber)-\d+ to-(?:yellow|red|orange)-\d+', 'from-violet-500 via-purple-400 to-fuchsia-300'),
        (r'from-orange-500 to-(?:red|orange)-\d+',    'from-violet-500 to-purple-600'),
        ('from-orange-100 to-red-100',                 'from-violet-100 to-purple-100'),
        ('from-orange-50 to-red-50',                   'from-violet-50 to-purple-50'),
        ('from-orange-50/60',                          'from-violet-50/60'),
        ('data-color="orange"',                        'data-color="violet"'),
        ('border border-orange-100',                   'border border-violet-100'),
        ('text-orange-600',                            'text-violet-600'),
        ('text-orange-500',                            'text-violet-500'),
        ('text-orange-700',                            'text-violet-700'),
        ('border-orange-200',                          'border-violet-200'),
        ('border-orange-100',                          'border-violet-100'),
        ('bg-orange-100',                              'bg-violet-100'),
        ('bg-orange-50',                               'bg-violet-50'),
        ('from-orange-',                               'from-violet-'),
        ('to-red-',                                    'to-purple-'),
        ('to-yellow-',                                 'to-purple-'),
        ('via-orange-',                                'via-purple-'),
        ('via-amber-',                                 'via-purple-'),
    ]

RULE_MAP = {
    ('pink',    'emerald'): rules_pink_to_emerald,
    ('pink',    'amber'):   rules_pink_to_amber,
    ('violet',  'amber'):   rules_violet_to_amber,
    ('violet',  'cyan'):    rules_violet_to_cyan,
    ('blue',    'cyan'):    rules_blue_to_cyan,
    ('blue',    'pink'):    rules_blue_to_pink,
    ('emerald', 'pink'):    rules_emerald_to_pink,
    ('emerald', 'violet'):  rules_emerald_to_violet,
    ('orange',  'amber'):   rules_orange_to_amber,
    ('orange',  'violet'):  rules_orange_to_violet,
}

def apply_rules(text, rules):
    for old, new in rules:
        if '(?:' in old or old.startswith(r'from-emerald-500 via') or old.startswith(r'from-orange-500'):
            text = re.sub(old, new, text)
        else:
            text = text.replace(old, new)
    return text

def convert_panel(panel_html, from_color, to_color):
    key = (from_color, to_color)
    if key not in RULE_MAP:
        raise ValueError(f'No rules defined for {from_color} -> {to_color}')
    return apply_rules(panel_html, RULE_MAP[key]())

def extract_panels(kc_html):
    starts = [m.start() for m in re.finditer(r'<div class="kc-panel', kc_html)]
    result = []
    for i, s in enumerate(starts):
        e = starts[i+1] if i+1 < len(starts) else len(kc_html)
        result.append((s, e))
    return result

# Per-lesson patches: (filename, panel_index, from_color, to_color)
PATCHES = [
    ('lesson01_pandas_and_dataframes.html',                        3, 'pink',    'emerald'),
    ('lesson01_pandas_and_dataframes.html',                        4, 'violet',  'amber'),
    ('lesson01_pandas_and_dataframes.html',                        5, 'blue',    'cyan'),
    ('lesson02_reading_files_csv_excel_json.html',                 3, 'pink',    'emerald'),
    ('lesson02_reading_files_csv_excel_json.html',                 4, 'violet',  'amber'),
    ('lesson02_reading_files_csv_excel_json.html',                 5, 'blue',    'cyan'),
    ('lesson03_selecting_and_filtering_data.html',                 6, 'emerald', 'pink'),
    ('lesson03_selecting_and_filtering_data.html',                 7, 'orange',  'violet'),
    ('lesson08_exporting_data.html',                               4, 'orange',  'amber'),
    ('lesson11_working_with_parquet_files.html',                   4, 'pink',    'amber'),
    ('lesson11_working_with_parquet_files.html',                   5, 'violet',  'cyan'),
    ('lesson11_working_with_parquet_files.html',                   6, 'blue',    'pink'),
    ('lesson11_working_with_parquet_files.html',                   7, 'emerald', 'violet'),
]

from collections import defaultdict
by_file = defaultdict(list)
for fname, pidx, fc, tc in PATCHES:
    by_file[fname].append((pidx, fc, tc))

for fname, patches in sorted(by_file.items()):
    path = os.path.join(folder, fname)
    content = open(path, encoding='utf-8').read()
    orig = content

    ks_abs = content.find('<section id="key-concepts"')
    ke_abs = content.find('</section>', ks_abs) + 10
    kc = content[ks_abs:ke_abs]

    panel_positions = extract_panels(kc)

    for pidx, fc, tc in sorted(patches, key=lambda x: x[0], reverse=True):
        ps, pe = panel_positions[pidx]
        panel_html = kc[ps:pe]

        dc = re.search(r'data-color="([^"]+)"', panel_html)
        actual = dc.group(1) if dc else '?'
        if actual != fc:
            print(f'  WARN {fname} panel[{pidx}]: expected from={fc} but got={actual}')
            continue

        new_panel = convert_panel(panel_html, fc, tc)
        kc = kc[:ps] + new_panel + kc[pe:]

    new_content = content[:ks_abs] + kc + content[ke_abs:]

    if new_content != orig:
        open(path, 'w', encoding='utf-8').write(new_content)
        print(f'OK {fname}')
    else:
        print(f'SKIP {fname} - no changes')

print('Done.')
