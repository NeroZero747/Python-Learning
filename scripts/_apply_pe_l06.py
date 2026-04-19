"""
Fix Practice Exercises section in Lesson 06 — NoSQL When Tables Aren't Enough
Changes:
  - All 4 existing panels: numbered sub-tasks, "Why this matters" sentence
  - Tab 1 (DB Decision): solution put behind accordion toggle
  - Add 5th tab: Query Operators
"""
import pathlib, re

FILE = pathlib.Path(
    r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_04_data_engineering"
    r"\lesson06_nosql_when_tables_arent_enough.html"
)

# ─── New practice body ────────────────────────────────────────────────────────
NEW_BODY = """\
<div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist"><button onclick="switchPeTab(0)" class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span><span class="pe-step-label text-xs font-bold">Insert &amp; Query</span></button>
<button onclick="switchPeTab(1)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span><span class="pe-step-label text-xs font-bold">NoSQL Categories</span></button>
<button onclick="switchPeTab(2)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span><span class="pe-step-label text-xs font-bold">Query Operators</span></button>
<button onclick="switchPeTab(3)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span><span class="pe-step-label text-xs font-bold">Aggregation Pipeline</span></button>
<button onclick="switchPeTab(4)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span><span class="pe-step-label text-xs font-bold">NoSQL or SQL?</span></button></div>

<!-- ── Panel 0 — Insert & Query ──────────────────── -->
<div class="pe-panel pe-panel-anim" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Insert &amp; Query</h3>
          <p class="text-xs text-gray-500 mt-0.5">Connect, insert, filter, and update with pymongo</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-2 text-brand">Tasks</p>
          <ol class="text-sm text-gray-600 space-y-1.5 list-decimal list-inside">
            <li>Connect to MongoDB on <code class="font-mono text-xs">localhost:27017</code> and select the <code class="font-mono text-xs">company.employees</code> collection.</li>
            <li>Use <code class="font-mono text-xs">insert_many()</code> to add Alice (engineer, salary 92000, a <code class="font-mono text-xs">languages</code> list), Bob (manager, salary 85000, a <code class="font-mono text-xs">team_size</code> integer), and Carol (analyst, salary 72000, a <code class="font-mono text-xs">tools</code> list). Notice that each document has different optional fields.</li>
            <li>Use <code class="font-mono text-xs">find()</code> with a <code class="font-mono text-xs">$gt</code> filter to retrieve all employees earning more than $80,000, then print each person's name and salary.</li>
            <li>Use <code class="font-mono text-xs">update_one()</code> with <code class="font-mono text-xs">$set</code> to change Alice's salary to $90,000. Do <em>not</em> pass the full document — only the field you want to change.</li>
          </ol>
        </div>
      </div>
      <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
        <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
          <div class="flex items-center gap-3">
            <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
              <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
              <span class="text-[11px] font-semibold text-gray-400">exercise_01.py</span>
            </div>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-python">from pymongo import MongoClient

# Task 1: connect and select collection
client = MongoClient(&quot;mongodb://localhost:27017/&quot;)
employees = client[&quot;company&quot;][&quot;employees&quot;]

# Task 2: TODO — insert Alice, Bob, and Carol with different optional fields

# Task 3: TODO — find employees with salary &gt; 80000 and print name + salary

# Task 4: TODO — update Alice's salary to 90000 using $set</code></pre>
        </div>
      </div>
      <div>
        <button class="accordion-toggle w-full flex items-center justify-between mt-4 px-4 py-3 rounded-xl bg-gray-50 border border-gray-100 text-sm font-semibold text-gray-700 hover:bg-[#fdf0f7] hover:border-[#f5c6e0] transition-colors" onclick="toggleAccordion(this)">
          <span class="flex items-center gap-2"><span class="iconify text-brand" data-icon="fa6-solid:eye"></span> Show Solution</span>
          <span class="iconify accordion-chevron text-gray-400 transition-transform" data-icon="fa6-solid:chevron-down"></span>
        </button>
        <div class="accordion-body">
          <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-3">
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
    print(emp["name"], emp["salary"])   # prints: Alice 92000  /  Bob 85000

# Task 4: $set updates only the named field — without it, update_one() replaces
#         the *entire* document and silently deletes every other field
employees.update_one({"name": "Alice"}, {"$set": {"salary": 90000}})</code></pre>
            </div>
          </div>
        </div>
      </div>
      <p class="text-xs text-gray-500 italic mt-1"><span class="font-semibold not-italic text-gray-600">Why this matters:</span> Every production pymongo application relies on these four operations, and failing to use <code class="font-mono text-[11px]">$set</code> in <code class="font-mono text-[11px]">update_one()</code> is the most common beginner mistake — it silently deletes every field you did not explicitly include in the replacement document.</p>
    </div>
  </div>
</div>

<!-- ── Panel 1 — NoSQL Categories ──────────────────── -->
<div class="pe-panel pe-panel-anim hidden" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">NoSQL Categories</h3>
          <p class="text-xs text-gray-500 mt-0.5">Match data scenarios to the correct NoSQL type</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-2 text-brand">Tasks</p>
          <ol class="text-sm text-gray-600 space-y-1.5 list-decimal list-inside">
            <li>For each scenario below, name the NoSQL category (Document, Key-Value, Column-Family, or Graph) that fits best:
              <ul class="mt-1.5 ml-4 space-y-1 list-disc list-inside text-gray-500">
                <li>(a) An e-commerce catalog where each product type has different attributes.</li>
                <li>(b) A session cache that maps a random token to a user object for fast lookup.</li>
                <li>(c) Billions of IoT sensor readings arriving every second from thousands of devices.</li>
                <li>(d) A social network that needs to find friends-of-friends within three relationship hops.</li>
              </ul>
            </li>
            <li>For each of your four answers, name one real-world tool that implements that NoSQL category.</li>
            <li>In one sentence each, explain why a standard SQL database would be a worse choice for scenarios (c) and (d).</li>
          </ol>
        </div>
      </div>
      <div>
        <button class="accordion-toggle w-full flex items-center justify-between mt-2 px-4 py-3 rounded-xl bg-gray-50 border border-gray-100 text-sm font-semibold text-gray-700 hover:bg-[#fdf0f7] hover:border-[#f5c6e0] transition-colors" onclick="toggleAccordion(this)">
          <span class="flex items-center gap-2"><span class="iconify text-brand" data-icon="fa6-solid:eye"></span> Show Solution</span>
          <span class="iconify accordion-chevron text-gray-400 transition-transform" data-icon="fa6-solid:chevron-down"></span>
        </button>
        <div class="accordion-body">
          <div class="rounded-xl border border-gray-100 bg-gray-50 px-5 py-4 mt-3 space-y-3">
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-1">Answers</p>
            <p class="text-sm text-gray-700"><span class="font-semibold">(a) Document — MongoDB / Firestore.</span> Each product is a self-contained JSON document, so electronics can have a <code class="font-mono text-xs">wattage</code> field that clothing products simply omit — no schema migration needed.</p>
            <p class="text-sm text-gray-700"><span class="font-semibold">(b) Key-Value — Redis / DynamoDB.</span> A single-token lookup returns the full session object in under a millisecond; there are no joins and no complex queries to perform.</p>
            <p class="text-sm text-gray-700"><span class="font-semibold">(c) Column-Family — Apache Cassandra / HBase.</span> SQL struggles here because write throughput is bounded by a single coordinator node; Cassandra distributes writes across a cluster with no single point of bottleneck, making it purpose-built for time-series and sensor workloads.</p>
            <p class="text-sm text-gray-700"><span class="font-semibold">(d) Graph — Neo4j / Amazon Neptune.</span> Finding friends-of-friends in SQL requires chaining multiple self-JOIN operations across a massive table; as the network grows, these joins become exponentially slower, whereas a graph database traverses relationships in constant time per hop.</p>
          </div>
        </div>
      </div>
      <p class="text-xs text-gray-500 italic mt-1"><span class="font-semibold not-italic text-gray-600">Why this matters:</span> Choosing the wrong database category for a use case is extremely costly to fix once data is in production — thinking through your access patterns before you write a single line of code saves months of re-architecture later.</p>
    </div>
  </div>
</div>

<!-- ── Panel 2 — Query Operators ──────────────────── -->
<div class="pe-panel pe-panel-anim hidden" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Query Operators</h3>
          <p class="text-xs text-gray-500 mt-0.5">Practice $gt, $in, array matching, and $regex</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-2 text-brand">Tasks</p>
          <ol class="text-sm text-gray-600 space-y-1.5 list-decimal list-inside">
            <li>Find all products where <code class="font-mono text-xs">price</code> is between 10 and 50 (exclusive). Use <code class="font-mono text-xs">$gt</code> and <code class="font-mono text-xs">$lt</code> inside a single filter document.</li>
            <li>Find all products whose <code class="font-mono text-xs">category</code> is either <code class="font-mono text-xs">"electronics"</code> or <code class="font-mono text-xs">"accessories"</code>. Use the <code class="font-mono text-xs">$in</code> operator instead of two separate queries.</li>
            <li>Find all products where the <code class="font-mono text-xs">tags</code> array contains the string <code class="font-mono text-xs">"sale"</code>. You can query an array field directly — no special operator is needed for a simple element-match.</li>
            <li>Find all products whose <code class="font-mono text-xs">name</code> contains the word <code class="font-mono text-xs">"Pro"</code> (case-insensitive). Use <code class="font-mono text-xs">$regex</code> with the <code class="font-mono text-xs">$options: "i"</code> flag.</li>
          </ol>
        </div>
      </div>
      <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
        <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
          <div class="flex items-center gap-3">
            <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
              <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
              <span class="text-[11px] font-semibold text-gray-400">exercise_03.py</span>
            </div>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-python">from pymongo import MongoClient

client = MongoClient(&quot;mongodb://localhost:27017/&quot;)
products = client[&quot;store&quot;][&quot;products&quot;]

# Seed data — run this once to populate the collection
products.drop()
products.insert_many([
    {&quot;name&quot;: &quot;Laptop Pro&quot;,  &quot;category&quot;: &quot;electronics&quot;, &quot;price&quot;: 999, &quot;tags&quot;: [&quot;sale&quot;, &quot;featured&quot;]},
    {&quot;name&quot;: &quot;USB Cable&quot;,   &quot;category&quot;: &quot;accessories&quot;, &quot;price&quot;: 12,  &quot;tags&quot;: [&quot;sale&quot;]},
    {&quot;name&quot;: &quot;Mouse Pro&quot;,   &quot;category&quot;: &quot;accessories&quot;, &quot;price&quot;: 45,  &quot;tags&quot;: [&quot;new&quot;]},
    {&quot;name&quot;: &quot;Desk Lamp&quot;,   &quot;category&quot;: &quot;furniture&quot;,   &quot;price&quot;: 35,  &quot;tags&quot;: [&quot;featured&quot;]},
    {&quot;name&quot;: &quot;Keyboard&quot;,    &quot;category&quot;: &quot;electronics&quot;, &quot;price&quot;: 80,  &quot;tags&quot;: [&quot;new&quot;, &quot;sale&quot;]},
])

# Task 1: TODO — find products with price &gt; 10 AND price &lt; 50

# Task 2: TODO — find products in "electronics" or "accessories" using $in

# Task 3: TODO — find products whose tags array contains "sale"

# Task 4: TODO — find products whose name contains "Pro" (case-insensitive)</code></pre>
        </div>
      </div>
      <div>
        <button class="accordion-toggle w-full flex items-center justify-between mt-4 px-4 py-3 rounded-xl bg-gray-50 border border-gray-100 text-sm font-semibold text-gray-700 hover:bg-[#fdf0f7] hover:border-[#f5c6e0] transition-colors" onclick="toggleAccordion(this)">
          <span class="flex items-center gap-2"><span class="iconify text-brand" data-icon="fa6-solid:eye"></span> Show Solution</span>
          <span class="iconify accordion-chevron text-gray-400 transition-transform" data-icon="fa6-solid:chevron-down"></span>
        </button>
        <div class="accordion-body">
          <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-3">
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

# Task 1: both conditions go inside the same filter dict (implicit AND)
mid_range = list(products.find({"price": {"$gt": 10, "$lt": 50}}))
print("Price 10–50:", [p["name"] for p in mid_range])   # USB Cable, Mouse Pro, Desk Lamp

# Task 2: $in matches any value in the provided list
multi_cat = list(products.find({"category": {"$in": ["electronics", "accessories"]}}))
print("Electronics/accessories:", [p["name"] for p in multi_cat])

# Task 3: querying an array field with a scalar value checks for membership
on_sale = list(products.find({"tags": "sale"}))
print("On sale:", [p["name"] for p in on_sale])   # Laptop Pro, USB Cable, Keyboard

# Task 4: $regex for pattern matching; $options "i" makes it case-insensitive
pro_items = list(products.find({"name": {"$regex": "Pro", "$options": "i"}}))
print("'Pro' in name:", [p["name"] for p in pro_items])   # Laptop Pro, Mouse Pro</code></pre>
            </div>
          </div>
        </div>
      </div>
      <p class="text-xs text-gray-500 italic mt-1"><span class="font-semibold not-italic text-gray-600">Why this matters:</span> Query operators are the building blocks of every MongoDB filter — once you understand how <code class="font-mono text-[11px]">$gt</code>, <code class="font-mono text-[11px]">$in</code>, and <code class="font-mono text-[11px]">$regex</code> compose inside a single filter document, you can express virtually any read query without writing a single SQL JOIN.</p>
    </div>
  </div>
</div>

<!-- ── Panel 3 — Aggregation Pipeline ──────────────────── -->
<div class="pe-panel pe-panel-anim hidden" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Aggregation Pipeline</h3>
          <p class="text-xs text-gray-500 mt-0.5">Build a $match → $group → $sort → $limit pipeline</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-2 text-brand">Tasks</p>
          <ol class="text-sm text-gray-600 space-y-1.5 list-decimal list-inside">
            <li>Add a <code class="font-mono text-xs">$match</code> stage to filter the <code class="font-mono text-xs">orders</code> collection to only EMEA orders.</li>
            <li>Add a <code class="font-mono text-xs">$group</code> stage that groups documents by <code class="font-mono text-xs">product</code>, computes the total revenue using <code class="font-mono text-xs">$sum</code> on the <code class="font-mono text-xs">amount</code> field, and also counts the number of orders using <code class="font-mono text-xs">$sum: 1</code>.</li>
            <li>Add a <code class="font-mono text-xs">$sort</code> stage to order results by total revenue descending (<code class="font-mono text-xs">-1</code>).</li>
            <li>Add a <code class="font-mono text-xs">$limit</code> stage to keep only the top 3 products, then call <code class="font-mono text-xs">aggregate()</code> and print the results.</li>
          </ol>
        </div>
      </div>
      <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
        <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
          <div class="flex items-center gap-3">
            <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
              <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
              <span class="text-[11px] font-semibold text-gray-400">exercise_04.py</span>
            </div>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-python">from pymongo import MongoClient

client = MongoClient(&quot;mongodb://localhost:27017/&quot;)
orders = client[&quot;sales&quot;][&quot;orders&quot;]

pipeline = [
    # Task 1: TODO — $match to keep only region == &quot;EMEA&quot;

    # Task 2: TODO — $group by product, sum amount as &quot;total&quot;, count orders

    # Task 3: TODO — $sort by total descending

    # Task 4: TODO — $limit to top 3
]

results = list(orders.aggregate(pipeline))
for r in results:
    print(r)</code></pre>
        </div>
      </div>
      <div>
        <button class="accordion-toggle w-full flex items-center justify-between mt-4 px-4 py-3 rounded-xl bg-gray-50 border border-gray-100 text-sm font-semibold text-gray-700 hover:bg-[#fdf0f7] hover:border-[#f5c6e0] transition-colors" onclick="toggleAccordion(this)">
          <span class="flex items-center gap-2"><span class="iconify text-brand" data-icon="fa6-solid:eye"></span> Show Solution</span>
          <span class="iconify accordion-chevron text-gray-400 transition-transform" data-icon="fa6-solid:chevron-down"></span>
        </button>
        <div class="accordion-body">
          <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg mt-3">
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
    {"$match": {"region": "EMEA"}},                    # Task 1: discard non-EMEA docs
    {"$group": {
        "_id": "$product",                              # Task 2: group key
        "total": {"$sum": "$amount"},                   # sum the amount field
        "order_count": {"$sum": 1},                     # increment by 1 per doc
    }},
    {"$sort": {"total": -1}},                          # Task 3: -1 = descending
    {"$limit": 3},                                     # Task 4: keep top 3 only
]

results = list(orders.aggregate(pipeline))
for r in results:
    print(r["_id"], r["total"], r["order_count"])</code></pre>
            </div>
          </div>
        </div>
      </div>
      <p class="text-xs text-gray-500 italic mt-1"><span class="font-semibold not-italic text-gray-600">Why this matters:</span> The aggregation pipeline is MongoDB's equivalent of SQL <code class="font-mono text-[11px]">GROUP BY</code> combined with <code class="font-mono text-[11px]">WHERE</code>, <code class="font-mono text-[11px]">ORDER BY</code>, and <code class="font-mono text-[11px]">LIMIT</code> — every analytics query your application needs can be expressed with these four stages, and the order of those stages directly affects both the result and the query's performance.</p>
    </div>
  </div>
</div>

<!-- ── Panel 4 — NoSQL or SQL? ──────────────────── -->
<div class="pe-panel pe-panel-anim hidden" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">05</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">NoSQL or SQL?</h3>
          <p class="text-xs text-gray-500 mt-0.5">Apply the decision framework to real-world scenarios</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-2 text-brand">Tasks</p>
          <p class="text-sm text-gray-600 mb-2">For each scenario below, (i) name the most appropriate database type, (ii) name one real-world tool, and (iii) write one sentence explaining why the alternatives would be a poor fit.</p>
          <ol class="text-sm text-gray-600 space-y-1.5 list-decimal list-inside">
            <li>A hospital patient records system where every patient has exactly the same 20 structured fields (name, DOB, blood type, …) and records are frequently joined to appointment and billing tables.</li>
            <li>A real-time leaderboard for a mobile game with 10 million active players, where each score update must complete in under 5 milliseconds.</li>
            <li>A content management system where blog posts have irregular custom metadata fields — news articles have a <code class="font-mono text-xs">dateline</code>, product reviews have a <code class="font-mono text-xs">rating</code>, and video posts have a <code class="font-mono text-xs">duration</code>.</li>
            <li>A fraud detection engine that must find rings of connected suspicious accounts (A → B → C → D) within 100 ms, tracing up to 4 relationship hops.</li>
          </ol>
        </div>
      </div>
      <div>
        <button class="accordion-toggle w-full flex items-center justify-between px-4 py-3 rounded-xl bg-gray-50 border border-gray-100 text-sm font-semibold text-gray-700 hover:bg-[#fdf0f7] hover:border-[#f5c6e0] transition-colors" onclick="toggleAccordion(this)">
          <span class="flex items-center gap-2"><span class="iconify text-brand" data-icon="fa6-solid:eye"></span> Show Solution</span>
          <span class="iconify accordion-chevron text-gray-400 transition-transform" data-icon="fa6-solid:chevron-down"></span>
        </button>
        <div class="accordion-body">
          <div class="rounded-xl border border-gray-100 bg-gray-50 px-5 py-4 mt-3 space-y-3">
            <p class="text-xs font-bold uppercase tracking-widest text-gray-400 mb-1">Answers</p>
            <p class="text-sm text-gray-700"><span class="font-semibold">(1) SQL — PostgreSQL or MySQL.</span> Every record is identical and the data has natural relationships to other tables (appointments, billing), so relational constraints and JOINs are a perfect fit. A document database would add complexity with zero benefit when the schema never varies.</p>
            <p class="text-sm text-gray-700"><span class="font-semibold">(2) Key-Value — Redis.</span> A single-key lookup (<code class="font-mono text-xs">player:42:score</code>) takes under a millisecond; Redis sorted sets (<code class="font-mono text-xs">ZADD</code> / <code class="font-mono text-xs">ZRANGE</code>) are purpose-built for leaderboards and an SQL database could not sustain 10 million concurrent score writes at that latency.</p>
            <p class="text-sm text-gray-700"><span class="font-semibold">(3) Document — MongoDB or Firestore.</span> The irregular per-post-type metadata (dateline, rating, duration) maps naturally to flexible JSON documents; an SQL table would require either dozens of nullable columns or a complex entity-attribute-value pattern to accommodate the variation.</p>
            <p class="text-sm text-gray-700"><span class="font-semibold">(4) Graph — Neo4j or Amazon Neptune.</span> Tracing four-hop relationship chains in SQL requires chaining four self-JOINs on a potentially enormous table, which grows exponentially slower as the network expands; a graph database traverses each relationship hop in constant time regardless of graph size.</p>
          </div>
        </div>
      </div>
      <p class="text-xs text-gray-500 italic mt-1"><span class="font-semibold not-italic text-gray-600">Why this matters:</span> Senior engineers are judged not just on writing correct code but on selecting the right tool for the job — being able to articulate the trade-offs between SQL and each NoSQL category is a skill that directly influences architecture decisions and is a common topic in data engineering interviews.</p>
    </div>
  </div>
</div>"""

