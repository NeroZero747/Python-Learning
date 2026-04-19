"""
Replace the entire #code-examples section body content in lesson06 with
5 fully-spec-compliant tabs:
  0 – MongoDB CRUD
  1 – Query Operators
  2 – Decision Framework
  3 – Redis Cache
  4 – Aggregation Pipeline

Each panel has: task-box, Style-A code block with terminal pane, amber tip.
"""

import pathlib, re, sys

TARGET = pathlib.Path(
    r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_04_data_engineering"
    r"\lesson06_nosql_when_tables_arent_enough.html"
)

# ── New content -----------------------------------------------------------
NEW_TABS = '''\
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        <button onclick="switchCeTab(0)" class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:file-code"></span>
          <span class="ce-step-label text-xs font-bold">MongoDB CRUD</span>
        </button>
        <button onclick="switchCeTab(1)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:magnifying-glass"></span>
          <span class="ce-step-label text-xs font-bold">Query Operators</span>
        </button>
        <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:code-branch"></span>
          <span class="ce-step-label text-xs font-bold">Decision Framework</span>
        </button>
        <button onclick="switchCeTab(3)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:key"></span>
          <span class="ce-step-label text-xs font-bold">Redis Cache</span>
        </button>
        <button onclick="switchCeTab(4)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:layer-group"></span>
          <span class="ce-step-label text-xs font-bold">Aggregation</span>
        </button>
      </div>
'''

# Helper: build a complete CE panel
def panel(num_str, title, difficulty, diff_color, diff_icon,
          icon, filename, code_html, terminal_cmd, terminal_output, tip_html,
          hidden=False):
    hidden_cls = " hidden" if hidden else ""
    diff_bg = {"Beginner": "emerald", "Intermediate": "amber"}[difficulty]
    diff_text = {"Beginner": "emerald", "Intermediate": "amber"}[difficulty]
    return f'''\
      <div class="ce-panel ce-panel-anim{hidden_cls}" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{num_str}</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="{icon}"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">{title}</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-{diff_bg}-50 text-{diff_text}-600 border border-{diff_bg}-200">
                    <span class="iconify text-[10px]" data-icon="{diff_icon}"></span> {difficulty}
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
                <p class="text-sm text-gray-600">{tip_desc}</p>
              </div>
            </div>
            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">{filename}</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">{code_html}</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ python {filename}</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">{terminal_output}</div>
              </div>
            </div>
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">{tip_html}</p>
            </div>
          </div>
        </div>
      </div>
'''

# Python doesn't support inline lambdas with multiple lines, so build each panel manually

P1_CODE = (
    'from pymongo import MongoClient\n'
    '\n'
    '# Connect to MongoDB running locally on the default port\n'
    'client = MongoClient(&quot;mongodb://localhost:27017/&quot;)\n'
    'db = client[&quot;ecommerce&quot;]           # select (or create) the database\n'
    'products = db[&quot;products&quot;]           # select (or create) the collection\n'
    '\n'
    '# CREATE — insert two documents; they can have completely different fields\n'
    'products.insert_many([\n'
    '    {&quot;sku&quot;: &quot;LAPTOP-001&quot;, &quot;name&quot;: &quot;Pro Laptop 15&quot;, &quot;price&quot;: 1299.99,\n'
    '     &quot;specs&quot;: {&quot;ram_gb&quot;: 16, &quot;storage_tb&quot;: 1}},   # nested sub-document is valid\n'
    '    {&quot;sku&quot;: &quot;BOOK-042&quot;,   &quot;name&quot;: &quot;Python for Engineers&quot;, &quot;price&quot;: 39.99,\n'
    '     &quot;author&quot;: &quot;Jane Smith&quot;}      # no &quot;specs&quot; field — flexible schema allows this\n'
    '])\n'
    'print(f&quot;Inserted {products.count_documents({})} products&quot;)\n'
    '\n'
    '# READ — find_one() returns the first matching document as a Python dict (or None)\n'
    'laptop = products.find_one({&quot;sku&quot;: &quot;LAPTOP-001&quot;})\n'
    'print(f&quot;Found: {laptop[&#39;name&#39;]} @ ${laptop[&#39;price&#39;]}&quot;)\n'
    '\n'
    '# UPDATE — $set modifies only named fields; omitting $set replaces the WHOLE document\n'
    'products.update_one({&quot;sku&quot;: &quot;LAPTOP-001&quot;}, {&quot;$set&quot;: {&quot;in_stock&quot;: True}})\n'
    '\n'
    '# DELETE — delete_many({}) with an empty filter removes the entire collection\n'
    'products.delete_many({&quot;discontinued&quot;: True})\n'
    'print(&quot;Update and delete applied&quot;)'
)

