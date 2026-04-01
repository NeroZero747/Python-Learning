#!/usr/bin/env python3
"""Rewrite #recap section for all track_03 mod_01 lessons."""

import re, pathlib

ROOT = pathlib.Path(r"c:\Users\nightwolf\Projects\Python-Learning\pages\track_03_data_engineering")
MOD01 = "mod_01_data_engineering_foundations"
PATTERN = re.compile(
    r'(<section id="recap">\s*<div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">\s*'
    r'<div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-\[#CB187D\]">.*?</div>\s*</div>\s*)'
    r'<div class="bg-white px-8 py-7 space-y-6">.*?</div>\s*'
    r'(</div>\s*</section>)',
    re.DOTALL
)


def card_html(num, icon, label, sentence):
    n = f"{num:02d}"
    return (
        f'  <!-- Card {n} -->\n'
        f'  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">\n'
        f'    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">\n'
        f'      <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{n}</span>\n'
        f'      <div class="relative flex items-start gap-3">\n'
        f'        <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">\n'
        f'          <span class="iconify text-sm" data-icon="{icon}"></span>\n'
        f'        </span>\n'
        f'        <div>\n'
        f'          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">{label}</p>\n'
        f'          <p class="text-[11px] text-gray-600 leading-snug">{sentence}</p>\n'
        f'        </div>\n'
        f'      </div>\n'
        f'    </div>\n'
        f'  </div>'
    )


BANNER = (
    '<div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">\n'
    '  <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">&#10003;</span>\n'
    '  <div class="relative flex items-center gap-4">\n'
    '    <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">\n'
    '      <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>\n'
    '    </span>\n'
    '    <div>\n'
    '      <p class="text-sm font-bold text-white">Lesson Complete!</p>\n'
    '      <p class="text-xs text-white/80 mt-0.5">You&#39;ve covered 4 key concepts. Ready for the knowledge check?</p>\n'
    '    </div>\n'
    '  </div>\n'
    '</div>'
)


def build_body(cards):
    """Build the recap body from 4 (icon, label, sentence) tuples."""
    card_blocks = "\n\n".join(card_html(i + 1, icon, label, sent) for i, (icon, label, sent) in enumerate(cards))
    grid = f'<div class="grid grid-cols-1 md:grid-cols-2 gap-4">\n\n{card_blocks}\n\n</div>'
    return f'<div class="bg-white px-8 py-7 space-y-6">\n\n{grid}\n\n{BANNER}\n\n</div>'


# ── Lesson data: (icon, label, sentence) per card ────────────────────────────

LESSONS = {

    f"{MOD01}/lesson01_what_is_data_engineering.html": [
        ("fa6-solid:gears", "Define data engineering",
         "You can explain how data engineers build and maintain automated data systems."),
        ("fa6-solid:arrows-split-up-and-left", "Distinguish related roles",
         "You can separate a data engineer's work from analyst and scientist roles."),
        ("fa6-solid:hammer", "Core responsibilities",
         "You know the daily tasks: build pipelines, ensure quality, manage infrastructure."),
        ("fa6-solid:link", "Why it matters",
         "Reliable pipelines let every downstream team trust the data they use."),
    ],

    f"{MOD01}/lesson02_etl_vs_elt.html": [
        ("fa6-solid:right-left", "Compare ETL and ELT",
         "You can describe when to transform before loading versus after loading."),
        ("fa6-solid:industry", "Traditional ETL pattern",
         "Extract, transform in memory, then load clean data into the target."),
        ("fa6-solid:cloud-arrow-up", "Modern ELT pattern",
         "Load raw data first, then transform it inside the cloud warehouse."),
        ("fa6-solid:scale-balanced", "Choose the right approach",
         "Pick ETL for sensitive data and ELT when warehouse compute is cheap."),
    ],

    f"{MOD01}/lesson03_handling_large_datasets.html": [
        ("fa6-solid:triangle-exclamation", "Recognise memory limits",
         "You can spot when a file is too large to load into memory at once."),
        ("fa6-solid:puzzle-piece", "Chunk-based reading",
         'Use <code class="font-mono">chunksize</code> in pandas to process a CSV batch by batch.'),
        ("fa6-solid:filter", "Selective column loading",
         'Pass <code class="font-mono">usecols</code> to read only the columns your pipeline needs.'),
        ("fa6-solid:microchip", "Downcast data types",
         'Shrink memory usage by converting columns to <code class="font-mono">int32</code> or <code class="font-mono">category</code>.'),
    ],

    f"{MOD01}/lesson05_parquet_efficient_storage.html": [
        ("fa6-solid:file-zipper", "What Parquet is",
         "A columnar file format that stores data smaller and reads it faster than CSV."),
        ("fa6-solid:database", "Columnar storage benefits",
         "Queries that touch a few columns skip all the others entirely."),
        ("fa6-solid:arrow-right-arrow-left", "Convert CSV to Parquet",
         'Call <code class="font-mono">df.to_parquet()</code> to save any DataFrame as a Parquet file.'),
        ("fa6-solid:magnifying-glass-chart", "Read Parquet efficiently",
         'Use the <code class="font-mono">columns</code> parameter to load only what you need.'),
    ],

    f"{MOD01}/lesson06_intro_to_polars_optional.html": [
        ("fa6-solid:bolt", "What Polars is",
         "A Rust-powered DataFrame library built for speed on modern hardware."),
        ("fa6-solid:gauge-high", "Why Polars is faster",
         "It uses lazy evaluation and multi-threading to avoid unnecessary work."),
        ("fa6-solid:laptop-code", "Basic Polars operations",
         'You can filter, select, and group data with <code class="font-mono">pl.col()</code> expressions.'),
        ("fa6-solid:code-compare", "Compare with pandas",
         "Polars syntax is similar to pandas but runs significantly faster on large data."),
    ],

    f"{MOD01}/lesson07_pipeline_design_concepts.html": [
        ("fa6-solid:diagram-project", "Pipeline stages",
         "Every pipeline flows through extract, transform, and load stages in order."),
        ("fa6-solid:cubes", "Modular design",
         "Separate each stage into its own function so you can test it alone."),
        ("fa6-solid:arrows-rotate", "Idempotent processing",
         "Re-running the same pipeline produces the same result without duplicating data."),
        ("fa6-solid:shield-halved", "Error handling patterns",
         'Wrap risky steps in <code class="font-mono">try/except</code> so failures do not crash the pipeline.'),
    ],
}


# ── Main ──────────────────────────────────────────────────────────────────────

ok = fail = 0
for rel, cards in LESSONS.items():
    path = ROOT / rel
    if not path.exists():
        print(f"\u274c NOT FOUND  {rel}")
        fail += 1
        continue
    text = path.read_text(encoding="utf-8")
    body = build_body(cards)
    new_text, n = PATTERN.subn(lambda m: m.group(1) + body + "\n" + m.group(2), text, count=1)
    if n == 0:
        print(f"\u274c NO MATCH   {rel}")
        fail += 1
        continue
    path.write_text(new_text, encoding="utf-8")
    print(f"\u2705 OK         {rel}")
    ok += 1

print(f"\n{ok}/{ok + fail} recap sections rewritten")
