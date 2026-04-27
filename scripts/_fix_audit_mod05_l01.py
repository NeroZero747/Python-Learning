#!/usr/bin/env python3
"""
Full quality audit fix for lesson01_why_build_data_apps.html
Addresses all 14 audit checks: objectives, overview, key-ideas, key-concepts,
code-examples, comparison, practice, mistakes, recap, knowledge-check,
next-lesson, style fixes, and structural integrity.
"""
import re, os

FILE = os.path.join('pages', 'mod_05_data_application', 'lesson01_why_build_data_apps.html')

with open(FILE, 'r', encoding='utf-8') as f:
    text = f.read()

original_len = len(text)

# ═══════════════════════════════════════════════════════════════════════════════
# STYLE FIXES (Check 11 — obj-card hover + Check 4d — key-ideas hover)
# ═══════════════════════════════════════════════════════════════════════════════

# Fix obj-card hover — remove translateY, use neutral shadow, white bg
text = text.replace(
    '.obj-card { transition: transform 0.22s cubic-bezier(.4,0,.2,1), box-shadow 0.22s cubic-bezier(.4,0,.2,1), border-color 0.22s ease, background-color 0.22s ease; }',
    '.obj-card { transition: box-shadow 0.22s cubic-bezier(.4,0,.2,1), border-color 0.22s ease, background-color 0.22s ease; }'
)
text = text.replace(
    '.obj-card:hover { transform: translateY(-4px); box-shadow: 0 14px 32px -6px rgba(203, 24, 125, 0.18), 0 6px 12px -2px rgba(203, 24, 125, 0.1); border-color: #CB187D; background-color: #fdf0f7; }',
    '.obj-card:hover { box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08); border-color: #f5c6e0; background-color: #ffffff; }'
)

# Add key-ideas hover override (neutral border, keep icon gradient)
ki_rules = """
    #key-ideas .obj-card:hover { border-color: #f3f4f6; background-color: #ffffff; box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08); }
    #key-ideas .obj-card:hover .obj-icon { transform: scale(1.1); background-color: revert; }"""
text = text.replace(
    '.obj-card:hover .obj-icon .iconify { color: white !important; }',
    '.obj-card:hover .obj-icon .iconify { color: white !important; }' + ki_rules
)

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION REPLACEMENT HELPER
# ═══════════════════════════════════════════════════════════════════════════════

def replace_section(text, section_id, new_html):
    pattern = re.compile(
        rf'<section id="{re.escape(section_id)}"[^>]*>.*?</section>',
        re.DOTALL
    )
    result, count = pattern.subn(lambda m: new_html, text, count=1)
    status = "✅" if count else "⚠️  NOT FOUND"
    print(f"  {status} #{section_id}")
    return result

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION: OBJECTIVE (Check 1 — 4 cards with descriptions)
# ═══════════════════════════════════════════════════════════════════════════════

SECT_OBJECTIVE = """\
<section id="objective">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:bullseye"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Lesson Objective</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">What you will learn in this lesson</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:window-maximize"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Define what a data application is</p>
            <p class="text-xs text-gray-500 mt-0.5">Understand how data apps differ from static files and reports</p>
          </div>
        </div>
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:chart-column"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Explain why organizations choose data apps over static reports</p>
            <p class="text-xs text-gray-500 mt-0.5">Identify the limitations of emailing spreadsheets and PDFs</p>
          </div>
        </div>
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:arrows-spin"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Describe how data apps streamline analytics workflows</p>
            <p class="text-xs text-gray-500 mt-0.5">See how self-service tools eliminate repetitive analyst requests</p>
          </div>
        </div>
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:wrench"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Identify common Python frameworks for building data apps</p>
            <p class="text-xs text-gray-500 mt-0.5">Compare Streamlit, Dash, Shiny for Python, and Panel</p>
          </div>
        </div>
      </div>
      <div class="mt-5">
        <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">This lesson introduces <strong>data applications</strong> as a concept before you write any code &mdash; you will build your first Streamlit app in Lesson 2.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION: OVERVIEW (Check 3 — hook + analogy + 4 cards + tip)
# ═══════════════════════════════════════════════════════════════════════════════

SECT_OVERVIEW = """\
<section id="overview">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:binoculars"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Overview</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">A high-level look at data applications and why they matter</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-5">

      <!-- Part 1 — Hook quote -->
      <div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
        <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Py</span>
        <div class="relative flex items-start gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
            <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>
          </span>
          <p class="text-base text-gray-800 leading-relaxed font-medium">A data application is a web-based tool that lets users interact with live data through filters, charts, and tables &mdash; no coding or SQL required.</p>
        </div>
      </div>

      <!-- Part 2 — Analogy intro -->
      <p class="text-sm text-gray-600 leading-relaxed">Think of a data application like a self-service ordering kiosk at a fast-food restaurant. A static report is like reading a printed menu on the wall &mdash; you can see the options, but you cannot customize your order or watch the total update in real time. A data application gives you a touchscreen where you tap categories, add items, see your running total change instantly, and send the order straight to the kitchen.</p>

      <!-- Part 3 — Analogy card grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-base" data-icon="fa6-solid:window-maximize"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Data Application</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The touchscreen kiosk &mdash; a self-service interface for your data</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">A data application is a web page backed by live data that lets users filter rows, generate charts, and download results on their own. You open it in a browser, interact with widgets like dropdowns and sliders, and the page updates instantly without anyone rewriting a query or resending a file.</p>
        </div>
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-base" data-icon="fa6-solid:file-lines"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Static Reports</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The printed menu &mdash; fixed information that cannot answer new questions</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">A static report is a snapshot of data frozen at the moment it was exported &mdash; an Excel file, a PDF, or an emailed spreadsheet. The moment a stakeholder asks &ldquo;What about Q3?&rdquo; or &ldquo;Filter by the West region,&rdquo; someone has to rerun the query, rebuild the file, and send it again.</p>
        </div>
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-base" data-icon="fa6-solid:arrows-spin"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Interactive Analytics</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The customization screen &mdash; tap to filter, sort, and explore instantly</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">Interactive analytics means the user can change what they see without waiting for an analyst. You select a region from a dropdown, drag a date slider, or click a chart bar to drill down &mdash; and the dashboard recalculates on the fly, freeing analysts from repetitive ad-hoc requests.</p>
        </div>
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-base" data-icon="fa6-solid:wrench"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Python Frameworks</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The kiosk software &mdash; Streamlit, Dash, and Shiny power the screen</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">Python frameworks like Streamlit, Dash, Shiny for Python, and Panel let you build a full data app using only Python &mdash; no HTML, CSS, or JavaScript required. You write a regular Python script, and the framework turns it into a web page with widgets, charts, and tables that anyone can use in a browser.</p>
        </div>
      </div>

      <!-- Part 4 — Closing tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">Even if you never build a data app yourself, understanding what they are helps you communicate requirements to developers and evaluate which tool fits your team&rsquo;s needs.</p>
      </div>

    </div>
  </div>
