"""
Rewrite Lesson06 Practice Exercises to match the lesson04/05 reference design:
- Pink numbered circles for task list items
- Remove starter scaffold code blocks (tasks describe what to do; solution is in accordion)
- Accordion button: bare sibling, onclick="this.nextElementSibling.classList.toggle('open')"
- "Why this matters" moved inside accordion-body
- Panel subtitle colour: text-gray-400
- Panel icon: add shrink-0
"""
import pathlib

FILE = pathlib.Path(
    r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_04_data_engineering"
    r"\lesson06_nosql_when_tables_arent_enough.html"
)

# ── Markers ───────────────────────────────────────────────────────────────────
BODY_OPEN = '    <div class="bg-white px-8 py-7 space-y-6">\n'
# The practice section ends with this exact sequence before </section>
SECTION_CLOSE = "    </div>\n  </div>\n</section>"

# ── New section body (everything between BODY_OPEN and SECTION_CLOSE) ────────
NEW_BODY = """\
    <div class="bg-white px-8 py-7 space-y-6">
<div class="flex flex-wrap items-center gap-2 mb-6" role="tablist">
  <button onclick="switchPeTab(0)" class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:database"></span><span class="pe-step-label text-xs font-bold">Insert &amp; Query</span></button>
  <button onclick="switchPeTab(1)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:layer-group"></span><span class="pe-step-label text-xs font-bold">NoSQL Categories</span></button>
  <button onclick="switchPeTab(2)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:magnifying-glass"></span><span class="pe-step-label text-xs font-bold">Query Operators</span></button>
  <button onclick="switchPeTab(3)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:filter"></span><span class="pe-step-label text-xs font-bold">Aggregation Pipeline</span></button>
  <button onclick="switchPeTab(4)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code-branch"></span><span class="pe-step-label text-xs font-bold">NoSQL or SQL?</span></button>
</div>

<!-- ── Panel 0 — Insert & Query ──────────────────────────────── -->
<div class="pe-panel pe-panel-anim" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">
          <span class="iconify text-base" data-icon="fa6-solid:database"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Insert &amp; Query</h3>
          <p class="text-xs text-gray-400 mt-0.5">Covers: connect, insert_many, find, update_one</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div class="space-y-2">
          <p class="text-xs font-bold uppercase tracking-widest text-brand">Tasks</p>
          <ol class="space-y-1.5 list-none pl-0">
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">1</span><span>Connect to MongoDB on <code class="font-mono text-xs">localhost:27017</code> and select the <code class="font-mono text-xs">company.employees</code> collection.</span></li>
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">2</span><span>Use <code class="font-mono text-xs">insert_many()</code> to add Alice (engineer, salary 92000, a <code class="font-mono text-xs">languages</code> list), Bob (manager, salary 85000, a <code class="font-mono text-xs">team_size</code> integer), and Carol (analyst, salary 72000, a <code class="font-mono text-xs">tools</code> list) — each document has different optional fields.</span></li>
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">3</span><span>Use <code class="font-mono text-xs">find()</code> with a <code class="font-mono text-xs">$gt</code> filter to retrieve all employees earning more than $80,000 and print each person&rsquo;s name and salary.</span></li>
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">4</span><span>Use <code class="font-mono text-xs">update_one()</code> with <code class="font-mono text-xs">$set</code> to change Alice&rsquo;s salary to $90,000 &mdash; do <em>not</em> pass the full document.</span></li>
          </ol>
        </div>
      </div>
      <button class="accordion-toggle w-full flex items-center justify-between text-xs font-semibold text-gray-500 px-4 py-2.5 rounded-xl bg-gray-50 border border-gray-100 hover:bg-gray-100 transition-colors" onclick="this.nextElementSibling.classList.toggle('open')">
        <span class="flex items-center gap-2">
          <span class="iconify text-[#CB187D]" data-icon="fa6-solid:eye"></span>
          Show Solution
        </span>
        <span class="iconify accordion-chevron text-gray-400" data-icon="fa6-solid:chevron-down"></span>
      </button>
      <div class="accordion-body">
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-1">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">solution_01.py</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code">
            <pre class="overflow-x-auto pre-reset"><code class="language-python">from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
employees = client["company"]["employees"]   # database → collection

# Task 2: insert_many() takes a list of dicts — each can have different keys
employees.insert_many([
    {"name": "Alice", "role": "engineer", "salary": 92000, "languages": ["Python", "Go"]},
    {"name": "Bob",   "role": "manager",  "salary": 85000, "team_size": 8},
    {"name": "Carol", "role": "analyst",  "salary": 72000, "tools": ["SQL", "Tableau"]},
])

# Task 3: {"salary": {"$gt": 80000}} is a MongoDB filter document
high_earners = list(employees.find({"salary": {"$gt": 80000}}))
for emp in high_earners:
    print(emp["name"], emp["salary"])   # Alice 92000 / Bob 85000

# Task 4: $set updates only the named field — without it, update_one() replaces
#         the entire document and silently deletes every other field
employees.update_one({"name": "Alice"}, {"$set": {"salary": 90000}})</code></pre>
          </div>
        </div>
        <p class="text-xs text-gray-500 mt-3 px-1"><strong class="text-gray-700">Why this matters:</strong> Every production pymongo application relies on these four operations, and failing to use <code class="font-mono text-xs">$set</code> in <code class="font-mono text-xs">update_one()</code> is the most common beginner mistake &mdash; it silently deletes every field you did not explicitly include in the replacement document.</p>
      </div>
    </div>
  </div>
</div>

<!-- ── Panel 1 — NoSQL Categories ────────────────────────────── -->
<div class="pe-panel pe-panel-anim hidden" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">
          <span class="iconify text-base" data-icon="fa6-solid:layer-group"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">NoSQL Categories</h3>
          <p class="text-xs text-gray-400 mt-0.5">Covers: Document, Key-Value, Column-Family, Graph</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div class="space-y-2">
          <p class="text-xs font-bold uppercase tracking-widest text-brand">Tasks</p>
          <ol class="space-y-1.5 list-none pl-0">
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">1</span><span>For each scenario, name the NoSQL category that fits best: (a) an e-commerce catalog where each product type has different attributes; (b) a session cache that maps a token to a user object for fast lookup; (c) billions of IoT sensor readings arriving every second; (d) a social network that needs to find friends-of-friends within three hops.</span></li>
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">2</span><span>For each of your four answers, name one real-world tool that implements that NoSQL category (e.g., MongoDB, Redis, Cassandra, Neo4j).</span></li>
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">3</span><span>In one sentence each, explain why a standard SQL database would be a worse choice for scenarios (c) and (d).</span></li>
          </ol>
        </div>
      </div>
      <button class="accordion-toggle w-full flex items-center justify-between text-xs font-semibold text-gray-500 px-4 py-2.5 rounded-xl bg-gray-50 border border-gray-100 hover:bg-gray-100 transition-colors" onclick="this.nextElementSibling.classList.toggle('open')">
        <span class="flex items-center gap-2">
          <span class="iconify text-[#CB187D]" data-icon="fa6-solid:eye"></span>
          Show Solution
        </span>
        <span class="iconify accordion-chevron text-gray-400" data-icon="fa6-solid:chevron-down"></span>
      </button>
      <div class="accordion-body">
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-5 py-4 mt-1 space-y-3">
          <p class="text-xs font-bold uppercase tracking-widest text-gray-400">Answers</p>
          <p class="text-sm text-gray-700"><strong>(a) Document &mdash; MongoDB / Firestore.</strong> Each product is a self-contained JSON document, so electronics can have a <code class="font-mono text-xs">wattage</code> field that clothing products simply omit &mdash; no schema migration needed.</p>
          <p class="text-sm text-gray-700"><strong>(b) Key-Value &mdash; Redis / DynamoDB.</strong> A single-token lookup returns the full session object in under a millisecond; there are no joins and no complex queries to perform.</p>
          <p class="text-sm text-gray-700"><strong>(c) Column-Family &mdash; Apache Cassandra / HBase.</strong> SQL write throughput is bounded by a single coordinator node; Cassandra distributes writes across a cluster with no bottleneck, making it purpose-built for time-series and sensor workloads.</p>
          <p class="text-sm text-gray-700"><strong>(d) Graph &mdash; Neo4j / Amazon Neptune.</strong> Finding friends-of-friends in SQL requires chaining multiple self-JOIN operations on a massive table; as the network grows these joins become exponentially slower, whereas a graph database traverses relationships in constant time per hop.</p>
        </div>
        <p class="text-xs text-gray-500 mt-3 px-1"><strong class="text-gray-700">Why this matters:</strong> Choosing the wrong database category for a use case is extremely costly to fix once data is in production &mdash; thinking through your access patterns before you write a single line of code saves months of re-architecture later.</p>
      </div>
    </div>
  </div>
</div>

<!-- ── Panel 2 — Query Operators ──────────────────────────────── -->
<div class="pe-panel pe-panel-anim hidden" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">
          <span class="iconify text-base" data-icon="fa6-solid:magnifying-glass"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Query Operators</h3>
          <p class="text-xs text-gray-400 mt-0.5">Covers: $gt, $lt, $in, array matching, $regex</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div class="space-y-2">
          <p class="text-xs font-bold uppercase tracking-widest text-brand">Tasks</p>
          <ol class="space-y-1.5 list-none pl-0">
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">1</span><span>Seed the <code class="font-mono text-xs">store.products</code> collection with 5 products (Laptop Pro, USB Cable, Mouse Pro, Desk Lamp, Keyboard) each having a <code class="font-mono text-xs">category</code>, <code class="font-mono text-xs">price</code>, and <code class="font-mono text-xs">tags</code> array.</span></li>
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">2</span><span>Use <code class="font-mono text-xs">$gt</code> and <code class="font-mono text-xs">$lt</code> inside a single filter dict to find products with price between 10 and 50 (exclusive).</span></li>
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">3</span><span>Use <code class="font-mono text-xs">$in</code> to find products in category <code class="font-mono text-xs">"electronics"</code> or <code class="font-mono text-xs">"accessories"</code> in a single query, then find all products whose <code class="font-mono text-xs">tags</code> array contains <code class="font-mono text-xs">"sale"</code>.</span></li>
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">4</span><span>Use <code class="font-mono text-xs">$regex</code> with <code class="font-mono text-xs">$options: "i"</code> to find all products whose name contains the word <code class="font-mono text-xs">"Pro"</code> regardless of case.</span></li>
          </ol>
        </div>
      </div>
      <button class="accordion-toggle w-full flex items-center justify-between text-xs font-semibold text-gray-500 px-4 py-2.5 rounded-xl bg-gray-50 border border-gray-100 hover:bg-gray-100 transition-colors" onclick="this.nextElementSibling.classList.toggle('open')">
        <span class="flex items-center gap-2">
          <span class="iconify text-[#CB187D]" data-icon="fa6-solid:eye"></span>
          Show Solution
        </span>
        <span class="iconify accordion-chevron text-gray-400" data-icon="fa6-solid:chevron-down"></span>
      </button>
      <div class="accordion-body">
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-1">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">solution_03.py</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code">
            <pre class="overflow-x-auto pre-reset"><code class="language-python">from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
products = client["store"]["products"]

# Task 1: seed data
products.drop()
products.insert_many([
    {"name": "Laptop Pro",  "category": "electronics", "price": 999, "tags": ["sale", "featured"]},
    {"name": "USB Cable",   "category": "accessories", "price": 12,  "tags": ["sale"]},
    {"name": "Mouse Pro",   "category": "accessories", "price": 45,  "tags": ["new"]},
    {"name": "Desk Lamp",   "category": "furniture",   "price": 35,  "tags": ["featured"]},
    {"name": "Keyboard",    "category": "electronics", "price": 80,  "tags": ["new", "sale"]},
])

# Task 2: both conditions in the same dict = implicit AND
mid = list(products.find({"price": {"$gt": 10, "$lt": 50}}))
print("Price 10–50:", [p["name"] for p in mid])   # USB Cable, Mouse Pro, Desk Lamp

# Task 3a: $in matches any value in the list
multi = list(products.find({"category": {"$in": ["electronics", "accessories"]}}))
print("Elec/Access:", [p["name"] for p in multi])

# Task 3b: querying an array field with a scalar checks for membership
on_sale = list(products.find({"tags": "sale"}))
print("On sale:", [p["name"] for p in on_sale])   # Laptop Pro, USB Cable, Keyboard

# Task 4: $regex with $options "i" = case-insensitive
pro = list(products.find({"name": {"$regex": "Pro", "$options": "i"}}))
print("'Pro' items:", [p["name"] for p in pro])   # Laptop Pro, Mouse Pro</code></pre>
          </div>
        </div>
        <p class="text-xs text-gray-500 mt-3 px-1"><strong class="text-gray-700">Why this matters:</strong> Query operators are the building blocks of every MongoDB filter &mdash; once you understand how <code class="font-mono text-xs">$gt</code>, <code class="font-mono text-xs">$in</code>, and <code class="font-mono text-xs">$regex</code> compose inside a single filter document, you can express virtually any read query without writing a single SQL JOIN.</p>
      </div>
    </div>
  </div>
</div>

<!-- ── Panel 3 — Aggregation Pipeline ────────────────────────── -->
<div class="pe-panel pe-panel-anim hidden" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">
          <span class="iconify text-base" data-icon="fa6-solid:filter"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Aggregation Pipeline</h3>
          <p class="text-xs text-gray-400 mt-0.5">Covers: $match, $group, $sort, $limit</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div class="space-y-2">
          <p class="text-xs font-bold uppercase tracking-widest text-brand">Tasks</p>
          <ol class="space-y-1.5 list-none pl-0">
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">1</span><span>Add a <code class="font-mono text-xs">$match</code> stage to filter the <code class="font-mono text-xs">sales.orders</code> collection to EMEA orders only.</span></li>
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">2</span><span>Add a <code class="font-mono text-xs">$group</code> stage that groups by <code class="font-mono text-xs">product</code>, sums the <code class="font-mono text-xs">amount</code> field as <code class="font-mono text-xs">total</code>, and counts orders using <code class="font-mono text-xs">$sum: 1</code>.</span></li>
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">3</span><span>Add a <code class="font-mono text-xs">$sort</code> stage to order by total revenue descending (<code class="font-mono text-xs">-1</code>).</span></li>
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">4</span><span>Add a <code class="font-mono text-xs">$limit</code> stage to keep the top 3 products, call <code class="font-mono text-xs">aggregate(pipeline)</code>, and print the results.</span></li>
          </ol>
        </div>
      </div>
      <button class="accordion-toggle w-full flex items-center justify-between text-xs font-semibold text-gray-500 px-4 py-2.5 rounded-xl bg-gray-50 border border-gray-100 hover:bg-gray-100 transition-colors" onclick="this.nextElementSibling.classList.toggle('open')">
        <span class="flex items-center gap-2">
          <span class="iconify text-[#CB187D]" data-icon="fa6-solid:eye"></span>
          Show Solution
        </span>
        <span class="iconify accordion-chevron text-gray-400" data-icon="fa6-solid:chevron-down"></span>
      </button>
      <div class="accordion-body">
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-1">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">solution_04.py</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code">
            <pre class="overflow-x-auto pre-reset"><code class="language-python">from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
orders = client["sales"]["orders"]

pipeline = [
    {"$match": {"region": "EMEA"}},         # Task 1: discard non-EMEA documents
    {"$group": {
        "_id": "$product",                  # Task 2: group key
        "total": {"$sum": "$amount"},       # sum the amount field
        "order_count": {"$sum": 1},         # increment by 1 per document
    }},
    {"$sort": {"total": -1}},              # Task 3: -1 = descending
    {"$limit": 3},                         # Task 4: keep top 3 only
]

results = list(orders.aggregate(pipeline))
for r in results:
    print(r["_id"], r["total"], r["order_count"])</code></pre>
          </div>
        </div>
        <p class="text-xs text-gray-500 mt-3 px-1"><strong class="text-gray-700">Why this matters:</strong> The aggregation pipeline is MongoDB&rsquo;s answer to SQL <code class="font-mono text-xs">GROUP BY</code> + <code class="font-mono text-xs">WHERE</code> + <code class="font-mono text-xs">ORDER BY</code> + <code class="font-mono text-xs">LIMIT</code> &mdash; every analytics query your application needs can be expressed with these four stages, and placing <code class="font-mono text-xs">$match</code> first is critical because it reduces the number of documents all later stages must process.</p>
      </div>
    </div>
  </div>
</div>

<!-- ── Panel 4 — NoSQL or SQL? ────────────────────────────────── -->
<div class="pe-panel pe-panel-anim hidden" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">05</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">
          <span class="iconify text-base" data-icon="fa6-solid:code-branch"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">NoSQL or SQL?</h3>
          <p class="text-xs text-gray-400 mt-0.5">Covers: decision framework for real-world scenarios</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div class="space-y-2">
          <p class="text-xs font-bold uppercase tracking-widest text-brand">Tasks</p>
          <p class="text-sm text-gray-600 mb-1.5">For each scenario below: (i) name the most appropriate database type, (ii) name one real-world tool, and (iii) in one sentence explain why SQL would be a worse choice.</p>
          <ol class="space-y-1.5 list-none pl-0">
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">A</span><span>A hospital records system where every patient has the same 20 structured fields, with records frequently joined to appointment and billing tables.</span></li>
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">B</span><span>A real-time leaderboard for a mobile game with 10 million active players where each score update must complete in under 5 milliseconds.</span></li>
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">C</span><span>A content management system where blog posts have irregular custom metadata &mdash; news articles have a <code class="font-mono text-xs">dateline</code>, product reviews have a <code class="font-mono text-xs">rating</code>, video posts have a <code class="font-mono text-xs">duration</code>.</span></li>
            <li class="text-sm text-gray-600 flex gap-2"><span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-[#CB187D] text-white text-[10px] font-bold shrink-0 mt-0.5">D</span><span>A fraud detection engine that must trace rings of connected accounts (A &rarr; B &rarr; C &rarr; D) up to 4 relationship hops within 100 ms.</span></li>
          </ol>
        </div>
      </div>
      <button class="accordion-toggle w-full flex items-center justify-between text-xs font-semibold text-gray-500 px-4 py-2.5 rounded-xl bg-gray-50 border border-gray-100 hover:bg-gray-100 transition-colors" onclick="this.nextElementSibling.classList.toggle('open')">
        <span class="flex items-center gap-2">
          <span class="iconify text-[#CB187D]" data-icon="fa6-solid:eye"></span>
          Show Solution
        </span>
        <span class="iconify accordion-chevron text-gray-400" data-icon="fa6-solid:chevron-down"></span>
      </button>
      <div class="accordion-body">
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-5 py-4 mt-1 space-y-3">
          <p class="text-xs font-bold uppercase tracking-widest text-gray-400">Answers</p>
          <p class="text-sm text-gray-700"><strong>(A) SQL &mdash; PostgreSQL or MySQL.</strong> Every record is identical and the data has natural relationships to other tables, so relational constraints and JOINs are a perfect fit &mdash; a document database would add complexity with zero benefit when the schema never varies.</p>
          <p class="text-sm text-gray-700"><strong>(B) Key-Value &mdash; Redis.</strong> A single-key lookup takes under a millisecond and Redis sorted sets (<code class="font-mono text-xs">ZADD</code> / <code class="font-mono text-xs">ZRANGE</code>) are purpose-built for leaderboards &mdash; SQL could not sustain 10 million concurrent score writes at that latency.</p>
          <p class="text-sm text-gray-700"><strong>(C) Document &mdash; MongoDB or Firestore.</strong> The irregular per-post-type metadata maps naturally to flexible JSON documents &mdash; an SQL table would require either dozens of nullable columns or a complex entity-attribute-value pattern to accommodate the variation.</p>
          <p class="text-sm text-gray-700"><strong>(D) Graph &mdash; Neo4j or Amazon Neptune.</strong> Tracing four-hop chains in SQL requires chaining four self-JOINs on a massive table, which grows exponentially slower as the network expands &mdash; a graph database traverses each hop in constant time regardless of graph size.</p>
        </div>
        <p class="text-xs text-gray-500 mt-3 px-1"><strong class="text-gray-700">Why this matters:</strong> Senior engineers are judged not just on writing correct code but on selecting the right tool for the job &mdash; being able to articulate the trade-offs between SQL and each NoSQL category is a common topic in data engineering interviews and directly influences architecture decisions.</p>
      </div>
    </div>
  </div>
</div>
"""

