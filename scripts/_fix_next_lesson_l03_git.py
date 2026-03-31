"""Replace #next-lesson body + bottom nav in lesson03 with the canonical template structure."""

import re

TARGET = (
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson03_introduction_to_git_simple_workflow.html"
)

# ── New #next-lesson body content ─────────────────────────────────────────────
NEW_NEXT_BODY = """\

      <!-- Lesson badge -->
      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
          <span class="text-white font-bold text-lg">4</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module 4 · Lesson 4</p>
          <h3 class="text-base font-bold text-gray-800">Git in VS Code</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>

      <!-- 3-card preview grid -->
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-brands:git-alt"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">The Source Control Panel in VS Code</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:code-branch"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Staging &amp; Committing With a Few Clicks</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:rotate-left"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Undoing &amp; Reviewing Changes in the Editor</p>
            </div>
          </div>

        </div>
      </div>
    """

# ── New bottom nav (replaces old raw div) ─────────────────────────────────────
NEW_BOTTOM_NAV = """\
<section>
  <div class="flex flex-col sm:flex-row gap-3">

    <a href="lesson02_project_folder_structure.html" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Project Folder Structure</p>
      </div>
    </a>

    <a href="../../../hub_home_page.html" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>

    <a href="lesson04_git_in_vs_code.html" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Git in VS Code</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>

  </div>
</section>"""


def find_div_end(html: str, content_start: int) -> int:
    """Given the position just after an opening <div ...>, find the matching </div> position."""
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
                return next_close
            pos = next_close + 6
    return -1


def replace_next_lesson_body(html: str) -> str:
    """Replace the body div content inside #next-lesson and fix space-y-4 → space-y-6."""
    section_pos = html.find('<section id="next-lesson">')
    if section_pos == -1:
        print("❌ Could not find <section id=\"next-lesson\">")
        return html

    # Find the body div — may have space-y-4 or space-y-6
    for marker in (
        '<div class="bg-white px-8 py-7 space-y-4">',
        '<div class="bg-white px-8 py-7 space-y-6">',
    ):
        body_div_pos = html.find(marker, section_pos)
        if body_div_pos != -1:
            break
    else:
        print("❌ Could not find #next-lesson body div")
        return html

    content_start = body_div_pos + len(marker)
    close_pos = find_div_end(html, content_start)
    if close_pos == -1:
        print("❌ Could not find closing </div> of #next-lesson body")
        return html

    # Rebuild: ensure body div uses space-y-6
    new_body_open = '<div class="bg-white px-8 py-7 space-y-6">'
    result = html[:body_div_pos] + new_body_open + NEW_NEXT_BODY + html[close_pos:]
    print("  ✅ #next-lesson body replaced (space-y-6)")
    return result


def replace_bottom_nav(html: str) -> str:
    """Replace the old raw div bottom nav with the canonical <section> pattern."""
    # The old nav starts right after </section> of #next-lesson
    old_nav_marker = '<div class="flex flex-col sm:flex-row gap-3 mt-6">'
    nav_pos = html.find(old_nav_marker)
    if nav_pos == -1:
        print("⚠️  Old bottom nav div not found — checking for existing <section> nav")
        # If script run twice, a <section> may already be there
        if '<section>\n  <div class="flex flex-col sm:flex-row gap-3">' in html:
            print("  ℹ️  Canonical <section> nav already present — skipping")
        else:
            print("  ❌ Could not locate bottom nav")
        return html

    content_start = nav_pos + len(old_nav_marker)
    close_pos = find_div_end(html, content_start)
    if close_pos == -1:
        print("❌ Could not find closing </div> of old bottom nav")
        return html

    end_pos = close_pos + len('</div>')
    result = html[:nav_pos] + NEW_BOTTOM_NAV + html[end_pos:]
    print("  ✅ Bottom nav replaced with canonical <section> pattern")
    return result


def main():
    with open(TARGET, encoding="utf-8") as f:
        html = f.read()

    html = replace_next_lesson_body(html)
    html = replace_bottom_nav(html)

    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(html)

    print("\n── Verification ──────────────────────────────────────────")

    # Grab #next-lesson section to next </section> after bottom nav
    nl_start = html.find('<section id="next-lesson">')
    # The bottom nav section ends with </section>, then </main>
    main_close = html.find('</main>', nl_start)
    scope = html[nl_start:main_close]

    checks = [
        # Section shell
        ('id="next-lesson" present',                     'id="next-lesson"' in scope),
        ('scroll-mt-24 present',                         'scroll-mt-24' in scope),
        ('Header icon unchanged (circle-arrow-right)',   'fa6-solid:circle-arrow-right' in scope),
        ('Header title "Next Lesson"',                   '>Next Lesson<' in scope),
        ('body div uses space-y-6',                      'px-8 py-7 space-y-6' in scope),
        # Badge
        ('Badge shows lesson number 4',                  '>4<' in scope),
        ('Badge label "Module 4 · Lesson 4"',            'Module 4 · Lesson 4' in scope),
        ('Badge title "Git in VS Code"',                 'Git in VS Code' in scope),
        ('Badge "Next you will learn:" present',         'Next you will learn:' in scope),
        # Cards
        ('"What You Will Learn" heading',                'What You Will Learn' in scope),
        ('3 obj-card divs in grid',                      scope.count('obj-card flex items-center gap-3') == 3),
        ('Card 1 icon fa6-brands:git-alt',               'fa6-brands:git-alt' in scope),
        ('Card 1 text — Source Control Panel',           'Source Control Panel' in scope),
        ('Card 2 icon fa6-solid:code-branch',            'fa6-solid:code-branch' in scope),
        ('Card 2 text — Staging &amp; Committing',       'Staging &amp; Committing' in scope),
        ('Card 3 icon fa6-solid:rotate-left',            'fa6-solid:rotate-left' in scope),
        ('Card 3 text — Undoing &amp; Reviewing',        'Undoing &amp; Reviewing' in scope),
        # Bottom nav
        ('Bottom nav wrapped in <section>',              '<section>\n  <div class="flex flex-col sm:flex-row gap-3">' in scope),
        ('Previous link — lesson02',                     'lesson02_project_folder_structure.html' in scope),
        ('Previous label "Project Folder Structure"',    'Project Folder Structure' in scope),
        ('All Lessons link — hub_home_page.html',        '../../../hub_home_page.html' in scope),
        ('All Lessons table-cells-large icon',           'fa6-solid:table-cells-large' in scope),
        ('Next link — lesson04',                         'lesson04_git_in_vs_code.html' in scope),
        ('Next label "Git in VS Code"',                  '>Git in VS Code<' in scope),
        ('No old lesson05 references',                   'lesson05_git_in_vs_code.html' not in scope),
        ('No old mt-6 bottom nav div',                   'flex-row gap-3 mt-6' not in scope),
    ]

    passed = sum(1 for _, ok in checks if ok)
    for label, ok in checks:
        print(f"  {'✅' if ok else '❌'} {label}")
    print(f"\n{'✅' if passed == len(checks) else '⚠️'} {passed}/{len(checks)} checks passed")


if __name__ == "__main__":
    main()
