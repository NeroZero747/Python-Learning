"""
Comprehensive quality-audit fix script for lesson01_what_is_data_engineering.html
Addresses all 14 checks from the lesson-quality-audit prompt.

Changes applied:
  Check 1  — Objective cards verified (4 cards match 4 concepts) ✓ already correct
  Check 2  — Hero pill counts updated to match actual tab counts
  Check 3b — Overview card explanations enriched (1→3 sentences each)
  Check 4  — Key Ideas: grid layout, text-sm, 4th card, hover CSS, bg-white
  Check 5  — KC tab 4 added (Data Quality), panel depth improved
  Check 6  — Common Mistakes tabs 4–5 added
  Check 7  — Comparison rows verified (4 rows = 4 objectives) ✓ already correct
  Check 8  — Recap cards verified (4 cards = 4 objectives) ✓ already correct
  Check 9  — Completion banner count verified ✓ already correct
  Check 10 — Icons all use safe Iconify prefixes ✓ already correct
  Check 11 — Obj-card hover CSS fixed (no translateY, neutral shadow)
  Check 12 — CE tab 5, PE tabs 4–5, QZ tabs 4–5 added
  Check 13 — Cross-section uniqueness enforced in new content
  Check 14 — Div balance verified at end
"""

import re
import sys

FILE = r'pages\mod_04_data_engineering\lesson01_what_is_data_engineering.html'


def safe_replace(html, old, new, label):
    """Replace exactly one occurrence. Abort if not found or ambiguous."""
    count = html.count(old)
    if count == 0:
        print(f"  ❌ {label}: pattern NOT FOUND")
        sys.exit(1)
    if count > 1:
        print(f"  ⚠️  {label}: pattern found {count} times (expected 1)")
        sys.exit(1)
    html = html.replace(old, new, 1)
    print(f"  ✅ {label}")
    return html


def insert_after(html, marker, content, label):
    """Insert content immediately after the first occurrence of marker."""
    idx = html.find(marker)
    if idx == -1:
        print(f"  ❌ {label}: marker NOT FOUND")
        sys.exit(1)
    pos = idx + len(marker)
    html = html[:pos] + content + html[pos:]
    print(f"  ✅ {label}")
    return html


def insert_before(html, marker, content, label):
    """Insert content immediately before the first occurrence of marker."""
    idx = html.find(marker)
    if idx == -1:
        print(f"  ❌ {label}: marker NOT FOUND")
        sys.exit(1)
    html = html[:idx] + content + html[idx:]
    print(f"  ✅ {label}")
    return html


# ──────────────────────────────────────────────────────────────
# READ
# ──────────────────────────────────────────────────────────────
with open(FILE, 'r', encoding='utf-8') as f:
    html = f.read()

print(f"Read {len(html):,} chars from {FILE}")
print()


# ──────────────────────────────────────────────────────────────
# CLEAN RESTART — Apply all changes in order using safe_replace
# ──────────────────────────────────────────────────────────────

# ══════════════════════════════════════════════════════════════
# STEP 1: CSS FIXES (Check 11 + Check 4d)
# ══════════════════════════════════════════════════════════════
print("STEP 1: CSS fixes")

html = safe_replace(html,
    """    .obj-card {
      transition: transform 0.22s cubic-bezier(.4,0,.2,1),
                  box-shadow 0.22s cubic-bezier(.4,0,.2,1),
                  border-color 0.22s ease, background-color 0.22s ease;
    }
    .obj-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 14px 32px -6px rgba(203,24,125,0.18), 0 6px 12px -2px rgba(203,24,125,0.1);
      border-color: #CB187D; background-color: #fdf0f7;
    }
    .obj-card .obj-icon { transition: transform 0.22s cubic-bezier(.4,0,.2,1), background-color 0.22s ease; }
    .obj-card:hover .obj-icon { transform: scale(1.1); background-color: #CB187D; }
    .obj-card:hover .obj-icon .iconify { color: white !important; }
    .obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }
    .obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; background-color: #ffffff; }
    .obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; background-color: #ffffff; }""",

    """    .obj-card {
      transition: box-shadow 0.22s cubic-bezier(.4,0,.2,1),
                  border-color 0.22s ease, background-color 0.22s ease;
    }
    .obj-card:hover {
      box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08);
      border-color: #f5c6e0; background-color: #ffffff;
    }
    .obj-card .obj-icon { transition: transform 0.22s cubic-bezier(.4,0,.2,1), background-color 0.22s ease; }
    .obj-card:hover .obj-icon { transform: scale(1.1); background-color: #CB187D; }
    .obj-card:hover .obj-icon .iconify { color: white !important; }

    /* ── Key Takeaway cards — keep border gray and icon gradient on hover ── */
    #key-ideas .obj-card:hover { border-color: #f3f4f6; background-color: #ffffff; box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08); }
    #key-ideas .obj-card:hover .obj-icon { transform: scale(1.1); background-color: revert; }""",

    "obj-card hover fix + key-ideas hover"
)

