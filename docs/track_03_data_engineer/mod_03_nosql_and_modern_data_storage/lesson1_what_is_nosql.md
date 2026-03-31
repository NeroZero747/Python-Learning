# Module 14 — NoSQL & Modern Data Storage

# Lesson 1 — What is NoSQL?

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **NoSQL databases** are  
• why NoSQL databases were created  
• how NoSQL differs from **traditional SQL databases**  
• the types of problems NoSQL databases solve

This lesson introduces the concept of **non-relational databases** used in modern data systems.

---

# Overview

Traditional databases like:

- PostgreSQL  
- MySQL  
- Oracle  
- SQL Server  

store data in **structured tables** with fixed schemas.

Example SQL table:

| customer_id | name | city |
|---|---|---|
| 101 | Alice | LA |
| 102 | Bob | NY |

These are called **relational databases**.

However, modern applications began generating new types of data:

```text
Web activity logs
User profiles
Product catalogs
Sensor data
JSON API responses
```

These datasets are often:

```text
Large
Flexible
Unstructured
Rapidly changing
```

To handle this, **NoSQL databases** were developed.

NoSQL stands for:

```text
Not Only SQL
```

It represents databases designed to store **non-tabular or flexible data structures**.

---

# Key Idea Cards (3 Cards)

### SQL Databases Use Tables

Traditional relational databases store data like spreadsheets.

Example:

```text
Rows
Columns
Fixed schema
Relationships between tables
```

This structure works well for **structured business data**.

---

### NoSQL Databases Store Flexible Data

NoSQL databases store data in formats such as:

```text
Documents
Key-value pairs
Graphs
Wide-column tables
```

These formats allow applications to store **complex and evolving data**.

---

### NoSQL Supports Large-Scale Applications

Many modern platforms rely on NoSQL databases because they scale well.

Examples include:

```text
Social media platforms
E-commerce systems
Streaming platforms
Real-time analytics
```

---

# Key Concepts

## Relational Databases

Relational databases organize data into **tables with relationships**.

Example:

```text
Customers Table
Orders Table
Products Table
```

Relationships connect tables using keys.

Example:

```text
customer_id
product_id
order_id
```

SQL queries retrieve and combine this structured data.

Example SQL query:

```sql
SELECT name, order_date
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id;
```

---

## NoSQL Databases

NoSQL databases store data in **more flexible structures**.

Example document structure:

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

Instead of storing orders in a separate table, they can be stored **inside the same document**.

This reduces the need for complex joins.

---

## Schema Flexibility

Relational databases require predefined schemas.

Example SQL table:

```text
customer_id INT
name VARCHAR
city VARCHAR
```

Every row must follow the same structure.

NoSQL databases allow flexible schemas.

Example:

```json
{ "name": "Alice", "city": "LA" }

{ "name": "Bob", "orders": 12 }

{ "name": "Maria", "preferences": {"color": "blue"} }
```

Each record can have **different fields**.

---

## Horizontal Scaling

Traditional SQL databases often scale by upgrading hardware.

```text
More CPU
More RAM
Larger server
```

This is called **vertical scaling**.

NoSQL databases are designed for **horizontal scaling**, meaning:

```text
More servers
Distributed systems
Cloud-based clusters
```

This allows them to handle **massive datasets**.

---

# Decision Flow

When choosing between SQL and NoSQL:

```text
Is the data structured with clear relationships?
        ↓
Use SQL
```

If data is flexible or rapidly evolving:

```text
Use NoSQL
```

Example scenarios:

```text
Financial transactions → SQL
User activity logs → NoSQL
Product catalogs → NoSQL
Customer billing → SQL
```

---

# Code Examples

### Example 1 — SQL Table Structure

Relational database:

```text
Customers Table
```

| customer_id | name | city |
|---|---|---|
| 101 | Alice | LA |
| 102 | Bob | NY |

SQL query:

```sql
SELECT *
FROM customers;
```

---

### Example 2 — NoSQL Document

Document database example:

```json
{
  "customer_id": 101,
  "name": "Alice",
  "city": "LA",
  "orders": [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 25}
  ]
}
```

This structure allows related data to be stored together.

---

### Example 3 — JSON Data Storage

NoSQL databases commonly store **JSON documents**.

Example API response:

```json
{
  "user_id": 9021,
  "username": "data_guru",
  "followers": 12000
}
```

NoSQL databases store this data naturally.

---

### Example 4 — Real-Time Logging

NoSQL is often used for log storage.

Example record:

```json
{
  "timestamp": "2024-03-01T10:15:00",
  "event": "user_login",
  "user_id": 1234
}
```

Millions of these records can be stored efficiently.

---

# SQL vs NoSQL Comparison

| Feature | SQL Databases | NoSQL Databases |
|---|---|---|
| structure | tables | flexible documents |
| schema | fixed | dynamic |
| joins | common | uncommon |
| scaling | vertical | horizontal |
| query language | SQL | varies |

Examples of SQL databases:

```text
PostgreSQL
MySQL
Oracle
SQL Server
```

Examples of NoSQL databases:

```text
MongoDB
Cassandra
Redis
Neo4j
DynamoDB
```

---

# Practice Exercises

### Exercise 1

Tags: Databases, Schema, NoSQL

Explain why relational databases use **fixed schemas**.

---

### Exercise 2

Tags: NoSQL, SQL

Give two examples of data that might be better suited for **NoSQL storage**.

---

### Exercise 3

Tags: NoSQL, SQL

Explain the difference between **horizontal scaling and vertical scaling**.

---

### Exercise 4

Tags: Databases, NoSQL

Explain why storing **JSON documents** fits well in NoSQL databases.

---

# Common Mistakes

### Assuming NoSQL Replaces SQL

NoSQL does **not replace SQL**.

Most organizations use **both together**.

Example architecture:

```text
Transactions → SQL database
User activity → NoSQL database
Analytics → Data warehouse
```

---

### Using NoSQL for Highly Structured Data

If data contains:

```text
Clear relationships
Financial transactions
Strict schema requirements
```

SQL databases are usually better.

---

### Ignoring Data Consistency

Some NoSQL databases prioritize **availability and scalability** over strict consistency.

This tradeoff is important to understand in system design.

---

# Real-World Use

NoSQL databases power many large-scale platforms.

Examples:

```text
Netflix
Amazon
Facebook
Uber
Spotify
```

Common use cases:

```text
User profiles
Recommendation systems
Real-time analytics
Product catalogs
IoT data storage
```

Example architecture:

```text
Application → NoSQL database → analytics pipeline
```

This allows systems to handle **massive volumes of flexible data**.

---

# Lesson Recap

In this lesson you learned:

• what NoSQL databases are  
• why they were developed  
• how they differ from relational databases  
• when NoSQL is used in modern systems

NoSQL databases allow organizations to **store large volumes of flexible and rapidly changing data**.

---

# Next Lesson

Next we will continue Module 14 with:

# Lesson 2 — Types of NoSQL Databases

You will learn:

• the four major types of NoSQL databases  
• document databases  
• key-value stores  
• column-family databases  
• graph databases.
