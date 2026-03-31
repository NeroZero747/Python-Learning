"""Rewrite #real-world section in lesson04_logging_basics.html."""

TARGET = (
    r"pages\track_01_python_foundation"
    r"\mod_04_python_best_practices\lesson04_logging_basics.html"
)

# ── New body content (goes inside the space-y-5 wrapper) ────────────────────
NEW_BODY = """
        <!-- Intro paragraph -->
        <p class="text-sm text-gray-600 leading-relaxed">Imagine you are part of a data team that runs automated scripts overnight. Something breaks at 2 am — and by morning, all you have is a blank screen. The logging module lets every script write a permanent, timestamped record of what it did, so you can trace exactly where things went wrong without being there to watch.</p>

        <!-- Three scenario cards -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">

          <!-- Card 1 — violet: overnight pipeline -->
          <div class="relative rounded-2xl overflow-hidden border border-violet-100 bg-gradient-to-br from-violet-50 via-white to-purple-50 px-6 py-6 text-center">
            <div class="flex flex-col items-center gap-3">
              <span class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-violet-500 to-purple-600 shadow-lg shadow-violet-200">
                <span class="iconify text-white text-2xl" data-icon="fa6-solid:database"></span>
              </span>
              <h3 class="text-sm font-bold text-gray-800 leading-snug">An overnight pipeline<br>fails silently</h3>
              <p class="text-xs text-gray-500 leading-relaxed">Without logs, you have no record of where a five-step ETL job stopped. You call <code class="font-mono text-violet-700">logging.info()</code> after each step so the log always shows the exact point of failure.</p>
              <div class="flex items-center gap-1.5 mt-1 px-3 py-1.5 rounded-full bg-violet-100 border border-violet-200">
                <span class="iconify text-violet-700 text-[11px]" data-icon="fa6-solid:arrow-right-from-bracket"></span>
                <span class="text-[11px] font-semibold text-violet-700">returns <code class="font-mono">INFO:root: message</code></span>
              </div>
            </div>
          </div>

          <!-- Card 2 — pink: wrong report totals -->
          <div class="relative rounded-2xl overflow-hidden border border-pink-100 bg-gradient-to-br from-pink-50 via-white to-rose-50 px-6 py-6 text-center">
            <div class="flex flex-col items-center gap-3">
              <span class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-lg shadow-pink-200">
                <span class="iconify text-white text-2xl" data-icon="fa6-solid:triangle-exclamation"></span>
              </span>
              <h3 class="text-sm font-bold text-gray-800 leading-snug">A weekly report<br>produces wrong totals</h3>
              <p class="text-xs text-gray-500 leading-relaxed">You add <code class="font-mono text-[#CB187D]">logging.warning()</code> calls whenever a column is blank or a price is negative. The log file pinpoints bad rows so you fix the source data, not just the output.</p>
              <div class="flex items-center gap-1.5 mt-1 px-3 py-1.5 rounded-full bg-pink-100 border border-pink-200">
                <span class="iconify text-[#CB187D] text-[11px]" data-icon="fa6-solid:arrow-right-from-bracket"></span>
                <span class="text-[11px] font-semibold text-[#CB187D]">returns <code class="font-mono">WARNING:root: message</code></span>
              </div>
            </div>
          </div>

          <!-- Card 3 — emerald: audit trail -->
          <div class="relative rounded-2xl overflow-hidden border border-emerald-100 bg-gradient-to-br from-emerald-50 via-white to-teal-50 px-6 py-6 text-center">
            <div class="flex flex-col items-center gap-3">
              <span class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-emerald-500 to-teal-600 shadow-lg shadow-emerald-200">
                <span class="iconify text-white text-2xl" data-icon="fa6-solid:file-lines"></span>
              </span>
              <h3 class="text-sm font-bold text-gray-800 leading-snug">A script ran<br>three days ago</h3>
              <p class="text-xs text-gray-500 leading-relaxed">Your log file has a timestamp on every entry. You scroll to Monday and see exactly what data was loaded, what was skipped, and when the job finished — using one <code class="font-mono text-emerald-700">logging.basicConfig()</code> call.</p>
              <div class="flex items-center gap-1.5 mt-1 px-3 py-1.5 rounded-full bg-emerald-100 border border-emerald-200">
                <span class="iconify text-emerald-700 text-[11px]" data-icon="fa6-solid:arrow-right-from-bracket"></span>
                <span class="text-[11px] font-semibold text-emerald-700">returns <code class="font-mono">analysis.log</code></span>
              </div>
            </div>
          </div>

        </div>

        <!-- Before / After comparison table -->
        <div class="rounded-xl border border-gray-100 overflow-hidden">
          <div class="grid grid-cols-2">

            <!-- Without column -->
            <div class="border-r border-gray-100">
              <div class="flex items-center gap-2 px-4 py-3 bg-red-50 border-b border-red-100">
                <span class="iconify text-red-400 text-sm shrink-0" data-icon="fa6-solid:circle-xmark"></span>
                <p class="text-xs font-bold text-red-500 uppercase tracking-wide">Without logging</p>
              </div>
              <div class="px-4 py-4 space-y-3">
                <div class="flex items-start gap-2.5">
                  <span class="iconify text-red-300 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>
                  <p class="text-xs text-gray-500 leading-relaxed">When the overnight pipeline fails, you have no record of which step broke — you restart the whole job blind.</p>
                </div>
                <div class="flex items-start gap-2.5">
                  <span class="iconify text-red-300 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>
                  <p class="text-xs text-gray-500 leading-relaxed">A bad data row produces a wrong total and you spend hours comparing spreadsheets to find it.</p>
                </div>
                <div class="flex items-start gap-2.5">
                  <span class="iconify text-red-300 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>
                  <p class="text-xs text-gray-500 leading-relaxed">You cannot tell whether last Monday's script used fresh data or stale data from the previous week.</p>
                </div>
              </div>
            </div>

            <!-- With column -->
            <div>
              <div class="flex items-center gap-2 px-4 py-3 bg-[#fdf0f7] border-b border-[#f5c6e0]">
                <span class="iconify text-[#CB187D] text-sm shrink-0" data-icon="fa6-solid:circle-check"></span>
                <p class="text-xs font-bold text-[#CB187D] uppercase tracking-wide">With logging</p>
              </div>
              <div class="px-4 py-4 space-y-3">
                <div class="flex items-start gap-2.5">
                  <span class="iconify text-emerald-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>
                  <p class="text-xs text-gray-500 leading-relaxed"><strong class="text-gray-700">logging.info()</strong> writes a timestamped entry after every step, so you open the log and go straight to the failing line.</p>
                </div>
                <div class="flex items-start gap-2.5">
                  <span class="iconify text-emerald-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>
                  <p class="text-xs text-gray-500 leading-relaxed"><strong class="text-gray-700">logging.warning()</strong> flags every suspect row as it runs — you open the log and the bad row number is already there.</p>
                </div>
                <div class="flex items-start gap-2.5">
                  <span class="iconify text-emerald-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>
                  <p class="text-xs text-gray-500 leading-relaxed"><strong class="text-gray-700">logging.basicConfig()</strong> adds a timestamp to every entry, so Monday's log shows exactly when the file was loaded.</p>
                </div>
              </div>
            </div>

          </div>
        </div>

"""

