# Module 14 — NoSQL & Modern Data Storage

# Lesson 2 — Types of NoSQL Databases

---

# Lesson Objective

By the end of this lesson learners will understand:

• the **four main categories of NoSQL databases**  
• how each database type stores data  
• what problems each type is designed to solve  
• when organizations choose each database model

Not all NoSQL databases are the same. They are optimized for **different types of data and workloads**.

---

# Overview

NoSQL databases are commonly divided into **four major categories**:

```text
1. Document Databases
2. Key-Value Databases
3. Column-Family Databases
4. Graph Databases
```

Each category is designed for **specific data patterns and application needs**.

Example comparison:

| Database Type | Example | Primary Use |
|---|---|---|
| Document | MongoDB | flexible application data |
| Key-Value | Redis | caching and fast lookups |
| Column-Family | Cassandra | large-scale analytics |
| Graph | Neo4j | relationship analysis |

Understanding these types helps engineers choose the **right database for the right problem**.

---

# Key Idea Cards (3 Cards)

### NoSQL Is Not One Database Type

Unlike SQL databases which use tables, NoSQL databases can store data in multiple structures.

Examples include:

```text
Documents
Key-value pairs
Columns
Graphs
```

Each structure is optimized for different workloads.

---

### Each NoSQL Model Solves Different Problems

Example use cases:

```text
Document → flexible application data
Key-value → extremely fast lookups
Column-family → large distributed datasets
Graph → relationship-heavy data
```

---

### Modern Systems Often Combine Multiple Databases

Large platforms often use **multiple database types**.

Example architecture:

```text
User profiles → Document DB
Caching → Key-value store
Analytics → Column database
Fraud detection → Graph database
```

---

# Key Concepts

## 1. Document Databases

Document databases store data as **documents**, typically using **JSON format**.

Example document:

```json
{
  "customer_id": 101,
  "name": "Alice",
  "orders": [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 25}
  ]
}
```

Instead of separating data into multiple tables, related data can be stored **within a single document**.

Popular document databases:

```text
MongoDB
CouchDB
Firebase Firestore
```

Advantages:

```text
Flexible schema
Natural JSON storage
Great for web applications
```

Common use cases:

```text
User profiles
Product catalogs
Content management systems
Mobile apps
```

---

## 2. Key-Value Databases

Key-value databases store data as **simple key-value pairs**.

Example:

```text
Key: user_102
Value: {name: "Bob", city: "NY"}
```

Retrieval is extremely fast because the database simply looks up the key.

Example query concept:

```text
GET user_102
```

Popular key-value databases:

```text
Redis
Amazon DynamoDB
Riak
```

Advantages:

```text
Extremely fast
Simple structure
High scalability
```

Common use cases:

```text
Caching
Session storage
Real-time applications
Leaderboards
```

Example:

```text
User login sessions
Shopping cart data
Website caching
```

---

## 3. Column-Family Databases

Column-family databases store data in **columns instead of rows**.

Traditional SQL table:

| ID | Name | City |
|---|---|---|
| 1 | Alice | LA |

Column database structure:

```text
Column: ID → [1,2,3]
Column: Name → [Alice,Bob,Maria]
Column: City → [LA,NY,SF]
```

This structure is optimized for **large-scale analytics queries**.

Popular column-family databases:

```text
Apache Cassandra
HBase
Google Bigtable
```

Advantages:

```text
Handles massive datasets
Distributed architecture
Fast analytical queries
```

Common use cases:

```text
Event logging
IoT data
Recommendation systems
Large-scale analytics
```

These databases are designed to store **billions of rows across many servers**.

---

## 4. Graph Databases

Graph databases store data using **nodes and relationships**.

Example structure:

```text
User A → FRIEND → User B
User B → FRIEND → User C
User A → PURCHASED → Product X
```

Instead of tables, data is stored as a **network of relationships**.

Example representation:

```text
Node → entity
Edge → relationship
```

Popular graph databases:

