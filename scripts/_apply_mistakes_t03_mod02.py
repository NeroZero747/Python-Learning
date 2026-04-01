#!/usr/bin/env python3
"""
Rewrite <section id="mistakes"> for all 7 lessons in
track_03 / mod_02_nosql_and_modern_data_storage.
"""

import re, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
MOD = BASE / "pages" / "track_03_data_engineering" / "mod_02_nosql_and_modern_data_storage"

SECTION_RE = re.compile(
    r'(<section id="mistakes">).*?(</section>)',
    re.DOTALL,
)

# ── Content definitions ────────────────────────────────────────────────

LESSONS = {
    # ── Lesson 01: What Is NoSQL ──
    "lesson01_what_is_nosql.html": {
        "topic": "NoSQL concepts",
        "mistakes": [
            {
                "tab": "NoSQL Means No SQL",
                "title": "Assuming NoSQL Means You Can Never Use SQL",
                "subtitle": "Many NoSQL databases support SQL-like query languages.",
                "explanation": 'NoSQL stands for "Not Only SQL", not "No SQL at all". Databases like Cassandra offer CQL (Cassandra Query Language), and MongoDB supports rich query operators. Dismissing SQL skills because you use NoSQL limits your ability to learn these tools.',
                "wrong_label": "assumes no queries",
                "wrong_code": '# "NoSQL means I don\'t need queries"\nfor doc in collection:\n    if doc["status"] == "active":\n        results.append(doc)     # manual loop',
                "correct_label": "use the query language",
                "correct_code": '# MongoDB query — still structured\nresults = collection.find(\n    {"status": "active"}       # built-in filter\n)',
                "tip": "NoSQL databases have their own query languages. Learn them instead of writing manual loops — they are faster and easier to read.",
            },
            {
                "tab": "NoSQL Replaces SQL",
                "title": "Thinking NoSQL Replaces Relational Databases Entirely",
                "subtitle": "NoSQL and SQL solve different problems — one does not replace the other.",
                "explanation": 'Relational databases excel at structured, transactional data with strict consistency. NoSQL handles flexible schemas, massive scale, or graph-shaped data. Most real-world systems use both — choosing one for every use case leads to awkward workarounds.',
                "wrong_label": "force NoSQL everywhere",
                "wrong_code": '# Storing financial transactions in a document DB\ndb.transactions.insert_one({\n    "account": "A001",\n    "amount": -500,          # no ACID guarantees\n    "to_account": "B002"\n})',
                "correct_label": "match the database to the problem",
                "correct_code": '# Financial transactions → relational + ACID\ncursor.execute("""\n    UPDATE accounts SET balance = balance - 500\n    WHERE id = \'A001\'\n""")                                # transaction-safe',
                "tip": "Ask what your data looks like and what guarantees you need before picking a database. The answer is often a mix of both SQL and NoSQL.",
            },
            {
                "tab": "Ignoring Schema Design",
                "title": "Skipping Schema Design Because NoSQL Is Schema-Flexible",
                "subtitle": "Flexible schemas still need planning, or documents grow inconsistent over time.",
                "explanation": 'NoSQL lets you store documents without a fixed schema, but that does not mean you should skip planning. Without conventions, one document might have <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">customer_name</code> while another has <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">name</code> — making queries unreliable.',
                "wrong_label": "inconsistent documents",
                "wrong_code": 'db.users.insert_one({"customer_name": "Alice"})\ndb.users.insert_one({"name": "Bob"})  # different field',
                "correct_label": "consistent field names",
                "correct_code": '# Agree on a schema convention\ndb.users.insert_one({"name": "Alice", "email": "a@x.com"})\ndb.users.insert_one({"name": "Bob",   "email": "b@x.com"})',
                "tip": "Schema-flexible does not mean schema-free. Write down your field naming conventions before inserting data, even in a document database.",
            },
        ],
    },

    # ── Lesson 02: Types of NoSQL Databases ──
    "lesson02_types_of_nosql_databases.html": {
        "topic": "NoSQL database types",
        "mistakes": [
            {
                "tab": "One Type for Everything",
                "title": "Using One NoSQL Type for Every Problem",
                "subtitle": "Each NoSQL family is optimised for a specific access pattern.",
                "explanation": 'Document, key-value, column-family, and graph databases each solve different problems. Forcing a key-value store to handle complex relationships — or a document DB to act like a graph — leads to convoluted code and poor performance.',
                "wrong_label": "document DB for graph queries",
                "wrong_code": '# Storing relationships in a document DB\ndb.users.insert_one({\n    "name": "Alice",\n    "friends": ["Bob", "Charlie"]  # flat list\n})\n# Finding friends-of-friends requires multiple queries',
                "correct_label": "graph DB for relationships",
                "correct_code": '# Neo4j — relationships are first-class\nCREATE (a:Person {name: "Alice"})\nCREATE (b:Person {name: "Bob"})\nCREATE (a)-[:FRIENDS_WITH]->(b)\n# friends-of-friends in one query',
                "tip": "Match the database to the shape of your data: documents for nested records, key-value for fast lookups, column-family for time-series, and graphs for relationships.",
            },
            {
                "tab": "Mixing Up Families",
                "title": "Confusing Column-Family With Columnar Storage",
                "subtitle": "Cassandra's column families are not the same as Parquet's columnar format.",
                "explanation": 'Column-family databases like Cassandra store rows grouped by a partition key, with flexible columns per row. Columnar file formats like Parquet store all values of one column together for compression. The names sound alike, but the architectures are completely different.',
                "wrong_label": "treats Cassandra like Parquet",
                "wrong_code": '# Expecting Cassandra to compress by column like Parquet\n# and reading single columns efficiently\nresult = session.execute(\n    "SELECT price FROM orders"  # full table scan',
                "correct_label": "query by partition key",
                "correct_code": '# Cassandra is fast when you query by partition key\nresult = session.execute(\n    "SELECT price FROM orders WHERE region = \'EU\'")',
                "tip": "Column-family means flexible columns per row. Columnar storage means data stored by column for compression. Learn the distinction early and it will save confusion later.",
            },
            {
                "tab": "Ignoring Access Patterns",
                "title": "Choosing a Database Without Knowing Your Query Patterns",
                "subtitle": "NoSQL databases are designed around specific read/write patterns — picking blindly wastes their strengths.",
                "explanation": 'In NoSQL you model data around how you read it, not how it is structured logically. If your application needs fast lookups by key, a key-value store is ideal. If it needs full-text search across nested documents, a document database fits better. Choosing without understanding your queries leads to slow, awkward workarounds.',
                "wrong_label": "choose first, query later",
                "wrong_code": '# Picked Redis (key-value) but need complex filters\nimport redis\nr = redis.Redis()\nr.set("user:1", "{name: Alice, age: 30}")\n# No way to query "all users over 25"',
                "correct_label": "query patterns drive the choice",
                "correct_code": '# Need complex queries → document DB\nresult = db.users.find(\n    {"age": {"$gt": 25}}       # flexible filtering\n)',
                "tip": "List your top five queries before choosing a database. The queries should drive the technology choice, not the other way around.",
            },
        ],
    },

    # ── Lesson 03: Document Databases — MongoDB ──
    "lesson03_document_databases_mongodb.html": {
        "topic": "MongoDB document databases",
        "mistakes": [
            {
                "tab": "Deeply Nested Docs",
                "title": "Nesting Documents Too Many Levels Deep",
                "subtitle": "Deeply nested documents become hard to query, update, and index.",
                "explanation": 'MongoDB supports rich nesting, but going four or five levels deep makes updates brittle and queries verbose. If you need to reach <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">order.items[0].product.reviews[2].author.name</code>, your schema needs flattening.',
                "wrong_label": "excessive nesting",
                "wrong_code": 'db.orders.insert_one({\n    "customer": {\n        "address": {\n            "city": {\n                "district": "Central"  # 4 levels deep\n            }\n        }\n    }\n})',
                "correct_label": "flatter structure",
                "correct_code": 'db.orders.insert_one({\n    "customer_name": "Alice",\n    "city": "London",\n    "district": "Central"             # flat, easy to query\n})',
                "tip": "A good rule of thumb is two levels of nesting maximum. If you go deeper, consider splitting into separate collections and linking by ID.",
            },
            {
                "tab": "No Index on Queries",
                "title": "Querying Fields That Have No Index",
                "subtitle": "MongoDB scans every document in the collection when there is no index on the query field.",
                "explanation": 'Without an index, a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">find()</code> call triggers a collection scan — reading every document to check the filter. On millions of records this is extremely slow. Create an index on fields you filter or sort by.',
                "wrong_label": "no index",
                "wrong_code": '# 5 million documents, no index on "status"\nresults = db.orders.find({"status": "shipped"})\n# full collection scan — very slow',
                "correct_label": "create an index first",
                "correct_code": 'db.orders.create_index("status")       # one-time setup\nresults = db.orders.find({"status": "shipped"})\n# index scan — fast lookup',
                "tip": "Run <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">explain()</code> on slow queries to see if MongoDB is doing a collection scan. If it is, add an index on the filter field.",
            },
            {
                "tab": "insert_one in a Loop",
                "title": "Inserting Documents One at a Time in a Loop",
                "subtitle": "Calling insert_one thousands of times creates massive network overhead.",
                "explanation": 'Each <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">insert_one()</code> is a separate network round-trip. For bulk loads, use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">insert_many()</code> to send all documents in a single batch, which is dramatically faster.',
                "wrong_label": "one insert per loop",
                "wrong_code": 'for row in data:\n    db.orders.insert_one(row)  # 10,000 round-trips',
                "correct_label": "bulk insert",
                "correct_code": 'db.orders.insert_many(data)  # one round-trip for all 10,000',
                "tip": "Batch operations are almost always faster than loops. If you see a database call inside a <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">for</code> loop, look for a bulk alternative.",
            },
        ],
    },

    # ── Lesson 04: Key-Value Databases — Redis ──
    "lesson04_key_value_databases_redis.html": {
        "topic": "Redis key-value databases",
        "mistakes": [
            {
                "tab": "Storing Large Objects",
                "title": "Storing Large JSON Blobs as a Single Redis Value",
                "subtitle": "Redis is optimised for small, fast lookups — not multi-megabyte documents.",
                "explanation": 'Storing a 5 MB JSON blob in one key defeats the purpose of an in-memory cache. Reads slow down, memory fills up fast, and you cannot update a single field without rewriting the entire blob. Break large objects into smaller keys or use a hash.',
                "wrong_label": "giant JSON value",
                "wrong_code": 'import json, redis\nr = redis.Redis()\nblob = json.dumps(huge_dict)   # 5 MB string\nr.set("user:1", blob)           # one giant key',
                "correct_label": "use a Redis hash",
                "correct_code": 'r.hset("user:1", mapping={\n    "name": "Alice",\n    "email": "a@x.com",\n    "plan": "pro"\n})  # separate fields, updatable individually',
                "tip": "Redis hashes let you read and update individual fields without touching the rest of the record. Use them whenever a value has structure.",
            },
            {
                "tab": "No Expiry on Cache",
                "title": "Setting Cache Keys Without an Expiry Time",
                "subtitle": "Keys without TTL stay in memory forever, eventually exhausting available RAM.",
                "explanation": 'Redis holds everything in memory. If you keep adding keys without expiry, memory usage grows until Redis evicts data or the server runs out of RAM. Always set a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">TTL</code> (time-to-live) on cache keys.',
                "wrong_label": "no expiry",
                "wrong_code": 'r.set("session:abc123", user_data)\n# key lives forever — memory leak',
                "correct_label": "set a TTL",
                "correct_code": 'r.set("session:abc123", user_data, ex=3600)\n# expires after 1 hour — memory stays under control',
                "tip": "A good default TTL is one hour for caches and 24 hours for sessions. Adjust based on how often your data changes.",
            },
            {
                "tab": "Using Redis as Primary DB",
                "title": "Using Redis as the Only Database With No Persistence Backup",
                "subtitle": "In-memory data is lost on restart unless persistence is configured.",
                "explanation": 'Redis is designed as a cache or fast data layer, not a primary database. By default, data lives only in RAM. A server restart or crash wipes everything unless you enable RDB snapshots or AOF logging — and even then, Redis is not a substitute for a durable database.',
                "wrong_label": "Redis as sole data store",
                "wrong_code": '# All order data lives only in Redis\nfor order in orders:\n    r.set(f"order:{order[\'id\']}", json.dumps(order))\n# server restart → all orders gone',
                "correct_label": "Redis as cache, database for durability",
                "correct_code": '# Primary store in a database\ndf.to_sql("orders", engine, if_exists="append")\n# Redis caches hot data for speed\nfor order_id in hot_ids:\n    r.set(f"order:{order_id}", data, ex=3600)',
                "tip": "Use Redis to speed up reads, not to store the only copy of your data. A relational database or document store should hold the durable copy.",
            },
        ],
    },

    # ── Lesson 05: Column-Family Databases — Cassandra ──
    "lesson05_column_family_databases_cassandra.html": {
        "topic": "Cassandra column-family databases",
        "mistakes": [
            {
                "tab": "Querying Without Partition Key",
                "title": "Running Queries Without the Partition Key",
                "subtitle": "Cassandra scans every node in the cluster when the partition key is missing.",
                "explanation": 'Cassandra distributes data across nodes by partition key. A query without it (or with <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">ALLOW FILTERING</code>) triggers a full cluster scan, which defeats the purpose of a distributed database.',
                "wrong_label": "missing partition key",
                "wrong_code": 'SELECT * FROM orders\n    WHERE status = \'shipped\'\n    ALLOW FILTERING;          -- scans all nodes',
                "correct_label": "include partition key",
                "correct_code": 'SELECT * FROM orders\n    WHERE region = \'EU\'       -- partition key\n    AND status = \'shipped\';   -- fast lookup',
                "tip": "Design your table so that every common query includes the partition key. If a query cannot use the partition key, you may need a separate table for that access pattern.",
            },
            {
                "tab": "Normalising Data",
                "title": "Normalising Data Like a Relational Database",
                "subtitle": "Cassandra has no joins — normalised tables force multiple queries and client-side joins.",
                "explanation": 'In relational databases, you split data into small tables and join them. Cassandra does not support joins, so normalised data means multiple round-trips and manual merging in your application code. Instead, denormalise by duplicating data into query-specific tables.',
                "wrong_label": "normalised tables (no joins)",
                "wrong_code": '-- Two tables, expecting a join\nSELECT * FROM orders WHERE order_id = 1;\nSELECT * FROM customers WHERE id = 42;\n-- Must combine in Python — slow, fragile',
                "correct_label": "denormalised query table",
                "correct_code": '-- One table designed for the query\nSELECT * FROM orders_by_customer\n    WHERE customer_name = \'Alice\';  -- all data in one read',
                "tip": "In Cassandra, you model one table per query pattern. Duplication is expected — storage is cheaper than slow multi-query joins.",
            },
            {
                "tab": "Lightweight Transactions Overuse",
                "title": "Using Lightweight Transactions for Every Write",
                "subtitle": "LWT adds a multi-round-trip consensus protocol, slowing writes dramatically.",
                "explanation": 'Lightweight transactions (<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">IF NOT EXISTS</code>) use Paxos consensus, which is much slower than normal writes. Use them only when you actually need conditional uniqueness — not as a default safety measure.',
                "wrong_label": "LWT on every insert",
                "wrong_code": 'INSERT INTO events (id, ts, data)\n    VALUES (uuid(), now(), \'click\')\n    IF NOT EXISTS;    -- Paxos overhead on every write',
                "correct_label": "normal insert (no LWT)",
                "correct_code": 'INSERT INTO events (id, ts, data)\n    VALUES (uuid(), now(), \'click\');  -- fast write',
                "tip": "Reserve <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">IF NOT EXISTS</code> for cases where duplicate keys cause real problems, like user registration. For append-only event logs, a normal insert is perfectly safe.",
            },
        ],
    },

    # ── Lesson 06: Graph Databases — Neo4j ──
    "lesson06_graph_databases_neo4j.html": {
        "topic": "Neo4j graph databases",
        "mistakes": [
            {
                "tab": "Unbounded Traversals",
                "title": "Running Graph Queries Without a Depth Limit",
                "subtitle": "An unbounded traversal can follow millions of edges and never return.",
                "explanation": 'Cypher allows variable-length paths like <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">[:KNOWS*]</code> with no upper bound. On a large social graph this explores millions of nodes. Always set a maximum depth to keep queries predictable.',
                "wrong_label": "no depth limit",
                "wrong_code": 'MATCH (a:Person {name: "Alice"})\n      -[:KNOWS*]->(b)       // unbounded\nRETURN b.name               // could scan millions',
                "correct_label": "bounded depth",
                "correct_code": 'MATCH (a:Person {name: "Alice"})\n      -[:KNOWS*1..3]->(b)   // max 3 hops\nRETURN b.name               // fast, predictable',
                "tip": "Start with a low depth limit like 2 or 3 and increase only if results are too narrow. Social graphs expand exponentially with each hop.",
            },
            {
                "tab": "Storing Tabular Data",
                "title": "Storing Flat Tabular Data in a Graph Database",
                "subtitle": "A graph adds overhead when data has no meaningful relationships.",
                "explanation": 'If your data is a flat table of transactions with no relationships between rows, a relational database or a document store is simpler and faster. Graphs shine when relationships are the primary query target — put tabular data where it belongs.',
                "wrong_label": "flat data in a graph",
                "wrong_code": '// Each row is an isolated node — no edges\nCREATE (t:Transaction {id: 1, amount: 50})\nCREATE (t:Transaction {id: 2, amount: 75})\n// No relationships → no graph value',
                "correct_label": "use a relational table",
                "correct_code": '-- Flat tabular data belongs in SQL\nINSERT INTO transactions (id, amount)\n    VALUES (1, 50), (2, 75);',
                "tip": "Use a graph when the questions you ask involve paths, connections, or influences between entities. For flat records, a SQL table is simpler and faster.",
            },
            {
                "tab": "No Indexes on Properties",
                "title": "Querying Node Properties Without Creating an Index",
                "subtitle": "Neo4j scans all nodes of a label when the queried property has no index.",
                "explanation": 'Finding <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">Person {name: "Alice"}</code> without an index on <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">name</code> causes a label scan — checking every <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">Person</code> node. Create indexes on properties you filter by.',
                "wrong_label": "no index on name",
                "wrong_code": '// No index — scans all Person nodes\nMATCH (p:Person {name: "Alice"})\nRETURN p',
                "correct_label": "create an index first",
                "correct_code": '// One-time index creation\nCREATE INDEX FOR (p:Person) ON (p.name);\n\nMATCH (p:Person {name: "Alice"})\nRETURN p                           // fast lookup',
                "tip": "Run <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">PROFILE</code> before your query to see whether Neo4j uses an index or a full scan. Add indexes for any property that appears in a WHERE clause.",
            },
        ],
    },

    # ── Lesson 07: SQL vs NoSQL — Choosing the Right Database ──
    "lesson07_sql_vs_nosql_choosing_the_right_database.html": {
        "topic": "choosing between SQL and NoSQL",
        "mistakes": [
            {
                "tab": "Choosing by Hype",
                "title": "Choosing a Database Because It Is Popular, Not Because It Fits",
                "subtitle": "A trending database that does not match your access pattern creates more work, not less.",
                "explanation": 'Picking MongoDB because everyone uses it — when your data is highly relational and transactional — forces you to simulate joins and transactions in application code. Choose based on your data shape and query needs, not popularity.',
                "wrong_label": "popular choice, wrong fit",
                "wrong_code": '# Financial ledger in MongoDB — no ACID transactions\ndb.ledger.insert_one({\n    "account": "A001", "debit": 500\n})\ndb.ledger.insert_one({\n    "account": "B002", "credit": 500\n})  # no atomicity guarantee',
                "correct_label": "fit-driven choice",
                "correct_code": '# Financial ledger in PostgreSQL — ACID transactions\nwith engine.begin() as conn:\n    conn.execute("UPDATE accounts SET bal = bal - 500 WHERE id = \'A001\'")\n    conn.execute("UPDATE accounts SET bal = bal + 500 WHERE id = \'B002\'")\n    # both succeed or both roll back',
                "tip": "List your requirements first: consistency, scale, query complexity, schema flexibility. Then pick the database — not the other way around.",
            },
            {
                "tab": "One Database for All",
                "title": "Insisting on a Single Database for the Entire Application",
                "subtitle": "Different parts of your system may have different data and query needs.",
                "explanation": 'A user profile might fit a document store, while financial transactions need a relational database, and product recommendations need a graph. Using one database for everything means some parts of your application are fighting the technology instead of using it.',
                "wrong_label": "single database for everything",
                "wrong_code": '# Everything in one relational DB\n# Users, sessions, recommendations, logs...\ncursor.execute("SELECT * FROM recommendations\n    JOIN users ON ... JOIN products ON ...")\n# complex joins for simple lookups',
                "correct_label": "polyglot persistence",
                "correct_code": '# Users in PostgreSQL (relational)\n# Sessions in Redis (fast cache)\n# Recommendations in Neo4j (graph)\n# each database plays to its strengths',
                "tip": "Polyglot persistence means using the right database for each job. It adds operational complexity, so start with one database and split only when a clear need arises.",
            },
            {
                "tab": "Ignoring Consistency Needs",
                "title": "Choosing an Eventually Consistent Database When You Need Strong Consistency",
                "subtitle": "Eventual consistency means reads can return stale data for a window of time.",
                "explanation": 'Many NoSQL databases default to eventual consistency for speed. If your application handles money, inventory, or booking — where two conflicting writes cause real damage — you need strong consistency or ACID transactions, not eventual convergence.',
                "wrong_label": "eventual consistency for payments",
                "wrong_code": '# DynamoDB eventual read — may see stale balance\nimport boto3\ntable = boto3.resource("dynamodb").Table("accounts")\nresp = table.get_item(Key={"id": "A001"})\nbalance = resp["Item"]["balance"]  # might be outdated',
                "correct_label": "strong consistency read",
                "correct_code": '# DynamoDB strong read — always latest\nresp = table.get_item(\n    Key={"id": "A001"},\n    ConsistentRead=True           # guaranteed latest\n)',
                "tip": "If stale data could cause a double-spend or overbooking, choose strong consistency — even if it is slightly slower. Correctness matters more than speed for financial data.",
            },
        ],
    },
}