# ─── Find and replace ────────────────────────────────────────────────────────
content = FILE.read_text(encoding="utf-8")

# Locate the practice section body boundaries
# Start: the tablist div (unique in the file)
START = '<div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist"><button onclick="switchPeTab(0)"'

# End: we need to find the last </div> of the 4th pe-panel (just before the body close)
# Strategy: find the start of the tablist, then scan forward counting div depth
# to find the balanced close of all 4 panels

start_idx = content.find(START)
if start_idx == -1:
    print("❌ START marker not found")
    raise SystemExit(1)

# Find end of the content we want to replace:
# Move past the start, find the closing of the last pe-panel
# The pe-panel at depth 0 closes after 4 panels; we can detect by
# counting backward from the body close tag
body_open = '    <div class="bg-white px-8 py-7 space-y-6">'
# Find section end marker
practice_section_close = '    </div>\n  </div>\n</section>'
practice_close_idx = content.find(practice_section_close, start_idx)
if practice_close_idx == -1:
    print("❌ Practice section close not found")
    raise SystemExit(1)

# The content to replace is from START to practice_close_idx (exclusive)
old_body = content[start_idx:practice_close_idx]

# Verify no-double replacement using the full unique START marker
count = content.count(START)
if count != 1:
    print(f"⚠️  Start anchor found {count} times — aborting")
    raise SystemExit(1)

new_content = content.replace(old_body, NEW_BODY, 1)

if new_content == content:
    print("⚠️  No change made — content identical after replace")
    raise SystemExit(1)

FILE.write_text(new_content, encoding="utf-8")
print("✅ Practice section replaced")

# ─── Quick verification ───────────────────────────────────────────────────────
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
    print(" ", t[:80])
