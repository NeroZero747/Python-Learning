# Module 14 — NoSQL & Modern Data Storage

# Lesson 4 — Key-Value Databases (Redis)

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **key-value databases** are  
• how **Redis stores and retrieves data**  
• why key-value databases are **extremely fast**  
• how Redis is used for **caching and real-time applications**

Key-value databases are one of the **simplest and fastest database models** used in modern systems.

---

# Overview

A **key-value database** stores data as pairs:

```text
Key → Value
```

Example:

```text
user_101 → {name: "Alice", city: "Los Angeles"}
session_902 → {user_id: 101, login_time: "10:15"}
product_555 → {name: "Laptop", price: 1200}
```

The database retrieves data by **looking up the key directly**.

Example request:

```text
GET user_101
```

Result:

```json
{name: "Alice", city: "Los Angeles"}
```

Because the database does not need to search through tables or perform joins, key-value stores can return results **extremely quickly**.

One of the most popular key-value databases is **Redis**.

---

# Key Idea Cards (3 Cards)

### Key-Value Databases Use Simple Structure

Data is stored as:

```text
Key → Value
```

Example:

```text
user_101 → Alice
```

The key uniquely identifies the stored value.

---

### Lookups Are Extremely Fast

Because the database retrieves data using the key directly, the lookup process is very efficient.

Example:

```text
GET session_9281
```

The database instantly returns the stored value.

---

### Key-Value Databases Are Often Used as Caches

A **cache** temporarily stores frequently accessed data.

Example:

```text
User session data
Product search results
Website content
```

Caching improves application performance.

---

# Key Concepts

## Redis Overview

Redis is an **in-memory key-value database**.

This means data is stored in **RAM instead of disk**.

Benefits:

```text
Extremely fast read/write speed
Low latency
High throughput
```

Typical Redis performance:

```text
Millions of operations per second
```

Because RAM access is much faster than disk storage.

Popular uses of Redis:

```text
Caching
Session management
Real-time analytics
Message queues
Leaderboards
```

## Key Structure

Each value is associated with a unique key.

Example structure:

```text
Key: user_1001
Value: {name: "Alice", city: "LA"}
```

Another example:

```text
Key: cart_8129
Value: ["Laptop", "Mouse"]
```

Keys must be unique.

## Basic Redis Commands

### Store Data

```text
SET user_101 "Alice"
```

### Retrieve Data

```text
GET user_101
```

Result:

```text
"Alice"
```

### Delete Data

```text
DEL user_101
```

### Check if Key Exists

```text
EXISTS user_101
```

Returns:

```text
1 → exists
0 → does not exist
```

## Storing Complex Data

Redis can store more than simple text.

Supported structures include:

```text
Strings
Lists
Sets
Hashes
Sorted sets
```

Example using a **hash structure**:

```text
HSET user:101 name "Alice" city "LA"
```

Retrieve the data:

```text
HGETALL user:101
```

Result:

```text
name: Alice
city: LA
```

---

# Redis vs SQL Example

SQL example:

```sql
SELECT name
FROM users
WHERE user_id = 101;
```

Redis equivalent:

```text
GET user_101
```

SQL performs a **table search**, while Redis directly retrieves the value by key.

This makes Redis much faster for certain operations.

---

# Redis Data Types

Redis supports several data structures.

| Type | Example | Use Case |
|---|---|---|
| String | "Alice" | caching values |
| List | [A,B,C] | queues |
| Set | {A,B,C} | unique items |
| Hash | {name:Alice, city:LA} | objects |
| Sorted Set | ranked data | leaderboards |

Example sorted set:

```text
ZADD leaderboard 1000 "Alice"
ZADD leaderboard 900 "Bob"
```

This creates a ranking system.

---

# Decision Flow

When deciding to use Redis:

```text
Need extremely fast lookups?
        ↓
Use key-value database
```

```text
Need caching layer for application?
        ↓
Use Redis
```

```text
Need real-time data structures?
        ↓
Redis works well
```

Redis is often used **alongside SQL databases**.

Example architecture:

```text
Application
     ↓
Redis Cache
     ↓
SQL Database
```

Redis stores frequently accessed data to reduce database load.

---

# Code Examples

### Example 1 — Store User Session

```text
SET session_1001 "logged_in"
```

### Example 2 — Store Shopping Cart

```text
SET cart_2001 "[Laptop, Mouse]"
```

### Example 3 — Store User Profile

```text
HSET user:101 name "Alice" city "LA"
```

### Example 4 — Leaderboard Ranking

```text
ZADD leaderboard 1000 "Alice"
ZADD leaderboard 900 "Bob"
```

Retrieve ranking:

```text
ZRANGE leaderboard 0 -1
```

---

# SQL vs Redis Comparison

| Feature | SQL Database | Redis |
|---|---|---|
| structure | tables | key-value |
| storage | disk | memory |
| speed | fast | extremely fast |
| joins | supported | not supported |
| schema | fixed | flexible |

Redis is typically used for **speed**, not complex relational queries.

---

# Practice Exercises

### Exercise 1

Tags: Databases, NoSQL, Redis

Explain why Redis is faster than traditional disk-based databases.

### Exercise 2

Tags: WHERE, Databases, Caching, NoSQL

Describe a scenario where Redis would be useful for **caching data**.

### Exercise 3

Tags: Databases, NoSQL, Redis

Explain how Redis could store **shopping cart data** for an e-commerce site.

### Exercise 4

Tags: Databases, NoSQL, Redis

Explain how Redis sorted sets could be used to build a **leaderboard system**.

---

# Common Mistakes

### Using Redis as a Primary Database

Redis is often best used as a **cache layer**, not the main data storage system.

### Storing Too Much Data in Memory

Because Redis stores data in RAM, large datasets can consume significant memory.

### Ignoring Data Persistence

Some Redis configurations prioritize speed over durability.

If the server restarts, data may be lost unless persistence is configured.

---

# Real-World Use

Redis is used by many large platforms.

Examples include:

```text
Twitter
GitHub
Pinterest
Stack Overflow
Instagram
```

Common use cases:

```text
Website caching
User session storage
Real-time messaging
Gaming leaderboards
Rate limiting APIs
```

Example architecture:

```text
Web App
   ↓
Redis Cache
   ↓
SQL Database
```

Redis stores frequently accessed data so applications can respond faster.

---

# Lesson Recap

In this lesson you learned:

• how key-value databases work  
• how Redis stores and retrieves data  
• why Redis is extremely fast  
• how Redis is used for caching and real-time systems

Redis is one of the **fastest databases available** and is commonly used to improve application performance.

---

# Next Lesson

Next we will continue Module 14 with:

# Lesson 5 — Column-Family Databases (Cassandra)

You will learn:

• how column-family databases store data  
• how Cassandra distributes data across servers  
• why column databases scale to **massive datasets**  
• how large platforms handle billions of records.