P2_CODE = (
    'from pymongo import MongoClient\n'
    '\n'
    'client = MongoClient(&quot;mongodb://localhost:27017/&quot;)\n'
    'products = client[&quot;ecommerce&quot;][&quot;products&quot;]\n'
    '\n'
    '# Exact match — returns all documents where category equals &quot;laptop&quot;\n'
    'laptops = list(products.find({&quot;category&quot;: &quot;laptop&quot;}))\n'
    '\n'
    '# Range query — $lt (less than) and $gt (greater than)\n'
    'affordable = list(products.find({&quot;price&quot;: {&quot;$lt&quot;: 500, &quot;$gt&quot;: 50}}))\n'
    '\n'
    '# $in — matches any value in the list (equivalent to SQL&#39;s IN clause)\n'
    'selected = list(products.find({&quot;brand&quot;: {&quot;$in&quot;: [&quot;Dell&quot;, &quot;Lenovo&quot;, &quot;HP&quot;]}}))\n'
    '\n'
    '# Projection — second arg picks which fields to return (1 = include, 0 = exclude)\n'
    'names_only = list(products.find(\n'
    '    {&quot;in_stock&quot;: True},\n'
    '    {&quot;name&quot;: 1, &quot;price&quot;: 1, &quot;_id&quot;: 0}   # return name + price; exclude _id explicitly\n'
    '))\n'
    '\n'
    '# count_documents() is faster than len(list(find(...))) for large collections\n'
    'count = products.count_documents({&quot;price&quot;: {&quot;$gt&quot;: 1000}})\n'
    'print(f&quot;Premium products: {count}&quot;)\n'
    'print(f&quot;Affordable options: {len(affordable)}&quot;)\n'
    'print(f&quot;First result: {names_only[0] if names_only else &#39;none&#39;}&quot;)'
)

P3_CODE = (
    'def choose_database(requirements: dict) -&gt; str:\n'
    '    &quot;&quot;&quot;Return the recommended database type given a requirements checklist.&quot;&quot;&quot;\n'
    '    if requirements.get(&quot;acid_transactions&quot;) or requirements.get(&quot;complex_joins&quot;):\n'
    '        return &quot;SQL (PostgreSQL / MySQL)&quot;       # strong consistency is non-negotiable\n'
    '    if requirements.get(&quot;sub_ms_latency&quot;) and requirements.get(&quot;simple_key_lookup&quot;):\n'
    '        return &quot;Key-Value (Redis)&quot;               # speed + simplicity wins here\n'
    '    if requirements.get(&quot;flexible_schema&quot;) or requirements.get(&quot;nested_documents&quot;):\n'
    '        return &quot;Document DB (MongoDB)&quot;           # schema-free JSON storage\n'
    '    if requirements.get(&quot;relationship_traversal&quot;):\n'
    '        return &quot;Graph DB (Neo4j)&quot;                # traversal is native, no JOIN needed\n'
    '    return &quot;SQL (default — start here when unsure)&quot;\n'
    '\n'
    '# Scenario A — online banking\n'
    'print(choose_database({\n'
    '    &quot;acid_transactions&quot;: True,   # transfers must be atomic\n'
    '    &quot;complex_joins&quot;: True        # customers, accounts, and transactions are linked\n'
    '}))\n'
    '\n'
    '# Scenario B — e-commerce product catalog\n'
    'print(choose_database({\n'
    '    &quot;flexible_schema&quot;: True,     # laptops have specs; books have ISBNs\n'
    '    &quot;nested_documents&quot;: True     # store specs as a sub-document\n'
    '}))\n'
    '\n'
    '# Scenario C — user session management\n'
    'print(choose_database({\n'
    '    &quot;simple_key_lookup&quot;: True,   # look up session_id -&gt; session data\n'
    '    &quot;sub_ms_latency&quot;: True       # page load must respond in under 1 ms\n'
    '}))'
)

