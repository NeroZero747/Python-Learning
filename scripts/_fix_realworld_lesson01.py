"""
Replace the #real-world section body in lesson01 with Layout A (metric-cards).

3 gradient icon cards covering real data engineering use cases:
  0 — Retail: 50,000 daily transactions (violet)
  1 — Healthcare: patient records across 12 clinics (pink)
  2 — Finance: fraud detection on 2M transactions/hour (emerald)

Followed by a 2-column without/with data engineering table.
"""
import re
from pathlib import Path

TARGET = Path(r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_04_data_engineering\lesson01_what_is_data_engineering.html")

NEW_SECTION = r'''<section id="real-world">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:briefcase"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Real-World Use</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">How data engineering powers decisions across retail, healthcare, and finance</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">

      <p class="text-sm text-gray-600 leading-relaxed">Every organization that makes decisions from data relies on a data engineering layer underneath. You might never see it in the final dashboard, but the pipeline that loaded, cleaned, and organized that data was built by a data engineer. Here are three industries where the work you are learning in this lesson runs every day.</p>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">

        <!-- Card 1: Retail — violet -->
        <div class="relative rounded-2xl overflow-hidden border border-violet-100 bg-gradient-to-br from-violet-50 via-white to-purple-50 px-6 py-6 text-center">
          <div class="flex flex-col items-center gap-3">
            <span class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-violet-500 to-purple-600 shadow-lg shadow-violet-200">
              <span class="iconify text-white text-2xl" data-icon="fa6-solid:cart-shopping"></span>
            </span>
            <h3 class="text-sm font-bold text-gray-800 leading-snug">A Retailer Syncs 50,000&nbsp;Daily Transactions</h3>
            <p class="text-xs text-gray-500 leading-relaxed">Every night a pipeline reads point-of-sale data, removes duplicate rows, adds a <code class="font-mono text-violet-700">total</code> column, and loads clean sales into the analytics warehouse before 6&nbsp;AM.</p>
            <div class="flex items-center gap-1.5 mt-1 px-3 py-1.5 rounded-full bg-violet-100 border border-violet-200">
              <span class="iconify text-violet-700 text-[11px]" data-icon="fa6-solid:arrow-right-from-bracket"></span>
              <span class="text-[11px] font-semibold text-violet-700">delivers <code class="font-mono">clean_sales.csv</code></span>
            </div>
          </div>
        </div>

        <!-- Card 2: Healthcare — pink -->
        <div class="relative rounded-2xl overflow-hidden border border-pink-100 bg-gradient-to-br from-pink-50 via-white to-rose-50 px-6 py-6 text-center">
          <div class="flex flex-col items-center gap-3">
            <span class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-lg shadow-pink-200">
              <span class="iconify text-white text-2xl" data-icon="fa6-solid:hospital"></span>
            </span>
            <h3 class="text-sm font-bold text-gray-800 leading-snug">A Hospital Routes Records Across 12&nbsp;Clinics</h3>
            <p class="text-xs text-gray-500 leading-relaxed">An ETL pipeline extracts discharge notes from each clinic system, validates required fields with <code class="font-mono text-[#CB187D]">assert</code> checks, and loads clean patient records into the central reporting database.</p>
            <div class="flex items-center gap-1.5 mt-1 px-3 py-1.5 rounded-full bg-pink-100 border border-pink-200">
              <span class="iconify text-[#CB187D] text-[11px]" data-icon="fa6-solid:arrow-right-from-bracket"></span>
              <span class="text-[11px] font-semibold text-[#CB187D]">delivers <code class="font-mono">patient_records.db</code></span>
            </div>
          </div>
        </div>

        <!-- Card 3: Finance — emerald -->
        <div class="relative rounded-2xl overflow-hidden border border-emerald-100 bg-gradient-to-br from-emerald-50 via-white to-teal-50 px-6 py-6 text-center">
          <div class="flex flex-col items-center gap-3">
            <span class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br from-emerald-500 to-teal-600 shadow-lg shadow-emerald-200">
              <span class="iconify text-white text-2xl" data-icon="fa6-solid:shield-halved"></span>
            </span>
            <h3 class="text-sm font-bold text-gray-800 leading-snug">A Bank Screens 2&nbsp;Million Transactions Per&nbsp;Hour</h3>
            <p class="text-xs text-gray-500 leading-relaxed">A data quality layer runs type checks and null assertions on every incoming batch before the fraud model scores it — catching schema drift before it silently corrupts predictions.</p>
            <div class="flex items-center gap-1.5 mt-1 px-3 py-1.5 rounded-full bg-emerald-100 border border-emerald-200">
              <span class="iconify text-emerald-700 text-[11px]" data-icon="fa6-solid:arrow-right-from-bracket"></span>
              <span class="text-[11px] font-semibold text-emerald-700">delivers <code class="font-mono">validated_batch.parquet</code></span>
            </div>
          </div>
        </div>

      </div>

      <!-- Before / After table -->
      <div class="rounded-xl border border-gray-100 overflow-hidden">
        <div class="grid grid-cols-2">
          <div class="border-r border-gray-100">
            <div class="flex items-center gap-2 px-4 py-3 bg-red-50 border-b border-red-100">
              <span class="iconify text-red-400 text-sm shrink-0" data-icon="fa6-solid:circle-xmark"></span>
              <p class="text-xs font-bold text-red-500 uppercase tracking-wide">Without Data Engineering</p>
            </div>
            <div class="px-4 py-4 space-y-3">
              <div class="flex items-start gap-2.5">
                <span class="iconify text-red-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>
                <p class="text-xs text-gray-500">Analysts spend Monday morning manually downloading CSVs and fixing broken formulas in Excel before they can start their real work.</p>
              </div>
              <div class="flex items-start gap-2.5">
                <span class="iconify text-red-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>
                <p class="text-xs text-gray-500">Reports contain different numbers depending on who ran them and when, because no single source of clean data exists.</p>
              </div>
              <div class="flex items-start gap-2.5">
                <span class="iconify text-red-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>
                <p class="text-xs text-gray-500">A bad row in the source file silently skews every downstream chart for weeks before anyone notices.</p>
              </div>
            </div>
          </div>
          <div>
            <div class="flex items-center gap-2 px-4 py-3 bg-[#fdf0f7] border-b border-[#f5c6e0]">
              <span class="iconify text-[#CB187D] text-sm shrink-0" data-icon="fa6-solid:circle-check"></span>
              <p class="text-xs font-bold text-[#CB187D] uppercase tracking-wide">With Data Engineering</p>
            </div>
            <div class="px-4 py-4 space-y-3">
              <div class="flex items-start gap-2.5">
                <span class="iconify text-emerald-500 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>
                <p class="text-xs text-gray-500">Clean, validated data arrives in the warehouse automatically every morning — analysts open their dashboard and start asking questions immediately.</p>
              </div>
              <div class="flex items-start gap-2.5">
                <span class="iconify text-emerald-500 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>
                <p class="text-xs text-gray-500">Every report draws from the same pipeline output, so two people comparing numbers always see the same figures.</p>
              </div>
              <div class="flex items-start gap-2.5">
                <span class="iconify text-emerald-500 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>
                <p class="text-xs text-gray-500">Assert checks catch a bad row the moment it enters the pipeline, so it never reaches a dashboard or a model.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>
'''

html = TARGET.read_text(encoding="utf-8")

# Replace the entire #real-world section
pattern = re.compile(r'<section id="real-world">.*?</section>', re.DOTALL)
match = pattern.search(html)
if not match:
    print("❌ Could not find <section id='real-world'>")
    exit(1)

old = match.group(0)
new_html = html.replace(old, NEW_SECTION, 1)

if new_html == html:
    print("⚠️  No change made")
    exit(0)

TARGET.write_text(new_html, encoding="utf-8")
print(f"✅ Patched: {TARGET.name}")

# Balance check
def div_balance(text):
    return len(__import__('re').findall(r'<div\b', text)) - len(__import__('re').findall(r'</div>', text))

old_b = div_balance(old)
new_b = div_balance(NEW_SECTION)
full_b = div_balance(new_html)
print(f"  old section  div diff : {old_b:+d}")
print(f"  new section  div diff : {new_b:+d}")
print(f"  full file    div diff : {full_b:+d}  ({'OK ✅' if full_b == 0 else 'UNBALANCED ❌'})")
