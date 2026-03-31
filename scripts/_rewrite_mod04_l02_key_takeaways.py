"""Rewrite the #key-ideas section body in lesson02_project_folder_structure.html.

Also patches the CSS: adds missing border-color: #CB187D to .obj-card-kt:hover.

Overview topics already covered (no repetition allowed):
  - Why structure matters (high-level, filing cabinet analogy)
  - Organizing projects into named subfolders (labeled drawers concept)
  - One script, one job (concept only, briefly)
  - The standard analytics project layout (concept only, briefly)

Three takeaways (new ground):
  1. Pink  — Version chaos: the concrete cost of no structure
  2. Violet — Isolation benefit: fixing one script never breaks another
  3. Blue   — Collaboration: a standard layout lets colleagues navigate instantly
"""

from pathlib import Path

TARGET = Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices"
    "/lesson02_project_folder_structure.html"
)

# ── New body ──────────────────────────────────────────────────────────────────
NEW_BODY = """\
<div class="bg-white px-8 py-7 space-y-4">

<div class="obj-card obj-card-kt rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:triangle-exclamation"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Version Chaos Costs Real Time</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">Without a folder structure, you end up with files named <code>report_v3_FINAL_final.py</code> — and you spend 10 minutes hunting for the right version instead of running your analysis.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Version creep</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">File naming</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Maintainability</span>
    </div>
  </div>
</div>

<div class="obj-card obj-card-violet rounded-2xl border border-violet-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:scissors"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Fix One File, Break Nothing</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">When your data-cleaning logic lives in its own script, you can correct a bug there without touching the export or calculation scripts — the same way fixing one Excel formula never changes the rest of the sheet.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Isolation</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Safe edits</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Single responsibility</span>
    </div>
  </div>
</div>

<div class="obj-card obj-card-blue rounded-2xl border border-blue-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:users"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Structure Lets Others Navigate Fast</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">A new colleague can locate your raw data, your cleaning script, and your config file in under a minute when your project follows a standard folder layout — no tour guide needed.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Collaboration</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Onboarding</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Readability</span>
    </div>
  </div>
</div>

</div>"""

# ── CSS fix ───────────────────────────────────────────────────────────────────
OLD_KT_CSS = ".obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }"
NEW_KT_CSS = ".obj-card-kt:hover { box-shadow: none; background-color: #ffffff; border-color: #CB187D; }"


def main():
    html = TARGET.read_text(encoding="utf-8")

    # 1. Fix CSS
    if OLD_KT_CSS in html:
        html = html.replace(OLD_KT_CSS, NEW_KT_CSS, 1)
        print("✅  CSS: added border-color: #CB187D to .obj-card-kt:hover")
    elif NEW_KT_CSS in html:
        print("⚠️   CSS: obj-card-kt:hover already has border-color — skipping")
    else:
        print("❌  CSS: obj-card-kt:hover rule not found in expected form")

    # 2. Replace #key-ideas body
    ki_start = html.index('<section id="key-ideas">')
    ki_end   = html.index("</section>", ki_start) + len("</section>")

    body_open = '<div class="bg-white px-8 py-7 space-y-4">'
    body_open_pos = html.index(body_open, ki_start)

    # Find the closing </div> pair before </section>
    # Structure: ...content...</div>\n  </div>\n</section>
    closing = "\n  </div>\n</section>"
    closing_pos = html.rindex(closing, body_open_pos, ki_end)

    old_body = html[body_open_pos : closing_pos]
    old_len = len(old_body)

    html = html[:body_open_pos] + NEW_BODY + html[closing_pos:]

    TARGET.write_text(html, encoding="utf-8")
    print(f"✅  #key-ideas body replaced  ({old_len:,} chars → {len(NEW_BODY):,} chars)")
    print(f"File size: {len(html):,} chars")


if __name__ == "__main__":
    main()