</section>"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION: KEY IDEAS (Check 4 — 2-column grid, 4 cards)
# ═══════════════════════════════════════════════════════════════════════════════

SECT_KEY_IDEAS = """\
<section id="key-ideas">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:lightbulb"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Takeaways</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">The most important ideas to remember</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">

        <!-- Card 0 — pink -->
        <div class="obj-card rounded-2xl border border-gray-100 bg-white overflow-hidden shadow-sm">
          <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
          <div class="px-5 py-5 space-y-3 bg-white">
            <div class="flex items-center gap-3">
              <span class="obj-icon inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
                <span class="iconify text-white text-sm" data-icon="fa6-solid:clock-rotate-left"></span>
              </span>
              <h3 class="text-sm font-bold text-gray-900">Static Reports Become Stale the Moment They Are Exported</h3>
            </div>
            <p class="text-sm text-gray-600 leading-relaxed">A static report captures data at a single point in time, so any question about the latest numbers requires someone to re-run the query and re-send the file. A data application stays connected to the source, which means charts and tables always reflect the most recent data without any manual refresh.</p>
            <div class="flex flex-wrap gap-2">
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Real-time Data</span>
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Self-Service</span>
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">No Re-export</span>
            </div>
          </div>
        </div>

        <!-- Card 1 — violet -->
        <div class="obj-card rounded-2xl border border-violet-100 bg-white overflow-hidden shadow-sm">
          <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
          <div class="px-5 py-5 space-y-3 bg-white">
            <div class="flex items-center gap-3">
              <span class="obj-icon inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
                <span class="iconify text-white text-sm" data-icon="fa6-solid:users"></span>
              </span>
              <h3 class="text-sm font-bold text-gray-900">Self-Service Tools Eliminate Repeated Analyst Requests</h3>
            </div>
            <p class="text-sm text-gray-600 leading-relaxed">Without a data app, every &ldquo;Can you filter by region?&rdquo; or &ldquo;Show me Q3 numbers&rdquo; request lands on an analyst&rsquo;s desk, creating a backlog that delays decisions. When users can apply their own filters and drill-downs, analysts are freed to focus on deeper, more strategic analysis.</p>
            <div class="flex flex-wrap gap-2">
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Filter Widgets</span>
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Ad-Hoc Queries</span>
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Analyst Time</span>
            </div>
          </div>
        </div>

        <!-- Card 2 — blue -->
        <div class="obj-card rounded-2xl border border-blue-100 bg-white overflow-hidden shadow-sm">
          <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>
          <div class="px-5 py-5 space-y-3 bg-white">
            <div class="flex items-center gap-3">
              <span class="obj-icon inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">
                <span class="iconify text-white text-sm" data-icon="fa6-solid:wand-magic-sparkles"></span>
              </span>
              <h3 class="text-sm font-bold text-gray-900">Python Frameworks Turn Scripts into Web Pages</h3>
            </div>
            <p class="text-sm text-gray-600 leading-relaxed">Streamlit, Dash, Shiny for Python, and Panel all convert a standard Python script into a browser-based interface &mdash; you do not need to learn HTML, CSS, or JavaScript. This means the same person who writes pandas code to clean data can also build the front-end that stakeholders use to explore it.</p>
            <div class="flex flex-wrap gap-2">
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Streamlit</span>
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Dash</span>
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Shiny</span>
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Panel</span>
            </div>
          </div>
        </div>

        <!-- Card 3 — emerald -->
        <div class="obj-card rounded-2xl border border-emerald-100 bg-white overflow-hidden shadow-sm">
          <div class="h-1 bg-gradient-to-r from-emerald-500 to-teal-400"></div>
          <div class="px-5 py-5 space-y-3 bg-white">
            <div class="flex items-center gap-3">
              <span class="obj-icon inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shrink-0 shadow-md">
                <span class="iconify text-white text-sm" data-icon="fa6-solid:handshake"></span>
              </span>
              <h3 class="text-sm font-bold text-gray-900">Data Apps Bridge the Gap Between Data Teams and Business Users</h3>
            </div>
            <p class="text-sm text-gray-600 leading-relaxed">Business users often cannot write SQL or Python, so they depend on analysts to answer every data question. A data application gives those users a point-and-click interface to explore data themselves, which shortens the feedback loop from &ldquo;days waiting for a report&rdquo; to &ldquo;seconds clicking a filter.&rdquo;</p>
            <div class="flex flex-wrap gap-2">
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-600 border border-emerald-100">Business Users</span>
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-600 border border-emerald-100">Point-and-Click</span>
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-600 border border-emerald-100">Decision Speed</span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</section>"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION: KEY CONCEPTS (Check 5 — 4 tabs with code, tips, tables)
# ═══════════════════════════════════════════════════════════════════════════════

SECT_KEY_CONCEPTS = """\
<section id="key-concepts">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:book-open"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Concepts</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Core terms and how they work in practice</p>
      </div>
    </div>
    <div class="bg-white px-6 py-7">
      <div class="flex flex-col md:flex-row gap-0">
        <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">
          <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full bg-[#CB187D] transition-all duration-300" style="height:68px;"></div>
          <button onclick="switchKcTab(0)" class="kc-tab kc-tab-active group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-[#CB187D] text-white shadow-sm shadow-pink-200"><span class="iconify text-[11px]" data-icon="fa6-solid:window-maximize"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-900">Data Applications</span>
          </button>
          <button onclick="switchKcTab(1)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:file-lines"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Static vs Interactive</span>
          </button>
          <button onclick="switchKcTab(2)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:arrows-spin"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Interactive Analytics</span>
          </button>
          <button onclick="switchKcTab(3)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 bg-gray-100 text-gray-400"><span class="iconify text-[11px]" data-icon="fa6-solid:wrench"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Python Frameworks</span>
          </button>
        </div>
        <div class="flex-1 min-w-0 md:pl-5">

          <!-- KC Panel 0 — pink: Data Applications -->
          <div class="kc-panel kc-panel-anim" data-color="pink" role="tabpanel">
            <div class="rounded-2xl border border-pink-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-[#CB187D] via-pink-400 to-rose-300"></div>
              <div class="bg-gradient-to-br from-pink-50/60 to-white p-5 space-y-4">
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:window-maximize"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Data Applications</h3>
                      <p class="text-[10px] text-gray-400">Web-based interactive data tools</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-pink-100 to-rose-100 text-[#CB187D]">Core Concept</span>
                </div>
                <p class="text-sm text-gray-600 leading-relaxed">A data application is a web-based tool that connects directly to a data source and renders an interactive interface &mdash; tables, charts, and filter widgets &mdash; in the user&rsquo;s browser. Unlike a static file that you email or share on a drive, a data app stays live: when the underlying data changes, the app reflects those changes the next time a user opens it.</p>
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Python</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">import streamlit as st  # Framework that turns this script into a web app
import pandas as pd      # Data manipulation library

# Load data from a CSV file into a DataFrame
data = pd.read_csv("sales.csv")

# Render a title at the top of the web page
st.title("Sales Dashboard")

# Display the DataFrame as a scrollable, sortable table
st.dataframe(data)</code></pre>
                </div>
                <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                  <p class="text-sm text-gray-600">Streamlit re-runs your entire script from top to bottom every time a user interacts with a widget, so keep heavy data loading behind <code class="font-mono text-xs bg-pink-50 text-[#CB187D] px-1 py-0.5 rounded">@st.cache_data</code> to avoid slow reloads.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- KC Panel 1 — violet: Static vs Interactive -->
          <div class="kc-panel kc-panel-anim hidden" data-color="violet" role="tabpanel">
            <div class="rounded-2xl border border-violet-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-violet-500 via-purple-400 to-fuchsia-300"></div>
              <div class="bg-gradient-to-br from-violet-50/60 to-white p-5 space-y-4">
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:file-lines"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Static Reports vs Data Apps</h3>
                      <p class="text-[10px] text-gray-400">Why fixed snapshots fall short</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-violet-100 to-purple-100 text-violet-600">Comparison</span>
                </div>
                <p class="text-sm text-gray-600 leading-relaxed">A static report is a fixed snapshot &mdash; an Excel file, a PDF, or an emailed CSV &mdash; that captures data at the moment it was generated. A data application, by contrast, queries the source each time a user opens it and lets them filter, sort, and drill down without re-exporting anything.</p>
                <div class="rounded-xl border border-violet-100 overflow-hidden">
                  <table class="w-full text-sm">
                    <thead><tr class="bg-violet-50 text-violet-600">
                      <th class="px-4 py-2 text-left text-xs font-bold">Feature</th>
                      <th class="px-4 py-2 text-left text-xs font-bold">Static Report</th>
                      <th class="px-4 py-2 text-left text-xs font-bold">Data App</th>
                    </tr></thead>
                    <tbody class="text-xs text-gray-600">
                      <tr class="border-t border-gray-100"><td class="px-4 py-2 font-medium">Data freshness</td><td class="px-4 py-2">Frozen at export time</td><td class="px-4 py-2">Live or near-live</td></tr>
                      <tr class="border-t border-gray-100"><td class="px-4 py-2 font-medium">Filtering</td><td class="px-4 py-2">Re-run query manually</td><td class="px-4 py-2">Click a dropdown</td></tr>
                      <tr class="border-t border-gray-100"><td class="px-4 py-2 font-medium">Sharing</td><td class="px-4 py-2">Email / shared drive</td><td class="px-4 py-2">URL link</td></tr>
                      <tr class="border-t border-gray-100"><td class="px-4 py-2 font-medium">User skill needed</td><td class="px-4 py-2">Open a file</td><td class="px-4 py-2">Open a browser</td></tr>
                    </tbody>
                  </table>
                </div>
                <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                  <p class="text-sm text-gray-600">Static reports are still useful when you need a permanent record (an audit trail or a board-deck PDF). The goal is not to eliminate them but to stop using them as the only way stakeholders access data.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- KC Panel 2 — blue: Interactive Analytics -->
          <div class="kc-panel kc-panel-anim hidden" data-color="blue" role="tabpanel">
            <div class="rounded-2xl border border-blue-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-blue-500 via-cyan-400 to-teal-300"></div>
              <div class="bg-gradient-to-br from-blue-50/60 to-white p-5 space-y-4">
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:arrows-spin"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Interactive Analytics</h3>
                      <p class="text-[10px] text-gray-400">Filters, widgets, and real-time updates</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-blue-100 to-indigo-100 text-blue-600">Workflow</span>
                </div>
                <p class="text-sm text-gray-600 leading-relaxed">Interactive analytics means users can change what they see &mdash; filtering rows, selecting date ranges, or clicking chart elements &mdash; and the display updates instantly without anyone rewriting code. In Streamlit, every widget (dropdown, slider, checkbox) is a single function call that returns the user&rsquo;s current selection.</p>
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Python</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python"># Create a dropdown widget populated from the data itself
region = st.selectbox("Region", data["region"].unique())

# Filter the DataFrame to matching rows
filtered = data[data["region"] == region]

# Render a bar chart of sales by product for the selected region
st.bar_chart(filtered.set_index("product")["sales"])</code></pre>
                </div>
                <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                  <p class="text-sm text-gray-600">Always populate dropdown options from the data itself (<code class="font-mono text-xs bg-blue-50 text-blue-700 px-1 py-0.5 rounded">data["region"].unique()</code>) rather than hard-coding a list &mdash; this way the filter stays correct even when new categories appear in the dataset.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- KC Panel 3 — emerald: Python Frameworks -->
          <div class="kc-panel kc-panel-anim hidden" data-color="emerald" role="tabpanel">
            <div class="rounded-2xl border border-emerald-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-emerald-500 via-teal-400 to-cyan-300"></div>
              <div class="bg-gradient-to-br from-emerald-50/60 to-white p-5 space-y-4">
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shrink-0 shadow-md">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:wrench"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Python Data App Frameworks</h3>
                      <p class="text-[10px] text-gray-400">Choosing the right tool for the job</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-emerald-100 to-teal-100 text-emerald-600">Tooling</span>
                </div>
                <p class="text-sm text-gray-600 leading-relaxed">Several Python frameworks let you build data applications without writing any HTML, CSS, or JavaScript. Each framework has a different philosophy: Streamlit uses a top-to-bottom script model, Dash uses a callback model inspired by React, Shiny for Python uses a reactive model borrowed from R, and Panel integrates tightly with the HoloViz ecosystem.</p>
                <div class="rounded-xl border border-emerald-100 overflow-hidden">
                  <table class="w-full text-sm">
                    <thead><tr class="bg-emerald-50 text-emerald-600">
                      <th class="px-4 py-2 text-left text-xs font-bold">Framework</th>
                      <th class="px-4 py-2 text-left text-xs font-bold">Model</th>
                      <th class="px-4 py-2 text-left text-xs font-bold">Best For</th>
                    </tr></thead>
                    <tbody class="text-xs text-gray-600">
                      <tr class="border-t border-gray-100"><td class="px-4 py-2 font-medium">Streamlit</td><td class="px-4 py-2">Script (top-to-bottom)</td><td class="px-4 py-2">Fast prototyping, simple dashboards</td></tr>
                      <tr class="border-t border-gray-100"><td class="px-4 py-2 font-medium">Dash</td><td class="px-4 py-2">Callbacks (Plotly-based)</td><td class="px-4 py-2">Complex multi-page apps</td></tr>
                      <tr class="border-t border-gray-100"><td class="px-4 py-2 font-medium">Shiny for Python</td><td class="px-4 py-2">Reactive (R-style)</td><td class="px-4 py-2">Teams familiar with R Shiny</td></tr>
                      <tr class="border-t border-gray-100"><td class="px-4 py-2 font-medium">Panel</td><td class="px-4 py-2">Widget-based (HoloViz)</td><td class="px-4 py-2">Scientific / notebook-first workflows</td></tr>
                    </tbody>
                  </table>
                </div>
                <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                  <p class="text-sm text-gray-600">If you are new to data apps, start with Streamlit &mdash; its script-based model is the easiest to learn, and you can have a working prototype running in your browser in under 30 minutes.</p>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
</section>"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION: CODE EXAMPLES (Check 12a — 4 tabs, Style A + terminal pane)
# ═══════════════════════════════════════════════════════════════════════════════

SECT_CODE_EXAMPLES = """\
<section id="code-examples">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:code"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Code Examples</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Hands-on code snippets to explore the concepts</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-2 mb-6" role="tablist">
        <button onclick="switchCeTab(0)" class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code"></span><span class="ce-step-label text-xs font-bold">Basic App</span></button>
        <button onclick="switchCeTab(1)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code"></span><span class="ce-step-label text-xs font-bold">Add Filter</span></button>
        <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code"></span><span class="ce-step-label text-xs font-bold">Add Chart</span></button>
        <button onclick="switchCeTab(3)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code"></span><span class="ce-step-label text-xs font-bold">Export Data</span></button>
      </div>

      <!-- CE Panel 0 -->
      <div class="ce-panel ce-panel-anim" role="tabpanel">
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">basic_app.py</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code"><pre class="overflow-x-auto pre-reset"><code class="language-python">import streamlit as st    # Import the Streamlit framework
import pandas as pd        # Import pandas for data handling

# Load sales data from a CSV file into a DataFrame
data = pd.read_csv("sales.csv")

# Display the app title in the browser
st.title("Sales Dashboard")

# Show the first 10 rows as a scrollable table
st.dataframe(data.head(10))</code></pre></div>
          <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
            <div class="flex items-center gap-2 mb-1.5">
              <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
              <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
              <span class="text-[10px] text-gray-600 font-mono">$ streamlit run basic_app.py</span>
            </div>
            <div class="font-mono text-xs text-emerald-400 leading-relaxed">  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501</div>
          </div>
        </div>
        <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">Streamlit launches a local web server and opens a browser tab automatically. Every time you save the script, the page refreshes to show your changes.</p>
        </div>
      </div>

      <!-- CE Panel 1 -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">filter_app.py</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code"><pre class="overflow-x-auto pre-reset"><code class="language-python">import streamlit as st
import pandas as pd

data = pd.read_csv("sales.csv")
st.title("Sales Dashboard")

# Create a dropdown that lists every unique region from the dataset
region = st.selectbox("Select Region", data["region"].unique())

# Filter the DataFrame to only rows matching the selected region
filtered = data[data["region"] == region]

# Display the filtered results as a table
st.dataframe(filtered)</code></pre></div>
          <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
            <div class="flex items-center gap-2 mb-1.5">
              <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
              <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
              <span class="text-[10px] text-gray-600 font-mono">$ streamlit run filter_app.py</span>
            </div>
            <div class="font-mono text-xs text-emerald-400 leading-relaxed">  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501</div>
          </div>
        </div>
        <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">When the user selects a different region, Streamlit re-runs the script from top to bottom and the table shows only matching rows &mdash; no page reload required.</p>
        </div>
      </div>

      <!-- CE Panel 2 -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">chart_app.py</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code"><pre class="overflow-x-auto pre-reset"><code class="language-python">import streamlit as st
import pandas as pd

data = pd.read_csv("sales.csv")
st.title("Sales Dashboard")

region = st.selectbox("Select Region", data["region"].unique())
filtered = data[data["region"] == region]

# Display a bar chart of sales by product for the selected region
st.bar_chart(filtered.set_index("product")["sales"])

# Show a metric card with the total sales value
st.metric("Total Sales", f"${filtered['sales'].sum():,.0f}")</code></pre></div>
          <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
            <div class="flex items-center gap-2 mb-1.5">
              <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
              <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
              <span class="text-[10px] text-gray-600 font-mono">$ streamlit run chart_app.py</span>
            </div>
            <div class="font-mono text-xs text-emerald-400 leading-relaxed">  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501</div>
          </div>
        </div>
        <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">The chart and metric update automatically when the user picks a different region. This is the core benefit of a data app &mdash; stakeholders explore the data themselves instead of waiting for a new export.</p>
        </div>
      </div>

      <!-- CE Panel 3 -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">export_app.py</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code"><pre class="overflow-x-auto pre-reset"><code class="language-python">import streamlit as st
import pandas as pd

data = pd.read_csv("sales.csv")
st.title("Sales Dashboard")

region = st.selectbox("Select Region", data["region"].unique())
filtered = data[data["region"] == region]
st.dataframe(filtered)

# Add a download button that exports the filtered data as CSV
st.download_button(
    label="Download Filtered Data",         # Button text
    data=filtered.to_csv(index=False),      # Convert DataFrame to CSV string
    file_name="filtered_sales.csv",         # Default filename for download
    mime="text/csv"                         # File type
)</code></pre></div>
          <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
            <div class="flex items-center gap-2 mb-1.5">
              <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
              <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
              <span class="text-[10px] text-gray-600 font-mono">$ streamlit run export_app.py</span>
            </div>
            <div class="font-mono text-xs text-emerald-400 leading-relaxed">  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501</div>
          </div>
        </div>
        <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">The download button lets users export exactly the filtered subset they need. This replaces the old workflow of asking an analyst to rerun a query and email the results.</p>
        </div>
      </div>

    </div>
  </div>
</section>"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION: COMPARISON (Check 7 — 4 labeled rows)
# ═══════════════════════════════════════════════════════════════════════════════

SECT_COMPARISON = """\
<section id="comparison">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:scale-balanced"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">SQL / Excel Comparison</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">How data app features map to tools you already know</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-5">

      <!-- Row 1: Data Display -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0"><span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:table"></span></span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">Data Display</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Python</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">st.dataframe(df)</code><p class="text-xs text-gray-500 leading-relaxed">Renders a scrollable, sortable table in the browser.</p></div>
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">SQL</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">SELECT * FROM sales</code><p class="text-xs text-gray-500 leading-relaxed">Returns rows in a text terminal or query editor.</p></div>
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Excel</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">Open file &rarr; view sheet</code><p class="text-xs text-gray-500 leading-relaxed">Data appears in a spreadsheet grid.</p></div>
        </div>
      </div>

      <div class="flex items-center gap-3 mb-4"><span class="flex-1 h-px bg-gray-100"></span><span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#fdf0f7] shrink-0"><span class="iconify text-[#CB187D] text-xs" data-icon="fa6-solid:scale-balanced"></span></span><span class="flex-1 h-px bg-gray-100"></span></div>

      <!-- Row 2: Filtering -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0"><span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:filter"></span></span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">Filtering</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Python</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">st.selectbox() + mask</code><p class="text-xs text-gray-500 leading-relaxed">Dropdown widget filters the DataFrame interactively.</p></div>
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">SQL</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">WHERE region = 'West'</code><p class="text-xs text-gray-500 leading-relaxed">Hard-coded filter written into the query text.</p></div>
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Excel</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">Data &rarr; Filter</code><p class="text-xs text-gray-500 leading-relaxed">Column-header dropdowns filter rows in place.</p></div>
        </div>
      </div>

      <div class="flex items-center gap-3 mb-4"><span class="flex-1 h-px bg-gray-100"></span><span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#fdf0f7] shrink-0"><span class="iconify text-[#CB187D] text-xs" data-icon="fa6-solid:scale-balanced"></span></span><span class="flex-1 h-px bg-gray-100"></span></div>

      <!-- Row 3: Charts -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0"><span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:chart-bar"></span></span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">Charts</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Python</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">st.bar_chart(df)</code><p class="text-xs text-gray-500 leading-relaxed">Renders an interactive chart from a DataFrame.</p></div>
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">SQL</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">n/a (needs BI tool)</code><p class="text-xs text-gray-500 leading-relaxed">SQL alone cannot render charts; requires a BI layer.</p></div>
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Excel</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">Insert &rarr; Chart</code><p class="text-xs text-gray-500 leading-relaxed">Creates a chart linked to the selected range.</p></div>
        </div>
      </div>

      <div class="flex items-center gap-3 mb-4"><span class="flex-1 h-px bg-gray-100"></span><span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#fdf0f7] shrink-0"><span class="iconify text-[#CB187D] text-xs" data-icon="fa6-solid:scale-balanced"></span></span><span class="flex-1 h-px bg-gray-100"></span></div>

      <!-- Row 4: Exporting -->
      <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
        <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0"><span class="iconify text-indigo-400 text-[11px]" data-icon="fa6-solid:file-arrow-down"></span></span>
          <span class="text-xs font-bold uppercase tracking-widest text-gray-400">Exporting</span>
        </div>
        <div class="grid grid-cols-3 divide-x divide-gray-100">
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Python</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">st.download_button()</code><p class="text-xs text-gray-500 leading-relaxed">Lets users download filtered data as CSV with one click.</p></div>
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">SQL</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">\\COPY ... TO 'file.csv'</code><p class="text-xs text-gray-500 leading-relaxed">Exports query results to a file on the server.</p></div>
          <div class="px-4 py-4 flex flex-col gap-2"><span class="text-xs text-gray-400">Excel</span><code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">File &rarr; Save As &rarr; CSV</code><p class="text-xs text-gray-500 leading-relaxed">Saves the current sheet as a CSV file.</p></div>
        </div>
      </div>

    </div>
  </div>
</section>"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION: PRACTICE (Check 12b — 4 tabs with task-box + solutions)
# ═══════════════════════════════════════════════════════════════════════════════

SECT_PRACTICE = """\
<section id="practice">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:pencil"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Practice Exercises</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Guided exercises to reinforce your learning</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-2 mb-6" role="tablist">
        <button onclick="switchPeTab(0)" class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span><span class="pe-step-label text-xs font-bold">Create App</span></button>
        <button onclick="switchPeTab(1)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span><span class="pe-step-label text-xs font-bold">Load Data</span></button>
        <button onclick="switchPeTab(2)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span><span class="pe-step-label text-xs font-bold">Add Filter</span></button>
        <button onclick="switchPeTab(3)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span><span class="pe-step-label text-xs font-bold">Chart + Export</span></button>
      </div>

      <!-- PE Panel 0 -->
      <div class="pe-panel pe-panel-anim" role="tabpanel">
        <div class="rounded-xl p-4 task-box space-y-2">
          <p class="text-xs font-bold uppercase tracking-widest text-brand">Your Task</p>
          <ol class="list-decimal list-inside text-sm text-gray-600 space-y-1">
            <li>Create a new file called <code class="font-mono text-xs">app.py</code>.</li>
            <li>Import <code class="font-mono text-xs">streamlit</code> and give your app a title using <code class="font-mono text-xs">st.title()</code>.</li>
            <li>Add a subtitle with <code class="font-mono text-xs">st.write("Welcome to my first data app")</code>.</li>
            <li>Run the app with <code class="font-mono text-xs">streamlit run app.py</code> in your terminal.</li>
          </ol>
        </div>
        <button class="accordion-toggle w-full mt-3" onclick="toggleAccordion(this)"><span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Solution<span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span></button>
        <div class="accordion-body">
          <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-3">
            <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
              <div class="flex items-center gap-3"><div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5"><span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span><span class="text-[11px] font-semibold text-gray-400">app.py</span></div></div>
              <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
            </div>
            <div class="bg-code"><pre class="overflow-x-auto pre-reset"><code class="language-python">import streamlit as st  # Import Streamlit

st.title("My First Data App")              # App heading
st.write("Welcome to my first data app")   # Subtitle text</code></pre></div>
          </div>
          <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
            <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
            <p class="text-sm text-gray-600">This exercise proves that a working data app can be as short as three lines of Python.</p>
          </div>
        </div>
      </div>

      <!-- PE Panel 1 -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="rounded-xl p-4 task-box space-y-2">
          <p class="text-xs font-bold uppercase tracking-widest text-brand">Your Task</p>
          <ol class="list-decimal list-inside text-sm text-gray-600 space-y-1">
            <li>Import <code class="font-mono text-xs">pandas</code> and load <code class="font-mono text-xs">sales.csv</code> into a DataFrame.</li>
            <li>Display the full DataFrame using <code class="font-mono text-xs">st.dataframe(data)</code>.</li>
            <li>Add <code class="font-mono text-xs">st.write(f"Total rows: {len(data)}")</code> to show the row count.</li>
          </ol>
        </div>
        <button class="accordion-toggle w-full mt-3" onclick="toggleAccordion(this)"><span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Solution<span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span></button>
        <div class="accordion-body">
          <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-3">
            <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
              <div class="flex items-center gap-3"><div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5"><span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span><span class="text-[11px] font-semibold text-gray-400">solution_2.py</span></div></div>
              <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
            </div>
            <div class="bg-code"><pre class="overflow-x-auto pre-reset"><code class="language-python">import streamlit as st
import pandas as pd

data = pd.read_csv("sales.csv")     # Load the CSV into a DataFrame

st.title("Sales Dashboard")
st.dataframe(data)                   # Render the table in the browser
st.write(f"Total rows: {len(data)}") # Show row count below the table</code></pre></div>
          </div>
          <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
            <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
            <p class="text-sm text-gray-600">In a real project you would wrap <code class="font-mono text-xs">pd.read_csv()</code> inside <code class="font-mono text-xs">@st.cache_data</code> so the file is only loaded once, not on every widget interaction.</p>
          </div>
        </div>
      </div>

      <!-- PE Panel 2 -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="rounded-xl p-4 task-box space-y-2">
          <p class="text-xs font-bold uppercase tracking-widest text-brand">Your Task</p>
          <ol class="list-decimal list-inside text-sm text-gray-600 space-y-1">
            <li>Create a dropdown with <code class="font-mono text-xs">st.selectbox()</code> that lists unique regions from the data.</li>
            <li>Filter the DataFrame to only show rows matching the selected region.</li>
            <li>Display the filtered DataFrame below the dropdown.</li>
          </ol>
        </div>
        <button class="accordion-toggle w-full mt-3" onclick="toggleAccordion(this)"><span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Solution<span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span></button>
        <div class="accordion-body">
          <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-3">
            <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
              <div class="flex items-center gap-3"><div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5"><span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span><span class="text-[11px] font-semibold text-gray-400">solution_3.py</span></div></div>
              <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
            </div>
            <div class="bg-code"><pre class="overflow-x-auto pre-reset"><code class="language-python">import streamlit as st
import pandas as pd

data = pd.read_csv("sales.csv")
st.title("Sales Dashboard")

# Dropdown populated from the dataset
region = st.selectbox("Select Region", data["region"].unique())

# Boolean mask filters to matching rows
filtered = data[data["region"] == region]

st.dataframe(filtered)</code></pre></div>
          </div>
          <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
            <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
            <p class="text-sm text-gray-600">Using <code class="font-mono text-xs">data["region"].unique()</code> ensures the dropdown always matches the real data, even if new regions are added later.</p>
          </div>
        </div>
      </div>

      <!-- PE Panel 3 -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="rounded-xl p-4 task-box space-y-2">
          <p class="text-xs font-bold uppercase tracking-widest text-brand">Your Task</p>
          <ol class="list-decimal list-inside text-sm text-gray-600 space-y-1">
            <li>Add <code class="font-mono text-xs">st.bar_chart()</code> to visualize sales by product for the filtered data.</li>
            <li>Add a <code class="font-mono text-xs">st.download_button()</code> that exports the filtered data as CSV.</li>
            <li>Test the app by selecting different regions and downloading the results.</li>
          </ol>
        </div>
        <button class="accordion-toggle w-full mt-3" onclick="toggleAccordion(this)"><span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Solution<span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span></button>
        <div class="accordion-body">
          <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-3">
            <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
              <div class="flex items-center gap-3"><div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5"><span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span><span class="text-[11px] font-semibold text-gray-400">solution_4.py</span></div></div>
              <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
            </div>
            <div class="bg-code"><pre class="overflow-x-auto pre-reset"><code class="language-python">import streamlit as st
import pandas as pd

data = pd.read_csv("sales.csv")
st.title("Sales Dashboard")

region = st.selectbox("Select Region", data["region"].unique())
filtered = data[data["region"] == region]

# Bar chart showing sales by product
st.bar_chart(filtered.set_index("product")["sales"])

# Download button for the filtered CSV
st.download_button(
    label="Download Filtered Data",
    data=filtered.to_csv(index=False),
    file_name="filtered_sales.csv",
    mime="text/csv"
)</code></pre></div>
          </div>
          <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
            <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
            <p class="text-sm text-gray-600">Combining a chart, a filter, and a download button gives you a complete mini-dashboard that replaces the old &ldquo;email me the report&rdquo; workflow.</p>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION: MISTAKES (Check 6 — 4 tabs with split panels)
# ═══════════════════════════════════════════════════════════════════════════════

SECT_MISTAKES = """\
<section id="mistakes">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:triangle-exclamation"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Common Mistakes</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Frequent errors and how to avoid them</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-2 mb-6" role="tablist">
        <button onclick="switchMkTab(0)" class="mk-step mk-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span><span class="mk-step-label text-xs font-bold">Hardcoded Filters</span></button>
        <button onclick="switchMkTab(1)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span><span class="mk-step-label text-xs font-bold">Lost Filter Result</span></button>
        <button onclick="switchMkTab(2)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span><span class="mk-step-label text-xs font-bold">No Caching</span></button>
        <button onclick="switchMkTab(3)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span><span class="mk-step-label text-xs font-bold">Too Much Data</span></button>
      </div>

      <!-- MK Panel 0 -->
      <div class="mk-panel mk-panel-anim" role="tabpanel">
        <p class="text-sm font-semibold text-gray-800 mb-2">Hardcoding filter values instead of reading from the data</p>
        <p class="text-sm text-gray-600 mb-4">Beginners often type out a list of filter options by hand, which breaks the moment the dataset adds a new category.</p>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div><p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong</p><div class="rounded-xl overflow-hidden bg-code"><pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># Hard-coded list misses new regions
region = st.selectbox("Region", ["East", "West", "North"])</code></pre></div></div>
          <div><p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-500 mb-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct</p><div class="rounded-xl overflow-hidden bg-code"><pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># Read options from the data — always up to date
region = st.selectbox("Region", data["region"].unique())</code></pre></div></div>
        </div>
        <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip"><span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span><p class="text-sm text-gray-600">Always use <code class="font-mono text-xs">.unique()</code> or <code class="font-mono text-xs">.nunique()</code> to populate widget options so the app stays correct as the data grows.</p></div>
      </div>

      <!-- MK Panel 1 -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <p class="text-sm font-semibold text-gray-800 mb-2">Forgetting to assign the filtered DataFrame</p>
        <p class="text-sm text-gray-600 mb-4">The filter expression runs but the result is never saved to a variable, so the table still shows unfiltered data.</p>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div><p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong</p><div class="rounded-xl overflow-hidden bg-code"><pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># Filter runs but result is discarded
data[data["region"] == region]
st.dataframe(data)  # Still shows ALL rows</code></pre></div></div>
          <div><p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-500 mb-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct</p><div class="rounded-xl overflow-hidden bg-code"><pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># Assign the result to a new variable
filtered = data[data["region"] == region]
st.dataframe(filtered)  # Shows only matching rows</code></pre></div></div>
        </div>
        <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip"><span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span><p class="text-sm text-gray-600">This is a silent bug &mdash; no error is raised, but the filter has no effect. Always assign the result of a filter expression to a variable before displaying it.</p></div>
      </div>

      <!-- MK Panel 2 -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <p class="text-sm font-semibold text-gray-800 mb-2">Not caching data loads</p>
        <p class="text-sm text-gray-600 mb-4">Streamlit re-runs the entire script on every widget interaction, so loading a large CSV without caching makes the app painfully slow.</p>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div><p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong</p><div class="rounded-xl overflow-hidden bg-code"><pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># Re-reads the CSV on every interaction
data = pd.read_csv("big_dataset.csv")</code></pre></div></div>
          <div><p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-500 mb-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct</p><div class="rounded-xl overflow-hidden bg-code"><pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">@st.cache_data  # Cache the result
def load_data():
    return pd.read_csv("big_dataset.csv")

data = load_data()  # Only reads once</code></pre></div></div>
        </div>
        <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip"><span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span><p class="text-sm text-gray-600">Use <code class="font-mono text-xs">@st.cache_data</code> for any function that loads or transforms data. Streamlit stores the result and skips the function on subsequent re-runs until the input changes.</p></div>
      </div>

      <!-- MK Panel 3 -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <p class="text-sm font-semibold text-gray-800 mb-2">Displaying too much data at once</p>
        <p class="text-sm text-gray-600 mb-4">Rendering millions of rows in a browser table makes the app freeze. Limit the displayed rows and offer a download for the full dataset.</p>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div><p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong</p><div class="rounded-xl overflow-hidden bg-code"><pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># Renders all 2 million rows — browser freezes
st.dataframe(data)</code></pre></div></div>
          <div><p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-500 mb-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct</p><div class="rounded-xl overflow-hidden bg-code"><pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># Show a manageable preview
st.dataframe(data.head(1000))
# Let users download the full dataset
st.download_button("Download All", data.to_csv())</code></pre></div></div>
        </div>
        <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip"><span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span><p class="text-sm text-gray-600">Show a preview with <code class="font-mono text-xs">.head(1000)</code> and provide a download button for the full file. Users get fast feedback and can still access all the data when they need it.</p></div>
      </div>

    </div>
  </div>
</section>"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION: RECAP (Check 8-9 — 4 cards + banner)
# ═══════════════════════════════════════════════════════════════════════════════

SECT_RECAP = """\
<section id="recap">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:list-check"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Lesson Recap</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">A quick summary of what you learned</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5"><span class="iconify text-sm" data-icon="fa6-solid:check"></span></span>
              <p class="text-sm text-gray-700 font-medium leading-relaxed">You learned that a data application is a web-based tool that lets users interact with live data through filters, charts, and tables.</p>
            </div>
          </div>
        </div>
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5"><span class="iconify text-sm" data-icon="fa6-solid:check"></span></span>
              <p class="text-sm text-gray-700 font-medium leading-relaxed">You learned why organizations prefer data apps over static reports &mdash; reports go stale instantly and generate constant re-export requests.</p>
            </div>
          </div>
        </div>
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5"><span class="iconify text-sm" data-icon="fa6-solid:check"></span></span>
              <p class="text-sm text-gray-700 font-medium leading-relaxed">You learned how data apps streamline analytics workflows by letting business users filter, chart, and export data without writing code.</p>
            </div>
          </div>
        </div>
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5"><span class="iconify text-sm" data-icon="fa6-solid:check"></span></span>
              <p class="text-sm text-gray-700 font-medium leading-relaxed">You learned that Streamlit, Dash, Shiny for Python, and Panel are the main Python frameworks for building data applications.</p>
            </div>
          </div>
        </div>
      </div>
      <div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">
        <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">&#10003;</span>
        <div class="relative flex items-center gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0"><span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span></span>
          <div>
            <p class="text-sm font-bold text-white">Lesson Complete!</p>
            <p class="text-xs text-white/80 mt-0.5">You&#39;ve covered 4 key concepts. Ready for the knowledge check?</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION: KNOWLEDGE CHECK (Check 12c — 4 application questions)
# ═══════════════════════════════════════════════════════════════════════════════

SECT_QUIZ = """\
<section id="knowledge-check">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:brain"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Knowledge Check</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5">Test your understanding before moving on</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-2 mb-6" role="tablist">
        <button onclick="switchQzTab(0)" class="qz-step qz-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 1</span></button>
        <button onclick="switchQzTab(1)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 2</span></button>
        <button onclick="switchQzTab(2)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 3</span></button>
        <button onclick="switchQzTab(3)" class="qz-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question 4</span></button>
      </div>

      <!-- Q1 — Multiple Choice -->
      <div class="qz-panel qz-panel-anim" role="tabpanel">
        <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q1</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md"><span class="iconify text-base" data-icon="fa6-solid:circle-question"></span></span>
              <div><h3 class="font-bold text-gray-800">Multiple Choice</h3><p class="text-xs text-gray-500 mt-0.5">Select the best answer</p></div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="quiz-question" data-qid="quiz-q0">
              <p class="text-sm font-semibold text-gray-800 mb-4">Which of the following best describes a data application?</p>
              <div class="space-y-2">
                <button class="quiz-btn w-full text-left px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 transition-colors" onclick="checkQuiz(this, false)">A static PDF report emailed weekly</button>
                <button class="quiz-btn w-full text-left px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 transition-colors" onclick="checkQuiz(this, true)">A web-based tool that lets users filter, chart, and explore data interactively</button>
                <button class="quiz-btn w-full text-left px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 transition-colors" onclick="checkQuiz(this, false)">A Python script that runs once and prints output to the terminal</button>
                <button class="quiz-btn w-full text-left px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 transition-colors" onclick="checkQuiz(this, false)">An Excel file stored on a shared drive</button>
              </div>
              <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
            </div>
          </div>
        </div>
      </div>

      <!-- Q2 — True/False -->
      <div class="qz-panel qz-panel-anim hidden" role="tabpanel">
        <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q2</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md"><span class="iconify text-base" data-icon="fa6-solid:circle-question"></span></span>
              <div><h3 class="font-bold text-gray-800">True or False</h3><p class="text-xs text-gray-500 mt-0.5">Select the correct answer</p></div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="quiz-question" data-qid="quiz-q1">
              <p class="text-sm font-semibold text-gray-800 mb-4">A data application requires users to know SQL in order to filter and explore data.</p>
              <div class="flex gap-3">
                <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 transition-colors" onclick="checkQuiz(this, false)"><span class="iconify mr-1.5" data-icon="fa6-solid:check"></span> True</button>
                <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 transition-colors" onclick="checkQuiz(this, true)"><span class="iconify mr-1.5" data-icon="fa6-solid:xmark"></span> False</button>
              </div>
              <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
            </div>
          </div>
        </div>
      </div>

      <!-- Q3 — Multiple Choice (application) -->
      <div class="qz-panel qz-panel-anim hidden" role="tabpanel">
        <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q3</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md"><span class="iconify text-base" data-icon="fa6-solid:circle-question"></span></span>
              <div><h3 class="font-bold text-gray-800">Multiple Choice</h3><p class="text-xs text-gray-500 mt-0.5">Select the best answer</p></div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="quiz-question" data-qid="quiz-q2">
              <p class="text-sm font-semibold text-gray-800 mb-4">A sales manager asks you for a new filtered view of Q3 revenue every Monday. What is the best long-term solution?</p>
              <div class="space-y-2">
                <button class="quiz-btn w-full text-left px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 transition-colors" onclick="checkQuiz(this, false)">Write a SQL query and email the CSV each week</button>
                <button class="quiz-btn w-full text-left px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 transition-colors" onclick="checkQuiz(this, true)">Build a data app where the manager can filter by quarter themselves</button>
                <button class="quiz-btn w-full text-left px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 transition-colors" onclick="checkQuiz(this, false)">Create a pivot table in Excel and share the file</button>
                <button class="quiz-btn w-full text-left px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 transition-colors" onclick="checkQuiz(this, false)">Set up a cron job that emails the report automatically</button>
              </div>
              <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
            </div>
          </div>
        </div>
      </div>

      <!-- Q4 — Multiple Choice (framework) -->
      <div class="qz-panel qz-panel-anim hidden" role="tabpanel">
        <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q4</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md"><span class="iconify text-base" data-icon="fa6-solid:circle-question"></span></span>
              <div><h3 class="font-bold text-gray-800">Multiple Choice</h3><p class="text-xs text-gray-500 mt-0.5">Select the best answer</p></div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="quiz-question" data-qid="quiz-q3">
              <p class="text-sm font-semibold text-gray-800 mb-4">Which Python framework lets you build a data app using only a regular Python script &mdash; no HTML, CSS, or JavaScript required?</p>
              <div class="space-y-2">
                <button class="quiz-btn w-full text-left px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 transition-colors" onclick="checkQuiz(this, false)">Django</button>
                <button class="quiz-btn w-full text-left px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 transition-colors" onclick="checkQuiz(this, false)">Flask</button>
                <button class="quiz-btn w-full text-left px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 transition-colors" onclick="checkQuiz(this, true)">Streamlit</button>
                <button class="quiz-btn w-full text-left px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 transition-colors" onclick="checkQuiz(this, false)">FastAPI</button>
              </div>
              <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION: NEXT LESSON (canonical template format)
# ═══════════════════════════════════════════════════════════════════════════════

SECT_NEXT_LESSON = """\
<section id="next-lesson" class="scroll-mt-24">
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
          <span class="text-white font-bold text-lg">2</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module 5 &middot; Lesson 2</p>
          <h3 class="text-base font-bold text-gray-800">Introduction to Streamlit</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0"><span class="iconify text-white text-sm" data-icon="fa6-solid:play"></span></span>
            <div><p class="text-sm font-semibold text-gray-700">Install &amp; run Streamlit</p></div>
          </div>
          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0"><span class="iconify text-white text-sm" data-icon="fa6-solid:puzzle-piece"></span></span>
            <div><p class="text-sm font-semibold text-gray-700">Core Streamlit widgets</p></div>
          </div>
          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0"><span class="iconify text-white text-sm" data-icon="fa6-solid:sitemap"></span></span>
            <div><p class="text-sm font-semibold text-gray-700">App layout &amp; structure</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""

# ═══════════════════════════════════════════════════════════════════════════════
# APPLY ALL REPLACEMENTS
# ═══════════════════════════════════════════════════════════════════════════════

print(f"Patching {FILE}...\n")

sections = [
    ('objective', SECT_OBJECTIVE),
    ('overview', SECT_OVERVIEW),
    ('key-ideas', SECT_KEY_IDEAS),
    ('key-concepts', SECT_KEY_CONCEPTS),
    ('code-examples', SECT_CODE_EXAMPLES),
    ('comparison', SECT_COMPARISON),
    ('practice', SECT_PRACTICE),
    ('mistakes', SECT_MISTAKES),
    ('recap', SECT_RECAP),
    ('knowledge-check', SECT_QUIZ),
    ('next-lesson', SECT_NEXT_LESSON),
]

for sid, html in sections:
    text = replace_section(text, sid, html)

# ═══════════════════════════════════════════════════════════════════════════════
# FIX HERO PILL COUNTS (Check 2)
# ═══════════════════════════════════════════════════════════════════════════════

# Update "4 Examples" pill to match 4 CE tabs ✓
# Update "3 Exercises" pill to "4 Exercises" (now 4 practice tabs)
text = text.replace(
    '<span class="font-extrabold">3</span><span class="font-semibold opacity-55">Exercises</span>',
    '<span class="font-extrabold">4</span><span class="font-semibold opacity-55">Exercises</span>'
)

# ═══════════════════════════════════════════════════════════════════════════════
# WRITE RESULT
# ═══════════════════════════════════════════════════════════════════════════════

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(text)

new_len = len(text)
diff = new_len - original_len
sign = '+' if diff >= 0 else ''
print(f"\nDone. {sign}{diff} chars (was {original_len}, now {new_len})")

# Quick div balance check
opens = len(re.findall(r'<div[\s>]', text))
closes = text.count('</div>')
print(f"Div balance: open={opens} close={closes} diff={opens - closes}")