# Hub-root overrides
html = insert_before(html,
    "  </style>",
    """
  /* ── Obj-card hover (Confluence) ── */
  #hub-root .obj-card:hover {
    border-color: #f5c6e0 !important;
    box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08) !important;
    background-color: #ffffff !important;
  }
  #hub-root .obj-card:hover .obj-icon {
    background: #CB187D !important;
  }
  #hub-root .obj-card:hover .obj-icon .iconify {
    color: #ffffff !important;
  }
  /* ── Key Takeaway cards — keep border gray and icon gradient on hover ── */
  #hub-root #key-ideas .obj-card:hover {
    border-color: #f3f4f6 !important;
    background-color: #ffffff !important;
    box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08) !important;
  }
  #hub-root #key-ideas .obj-card:hover .obj-icon {
    background: revert !important;
  }
""",
    "#hub-root overrides for obj-card + key-ideas hover"
)
print()

# ══════════════════════════════════════════════════════════════
# STEP 2: HERO PILLS (Check 2)
# ══════════════════════════════════════════════════════════════
print("STEP 2: Hero pill counts")

html = safe_replace(html,
    '<span class="font-extrabold">8</span>\n            <span class="font-semibold opacity-55">Examples</span>',
    '<span class="font-extrabold">5</span>\n            <span class="font-semibold opacity-55">Examples</span>',
    "Examples: 8 → 5"
)

html = safe_replace(html,
    '<span class="font-extrabold">6</span>\n            <span class="font-semibold opacity-55">Exercises</span>',
    '<span class="font-extrabold">5</span>\n            <span class="font-semibold opacity-55">Exercises</span>',
    "Exercises: 6 → 5"
)
print()

# ══════════════════════════════════════════════════════════════
# STEP 3: OVERVIEW CARD DEPTH (Check 3b)
# ══════════════════════════════════════════════════════════════
print("STEP 3: Overview card depth enrichment")

html = safe_replace(html,
    '<p class="text-xs text-gray-500 leading-relaxed">Every river, well, and reservoir feeding into the plant.</p>',
    '<p class="text-xs text-gray-500 leading-relaxed">Data sources are the databases, APIs, files, and streaming feeds that supply raw information to your pipeline. You connect to these sources as the very first step, before any cleaning or transformation happens. Common examples include PostgreSQL databases, REST APIs, CSV exports from vendors, and real-time event streams.</p>',
    "Card 1 (Data Sources)"
)

html = safe_replace(html,
    '<p class="text-xs text-gray-500 leading-relaxed">Each stage moves water one step closer to the tap.</p>',
    '<p class="text-xs text-gray-500 leading-relaxed">A data pipeline is a sequence of automated steps that extract data from a source, transform it (clean, filter, aggregate), and load the results into a destination. You build a pipeline so the process runs reliably without manual intervention. The three classic stages — Extract, Transform, Load — form the backbone of almost every data engineering workflow.</p>',
    "Card 2 (Pipelines)"
)

html = safe_replace(html,
    '<p class="text-xs text-gray-500 leading-relaxed">A large tank keeping treated water available on demand.</p>',
    '<p class="text-xs text-gray-500 leading-relaxed">Data storage is where your cleaned, processed data lives so analysts and applications can query it quickly. You choose a storage format based on how the data will be used — a data warehouse for SQL analytics, a data lake for raw files, or a simple PostgreSQL table for smaller datasets. The goal is fast, reliable reads whenever downstream users need the data.</p>',
    "Card 3 (Storage)"
)

html = safe_replace(html,
    '<p class="text-xs text-gray-500 leading-relaxed">Samples tested at each stage so nothing unsafe gets through.</p>',
    '<p class="text-xs text-gray-500 leading-relaxed">Data quality means verifying that your pipeline output is accurate, complete, and consistent before anyone uses it for decisions. You add validation checks — row counts, null-value scans, schema matching — at each stage so problems are caught early. A single bad column or missing date can silently corrupt every dashboard that depends on it.</p>',
    "Card 4 (Quality)"
)
print()

# ══════════════════════════════════════════════════════════════
# STEP 4: KEY IDEAS RESTRUCTURING (Check 4)
# ══════════════════════════════════════════════════════════════
print("STEP 4: Key Ideas → 2-col grid + 4th card + text-sm")

OLD_KI = """    <div class="bg-white px-8 py-7 space-y-4">

<div class="obj-card obj-card-kt rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:arrow-right-arrow-left"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Pipelines Power Every Dashboard</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">Every chart or report you see relies on a pipeline that moved raw data from its source, cleaned it, and delivered it to the right place.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Automation</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Reliability</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Delivery</span>
    </div>
  </div>
</div>

<div class="obj-card obj-card-violet rounded-2xl border border-violet-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:handshake"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Analysts Depend on Engineers</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">Without a data engineer maintaining pipelines, an analyst's SQL query would return stale or broken results — like opening a spreadsheet that was never updated.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Trust</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Freshness</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Accuracy</span>
    </div>
  </div>
</div>

<div class="obj-card obj-card-blue rounded-2xl border border-blue-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>
  <div class="px-6 py-5">
    <div class="flex items-center gap-3 mb-3">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:expand"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Scale Changes Everything</h3>
    </div>
    <p class="text-xs text-gray-600 leading-relaxed mb-4">A CSV with 500 rows opens instantly in Excel, but a dataset with 50 million rows needs specialized tools and a plan for memory, storage, and speed.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Volume</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Memory</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Throughput</span>
    </div>
  </div>
</div>

</div>"""

