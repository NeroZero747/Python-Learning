# Module 14 — NoSQL & Modern Data Storage

# Lesson 5 — Column-Family Databases (Cassandra)

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **column-family databases** are  
• how **Apache Cassandra stores data**  
• how column databases differ from **relational tables**  
• why column databases scale to **massive distributed systems**

Column-family databases are designed to store **very large datasets across many servers**, often handling **billions or trillions of records**.

---

# Overview

Traditional relational databases store data **row by row**.

Example SQL table:

| user_id | name | city |
|---|---|---|
| 1 | Alice | LA |
| 2 | Bob | NY |
| 3 | Maria | SF |

Each row stores all column values together.

Column-family databases instead organize data **by column groups**.

Conceptual structure:

```text
Column: user_id → [1,2,3]
Column: name → [Alice,Bob,Maria]
Column: city → [LA,NY,SF]
```

This structure allows databases to process **large-scale analytics queries more efficiently**.

One of the most popular column-family databases is **Apache Cassandra**.

---

# Key Idea Cards (3 Cards)

### Column Databases Store Data by Columns

Instead of storing rows together, column databases group values by column.

Example:

```text
Column: revenue
Column: timestamp
Column: customer_id
```

This structure is efficient for analytical queries.

---

### Cassandra Is Built for Distributed Systems

Cassandra is designed to run on **clusters of servers**.

Example architecture:

```text
Server 1
Server 2
Server 3
Server 4
```

Data is automatically distributed across the cluster.

This allows Cassandra to scale **almost indefinitely**.

---

### Column Databases Handle Massive Data

Column-family databases are used for:

```text
Event logging
IoT data
Real-time analytics
Recommendation systems
```

These workloads may generate **billions of records per day**.

---

# Key Concepts

## Cassandra Data Model

Cassandra organizes data into several layers:

```text
Keyspace
   ↓
Table
   ↓
Rows
   ↓
Columns
```

Equivalent SQL concepts:

| Cassandra | SQL Equivalent |
|---|---|
| Keyspace | Database |
| Table | Table |
| Row | Row |
| Column | Column |

However, Cassandra tables are optimized for **distributed storage and fast writes**.

## Partition Keys

Cassandra distributes data across servers using **partition keys**.

Example table:

```text
user_activity
```

Columns:

```text
user_id
timestamp
event_type
```

Example record:

| user_id | timestamp | event_type |
|---|---|---|
| 101 | 10:00 | login |

The **partition key** determines where the data is stored in the cluster.

Example:

```text
Partition key: user_id
```

All records for that user may be stored together.

This improves query performance.

## Distributed Storage

Cassandra distributes data across multiple servers.

Example cluster:

```text
Node 1 → user_id 1–1000
Node 2 → user_id 1001–2000
Node 3 → user_id 2001–3000
```

Benefits:

```text
Scalability
Fault tolerance
High availability
```

If one server fails, the system continues operating.

## High Write Performance

Cassandra is optimized for **fast data writes**.

Example workloads:

```text
Sensor readings
User activity logs
Website events
Transaction streams
```

These systems may generate **millions of events per second**.

Cassandra can handle this by distributing writes across servers.

---

# Cassandra Query Example

Cassandra uses a SQL-like language called **CQL (Cassandra Query Language)**.

Example table creation:

```sql
CREATE TABLE user_activity (
  user_id INT,
  timestamp TIMESTAMP,
  event_type TEXT,
  PRIMARY KEY (user_id, timestamp)
);
```

Insert data:

```sql
INSERT INTO user_activity (user_id, timestamp, event_type)
VALUES (101, '2024-03-01 10:15:00', 'login');
```

Query data:

```sql
SELECT *
FROM user_activity
WHERE user_id = 101;
```

Cassandra queries must include the **partition key**.

---

# SQL vs Cassandra Example

SQL table:

| order_id | customer_id | amount |
|---|---|---|
| 1 | 101 | 50 |
| 2 | 102 | 100 |

