# Module 12 — SQL Foundations

# Lesson 4 — Filtering Data with WHERE

---

# Lesson Objective

By the end of this lesson learners will understand:

• how to **filter rows using the WHERE clause**  
• how **comparison operators** work in SQL  
• how to combine conditions using **AND and OR**  
• how analysts isolate specific records from large datasets  

Filtering data is one of the most common tasks in SQL because analysts rarely need **every row in a table**.

---

# Overview

In real-world datasets, tables can contain **thousands or millions of records**.

Example table:

| customer_id | name | city | age |
|---|---|---|---|
| 101 | Maria | Los Angeles | 32 |
| 102 | James | Chicago | 41 |
| 103 | Sarah | New York | 28 |
| 104 | Daniel | Los Angeles | 45 |

If we run:

```sql
SELECT *
FROM customers;
```

We retrieve **all rows**.

But often we only want **specific records**.

Example:

```text
Customers from Los Angeles
```

SQL allows us to filter rows using the **WHERE clause**.

Example query:

```sql
SELECT *
FROM customers
WHERE city = 'Los Angeles';
```

Result:

| customer_id | name | city | age |
|---|---|---|---|
| 101 | Maria | Los Angeles | 32 |
| 104 | Daniel | Los Angeles | 45 |

The WHERE clause filters the dataset to only the rows that meet the condition.

---

# Key Idea Cards (3 Cards)

### WHERE Filters Rows

The WHERE clause restricts the rows returned by a query.

Example:

```sql
SELECT *
FROM customers
WHERE city = 'Chicago';
```

Only rows meeting the condition are returned.

---

### Conditions Use Comparison Operators

SQL compares values using operators such as:

```text
=
>
<
>=
<=
<>
```

Example:

```sql
WHERE age > 30
```

---

### Multiple Conditions Can Be Combined

SQL allows combining filters using logical operators.

Example:

```sql
WHERE city = 'Los Angeles'
AND age > 35
```

---

# Key Concepts

## Comparison Operators

SQL uses operators to compare values.

| Operator | Meaning |
|---|---|
| = | equal to |
| > | greater than |
| < | less than |
| >= | greater than or equal |
| <= | less than or equal |
| <> | not equal |

Example:

```sql
SELECT *
FROM customers
WHERE age > 30;
```

---

## AND Operator

The **AND operator** requires all conditions to be true.

Example:

```sql
SELECT *
FROM customers
WHERE city = 'Los Angeles'
AND age > 35;
```

Result:

| name | city | age |
|---|---|---|
| Daniel | Los Angeles | 45 |

Both conditions must be satisfied.

---

## OR Operator

The **OR operator** returns rows where at least one condition is true.

Example:

```sql
SELECT *
FROM customers
WHERE city = 'Los Angeles'
OR city = 'Chicago';
```

Result includes customers from both cities.

---

# Decision Flow

When filtering data:

```text
What rows are needed?
        ↓
Define filter condition
        ↓
Apply WHERE clause
        ↓
Return filtered results
```

Example workflow:

```text
Need customers older than 40
        ↓
WHERE age > 40
```

---

# Code Examples

### Example 1 — Basic Filter

```sql
SELECT *
FROM customers
WHERE city = 'Chicago';
```

This returns customers from Chicago.

---

### Example 2 — Numeric Filter

```sql
SELECT *
FROM customers
WHERE age > 30;
```

This returns customers older than 30.

---

### Example 3 — Multiple Conditions

```sql
SELECT *
FROM customers
WHERE city = 'Los Angeles'
AND age > 40;
```

Only customers meeting both conditions appear.

---

### Example 4 — OR Condition

```sql
SELECT *
FROM customers
WHERE city = 'Chicago'
OR city = 'New York';
```

Returns customers from either city.

---

# SQL / Excel Comparison

Filtering in SQL is similar to filtering in Excel.

| SQL | Excel | Python |
|---|---|---|
| WHERE | Filter rows | df[df["column"] == value] |
| AND | multiple filter rules | & |
| OR | filter alternatives | \| |

Example Excel filter:

```text
City = Los Angeles
```

Equivalent SQL query:

```sql
SELECT *
FROM customers
WHERE city = 'Los Angeles';
```

Equivalent Python:

```python
df[df["city"] == "Los Angeles"]
```

---

# Practice Exercises

### Exercise 1

Tags: Filtering, SELECT, WHERE

Retrieve customers who live in **New York**.

Table:

```text
customers
```

---

### Exercise 2

Tags: Filtering, SELECT, WHERE, Arithmetic

Retrieve products with price greater than **100**.

Table:

```text
products
```

---

### Exercise 3

Tags: Missing Data, Filtering, SELECT, WHERE

Retrieve employees who work in the **Finance department**.

Table:

```text
employees
```

---

### Exercise 4

Tags: Filtering, SELECT, WHERE

Retrieve customers who live in **Los Angeles and are older than 30**.

---

# Common Mistakes

### Missing Quotes for Text

Incorrect:

```sql
WHERE city = Los Angeles
```

Correct:

```sql
WHERE city = 'Los Angeles'
```

Text values must be enclosed in quotes.

---

### Using AND Instead of OR

Incorrect logic may filter out desired results.

Example:

```sql
WHERE city = 'Chicago'
AND city = 'New York'
```

No row can satisfy both conditions simultaneously.

Correct:

```sql
WHERE city = 'Chicago'
OR city = 'New York'
```

---

### Filtering Wrong Column

Always verify the column name exists in the table.

Incorrect:

```sql
WHERE location = 'Chicago'
```

Correct:

```sql
WHERE city = 'Chicago'
```

---

# Real-World Use

Filtering is one of the most common operations analysts perform.

Example use cases:

```text
Customers in a specific region
Sales above a certain threshold
Orders placed in the last month
Claims exceeding a certain cost
```

Example business query:

```sql
SELECT *
FROM claims
WHERE claim_amount > 10000;
```

This identifies high-cost claims for further investigation.

Filtering allows analysts to **focus on relevant subsets of data**.

---

# Lesson Recap

In this lesson you learned:

• how the WHERE clause filters rows  
• how comparison operators work  
• how AND and OR combine conditions  
• how analysts isolate specific records

Filtering data allows analysts to retrieve **only the records relevant to their analysis**.

---

# Next Lesson

Next we will continue Module 12 with:

# Lesson 5 — Sorting Data with ORDER BY

You will learn:

• how SQL sorts query results  
• ascending vs descending order  
• sorting multiple columns  
• how analysts organize results for reporting.
