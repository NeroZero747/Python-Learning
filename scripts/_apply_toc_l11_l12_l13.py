"""
Batch-update existing mod_04 lessons (L01–L10):
1. Add L11, L12, L13 entries to the TOC module-lessons sidebar
2. Update hero progress pill from /10 to /13
3. Update L10's next-lesson section to point to L11
4. Update L10's bottom nav to add a Next link to L11
"""
import re, pathlib

BASE = pathlib.Path(r"pages/mod_04_data_engineering")

FILES = [BASE / f"lesson{i:02d}_{suf}.html" for i, suf in [
    (1, "what_is_data_engineering"),
    (2, "etl_elt_pipeline_thinking"),
    (3, "working_with_large_datasets"),
    (4, "efficient_storage_parquet"),
    (5, "faster_dataframes_polars_duckdb"),
    (6, "nosql_when_tables_arent_enough"),
    (7, "api_data_integration"),
    (8, "data_quality_validation"),
    (9, "pipeline_automation_deployment"),
    (10, "performance_at_scale"),
]]

# New TOC entries to inject after the L10 link
NEW_TOC_ENTRIES = """
<a href="lesson11_distributed_processing_spark.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">
  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>
  <span class="truncate">11. Distributed Processing: Spark</span>
</a>
<a href="lesson12_data_warehouses_and_lakes.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">
  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>
  <span class="truncate">12. Data Warehouses &amp; Lakes</span>
</a>
<a href="lesson13_data_modeling_fundamentals.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">
  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>
  <span class="truncate">13. Data Modeling Fundamentals</span>
</a>"""

# ---------- L10-specific: replace "Module Complete" next-lesson with real next lesson ----------
L10_NEXT_LESSON_OLD_PATTERN = re.compile(
    r'<section id="next-lesson"[^>]*>.*?</section>',
    re.DOTALL
)

L10_NEXT_LESSON_NEW = """<section id="next-lesson" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:circle-arrow-right"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Next Lesson</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Preview of what comes next</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
          <span class="text-white font-bold text-lg">11</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module 4 · Lesson 11</p>
          <h3 class="text-base font-bold text-gray-800">Distributed Processing with Apache Spark</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:server"></span>
            </span>
            <div><p class="text-sm font-semibold text-gray-700">Cluster Architecture</p></div>
          </div>
          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:bolt"></span>
            </span>
            <div><p class="text-sm font-semibold text-gray-700">Lazy Evaluation</p></div>
          </div>
          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:table-columns"></span>
            </span>
            <div><p class="text-sm font-semibold text-gray-700">PySpark DataFrames</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""

# L10 bottom nav: replace the spacer div with a Next link
L10_BOTTOM_NAV_SPACER = '<div class="flex-1"></div>'
L10_BOTTOM_NAV_NEXT = """<a href="lesson11_distributed_processing_spark.html" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Distributed Processing: Spark</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>"""


def patch_file(path):
    if not path.exists():
        print(f"  ❌ NOT FOUND: {path}")
        return
    text = path.read_text(encoding="utf-8")
    original = text
    changes = []

    # --- 1. Add L11-L13 to TOC sidebar (only if not already there) ---
    if "lesson11_distributed_processing_spark.html" not in text:
        # Find the last L10 link in the TOC
        # Match the closing </a> tag that ends the L10 link
        l10_link_pattern = re.compile(
            r'(<a\s+href="lesson10_performance_at_scale\.html"[^>]*>.*?</a>)',
            re.DOTALL
        )
        m = l10_link_pattern.search(text)
        if m:
            insert_pos = m.end()
            text = text[:insert_pos] + NEW_TOC_ENTRIES + text[insert_pos:]
            changes.append("TOC: added L11-L13 entries")
        else:
            changes.append("⚠️  TOC: could not find L10 link to insert after")
    else:
        changes.append("TOC: L11 already present, skipped")

    # --- 2. Update hero progress pill from /10 to /13 ---
    # Pattern: <span class="font-bold opacity-50">/10</span>
    progress_re = re.compile(r'(<span[^>]*class="font-bold opacity-50[^"]*"[^>]*>)/10(</span>)')
    if progress_re.search(text):
        text = progress_re.sub(r'\g<1>/13\2', text)
        changes.append("Hero: updated progress /10 → /13")
    else:
        # Try alternate pattern
        alt_re = re.compile(r'(<span[^>]*opacity-50[^>]*>)/10(</span>)')
        if alt_re.search(text):
            text = alt_re.sub(r'\g<1>/13\2', text)
            changes.append("Hero: updated progress /10 → /13 (alt)")
        else:
            changes.append("Hero: /10 not found (may already be /13)")

    # --- 3. L10-specific: replace next-lesson section ---
    if "lesson10_" in str(path):
        if L10_NEXT_LESSON_OLD_PATTERN.search(text):
            text = L10_NEXT_LESSON_OLD_PATTERN.sub(L10_NEXT_LESSON_NEW, text)
            changes.append("Next-lesson: replaced Module Complete with L11 preview")

        # Replace spacer with Next link in bottom nav
        if L10_BOTTOM_NAV_SPACER in text:
            text = text.replace(L10_BOTTOM_NAV_SPACER, L10_BOTTOM_NAV_NEXT, 1)
            changes.append("Bottom nav: added Next → L11")

    if text != original:
        path.write_text(text, encoding="utf-8")
        status = "✅ PATCHED"
    else:
        status = "⚠️  NO CHANGES"

    print(f"  {status}: {path.name}  ({', '.join(changes)})")


if __name__ == "__main__":
    print("Updating mod_04 lessons L01–L10 with L11-L13 TOC entries + progress...\n")
    for f in FILES:
        patch_file(f)
    print("\nDone.")
