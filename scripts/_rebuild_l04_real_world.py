"""
Replace <section id="real-world"> in lesson04.
3 real-world use cases using ReportRunner pattern.
No ClaimsPipeline / DataPipeline / healthcare.
Scenarios: sales report, web scraper, file processor.
"""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_SECTION = '''<section id="real-world" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:briefcase"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Real-World Applications</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Where you will use this refactoring pattern in professional Python projects</p>
      </div>
    </div>

    <div class="bg-white px-8 py-7 space-y-6">

      <p class="text-sm text-gray-600 leading-relaxed">Refactoring scripts into classes is not just a coding exercise — it is the natural next step any time a working script starts to grow. You will encounter this pattern constantly in professional Python work, across every domain from data analysis to automation to web development.</p>

      <!-- Three use-case cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">

        <!-- Card 1 — Sales report runner -->
        <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="h-1 bg-gradient-to-r from-[#CB187D] to-[#e84aad]"></div>
          <div class="px-5 py-5">
            <div class="flex items-center gap-3 mb-3">
              <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shrink-0 shadow-md">
                <span class="iconify text-white text-sm" data-icon="fa6-solid:chart-bar"></span>
              </span>
              <div>
                <p class="text-sm font-bold text-gray-800">Sales Report Runner</p>
                <p class="text-[10px] text-gray-400 italic leading-tight">Daily automation — runs on a schedule</p>
              </div>
            </div>
            <p class="text-xs text-gray-500 leading-relaxed mb-3">A loose script that generates daily sales summaries gets refactored into a <code class="font-mono text-[10px] bg-gray-100 px-1 py-0.5 rounded border border-gray-200">SalesReporter</code> class. The same structure — load, clean, save — applies here, and the class makes it easy to swap out the data source or add new steps later.</p>
            <div class="flex flex-wrap gap-1.5">
              <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Automation</span>
              <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold bg-pink-50 text-[#CB187D] border border-pink-100">Scheduling</span>
            </div>
          </div>
        </div>

        <!-- Card 2 — Web scraper -->
        <div class="rounded-2xl border border-violet-100 overflow-hidden shadow-sm hover:shadow-md hover:border-violet-200 transition-all duration-300">
          <div class="h-1 bg-gradient-to-r from-violet-500 to-purple-400"></div>
          <div class="px-5 py-5">
            <div class="flex items-center gap-3 mb-3">
              <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shrink-0 shadow-md">
                <span class="iconify text-white text-sm" data-icon="fa6-solid:spider"></span>
              </span>
              <div>
                <p class="text-sm font-bold text-gray-800">Web Scraper</p>
                <p class="text-[10px] text-gray-400 italic leading-tight">Fetch, parse, save — same pattern</p>
              </div>
            </div>
            <p class="text-xs text-gray-500 leading-relaxed mb-3">Web scrapers follow a fixed sequence: fetch the page, parse the content, save the results. Wrapping these steps inside a class means you can scrape different URLs without rewriting the logic — create a new object for each target and call <code class="font-mono text-[10px] bg-gray-100 px-1 py-0.5 rounded border border-gray-200">run()</code>.</p>
            <div class="flex flex-wrap gap-1.5">
              <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Web scraping</span>
              <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold bg-violet-50 text-violet-600 border border-violet-100">Reusability</span>
            </div>
          </div>
        </div>

        <!-- Card 3 — File processor -->
        <div class="rounded-2xl border border-blue-100 overflow-hidden shadow-sm hover:shadow-md hover:border-blue-200 transition-all duration-300">
          <div class="h-1 bg-gradient-to-r from-blue-500 to-indigo-400"></div>
          <div class="px-5 py-5">
            <div class="flex items-center gap-3 mb-3">
              <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shrink-0 shadow-md">
                <span class="iconify text-white text-sm" data-icon="fa6-solid:folder-open"></span>
              </span>
              <div>
                <p class="text-sm font-bold text-gray-800">File Processor</p>
                <p class="text-[10px] text-gray-400 italic leading-tight">Batch processing across many files</p>
              </div>
            </div>
            <p class="text-xs text-gray-500 leading-relaxed mb-3">A script that reads CSV files, validates them, and moves them to an archive folder benefits enormously from a class. Once refactored, you can create one object per file and run the whole pipeline in a loop — no copy-pasting of function calls.</p>
            <div class="flex flex-wrap gap-1.5">
              <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">File handling</span>
              <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold bg-blue-50 text-blue-600 border border-blue-100">Batch jobs</span>
            </div>
          </div>
        </div>

      </div>

      <!-- Code example: real-world ReportRunner pattern -->
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-3">The same class pattern — applied to a sales report</p>
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex gap-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-red-400/80"></span>
                <span class="w-2.5 h-2.5 rounded-full bg-amber-400/80"></span>
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-400/80"></span>
              </div>
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">report_runner.py — production style</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code">
            <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:
    """Loads, cleans, and saves the daily sales report."""

    def load_data(self):
        print("Loading sales data from database...")
        # in production: self.data = db.query("SELECT * FROM sales")

    def clean_data(self):
        print("Removing duplicates and nulls...")
        # in production: self.data = self.data.dropna().drop_duplicates()

    def save_report(self):
        print("Report saved to /reports/daily_sales.csv")
        # in production: self.data.to_csv("daily_sales.csv", index=False)

    def run(self):
        """Entry point — runs all steps in order."""
        self.load_data()
        self.clean_data()
        self.save_report()

# one line to run the whole report
ReportRunner().run()</code></pre>
          </div>
        </div>
      </div>

      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">Notice that the comments inside each method describe what real production code would do. The class structure does not change between a learning example and a production script — only the code inside each method grows more complex as the project matures.</p>
      </div>

    </div>
  </div>
</section>'''

