#!/usr/bin/env python3
"""
Reorder mod_04_data_engineering lessons for better pedagogical flow.

New order:
  01 What Is Data Engineering?         (was 01)
  02 ETL, ELT & Pipeline Thinking      (was 02)
  03 Data Modeling Fundamentals         (was 13)
  04 Working with Large Datasets        (was 03)
  05 Efficient Storage: Parquet         (was 04)
  06 Data Quality & Validation          (was 08)
  07 API Data Integration               (was 07)
  08 NoSQL: When Tables Aren't Enough   (was 06)
  09 Data Warehouses & Data Lakes       (was 12)
  10 Faster DataFrames: Polars & DuckDB (was 05)
  11 Performance at Scale               (was 10)
  12 Distributed Processing: Spark      (was 11)
  13 Pipeline Automation & Deployment   (was 09)

Changes per file:
  - Hero lesson number (Lesson NN)
  - Progress pill (N/13)
  - TOC module lessons list (full rebuild, normalised)
  - Section-TOC #next-lesson link (add / remove as needed)
  - Next-lesson preview section (transplanted from correct source)
  - Bottom nav (Previous / All Lessons / Next — rebuilt)
  - Recap banner (Module Complete on L13 only)
  - Hub path normalised to ../hub_home_page.html
  - Module 3 → Module 4 label fix
  - &middot; → literal · normalisation
"""

import os, re, sys

DIR = "pages/mod_04_data_engineering"

# ── LESSON ORDER ──────────────────────────────────────────────
# (new_num, old_num, slug, nav_title, toc_title)
LESSONS = [
    (1,  1,  "what_is_data_engineering",        "What Is Data Engineering?",          "What Is Data Engineering?"),
    (2,  2,  "etl_elt_pipeline_thinking",        "ETL, ELT &amp; Pipeline Thinking",  "ETL, ELT &amp; Pipeline Thinking"),
    (3,  13, "data_modeling_fundamentals",        "Data Modeling Fundamentals",         "Data Modeling Fundamentals"),
    (4,  3,  "working_with_large_datasets",       "Working with Large Datasets",        "Working with Large Datasets"),
    (5,  4,  "efficient_storage_parquet",          "Efficient Storage: Parquet",         "Efficient Storage: Parquet"),
    (6,  8,  "data_quality_validation",            "Data Quality &amp; Validation",     "Data Quality &amp; Validation"),
    (7,  7,  "api_data_integration",               "API Data Integration",               "API Data Integration"),
    (8,  6,  "nosql_when_tables_arent_enough",     "NoSQL Databases",                    "NoSQL Databases"),
    (9,  12, "data_warehouses_and_lakes",           "Data Warehouses &amp; Data Lakes",  "Data Warehouses &amp; Lakes"),
    (10, 5,  "faster_dataframes_polars_duckdb",    "Polars &amp; DuckDB",               "Polars &amp; DuckDB"),
    (11, 10, "performance_at_scale",                "Performance at Scale",               "Performance at Scale"),
    (12, 11, "distributed_processing_spark",        "Distributed Processing: Spark",      "Distributed Processing: Spark"),
    (13, 9,  "pipeline_automation_deployment",      "Automation &amp; Deployment",        "Automation &amp; Deployment"),
]

TOTAL = len(LESSONS)

# Helpers
NEW_BY_NEW = {}   # new_num → (old_num, slug, nav_title, toc_title)
for n, o, s, nav, toc in LESSONS:
    NEW_BY_NEW[n] = (o, s, nav, toc)

def fname(num, slug):
    return f"lesson{num:02d}_{slug}.html"

# Next-lesson section source mapping:
# new_file_num → old_file_num whose next-lesson section to transplant
NEXT_SRC = {
    1:  1,   2:  12,  3:  2,   4:  3,   5:  7,
    6:  6,   7:  5,   8:  11,  9:  4,   10: 9,
    11: 10,  12: 8,
    # 13 = last lesson, no next
}


# ═══════════════════════════════════════════════════════════════
# STEP 1: Read all files
# ═══════════════════════════════════════════════════════════════
print("Step 1: Reading all files...")
old_contents = {}
for new, old, slug, nav, toc in LESSONS:
    path = os.path.join(DIR, fname(old, slug))
    if not os.path.exists(path):
        print(f"  ❌ NOT FOUND: {fname(old, slug)}")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        old_contents[old] = f.read()
    print(f"  ✅ {fname(old, slug)}  ({len(old_contents[old]):,} chars)")


