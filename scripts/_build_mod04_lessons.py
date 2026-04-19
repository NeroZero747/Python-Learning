#!/usr/bin/env python3
"""
Build all 9 remaining lesson HTML files for mod_04_data_engineering.
Reads the CSS/JS framework from lesson01 and generates each lesson's
unique content sections from the markdown source material.
"""
import os, html as html_mod

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(BASE, "pages", "mod_04_data_engineering")

# ── Lesson metadata ──────────────────────────────────────────────────
LESSONS = [
    # (num, filename_slug, title, subtitle, difficulty_dots, duration, date)
    (2, "lesson02_etl_elt_pipeline_thinking",
     "ETL, ELT &amp; Pipeline Thinking",
     "Understand the two dominant pipeline architectures and learn to write modular, idempotent data pipelines.",
     1, "12 min", "March 31, 2026"),
    (3, "lesson03_working_with_large_datasets",
     "Working with Large Datasets",
     "Process files larger than RAM using chunked reading, dtype optimization, and vectorized operations.",
     2, "12 min", "March 31, 2026"),
    (4, "lesson04_efficient_storage_parquet",
     "Efficient Storage: Parquet &amp; Columnar Formats",
     "Learn why Parquet is the standard for analytics and how to read, write, and partition columnar files.",
     1, "10 min", "March 31, 2026"),
    (5, "lesson05_faster_dataframes_polars_duckdb",
     "Faster DataFrames: Polars &amp; DuckDB",
     "Add two faster alternatives to pandas for processing millions of rows on your laptop.",
     2, "12 min", "March 31, 2026"),
    (6, "lesson06_nosql_when_tables_arent_enough",
     "NoSQL: When Tables Aren&rsquo;t Enough",
     "Discover document, key-value, column-family, and graph databases and know when each fits.",
     1, "12 min", "March 31, 2026"),
    (7, "lesson07_api_data_integration",
     "API Data Integration with Python",
     "Build resilient API collection scripts with authentication, pagination, rate-limit handling, and DataFrame loading.",
     2, "14 min", "March 31, 2026"),
    (8, "lesson08_data_quality_validation",
     "Data Quality &amp; Validation",
     "Write validation layers that catch bad data before it reaches dashboards — quarantine, don&rsquo;t crash.",
     2, "12 min", "March 31, 2026"),
    (9, "lesson09_pipeline_automation_deployment",
     "Pipeline Automation &amp; Deployment",
     "Schedule pipelines with cron, deploy through CI/CD, and add monitoring so failures wake you up.",
     3, "14 min", "March 31, 2026"),
    (10, "lesson10_performance_at_scale",
     "Performance at Scale",
     "Profile bottlenecks, parallelize file processing, and apply the performance best-practices checklist.",
     2, "12 min", "March 31, 2026"),
]

# Module sidebar lesson list (all 10)
ALL_LESSONS_SIDEBAR = [
    ("lesson01_what_is_data_engineering.html", "1. What Is Data Engineering?"),
    ("lesson02_etl_elt_pipeline_thinking.html", "2. ETL, ELT &amp; Pipeline Thinking"),
    ("lesson03_working_with_large_datasets.html", "3. Working with Large Datasets"),
    ("lesson04_efficient_storage_parquet.html", "4. Efficient Storage: Parquet"),
    ("lesson05_faster_dataframes_polars_duckdb.html", "5. Polars &amp; DuckDB"),
    ("lesson06_nosql_when_tables_arent_enough.html", "6. NoSQL Databases"),
    ("lesson07_api_data_integration.html", "7. API Data Integration"),
    ("lesson08_data_quality_validation.html", "8. Data Quality &amp; Validation"),
    ("lesson09_pipeline_automation_deployment.html", "9. Automation &amp; Deployment"),
    ("lesson10_performance_at_scale.html", "10. Performance at Scale"),
]

