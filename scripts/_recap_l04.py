"""Rewrite #recap section in lesson04_logging_basics.html (mirror objectives)."""

TARGET = (
    r"pages\track_01_python_foundation"
    r"\mod_04_python_best_practices\lesson04_logging_basics.html"
)

# Objective cards (copied exactly from #objective):
# Card 1: label="What logging is",          icon=fa6-solid:scroll
# Card 2: label="Logging levels explained",  icon=fa6-solid:triangle-exclamation
# Card 3: label="Writing logs to a file",    icon=fa6-solid:file-lines
# Card 4: label="Replacing print with logging", icon=fa6-solid:bug-slash

NEW_BODY = """
        <!-- 2x2 Recap card grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

          <!-- Card 01 -->
          <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
            <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
              <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
              <div class="relative flex items-start gap-3">
                <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                  <span class="iconify text-sm" data-icon="fa6-solid:scroll"></span>
                </span>
                <div>
                  <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">What logging is</p>
                  <p class="text-[11px] text-gray-600 leading-snug">Python's <code class="font-mono">logging</code> module writes timestamped event records your script produces as it runs.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Card 02 -->
          <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
            <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
              <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
              <div class="relative flex items-start gap-3">
                <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                  <span class="iconify text-sm" data-icon="fa6-solid:triangle-exclamation"></span>
                </span>
                <div>
                  <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Logging levels explained</p>
                  <p class="text-[11px] text-gray-600 leading-snug">You set a threshold — <code class="font-mono">DEBUG</code>, <code class="font-mono">INFO</code>, <code class="font-mono">WARNING</code>, <code class="font-mono">ERROR</code>, <code class="font-mono">CRITICAL</code> — and messages below it stay silent.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Card 03 -->
          <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
            <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
              <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
              <div class="relative flex items-start gap-3">
                <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                  <span class="iconify text-sm" data-icon="fa6-solid:file-lines"></span>
                </span>
                <div>
                  <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Writing logs to a file</p>
                  <p class="text-[11px] text-gray-600 leading-snug">Passing <code class="font-mono">filename=</code> to <code class="font-mono">basicConfig()</code> saves every message to a file your team can read days later.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Card 04 -->
          <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
            <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
              <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
              <div class="relative flex items-start gap-3">
                <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                  <span class="iconify text-sm" data-icon="fa6-solid:bug-slash"></span>
                </span>
                <div>
                  <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Replacing print with logging</p>
                  <p class="text-[11px] text-gray-600 leading-snug">Swapping <code class="font-mono">print()</code> for <code class="font-mono">logging.info()</code> gives every message a level, a timestamp, and a one-line off switch.</p>
                </div>
              </div>
            </div>
          </div>

        </div>

        <!-- Completion banner -->
        <div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">
          <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">&#10003;</span>
          <div class="relative flex items-center gap-4">
            <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">
              <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-white">Lesson Complete!</p>
              <p class="text-xs text-white/80 mt-0.5">You&#39;ve covered 4 key concepts. Ready for the knowledge check?</p>
            </div>
          </div>
        </div>

"""

# ── Verification checks ──────────────────────────────────────────────────────
CHECKS = [
    # Shell
    ("Section id=recap unchanged",        lambda h: 'id="recap"' in h),
    ("Header icon list-check unchanged",  lambda h: 'data-icon="fa6-solid:list-check"' in h),
    # Cards match objectives
    ("Card 1 label: What logging is",     lambda h: "What logging is" in h),
    ("Card 1 icon: scroll",               lambda h: 'data-icon="fa6-solid:scroll"' in h),
    ("Card 2 label: Logging levels",      lambda h: "Logging levels explained" in h),
    ("Card 2 icon: triangle-exclamation", lambda h: 'data-icon="fa6-solid:triangle-exclamation"' in h),
    ("Card 3 label: Writing logs to a file", lambda h: "Writing logs to a file" in h),
    ("Card 3 icon: file-lines",           lambda h: 'data-icon="fa6-solid:file-lines"' in h),
    ("Card 4 label: Replacing print",     lambda h: "Replacing print with logging" in h),
    ("Card 4 icon: bug-slash",            lambda h: 'data-icon="fa6-solid:bug-slash"' in h),
    # Structure
    ("Watermarks 01 02 03 04",            lambda h: "01</span>" in h and "02</span>" in h and "03</span>" in h and "04</span>" in h),
    ("No watermark 05+",                  lambda h: "05</span>" not in h and "06</span>" not in h),
    ("Exactly 4 recap cards",             lambda h: h.count("from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5") == 4),
    ("Labels use uppercase tracking",     lambda h: h.count("uppercase tracking-widest text-[#CB187D]") >= 4),
    ("Sentences use text-[11px]",         lambda h: h.count('text-[11px] text-gray-600') >= 4),
    # Completion banner
    ("Trophy banner present",             lambda h: 'data-icon="fa6-solid:trophy"' in h),
    ("4 key concepts in banner",          lambda h: "4 key concepts" in h),
    ("Lesson Complete text",              lambda h: "Lesson Complete!" in h),
    # Old content gone
    ("No old generic content",            lambda h: "use Git for version control" not in h and "organize code into modules" not in h),
    ("No check-only icons in cards",      lambda h: h.count('data-icon="fa6-solid:check"') == 0 or "trophy" in h),  # trophy has check mark glyph ✓
]


def main():
    with open(TARGET, encoding="utf-8") as f:
        content = f.read()

    SECTION_OPEN = '<section id="recap">'
    SECTION_CLOSE = "</section>"

    sec_start = content.find(SECTION_OPEN)
    if sec_start == -1:
        print("ERROR: #recap section not found")
        return

    sec_end = content.find(SECTION_CLOSE, sec_start) + len(SECTION_CLOSE)
    section_html = content[sec_start:sec_end]

    BODY_MARKER = '<div class="bg-white px-8 py-7 space-y-6">'
    body_open = section_html.find(BODY_MARKER)
    if body_open == -1:
        print("ERROR: body div not found in #recap")
        return

    body_open_end = body_open + len(BODY_MARKER)

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
    new_content = content[:sec_start] + new_section + content[sec_end:]

    # Verify — scope to section only
    rc_start = new_content.find(SECTION_OPEN)
    rc_end = new_content.find(SECTION_CLOSE, rc_start) + len(SECTION_CLOSE)
    section_only = new_content[rc_start:rc_end]

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