# ── Verification checks ──────────────────────────────────────────────────────
CHECKS = [
    # Shell
    ("Section id=real-world unchanged",  lambda h: 'id="real-world"' in h),
    ("Header icon briefcase unchanged",  lambda h: 'data-icon="fa6-solid:briefcase"' in h),
    ("Subtitle updated to logging",      lambda h: "logging" in h.split("Real-World Use")[1].split("space-y")[0] or "logging" in h[:200]),
    # Body structure
    ("space-y-5 body wrapper",           lambda h: 'class="bg-white px-8 py-7 space-y-5"' in h),
    # Intro
    ("Intro paragraph present",          lambda h: "data team" in h),
    ("No code blocks in section",        lambda h: "bg-[#181825]" not in h and "bg-code" not in h),
    # Cards
    ("3 scenario cards (grid)",          lambda h: "grid-cols-1 md:grid-cols-3" in h),
    ("Card 1 violet color",              lambda h: "border-violet-100" in h and "from-violet-50" in h),
    ("Card 2 pink color",                lambda h: "border-pink-100" in h and "from-pink-50" in h),
    ("Card 3 emerald color",             lambda h: "border-emerald-100" in h and "from-emerald-50" in h),
    ("3 w-14 h-14 icon badges",          lambda h: h.count("w-14 h-14") >= 3),
    ("3 returns pills",                  lambda h: h.count("arrow-right-from-bracket") >= 3),
    ("Headline br present",              lambda h: "<br>" in h),
    # Before/After table
    ("Without/With table present",       lambda h: "Without logging" in h and "With logging" in h),
    ("Red without header",               lambda h: "bg-red-50" in h and "text-red-500" in h),
    ("Pink with header",                 lambda h: 'bg-[#fdf0f7]' in h and 'text-[#CB187D]' in h),
    ("3 red xmark rows",                 lambda h: h.count("fa6-solid:xmark") >= 3),
    ("3 emerald check rows",             lambda h: h.count("fa6-solid:check") >= 3),
    ("Function names bolded",            lambda h: '<strong class="text-gray-700">logging.info()</strong>' in h),
    ("No generic filler text",           lambda h: "Logging is widely used in production" not in h),
]


def main():
    with open(TARGET, encoding="utf-8") as f:
        content = f.read()

    SECTION_OPEN = '<section id="real-world">'
    SECTION_CLOSE = "</section>"

    sec_start = content.find(SECTION_OPEN)
    if sec_start == -1:
        print("ERROR: #real-world section not found")
        return

    sec_end = content.find(SECTION_CLOSE, sec_start) + len(SECTION_CLOSE)
    section_html = content[sec_start:sec_end]

    # Fix subtitle in the header
    OLD_SUBTITLE = "Practical applications in real-world workflows"
    NEW_SUBTITLE = "How logging is used across real-world workflows"
    section_html = section_html.replace(OLD_SUBTITLE, NEW_SUBTITLE, 1)

    # Replace body wrapper class (space-y-6 → space-y-5) and its contents
    OLD_BODY_OPEN = '<div class="bg-white px-8 py-7 space-y-6">'
    NEW_BODY_OPEN = '<div class="bg-white px-8 py-7 space-y-5">'

    body_marker = OLD_BODY_OPEN
    body_open = section_html.find(body_marker)
    if body_open == -1:
        # Try the space-y-5 version in case already updated
        body_marker = NEW_BODY_OPEN
        body_open = section_html.find(body_marker)
    if body_open == -1:
        print("ERROR: body div not found in #real-world")
        return

    body_open_end = body_open + len(body_marker)

    # Find matching closing </div>
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
    # Also fix the wrapper class
    new_section = new_section.replace(OLD_BODY_OPEN, NEW_BODY_OPEN, 1)

    new_content = content[:sec_start] + new_section + content[sec_end:]

    # Verify — scope to section only
    rw_start = new_content.find(SECTION_OPEN)
    rw_end = new_content.find(SECTION_CLOSE, rw_start) + len(SECTION_CLOSE)
    section_only = new_content[rw_start:rw_end]

    print("\nRunning checks:")
    all_ok = True
    for label, check in CHECKS:
        ok = check(section_only)
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
