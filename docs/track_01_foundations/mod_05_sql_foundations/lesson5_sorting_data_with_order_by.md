# Module 12 — SQL Foundations

# Lesson 5 — Sorting Data with ORDER BY

---

# Lesson Objective

By the end of this lesson learners will understand:

• how the **ORDER BY clause sorts query results**  
• how to sort data in **ascending (ASC)** order  
• how to sort data in **descending (DESC)** order  
• how to sort by **multiple columns**

Sorting data is an important step in analysis because it helps identify patterns such as **top sales, lowest values, newest records, or highest costs**.

---

# Overview

When retrieving data from a database, results are **not always returned in a meaningful order**.

Example table:

| product_id | product_name | price |
|---|---|---|
| 1 | Laptop | 1200 |
| 2 | Phone | 800 |
| 3 | Tablet | 600 |
| 4 | Monitor | 300 |

If we run:

```sql
SELECT *
FROM products;
```

The results may appear in the order the database stores them.

However, analysts often want to sort the results.

Example: sort products by price.

```sql
SELECT *
FROM products
ORDER BY price;
```

Result:

| product_name | price |
|---|---|
| Monitor | 300 |
| Tablet | 600 |
| Phone | 800 |
| Laptop | 1200 |

Sorting helps analysts quickly identify **lowest or highest values**.

---

# Key Idea Cards (3 Cards)

### ORDER BY Sorts Query Results

The ORDER BY clause organizes query results.

Example:

```sql
SELECT *
FROM products
ORDER BY price;
```

This sorts rows by the `price` column.

---

### ASC Means Ascending Order

Ascending order sorts values from **smallest to largest**.

Example:

```sql
ORDER BY price ASC
```

Numbers increase upward.

Text values sort alphabetically.

---

### DESC Means Descending Order

Descending order sorts values from **largest to smallest**.

Example:

```sql
ORDER BY price DESC
```

This is useful when finding:

```text
Top sales
Highest values
Latest records
```

---

# Key Concepts

## Ascending Order

Ascending order sorts data from smallest to largest.

Example:

```sql
SELECT *
FROM products
ORDER BY price ASC;
```

Result:

| price |
|---|
| 300 |
| 600 |
| 800 |
| 1200 |

`ASC` is the **default sorting order**.

---

## Descending Order

Descending order sorts values from largest to smallest.

Example:

```sql
SELECT *
FROM products
ORDER BY price DESC;
```

Result:

| price |
|---|
| 1200 |
| 800 |
| 600 |
| 300 |

This is commonly used when analyzing **top performers**.

---

## Sorting Multiple Columns

SQL allows sorting by multiple columns.

Example:

```sql
SELECT *
FROM customers
ORDER BY city, age;
```

This sorts:

```text
First by city
Then by age within each city
```

Example with mixed sorting:

```sql
SELECT *
FROM customers
ORDER BY city ASC, age DESC;
```

---

# Decision Flow

When organizing query results:

```text
Do results need ordering?
        ↓
Choose column to sort
        ↓
Use ORDER BY
        ↓
Choose ASC or DESC
```

Example:

```text
Need highest sales first
       ↓
ORDER BY sales DESC
```

---

# Code Examples

### Example 1 — Basic Sorting

```sql
SELECT *
FROM products
ORDER BY price;
```

This sorts products by price in ascending order.

---

### Example 2 — Descending Sort

```sql
SELECT *
FROM products
ORDER BY price DESC;
```

This shows the most expensive products first.

---

### Example 3 — Alphabetical Sort

```sql
SELECT *
FROM customers
ORDER BY name;
```

Names will be sorted alphabetically.

---

### Example 4 — Multiple Sorting Columns

```sql
SELECT *
FROM employees
ORDER BY department, salary DESC;
```

This sorts employees by department, then highest salary within each department.

---

# SQL / Excel Comparison

Sorting in SQL works similarly to sorting in Excel.

| SQL | Excel | Python |
|---|---|---|
| ORDER BY | Sort column | df.sort_values() |
| ASC | Smallest to largest | ascending=True |
| DESC | Largest to smallest | ascending=False |

Example Excel sort:

```text
Sort column "Sales"
Largest to Smallest
```

Equivalent SQL query:

```sql
SELECT *
FROM sales
ORDER BY sales DESC;
```

Equivalent Python:

```python
df.sort_values("sales", ascending=False)
```

---

# Practice Exercises

### Exercise 1

Tags: Sorting, ORDER BY

Sort the `products` table by price in ascending order.

---

### Exercise 2

Tags: Sorting, ORDER BY, Streamlit

Sort employees by salary from highest to lowest.

Table:

```text
employees
```

---

### Exercise 3

Tags: Sorting, ORDER BY

Sort customers alphabetically by name.

Table:

```text
customers
```

---

### Exercise 4

Tags: Sorting, ORDER BY

Sort sales records by region and then by revenue descending.

---

# Common Mistakes

### Forgetting ORDER BY Column

Incorrect:

```sql
ORDER BY;
```

Correct:

```sql
ORDER BY price;
```

A column must be specified.

---

### Sorting the Wrong Column

Make sure the column being sorted is appropriate.

Example:

Sorting by `customer_id` may not be meaningful if analyzing sales.

---

### Forgetting DESC for Top Results

If you want highest values first:

```sql
ORDER BY sales DESC
```

Without `DESC`, the lowest values will appear first.

---

# Real-World Use

Sorting is widely used in business reporting and analytics.

Example queries:

```text
Top 10 customers by revenue
Highest claim amounts
Most recent transactions
Products with lowest inventory
```

Example business query:

```sql
SELECT *
FROM sales
ORDER BY revenue DESC;
```

This identifies the highest sales values.

Sorting allows analysts to **quickly interpret data and identify trends**.

---

# Lesson Recap

In this lesson you learned:

• how the ORDER BY clause sorts query results  
• how ascending and descending sorting works  
• how to sort by multiple columns  
• how analysts organize data for reporting

Sorting helps transform raw data into **structured, meaningful results**.

---

# Next Lesson

Next we will continue Module 12 with:

# Lesson 6 — Aggregations (COUNT, SUM, AVG)

You will learn:

• how SQL summarizes data  
• how aggregation functions work  
• how analysts calculate totals and averages  
• how summary statistics support analysis.