# ═══════════════════════════════════════════════════════════════
# STEP 2: Extract next-lesson sections
# ═══════════════════════════════════════════════════════════════
print("\nStep 2: Extracting next-lesson sections...")
next_sections = {}
for old_num, content in old_contents.items():
    m = re.search(r"<section id=\"next-lesson\"[\s\S]*?</section>", content)
    next_sections[old_num] = m.group(0) if m else None
    print(f"  L{old_num:02d}: {'✅ found' if m else '— none (ok for last lesson)'}")


# ═══════════════════════════════════════════════════════════════
# Helper functions
# ═══════════════════════════════════════════════════════════════

def build_module_links(active_num, indent="              "):
    """Generate the <a> tags for the module lessons list."""
    lines = []
    for n, o, s, nav, toc in LESSONS:
        fn = fname(n, s)
        if n == active_num:
            lines.append(
                f'{indent}<a href="{fn}" class="mod-lesson-active flex items-center gap-2 px-3 py-2 rounded-lg border border-[#CB187D] bg-[#fdf0f7] text-[#CB187D] text-xs font-medium no-underline transition-colors">'
                f'\n{indent}  <span class="lesson-dot w-2 h-2 rounded-full bg-[#CB187D] shrink-0"></span>'
                f'\n{indent}  <span class="truncate">{n}. {toc}</span>'
                f'\n{indent}</a>'
            )
        else:
            lines.append(
                f'{indent}<a href="{fn}" class="flex items-center gap-2 px-3 py-2 rounded-lg border border-gray-100 bg-white text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">'
                f'\n{indent}  <span class="lesson-dot w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>'
                f'\n{indent}  <span class="truncate">{n}. {toc}</span>'
                f'\n{indent}</a>'
            )
    return "\n".join(lines)


def replace_module_list(content, active_num):
    """Replace the entire toc-module-list div."""
    start = content.find('<div class="toc-module-list')
    if start == -1:
        return content, False

    # Find matching closing </div> by counting nesting
    depth = 0
    i = start
    end = -1
    while i < len(content):
        if content[i : i + 4] == "<div":
            depth += 1
            i += 4
        elif content[i : i + 6] == "</div>":
            depth -= 1
            if depth == 0:
                end = i + 6
                break
            i += 6
        else:
            i += 1
    if end == -1:
        return content, False

    # Detect indentation of the toc-module-list div
    line_start = content.rfind("\n", 0, start) + 1
    base = ""
    for ch in content[line_start:start]:
        if ch in " \t":
            base += ch
        else:
            break

    links = build_module_links(active_num, indent=base + "      ")
    replacement = (
        f'{base}<div class="toc-module-list px-3 py-3">\n'
        f'{base}  <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-2 px-1">Module Lessons</p>\n'
        f'{base}  <div class="space-y-1">\n'
        f"{links}\n"
        f"{base}  </div>\n"
        f"{base}</div>"
    )
    return content[:start] + replacement + content[end:], True


def build_bottom_nav(new_num):
    """Generate bottom nav section HTML."""
    parts = []
    parts.append('<section>')
    parts.append('  <div class="flex flex-col sm:flex-row gap-3">')

    if new_num > 1:
        po, ps, pn, pt = NEW_BY_NEW[new_num - 1]
        pf = fname(new_num - 1, ps)
        parts.append(f'    <a href="{pf}" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">')
        parts.append('      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>')
        parts.append('      <div class="min-w-0">')
        parts.append('        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>')
        parts.append(f'        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{pn}</p>')
        parts.append('      </div>')
        parts.append('    </a>')
    else:
        parts.append('    <div class="flex-1"></div>')

    parts.append('    <a href="../hub_home_page.html" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">')
    parts.append('      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>')
    parts.append('      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>')
    parts.append('    </a>')

    if new_num < TOTAL:
        no, ns, nn, nt = NEW_BY_NEW[new_num + 1]
        nf = fname(new_num + 1, ns)
        parts.append(f'    <a href="{nf}" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">')
        parts.append('      <div class="min-w-0">')
        parts.append('        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>')
        parts.append(f'        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{nn}</p>')
        parts.append('      </div>')
        parts.append('      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>')
        parts.append('    </a>')
    else:
        parts.append('    <div class="flex-1"></div>')

    parts.append('  </div>')
    parts.append('</section>')
    return "\n".join(parts)