# ── HTML builders ──────────────────────────────────────────────────────

def _tab_btn(index: int, label: str, *, active: bool) -> str:
    if active:
        cls = (
            'mk-step mk-step-active flex items-center gap-2 px-4 py-2 '
            'rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] '
            'text-white shadow-lg shadow-pink-200/50 transition-all duration-250'
        )
    else:
        cls = (
            'mk-step flex items-center gap-2 px-4 py-2 '
            'rounded-full bg-gray-800 text-gray-400 transition-all duration-250'
        )
    return (
        f'<button onclick="switchMkTab({index})" '
        f'class="{cls}" role="tab">\n'
        f'  <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>\n'
        f'  <span class="mk-step-label text-xs font-bold">{label}</span>\n'
        f'</button>'
    )


def _panel(mk: dict, *, hidden: bool) -> str:
    hide = " hidden" if hidden else ""
    return f'''\
<div class="mk-panel mk-panel-anim{hide}" role="tabpanel">
  <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

    <!-- Card header -->
    <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
        <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
      </span>
      <div class="min-w-0 flex-1">
        <h4 class="font-bold text-gray-800 text-sm">{mk["title"]}</h4>
        <p class="text-xs text-gray-500 mt-0.5">{mk["subtitle"]}</p>
      </div>
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
        <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
      </span>
    </div>

    <!-- Explanation paragraph -->
    <div class="px-6 py-5">
      <p class="text-sm text-gray-600 leading-relaxed">{mk["explanation"]}</p>
    </div>

    <!-- Wrong / Correct split panel -->
    <div class="relative grid grid-cols-1 sm:grid-cols-2">
      <div class="p-5 bg-red-50/30">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong \u2014 {mk["wrong_label"]}
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">{mk["wrong_code"]}</code></pre>
        </div>
      </div>
      <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
        <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
          <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
        </span>
      </div>
      <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct \u2014 {mk["correct_label"]}
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">{mk["correct_code"]}</code></pre>
        </div>
      </div>
    </div>

    <!-- Amber tip footer -->
    <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
      <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
      <p class="text-xs text-gray-600 leading-relaxed">{mk["tip"]}</p>
    </div>

  </div>
</div>'''


