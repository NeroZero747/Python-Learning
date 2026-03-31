"""Replace the #real-world section body in lesson03 with proper Git scenario content."""

TARGET = (
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson03_introduction_to_git_simple_workflow.html"
)

NEW_BODY = '''\
      <!-- Intro paragraph -->
      <p class="text-sm text-gray-600 leading-relaxed">Every data team produces dozens of scripts, queries, and reports that change week after week. Without version control, a single accidental overwrite can erase hours of work — and no one can tell what changed or who changed it. Git gives every file a full edit history you can search, compare, and rewind at any point.</p>

      <!-- Three scenario cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">

        <!-- Card 1 — violet: git commit -->
        <div class="relative rounded-2xl overflow-hidden border border-violet-100 bg-gradient-to-br from-violet-50 via-white to-purple-50 px-6 py-6 text-center">
          <div class="flex flex-col items-center gap-3">
            <span class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-violet-500 to-purple-600 shadow-lg shadow-violet-200">
              <span class="iconify text-white text-2xl" data-icon="fa6-brands:git-alt"></span>
            </span>
            <h3 class="text-sm font-bold text-gray-800 leading-snug">Your team edits<br>the same script today</h3>
            <p class="text-xs text-gray-500 leading-relaxed">Two analysts updating the same file at once will overwrite each other's work. With <code class="font-mono text-violet-700">git commit</code>, each analyst saves a named snapshot — both versions are preserved and can be merged.</p>
            <div class="flex items-center gap-1.5 mt-1 px-3 py-1.5 rounded-full bg-violet-100 border border-violet-200">
              <span class="iconify text-violet-700 text-[11px]" data-icon="fa6-solid:arrow-right-from-bracket"></span>
              <span class="text-[11px] font-semibold text-violet-700">returns <code class="font-mono">commit hash</code></span>
            </div>
          </div>
        </div>

        <!-- Card 2 — pink: git log -->
        <div class="relative rounded-2xl overflow-hidden border border-pink-100 bg-gradient-to-br from-pink-50 via-white to-rose-50 px-6 py-6 text-center">
          <div class="flex flex-col items-center gap-3">
            <span class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-lg shadow-pink-200">
              <span class="iconify text-white text-2xl" data-icon="fa6-solid:clock-rotate-left"></span>
            </span>
            <h3 class="text-sm font-bold text-gray-800 leading-snug">A report broke<br>after last week's change</h3>
            <p class="text-xs text-gray-500 leading-relaxed">Without history, finding the broken line means reading every change made in the past week by hand. With <code class="font-mono text-[#CB187D]">git log</code>, you see exactly which commit introduced the bug — and can reverse it in one command.</p>
            <div class="flex items-center gap-1.5 mt-1 px-3 py-1.5 rounded-full bg-pink-100 border border-pink-200">
              <span class="iconify text-[#CB187D] text-[11px]" data-icon="fa6-solid:arrow-right-from-bracket"></span>
              <span class="text-[11px] font-semibold text-[#CB187D]">returns <code class="font-mono">commit history</code></span>
            </div>
          </div>
        </div>

        <!-- Card 3 — emerald: git push -->
        <div class="relative rounded-2xl overflow-hidden border border-emerald-100 bg-gradient-to-br from-emerald-50 via-white to-teal-50 px-6 py-6 text-center">
          <div class="flex flex-col items-center gap-3">
            <span class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-emerald-500 to-teal-600 shadow-lg shadow-emerald-200">
              <span class="iconify text-white text-2xl" data-icon="fa6-brands:gitlab"></span>
            </span>
            <h3 class="text-sm font-bold text-gray-800 leading-snug">Your manager wants<br>to review the code</h3>
            <p class="text-xs text-gray-500 leading-relaxed">Emailing script files back and forth creates version chaos immediately. With <code class="font-mono text-emerald-700">git push</code>, your manager gets a single GitLab URL showing every change, comment, and approval in one place.</p>
            <div class="flex items-center gap-1.5 mt-1 px-3 py-1.5 rounded-full bg-emerald-100 border border-emerald-200">
              <span class="iconify text-emerald-700 text-[11px]" data-icon="fa6-solid:arrow-right-from-bracket"></span>
              <span class="text-[11px] font-semibold text-emerald-700">returns <code class="font-mono">remote branch</code></span>
            </div>
          </div>
        </div>

      </div>

      <!-- Before / After comparison table -->
      <div class="rounded-xl border border-gray-100 overflow-hidden">
        <div class="grid grid-cols-2">

          <!-- Without Git column -->
          <div class="border-r border-gray-100">
            <div class="flex items-center gap-2 px-4 py-3 bg-red-50 border-b border-red-100">
              <span class="iconify text-red-400 text-sm shrink-0" data-icon="fa6-solid:circle-xmark"></span>
              <p class="text-xs font-bold text-red-500 uppercase tracking-wide">Without Git</p>
            </div>
            <div class="px-4 py-4 space-y-3">
              <div class="flex items-start gap-2.5">
                <span class="iconify text-red-300 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>
                <p class="text-xs text-gray-500 leading-relaxed">Two analysts editing the same file overwrite each other — the most recent save wins and the other's work is gone.</p>
              </div>
              <div class="flex items-start gap-2.5">
                <span class="iconify text-red-300 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>
                <p class="text-xs text-gray-500 leading-relaxed">Finding which change broke a report means scanning files manually — there is no record of what changed or when.</p>
              </div>
              <div class="flex items-start gap-2.5">
                <span class="iconify text-red-300 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>
                <p class="text-xs text-gray-500 leading-relaxed">Sharing scripts by email creates duplicate files with no way to know which version is the latest or correct one.</p>
              </div>
            </div>
          </div>

          <!-- With Git column -->
          <div>
            <div class="flex items-center gap-2 px-4 py-3 bg-[#fdf0f7] border-b border-[#f5c6e0]">
              <span class="iconify text-[#CB187D] text-sm shrink-0" data-icon="fa6-solid:circle-check"></span>
              <p class="text-xs font-bold text-[#CB187D] uppercase tracking-wide">With Git</p>
            </div>
            <div class="px-4 py-4 space-y-3">
              <div class="flex items-start gap-2.5">
                <span class="iconify text-emerald-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>
                <p class="text-xs text-gray-500 leading-relaxed"><strong class="text-gray-700">git commit</strong> gives each analyst a permanent named snapshot — no work is lost and the team can merge both versions.</p>
              </div>
              <div class="flex items-start gap-2.5">
                <span class="iconify text-emerald-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>
                <p class="text-xs text-gray-500 leading-relaxed"><strong class="text-gray-700">git log</strong> shows every change in order — you can pinpoint the exact commit that introduced the bug and reverse it.</p>
              </div>
              <div class="flex items-start gap-2.5">
                <span class="iconify text-emerald-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>
                <p class="text-xs text-gray-500 leading-relaxed"><strong class="text-gray-700">git push</strong> sends all commits to one GitLab URL — the team always reads from the same single source of truth.</p>
              </div>
            </div>
          </div>

        </div>
      </div>
'''