P4_CODE = (
    'import redis, json\n'
    '\n'
    '# decode_responses=True returns Python strings instead of raw bytes\n'
    'r = redis.Redis(host=&quot;localhost&quot;, port=6379, decode_responses=True)\n'
    '\n'
    'def get_user_profile(user_id: int) -&gt; dict:\n'
    '    cache_key = f&quot;user:{user_id}&quot;      # prefix key to namespace entries by domain\n'
    '    cached = r.get(cache_key)           # returns None if key is absent or has expired\n'
    '    if cached:\n'
    '        print(f&quot;  Cache HIT  — {cache_key}&quot;)\n'
    '        return json.loads(cached)       # deserialise the stored JSON string\n'
    '\n'
    '    # Cache miss — query the database, then store result with a TTL\n'
    '    profile = {&quot;id&quot;: user_id, &quot;name&quot;: f&quot;User{user_id}&quot;, &quot;role&quot;: &quot;analyst&quot;}\n'
    '    r.setex(cache_key, 300, json.dumps(profile))  # store for 300 seconds (5 min)\n'
    '    print(f&quot;  Cache MISS — {cache_key} stored for 300 s&quot;)\n'
    '    return profile\n'
    '\n'
    'print(get_user_profile(42))     # first call: cache miss, written to Redis\n'
    'print(get_user_profile(42))     # second call: served from Redis, no DB query\n'
    'print(f&quot;TTL remaining: {r.ttl(&#39;user:42&#39;)} seconds&quot;)'
)

P5_CODE = (
    'from pymongo import MongoClient\n'
    '\n'
    'client = MongoClient(&quot;mongodb://localhost:27017/&quot;)\n'
    'orders = client[&quot;ecommerce&quot;][&quot;orders&quot;]\n'
    '\n'
    '# Aggregation pipeline — data flows through each stage sequentially\n'
    'pipeline = [\n'
    '    # Stage 1: $match filters early — less data to process in later stages\n'
    '    {&quot;$match&quot;: {&quot;status&quot;: &quot;completed&quot;}},\n'
    '\n'
    '    # Stage 2: $group acts like SQL GROUP BY; _id is the grouping key\n'
    '    {&quot;$group&quot;: {\n'
    '        &quot;_id&quot;: &quot;$region&quot;,                    # group documents by their &quot;region&quot; field\n'
    '        &quot;total_revenue&quot;: {&quot;$sum&quot;: &quot;$amount&quot;},# sum the &quot;amount&quot; field for each group\n'
    '        &quot;order_count&quot;:   {&quot;$sum&quot;: 1}         # count documents per group (like COUNT(*))\n'
    '    }},\n'
    '\n'
    '    # Stage 3: $sort orders results (-1 = descending, highest revenue first)\n'
    '    {&quot;$sort&quot;: {&quot;total_revenue&quot;: -1}},\n'
    '\n'
    '    # Stage 4: $limit keeps only the top 5 groups\n'
    '    {&quot;$limit&quot;: 5}\n'
    ']\n'
    '\n'
    'results = list(orders.aggregate(pipeline))   # execute and materialise the cursor\n'
    'for row in results:\n'
    '    print(f&quot;{row[&#39;_id&#39;]:12}  revenue=${row[&#39;total_revenue&#39;]:,.2f}  orders={row[&#39;order_count&#39;]}&quot;)'
)