# Next lesson titles for bottom nav
NEXT_LESSON_PREVIEW = {
    2: {"num": 3, "file": "lesson03_working_with_large_datasets.html",
        "title": "Working with Large Datasets", "mod_label": "Module 1 &middot; Lesson 3",
        "items": [
            ("fa6-solid:memory", "Chunk Processing"),
            ("fa6-solid:compress", "Dtype Optimization"),
            ("fa6-solid:gauge-high", "Vectorized Operations"),
        ]},
    3: {"num": 4, "file": "lesson04_efficient_storage_parquet.html",
        "title": "Efficient Storage: Parquet", "mod_label": "Module 1 &middot; Lesson 4",
        "items": [
            ("fa6-solid:table-columns", "Columnar Storage"),
            ("fa6-solid:file-zipper", "Parquet Compression"),
            ("fa6-solid:filter", "Predicate Pushdown"),
        ]},
    4: {"num": 5, "file": "lesson05_faster_dataframes_polars_duckdb.html",
        "title": "Faster DataFrames: Polars &amp; DuckDB", "mod_label": "Module 2 &middot; Lesson 5",
        "items": [
            ("fa6-solid:bolt", "Polars Lazy Evaluation"),
            ("fa6-solid:database", "DuckDB SQL on Files"),
            ("fa6-solid:scale-balanced", "Choosing the Right Tool"),
        ]},
    5: {"num": 6, "file": "lesson06_nosql_when_tables_arent_enough.html",
        "title": "NoSQL: When Tables Aren&rsquo;t Enough", "mod_label": "Module 2 &middot; Lesson 6",
        "items": [
            ("fa6-solid:file-code", "Document Databases"),
            ("fa6-solid:key", "Key-Value Stores"),
            ("fa6-solid:diagram-project", "SQL vs NoSQL Decision"),
        ]},
    6: {"num": 7, "file": "lesson07_api_data_integration.html",
        "title": "API Data Integration", "mod_label": "Module 3 &middot; Lesson 7",
        "items": [
            ("fa6-solid:plug", "REST API Requests"),
            ("fa6-solid:lock", "API Authentication"),
            ("fa6-solid:rotate", "Pagination &amp; Rate Limits"),
        ]},
    7: {"num": 8, "file": "lesson08_data_quality_validation.html",
        "title": "Data Quality &amp; Validation", "mod_label": "Module 3 &middot; Lesson 8",
        "items": [
            ("fa6-solid:shield-halved", "Quality Dimensions"),
            ("fa6-solid:flask", "Validation Assertions"),
            ("fa6-solid:box-archive", "Quarantine Pattern"),
        ]},
    8: {"num": 9, "file": "lesson09_pipeline_automation_deployment.html",
        "title": "Pipeline Automation &amp; Deployment", "mod_label": "Module 4 &middot; Lesson 9",
        "items": [
            ("fa6-solid:clock", "Cron Scheduling"),
            ("fa6-solid:code-branch", "CI/CD Pipelines"),
            ("fa6-solid:chart-line", "Monitoring &amp; Alerts"),
        ]},
    9: {"num": 10, "file": "lesson10_performance_at_scale.html",
        "title": "Performance at Scale", "mod_label": "Module 4 &middot; Lesson 10",
        "items": [
            ("fa6-solid:stopwatch", "Pipeline Profiling"),
            ("fa6-solid:microchip", "Parallel Processing"),
            ("fa6-solid:list-check", "Best Practices Checklist"),
        ]},
    10: None,  # last lesson
}

PREV_LESSON = {
    2: ("lesson01_what_is_data_engineering.html", "What Is Data Engineering?"),
    3: ("lesson02_etl_elt_pipeline_thinking.html", "ETL, ELT &amp; Pipeline Thinking"),
    4: ("lesson03_working_with_large_datasets.html", "Working with Large Datasets"),
    5: ("lesson04_efficient_storage_parquet.html", "Efficient Storage: Parquet"),
    6: ("lesson05_faster_dataframes_polars_duckdb.html", "Polars &amp; DuckDB"),
    7: ("lesson06_nosql_when_tables_arent_enough.html", "NoSQL Databases"),
    8: ("lesson07_api_data_integration.html", "API Data Integration"),
    9: ("lesson08_data_quality_validation.html", "Data Quality &amp; Validation"),
    10: ("lesson09_pipeline_automation_deployment.html", "Automation &amp; Deployment"),
}


def e(text):
    """HTML-escape text for safe embedding."""
    return html_mod.escape(text, quote=True)


def skill_dots_html(active_count):
    """Return 3 skill dots with active_count lit green."""
    out = []
    for i in range(3):
        if i < active_count:
            out.append('<span style="width:6px;height:6px;border-radius:50%;background:#22c55e;display:inline-block;"></span>')
        else:
            out.append('<span style="width:6px;height:6px;border-radius:50%;background:#d1d5db;display:inline-block;"></span>')
    return "\n              ".join(out)


def difficulty_label(dots):
    if dots == 1: return "Beginner"
    if dots == 2: return "Intermediate"
    return "Advanced"


def sidebar_html(active_num):
    """Build the module lessons sidebar list."""
    items = []
    for fname, label in ALL_LESSONS_SIDEBAR:
        num = int(fname.split("lesson")[1][:2])
        if num == active_num:
            items.append(f'''<a href="{fname}" class="mod-lesson-active flex items-center gap-2 px-3 py-2 rounded-lg border bg-[#fdf0f7] border-[#CB187D] text-[#CB187D] text-xs font-medium no-underline transition-colors">
  <span class="lesson-dot w-2 h-2 rounded-full bg-[#CB187D] shrink-0"></span>
  <span class="truncate">{label}</span>
</a>''')
        else:
            items.append(f'''<a href="{fname}" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">
  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>
  <span class="truncate">{label}</span>
</a>''')
    return "\n".join(items)