def find_realworld_body(html: str):
    """Find start/end indices of the body div inside #real-world."""
    section_pos = html.find('<section id="real-world">')
    if section_pos == -1:
        return None, None

    # Body div may use space-y-5 or space-y-6 — search generically
    marker_5 = '<div class="bg-white px-8 py-7 space-y-5">'
    marker_6 = '<div class="bg-white px-8 py-7 space-y-6">'
    pos_5 = html.find(marker_5, section_pos)
    pos_6 = html.find(marker_6, section_pos)

    if pos_5 == -1 and pos_6 == -1:
        return None, None

    if pos_5 == -1:
        body_start = pos_6
        marker = marker_6
    elif pos_6 == -1:
        body_start = pos_5
        marker = marker_5
    else:
        # pick whichever comes first
        if pos_5 < pos_6:
            body_start = pos_5
            marker = marker_5
        else:
            body_start = pos_6
            marker = marker_6

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

    start, end = find_realworld_body(html)
    if start is None:
        print("❌ Could not locate #real-world body div")
        return

    # Also fix the subtitle and space-y value in the body wrapper
    # Replace the body wrapper class to ensure space-y-5
    section_start = html.find('<section id="real-world">')
    body_tag_start = html.rfind('<div class="bg-white px-8 py-7', section_start, start)
    body_tag_end = html.find('>', body_tag_start) + 1

    old_body_tag = html[body_tag_start:body_tag_end]
    # Normalise to space-y-5
    new_body_tag = '<div class="bg-white px-8 py-7 space-y-5">'

    html = html[:body_tag_start] + new_body_tag + html[body_tag_end:]

    # Re-find start/end after tag replacement (length may have changed)
    start, end = find_realworld_body(html)
    if start is None:
        print("❌ Could not re-locate #real-world body div after tag fix")
        return

    # Also fix the subtitle in the section header
    html = html.replace(
        '<p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Practical applications in real-world workflows</p>',
        '<p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">How Git is used across real data team workflows</p>',
        # Only replace within the real-world section
    )

    # Re-find again after subtitle fix
    start, end = find_realworld_body(html)

    new_html = html[:start] + "\n" + NEW_BODY + "    " + html[end:]

    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(new_html)

    print("✅ #real-world body replaced")

    # ── Verification ──────────────────────────────────────────────
    rw = new_html[new_html.find('<section id="real-world">'):
                  new_html.find('<section id="recap">')]

    checks = [
        # Section shell
        ("Section id unchanged",            'id="real-world"' in rw),
        ("Header icon unchanged",           "fa6-solid:briefcase" in rw),
        ("Header title unchanged",          "Real-World Use" in rw),
        ("Body uses space-y-5",             "space-y-5" in rw),
        ("Subtitle updated",                "How Git is used" in rw),
        # Intro paragraph
        ("Intro paragraph present",         "data team" in rw and "overwrite" in rw),
        # Three cards
        ("Card 1 violet border",            "border-violet-100" in rw),
        ("Card 2 pink border",              "border-pink-100" in rw),
        ("Card 3 emerald border",           "border-emerald-100" in rw),
        ("Card 1 icon git-alt",             "fa6-brands:git-alt" in rw),
        ("Card 2 icon clock-rotate-left",   "fa6-solid:clock-rotate-left" in rw),
        ("Card 3 icon gitlab",              "fa6-brands:gitlab" in rw),
        ("Card 1 headline present",         "same script today" in rw),
        ("Card 2 headline present",         "last week" in rw),
        ("Card 3 headline present",         "review the code" in rw),
        # Returns pills
        ("Returns pills (3)",               rw.count("fa6-solid:arrow-right-from-bracket") >= 3),
        ("Pill 1: commit hash",             "commit hash" in rw),
        ("Pill 2: commit history",          "commit history" in rw),
        ("Pill 3: remote branch",           "remote branch" in rw),
        # Before/after table
        ("Without Git header",              "Without Git" in rw),
        ("With Git header",                 "With Git" in rw),
        ("3 ✗ rows",                        rw.count('data-icon="fa6-solid:xmark"') >= 3),
        ("3 ✓ rows",                        rw.count('data-icon="fa6-solid:check"') >= 3),
        ("git commit bolded",               '<strong class="text-gray-700">git commit</strong>' in rw),
        ("git log bolded",                  '<strong class="text-gray-700">git log</strong>' in rw),
        ("git push bolded",                 '<strong class="text-gray-700">git push</strong>' in rw),
        # No code blocks
        ("No code blocks in section",       "<pre " not in rw),
    ]

    passed = sum(1 for _, ok in checks if ok)
    for label, ok in checks:
        print(f"  {'✅' if ok else '❌'} {label}")
    print(f"\n{'✅' if passed == len(checks) else '⚠️'} {passed}/{len(checks)} checks passed")


if __name__ == "__main__":
    main()