# ── Build all 5 panels with manual string building (avoids f-string collision) ──

def make_panel(num_str, title, difficulty, diff_icon, icon, filename,
               code_html, terminal_cmd, terminal_output, what_it_does, tip_html,
               hidden=False):
    diff_bg = "emerald" if difficulty == "Beginner" else "amber"
    hidden_cls = " hidden" if hidden else ""
    return (
        f'      <div class="ce-panel ce-panel-anim{hidden_cls}" role="tabpanel">\n'
        f'        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">\n'
        f'          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">\n'
        f'            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{num_str}</span>\n'
        f'            <div class="relative flex items-center gap-3">\n'
        f'              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">\n'
        f'                <span class="iconify text-base" data-icon="{icon}"></span>\n'
        f'              </span>\n'
        f'              <div>\n'
        f'                <h3 class="font-bold text-gray-800">{title}</h3>\n'
        f'                <div class="flex items-center gap-2 mt-1">\n'
        f'                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-{diff_bg}-50 text-{diff_bg}-600 border border-{diff_bg}-200">\n'
        f'                    <span class="iconify text-[10px]" data-icon="{diff_icon}"></span> {difficulty}\n'
        f'                  </span>\n'
        f'                </div>\n'
        f'              </div>\n'
        f'            </div>\n'
        f'          </div>\n'
        f'          <div class="px-6 py-5 space-y-4">\n'
        f'            <div class="flex items-start gap-3 rounded-xl p-4 task-box">\n'
        f'              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>\n'
        f'              <div>\n'
        f'                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>\n'
        f'                <p class="text-sm text-gray-600">{what_it_does}</p>\n'
        f'              </div>\n'
        f'            </div>\n'
        f'            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">\n'
        f'              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">\n'
        f'                <div class="flex items-center gap-3">\n'
        f'                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">\n'
        f'                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>\n'
        f'                    <span class="text-[11px] font-semibold text-gray-400">{filename}</span>\n'
        f'                  </div>\n'
        f'                </div>\n'
        f'                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>\n'
        f'              </div>\n'
        f'              <div class="bg-code">\n'
        f'                <pre class="overflow-x-auto pre-reset"><code class="language-python">{code_html}</code></pre>\n'
        f'              </div>\n'
        f'              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">\n'
        f'                <div class="flex items-center gap-2 mb-1.5">\n'
        f'                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>\n'
        f'                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>\n'
        f'                  <span class="text-[10px] text-gray-600 font-mono">$ python {filename}</span>\n'
        f'                </div>\n'
        f'                <div class="font-mono text-xs text-emerald-400 leading-relaxed">{terminal_output}</div>\n'
        f'              </div>\n'
        f'            </div>\n'
        f'            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">\n'
        f'              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>\n'
        f'              <p class="text-sm text-gray-600">{tip_html}</p>\n'
        f'            </div>\n'
        f'          </div>\n'
        f'        </div>\n'
        f'      </div>\n'
    )


panel1 = make_panel(
    num_str="01",
    title="MongoDB CRUD",
    difficulty="Beginner",
    diff_icon="fa6-solid:leaf",
    icon="fa6-solid:file-code",
    filename="mongodb_crud.py",
    code_html=P1_CODE,
    terminal_cmd="python mongodb_crud.py",
    terminal_output=(
        "Inserted 2 products<br>"
        "Found: Pro Laptop 15 @ $1299.99<br>"
        "Update and delete applied"
    ),
    what_it_does="Perform all four CRUD operations on a MongoDB collection using pymongo — with realistic e-commerce product data.",
    tip_html=(
        "The <code class=\"font-mono\">$set</code> operator in "
        "<code class=\"font-mono\">update_one()</code> is not optional. "
        "Writing <code class=\"font-mono\">update_one({\"sku\": \"X\"}, {\"price\": 999})</code> "
        "without <code class=\"font-mono\">$set</code> replaces the "
        "<em>entire</em> document with only <code class=\"font-mono\">{\"price\": 999}</code>, "
        "silently deleting every other field."
    ),
    hidden=False,
)