def replace_bottom_nav(content, new_nav):
    """Replace bottom nav section (bare <section> with lesson-nav-link)."""
    m = re.search(
        r"<section>\s*<div class=\"flex flex-col sm:flex-row gap-3\">[\s\S]*?</section>",
        content,
    )
    if not m:
        return content, False
    return content[: m.start()] + new_nav + content[m.end() :], True


def update_next_section_nums(section_html, new_next_num):
    """Update lesson number badge and Module label in a next-lesson section."""
    # Number badge
    section_html = re.sub(
        r'(<span class="text-white font-bold text-lg">)\d+(</span>)',
        rf"\g<1>{new_next_num}\g<2>",
        section_html,
    )
    # "Module 4 · Lesson N" label (handles · and &middot;)
    section_html = re.sub(
        r"(Module\s+\d+\s*(?:·|&middot;)\s*Lesson\s*)\d+",
        rf"\g<1>{new_next_num}",
        section_html,
    )
    return section_html


NEXT_TOC_LINK = '<a href="#next-lesson" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline"><span class="iconify text-brand shrink-0" data-icon="fa6-solid:circle-arrow-right"></span> Next Lesson</a>'


# ═══════════════════════════════════════════════════════════════
# STEP 3: Process each file
# ═══════════════════════════════════════════════════════════════
print("\nStep 3: Processing files...")
new_contents = {}

for new_num, old_num, slug, nav_title, toc_title in LESSONS:
    content = old_contents[old_num]
    changes = []

    # ── 3a. Hero lesson number ────────────────────────────────
    content = re.sub(r">Lesson \d+</p>", f">Lesson {new_num:02d}</p>", content)
    changes.append("hero#")

    # ── 3b. Progress pill ─────────────────────────────────────
    content = re.sub(
        r'(<span class="font-extrabold">)\d+(<span)',
        rf"\g<1>{new_num}\g<2>",
        content,
    )
    changes.append("pill")

    # ── 3c. Module lessons list ───────────────────────────────
    content, ok = replace_module_list(content, new_num)
    changes.append("TOC" if ok else "⚠ TOC")

    # ── 3d. Hub path ──────────────────────────────────────────
    content = content.replace("../../../hub_home_page.html", "../hub_home_page.html")
    content = content.replace("../../hub_home_page.html", "../hub_home_page.html")

    # ── 3e. Module 3 → Module 4 ──────────────────────────────
    content = re.sub(r"Module 3\s*·\s*Lesson", "Module 4 · Lesson", content)
    content = re.sub(r"Module 3\s*&middot;\s*Lesson", "Module 4 · Lesson", content)

    # ── 3f. Normalise &middot; ────────────────────────────────
    content = content.replace("&middot;", "·")

    # ── 3g. Next-lesson section ───────────────────────────────
    if new_num < TOTAL:
        # This file needs a next-lesson preview
        src_old = NEXT_SRC[new_num]
        src_section = next_sections.get(src_old)

        if src_section:
            next_new = new_num + 1
            patched = update_next_section_nums(src_section, next_new)
            patched = patched.replace("../../../hub_home_page.html", "../hub_home_page.html")
            patched = patched.replace("../../hub_home_page.html", "../hub_home_page.html")
            patched = patched.replace("&middot;", "·")
            patched = re.sub(r"Module 3\s*(?:·|&middot;)\s*Lesson", "Module 4 · Lesson", patched)

            has_next = bool(re.search(r'<section id="next-lesson"', content))
            if has_next:
                content = re.sub(
                    r'<section id="next-lesson"[\s\S]*?</section>',
                    patched,
                    content,
                )
                changes.append(f"next←L{src_old:02d}")
            else:
                # Insert before bottom nav
                nav_m = re.search(
                    r"<section>\s*<div class=\"flex flex-col sm:flex-row gap-3\">",
                    content,
                )
                if nav_m:
                    content = content[: nav_m.start()] + patched + "\n\n" + content[nav_m.start() :]
                    changes.append(f"next+←L{src_old:02d}")
                else:
                    changes.append("⚠ no nav anchor")

            # Ensure #next-lesson TOC link exists
            if '<a href="#next-lesson"' not in content:
                # Insert before </nav> in the section-level TOC
                nav_close_idx = content.find("</nav>")
                if nav_close_idx > 0:
                    content = (
                        content[:nav_close_idx]
                        + "          " + NEXT_TOC_LINK + "\n"
                        + content[nav_close_idx:]
                    )
                    changes.append("TOC#next+")
        else:
            changes.append(f"⚠ no src L{src_old:02d}")
    else:
        # Last lesson — remove next-lesson section
        had = bool(re.search(r'<section id="next-lesson"', content))
        if had:
            content = re.sub(
                r"\n*<section id=\"next-lesson\"[\s\S]*?</section>\n*",
                "\n\n",
                content,
            )
            changes.append("next−")

        # Remove #next-lesson TOC link
        content = re.sub(
            r"\s*<a href=\"#next-lesson\"[^>]*>[\s\S]*?</a>\s*",
            "\n",
            content,
        )
        changes.append("TOC#next−")

    # ── 3h. Bottom nav ────────────────────────────────────────
    nav_html = build_bottom_nav(new_num)
    content, ok = replace_bottom_nav(content, nav_html)
    changes.append("nav" if ok else "⚠ nav")

    # ── 3i. Recap banner ──────────────────────────────────────
    if new_num == TOTAL:
        # Last lesson → Module Complete!
        if "Lesson Complete!" in content:
            content = content.replace("Lesson Complete!", "Module Complete!")
            content = re.sub(
                r"You(?:'|&#39;)ve covered \d+ key concepts\. Ready for the knowledge check\?",
                "You've finished all 13 lessons in the Data Engineering module. Congratulations!",
                content,
            )
            changes.append("recap→ModComplete")
    else:
        # Non-last lesson → Lesson Complete!
        if "Module Complete!" in content:
            content = content.replace("Module Complete!", "Lesson Complete!")
            content = re.sub(
                r"You've finished all \d+ lessons in the Data Engineering module\. Congratulations!",
                "You've covered 4 key concepts. Ready for the knowledge check?",
                content,
            )
            changes.append("recap→LsnComplete")

    new_contents[new_num] = content
    print(f"  L{new_num:02d} (was L{old_num:02d}): {', '.join(changes)}")


