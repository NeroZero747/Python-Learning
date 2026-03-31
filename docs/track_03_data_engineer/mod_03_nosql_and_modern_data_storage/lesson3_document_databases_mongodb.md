# Module 14 — NoSQL & Modern Data Storage

# Lesson 3 — Document Databases (MongoDB)

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **document databases** are  
• how **MongoDB stores data using JSON documents**  
• how documents compare to **SQL tables**  
• how basic **MongoDB queries** work

Document databases are the **most commonly used NoSQL databases**, especially for modern web applications.

---

# Overview

A **document database** stores data as **documents**, typically in **JSON format**.

Example document:

```json
{
  "customer_id": 101,
  "name": "Alice",
  "city": "Los Angeles",
  "orders": [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 25}
  ]
}
```

Instead of splitting data into multiple tables like SQL, related information can be stored **within the same document**.

This reduces the need for complex joins.

Popular document databases include:

```text
MongoDB
CouchDB
Firebase Firestore
Amazon DocumentDB
```

Among these, **MongoDB** is the most widely used.

---

# Key Idea Cards (3 Cards)

### Documents Store Related Data Together

In relational databases, related data is stored in **multiple tables**.

Example SQL structure:

```text
Customers table
Orders table
Products table
```

Document databases allow this data to be stored **within a single document**.

This can simplify application development.

---

### Documents Use JSON Format

Most document databases use **JSON-like structures**.

Example:

```json
{
  "product": "Laptop",
  "price": 1200,
  "category": "Electronics"
}
```

This format matches how many applications already represent data.

---

### Schema is Flexible

Document databases allow records to have **different structures**.

Example:

```json
{ "name": "Alice", "city": "LA" }

{ "name": "Bob", "orders": 10 }

{ "name": "Maria", "preferences": {"color": "blue"} }
```

Unlike SQL tables, documents do not require identical columns.

---

# Key Concepts

## Database → Collection → Document

MongoDB organizes data in three layers:

```text
Database
   ↓
Collection
   ↓
Documents
```

Example:

```text
Database: store_app
Collection: customers
Document: individual customer record
```

Equivalent SQL structure:

| SQL Concept | MongoDB Equivalent |
|---|---|
| Database | Database |
| Table | Collection |
| Row | Document |
| Column | Field |

---

## Example MongoDB Document

Example customer document:

```json
{
  "_id": 101,
  "name": "Alice",
  "city": "Los Angeles",
  "orders": [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 25}
  ]
}
```

Important components:

```text
_id → unique identifier
fields → attributes of the record
nested objects → related data
arrays → multiple related items
```

---

## Nested Documents

MongoDB allows documents to contain **nested objects**.

Example:

```json
{
  "name": "Alice",
  "address": {
    "city": "Los Angeles",
    "zip": "90001"
  }
}
```

This allows complex data structures to be stored naturally.

---

## Arrays in Documents

Documents can also store arrays.

Example:

```json
{
  "name": "Alice",
  "orders": [
    {"product": "Laptop"},
    {"product": "Keyboard"},
    {"product": "Mouse"}
  ]
}
```

This allows one document to store **multiple related records**.

---

# MongoDB vs SQL Example

SQL structure:

**Customers table**

| customer_id | name | city |
|---|---|---|
| 101 | Alice | LA |

**Orders table**

| order_id | customer_id | product |
|---|---|---|
| 1 | 101 | Laptop |

This requires a join:

```sql
SELECT *
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id;
```

MongoDB document structure:

```json
{
  "customer_id": 101,
  "name": "Alice",
  "orders": [
    {"product": "Laptop"}
  ]
}
```

The relationship is already stored inside the document.

---

# Basic MongoDB Queries

MongoDB uses **JavaScript-style query syntax** instead of SQL.

### Example 1 — Retrieve All Documents

SQL:

```sql
SELECT * FROM customers;
```

MongoDB:

```javascript
db.customers.find()
```