def bottom_nav_html(lesson_num):
    """Build the Previous / All Lessons / Next bottom nav."""
    prev = PREV_LESSON.get(lesson_num)
    nxt_data = NEXT_LESSON_PREVIEW.get(lesson_num)

    prev_block = ""
    if prev:
        prev_block = f'''<a href="{prev[0]}" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{prev[1]}</p>
      </div>
    </a>'''
    else:
        prev_block = '<div class="flex-1"></div>'

    hub_link = '''<a href="../../hub_home_page.html" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>'''

    next_block = ""
    if nxt_data:
        next_block = f'''<a href="{nxt_data['file']}" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{nxt_data['title']}</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>'''

    return f"""<section>
  <div class="flex flex-col sm:flex-row gap-3">
    {prev_block}
    {hub_link}
    {next_block}
  </div>
</section>"""


def next_lesson_section(lesson_num):
    """Build the #next-lesson section."""
    nxt = NEXT_LESSON_PREVIEW.get(lesson_num)
    if not nxt:
        # Last lesson — no next lesson section
        return ""
    items_html = ""
    for icon, label in nxt["items"]:
        items_html += f'''
          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="{icon}"></span>
            </span>
            <div><p class="text-sm font-semibold text-gray-700">{label}</p></div>
          </div>'''

    return f'''<section id="next-lesson" class="scroll-mt-24">
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
          <span class="text-white font-bold text-lg">{nxt['num']}</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">{nxt['mod_label']}</p>
          <h3 class="text-base font-bold text-gray-800">{nxt['title']}</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">{items_html}
        </div>
      </div>
    </div>
  </div>
</section>'''


# ══════════════════════════════════════════════════════════════════════
# Per-lesson section content generators
# ══════════════════════════════════════════════════════════════════════

def _code_block_a(filename, code, lang="python", terminal_output=None):
    """Style A — dark-chrome code block for code-examples section."""
    icon = 'logos:python' if lang == 'python' else 'fa6-solid:terminal'
    escaped = e(code)
    terminal = ""
    if terminal_output:
        terminal = f'''
  <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
    <div class="flex items-center gap-2 mb-1.5">
      <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
      <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
      <span class="text-[10px] text-gray-600 font-mono">$ python {filename}</span>
    </div>
    <div class="font-mono text-xs text-emerald-400 leading-relaxed whitespace-pre">{e(terminal_output)}</div>
  </div>'''
    return f'''<div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
  <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
    <div class="flex items-center gap-3">
      <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
        <span class="iconify text-yellow-400 text-xs" data-icon="{icon}" data-width="12" data-height="12"></span>
        <span class="text-[11px] font-semibold text-gray-400">{filename}</span>
      </div>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
  </div>
  <div class="bg-code">
    <pre class="overflow-x-auto pre-reset"><code class="language-{lang}">{escaped}</code></pre>
  </div>{terminal}
</div>'''


def _code_block_b(label, code, lang="python"):
    """Style B — simple-dark code block for key-concepts section."""
    icon = 'logos:python' if lang == 'python' else 'fa6-solid:terminal'
    return f'''<div class="rounded-xl overflow-hidden bg-code shadow-md">
  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
    <div class="flex items-center gap-2">
      <span class="iconify" data-icon="{icon}" data-width="14" data-height="14"></span>
      <span class="text-[11px] font-semibold text-gray-400">{label}</span>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
  </div>
  <pre class="overflow-x-auto pre-reset"><code class="language-{lang}">{e(code)}</code></pre>
</div>'''


def _code_block_b_lite(code, lang="python"):
    """Style B-lite — bare code for mistakes split panels."""
    return f'''<div class="rounded-xl overflow-hidden bg-code">
  <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-{lang}">{e(code)}</code></pre>
</div>'''


# ══════════════════════════════════════════════════════════════════════
# Lesson-specific content for lessons 02-10
# ══════════════════════════════════════════════════════════════════════

def get_lesson_content(num):
    """Return dict with keys: objective, overview, key_ideas, key_concepts,
    code_examples, comparison, practice, mistakes, real_world, recap, quiz
    Each value is raw HTML for that section's body (inside bg-white px-8 py-7)."""
    return LESSON_CONTENT[num]