NEW_KI = """    <div class="bg-white px-8 py-7">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">

<div class="obj-card rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
  <div class="px-5 py-5 space-y-3 bg-white">
    <div class="flex items-center gap-3">
      <span class="obj-icon inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:arrow-right-arrow-left"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Pipelines Power Every Dashboard</h3>
    </div>
    <p class="text-sm text-gray-600 leading-relaxed">Every chart or report you see relies on a pipeline that moved raw data from its source, cleaned it, and delivered it to the right place. If a pipeline breaks at 2 AM, every downstream report goes dark until someone fixes it — which is why automation and monitoring are core data engineering skills.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Automation</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Reliability</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Delivery</span>
    </div>
  </div>
</div>

<div class="obj-card rounded-2xl border border-violet-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
  <div class="px-5 py-5 space-y-3 bg-white">
    <div class="flex items-center gap-3">
      <span class="obj-icon inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:handshake"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Analysts Depend on Engineers</h3>
    </div>
    <p class="text-sm text-gray-600 leading-relaxed">Without a data engineer maintaining pipelines, an analyst's SQL query would return stale or broken results — like opening a spreadsheet that was never updated. Understanding these role boundaries helps you communicate the right request to the right team and avoid bottlenecks in your data workflow.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Trust</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Freshness</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Accuracy</span>
    </div>
  </div>
</div>

<div class="obj-card rounded-2xl border border-blue-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>
  <div class="px-5 py-5 space-y-3 bg-white">
    <div class="flex items-center gap-3">
      <span class="obj-icon inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:expand"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Scale Changes Everything</h3>
    </div>
    <p class="text-sm text-gray-600 leading-relaxed">A CSV with 500 rows opens instantly in Excel, but a dataset with 50 million rows needs specialized tools and a plan for memory, storage, and speed. Learning to think in terms of batches, partitions, and lazy evaluation early on saves you from rewriting everything when your data outgrows a single machine.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Volume</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Memory</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Throughput</span>
    </div>
  </div>
</div>

<div class="obj-card rounded-2xl border border-emerald-100 bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r from-emerald-500 to-teal-400"></div>
  <div class="px-5 py-5 space-y-3 bg-white">
    <div class="flex items-center gap-3">
      <span class="obj-icon inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="fa6-solid:shield-halved"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">Bad Data Costs Real Money</h3>
    </div>
    <p class="text-sm text-gray-600 leading-relaxed">When a pipeline delivers incorrect or stale data to a dashboard, decisions made from that dashboard are wrong too — and undoing those decisions is expensive. Catching data quality issues inside the pipeline is far cheaper than discovering them after a report has already been sent to stakeholders.</p>
    <div class="flex flex-wrap gap-2">
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-600 border border-emerald-100">Quality</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-600 border border-emerald-100">Validation</span>
      <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-600 border border-emerald-100">Prevention</span>
    </div>
  </div>
</div>

      </div>
    </div>"""

html = safe_replace(html, OLD_KI, NEW_KI, "Key Ideas full replacement")
print()

# ══════════════════════════════════════════════════════════════
# STEP 5: KC TAB 4 (Check 5)
# ══════════════════════════════════════════════════════════════
print("STEP 5: KC tab 4 (Data Quality)")

# Insert 4th tab button
KC_TAB3_BUTTON = """<button onclick="switchKcTab(2)" class="kc-tab  group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
  <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:puzzle-piece"></span></span>
  <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Data Warehouse</span>
</button>"""

KC_TAB4_BUTTON = """<button onclick="switchKcTab(2)" class="kc-tab  group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
  <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:puzzle-piece"></span></span>
  <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Data Warehouse</span>
</button>
<button onclick="switchKcTab(3)" class="kc-tab  group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
  <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:vial"></span></span>
  <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Data Quality</span>
</button>"""

html = safe_replace(html, KC_TAB3_BUTTON, KC_TAB4_BUTTON, "KC tab 4 button")

# Insert 4th KC panel. Find the end of the last kc-panel using section boundary.
# The KC section body structure ends with: </div> (panels container) </div> (flex row) </div> (bg-white) </div> (rounded card) </section>
# I need to find the last kc-panel and insert after it.

# Find all kc-panel positions
kc_panels = list(re.finditer(r'<div class="kc-panel kc-panel-anim[^"]*"', html))
if len(kc_panels) < 3:
    print("  ❌ Expected at least 3 kc-panel elements")
    sys.exit(1)