panel2 = make_panel(
    num_str="02",
    title="MongoDB Query Operators",
    difficulty="Beginner",
    diff_icon="fa6-solid:leaf",
    icon="fa6-solid:magnifying-glass",
    filename="mongo_queries.py",
    code_html=P2_CODE,
    terminal_cmd="python mongo_queries.py",
    terminal_output=(
        "Premium products: 3<br>"
        "Affordable options: 12<br>"
        "First result: {'name': 'Wireless Mouse', 'price': 29.99}"
    ),
    what_it_does="Filter documents using MongoDB query operators — exact match, range ($lt/$gt), list membership ($in), and field projection.",
    tip_html=(
        "<code class=\"font-mono\">find()</code> returns a <strong>cursor</strong>, not a list. "
        "Wrapping it in <code class=\"font-mono\">list()</code> loads all results into memory at once. "
        "For large collections, iterate with "
        "<code class=\"font-mono\">for doc in col.find(...)</code> instead "
        "so Python processes one document at a time without exhausting RAM."
    ),
    hidden=True,
)

panel3 = make_panel(
    num_str="03",
    title="Decision Framework",
    difficulty="Beginner",
    diff_icon="fa6-solid:leaf",
    icon="fa6-solid:code-branch",
    filename="db_chooser.py",
    code_html=P3_CODE,
    terminal_cmd="python db_chooser.py",
    terminal_output=(
        "SQL (PostgreSQL / MySQL)<br>"
        "Document DB (MongoDB)<br>"
        "Key-Value (Redis)"
    ),
    what_it_does="Apply a requirements checklist to three real-world scenarios — banking, product catalog, session management — and pick the right database type for each.",
    tip_html=(
        "When requirements overlap two categories — for example, a catalog that also needs "
        "ACID checkout — start with SQL. "
        "SQL handles hybrid workloads better than running two separate databases, "
        "and you can migrate a specific collection to MongoDB later "
        "if schema flexibility genuinely becomes a bottleneck."
    ),
    hidden=True,
)

panel4 = make_panel(
    num_str="04",
    title="Redis Key-Value Cache",
    difficulty="Intermediate",
    diff_icon="fa6-solid:fire",
    icon="fa6-solid:key",
    filename="redis_cache.py",
    code_html=P4_CODE,
    terminal_cmd="python redis_cache.py",
    terminal_output=(
        "  Cache MISS &mdash; user:42 stored for 300 s<br>"
        "{'id': 42, 'name': 'User42', 'role': 'analyst'}<br>"
        "  Cache HIT  &mdash; user:42<br>"
        "{'id': 42, 'name': 'User42', 'role': 'analyst'}<br>"
        "TTL remaining: 298 seconds"
    ),
    what_it_does="Use Redis as a sub-millisecond cache layer — serve repeat lookups from memory and automatically expire stale data after a configurable TTL.",
    tip_html=(
        "<code class=\"font-mono\">setex(key, seconds, value)</code> sets the value and the "
        "expiry in a single atomic operation. "
        "Never call <code class=\"font-mono\">r.set(key, value)</code> followed by "
        "<code class=\"font-mono\">r.expire(key, seconds)</code> as two separate commands — "
        "if your process crashes between them, the key lives forever and stale data is served indefinitely."
    ),
    hidden=True,
)

