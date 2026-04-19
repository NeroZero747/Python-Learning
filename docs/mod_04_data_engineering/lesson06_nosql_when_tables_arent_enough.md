# Lesson 06 — NoSQL: When Tables Aren't Enough

**Track:** Data Engineering for Analysts  
**Module:** Module 2 — Modern Data Tools  
**Difficulty:** Beginner | **Duration:** 12 min  
**Sources:** M2-L01 (What Is NoSQL?) · M2-L02 (Types of NoSQL Databases) · M2-L03 (Document DBs / MongoDB) · M2-L04 (Key-Value / Redis — trimmed) · M2-L07 (SQL vs NoSQL Decision)  
**Dropped:** M2-L05 (Cassandra), M2-L06 (Neo4j) — too specialized for this audience

---

## Learning Objectives

1. **Define NoSQL** — Explain why NoSQL databases exist and what problems they solve that SQL can't.
2. **4 NoSQL categories** — Describe document, key-value, column-family, and graph databases with one use case each.
3. **Hands-on with MongoDB** — Perform basic CRUD operations on a document database using Python.
4. **Decision framework** — Apply the SQL vs NoSQL decision criteria to a given data scenario.

> By the end of this lesson you'll be able to recognize when a project calls for NoSQL and hold an informed conversation about which type to recommend.

---

## Overview

### Hook
SQL databases are exceptional for structured, consistent data with defined relationships. But not all data is structured, consistent, or relational. When you're storing user activity events, product catalogs with irregular attributes, or sensor readings by the billions — SQL tables become an uncomfortable fit. That's when a data engineer reaches for NoSQL.

### Analogy: The Office Filing System
Think of the difference between SQL and NoSQL like two kinds of office filing. An **SQL database** is like a rigidly organized file cabinet — every drawer has labeled sections, every document must fit the section's template, and pulling related records involves checking multiple drawers for matching reference numbers. A **NoSQL database** is like a flexible document storage room — documents can have different structures, you can stuff everything about one customer into one envelope, and new fields can be added without redesigning the entire cabinet.

| Database Type | Filing Analogy |
|--------------|---------------|
| **Document DB** | One envelope per record — holds everything about it, any shape |
| **Key-Value DB** | A wall of numbered lockers — instant access if you know the locker number |
| **Column-Family DB** | A notebook with infinitely expanding rows — each row can have different columns |
| **Graph DB** | A pinboard with thread connecting related items |

> **Key takeaway:** NoSQL doesn't mean "no structure" — it means "not only SQL." Most production systems use SQL and NoSQL together, letting each handle what it's best at.

---

## Key Takeaways

### 1. NoSQL Trades Rigid Schema for Flexibility
A SQL table requires every row to have the same columns. A document database lets each document have different fields. This is essential when your data shape is evolving rapidly (like an e-commerce product catalog where some products have 3 attributes and others have 30).  
**Keywords:** Schema-less · Flexible · Evolving data

### 2. Horizontal Scaling Is Why NoSQL Exists at Scale
SQL databases scale **vertically** (bigger server). Many NoSQL databases scale **horizontally** (more servers). When you need to store billions of records, adding more machines is cheaper and more reliable than buying a single enormous one. This is the architectural choice behind databases like Cassandra and DynamoDB.  
**Keywords:** Horizontal scaling · Sharding · Distributed

### 3. Choose Based on Your Data's Shape and Access Pattern
The best database is the one where your most common query reads data the way it's stored. If you retrieve complete customer records by ID, a document DB is natural. If you need millisecond cache lookups by key, use a key-value store. If you have rich relationship queries, use a graph DB. If everything is structured and relational, SQL is still the right choice.  
**Keywords:** Access pattern · Query shape · Data modeling

---

## Key Concepts

### The 4 NoSQL Categories

| Category | What it stores | Best for | Example tools |
|----------|---------------|---------|---------------|
| **Document** | JSON/BSON documents, variable structure | User profiles, product catalogs, content | MongoDB, Firestore, CouchDB |
| **Key-Value** | Simple value (string, list, hash) indexed by key | Caching, sessions, real-time leaderboards | Redis, DynamoDB, Memcached |
| **Column-Family** | Rows with variable columns per row | Time-series, write-heavy IoT, event logging | Cassandra, HBase, ScyllaDB |
| **Graph** | Nodes and edges with properties | Social networks, fraud detection, recommendations | Neo4j, Amazon Neptune |

