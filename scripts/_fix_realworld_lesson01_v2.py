"""
Replace #real-world section in lesson01 with Layout B (inbox-gotcha).

Layout B: 3 file/ticket inbox cards (CSV, JSON, Parquet) + 2-step habit block + amber tip.
Each card has a dark IDE header, source system, description, gotcha box,
"Loaded with:" badge, and "Unlocks:" line.
"""
import re

TARGET = r'pages\mod_04_data_engineering\lesson01_what_is_data_engineering.html'

# ── New subtitle ───────────────────────────────────────────────────────────────
NEW_SUBTITLE = 'Real data files a data engineer inherits — and the silent failure hiding in each one'

# ── New section body (everything inside <div class="bg-white px-8 py-7...">)  ─
NEW_BODY = '''\
      <p class="text-sm text-gray-600 leading-relaxed">Data engineering is not just about moving files — it is about catching the problems inside those files before they corrupt every report downstream. The three datasets below are the kind you will encounter in your first week on the job. Each one looks clean at first glance. Each one has a trap.</p>

      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">Files a data engineer inherits</p>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">

          <!-- Card 1: CSV — retail -->
          <div class="rounded-2xl overflow-hidden border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300">
            <div class="flex items-center justify-between px-4 py-2.5 bg-[#1f2937]">
              <div class="flex items-center gap-2">
                <span class="iconify text-violet-400 text-xs" data-icon="fa6-solid:file-lines"></span>
                <span class="text-[10px] font-bold text-gray-300 uppercase tracking-wider">ecommerce_sales.csv</span>
              </div>
              <span class="text-[9px] font-bold px-1.5 py-0.5 rounded bg-violet-900/40 text-violet-300 border border-violet-800/40">CSV</span>
            </div>
            <div class="bg-white px-4 py-4 space-y-3">
              <div class="flex items-center gap-2">
                <span class="iconify text-gray-300 text-[11px]" data-icon="fa6-solid:cart-shopping"></span>
                <span class="text-[11px] text-gray-400">From: Retail POS System</span>
              </div>
              <p class="text-xs text-gray-600 leading-relaxed">50,000 daily transaction rows exported every night. It opens in Excel without complaint. The <code class="font-mono text-violet-700">amount</code> column looks fine until you count how many rows are blank.</p>
              <div class="rounded-lg bg-amber-50 border border-amber-100 px-3 py-2">
                <p class="text-[10px] font-semibold text-amber-700 leading-snug">&#9888; Gotcha: pandas reads null values in <code class="font-mono">amount</code> as zero by default — your revenue total is wrong and no error is raised.</p>
              </div>
              <div class="flex flex-wrap items-center gap-2">
                <span class="text-[10px] text-gray-400">Loaded with:</span>
                <code class="text-[10px] font-mono font-bold px-1.5 py-0.5 rounded bg-violet-50 text-violet-700 border border-violet-100">pd.read_csv()</code>
              </div>
              <p class="text-[11px] text-gray-500 leading-snug"><span class="font-semibold text-gray-700">Unlocks:</span> daily revenue dashboards, low-stock alerts, and promotional lift analysis across 200+ stores.</p>
            </div>
          </div>

          <!-- Card 2: JSON — healthcare -->
          <div class="rounded-2xl overflow-hidden border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300">
            <div class="flex items-center justify-between px-4 py-2.5 bg-[#1f2937]">
              <div class="flex items-center gap-2">
                <span class="iconify text-blue-400 text-xs" data-icon="fa6-solid:file-code"></span>
                <span class="text-[10px] font-bold text-gray-300 uppercase tracking-wider">patient_records.json</span>
              </div>
              <span class="text-[9px] font-bold px-1.5 py-0.5 rounded bg-blue-900/40 text-blue-300 border border-blue-800/40">JSON</span>
            </div>
            <div class="bg-white px-4 py-4 space-y-3">
              <div class="flex items-center gap-2">
                <span class="iconify text-gray-300 text-[11px]" data-icon="fa6-solid:hospital"></span>
                <span class="text-[11px] text-gray-400">From: Hospital EHR System</span>
              </div>
              <p class="text-xs text-gray-600 leading-relaxed">Discharge records from 12 regional clinics, each exported by a different vendor. Every record has a patient identifier — but not all of them call it the same thing.</p>
              <div class="rounded-lg bg-amber-50 border border-amber-100 px-3 py-2">
                <p class="text-[10px] font-semibold text-amber-700 leading-snug">&#9888; Gotcha: Clinic A sends <code class="font-mono">patientId</code>, Clinic B sends <code class="font-mono">patient_id</code> — a join silently drops half the records with no error.</p>
              </div>
              <div class="flex flex-wrap items-center gap-2">
                <span class="text-[10px] text-gray-400">Loaded with:</span>
                <code class="text-[10px] font-mono font-bold px-1.5 py-0.5 rounded bg-blue-50 text-blue-700 border border-blue-100">pd.read_json()</code>
              </div>
              <p class="text-[11px] text-gray-500 leading-snug"><span class="font-semibold text-gray-700">Unlocks:</span> cross-clinic outcome reports, readmission rate tracking, and insurance billing reconciliation.</p>
            </div>
          </div>

          <!-- Card 3: Parquet — finance -->
          <div class="rounded-2xl overflow-hidden border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300">
            <div class="flex items-center justify-between px-4 py-2.5 bg-[#1f2937]">
              <div class="flex items-center gap-2">
                <span class="iconify text-emerald-400 text-xs" data-icon="fa6-solid:database"></span>
                <span class="text-[10px] font-bold text-gray-300 uppercase tracking-wider">transactions.parquet</span>
              </div>
              <span class="text-[9px] font-bold px-1.5 py-0.5 rounded bg-emerald-900/40 text-emerald-300 border border-emerald-800/40">PARQUET</span>
            </div>
            <div class="bg-white px-4 py-4 space-y-3">
              <div class="flex items-center gap-2">
                <span class="iconify text-gray-300 text-[11px]" data-icon="fa6-solid:landmark"></span>
                <span class="text-[11px] text-gray-400">From: Banking Event Stream</span>
              </div>
              <p class="text-xs text-gray-600 leading-relaxed">2 million card transaction events per hour, stored in a columnar format that loads in seconds even at that scale. The timestamps, however, are not what you expect.</p>
              <div class="rounded-lg bg-amber-50 border border-amber-100 px-3 py-2">
                <p class="text-[10px] font-semibold text-amber-700 leading-snug">&#9888; Gotcha: <code class="font-mono">timestamp</code> is Unix epoch seconds — every time-based chart plots numbers in the billions until you convert it.</p>
              </div>
              <div class="flex flex-wrap items-center gap-2">
                <span class="text-[10px] text-gray-400">Loaded with:</span>
                <code class="text-[10px] font-mono font-bold px-1.5 py-0.5 rounded bg-emerald-50 text-emerald-700 border border-emerald-100">pd.read_parquet()</code>
              </div>
              <p class="text-[11px] text-gray-500 leading-snug"><span class="font-semibold text-gray-700">Unlocks:</span> real-time fraud scoring, daily settlement reports, and regulatory compliance exports.</p>
            </div>
          </div>

        </div>
      </div>

      <!-- 2-step habit block -->
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">Two habits every data engineer builds</p>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div class="flex items-start gap-4 rounded-2xl border border-gray-100 bg-gray-50 px-5 py-4 hover:border-[#f5c6e0] transition-colors">
            <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-black shadow-md shrink-0 mt-0.5">1</span>
            <div>
              <p class="text-sm font-bold text-gray-800 mb-1">Inspect Before You Transform</p>
              <p class="text-xs text-gray-500 leading-relaxed">Run <code class="font-mono">.info()</code> and <code class="font-mono">.head()</code> the moment data arrives. Understanding the shape, column names, and data types of your input is not optional — it is the first step of every pipeline.</p>
            </div>
          </div>
          <div class="flex items-start gap-4 rounded-2xl border border-gray-100 bg-gray-50 px-5 py-4 hover:border-[#f5c6e0] transition-colors">
            <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-black shadow-md shrink-0 mt-0.5">2</span>
            <div>
              <p class="text-sm font-bold text-gray-800 mb-1">Assert Before You Load</p>
              <p class="text-xs text-gray-500 leading-relaxed">Validate row counts, required columns, and data types with <code class="font-mono">assert</code> statements before writing anything to the warehouse. A failed assert stops the pipeline — which is exactly what you want when data is wrong.</p>
            </div>
          </div>
        </div>
        <div class="mt-4 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">If you skip the inspection step, schema drift silently corrupts your pipeline — and the first person to notice is usually an analyst asking why the weekly numbers do not match last week's report.</p>
        </div>
      </div>\
'''

