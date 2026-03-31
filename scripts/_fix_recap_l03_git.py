"""Replace the #recap section body in lesson03 with proper Git recap content mirroring objectives."""

TARGET = (
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson03_introduction_to_git_simple_workflow.html"
)

# Objective labels & icons (copied exactly from #objective section):
# Card 1: "What version control is"    — fa6-solid:code-branch
# Card 2: "Save and undo code changes" — fa6-solid:rotate-left
# Card 3: "Push work to GitLab"        — fa6-solid:arrow-up-from-bracket
# Card 4: "The full Git loop"          — fa6-solid:arrows-rotate

NEW_BODY = '''\
      <!-- 2×2 recap card grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

        <!-- Card 01 -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:code-branch"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">What version control is</p>
                <p class="text-[11px] text-gray-600 leading-snug">Git records every change to your files so you can always return to a version that worked.</p>
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
                <span class="iconify text-sm" data-icon="fa6-solid:rotate-left"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Save and undo code changes</p>
                <p class="text-[11px] text-gray-600 leading-snug"><code class="font-mono">git add</code> stages a file and <code class="font-mono">git commit</code> saves a permanent snapshot you can rewind to.</p>
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
                <span class="iconify text-sm" data-icon="fa6-solid:arrow-up-from-bracket"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Push work to GitLab</p>
                <p class="text-[11px] text-gray-600 leading-snug"><code class="font-mono">git push</code> uploads your commits to GitLab so teammates can see and download your changes.</p>
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
                <span class="iconify text-sm" data-icon="fa6-solid:arrows-rotate"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">The full Git loop</p>
                <p class="text-[11px] text-gray-600 leading-snug">You now follow the modify → stage → commit → push cycle that professional teams use every day.</p>
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
'''


def find_recap_body(html: str):
    """Find start/end indices of the body div inside #recap."""
    section_pos = html.find('<section id="recap">')
    if section_pos == -1:
        return None, None

    marker = '<div class="bg-white px-8 py-7 space-y-6">'
    body_start = html.find(marker, section_pos)
    if body_start == -1:
        return None, None

    content_start = body_start + len(marker)
    depth = 1
    pos = content_start
    while pos < len(html) and depth > 0:
        next_open = html.find('<div', pos)
        next_close = html.find('</div>', pos)
        if next_close == -1:
            break
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            if depth == 0:
                return content_start, next_close
            pos = next_close + 6
    return None, None


def main():
    with open(TARGET, encoding="utf-8") as f:
        html = f.read()

    start, end = find_recap_body(html)
    if start is None:
        print("❌ Could not locate #recap body div")
        return

    new_html = html[:start] + "\n" + NEW_BODY + "    " + html[end:]

    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(new_html)

    print("✅ #recap body replaced")

    # ── Verification ──────────────────────────────────────────────
    recap = new_html[new_html.find('<section id="recap">'):
                     new_html.find('<section id="knowledge-check">')]

    checks = [
        # Section shell
        ("Section id unchanged",            'id="recap"' in recap),
        ("Header icon unchanged",           "fa6-solid:list-check" in recap),
        ("Header title unchanged",          "Lesson Recap" in recap),
        # Watermarks
        ("Watermark 01 present",            ">01<" in recap),
        ("Watermark 02 present",            ">02<" in recap),
        ("Watermark 03 present",            ">03<" in recap),
        ("Watermark 04 present",            ">04<" in recap),
        # Labels — exact copies from objective
        ("Label 1: What version control is","What version control is" in recap),
        ("Label 2: Save and undo code changes","Save and undo code changes" in recap),
        ("Label 3: Push work to GitLab",    "Push work to GitLab" in recap),
        ("Label 4: The full Git loop",      "The full Git loop" in recap),
        # Icons — exact copies from objective
        ("Icon 1: code-branch",             "fa6-solid:code-branch" in recap),
        ("Icon 2: rotate-left",             "fa6-solid:rotate-left" in recap),
        ("Icon 3: arrow-up-from-bracket",   "fa6-solid:arrow-up-from-bracket" in recap),
        ("Icon 4: arrows-rotate",           "fa6-solid:arrows-rotate" in recap),
        # Completion banner
        ("Completion banner present",       "Lesson Complete!" in recap),
        ("4 key concepts in banner",        "4 key concepts" in recap),
        ("Trophy icon present",             "fa6-solid:trophy" in recap),
        ("Banner gradient present",         "from-[#CB187D] to-[#e84aad]" in recap),
    ]

    passed = sum(1 for _, ok in checks if ok)
    for label, ok in checks:
        print(f"  {'✅' if ok else '❌'} {label}")
    print(f"\n{'✅' if passed == len(checks) else '⚠️'} {passed}/{len(checks)} checks passed")


if __name__ == "__main__":
    main()