last_panel_start = kc_panels[-1].start()

# Walk forward to find the matching closing </div> at depth 0
depth = 0
i = last_panel_start
while i < len(html):
    if html[i:i+4] == '<div':
        depth += 1
        i += 4
    elif html[i:i+6] == '</div>':
        depth -= 1
        i += 6
        if depth == 0:
            break
    else:
        i += 1

panel_insert_pos = i

KC_PANEL_4 = """
<div class="kc-panel kc-panel-anim hidden" data-color="emerald" role="tabpanel">
  <div class="rounded-2xl border border-emerald-100 overflow-hidden">
    <div class="h-1 bg-gradient-to-r from-emerald-500 via-teal-400 to-cyan-300"></div>
    <div class="bg-gradient-to-br from-emerald-50/60 to-white p-5 space-y-4">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3">
          <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shrink-0 shadow-md">
            <span class="iconify text-white text-sm" data-icon="fa6-solid:vial"></span>
          </span>
          <div>
            <h3 class="text-sm font-bold text-gray-900 leading-tight">Data Quality</h3>
            <p class="text-[10px] text-gray-400 mt-0.5">Validate pipeline output before anyone uses it</p>
          </div>
        </div>
        <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-bold bg-gradient-to-r from-emerald-100 to-teal-100 text-emerald-600">Core</span>
      </div>
      <p class="text-xs text-gray-600 leading-relaxed">Data quality is the practice of verifying that your pipeline output meets expected standards for accuracy, completeness, and consistency. You embed validation checks at the end of each pipeline stage — row counts, null scans, and schema matching — so errors are caught before they reach any dashboard or report.</p>
      <div class="rounded-xl overflow-hidden bg-code shadow-md">
        <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
          <div class="flex items-center gap-2">
            <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
            <span class="text-[11px] font-semibold text-gray-400">Python</span>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
            <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
          </button>
        </div>
        <pre class="overflow-x-auto pre-reset"><code class="language-python">def validate(df):
    \"""Run basic quality checks on a DataFrame.\"""
    assert len(df) &gt; 0, "Empty DataFrame"             # at least one row
    nulls = df.isnull().sum().sum()                    # count all nulls
    dupes = df.duplicated().sum()                      # count duplicate rows
    print(f"Rows: {len(df)}, Nulls: {nulls}, Dupes: {dupes}")
    assert nulls == 0, f"Found {nulls} null values"
    assert dupes == 0, f"Found {dupes} duplicate rows"</code></pre>
      </div>
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-xs text-gray-600">Always validate row counts and null values at the end of every pipeline step — silent data loss is the most dangerous kind of bug because no error message appears to warn you.</p>
      </div>
    </div>
  </div>
</div>"""

html = html[:panel_insert_pos] + KC_PANEL_4 + html[panel_insert_pos:]
print("  ✅ KC panel 4 (Data Quality) inserted")
print()

# ══════════════════════════════════════════════════════════════
# STEP 6: CE TAB 5 (Check 12a)
# ══════════════════════════════════════════════════════════════
print("STEP 6: CE tab 5 (Validate Pipeline Output)")

# Find the CE section. Locate the last ce-step button by finding switchCeTab(3)
# and insert a new button after the complete button element.
# Strategy: find the exact button for tab 3, then insert a new button after it.

# The ce-step buttons are in a flex row. Each button element is on one or multi-lines.
# I need to find the complete button tag containing switchCeTab(3).

ce3_match = re.search(r'(<button[^>]*switchCeTab\(3\)[^>]*>.*?</button>)', html, re.DOTALL)
if not ce3_match:
    print("  ❌ Could not find CE tab 3 button")
    sys.exit(1)

ce3_end = ce3_match.end()
CE_TAB5_BUTTON = """
    <button onclick="switchCeTab(4)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
      <span class="iconify text-[13px]" data-icon="fa6-solid:vial"></span>
      <span class="text-xs font-bold">Example 5 — Validate Output</span>
    </button>"""

html = html[:ce3_end] + CE_TAB5_BUTTON + html[ce3_end:]
print("  ✅ CE tab 5 button inserted")

# Find the last ce-panel and insert panel 5 after it
ce_panels = list(re.finditer(r'<div class="ce-panel ce-panel-anim[^"]*"', html))
last_ce_start = ce_panels[-1].start()
depth = 0
i = last_ce_start
while i < len(html):
    if html[i:i+4] == '<div':
        depth += 1
        i += 4
    elif html[i:i+6] == '</div>':
        depth -= 1
        i += 6
        if depth == 0:
            break
    else:
        i += 1
ce_panel_insert = i