# ── LESSON 02 ────────────────────────────────────────────────────────
L02_OBJECTIVE = '''<div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
  <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
    <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
      <span class="iconify text-brand text-lg" data-icon="fa6-solid:right-left"></span>
    </span>
    <div>
      <p class="text-sm font-semibold text-gray-800">Contrast ETL and ELT</p>
      <p class="text-xs text-gray-500 mt-0.5">Explain the difference and identify when each pattern is appropriate.</p>
    </div>
  </div>
  <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
    <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
      <span class="iconify text-brand text-lg" data-icon="fa6-solid:diagram-project"></span>
    </span>
    <div>
      <p class="text-sm font-semibold text-gray-800">Pipeline design principles</p>
      <p class="text-xs text-gray-500 mt-0.5">Describe what makes a pipeline reliable, idempotent, and debuggable.</p>
    </div>
  </div>
  <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
    <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
      <span class="iconify text-brand text-lg" data-icon="fa6-solid:code-branch"></span>
    </span>
    <div>
      <p class="text-sm font-semibold text-gray-800">Common patterns</p>
      <p class="text-xs text-gray-500 mt-0.5">Recognize batch vs streaming and fan-out/merge architectures.</p>
    </div>
  </div>
  <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
    <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
      <span class="iconify text-brand text-lg" data-icon="fa6-solid:cubes"></span>
    </span>
    <div>
      <p class="text-sm font-semibold text-gray-800">Write modular code</p>
      <p class="text-xs text-gray-500 mt-0.5">Structure an ETL pipeline as separate, testable functions.</p>
    </div>
  </div>
</div>
<div class="mt-5 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">This lesson introduces <strong>ETL and ELT</strong> so you can design a data pipeline on paper and explain your choices to a colleague.</p>
</div>'''