### Example 2 — Filter Records

SQL:

```sql
SELECT *
FROM customers
WHERE city = 'Los Angeles';
```

MongoDB:

```javascript
db.customers.find({ city: "Los Angeles" })
```

### Example 3 — Insert Document

SQL:

```sql
INSERT INTO customers (name, city)
VALUES ('Alice', 'LA');
```

MongoDB:

```javascript
db.customers.insertOne({
  name: "Alice",
  city: "LA"
})
```

### Example 4 — Update Document

SQL:

```sql
UPDATE customers
SET city = 'San Diego'
WHERE name = 'Alice';
```

MongoDB:

```javascript
db.customers.updateOne(
  { name: "Alice" },
  { $set: { city: "San Diego" } }
)
```

---

# SQL vs MongoDB Comparison

| SQL | MongoDB |
|---|---|
| tables | collections |
| rows | documents |
| columns | fields |
| joins | embedded documents |
| SQL language | JSON queries |

MongoDB queries resemble **JavaScript object syntax**.

---

# Decision Flow

When deciding whether to use a document database:

```text
Is the data JSON-like or hierarchical?
        ↓
Use document database
```

```text
Do records have flexible structure?
        ↓
Document database works well
```

Example use cases:

```text
User profiles
Product catalogs
Content management
Mobile apps
```

---

# Code Examples

### Example 1 — Product Document

```json
{
  "product_id": 1001,
  "name": "Laptop",
  "price": 1200,
  "category": "Electronics"
}
```

### Example 2 — User Profile

```json
{
  "username": "data_guru",
  "followers": 12000,
  "posts": 350
}
```

### Example 3 — Order Document

```json
{
  "order_id": 501,
  "customer": "Alice",
  "items": [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 25}
  ]
}
```

### Example 4 — Event Log Document

```json
{
  "timestamp": "2024-03-01T10:15:00",
  "event": "user_login",
  "user_id": 1234
}
```

This structure works well for **log storage and event tracking**.

---

# Practice Exercises

### Exercise 1

Tags: Databases, NoSQL, Performance Profiling, MongoDB

Explain why document databases are well suited for **user profile data**.

### Exercise 2

Tags: Databases, NoSQL, MongoDB

Explain how nested documents reduce the need for **SQL joins**.

### Exercise 3

Tags: SELECT, SQL Queries, Databases, NoSQL

Write a MongoDB query to retrieve all users from **New York**.

### Exercise 4

Tags: Databases, NoSQL, MongoDB

Explain the difference between a **collection** and a **document**.

---

# Common Mistakes

### Treating MongoDB Like SQL

MongoDB is designed differently than relational databases.

Instead of many tables and joins, MongoDB often stores related data **inside documents**.

### Storing Too Much Data in One Document

Documents should remain manageable in size.

Very large documents can impact performance.

### Ignoring Data Modeling

Even though schemas are flexible, good data modeling is still important.

Design should consider:

```text
Query patterns
Update frequency
Document size
```

---

# Real-World Use

Many modern applications use document databases.

Examples include:

```text
E-commerce product catalogs
User profile systems
Content management platforms
Mobile applications
Real-time web applications
```

Example architecture:

```text
Web Application
      ↓
API
      ↓
MongoDB
```

MongoDB stores application data in flexible document structures.

Large platforms using document databases include:

```text
eBay
Adobe
LinkedIn
Shopify
```

---

# Lesson Recap

In this lesson you learned:

• what document databases are  
• how MongoDB stores JSON documents  
• how documents compare to SQL tables  
• how MongoDB queries data

Document databases are powerful for storing **flexible, hierarchical data used by modern applications**.

---

# Next Lesson

Next we will continue Module 14 with:

# Lesson 4 — Key-Value Databases (Redis)

You will learn:

• how key-value databases work  
• how Redis stores data in memory  
• why Redis is extremely fast  
• how caching improves application performance.