# ═══════════════════════════════════════════════════════════════
# STEP 4: Write files & clean up
# ═══════════════════════════════════════════════════════════════
print("\nStep 4: Writing files...")

old_fnames = set()
new_fnames = set()
for n, o, s, nav, toc in LESSONS:
    old_fnames.add(fname(o, s))
    new_fnames.add(fname(n, s))

# Write all new files
for n, o, s, nav, toc in LESSONS:
    path = os.path.join(DIR, fname(n, s))
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_contents[n])
    print(f"  ✅ {fname(n, s)}")

# Delete stale old files (old names that don't match any new name)
stale = old_fnames - new_fnames
for sf in sorted(stale):
    sp = os.path.join(DIR, sf)
    if os.path.exists(sp):
        os.remove(sp)
        print(f"  🗑  Deleted stale: {sf}")


# ═══════════════════════════════════════════════════════════════
# STEP 5: Validate
# ═══════════════════════════════════════════════════════════════
print("\nStep 5: Validating...")
all_ok = True
for n, o, s, nav, toc in LESSONS:
    path = os.path.join(DIR, fname(n, s))
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    errors = []
    for tag in ["div", "section", "table", "pre", "code"]:
        opens = len(re.findall(rf"<{tag}[\s>]", html))
        closes = len(re.findall(rf"</{tag}>", html))
        if opens != closes:
            errors.append(f"{tag}={opens}/{closes}")

    # Check hero number
    if f">Lesson {n:02d}</p>" not in html:
        errors.append(f"hero says wrong number")

    # Check progress pill
    if f'>{n}<span class="font-bold opacity-50">/13</span>' not in html:
        errors.append("progress pill wrong")

    # Check mod-lesson-active points to self
    expected_fn = fname(n, s)
    if f'href="{expected_fn}" class="mod-lesson-active' not in html:
        errors.append("mod-lesson-active wrong")

    # Check hub path
    if "../../hub_home_page.html" in html or "../../../hub_home_page.html" in html:
        errors.append("hub path not normalised")

    # Check Module 3 remnants
    if re.search(r"Module 3\s*[·]", html):
        errors.append("Module 3 remnant")

    status = "✅" if not errors else "❌"
    if errors:
        all_ok = False
    print(f"  {status} L{n:02d} {fname(n, s)}" + (f"  [{', '.join(errors)}]" if errors else ""))

if all_ok:
    print("\n✅ All 13 lessons validated successfully!")
else:
    print("\n⚠️  Some issues found — review above.")
