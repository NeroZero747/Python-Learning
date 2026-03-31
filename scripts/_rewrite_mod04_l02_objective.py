"""Rewrite the #objective section in lesson02_project_folder_structure.html."""

from pathlib import Path

TARGET = Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices"
    "/lesson02_project_folder_structure.html"
)

NEW_SECTION = """\
<section id="objective">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:bullseye"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Lesson Objective</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">The goal and expected outcome of this lesson</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">

        <!-- Card 1 — Why structure matters -->
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:folder-open"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Why structure matters</p>
            <p class="text-xs text-gray-500 mt-0.5">Organised projects let you find and update any piece of code without hunting through one enormous file.</p>
          </div>
        </div>

        <!-- Card 2 — Organising projects into folders -->
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:folder-tree"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Organising projects into folders</p>
            <p class="text-xs text-gray-500 mt-0.5">Putting scripts, data files, and settings into separate folders gives every type of file a predictable home.</p>
          </div>
        </div>

        <!-- Card 3 — Splitting scripts by purpose -->
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:file-code"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Splitting scripts by purpose</p>
            <p class="text-xs text-gray-500 mt-0.5">Keeping cleaning, calculation, and export code in separate files means fixing one step won&#39;t break the others.</p>
          </div>
        </div>

        <!-- Card 4 — A typical analytics layout -->
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:layer-group"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">A typical analytics layout</p>
            <p class="text-xs text-gray-500 mt-0.5">Learning one standard folder layout means you can start any new analytics project with a consistent structure.</p>
          </div>
        </div>

      </div>
      <div class="mt-5">
        <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">This lesson gives you a practical folder layout you can apply immediately to any Python project you build.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""


def main():
    html = TARGET.read_text(encoding="utf-8")

    open_tag = '<section id="objective">'
    close_tag = '</section>'

    start = html.index(open_tag)
    end = html.index(close_tag, start) + len(close_tag)

    old = html[start:end]
    html = html[:start] + NEW_SECTION + html[end:]

    TARGET.write_text(html, encoding="utf-8")
    print(f"✅  #objective replaced  ({len(old):,} chars → {len(NEW_SECTION):,} chars)")
    print(f"File size: {len(html):,} chars")


if __name__ == "__main__":
    main()