panel5 = make_panel(
    num_str="05",
    title="MongoDB Aggregation Pipeline",
    difficulty="Intermediate",
    diff_icon="fa6-solid:fire",
    icon="fa6-solid:layer-group",
    filename="mongo_agg.py",
    code_html=P5_CODE,
    terminal_cmd="python mongo_agg.py",
    terminal_output=(
        "North East    revenue=$482,310.00  orders=1203<br>"
        "West Coast    revenue=$371,845.50  orders=988<br>"
        "Midwest       revenue=$298,410.00  orders=754<br>"
        "South         revenue=$241,620.75  orders=623<br>"
        "Mountain      revenue=$189,300.00  orders=412"
    ),
    what_it_does="Use the MongoDB aggregation pipeline to compute GROUP BY-style analytics — filter completed orders, sum revenue by region, sort descending, and return the top 5.",
    tip_html=(
        "Always place <code class=\"font-mono\">$match</code> as the <strong>first</strong> stage. "
        "MongoDB can use an index to satisfy a leading <code class=\"font-mono\">$match</code>, "
        "but if <code class=\"font-mono\">$group</code> runs first it must read every document "
        "in the collection before any filter is applied. "
        "Putting <code class=\"font-mono\">$match</code> last on a 10-million-document collection "
        "can turn a 0.3-second query into a 45-second one."
    ),
    hidden=True,
)

NEW_BODY = NEW_TABS + panel1 + panel2 + panel3 + panel4 + panel5

# ── Locate section body and replace ──────────────────────────────────────

html = TARGET.read_text(encoding="utf-8")

# Identify the section body open tag inside #code-examples
MARKER_START = '    <div class="bg-white px-8 py-7 space-y-6">'
MARKER_END   = '\n    </div>\n  </div>\n</section>'   # closes body + outer card + section

# Find the code-examples section specifically
ce_idx = html.find('<section id="code-examples">')
if ce_idx == -1:
    sys.exit("ERROR: could not find #code-examples section")

# Find the start of the section body AFTER the section header
body_start = html.find(MARKER_START, ce_idx)
if body_start == -1:
    sys.exit("ERROR: could not find section body open div in #code-examples")

# Find the end: </div></div></section> that terminates this section
# (two closing divs then </section> — the next section starts immediately after)
body_end = html.find('\n    </div>\n  </div>\n</section>', body_start)
if body_end == -1:
    # Fallback: look for </section> after body_start
    body_end = html.find('</section>', body_start)
    if body_end == -1:
        sys.exit("ERROR: could not find end of #code-examples section")
    close_block = '\n</section>'
    new_content = MARKER_START + "\n" + NEW_BODY + "\n    </div>\n  </div>\n"
else:
    close_block = '\n    </div>\n  </div>\n</section>'

# Build replacement
old_block = html[body_start : body_end + len(close_block)]
new_block  = MARKER_START + "\n" + NEW_BODY + "    </div>\n  </div>\n</section>"

if old_block not in html:
    # This shouldn't happen given we located it above; sanity check
    sys.exit("ERROR: old_block not found in html (sanity check failed)")

new_html = html.replace(old_block, new_block, 1)

if new_html == html:
    print("⚠️  No change made — old block was not found")
    sys.exit(1)

TARGET.write_text(new_html, encoding="utf-8")
print(f"✅ Patched: {TARGET.name}")

# Quick structural check
lines = new_html.split("\n")
ce_s = next(i for i,l in enumerate(lines) if '<section id="code-examples"' in l)
nxt  = next(i for i,l in enumerate(lines[ce_s+1:], ce_s+1) if '<section id=' in l)
block = "\n".join(lines[ce_s:nxt])
opens  = block.count("<div")
closes = block.count("</div>")
tabs   = sum(1 for l in lines[ce_s:nxt] if "ce-step" in l and "onclick" in l)
panels = sum(1 for l in lines[ce_s:nxt] if 'class="ce-panel' in l)
print(f"   div opens={opens}, closes={closes}, diff={opens-closes}")
print(f"   ce-step buttons={tabs}, ce-panels={panels}")
