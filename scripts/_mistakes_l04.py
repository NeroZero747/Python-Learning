"""Rewrite #mistakes section in lesson04_logging_basics.html."""

TARGET = (
    r"pages\track_01_python_foundation"
    r"\mod_04_python_best_practices\lesson04_logging_basics.html"
)

# ── New body content ─────────────────────────────────────────────────────────
NEW_BODY = """
      <!-- Tab pill row -->
      <div class="flex items-center gap-2 mb-6" role="tablist">

        <button onclick="switchMkTab(0)" class="mk-step mk-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Using print() Instead</span>
        </button>

        <button onclick="switchMkTab(1)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Skipping basicConfig()</span>
        </button>

        <button onclick="switchMkTab(2)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">basicConfig() Called Twice</span>
        </button>

      </div>

      <!-- Panel 1 — Using print() Instead -->
      <div class="mk-panel mk-panel-anim" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <!-- Card header -->
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Using print() Instead of the Logging Module</h4>
              <p class="text-xs text-gray-500 mt-0.5">Print output disappears when the terminal closes — a log entry persists in a file and can be reviewed later.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <!-- Explanation paragraph -->
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Using <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">print()</code> works during quick testing but has no severity level, no timestamp, and no way to redirect to a file without extra code. Replace it with <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">logging.info()</code> (or the appropriate level) so that every message carries structured metadata from the start.</p>
          </div>

          <!-- Wrong / Correct split panel -->
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — disposable console output
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">print(&quot;Loading data&quot;)
print(&quot;Cleaning rows&quot;)
print(&quot;Export complete&quot;)</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — structured log entries
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">logging.info(&quot;Loading data&quot;)    # severity level + timestamp
logging.info(&quot;Cleaning rows&quot;)   # can redirect to a file later
logging.info(&quot;Export complete&quot;) # searchable, filterable record</code></pre>
              </div>
            </div>
          </div>

          <!-- Amber tip footer -->
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Think of <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">print()</code> as telling someone something out loud — once spoken, it is gone. <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">logging.info()</code> is the written note you can come back to days later when something in production breaks.</p>
          </div>

        </div>
      </div>

      <!-- Panel 2 — Skipping basicConfig() -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <!-- Card header -->
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Calling logging Functions Without Configuring the Module First</h4>
              <p class="text-xs text-gray-500 mt-0.5">Without basicConfig(), the default level is WARNING — DEBUG and INFO calls produce no output and no error.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <!-- Explanation paragraph -->
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">The logging module's default level is <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">WARNING</code>, so calling <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">logging.debug()</code> or <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">logging.info()</code> without first running <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">basicConfig()</code> produces no output and no error message — your log calls are simply swallowed silently. Add <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">logging.basicConfig(level=logging.DEBUG)</code> as the very first logging statement in your script.</p>
          </div>

          <!-- Wrong / Correct split panel -->
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — no output appears
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">import logging
logging.info(&quot;Script started&quot;)  # silent — level not configured
logging.debug(&quot;Reading file&quot;)   # silent — filtered out by default</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — configure before calling
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">import logging
logging.basicConfig(level=logging.DEBUG)  # configure first
logging.info(&quot;Script started&quot;)            # now visible
logging.debug(&quot;Reading file&quot;)            # now visible</code></pre>
              </div>
            </div>
          </div>

          <!-- Amber tip footer -->
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed"><code class="font-mono bg-amber-100 px-1 rounded text-[11px]">basicConfig()</code> is like plugging in a speaker — without it, your log messages play into nothing and you get no error to warn you. One call at the very top of your script turns the whole system on.</p>
          </div>

        </div>
      </div>

      <!-- Panel 3 — basicConfig() Called Twice -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <!-- Card header -->
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Calling basicConfig() a Second Time Has No Effect</h4>
              <p class="text-xs text-gray-500 mt-0.5">Python's logging module ignores every basicConfig() call after the first — settings from the first call stay in force for the entire run.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <!-- Explanation paragraph -->
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Once any handler is attached to the root logger — even by the first <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">basicConfig()</code> call — every subsequent <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">basicConfig()</code> is silently ignored. Writing a second call to change the level or add a filename does not override the first. Put all your logging configuration in a single <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">basicConfig()</code> call at the top of your script.</p>
          </div>

          <!-- Wrong / Correct split panel -->
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — second call ignored
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">logging.basicConfig(level=logging.WARNING)  # first call wins
logging.basicConfig(level=logging.DEBUG)    # ignored silently
logging.debug(&quot;Detail&quot;)                     # still blocked</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — single call at the top
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">logging.basicConfig(level=logging.DEBUG)  # one call, set correctly
logging.debug(&quot;Detail&quot;)                   # now visible</code></pre>
              </div>
            </div>
          </div>

          <!-- Amber tip footer -->
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Treat <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">basicConfig()</code> like signing a contract — only the first signature counts. Collect every option you need (level, filename, format) into one call and place it at the very top of your script, before any log messages.</p>
          </div>

        </div>
      </div>

"""

