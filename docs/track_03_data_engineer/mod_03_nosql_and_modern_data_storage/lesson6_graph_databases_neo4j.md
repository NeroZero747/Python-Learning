# Module 14 — NoSQL & Modern Data Storage

# Lesson 6 — Graph Databases (Neo4j)

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **graph databases** are  
• how **nodes and relationships** represent data  
• how graph queries work in **Neo4j**  
• why graph databases are powerful for **relationship analysis**

Graph databases are designed to analyze **connections between data**, which can be difficult to model in traditional relational databases.

---

# Overview

Most databases store data in **tables or documents**.

Graph databases instead represent data as a **network of connected entities**.

Core components of graph databases:

```text
Nodes → entities
Relationships → connections
Properties → attributes
```

Example graph:

```text
Alice → FRIEND → Bob
Bob → FRIEND → Maria
Alice → PURCHASED → Laptop
```

This structure makes it easy to analyze **complex relationships between entities**.

One of the most popular graph databases is **Neo4j**.

---

# Key Idea Cards (3 Cards)

### Graph Databases Model Relationships

Graph databases are built specifically to analyze connections.

Example:

```text
Person → FRIEND → Person
Customer → PURCHASED → Product
Account → TRANSFERRED → Account
```

Relationships are stored **directly in the database structure**.

---

### Graph Queries Follow Relationships

Graph databases can easily answer questions like:

```text
Friends of friends
Customers who bought similar products
Accounts connected through transactions
```

These queries can be difficult in relational databases.

---

### Graph Databases Power Recommendation Systems

Graph databases are commonly used for:

```text
Social networks
Recommendation engines
Fraud detection
Knowledge graphs
```

These systems depend on understanding **how entities connect to each other**.

---

# Key Concepts

## Nodes

A **node** represents an entity.

Examples:

```text
Person
Customer
Product
Account
City
```

Example node:

```text
Node: Person
Properties:
name: Alice
age: 30
city: LA
```

Graph representation:

```text
(Alice)
```

Nodes may contain **properties**, which store attributes.

## Relationships

A **relationship** connects two nodes.

Example:

```text
(Alice) → FRIEND → (Bob)
```

Relationships are directional.

Example:

```text
(Alice) → PURCHASED → (Laptop)
```

Relationships may also contain properties.

Example:

```text
(Alice) → PURCHASED → (Laptop)

Properties:
date: 2024-01-01
price: 1200
```

## Graph Structure

Example graph:

```text
(Alice) → FRIEND → (Bob)
(Bob) → FRIEND → (Maria)
(Alice) → PURCHASED → (Laptop)
(Maria) → PURCHASED → (Phone)
```

This structure allows queries such as:

```text
Friends of Alice
Products purchased by friends of Alice
```

Graph traversal makes these queries efficient.

---

# Neo4j Query Language (Cypher)

Neo4j uses a query language called **Cypher**.

Cypher uses a visual pattern syntax to describe relationships.

Example syntax:

```text
(node)-[relationship]->(node)
```

## Create Nodes

Example:

```cypher
CREATE (p:Person {name: "Alice", age: 30})
```

## Create Relationships

Example:

```cypher
MATCH (a:Person {name: "Alice"})
MATCH (b:Person {name: "Bob"})
CREATE (a)-[:FRIEND]->(b)
```

This creates a relationship:

```text
Alice → FRIEND → Bob
```

## Query Nodes

Example:

```cypher
MATCH (p:Person)
RETURN p
```

## Query Relationships

Example:

```cypher
MATCH (a:Person)-[:FRIEND]->(b:Person)
RETURN a, b
```

Result:

```text
Alice → Bob
Bob → Maria
```

---

# Graph Database Example

Graph model:

```text
(Alice) → FRIEND → (Bob)
(Bob) → FRIEND → (Maria)
(Alice) → PURCHASED → (Laptop)
(Bob) → PURCHASED → (Laptop)
(Maria) → PURCHASED → (Phone)
```

Example query:

```cypher
MATCH (a:Person {name:"Alice"})-[:FRIEND]->(friends)
RETURN friends
```

Result:

```text
Bob
```

Another query:

```cypher
MATCH (a:Person {name:"Alice"})-[:FRIEND]->(f)-[:PURCHASED]->(product)
RETURN product
```

Result:

```text
Laptop
```

This identifies **products purchased by Alice’s friends**.

---

# SQL vs Graph Query Comparison

Relational query example:

```sql
SELECT p.product
FROM customers c
JOIN purchases p
ON c.customer_id = p.customer_id
JOIN friendships f
ON c.customer_id = f.customer_id
WHERE c.name = 'Alice';
```

Graph query:

```cypher
MATCH (Alice)-[:FRIEND]->()-[:PURCHASED]->(product)
RETURN product
```

Graph queries are often **simpler when analyzing relationships**.

---

# Decision Flow

When deciding to use a graph database:

```text
Is the data highly connected?
        ↓
Graph database works well
```

```text
Need relationship analysis?
        ↓
Use graph database
```

Example use cases:

```text
Social networks
Fraud detection
Recommendation engines
Network analysis
```

---

# Code Examples

### Example 1 — Create Person Node

```cypher
CREATE (:Person {name: "Alice"})
```

### Example 2 — Create Relationship

```cypher
CREATE (Alice)-[:FRIEND]->(Bob)
```

### Example 3 — Find Friends

```cypher
MATCH (p:Person)-[:FRIEND]->(friend)
RETURN friend
```

### Example 4 — Recommendation Query

```cypher
MATCH (user)-[:FRIEND]->(friend)-[:PURCHASED]->(product)
RETURN product
```

This identifies **recommended products based on social connections**.

---

# SQL vs Graph Database Comparison

| Feature | SQL Databases | Graph Databases |
|---|---|---|
| structure | tables | nodes + edges |
| relationships | foreign keys | direct relationships |
| joins | required | not required |
| queries | complex joins | graph traversal |
| performance | moderate | excellent for relationship queries |

Graph databases excel at analyzing **deep connections between entities**.

---

# Practice Exercises

### Exercise 1

Tags: Visualization, Databases, Neo4j

Explain why graph databases are ideal for **social networks**.

### Exercise 2

Tags: Visualization, Databases, Neo4j

Describe how a graph database could be used for **fraud detection**.

### Exercise 3

Tags: Visualization, Databases, Neo4j

Explain the difference between a **node** and a **relationship**.

### Exercise 4

Tags: Visualization, SQL Queries, Databases, Neo4j

Write a Cypher query to find **friends of Alice**.

---

# Common Mistakes

### Using Graph Databases for Non-Relational Data

Graph databases are optimized for **relationship-heavy datasets**.

### Overcomplicating Data Models

Graph models should focus on **meaningful relationships**.

### Confusing Graph Relationships with SQL Joins

Graph relationships are stored directly in the database.

---

# Real-World Use

Graph databases power many modern systems.

Examples include:

```text
Facebook → social network analysis
LinkedIn → connection recommendations
PayPal → fraud detection
Netflix → recommendation systems
```

Example fraud detection pattern:

```text
Account A → same phone number → Account B
Account B → same IP address → Account C
```

Graph queries can quickly detect suspicious patterns.

Example architecture:

```text
Application
     ↓
Graph Database
     ↓
Fraud Detection Engine
```

Graph databases allow systems to analyze **complex networks of relationships** efficiently.

---

# Lesson Recap

In this lesson you learned:

• how graph databases store nodes and relationships  
• how Neo4j queries connected data  
• why graph databases are powerful for relationship analysis  
• how graph databases power recommendation and fraud detection systems

Graph databases are the best solution when analyzing **connections between entities**.

---

# Next Lesson

Next we will complete Module 14 with:

# Lesson 7 — SQL vs NoSQL: Choosing the Right Database

You will learn:

• when to choose SQL vs NoSQL  
• how modern architectures combine both  
• the tradeoffs between consistency, scalability, and flexibility  
• how real-world systems use multiple database types.