SQL query:

```sql
SELECT *
FROM orders
WHERE customer_id = 101;
```

Cassandra equivalent:

```sql
SELECT *
FROM orders_by_customer
WHERE customer_id = 101;
```

Notice the table is designed specifically for that query.

Cassandra often requires **query-driven data modeling**.

---

# Column-Family Structure Example

Example table storing user events:

| user_id | timestamp | event |
|---|---|---|
| 101 | 10:00 | login |
| 101 | 10:05 | view_page |
| 101 | 10:08 | logout |

Query:

```sql
SELECT *
FROM user_activity
WHERE user_id = 101;
```

This retrieves events efficiently because they are stored **together in the same partition**.

---

# Decision Flow

When deciding to use Cassandra:

```text
Need to store massive datasets?
        ↓
Use column-family database
```

```text
Need extremely high write throughput?
        ↓
Cassandra works well
```

```text
Need distributed storage across servers?
        ↓
Column-family database
```

Typical use cases:

```text
Event logging
IoT platforms
Messaging systems
Analytics pipelines
```

---

# Code Examples

### Example 1 — Create Table

```sql
CREATE TABLE page_views (
  user_id INT,
  timestamp TIMESTAMP,
  page TEXT,
  PRIMARY KEY (user_id, timestamp)
);
```

### Example 2 — Insert Data

```sql
INSERT INTO page_views (user_id, timestamp, page)
VALUES (101, '2024-03-01 10:00:00', 'homepage');
```

### Example 3 — Query User Events

```sql
SELECT *
FROM page_views
WHERE user_id = 101;
```

### Example 4 — Large Event Dataset

Example event record:

```text
user_id: 101
timestamp: 2024-03-01 10:15
event: purchase
```

Millions of these events can be stored efficiently across distributed nodes.

---

# SQL vs Cassandra Comparison

| Feature | SQL Databases | Cassandra |
|---|---|---|
| storage | rows | column families |
| scaling | vertical | horizontal |
| joins | supported | limited |
| schema | fixed | query-driven |
| performance | balanced | high write throughput |

Cassandra is optimized for **large distributed workloads**.

---

# Practice Exercises

### Exercise 1

Tags: Databases, Cassandra

Explain why Cassandra distributes data across multiple servers.

### Exercise 2

Tags: Databases, Logging, Cassandra

Explain why Cassandra is good for **event logging systems**.

### Exercise 3

Tags: Databases, Partitioning, Cassandra

Describe the role of a **partition key** in Cassandra.

### Exercise 4

Tags: Databases, Cassandra

Explain why Cassandra tables are often designed **around specific queries**.

---

# Common Mistakes

### Designing Cassandra Like SQL

Cassandra does not work well with complex joins.

### Ignoring Partition Keys

Partition keys determine where data is stored.

### Using Cassandra for Small Datasets

Cassandra is optimized for **large distributed systems**.

---

# Real-World Use

Cassandra is used by many large-scale platforms.

Examples include:

```text
Netflix
Apple
Uber
Instagram
Spotify
```

Common workloads:

```text
Event tracking
Recommendation systems
Messaging systems
IoT sensor data
```

Example architecture:

```text
Application
     ↓
Kafka event stream
     ↓
Cassandra cluster
     ↓
Analytics pipeline
```

This architecture allows platforms to handle **massive volumes of real-time data**.

---

# Lesson Recap

In this lesson you learned:

• how column-family databases store data  
• how Cassandra distributes data across servers  
• how partition keys control data placement  
• why Cassandra scales to extremely large datasets

Column-family databases are essential for **large-scale distributed analytics and event systems**.

---

# Next Lesson

Next we will continue Module 14 with:

# Lesson 6 — Graph Databases (Neo4j)

You will learn:

• how graph databases store **nodes and relationships**  
• how Neo4j queries connected data  
• why graph databases are powerful for **relationship analysis**  
• how they are used for **fraud detection and recommendation systems**.