def replace_section(html, section_id, new_html):
    marker = f'<section id="{section_id}"'
    start = html.find(marker)
    if start == -1:
        print(f'❌ Could not find <section id="{section_id}">'); return html, False
    search = html[start:]
    depth, end, i = 0, -1, 0
    while i < len(search):
        if search[i:].startswith('<section'):
            depth += 1; i += len('<section')
        elif search[i:].startswith('</section>'):
            depth -= 1
            if depth == 0:
                end = start + i + len('</section>'); break
            i += len('</section>')
        else:
            i += 1
    if end == -1:
        print(f'❌ No closing </section> for #{section_id}'); return html, False
    old = html[start:end]
    print(f'  Old #{section_id}: {len(old):,} chars')
    print(f'  New #{section_id}: {len(new_html):,} chars')
    return html[:start] + new_html + html[end:], True

html = TARGET.read_text(encoding='utf-8')
html, ok = replace_section(html, 'real-world', NEW_SECTION)
if not ok: sys.exit(1)
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# --- Verification ---
result = TARGET.read_text(encoding='utf-8')
se_start = result.find('<section id="real-world"')
nx_start = result.find('<section id="recap"')
s = result[se_start:nx_start] if se_start != -1 and nx_start != -1 else result

checks = [
    ("scroll-mt-24",                        'class="scroll-mt-24"'),
    ("Icon fa6-solid:briefcase",            'data-icon="fa6-solid:briefcase"'),
    ("Header: Real-World Applications",     ">Real-World Applications<"),
    ("Card 1: Sales Report Runner",         ">Sales Report Runner<"),
    ("Card 2: Web Scraper",                 ">Web Scraper<"),
    ("Card 3: File Processor",              ">File Processor<"),
    ("3 card colour bars",                  3),
    ("Code: class ReportRunner docstrs",    '"""Loads, cleans, and saves'),
    ("Code: def run(self) entry point",     '"""Entry point'),
    ("Code: ReportRunner().run()",         "ReportRunner().run()"),
    ("1 amber tip",                         1),
    ("No ClaimsPipeline refs",              True),
    ("No DataPipeline refs",                True),
    ("No healthcare refs",                  True),
]

passed, failed = 0, 0
for label, needle in checks:
    if needle is True:
        label_map = {
            "No ClaimsPipeline refs": "ClaimsPipeline",
            "No DataPipeline refs": "DataPipeline",
            "No healthcare refs": "healthcare",
        }
        term = label_map.get(label, "")
        ok2 = term not in s
        print(f'  {"✅" if ok2 else "❌"} {label}')
        if ok2: passed += 1
        else: failed += 1
    elif isinstance(needle, int):
        if "card colour bars" in label:
            count = s.count('<div class="h-1 bg-gradient-to-r')
        elif "amber tip" in label:
            count = s.count("bg-amber-tip")
        else:
            count = 0
        ok3 = count >= needle
        print(f'  {"✅" if ok3 else "❌"} {label} (found {count})')
        if ok3: passed += 1
        else: failed += 1
    elif needle in s:
        print(f'  ✅ {label}'); passed += 1
    else:
        print(f'  ❌ {label} — not found'); failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