# Build full HTML file from template
# Read the CSS from lesson01 (lines 1 through the end of </style>)
def read_css_block():
    """Read the entire CSS + CDN block from lesson01."""
    p = os.path.join(OUT_DIR, "lesson01_what_is_data_engineering.html")
    with open(p, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # Find the end of </style>
    css_end = 0
    for i, line in enumerate(lines):
        if "</style>" in line:
            css_end = i + 1
            break
    return "".join(lines[:css_end])


def read_js_block():
    """Read the JS block from lesson01."""
    p = os.path.join(OUT_DIR, "lesson01_what_is_data_engineering.html")
    with open(p, "r", encoding="utf-8") as f:
        content = f.read()
    idx = content.rfind("<script>")
    return content[idx:]


# Read template blocks once
CSS_BLOCK = None
JS_BLOCK = None

def get_css():
    global CSS_BLOCK
    if CSS_BLOCK is None:
        CSS_BLOCK = read_css_block()
    return CSS_BLOCK

def get_js():
    global JS_BLOCK
    if JS_BLOCK is None:
        JS_BLOCK = read_js_block()
    return JS_BLOCK


# ── Hero section (same hex SVG for all) ──────────────────────────────
def hero_html(num, title, subtitle, diff_dots, duration, date):
    dots = skill_dots_html(diff_dots)
    diff_label = difficulty_label(diff_dots)
    return f'''<div class="max-w-[1280px] mx-auto px-4 pt-5 pb-0">
    <section class="hero-container">
  <div class="hero-dots"></div>
  <div class="hero-glow hero-glow-1"></div>
  <div class="hero-glow hero-glow-2"></div>
  <div class="hero-glow-line"></div>
  <div class="relative z-10 px-8 py-8 md:px-12 md:py-10">
    <div class="hero-split flex flex-col md:flex-row items-center gap-6 md:gap-10">
      <div class="flex-1 min-w-0">
        <div class="flex flex-wrap items-center gap-2 mb-4">
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="iconify text-[10px]" data-icon="fa6-solid:rocket"></span> Module 4
          </span>
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="inline-flex items-center gap-1">
              {dots}
            </span>
            {diff_label}
          </span>
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="iconify text-[10px]" data-icon="fa6-regular:clock"></span> {duration}
          </span>
        </div>
        <p class="text-xs font-bold uppercase tracking-[0.2em] text-white/90 mb-2">Lesson {num:02d}</p>
        <h1 class="text-3xl md:text-4xl font-extrabold text-white mb-3 leading-[1.15] tracking-tight">{title}</h1>
        <p class="text-white/80 text-sm md:text-base leading-relaxed mt-4 mb-5 max-w-prose">{subtitle}</p>
        <div class="flex items-center gap-4 mb-5 text-sm">
          <div class="flex items-center gap-2">
            <span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-white/15">
              <span class="iconify text-white text-[10px]" data-icon="fa6-solid:user"></span>
            </span>
            <span class="text-white/85 font-medium text-xs">Python Learning Hub</span>
          </div>
          <span class="text-white/30">|</span>
          <div class="flex items-center gap-2">
            <span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-white/15">
              <span class="iconify text-white text-[10px]" data-icon="fa6-regular:calendar"></span>
            </span>
            <span class="text-white/85 font-medium text-xs">{date}</span>
          </div>
        </div>
        <div class="flex items-center gap-2 flex-wrap">
          <a href="#objective" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline">
            <span class="iconify text-[10px]" data-icon="fa6-solid:bullseye" style="opacity:0.5;"></span>
            <span class="font-extrabold">4</span><span class="font-semibold opacity-55">Goals</span>
          </a>
          <a href="#code-examples" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline">
            <span class="iconify text-[10px]" data-icon="fa6-solid:code" style="opacity:0.5;"></span>
            <span class="font-extrabold">4</span><span class="font-semibold opacity-55">Examples</span>
          </a>
          <a href="#practice" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline">
            <span class="iconify text-[10px]" data-icon="fa6-solid:dumbbell" style="opacity:0.5;"></span>
            <span class="font-extrabold">3</span><span class="font-semibold opacity-55">Exercises</span>
          </a>
          <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs">
            <span class="iconify text-[10px]" data-icon="fa6-solid:layer-group" style="opacity:0.5;"></span>
            <span class="font-extrabold">{num}<span class="font-bold opacity-50">/10</span></span>
            <span class="font-semibold opacity-55">Progress</span>
          </span>
        </div>
      </div>
      <div class="w-full md:w-[300px] lg:w-[320px] shrink-0 self-center">
        <div class="hero-abstract-card" style="padding:0.25rem;opacity:0.75;">
          <svg viewBox="0 0 280 324" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-auto" style="max-height:320px;" aria-hidden="true">
            <defs>
              <linearGradient id="hexFill" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1a0a12"/><stop offset="45%" stop-color="#2d0a1e"/><stop offset="100%" stop-color="#0d0610"/></linearGradient>
              <linearGradient id="hexBorder" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#CB187D"/><stop offset="50%" stop-color="#e84aad"/><stop offset="100%" stop-color="#CB187D"/></linearGradient>
              <radialGradient id="hexGlow" cx="50%" cy="38%" r="45%"><stop offset="0%" stop-color="#CB187D" stop-opacity="0.18"/><stop offset="100%" stop-color="#CB187D" stop-opacity="0"/></radialGradient>
              <radialGradient id="pyGlow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#FFD43B" stop-opacity="0.12"/><stop offset="100%" stop-color="#FFD43B" stop-opacity="0"/></radialGradient>
              <clipPath id="hexClip"><polygon points="140,14 268,88 268,236 140,310 12,236 12,88"/></clipPath>
            </defs>
            <polygon points="140,14 268,88 268,236 140,310 12,236 12,88" fill="url(#hexFill)"/>
            <polygon points="140,14 268,88 268,236 140,310 12,236 12,88" fill="url(#hexGlow)"/>
            <g clip-path="url(#hexClip)" opacity="1">
              <g opacity="0.06"><circle cx="40" cy="100" r="1.2" fill="white"/><circle cx="60" cy="100" r="1.2" fill="white"/><circle cx="80" cy="100" r="1.2" fill="white"/><circle cx="100" cy="100" r="1.2" fill="white"/><circle cx="120" cy="100" r="1.2" fill="white"/><circle cx="160" cy="100" r="1.2" fill="white"/><circle cx="180" cy="100" r="1.2" fill="white"/><circle cx="200" cy="100" r="1.2" fill="white"/><circle cx="220" cy="100" r="1.2" fill="white"/><circle cx="240" cy="100" r="1.2" fill="white"/></g>
              <circle cx="140" cy="145" r="55" fill="url(#pyGlow)"/>
            </g>
            <polygon points="140,14 268,88 268,236 140,310 12,236 12,88" fill="none" stroke="url(#hexBorder)" stroke-width="4" stroke-linejoin="round"/>
            <polygon points="140,24 258,93 258,231 140,300 22,231 22,93" fill="none" stroke="#CB187D" stroke-width="0.8" stroke-linejoin="round" stroke-opacity="0.25"/>
            <foreignObject x="95" y="85" width="90" height="90"><div xmlns="http://www.w3.org/1999/xhtml" style="display:flex;align-items:center;justify-content:center;width:100%;height:100%;"><span class="iconify" data-icon="logos:python" style="font-size:70px;filter:drop-shadow(0 0 14px rgba(255,212,59,0.25));"></span></div></foreignObject>
            <text x="140" y="205" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-weight="800" font-size="30" letter-spacing="4" opacity="0.95">PYTHON</text>
            <text x="140" y="230" text-anchor="middle" fill="#f5c6e0" font-family="Inter,sans-serif" font-weight="600" font-size="14" letter-spacing="5" opacity="0.8">LEARNING HUB</text>
            <line x1="85" y1="185" x2="195" y2="185" stroke="#CB187D" stroke-width="1" stroke-opacity="0.35" stroke-linecap="round"/>
          </svg>
        </div>
      </div>
    </div>
  </div>
</section>
  </div>'''


# TOC sidebar links
TOC_LINKS = '''<a href="#objective" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">
  <span class="iconify text-brand shrink-0" data-icon="fa6-solid:bullseye"></span> Lesson Objective
</a>
<a href="#overview" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">
  <span class="iconify text-brand shrink-0" data-icon="fa6-solid:binoculars"></span> Overview
</a>
<a href="#key-ideas" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">
  <span class="iconify text-brand shrink-0" data-icon="fa6-solid:lightbulb"></span> Key Takeaways
</a>
<a href="#key-concepts" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">
  <span class="iconify text-brand shrink-0" data-icon="fa6-solid:book-open"></span> Key Concepts
</a>
<a href="#code-examples" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">
  <span class="iconify text-brand shrink-0" data-icon="fa6-solid:code"></span> Code Examples
</a>
<a href="#practice" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">
  <span class="iconify text-brand shrink-0" data-icon="fa6-solid:dumbbell"></span> Practice Exercises
</a>
<a href="#mistakes" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">
  <span class="iconify text-brand shrink-0" data-icon="fa6-solid:triangle-exclamation"></span> Common Mistakes
</a>
<a href="#recap" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">
  <span class="iconify text-brand shrink-0" data-icon="fa6-solid:list-check"></span> Lesson Recap
</a>
<a href="#knowledge-check" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">
  <span class="iconify text-brand shrink-0" data-icon="fa6-solid:brain"></span> Knowledge Check
</a>
<a href="#next-lesson" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline">
  <span class="iconify text-brand shrink-0" data-icon="fa6-solid:circle-arrow-right"></span> Next Lesson
</a>'''

# ══════════════════════════════════════════════════════════════════════
# SECTION BUILDERS — generic wrappers
# ══════════════════════════════════════════════════════════════════════

def section_wrap(section_id, icon, title, subtitle, body_html):
    return f'''<section id="{section_id}">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="{icon}"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">{title}</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">{subtitle}</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
{body_html}
    </div>
  </div>
</section>'''


def build_full_html(num, title, subtitle, diff_dots, duration, date, sections_html):
    """Assemble the complete lesson HTML file."""
    css = get_css()
    js = get_js()

    hero = hero_html(num, title, subtitle, diff_dots, duration, date)
    sb = sidebar_html(num)
    nxt_section = next_lesson_section(num)
    bot_nav = bottom_nav_html(num)

    return f'''{css}
<div class="scroll-progress" id="scroll-progress" style="width: 0%;"></div>
<button class="back-to-top" id="back-to-top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">
  <span class="iconify text-lg" data-icon="fa6-solid:arrow-up"></span>
</button>

<div id="hub-root" class="bg-gray-50 min-h-screen">

  <!-- HERO -->
  {hero}

  <!-- MAIN LAYOUT -->
  <div class="max-w-[1280px] mx-auto px-4 pt-8 pb-12">
    <div class="lesson-layout">
      <aside class="lesson-toc-sidebar">
        <div class="rounded-2xl border border-gray-100 shadow-sm overflow-hidden bg-white">
          <div class="toc-header relative flex items-center gap-2 px-4 py-3 border-b border-gray-100">
            <span class="toc-header-label text-xs font-bold uppercase tracking-widest text-brand">On This Page</span>
            <button class="toc-toggle-btn" onclick="toggleToc()" title="Toggle navigation">
              <span class="iconify text-sm" id="toc-toggle-icon" data-icon="fa6-solid:angles-left"></span>
            </button>
          </div>
          <nav class="toc-body px-2 py-2 border-b border-gray-100" aria-label="Page sections">
            {TOC_LINKS}
          </nav>
          <div class="toc-module-list px-3 py-3">
            <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-2 px-1">Module Lessons</p>
            <div class="space-y-1">
{sb}
            </div>
          </div>
        </div>
      </aside>

      <main class="min-w-0 flex-1 space-y-10">
{sections_html}

{nxt_section}

{bot_nav}

      </main>
    </div>
  </div>
</div>

{js}'''


# ══════════════════════════════════════════════════════════════════════
# All lesson content is generated inline from the markdown data
# ══════════════════════════════════════════════════════════════════════

# This file is already very long. Instead of hand-coding all 9 lessons,
# we use a data-driven approach — see the generate_lesson_X() functions.

# For efficiency, let's build content for each lesson with compact helpers.


def _obj_card(icon, title, desc):
    return f'''  <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
    <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
      <span class="iconify text-brand text-lg" data-icon="{icon}"></span>
    </span>
    <div>
      <p class="text-sm font-semibold text-gray-800">{title}</p>
      <p class="text-xs text-gray-500 mt-0.5">{desc}</p>
    </div>
  </div>'''


def obj_section(cards, tip):
    grid = '\n'.join(cards)
    return f'''<div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
{grid}
</div>
<div class="mt-5 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">{tip}</p>
</div>'''


def _overview_hook(text):
    return f'''<div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
  <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Py</span>
  <div class="relative flex items-center gap-4">
    <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">
      <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>
    </span>
    <p class="text-base text-gray-800 leading-relaxed font-medium">{text}</p>
  </div>
</div>'''


def _overview_card(icon, title, analogy_sub, desc, color="pink"):
    colors = {
        "pink": ("bg-[#fdf0f7]", "text-brand", "hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40"),
        "violet": ("bg-violet-50", "text-violet-500", "hover:border-violet-100 hover:bg-violet-50/30"),
        "blue": ("bg-blue-50", "text-blue-500", "hover:border-blue-100 hover:bg-blue-50/30"),
        "emerald": ("bg-emerald-50", "text-emerald-500", "hover:border-emerald-100 hover:bg-emerald-50/30"),
    }
    bg, tc, hover = colors.get(color, colors["pink"])
    return f'''<div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 {hover} transition-colors">
    <div class="flex items-center gap-3 mb-2.5">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg {bg} shrink-0">
        <span class="iconify {tc} text-base" data-icon="{icon}"></span>
      </span>
      <div>
        <p class="text-sm font-bold text-gray-800 leading-tight">{title}</p>
        <p class="text-[10px] text-gray-400 italic leading-tight">{analogy_sub}</p>
      </div>
    </div>
    <p class="text-xs text-gray-500 leading-relaxed">{desc}</p>
  </div>'''


def overview_section(hook, analogy_text, cards_html, tip):
    return f'''{_overview_hook(hook)}
<p class="text-sm text-gray-600 leading-relaxed">{analogy_text}</p>
<div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
{cards_html}
</div>
<div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">{tip}</p>
</div>'''


def _ki_card(color, icon, title, desc, keywords):
    configs = {
        "pink": ("border-gray-100", "from-[#CB187D] to-[#e84aad]", "from-[#CB187D] to-[#e84aad]", "bg-pink-50 text-[#CB187D] border-pink-100", "obj-card-kt"),
        "violet": ("border-violet-100", "from-violet-500 to-purple-400", "from-violet-500 to-purple-600", "bg-violet-50 text-violet-600 border-violet-100", "obj-card-violet"),
        "blue": ("border-blue-100", "from-blue-500 to-indigo-400", "from-blue-500 to-indigo-600", "bg-blue-50 text-blue-600 border-blue-100", "obj-card-blue"),
    }
    border, grad_top, grad_icon, pill_cls, card_cls = configs[color]
    pills = "\n      ".join([f'<span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold {pill_cls}">{k}</span>' for k in keywords])
    return f'''<div class="obj-card {card_cls} rounded-2xl border {border} bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r {grad_top}"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br {grad_icon} shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="{icon}"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">{title}</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">{desc}</p>
    <div class="flex flex-wrap gap-2">
      {pills}
    </div>
  </div>
</div>'''


def _ce_tab_btn(idx, label, active=False):
    if active:
        return f'<button onclick="switchCeTab({idx})" class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code"></span><span class="ce-step-label text-xs font-bold">{label}</span></button>'
    return f'<button onclick="switchCeTab({idx})" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code"></span><span class="ce-step-label text-xs font-bold">{label}</span></button>'


def _ce_panel(idx, num_label, title, difficulty, task_desc, code_html, hidden=False):
    h = ' hidden' if hidden else ''
    diff_colors = {
        "Beginner": ("bg-emerald-50 text-emerald-600 border-emerald-200", "fa6-solid:leaf"),
        "Intermediate": ("bg-amber-50 text-amber-600 border-amber-200", "fa6-solid:fire"),
    }
    dc, di = diff_colors.get(difficulty, diff_colors["Beginner"])
    return f'''<div class="ce-panel ce-panel-anim{h}" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{num_label}</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:code"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">{title}</h3>
          <div class="flex items-center gap-2 mt-1">
            <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full {dc}">
              <span class="iconify text-[10px]" data-icon="{di}"></span> {difficulty}
            </span>
          </div>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
          <p class="text-sm text-gray-600">{task_desc}</p>
        </div>
      </div>
{code_html}
    </div>
  </div>
</div>'''


def _mistake_card(idx, title, wrong_code, right_code, explanation=""):
    exp_html = f'<p class="text-xs text-gray-500 leading-relaxed mt-3">{explanation}</p>' if explanation else ""
    return f'''<div class="mistake-card rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
  <div class="px-6 py-4 bg-gradient-to-r from-red-50 to-white border-b border-gray-100">
    <div class="flex items-center gap-3">
      <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-red-100 shrink-0">
        <span class="iconify text-red-500 text-sm" data-icon="fa6-solid:triangle-exclamation"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-800">Mistake {idx}: {title}</h3>
    </div>
  </div>
  <div class="px-6 py-5 space-y-3">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
      <div>
        <p class="text-[10px] font-bold uppercase tracking-widest text-red-400 mb-1.5">&#10007; Wrong</p>
        {_code_block_b_lite(wrong_code)}
      </div>
      <div>
        <p class="text-[10px] font-bold uppercase tracking-widest text-emerald-500 mb-1.5">&#10003; Correct</p>
        {_code_block_b_lite(right_code)}
      </div>
    </div>{exp_html}
  </div>
</div>'''


def _pe_tab_btn(idx, label, active=False):
    if active:
        return f'<button onclick="switchPeTab({idx})" class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span><span class="pe-step-label text-xs font-bold">{label}</span></button>'
    return f'<button onclick="switchPeTab({idx})" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span><span class="pe-step-label text-xs font-bold">{label}</span></button>'

def _pe_panel(idx, num_label, title, task_desc, code_html, hidden=False):
    h = ' hidden' if hidden else ''
    return f'''<div class="pe-panel pe-panel-anim{h}" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{num_label}</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">{title}</h3>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Task</p>
          <p class="text-sm text-gray-600">{task_desc}</p>
        </div>
      </div>
{code_html}
    </div>
  </div>
</div>'''


def _recap_card(num, text):
    return f'''<div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
  <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
    <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{num:02d}</span>
    <div class="relative flex items-start gap-3">
      <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
        <span class="iconify text-sm" data-icon="fa6-solid:check"></span>
      </span>
      <p class="text-sm text-gray-700 font-medium leading-relaxed">{text}</p>
    </div>
  </div>
</div>'''


def _quiz_tab_btn(idx, label, active=False):
    if active:
        return f'<button onclick="switchQzTab({idx})" class="qz-step qz-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">{label}</span></button>'
    return f'<button onclick="switchQzTab({idx})" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">{label}</span></button>'


def _quiz_panel(idx, question, correct_btn_label, incorrect_btn_label, correct_is_first=True, hidden=False):
    h = ' hidden' if hidden else ''
    q_num = f"Q{idx+1}"
    if correct_is_first:
        btns = f'''<button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors" onclick="checkQuiz(this, true)">
              <span class="iconify mr-1.5" data-icon="fa6-solid:check"></span> {correct_btn_label}
            </button>
            <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors" onclick="checkQuiz(this, false)">
              <span class="iconify mr-1.5" data-icon="fa6-solid:xmark"></span> {incorrect_btn_label}
            </button>'''
    else:
        btns = f'''<button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors" onclick="checkQuiz(this, false)">
              <span class="iconify mr-1.5" data-icon="fa6-solid:xmark"></span> {incorrect_btn_label}
            </button>
            <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors" onclick="checkQuiz(this, true)">
              <span class="iconify mr-1.5" data-icon="fa6-solid:check"></span> {correct_btn_label}
            </button>'''
    return f'''<div class="qz-panel qz-panel-anim{h}" role="tabpanel">
  <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{q_num}</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:circle-question"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Question {idx+1}</h3>
          <p class="text-xs text-gray-500 mt-0.5">Select the correct answer</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="quiz-question" data-qid="quiz-q{idx}">
        <p class="text-sm font-semibold text-gray-800 mb-4">{question}</p>
        <div class="flex gap-3">
            {btns}
        </div>
        <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
      </div>
    </div>
  </div>
</div>'''


COMPLETION_BANNER = '''<div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">
  <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">&#10003;</span>
  <div class="relative flex items-center gap-4">
    <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">
      <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>
    </span>
    <div>
      <p class="text-sm font-bold text-white">Lesson Complete!</p>
      <p class="text-xs text-white/80 mt-0.5">You\'ve covered 4 key concepts. Ready for the knowledge check?</p>
    </div>
  </div>
</div>'''


# ══════════════════════════════════════════════════════════════════════
#  Now the actual content generation — imported from the md files
# ══════════════════════════════════════════════════════════════════════

# Due to the extreme length of hand-crafted content, we use a content
# mapping approach. Each lesson has a function that builds all sections.

def build_all():
    from _build_mod04_content import LESSON_SECTIONS
    os.makedirs(OUT_DIR, exist_ok=True)
    for num, slug, title, subtitle, diff_dots, duration, date in LESSONS:
        sections = LESSON_SECTIONS[num]
        sections_html = "\n\n".join(sections)
        full = build_full_html(num, title, subtitle, diff_dots, duration, date, sections_html)
        outpath = os.path.join(OUT_DIR, f"{slug}.html")
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(full)
        lines = full.count("\n") + 1
        print(f"  ✅ {slug}.html ({lines:,} lines)")

if __name__ == "__main__":
    build_all()