### When SQL Is Still the Right Choice
- Your data is naturally tabular with consistent attributes
- You need complex JOIN queries across multiple entities
- ACID transactions are required (banking, inventory)
- Your team has strong SQL expertise and the data volume isn't extreme

### When NoSQL Makes Sense
- Data structure is irregular or changes frequently
- You need to store and retrieve complete entity records (not join them)
- Write throughput needs to be extremely high (IoT, events)
- You need horizontal scaling across many nodes
- Data has rich relationship traversal requirements (graphs)

---

## Code Examples

### Example 1: MongoDB CRUD with pymongo
```python
from pymongo import MongoClient

# Connect to MongoDB (local instance)
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]             # select (or create) database
products = db["products"]            # select (or create) collection

# INSERT — documents can have different shapes
products.insert_many([
    {
        "sku": "LAPTOP-001",
        "name": "Pro Laptop 15",
        "price": 1299.99,
        "specs": {"ram_gb": 16, "storage_tb": 1, "os": "Windows 11"}
    },
    {
        "sku": "BOOK-042",
        "name": "Python for Engineers",
        "price": 39.99,
        "author": "Jane Smith",         # ← different fields than laptop!
        "isbn": "978-0000000000"
    }
])

# READ — find by field
laptop = products.find_one({"sku": "LAPTOP-001"})
print(laptop["name"])                  # Pro Laptop 15

# READ — find all products under £100
cheap = list(products.find({"price": {"$lt": 100}}))
print(f"Found {len(cheap)} products under £100")

# UPDATE — add a new field to one document
products.update_one(
    {"sku": "LAPTOP-001"},
    {"$set": {"in_stock": True, "warehouse": "LHR-01"}}
)

# DELETE — remove discontinued products
products.delete_many({"discontinued": True})
```

### Example 2: Redis as a cache (key-value)
```python
import redis, json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def get_user_profile(user_id: str) -> dict:
    """Return user profile — from cache if available, otherwise from DB."""
    cache_key = f"user:{user_id}"

    # Try cache first (sub-millisecond lookup)
    cached = r.get(cache_key)
    if cached:
        print("Cache hit")
        return json.loads(cached)

    # Cache miss — query the database
    print("Cache miss — querying DB")
    profile = query_database(user_id)   # your SQL/NoSQL query

    # Store in cache with a 5-minute expiry
    r.setex(cache_key, 300, json.dumps(profile))
    return profile
```

### Example 3: The SQL vs NoSQL decision in practice
```python
"""
Scenario A: Online banking transactions
  - Fixed schema (amount, date, account_id, merchant)
  - ACID transactions required (can't partially record a transfer)
  - Complex JOIN queries (account balance = sum of transactions)
  → USE SQL (PostgreSQL, MySQL)

Scenario B: E-commerce product catalog
  - Irregular attributes (laptops have RAM specs, books have ISBN)
  - Schema evolves weekly as new product categories are added
  - Fetch complete product document by SKU (no JOIN needed)
  → USE Document DB (MongoDB)

Scenario C: User session management (who is logged in)
  - Simple key → value lookup (session_token → user_id)
  - Must expire automatically after 30 minutes
  - Needs millisecond response time for every web request
  → USE Key-Value DB (Redis)
"""
```

### Example 4: MongoDB aggregation pipeline
```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
orders = client["shop"]["orders"]

# MongoDB's aggregation pipeline is like SQL GROUP BY
pipeline = [
    {"$match": {"status": "completed"}},                       # WHERE
    {"$group": {
        "_id": "$region",                                       # GROUP BY region
        "total_revenue": {"$sum": "$amount"},                   # SUM(amount)
        "order_count":   {"$count": {}}                         # COUNT(*)
    }},
    {"$sort": {"total_revenue": -1}},                          # ORDER BY DESC
    {"$limit": 5}                                               # LIMIT 5
]

results = list(orders.aggregate(pipeline))
for r in results:
    print(f"{r['_id']}: £{r['total_revenue']:,.2f} ({r['order_count']} orders)")
```

