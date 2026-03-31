"""Rewrite the #overview section body in lesson02_project_folder_structure.html.

Analogy: a well-organized filing cabinet
  - Cabinet = the project folder
  - Labeled drawers = named subfolders (scripts, data, config)
  - Documents in each drawer = individual .py / .csv files
  - The cabinet model = the standard analytics project layout
"""

from pathlib import Path

TARGET = Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices"
    "/lesson02_project_folder_structure.html"
)

# The full replacement body (everything inside the space-y-5 div,
# starting after the hook banner closing </div> and ending before
# the body div's own closing </div>).
HOOK_BANNER = """\
<div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
  <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Py</span>
  <div class="relative flex items-center gap-4">
    <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">
      <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>
    </span>
    <p class="text-base text-gray-800 leading-relaxed font-medium">A project folder structure is the system of subfolders that gives every file in your Python project a clear, predictable home.</p>
  </div>
</div>

<!-- Part 2 — Analogy intro paragraph -->
<p class="text-sm text-gray-600 leading-relaxed">Think of your Python project like a filing cabinet: the whole cabinet is your project folder, each drawer holds a different type of file, and every document inside has a labeled home so you can find it in seconds. A <strong>project folder structure</strong> is that cabinet, and Python is the language you use to create everything inside it.</p>

<!-- Part 3 — Analogy card grid -->
<div class="grid grid-cols-1 sm:grid-cols-2 gap-3">

  <!-- Card 1 — pink accent: why structure matters -->
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
        <span class="iconify text-brand text-base" data-icon="fa6-solid:folder-open"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">Why structure matters</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">The cabinet itself — tidy cabinets find things; messy desks don't</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">The bigger the project, the more a clear layout saves you time.</p>
  </div>

  <!-- Card 2 — violet accent: organizing into folders -->
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-violet-100 hover:bg-violet-50/30 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-violet-50 shrink-0">
        <span class="iconify text-violet-500 text-base" data-icon="fa6-solid:folder-tree"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">Organizing into folders</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">The labeled drawers — one for scripts, one for data, one for config</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">Each drawer holds one type of file so you always know where to look.</p>
  </div>

  <!-- Card 3 — blue accent: splitting scripts by purpose -->
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-blue-100 hover:bg-blue-50/30 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-blue-50 shrink-0">
        <span class="iconify text-blue-500 text-base" data-icon="fa6-solid:file-code"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">One script, one job</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">The document in each drawer — focused on a single task</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">Focused files let you fix one step without touching everything else.</p>
  </div>

  <!-- Card 4 — emerald accent: a typical analytics layout -->
  <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-emerald-100 hover:bg-emerald-50/30 transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-emerald-50 shrink-0">
        <span class="iconify text-emerald-500 text-base" data-icon="fa6-solid:layer-group"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">The standard layout</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">The cabinet model — a format any colleague navigates instantly</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">One shared layout means any new project starts with a familiar structure.</p>
  </div>

</div>

<!-- Part 4 — Amber tip -->
<div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">If you already create folders on your desktop to separate work by project or date, you already understand the thinking — this lesson shows you the standard way Python projects apply that same habit.</p>
</div>"""


def main():
    html = TARGET.read_text(encoding="utf-8")

    # Locate the overview section body div
    overview_start = html.index('<section id="overview">')
    overview_end = html.index('</section>', overview_start) + len('</section>')

    # The body div starts at: <div class="bg-white px-8 py-7 space-y-5">
    body_open = '<div class="bg-white px-8 py-7 space-y-5">'
    body_open_pos = html.index(body_open, overview_start)

    # Body content is everything between the opening div and the closing </div></div></section>
    # The closing structure is two closing divs then the section close
    body_content_start = body_open_pos + len(body_open)

    # Find the last two closing divs before </section>
    # Pattern: content ... </div>\n  </div>\n</section>
    closing = '\n  </div>\n</section>'
    closing_pos = html.rindex(closing, body_open_pos, overview_end)

    old_body = html[body_content_start:closing_pos]
    old_len = len(old_body)

    new_body = "\n" + HOOK_BANNER + "\n"

    html = html[:body_content_start] + new_body + html[closing_pos:]

    TARGET.write_text(html, encoding="utf-8")
    print(f"✅  #overview body replaced  ({old_len:,} chars → {len(new_body):,} chars)")
    print(f"File size: {len(html):,} chars")


if __name__ == "__main__":
    main()
