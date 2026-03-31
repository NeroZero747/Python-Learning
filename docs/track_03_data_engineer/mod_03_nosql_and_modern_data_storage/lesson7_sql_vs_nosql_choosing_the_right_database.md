# Module 14 — NoSQL & Modern Data Storage

# Lesson 7 — SQL vs NoSQL: Choosing the Right Database

---

# Lesson Objective

By the end of this lesson learners will understand:

• the **differences between SQL and NoSQL databases**  
• when to choose **SQL vs NoSQL**  
• the **tradeoffs between consistency, scalability, and flexibility**  
• how modern systems combine **multiple database technologies**

Most real-world systems use **both SQL and NoSQL databases**, each solving different data challenges.

---

# Overview

Databases fall into two broad categories:

```text
SQL Databases
NoSQL Databases
```

SQL databases store structured data in **tables with fixed schemas**.

NoSQL databases store flexible data using structures such as:

```text
Documents
Key-value pairs
Column families
Graphs
```

Each model has advantages depending on the **type of data and workload**.

---

# Key Idea Cards (3 Cards)

### SQL Databases Are Structured

SQL databases enforce a **strict schema**.

Example table:

| user_id | name | city |
|---|---|---|
| 101 | Alice | LA |

Every row must follow the same structure.

SQL databases excel at:

```text
Transactions
Structured business data
Financial systems
Relational queries
```

---

### NoSQL Databases Are Flexible

NoSQL databases allow flexible data models.

Example document:

```json
{
  "user_id": 101,
  "name": "Alice",
  "preferences": {
    "theme": "dark"
  }
}
```

Records can contain **different fields**.

NoSQL databases excel at:

```text
Large-scale distributed systems
Flexible application data
Real-time analytics
Unstructured data
```

---

### Modern Systems Use Both

Most organizations use **polyglot persistence**, meaning multiple database technologies.

Example architecture:

```text
Transactions → SQL database
User profiles → Document database
Cache → Redis
Fraud detection → Graph database
Analytics → Data warehouse
```

Each database type handles a **specific workload**.

---

# Key Concepts

## SQL Database Characteristics

SQL databases are **relational**.

Key features:

```text
Tables
Rows
Columns
Relationships between tables
```

Example SQL query:

```sql
SELECT name
FROM customers
WHERE city = 'Los Angeles';
```

Advantages:

```text
Strong consistency
Structured schema
Powerful joins
ACID transactions
```

Popular SQL databases:

```text
PostgreSQL
MySQL
Oracle
SQL Server
```

## NoSQL Database Characteristics

NoSQL databases use **non-relational data models**.

Examples:

```text
Document databases → MongoDB
Key-value databases → Redis
Column-family databases → Cassandra
Graph databases → Neo4j
```

Advantages:

```text
Flexible schema
Horizontal scaling
High write throughput
Distributed architecture
```

---

# SQL vs NoSQL Comparison

| Feature | SQL | NoSQL |
|---|---|---|
| structure | tables | flexible models |
| schema | fixed | dynamic |
| joins | supported | limited |
| scaling | vertical | horizontal |
| consistency | strong | sometimes eventual |

---

# Example Scenario Comparison

### Financial System

Example data:

| transaction_id | amount | account |
|---|---|---|
| 1 | 100 | 101 |

Requirements:

```text
Strong consistency
Transactions
Data integrity
```

Best choice:

```text
SQL database
```

### Social Media Platform

Example data:

```json
{
  "user": "Alice",
  "followers": ["Bob", "Maria"],
  "posts": 320
}
```

Requirements:

```text
Flexible data
High scalability
Rapid writes
```

Best choice:

```text
NoSQL database
```

---

# CAP Theorem (Important Concept)

Distributed systems often follow the **CAP Theorem**.

It states that a system can only guarantee two of these three properties:

```text
Consistency
Availability
Partition tolerance
```

Explanation:

```text
Consistency → all nodes return the same data
Availability → system always responds
Partition tolerance → system continues despite network failures
```

Tradeoffs are necessary when designing distributed databases.

---

# SQL vs NoSQL Architecture Example

Example modern architecture:

```text
User Application
        ↓
API Layer
        ↓
--------------------------------
SQL Database → transactions
--------------------------------
Redis → caching
--------------------------------
MongoDB → user profiles
--------------------------------
Cassandra → event logging
--------------------------------
Neo4j → relationship analysis
```

Each database serves a **specific role**.

---

# Decision Flow

When selecting a database:

```text
Is the data highly structured with relationships?
        ↓
Use SQL
```

```text
Is the data flexible or rapidly evolving?
        ↓
Use NoSQL
```

```text
Is the system extremely large or distributed?
        ↓
NoSQL may scale better
```

Example decisions:

```text
Banking system → SQL
E-commerce product catalog → Document database
Website cache → Redis
Fraud detection → Graph database
```

---

# Code Examples

### Example 1 — SQL Query

```sql
SELECT *
FROM customers
WHERE city = 'New York';
```

### Example 2 — MongoDB Query

```javascript
db.customers.find({ city: "New York" })
```

### Example 3 — Redis Lookup

```text
GET session_101
```

### Example 4 — Graph Query

```cypher
MATCH (a:Person)-[:FRIEND]->(b)
RETURN b
```

Each database uses a **different query style**.

---

# Practice Exercises

### Exercise 1

Tags: Missing Data, Databases, NoSQL

Explain why SQL databases are ideal for **financial transactions**.

### Exercise 2

Tags: Databases, NoSQL

Explain why NoSQL databases scale well for **large web applications**.

### Exercise 3

Tags: WHERE, Databases, HTTP Methods, NoSQL

Describe a scenario where both **SQL and NoSQL databases** would be used together.

### Exercise 4

Tags: Databases, NoSQL

Explain the tradeoff between **consistency and scalability**.

---

# Common Mistakes

### Assuming NoSQL Replaces SQL

NoSQL does not replace SQL.

### Choosing NoSQL Without a Clear Need

Relational databases are often simpler for structured data.

### Ignoring Data Relationships

If data contains complex relationships, relational databases or graph databases may be better.

---

# Real-World Use

Large technology companies use **multiple databases simultaneously**.

Examples include:

```text
Amazon → DynamoDB + Aurora + Redis
Netflix → Cassandra + MySQL
Facebook → MySQL + graph databases
Uber → PostgreSQL + Cassandra + Redis
```

Example architecture:

```text
Mobile App
     ↓
API
     ↓
SQL database → transactions
NoSQL database → user profiles
Redis cache → fast access
Analytics pipeline → large-scale data processing
```

This architecture allows systems to **handle both structured and massive-scale data workloads**.

---

# Lesson Recap

In this lesson you learned:

• the differences between SQL and NoSQL databases  
• when to use SQL vs NoSQL  
• how modern systems combine multiple databases  
• how tradeoffs affect system design

Understanding SQL and NoSQL together allows engineers to **design scalable data architectures**.

---

# Module 14 Complete

You have now learned the foundations of NoSQL systems:

```text
What NoSQL databases are
Types of NoSQL databases
Document databases (MongoDB)
Key-value databases (Redis)
Column-family databases (Cassandra)
Graph databases (Neo4j)
SQL vs NoSQL decision frameworks
```

These concepts form the **modern foundation of large-scale data systems**.