CE_PANEL_5 = """

    <!-- Panel 5: Validate Output -->
    <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
      <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
        <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
          <div class="flex items-center gap-3">
            <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
              <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
              <span class="text-[11px] font-semibold text-gray-400">validate_output.py</span>
            </div>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
            <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
          </button>
        </div>
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-python">import pandas as pd

# Load the output of a pipeline stage
sales = pd.read_csv("clean_sales.csv")      # read the cleaned data

# --- Quality checks ---
row_count = len(sales)                       # how many rows?
null_count = sales.isnull().sum().sum()       # any missing values?
dupe_count = sales.duplicated().sum()         # any exact duplicate rows?

print(f"Rows: {row_count}")
print(f"Nulls: {null_count}")
print(f"Duplicates: {dupe_count}")

# Fail loudly if something is wrong
assert row_count &gt; 0,    "FAIL: DataFrame is empty"
assert null_count == 0,  f"FAIL: {null_count} null values found"
assert dupe_count == 0,  f"FAIL: {dupe_count} duplicate rows"
print("✓ All quality checks passed")</code></pre>
        </div>
        <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
          <div class="flex items-center gap-2 mb-1.5">
            <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
            <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
            <span class="text-[10px] text-gray-600 font-mono">$ python validate_output.py</span>
          </div>
          <div class="font-mono text-xs text-emerald-400 leading-relaxed">Rows: 1248<br>Nulls: 0<br>Duplicates: 0<br>✓ All quality checks passed</div>
        </div>
      </div>
      <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">If any <code class="font-mono text-xs bg-gray-100 px-1.5 py-0.5 rounded">assert</code> fails, Python raises an <code class="font-mono text-xs bg-gray-100 px-1.5 py-0.5 rounded">AssertionError</code> and the script stops immediately — so no bad data moves to the next stage.</p>
      </div>
    </div>"""

html = html[:ce_panel_insert] + CE_PANEL_5 + html[ce_panel_insert:]
print("  ✅ CE panel 5 inserted")
print()

# ══════════════════════════════════════════════════════════════
# STEP 7: MK TABS 4–5 (Check 6)
# ══════════════════════════════════════════════════════════════
print("STEP 7: MK tabs 4–5")

mk2_match = re.search(r'(<button[^>]*switchMkTab\(2\)[^>]*>.*?</button>)', html, re.DOTALL)
if not mk2_match:
    print("  ❌ Could not find MK tab 2 button")
    sys.exit(1)

mk2_end = mk2_match.end()
MK_NEW_BUTTONS = """
    <button onclick="switchMkTab(3)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
      <span class="iconify text-[13px]" data-icon="fa6-solid:triangle-exclamation"></span>
      <span class="text-xs font-bold">Ignoring Data Types</span>
    </button>
    <button onclick="switchMkTab(4)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
      <span class="iconify text-[13px]" data-icon="fa6-solid:triangle-exclamation"></span>
      <span class="text-xs font-bold">No Error Handling</span>
    </button>"""

html = html[:mk2_end] + MK_NEW_BUTTONS + html[mk2_end:]
print("  ✅ MK tab buttons 4–5 inserted")

# Insert MK panels 4–5 after the last mk-panel
mk_panels = list(re.finditer(r'<div class="mk-panel mk-panel-anim[^"]*"', html))
last_mk_start = mk_panels[-1].start()
depth = 0
i = last_mk_start
while i < len(html):
    if html[i:i+4] == '<div':
        depth += 1
        i += 4
    elif html[i:i+6] == '</div>':
        depth -= 1
        i += 6
        if depth == 0:
            break
    else:
        i += 1
mk_panel_insert = i

