"""
Rewrites the #key-ideas section body in lesson04_logging_basics.html
and ensures the obj-card-kt:hover CSS has border-color: #CB187D.
"""

TARGET = r'pages\track_01_python_foundation\mod_04_python_best_practices\lesson04_logging_basics.html'

# ── New section body ──────────────────────────────────────────────────────────
NEW_BODY = '''<div class="bg-white px-8 py-7 space-y-4">

<div class="obj-card obj-card-kt rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:hard-drive"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Logging Outlasts Your Session</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">A print statement disappears the moment your terminal closes, but a log file stays on disk so you can review exactly what happened hours or days later.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Persistent logs</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">File output</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Post-mortem review</span>
    </div>
  </div>
</div>

<div class="obj-card obj-card-violet rounded-2xl border border-violet-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:sliders"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">One Setting Silences Debug Noise</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">Raise your logger\u2019s minimum level to WARNING and every DEBUG and INFO message disappears instantly \u2014 without touching a single line of your script\u2019s logic.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Level filter</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">WARNING threshold</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Zero edits</span>
    </div>
  </div>
</div>

<div class="obj-card obj-card-blue rounded-2xl border border-blue-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:clock"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Timestamps Come for Free</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">Unlike recording the current time into an Excel cell by hand, Python\u2019s logging formatter stamps every message with the exact date and time automatically.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Auto-timestamp</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">No extra code</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Built-in datetime</span>
    </div>
  </div>
</div>

</div>'''

# ── Read file ─────────────────────────────────────────────────────────────────
with open(TARGET, encoding='utf-8') as fh:
    content = fh.read()

# ── Fix 1: add border-color to obj-card-kt:hover if missing ──────────────────
OLD_KT = '.obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }'
NEW_KT = '.obj-card-kt:hover { box-shadow: none; background-color: #ffffff; border-color: #CB187D; }'
if OLD_KT in content:
    content = content.replace(OLD_KT, NEW_KT, 1)
    print('CSS fix: added border-color to obj-card-kt:hover')
elif NEW_KT in content:
    print('CSS fix: obj-card-kt:hover already has border-color — skipped')
else:
    print('WARNING: obj-card-kt:hover rule not found in expected form')

# ── Fix 2: replace #key-ideas body div ───────────────────────────────────────
BODY_OPEN = '<div class="bg-white px-8 py-7 space-y-4">'

sec_start = content.find('<section id="key-ideas">')
if sec_start == -1:
    print('ERROR: <section id="key-ideas"> not found'); exit(1)

body_start = content.find(BODY_OPEN, sec_start)
if body_start == -1:
    print('ERROR: body div not found in #key-ideas'); exit(1)

# Walk the div nesting to find the matching </div>
depth = 0
pos = body_start
while pos < len(content):
    open_pos = content.find('<div', pos)
    close_pos = content.find('</div>', pos)
    if open_pos == -1 and close_pos == -1:
        break
    if open_pos != -1 and (close_pos == -1 or open_pos < close_pos):
        depth += 1
        pos = open_pos + 4
    else:
        depth -= 1
        pos = close_pos + 6
        if depth == 0:
            body_end = pos
            break

new_content = content[:body_start] + NEW_BODY + content[body_end:]

with open(TARGET, 'w', encoding='utf-8') as fh:
    fh.write(new_content)

print('Section written successfully.')

# ── Verify ────────────────────────────────────────────────────────────────────
with open(TARGET, encoding='utf-8') as fh:
    result = fh.read()

s = result.find('<section id="key-ideas">')
e = result.find('</section>', s) + len('</section>')
section = result[s:e]

checks = [
    ('3 obj-cards total',             section.count('obj-card obj-card-') == 3),
    ('Pink card present',             'obj-card-kt' in section),
    ('Violet card present',           'obj-card-violet' in section),
    ('Blue card present',             'obj-card-blue' in section),
    ('Pink gradient bar',             'from-[#CB187D] to-[#e84aad]' in section),
    ('Violet gradient bar',           'from-violet-500 to-purple-400' in section),
    ('Blue gradient bar',             'from-blue-500 to-indigo-400' in section),
    ('Icon fa6-solid:hard-drive',     'fa6-solid:hard-drive' in section),
    ('Icon fa6-solid:sliders',        'fa6-solid:sliders' in section),
    ('Icon fa6-solid:clock',          'fa6-solid:clock' in section),
    ('Title 1: Logging Outlasts',     'Logging Outlasts Your Session' in section),
    ('Title 2: One Setting',          'One Setting Silences Debug Noise' in section),
    ('Title 3: Timestamps',           'Timestamps Come for Free' in section),
    ('3 descriptions present',        section.count('text-xs text-gray-600 leading-relaxed mb-4') == 3),
    ('9 pills total (3 per card)',     section.count('rounded-full text-[11px] font-semibold') == 9),
    ('No old split-panel layout',     'md:w-1/2' not in section),
    ('No old pre blocks',             '<pre class="font-mono' not in section),
    ('No overview topics repeated',   'severity levels' not in section),
    ('CSS kt border-color fixed',     'border-color: #CB187D; }' in result),
    ('space-y-4 preserved',           'space-y-4' in section),
]

print()
all_ok = True
for label, ok in checks:
    print(f'  {"OK  " if ok else "FAIL"}: {label}')
    if not ok:
        all_ok = False

print()
print('All checks passed.' if all_ok else 'Some checks FAILED.')
