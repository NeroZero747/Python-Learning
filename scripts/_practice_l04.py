"""Rewrite #practice section in lesson04_logging_basics.html."""

TARGET = (
    r"pages\track_01_python_foundation"
    r"\mod_04_python_best_practices\lesson04_logging_basics.html"
)

# ── New body content ─────────────────────────────────────────────────────────
NEW_BODY = """
      <!-- Tab pill row -->
      <div class="flex items-center gap-2 mb-6" role="tablist">

        <button onclick="switchPeTab(0)" class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Log a Start Message</span>
        </button>

        <button onclick="switchPeTab(1)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Filter by Level</span>
        </button>

        <button onclick="switchPeTab(2)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Log to a File</span>
        </button>

      </div>

      <!-- ── Panel 1 — Log a Start Message ── -->
      <div class="pe-panel pe-panel-anim" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Log a Start Message</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Scripts</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">basicConfig()</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">logging.DEBUG</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">

            <!-- Task description -->
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">You are writing a daily backup script that needs to record what it is doing as it runs. Set up the logging module with <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">basicConfig()</code> at <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">DEBUG</code> level, then add one log call each at <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">debug</code>, <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">info</code>, and <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">warning</code>. Run the script and check that all three messages appear in the console, each prefixed with its level name.</p>
              </div>
            </div>

            <!-- Show Answer accordion -->
            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>

            <div class="accordion-body">

              <!-- Code block — Style A -->
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">daily_check.py</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">import logging                              # load Python's built-in logging module
logging.basicConfig(level=logging.DEBUG)   # show all messages, including DEBUG
logging.debug("Checking connection")       # lowest level — detailed diagnostic
logging.info("Backup started")             # normal progress message
logging.warning("Disk space below 15%")    # something to pay attention to</code></pre>
                </div>
                <!-- Terminal output pane -->
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ python daily_check.py</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">DEBUG:root:Checking connection<br>INFO:root:Backup started<br>WARNING:root:Disk space below 15%</div>
                </div>
              </div>

              <!-- Amber tip -->
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">The <code class="text-xs font-mono px-1 py-0.5 rounded bg-orange-50 text-gray-700">DEBUG:root:</code> prefix tells you the severity level and the logger name. Changing <code class="text-xs font-mono px-1 py-0.5 rounded bg-orange-50 text-gray-700">level=logging.INFO</code> hides all <code class="text-xs font-mono px-1 py-0.5 rounded bg-orange-50 text-gray-700">debug()</code> calls in a single edit — you do not need to delete or comment them out.</p>
              </div>

            </div>
          </div>

        </div>
      </div>

      <!-- ── Panel 2 — Filter by Level ── -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Filter by Level</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Reports</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">logging.WARNING</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Level threshold</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">

            <!-- Task description -->
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">You are building a weekly report script that logged debug messages while you were testing. Now that it runs in production, you want to suppress those noisy lines. Set <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">basicConfig()</code> to <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">WARNING</code> level, then add one log call each at <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">debug</code>, <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">info</code>, and <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">warning</code>. Run the script and notice that only the warning line appears in the console.</p>
              </div>
            </div>

            <!-- Show Answer accordion -->
            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>

            <div class="accordion-body">

              <!-- Code block — Style A -->
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">report_filter.py</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">import logging                               # import the logging module
logging.basicConfig(level=logging.WARNING)   # only show WARNING and above
logging.debug("Debug details")               # blocked — below the threshold
logging.info("Report started")               # blocked — below the threshold
logging.warning("Missing column")            # shown — at or above WARNING</code></pre>
                </div>
                <!-- Terminal output pane -->
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ python report_filter.py</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">WARNING:root:Missing column</div>
                </div>
              </div>

              <!-- Amber tip -->
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">Setting the level to <code class="text-xs font-mono px-1 py-0.5 rounded bg-orange-50 text-gray-700">WARNING</code> acts like a noise filter — it silently ignores every message below that threshold. You can write as many <code class="text-xs font-mono px-1 py-0.5 rounded bg-orange-50 text-gray-700">logging.debug()</code> calls as you like during development, then suppress them all with one setting change when you deploy.</p>
              </div>

            </div>
          </div>

        </div>
      </div>

      <!-- ── Panel 3 — Log to a File ── -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Log to a File</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-amber-50 text-amber-600 border border-amber-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:fire"></span> Intermediate
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Analysis</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">filename=</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">filemode=&quot;a&quot;</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">

            <!-- Task description -->
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">You are analysing monthly sales data and want to keep a record of what your script did, even after the console closes. Configure the logging module to write messages to a file called <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">analysis.log</code>. Set <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">filemode</code> to <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">&quot;a&quot;</code> so the file grows with each run instead of being overwritten. Add one <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">info</code> and one <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">warning</code> message, then open the file to verify your entries are there.</p>
              </div>
            </div>

            <!-- Show Answer accordion -->
            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>

            <div class="accordion-body">

              <!-- Code block — Style A -->
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">file_logger.py</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">import logging                                # import the logging module
logging.basicConfig(                          # configure file-based logging
    filename=&quot;analysis.log&quot;,                  # write messages to this file
    filemode=&quot;a&quot;,                             # append — keep old entries
    level=logging.INFO,                       # record INFO and above
)
logging.info(&quot;Analysis started&quot;)              # written to analysis.log
logging.warning(&quot;Input has blank rows&quot;)       # also written to analysis.log</code></pre>
                </div>
                <!-- Terminal output pane -->
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ python file_logger.py</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">INFO:root:Analysis started<br>WARNING:root:Input has blank rows</div>
                </div>
              </div>

              <!-- Amber tip -->
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">Using <code class="text-xs font-mono px-1 py-0.5 rounded bg-orange-50 text-gray-700">filemode=&quot;a&quot;</code> (append) means each run adds to the log rather than starting fresh. This gives you a complete history across runs — if something breaks on Friday, you can read back through the file to see exactly what every previous run recorded.</p>
              </div>

            </div>
          </div>

        </div>
      </div>

"""