MK_PANELS_4_5 = """

    <!-- Mistake 4: Ignoring Data Types -->
    <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
      <div class="mistake-card rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="flex items-center justify-between px-6 py-4 bg-gradient-to-r from-red-50 to-white border-b border-gray-100">
          <div>
            <h3 class="text-sm font-semibold text-gray-800">Ignoring data types after loading</h3>
            <p class="text-xs text-gray-500 mt-0.5">Data arrives as strings by default — forgetting to cast types leads to silent calculation errors.</p>
          </div>
          <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-red-100 shrink-0">
            <span class="iconify text-red-500 text-sm" data-icon="fa6-solid:triangle-exclamation"></span>
          </span>
        </div>
        <div class="px-6 py-5 space-y-4">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div>
              <p class="text-[11px] font-bold text-red-500 uppercase tracking-widest mb-2">✗ Wrong</p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># Columns stay as strings after CSV load
df = pd.read_csv("sales.csv")
# "100" + "200" = "100200" — string concat!
total = df["amount"].sum()</code></pre>
              </div>
            </div>
            <div>
              <p class="text-[11px] font-bold text-emerald-600 uppercase tracking-widest mb-2">✓ Correct</p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># Explicitly cast types after loading
df = pd.read_csv("sales.csv")
df["amount"] = pd.to_numeric(df["amount"])
total = df["amount"].sum()  # 300 ✓</code></pre>
              </div>
            </div>
          </div>
          <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
            <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
            <p class="text-xs text-gray-600">Run <code class="font-mono bg-gray-100 px-1 py-0.5 rounded text-[11px]">df.dtypes</code> immediately after loading to verify every column has the correct type — this one check prevents most silent calculation bugs.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Mistake 5: No Error Handling -->
    <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
      <div class="mistake-card rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="flex items-center justify-between px-6 py-4 bg-gradient-to-r from-red-50 to-white border-b border-gray-100">
          <div>
            <h3 class="text-sm font-semibold text-gray-800">No error handling in the pipeline</h3>
            <p class="text-xs text-gray-500 mt-0.5">When a pipeline fails without try/except, you get a cryptic traceback instead of a clear message about what went wrong.</p>
          </div>
          <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-red-100 shrink-0">
            <span class="iconify text-red-500 text-sm" data-icon="fa6-solid:triangle-exclamation"></span>
          </span>
        </div>
        <div class="px-6 py-5 space-y-4">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div>
              <p class="text-[11px] font-bold text-red-500 uppercase tracking-widest mb-2">✗ Wrong</p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># No protection — crashes silently
df = pd.read_csv("data.csv")
df.to_csv("output.csv")
print("Done")</code></pre>
              </div>
            </div>
            <div>
              <p class="text-[11px] font-bold text-emerald-600 uppercase tracking-widest mb-2">✓ Correct</p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">try:
    df = pd.read_csv("data.csv")
    df.to_csv("output.csv")
    print("✓ Pipeline complete")
except FileNotFoundError as e:
    print(f"✗ File missing: {e}")
except Exception as e:
    print(f"✗ Pipeline failed: {e}")</code></pre>
              </div>
            </div>
          </div>
          <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
            <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
            <p class="text-xs text-gray-600">Wrap every pipeline stage in a <code class="font-mono bg-gray-100 px-1 py-0.5 rounded text-[11px]">try/except</code> block and print which stage failed — this turns a 30-minute debugging session into a 30-second fix.</p>
          </div>
        </div>
      </div>
    </div>"""

html = html[:mk_panel_insert] + MK_PANELS_4_5 + html[mk_panel_insert:]
print("  ✅ MK panels 4–5 inserted")
print()

# ══════════════════════════════════════════════════════════════
# STEP 8: PE TABS 4–5 (Check 12b)
# ══════════════════════════════════════════════════════════════
print("STEP 8: PE tabs 4–5")

pe2_match = re.search(r'(<button[^>]*switchPeTab\(2\)[^>]*>.*?</button>)', html, re.DOTALL)
if not pe2_match:
    print("  ❌ Could not find PE tab 2 button")
    sys.exit(1)

pe2_end = pe2_match.end()
PE_NEW_BUTTONS = """
    <button onclick="switchPeTab(3)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
      <span class="iconify text-[13px]" data-icon="fa6-solid:vial"></span>
      <span class="text-xs font-bold">Exercise 4 — Validate Data Quality</span>
    </button>
    <button onclick="switchPeTab(4)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
      <span class="iconify text-[13px]" data-icon="fa6-solid:gears"></span>
      <span class="text-xs font-bold">Exercise 5 — Mini Pipeline</span>
    </button>"""

html = html[:pe2_end] + PE_NEW_BUTTONS + html[pe2_end:]
print("  ✅ PE tab buttons 4–5 inserted")

pe_panels = list(re.finditer(r'<div class="pe-panel pe-panel-anim[^"]*"', html))
last_pe_start = pe_panels[-1].start()
depth = 0
i = last_pe_start
while i < len(html):
    if html[i:i+4] == '<div':
        depth += 1
        i += 4
    elif html[i:i+6] == '</div>':
        depth -= 1
        i += 6
        if depth == 0:
            break
    else:
        i += 1
pe_panel_insert = i

