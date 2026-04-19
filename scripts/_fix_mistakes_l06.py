"""
Rewrite Lesson06 #mistakes section body to match the canonical template:
- fa6-solid:bug tab icons
- mistake-card class + border-gray-200 outer wrapper
- Canonical card header: w-9 h-9 icon, h4 title, p subtitle, Pitfall badge
- relative grid sm:grid-cols-2 split + pink arrow circle divider
- Amber tip as border-t footer (bg-amber-50/40, fa6-solid:lightbulb, text-xs)
- Section subtitle updated
- Tab icon: fa6-solid:bug
"""
import pathlib

FILE = pathlib.Path(
    r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_04_data_engineering"
    r"\lesson06_nosql_when_tables_arent_enough.html"
)

# ── New section subtitle + body ───────────────────────────────────────────────
NEW_SUBTITLE = 'Pitfalls beginners hit when working with NoSQL databases'

NEW_BODY = """\
    <div class="bg-white px-8 py-7 space-y-6">
<div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
  <button onclick="switchMkTab(0)" class="mk-step mk-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
    <span class="mk-step-label text-xs font-bold">Relational Joins</span>
  </button>
  <button onclick="switchMkTab(1)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
    <span class="mk-step-label text-xs font-bold">Missing Index</span>
  </button>
  <button onclick="switchMkTab(2)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
    <span class="mk-step-label text-xs font-bold">NoSQL for Uniform Data</span>
  </button>
  <button onclick="switchMkTab(3)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
    <span class="mk-step-label text-xs font-bold">Missing $set</span>
  </button>
  <button onclick="switchMkTab(4)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
    <span class="mk-step-label text-xs font-bold">Redis as Primary Store</span>
  </button>
</div>

<!-- ── Mistake 1: Relational Joins ──────────────────────────────── -->
<div class="mk-panel mk-panel-anim" role="tabpanel">
  <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">
    <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
        <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
      </span>
      <div class="min-w-0 flex-1">
        <h4 class="font-bold text-gray-800 text-sm">Replicating SQL JOINs with Manual Python Lookups</h4>
        <p class="text-xs text-gray-500 mt-0.5">In-Python joins across two collections make two network round-trips and lose all query optimization.</p>
      </div>
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
        <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
      </span>
    </div>
    <div class="px-6 py-5">
      <p class="text-sm text-gray-600 leading-relaxed">MongoDB has no native JOIN &mdash; fetching a customer then looping over a separate orders collection makes two round-trips and bypasses the query optimizer, making the code slower and harder to maintain than a SQL JOIN. If your query always needs data from two collections, either embed the related data in one document or move to a relational database.</p>
    </div>
    <div class="relative grid grid-cols-1 sm:grid-cols-2">
      <div class="p-5 bg-red-50/30">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong &mdash; two round-trips, no optimizer
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># Two network calls + Python loop = slow + fragile
customer = customers.find_one({&quot;_id&quot;: customer_id})
order_list = list(orders_col.find({&quot;customer_id&quot;: customer_id}))</code></pre>
        </div>
      </div>
      <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
        <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
          <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
        </span>
      </div>
      <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct &mdash; embed related data in one document
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># recent_orders is embedded — one round-trip, no join needed
customer = customers.find_one({&quot;_id&quot;: customer_id})
order_list = customer[&quot;recent_orders&quot;]  # already inside the document</code></pre>
        </div>
      </div>
    </div>
    <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
      <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
      <p class="text-xs text-gray-600 leading-relaxed">Think of each MongoDB document as a self-contained record &mdash; if you find yourself writing a second <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">find()</code> call to &ldquo;complete&rdquo; the first, that data probably belongs embedded in the original document. When data has many complex relationships with strict integrity rules, PostgreSQL will serve you better.</p>
    </div>
  </div>
</div>

<!-- ── Mistake 2: Missing Index ──────────────────────────────────── -->
<div class="mk-panel mk-panel-anim hidden" role="tabpanel">
  <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">
    <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
        <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
      </span>
      <div class="min-w-0 flex-1">
        <h4 class="font-bold text-gray-800 text-sm">Querying Without an Index Causes a Full Collection Scan</h4>
        <p class="text-xs text-gray-500 mt-0.5">Without an explicit index, every find() reads every document in the collection regardless of size.</p>
      </div>
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
        <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
      </span>
    </div>
    <div class="px-6 py-5">
      <p class="text-sm text-gray-600 leading-relaxed">MongoDB does not create indexes on arbitrary fields automatically &mdash; without one, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">find()</code> performs a COLLSCAN (collection scan), reading every document even when only one matches. Call <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">create_index()</code> once at application startup for every field you filter on regularly.</p>
    </div>
    <div class="relative grid grid-cols-1 sm:grid-cols-2">
      <div class="p-5 bg-red-50/30">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong &mdash; COLLSCAN on every query
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># Reads all 500,000 documents to find one product
product = products.find_one({&quot;sku&quot;: &quot;LAPTOP-001&quot;})</code></pre>
        </div>
      </div>
      <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
        <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
          <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
        </span>
      </div>
      <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct &mdash; index created at startup
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># Create once at startup &mdash; find() now uses O(log n) IXSCAN
products.create_index([(&quot;sku&quot;, 1)], unique=True)
product = products.find_one({&quot;sku&quot;: &quot;LAPTOP-001&quot;})  # instant lookup</code></pre>
        </div>
      </div>
    </div>
    <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
      <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
      <p class="text-xs text-gray-600 leading-relaxed">Run <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">products.find({&quot;sku&quot;: &quot;LAPTOP-001&quot;}).explain()</code> before and after adding the index. Look for <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">&quot;stage&quot;: &quot;COLLSCAN&quot;</code> vs <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">&quot;IXSCAN&quot;</code> to confirm the query plan changed. Only bulk export queries should ever show COLLSCAN.</p>
    </div>
  </div>
</div>

<!-- ── Mistake 3: NoSQL for Uniform Data ───────────────────────── -->
<div class="mk-panel mk-panel-anim hidden" role="tabpanel">
  <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">
    <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
        <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
      </span>
      <div class="min-w-0 flex-1">
        <h4 class="font-bold text-gray-800 text-sm">Choosing MongoDB When Every Record Has Identical Fields</h4>
        <p class="text-xs text-gray-500 mt-0.5">Uniform-schema data belongs in SQL, which provides type constraints, JOIN support, and aggregation optimization for free.</p>
      </div>
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
        <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
      </span>
    </div>
    <div class="px-6 py-5">
      <p class="text-sm text-gray-600 leading-relaxed">When every record has the same fixed fields &mdash; like a payroll table with identical columns for all 5,000 employees &mdash; MongoDB adds no flexibility benefit and removes the type enforcement, foreign-key constraints, and aggregation optimizer that SQL provides automatically. A quick test: if fewer than 20% of your sampled records have unique field combinations, use SQL.</p>
    </div>
    <div class="relative grid grid-cols-1 sm:grid-cols-2">
      <div class="p-5 bg-red-50/30">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong &mdash; fixed schema in MongoDB
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># Same 4 fields on every document &mdash; zero flexibility benefit
employees.insert_one({&quot;emp_id&quot;: 42, &quot;name&quot;: &quot;Alice&quot;,
    &quot;dept&quot;: &quot;Engineering&quot;, &quot;salary&quot;: 92000})</code></pre>
        </div>
      </div>
      <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
        <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
          <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
        </span>
      </div>
      <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct &mdash; use SQL for uniform records
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># SQL enforces types, constraints, and enables JOINs automatically
# INSERT INTO employees (emp_id, name, dept, salary)
# VALUES (42, 'Alice', 'Engineering', 92000);</code></pre>
        </div>
      </div>
    </div>
    <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
      <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
      <p class="text-xs text-gray-600 leading-relaxed">Ask: &ldquo;Would this data fit neatly in a spreadsheet with consistent columns?&rdquo; If yes, it is relational data &mdash; use SQL. NoSQL's flexibility benefit only applies when records genuinely have different shapes, such as a product catalog where electronics have a <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">wattage</code> field that furniture items simply omit.</p>
    </div>
  </div>
</div>

<!-- ── Mistake 4: Missing $set ──────────────────────────────────── -->
<div class="mk-panel mk-panel-anim hidden" role="tabpanel">
  <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">
    <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
        <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
      </span>
      <div class="min-w-0 flex-1">
        <h4 class="font-bold text-gray-800 text-sm">Calling update_one() Without $set Silently Replaces the Entire Document</h4>
        <p class="text-xs text-gray-500 mt-0.5">A bare update dictionary deletes every field not included in the update, causing irreversible silent data loss.</p>
      </div>
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
        <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
      </span>
    </div>
    <div class="px-6 py-5">
      <p class="text-sm text-gray-600 leading-relaxed">Unlike SQL UPDATE which patches named columns, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">update_one()</code> treats a bare dictionary as a full replacement document &mdash; it overwrites the matched document with your dict and silently deletes every field you did not include. Always wrap the fields you want to change inside <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">{&quot;$set&quot;: {...}}</code>.</p>
    </div>
    <div class="relative grid grid-cols-1 sm:grid-cols-2">
      <div class="p-5 bg-red-50/30">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong &mdash; replaces entire document
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># DANGER: deletes name, role, languages &mdash; only price survives
products.update_one({&quot;sku&quot;: &quot;LAPTOP-001&quot;}, {&quot;price&quot;: 899.99})</code></pre>
        </div>
      </div>
      <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
        <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
          <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
        </span>
      </div>
      <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct &mdash; patches price field only
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># $set updates only price; name, role, languages are untouched
products.update_one(
    {&quot;sku&quot;: &quot;LAPTOP-001&quot;},
    {&quot;$set&quot;: {&quot;price&quot;: 899.99}}   # only this field changes
)</code></pre>
        </div>
      </div>
    </div>
    <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
      <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
      <p class="text-xs text-gray-600 leading-relaxed">This mistake is silent &mdash; MongoDB confirms &ldquo;1 document modified&rdquo; in both cases, so you will not notice until you read the document back and find only one field. Always read the document after your first <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">update_one()</code> in a new application to confirm only the intended field changed.</p>
    </div>
  </div>
</div>

<!-- ── Mistake 5: Redis as Primary Store ────────────────────────── -->
<div class="mk-panel mk-panel-anim hidden" role="tabpanel">
  <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">
    <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
        <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
      </span>
      <div class="min-w-0 flex-1">
        <h4 class="font-bold text-gray-800 text-sm">Using Redis as the Sole Data Store Instead of a Cache Layer</h4>
        <p class="text-xs text-gray-500 mt-0.5">Redis stores data in RAM; all data is lost on server restart unless persistence is configured, making it unsuitable as a primary database.</p>
      </div>
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
        <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
      </span>
    </div>
    <div class="px-6 py-5">
      <p class="text-sm text-gray-600 leading-relaxed">Redis is designed for temporary, fast lookups in RAM &mdash; it is not a durable database. Storing order records or user profiles in Redis without a TTL and without a persistent backing store means all data is permanently lost on every server restart or crash. Save durable records in PostgreSQL or MongoDB first, then use Redis as a short-lived cache layer with a TTL.</p>
    </div>
    <div class="relative grid grid-cols-1 sm:grid-cols-2">
      <div class="p-5 bg-red-50/30">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong &mdash; orders in Redis only
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># No TTL, no persistent backing store &mdash; lost on restart
r.set(f&quot;order:{order_id}&quot;, json.dumps(order_data))</code></pre>
        </div>
      </div>
      <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
        <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
          <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
        </span>
      </div>
      <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct &mdash; MongoDB primary, Redis cache
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">orders_col.insert_one(order_data)        # persist permanently in MongoDB
r.setex(f&quot;order:{order_id}&quot;, 300,      # cache in Redis, expires in 5 min
        json.dumps(order_data))</code></pre>
        </div>
      </div>
    </div>
    <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
      <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
      <p class="text-xs text-gray-600 leading-relaxed">The rule: if losing this data for 5 minutes would cause a business problem, it must live in a durable database. Redis fits perfectly as a cache layer in front of MongoDB or PostgreSQL &mdash; write to the durable store first, then populate Redis for fast reads with a TTL.</p>
    </div>
  </div>
</div>
"""