with open(TARGET, encoding='utf-8') as f:
    html = f.read()

# ── 1. Update subtitle ─────────────────────────────────────────────────────────
OLD_SUB = 'Real data files a data engineer inherits — and the silent failure hiding in each one'
PREV_SUB = 'How data engineering powers decisions across retail, healthcare, and finance'
if PREV_SUB in html:
    html = html.replace(PREV_SUB, OLD_SUB, 1)
    print("  subtitle updated")

# ── 2. Replace section body ────────────────────────────────────────────────────
# Match the body div and its content, leaving the section shell intact
pattern = re.compile(
    r'(<section id="real-world">.*?<div class="bg-white px-8 py-7[^"]*">)'
    r'(.*?)'
    r'(</div>\s*</div>\s*</section>)',
    re.DOTALL
)

m = pattern.search(html)
if not m:
    print("❌ Section body pattern not found — check the file manually")
    exit(1)

old_section = m.group(0)
new_section = m.group(1) + '\n' + NEW_BODY + '\n\n      ' + m.group(3)
new_html = html[:m.start()] + new_section + html[m.end():]

# ── 3. Verify div balance ──────────────────────────────────────────────────────
sm = re.search(r'<section id="real-world">(.*?)</section>', new_html, re.DOTALL)
if sm:
    sec_block = sm.group(0)
    old_sm = re.search(r'<section id="real-world">(.*?)</section>', html, re.DOTALL)
    old_block = old_sm.group(0) if old_sm else ''

    old_diff = old_block.count('<div') - old_block.count('</div>')
    new_diff = sec_block.count('<div') - sec_block.count('</div>')
    full_old = html.count('<div') - html.count('</div>')
    full_new = new_html.count('<div') - new_html.count('</div>')

    print(f"  old section div diff : {old_diff:+d}")
    print(f"  new section div diff : {new_diff:+d}")
    print(f"  full file div diff   : {full_new:+d}  {'(OK ✅)' if full_new == 0 else '(❌ MISMATCH)'}")

if new_diff != 0:
    print(f"\n⚠️  Section div imbalance ({new_diff:+d}) — NOT writing file")
    exit(1)

with open(TARGET, 'w', encoding='utf-8') as f:
    f.write(new_html)
print(f"✅ Patched: {TARGET}")