# ── Verification checks ──────────────────────────────────────────────────────
CHECKS = [
    # Tab labels
    ("3 tab pills",              lambda h: h.count("pe-step ") + h.count("pe-step-active") >= 3),
    ("No 'Exercise N' labels",   lambda h: "Exercise 1" not in h and "Exercise 2" not in h and "Exercise 3" not in h),
    ("Tab 0: Log a Start Message",  lambda h: "Log a Start Message" in h),
    ("Tab 1: Filter by Level",      lambda h: "Filter by Level" in h),
    ("Tab 2: Log to a File",        lambda h: "Log to a File" in h),
    # Panels
    ("3 pe-panels",              lambda h: h.count('class="pe-panel') >= 3),
    ("2 hidden panels",          lambda h: h.count("pe-panel-anim hidden") == 2),
    ("Watermarks 01 02 03",      lambda h: "01</span>" in h and "02</span>" in h and "03</span>" in h),
    # Code quality
    ("No traffic-light dots",    lambda h: "bg-red-400/80" not in h and "bg-amber-400/80" not in h),
    ("3 code blocks (Style A)",  lambda h: h.count("bg-[#181825]") >= 3),
    ("3 terminal panes",         lambda h: h.count("bg-[#11111b]") >= 3),
    # Content
    ("3 task-box descriptions",  lambda h: h.count("task-box") >= 3),
    ("3 amber tips",             lambda h: h.count("bg-amber-tip") >= 3),
    ("No 'Your Task' tag lists", lambda h: "Tags: Logging" not in h),
    # Filenames
    ("Filename daily_check.py",  lambda h: "daily_check.py" in h),
    ("Filename report_filter.py",lambda h: "report_filter.py" in h),
    ("Filename file_logger.py",  lambda h: "file_logger.py" in h),
    # Correctness
    ("No step-header dividers",  lambda h: "──" not in h.split("bg-amber-tip")[0].split("pe-panel")[1] if "pe-panel" in h else True),
    ("No __main__ guard",        lambda h: "__main__" not in h),
    # Icon fix
    ("Header icon is pencil",    lambda h: 'data-icon="fa6-solid:pencil"' in h and 'data-icon="fa6-solid:dumbbell"' not in h),
]


def main():
    with open(TARGET, encoding="utf-8") as f:
        content = f.read()

    # ── 1. Replace body ──────────────────────────────────────────────────────
    SECTION_OPEN = '<section id="practice">'
    SECTION_CLOSE = "</section>"

    sec_start = content.find(SECTION_OPEN)
    if sec_start == -1:
        print("ERROR: #practice section not found")
        return

    sec_end = content.find(SECTION_CLOSE, sec_start) + len(SECTION_CLOSE)

    section_html = content[sec_start:sec_end]

    BODY_MARKER = '<div class="bg-white px-8 py-7 space-y-6">'
    body_open = section_html.find(BODY_MARKER)
    if body_open == -1:
        print("ERROR: body div not found in #practice")
        return

    body_open_end = body_open + len(BODY_MARKER)

    # Find the matching closing </div> for the body div
    depth = 1
    i = body_open_end
    while i < len(section_html) and depth > 0:
        if section_html[i:i+4] == "<div":
            depth += 1
            i += 4
        elif section_html[i:i+6] == "</div>":
            depth -= 1
            if depth == 0:
                body_close = i
                break
            i += 6
        else:
            i += 1

    old_body_inner = section_html[body_open_end:body_close]
    new_section = section_html.replace(old_body_inner, NEW_BODY, 1)

    # Fix section header icon: dumbbell → pencil (scoped to this section only)
    OLD_ICON = 'data-icon="fa6-solid:dumbbell"'
    NEW_ICON = 'data-icon="fa6-solid:pencil"'
    if OLD_ICON in new_section:
        new_section = new_section.replace(OLD_ICON, NEW_ICON, 1)
        print("  Fixed header icon: dumbbell → pencil")
    else:
        print("  (header icon already pencil)")

    new_content = content[:sec_start] + new_section + content[sec_end:]

    # ── 3. Verify ────────────────────────────────────────────────────────────
    practice_start = new_content.find(SECTION_OPEN)
    practice_end = new_content.find(SECTION_CLOSE, practice_start) + len(SECTION_CLOSE)
    practice_html = new_content[practice_start:practice_end]

    print("\nRunning checks:")
    all_ok = True
    for label, check in CHECKS:
        ok = check(practice_html)
        status = "OK  " if ok else "FAIL"
        print(f"  {status}: {label}")
        if not ok:
            all_ok = False

    if not all_ok:
        print("\nSome checks failed — file NOT written.")
        return

    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("\nSection written successfully.\n")
    print("All checks passed.")


if __name__ == "__main__":
    main()