# ── Read, locate, and replace ─────────────────────────────────────────────────
content = FILE.read_text(encoding="utf-8")

# Find the practice section boundaries
pe_section_start = content.find('<section id="practice">')
if pe_section_start == -1:
    print("❌ Practice section not found"); raise SystemExit(1)

# Locate the body open div inside that section
body_open_idx = content.find(BODY_OPEN, pe_section_start)
if body_open_idx == -1:
    print("❌ Body open div not found"); raise SystemExit(1)

# Locate the first matching SECTION_CLOSE after body_open
section_close_idx = content.find(SECTION_CLOSE, body_open_idx)
if section_close_idx == -1:
    print("❌ Section close not found"); raise SystemExit(1)

# The old body is from body_open through the last </div> before </section>
old_body = content[body_open_idx : section_close_idx]

new_content = content.replace(old_body, NEW_BODY, 1)
if new_content == content:
    print("⚠️  No change — content identical"); raise SystemExit(1)

FILE.write_text(new_content, encoding="utf-8")
print("✅ Practice section replaced")

# ── Verify ────────────────────────────────────────────────────────────────────
c2 = FILE.read_text(encoding="utf-8")
lines2 = c2.split("\n")
pe_start = next(i for i, l in enumerate(lines2) if '<section id="practice"' in l)
next_sec = next(i for i, l in enumerate(lines2[pe_start + 1:], pe_start + 1) if "<section id=" in l)
block = "\n".join(lines2[pe_start:next_sec])
opens = block.count("<div")
closes = block.count("</div>")
tabs = [l.strip() for l in lines2[pe_start:next_sec] if "pe-step-label" in l]
print(f"div diff: {opens - closes}")
print(f"Tab count: {len(tabs)}")
for t in tabs:
    import re
    m = re.search(r'font-bold">(.+?)</span>', t)
    if m: print(" ", m.group(1))
# main balance
main_start = next(i for i, l in enumerate(lines2) if "<main " in l or "<main>" in l)
main_end   = next(i for i, l in enumerate(lines2) if "</main>" in l)
blk2 = "\n".join(lines2[main_start:main_end + 1])
print(f"main div diff: {blk2.count('<div') - blk2.count('</div>')}")