```text
Neo4j
Amazon Neptune
ArangoDB
```

Advantages:

```text
Excellent for relationship analysis
Fast graph traversal
Natural representation of networks
```

Common use cases:

```text
Social networks
Fraud detection
Recommendation engines
Knowledge graphs
```

Example fraud detection pattern:

```text
Customer → shared phone → multiple accounts
```

Graph databases make these patterns easier to detect.

---

# Decision Flow

When choosing a NoSQL database:

```text
Need flexible JSON data?
        ↓
Use Document Database
```

```text
Need extremely fast key lookups?
        ↓
Use Key-Value Database
```

```text
Need massive distributed analytics storage?
        ↓
Use Column-Family Database
```

```text
Need relationship analysis?
        ↓
Use Graph Database
```

Choosing the right database depends on **the structure of the data and the queries being performed**.

---

# Code Examples

### Example 1 — Document Database Record

```json
{
  "user_id": 9001,
  "name": "Alice",
  "purchases": [
    {"item": "Laptop", "price": 1200}
  ]
}
```

---

### Example 2 — Key-Value Record

```text
Key: session_9281
Value: {user_id: 1001, login_time: "10:15"}
```

---

### Example 3 — Column Database Example

Column storage structure:

```text
Column: timestamp
Column: event_type
Column: user_id
```

Large datasets are stored across distributed servers.

---

### Example 4 — Graph Database Relationship

Graph example:

```text
User A → FOLLOWS → User B
User B → FOLLOWS → User C
```

Graph databases can easily find patterns like:

```text
Friends of friends
Recommendation connections
```

---

# SQL / NoSQL Model Comparison

| Model | Structure | Example |
|---|---|---|
| SQL | tables | PostgreSQL |
| Document | JSON documents | MongoDB |
| Key-value | key → value | Redis |
| Column-family | distributed columns | Cassandra |
| Graph | nodes + edges | Neo4j |

Each model is designed to solve **different data problems**.

---

# Practice Exercises

### Exercise 1

Tags: Databases, NoSQL

Explain why **document databases are good for web applications**.

---

### Exercise 2

Tags: Databases, Caching, NoSQL

Explain why **key-value databases are used for caching**.

---

### Exercise 3

Tags: Visualization, WHERE, Databases, NoSQL

Describe a scenario where **graph databases are useful**.

---

### Exercise 4

Tags: Databases, NoSQL

Explain why column-family databases are used for **large-scale analytics**.

---

# Common Mistakes

### Thinking One Database Fits All Problems

Different data problems require different database models.

Example:

```text
Transactions → SQL
User profiles → Document DB
Cache → Redis
Fraud detection → Graph DB
```

---

### Ignoring Query Patterns

Database design should consider **how the data will be queried**.

Example:

```text
Relationship queries → Graph DB
Fast lookups → Key-value
```

---

### Choosing NoSQL Without Understanding Tradeoffs

NoSQL databases may sacrifice:

```text
Strict schema
Complex joins
Strong consistency
```

Understanding tradeoffs is important.

---

# Real-World Use

Many modern platforms use multiple NoSQL databases.

Examples:

```text
Netflix → Cassandra
Amazon → DynamoDB
LinkedIn → graph databases
Twitter → Redis + Cassandra
```

Example architecture:

```text
Web Application
      ↓
User Profiles → Document DB
Caching → Redis
Analytics → Cassandra
Recommendations → Graph DB
```

Large systems often combine multiple database technologies.

---

# Lesson Recap

In this lesson you learned:

• the four major types of NoSQL databases  
• how each database stores data  
• the problems each type solves  
• when organizations use each database model

Understanding these database types helps engineers choose the **best storage solution for different data problems**.

---

# Next Lesson

Next we will continue Module 14 with:

# Lesson 3 — Document Databases (MongoDB)

You will learn:

• how document databases work  
• how JSON documents are stored  
• how MongoDB queries data  
• how document databases compare to SQL tables.