def build_section(topic: str, mistakes: list[dict]) -> str:
    tabs = "\n".join(
        _tab_btn(i, m["tab"], active=(i == 0))
        for i, m in enumerate(mistakes)
    )
    tab_row = f'<div class="flex items-center gap-2 mb-6" role="tablist">\n{tabs}\n</div>'

    panels = "\n\n".join(
        _panel(m, hidden=(i > 0))
        for i, m in enumerate(mistakes)
    )

    body = f'{tab_row}\n\n{panels}'

    return f'''\
<section id="mistakes">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:triangle-exclamation"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Common Mistakes</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Pitfalls beginners hit when working with {topic}</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">

{body}

    </div>
  </div>
</section>'''


# ── Main ───────────────────────────────────────────────────────────────

ok = fail = 0
for filename, lesson in LESSONS.items():
    path = MOD / filename
    if not path.exists():
        print(f"\u274c NOT FOUND  {filename}")
        fail += 1
        continue

    text = path.read_text(encoding="utf-8")
    replacement = build_section(lesson["topic"], lesson["mistakes"])
    new_text, n = SECTION_RE.subn(replacement, text, count=1)

    if n == 0:
        print(f"\u274c NO MATCH   {filename}")
        fail += 1
        continue

    path.write_text(new_text, encoding="utf-8")
    print(f"\u2705 OK         {filename}")
    ok += 1

print(f"\n{ok}/{ok + fail} mistakes sections rewritten")