# ── Read, locate, and replace ─────────────────────────────────────────────────
content = FILE.read_text(encoding="utf-8")

# Fix section subtitle
OLD_SUBTITLE = 'Pitfalls to avoid'
if OLD_SUBTITLE in content:
    content = content.replace(OLD_SUBTITLE, NEW_SUBTITLE, 1)
    print(f"✅ Subtitle updated")
else:
    print(f"⚠️  Subtitle not found — check manually")

# Find mistake section boundaries
mk_section_start = content.find('<section id="mistakes">')
if mk_section_start == -1:
    print("❌ Mistakes section not found"); raise SystemExit(1)

BODY_OPEN  = '    <div class="bg-white px-8 py-7 space-y-6">\n'
SECTION_END = "    </div>\n  </div>\n</section>"

body_open_idx    = content.find(BODY_OPEN, mk_section_start)
section_close_idx = content.find(SECTION_END, body_open_idx)

if body_open_idx == -1 or section_close_idx == -1:
    print("❌ Body delimiters not found"); raise SystemExit(1)

old_body = content[body_open_idx:section_close_idx]
new_content = content.replace(old_body, NEW_BODY, 1)

if new_content == content:
    print("⚠️  No change — replacement produced identical content"); raise SystemExit(1)

FILE.write_text(new_content, encoding="utf-8")
print("✅ Mistakes section replaced")

# ── Verify ────────────────────────────────────────────────────────────────────
c2 = FILE.read_text(encoding="utf-8")
lines2 = c2.split("\n")
mk_start = next(i for i, l in enumerate(lines2) if '<section id="mistakes"' in l)
next_sec  = next(i for i, l in enumerate(lines2[mk_start + 1:], mk_start + 1) if "<section id=" in l)
block = "\n".join(lines2[mk_start:next_sec])
opens  = block.count("<div")
closes = block.count("</div>")
tabs = [l.strip() for l in lines2[mk_start:next_sec] if "mk-step-label" in l]
print(f"div diff: {opens - closes}")
print(f"Tab count: {len(tabs)}")
import re
for t in tabs:
    m = re.search(r'font-bold">(.+?)</span>', t)
    if m: print(" ", m.group(1))
# main balance
main_start = next(i for i, l in enumerate(lines2) if "<main " in l or "<main>" in l)
main_end   = next(i for i, l in enumerate(lines2) if "</main>" in l)
blk2 = "\n".join(lines2[main_start:main_end + 1])
print(f"main div diff: {blk2.count('<div') - blk2.count('</div>')}")