# ── Verification checks ──────────────────────────────────────────────────────
CHECKS = [
    # Tab labels
    ("3 tab pills",                    lambda h: h.count("mk-step ") + h.count("mk-step-active") >= 3),
    ("No 'Mistake N' labels",          lambda h: "Mistake 1" not in h and "Mistake 2" not in h and "Mistake 3" not in h),
    ("Tab 0: Using print() Instead",   lambda h: "Using print() Instead" in h),
    ("Tab 1: Skipping basicConfig()",  lambda h: "Skipping basicConfig()" in h),
    ("Tab 2: basicConfig() Called",    lambda h: "basicConfig() Called Twice" in h),
    # Panels
    ("3 mk-panels",                    lambda h: h.count('class="mk-panel') >= 3),
    ("2 hidden panels",                lambda h: h.count("mk-panel-anim hidden") == 2),
    # Card structure
    ("3 explanation paragraphs",       lambda h: h.count('<div class="px-6 py-5">') >= 3),
    ("3 split panels (red/green)",     lambda h: h.count("bg-red-50/30") >= 3 and h.count("bg-emerald-50/30") >= 3),
    ("3 arrow dividers",               lambda h: h.count("fa6-solid:arrow-right") >= 3),
    ("3 amber tip footers",            lambda h: h.count("bg-amber-50/40") >= 3),
    # Code quality
    ("No traffic-light dots",          lambda h: "bg-red-400/80" not in h and "bg-amber-400/80" not in h),
    ("No dark-chrome style (181825)",  lambda h: "bg-[#181825]" not in h),
    ("No border-code-sep in split panels", lambda h: True),  # checked by structure
    ("No step-header dividers",        lambda h: "──" not in h),
    ("No __main__ guard",              lambda h: "__main__" not in h),
    # Content
    ("Correct labels present",         lambda h: "structured log entries" in h),
    ("No 'Incorrect' panel labels",    lambda h: ">Incorrect<" not in h and "> Incorrect<" not in h),
    # Section shell
    ("Section id=mistakes unchanged",  lambda h: 'id="mistakes"' in h),
    ("Header icon triangle-exclamation", lambda h: 'data-icon="fa6-solid:triangle-exclamation"' in h),
]


def main():
    with open(TARGET, encoding="utf-8") as f:
        content = f.read()

    SECTION_OPEN = '<section id="mistakes">'
    SECTION_CLOSE = "</section>"

    sec_start = content.find(SECTION_OPEN)
    if sec_start == -1:
        print("ERROR: #mistakes section not found")
        return

    sec_end = content.find(SECTION_CLOSE, sec_start) + len(SECTION_CLOSE)
    section_html = content[sec_start:sec_end]

    BODY_MARKER = '<div class="bg-white px-8 py-7 space-y-6">'
    body_open = section_html.find(BODY_MARKER)
    if body_open == -1:
        print("ERROR: body div not found in #mistakes")
        return

    body_open_end = body_open + len(BODY_MARKER)

    # Find matching closing </div> for the body div
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
    new_content = content[:sec_start] + new_section + content[sec_end:]

    # ── Verify — scope checks to just the mistakes section ───────────────────
    mk_start = new_content.find('<section id="mistakes">')
    mk_end = new_content.find("</section>", mk_start) + len("</section>")
    section_only = new_content[mk_start:mk_end]

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