---

## Common Mistakes

### Mistake 1: Using MongoDB when your data is actually relational
```
WRONG: Storing orders and customers as separate MongoDB collections,
then doing multiple queries to join them in Python.

BETTER: Embed the relevant customer fields inside each order document
(denormalization), OR use a relational database if you need many
different join patterns.

NoSQL works best when you read documents whole, not when you join them.
```

### Mistake 2: Indexing nothing in MongoDB
```python
# WRONG — queries on un-indexed fields do full collection scans
products.find({"sku": "LAPTOP-001"})  # scans 1M documents if no index

# RIGHT — create an index on fields you filter by frequently
products.create_index([("sku", 1)], unique=True)   # 1 = ascending
products.create_index([("price", 1)])
# Now the sku query is a fast O(log n) lookup
```

### Mistake 3: Storing everything in MongoDB "because it's flexible"
Using a document DB for data that is naturally tabular and consistent just adds complexity without benefit. If every product actually has the same 5 attributes, a relational table is simpler, faster to query, and easier to enforce constraints on.

---

## Practice Exercises

### Exercise 1 — Insert and query
```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
employees = client["company"]["employees"]

# TODO: Insert 3 employees with different fields:
# - Alice: role="engineer", skills=["python","sql"], salary=85000
# - Bob: role="manager", direct_reports=["Alice","Carol"], salary=95000
# - Carol: role="analyst", tools=["tableau","excel"], salary=72000

# TODO: Find all employees with salary > 80000
# TODO: Update Alice's salary to 90000
# TODO: Add a field "active": True to all documents
```

### Exercise 2 — Decision exercise
For each scenario, choose SQL or a NoSQL type (Document, Key-Value, Column-Family, Graph) and explain why:
1. Storing 500 million IoT sensor readings ingested at 10,000/second.
2. Managing a social network's friendship connections and recommendations.
3. A payroll system that processes employee salaries with strict accuracy requirements.
4. A content management system where each article has different metadata fields.

### Exercise 3 — MongoDB aggregation
```python
# Given an "orders" collection with fields: customer_id, product, amount, region
# TODO: Write an aggregation pipeline that:
# 1. Filters to orders in the "EMEA" region
# 2. Groups by product
# 3. Calculates total revenue and order count per product
# 4. Sorts by total revenue descending
# 5. Returns the top 3 products
```

---

## Lesson Recap

1. **NoSQL databases** exist to handle data that doesn't fit the relational model — irregular schemas, horizontal scale, or relationship-heavy traversal.
2. The **4 categories** are: Document (flexible JSON records), Key-Value (instant lookup by key), Column-Family (wide rows, write-heavy), and Graph (relationship traversal).
3. **MongoDB** is the most common document database — use it when your records have variable fields and are retrieved whole rather than joined.
4. The **decision rule**: SQL when data is uniform, relational, and ACID-required; NoSQL when data is irregular, high-volume, or needs a specific access pattern that SQL handles poorly.

---

## Knowledge Check

**Q1.** Name the 4 categories of NoSQL databases and give one real-world use case for each.  
**Answer:** Document (product catalog with variable attributes), Key-Value (user session cache), Column-Family (IoT sensor time-series), Graph (social network friend recommendations).

**Q2.** You're building a system that must look up a user's shopping cart with sub-millisecond latency, and each cart only needs to live for 30 minutes. Which NoSQL type fits best?  
**Answer:** Key-Value (Redis) — instant lookup by session key, with built-in TTL (time-to-live) expiry.

**Q3.** True or False: NoSQL databases can never perform joins.  
**Answer:** True in the strict sense — most NoSQL databases don't have native JOIN operations. Instead, you either denormalize (embed related data in the document) or perform the join in application code. This is a deliberate trade-off for flexibility and scale.

---

## Next Lesson
**Lesson 07 — API Data Integration with Python**  
Now that you know where to store different types of data, you'll learn how to collect it from one of the most common modern sources — REST APIs. You'll make HTTP requests, parse JSON, handle authentication, pagination, and rate limits.
