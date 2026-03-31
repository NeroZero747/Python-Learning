"""
Rewrites the #code-examples section body in lesson04_logging_basics.html.
"""

TARGET = r'pages\track_01_python_foundation\mod_04_python_best_practices\lesson04_logging_basics.html'

NEW_BODY = '''\
<div class="bg-white px-8 py-7 space-y-6">

      <!-- Tab pill row -->
      <div class="flex items-center gap-2 mb-6" role="tablist">

        <button onclick="switchCeTab(0)" class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Log Your First Message</span>
        </button>

        <button onclick="switchCeTab(1)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Logging Levels in Action</span>
        </button>

        <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
          <span class="ce-step-label text-xs font-bold">Write Logs to a File</span>
        </button>

      </div>

      <!-- ── Panel 1 — Log Your First Message ── -->
      <div class="ce-panel ce-panel-anim" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Log Your First Message</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Script</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">basicConfig()</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">

            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This script sets up Python\u2019s <strong class="text-gray-800">logging module</strong> with one line and records a message. You\u2019ll see how a logged message looks different from a plain <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">print()</code> call.</p>
              </div>
            </div>

            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">first_log.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">import logging                              # load the built-in logging module

logging.basicConfig(level=logging.DEBUG)   # accept all messages, including DEBUG

logging.debug("Checking setup")            # detailed trace \u2014 for diagnosing problems
logging.info("Script started")             # routine progress message
logging.warning("Config file not found")   # something unexpected \u2014 still running</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python first_log.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">
                  DEBUG:root:Checking setup<br>
                  INFO:root:Script started<br>
                  WARNING:root:Config file not found
                </div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Notice the format: Python automatically adds the level name and logger name before your message \u2014 you get that extra context for free without writing any extra code.</p>
            </div>

          </div>
        </div>
      </div><!-- /panel 1 -->

      <!-- ── Panel 2 — Logging Levels in Action ── -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Logging Levels in Action</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Data Pipeline</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Level filter</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">

            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This script records messages at all five <strong class="text-gray-800">severity levels</strong>, then raises the minimum level to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">WARNING</code> so lower-priority messages disappear without any other code changes.</p>
              </div>
            </div>

            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">level_demo.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">import logging

logging.basicConfig(level=logging.WARNING)    # only WARNING and above appear

logging.debug("Loading config")               # hidden \u2014 below the threshold
logging.info("Pipeline started")              # hidden \u2014 below the threshold
logging.warning("Missing values detected")    # shown \u2014 at the threshold
logging.error("Database connection failed")   # shown \u2014 above the threshold
logging.critical("Out of memory \u2014 stopping") # shown \u2014 most urgent level</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python level_demo.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">
                  WARNING:root:Missing values detected<br>
                  ERROR:root:Database connection failed<br>
                  CRITICAL:root:Out of memory \u2014 stopping
                </div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Change <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">logging.WARNING</code> to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">logging.DEBUG</code> and run again \u2014 all five messages appear instantly, with no other edits needed.</p>
            </div>

          </div>
        </div>
      </div><!-- /panel 2 -->

      <!-- ── Panel 3 — Write Logs to a File ── -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Write Logs to a File</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Sales Report</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">FileHandler</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Timestamps</span>
                </div>
              </div>
            </div>
          </div>

          <div class="px-6 py-5 space-y-4">

            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This script saves every log message to a file on disk, with a timestamp on each line. Each run <em>adds</em> to the file rather than overwriting it, so you build up a full history of every time the script ran.</p>
              </div>
            </div>

            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">sales_log.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">import logging

logging.basicConfig(
    filename="sales_report.log",                      # write to this file
    filemode="a",                                     # append \u2014 keeps previous entries
    level=logging.INFO,                               # record INFO and above
    format="%(asctime)s %(levelname)s: %(message)s"   # timestamp + level + text
)
logging.info("Sales report started")                  # first entry in the log file
logging.warning("Missing data in Q3 column")          # flagged for follow-up</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python sales_log.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">
                  <span class="text-gray-500"># output written to sales_report.log:</span><br>
                  2026-03-30 09:14:02 INFO: Sales report started<br>
                  2026-03-30 09:14:02 WARNING: Missing data in Q3 column
                </div>
              </div>
            </div>

            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Use <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">filemode="a"</code> (append) rather than <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">"w"</code> (write) \u2014 append mode keeps every previous run, so you never accidentally erase your audit trail.</p>
            </div>

          </div>
        </div>
      </div><!-- /panel 3 -->

    </div>'''

# ── Read & replace ────────────────────────────────────────────────────────────
with open(TARGET, encoding='utf-8') as fh:
    content = fh.read()

BODY_OPEN = '<div class="bg-white px-8 py-7 space-y-6">'

sec_start = content.find('<section id="code-examples">')
if sec_start == -1:
    print('ERROR: section not found'); exit(1)

body_start = content.find(BODY_OPEN, sec_start)
if body_start == -1:
    print('ERROR: body div not found'); exit(1)

# Walk divs to find matching close
depth = 0
pos = body_start
while pos < len(content):
    open_pos  = content.find('<div', pos)
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

s = result.find('<section id="code-examples">')
e = result.find('</section>', s) + len('</section>')
sec = result[s:e]

checks = [
    ('3 tab pills',                    sec.count('onclick="switchCeTab(') == 3),
    ('No "Example 1/2/3/4" labels',    'Example 1' not in sec and 'Example 2' not in sec),
    ('Tab 0: Log Your First Message',  'Log Your First Message' in sec),
    ('Tab 1: Logging Levels in Action','Logging Levels in Action' in sec),
    ('Tab 2: Write Logs to a File',    'Write Logs to a File' in sec),
    ('3 ce-panels',                    sec.count('class="ce-panel ce-panel-anim') == 3),
    ('2 hidden panels',                sec.count('ce-panel ce-panel-anim hidden"') == 2),
    ('Watermarks 01 02 03',            '01' in sec and '02' in sec and '03' in sec),
    ('No traffic-light dots',          'bg-red-400/80' not in sec),
    ('3 code blocks (Style A)',        sec.count('bg-[#181825]') == 3),
    ('3 terminal panes',               sec.count('bg-[#11111b]') == 3),
    ('3 task-box descriptions',        sec.count('task-box') == 3),
    ('3 amber tips',                   sec.count('bg-amber-tip') == 3),
    ('filename first_log.py',          'first_log.py' in sec),
    ('filename level_demo.py',         'level_demo.py' in sec),
    ('filename sales_log.py',          'sales_log.py' in sec),
    ('Domain pills present',           'Sales Report' in sec and 'Data Pipeline' in sec and 'Script' in sec),
    ('No step-header dividers',        'Step 1' not in sec),
    ('No __main__ guard',              '__name__' not in sec),
    ('No empty task-box (Output:)',    'What This Does</p>\n          <p' not in sec),
]

print()
all_ok = True
for label, ok in checks:
    print(f'  {"OK  " if ok else "FAIL"}: {label}')
    if not ok:
        all_ok = False

print()
print('All checks passed.' if all_ok else 'Some checks FAILED.')