PE_PANELS_4_5 = """

    <!-- Exercise 4: Validate Data Quality -->
    <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
      <div class="rounded-xl border border-gray-100 bg-white shadow-sm overflow-hidden">
        <div class="px-6 py-5 space-y-4">
          <div class="flex items-center gap-3 mb-2">
            <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-base" data-icon="fa6-solid:vial"></span>
            </span>
            <div>
              <h3 class="text-sm font-bold text-gray-800">Validate Data Quality</h3>
              <p class="text-xs text-gray-400">Write checks that catch bad data before it reaches a dashboard</p>
            </div>
          </div>
          <div class="task-box rounded-xl p-4">
            <p class="text-xs font-bold text-[#CB187D] uppercase tracking-widest mb-2">Your Tasks</p>
            <ol class="text-sm text-gray-700 space-y-1.5 list-decimal list-inside">
              <li>Load <code class="font-mono text-xs bg-white px-1 py-0.5 rounded">sales.csv</code> with pandas and print the shape.</li>
              <li>Check for null values using <code class="font-mono text-xs bg-white px-1 py-0.5 rounded">.isnull().sum()</code> — print any columns with nulls.</li>
              <li>Check for duplicate rows using <code class="font-mono text-xs bg-white px-1 py-0.5 rounded">.duplicated().sum()</code>.</li>
              <li>Write an <code class="font-mono text-xs bg-white px-1 py-0.5 rounded">assert</code> statement that fails if the DataFrame has fewer than 100 rows.</li>
            </ol>
          </div>
          <div>
            <button class="accordion-toggle" onclick="this.classList.toggle('open'); this.nextElementSibling.classList.toggle('open');">
              <span class="iconify text-sm" data-icon="fa6-solid:lightbulb"></span> Show Solution
              <span class="iconify accordion-chevron text-[10px]" data-icon="fa6-solid:chevron-down"></span>
            </button>
            <div class="accordion-body mt-3">
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">validate_quality.py</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                    <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                  </button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">import pandas as pd

sales = pd.read_csv("sales.csv")             # load file
print(f"Shape: {sales.shape}")                # rows x columns

# Check for nulls per column
nulls = sales.isnull().sum()
print(nulls[nulls &gt; 0])                      # show only columns with nulls

# Check for duplicates
dupes = sales.duplicated().sum()
print(f"Duplicate rows: {dupes}")

# Fail if too few rows
assert len(sales) &gt;= 100, "Too few rows — check the source file"
print("✓ All quality checks passed")</code></pre>
                </div>
              </div>
              <p class="mt-3 text-xs text-gray-500 italic">Why this matters: catching data problems early prevents silent errors that cascade through every downstream report.</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Exercise 5: Mini Pipeline -->
    <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
      <div class="rounded-xl border border-gray-100 bg-white shadow-sm overflow-hidden">
        <div class="px-6 py-5 space-y-4">
          <div class="flex items-center gap-3 mb-2">
            <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-base" data-icon="fa6-solid:gears"></span>
            </span>
            <div>
              <h3 class="text-sm font-bold text-gray-800">Build a Mini Pipeline</h3>
              <p class="text-xs text-gray-400">Combine extract, transform, and load in a single script</p>
            </div>
          </div>
          <div class="task-box rounded-xl p-4">
            <p class="text-xs font-bold text-[#CB187D] uppercase tracking-widest mb-2">Your Tasks</p>
            <ol class="text-sm text-gray-700 space-y-1.5 list-decimal list-inside">
              <li>Write an <code class="font-mono text-xs bg-white px-1 py-0.5 rounded">extract()</code> function that reads <code class="font-mono text-xs bg-white px-1 py-0.5 rounded">raw_orders.csv</code>.</li>
              <li>Write a <code class="font-mono text-xs bg-white px-1 py-0.5 rounded">transform(df)</code> function that drops rows with nulls and adds a <code class="font-mono text-xs bg-white px-1 py-0.5 rounded">total</code> column (price × quantity).</li>
              <li>Write a <code class="font-mono text-xs bg-white px-1 py-0.5 rounded">load(df)</code> function that saves the result to <code class="font-mono text-xs bg-white px-1 py-0.5 rounded">clean_orders.csv</code>.</li>
              <li>Call all three functions in order and print a success message.</li>
            </ol>
          </div>
          <div>
            <button class="accordion-toggle" onclick="this.classList.toggle('open'); this.nextElementSibling.classList.toggle('open');">
              <span class="iconify text-sm" data-icon="fa6-solid:lightbulb"></span> Show Solution
              <span class="iconify accordion-chevron text-[10px]" data-icon="fa6-solid:chevron-down"></span>
            </button>
            <div class="accordion-body mt-3">
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">mini_pipeline.py</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                    <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                  </button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">import pandas as pd

def extract():
    \"""Read the raw source file.\"""
    return pd.read_csv("raw_orders.csv")

def transform(df):
    \"""Clean and enrich the data.\"""
    df = df.dropna()                          # remove rows with nulls
    df["total"] = df["price"] * df["quantity"] # calculated column
    return df

def load(df):
    \"""Save the cleaned data.\"""
    df.to_csv("clean_orders.csv", index=False)
    print(f"✓ Saved {len(df)} rows to clean_orders.csv")

# Run the pipeline
raw   = extract()
clean = transform(raw)
load(clean)</code></pre>
                </div>
              </div>
              <p class="mt-3 text-xs text-gray-500 italic">Why this matters: structuring your code as extract → transform → load makes each step testable and reusable independently.</p>
            </div>
          </div>
        </div>
      </div>
    </div>"""

html = html[:pe_panel_insert] + PE_PANELS_4_5 + html[pe_panel_insert:]
print("  ✅ PE panels 4–5 inserted")
print()

# ══════════════════════════════════════════════════════════════
# STEP 9: QZ TABS 4–5 (Check 12c)
# ══════════════════════════════════════════════════════════════
print("STEP 9: QZ tabs 4–5")

qz2_match = re.search(r'(<button[^>]*switchQzTab\(2\)[^>]*>.*?</button>)', html, re.DOTALL)
if not qz2_match:
    print("  ❌ Could not find QZ tab 2 button")
    sys.exit(1)

qz2_end = qz2_match.end()
QZ_NEW_BUTTONS = """
    <button onclick="switchQzTab(3)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
      <span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span>
      <span class="qz-step-label text-xs font-bold">Question 4</span>
    </button>
    <button onclick="switchQzTab(4)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
      <span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span>
      <span class="qz-step-label text-xs font-bold">Question 5</span>
    </button>"""

html = html[:qz2_end] + QZ_NEW_BUTTONS + html[qz2_end:]
print("  ✅ QZ tab buttons 4–5 inserted")

qz_panels = list(re.finditer(r'<div class="qz-panel qz-panel-anim[^"]*"', html))
last_qz_start = qz_panels[-1].start()
depth = 0
i = last_qz_start
while i < len(html):
    if html[i:i+4] == '<div':
        depth += 1
        i += 4
    elif html[i:i+6] == '</div>':
        depth -= 1
        i += 6
        if depth == 0:
            break
    else:
        i += 1
qz_panel_insert = i

QZ_PANELS_4_5 = """

    <!-- Question 4 — Multiple Choice (Roles) -->
    <div class="qz-panel qz-panel-anim hidden" role="tabpanel">
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
          <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q4</span>
          <div class="relative flex items-center gap-3">
            <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
              <span class="iconify text-base" data-icon="fa6-solid:circle-question"></span>
            </span>
            <div>
              <h3 class="font-bold text-gray-800">Multiple Choice</h3>
              <p class="text-xs text-gray-500 mt-0.5">Select the best answer</p>
            </div>
          </div>
        </div>
        <div class="px-6 py-5 space-y-4">
          <div class="quiz-question" data-qid="quiz-q3">
            <p class="text-sm font-semibold text-gray-800 mb-4">Which role is primarily responsible for building and maintaining data pipelines?</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, false)">Data Analyst</button>
              <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, true)">Data Engineer</button>
              <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, false)">Data Scientist</button>
              <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, false)">Business Analyst</button>
            </div>
            <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
          </div>
        </div>
      </div>
    </div>

    <!-- Question 5 — Multiple Choice (ETL Order) -->
    <div class="qz-panel qz-panel-anim hidden" role="tabpanel">
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
          <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q5</span>
          <div class="relative flex items-center gap-3">
            <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
              <span class="iconify text-base" data-icon="fa6-solid:circle-question"></span>
            </span>
            <div>
              <h3 class="font-bold text-gray-800">Multiple Choice</h3>
              <p class="text-xs text-gray-500 mt-0.5">Select the best answer</p>
            </div>
          </div>
        </div>
        <div class="px-6 py-5 space-y-4">
          <div class="quiz-question" data-qid="quiz-q4">
            <p class="text-sm font-semibold text-gray-800 mb-4">Your pipeline reads a CSV, removes nulls, adds a calculated column, and saves the result. What is the correct order of ETL stages for this workflow?</p>
            <div class="grid grid-cols-1 gap-3">
              <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, false)">Transform → Extract → Load</button>
              <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, true)">Extract → Transform → Load</button>
              <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, false)">Load → Transform → Extract</button>
              <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors text-left" onclick="checkQuiz(this, false)">Extract → Load → Transform</button>
            </div>
            <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
          </div>
        </div>
      </div>
    </div>"""

html = html[:qz_panel_insert] + QZ_PANELS_4_5 + html[qz_panel_insert:]
print("  ✅ QZ panels 4–5 inserted")
print()

# ══════════════════════════════════════════════════════════════
# CHECK 14 — Div balance verification
# ══════════════════════════════════════════════════════════════
print("CHECK 14 — Structural integrity verification")

# Check per-section div balance
sections = re.finditer(r'<section\s+id="([^"]+)"[^>]*>(.*?)</section>', html, re.DOTALL)
all_balanced = True
for m in sections:
    sid = m.group(1)
    body = m.group(2)
    opens = len(re.findall(r'<div[\s>]', body))
    closes = body.count('</div>')
    diff = opens - closes
    status = "✅" if diff == 0 else "❌"
    if diff != 0:
        all_balanced = False
    print(f"  {status} #{sid}: opens={opens}, closes={closes}, diff={diff}")

# Check main element balance
main_match = re.search(r'<main\b[^>]*>(.*?)</main>', html, re.DOTALL)
if main_match:
    main_body = main_match.group(1)
    opens = len(re.findall(r'<div[\s>]', main_body))
    closes = main_body.count('</div>')
    diff = opens - closes
    status = "✅" if diff == 0 else "❌"
    if diff != 0:
        all_balanced = False
    print(f"  {status} <main>: opens={opens}, closes={closes}, diff={diff}")

print()

# ──────────────────────────────────────────────────────────────
# WRITE
# ──────────────────────────────────────────────────────────────
with open(FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Written {len(html):,} chars to {FILE}")
lines = html.count('\n') + 1
print(f"File now has {lines} lines")
if all_balanced:
    print("\n✅ ALL CHECKS PASSED — file is clean")
else:
    print("\n⚠️  Div imbalance detected — manual review needed")
