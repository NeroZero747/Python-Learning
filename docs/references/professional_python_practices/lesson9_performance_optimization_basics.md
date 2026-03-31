# Module 9 — Professional Python Practices

# Lesson 9 — Performance Optimization Basics

---

# Lesson Objective

By the end of this lesson learners will understand:

• why **performance optimization** matters in Python applications  
• how inefficient code can slow systems down  
• common causes of performance bottlenecks  
• techniques for improving Python performance  

As applications grow and datasets become larger, inefficient code can significantly slow down systems. Learning how to identify and optimize performance issues is an important skill for developers working with **data pipelines, analytics systems, and large datasets**.

---

# Overview

When working with small datasets, inefficient code may still perform well.

Example:

```python
numbers = [1,2,3,4,5]

result = []

for n in numbers:
    result.append(n * 2)

print(result)
```

For small lists, this approach works fine.

However, when dealing with **large datasets**, inefficient operations can cause serious problems.

Example data pipeline scenario:

```text
Raw Data
   ↓
Python Processing
   ↓
Database Storage
   ↓
Dashboard Visualization
```

If the processing step is slow, the entire system becomes slow.

Performance problems often occur due to:

• inefficient loops  
• unnecessary computations  
• repeated database queries  
• loading too much data into memory.

Understanding how to write efficient Python code helps developers build **scalable systems**.

---

# Key Idea Cards (3 Cards)

### Performance Problems Often Come from Inefficient Loops

Loops that process large datasets can slow applications.

Example inefficient approach:

```python
for row in data:
    process(row)
```

Vectorized operations or optimized libraries can improve performance.

---

### Efficient Libraries Improve Performance

Libraries like **NumPy** and **Pandas** perform operations using optimized code.

Example:

```python
data["sales"] * 2
```

This operation runs much faster than looping through rows manually.

---

### Profiling Helps Identify Bottlenecks

Before optimizing code, developers should measure where time is being spent.

Example workflow:

```text
Measure performance
       ↓
Identify slow code
       ↓
Optimize bottleneck
```

Optimization should target the most expensive operations.

---

# Key Concepts

## Time Complexity

Time complexity describes how execution time grows as input size increases.

Example:

| Complexity | Example |
|------|------|
| O(1) | constant time |
| O(n) | linear time |
| O(n²) | quadratic time |

Example inefficient loop:

```python
for i in range(n):
    for j in range(n):
        process(i,j)
```

This runs **n² operations**, which becomes slow for large values.

---

## Vectorization

Vectorization means performing operations on entire datasets at once instead of looping.

Example with Pandas:

```python
data["tax"] = data["sales"] * 0.08
```

This performs the operation on the entire column efficiently.

---

## Avoiding Repeated Computations

Repeated operations can waste processing time.

Example inefficient code:

```python
for row in data:
    total = data["sales"].sum()
```

Better approach:

```python
total = data["sales"].sum()

for row in data:
    process(row, total)
```

Compute values once when possible.

---

# Decision Flow

Developers typically follow this process when optimizing performance:

```text
Program is slow
      ↓
Profile the code
      ↓
Identify slow operations
      ↓
Optimize only bottlenecks
```

Optimization should be targeted rather than applied everywhere.

---

# Code Examples

### Example 1 — Inefficient Loop

```python
numbers = []

for i in range(1000000):
    numbers.append(i * 2)
```

This approach may become slow for large datasets.

---

### Example 2 — List Comprehension

```python
numbers = [i * 2 for i in range(1000000)]
```

List comprehensions are typically faster and more concise.

---

### Example 3 — Vectorized Pandas Operation

```python
data["sales_with_tax"] = data["sales"] * 1.08
```

This performs calculations efficiently across an entire column.

---

### Example 4 — Avoid Repeated Database Queries

Inefficient code:

```python
for customer in customers:
    query_database(customer)
```

Better approach:

```python
query_database(customers)
```

Batch operations are often more efficient.

---

# SQL / Excel Comparison

Performance optimization exists in other tools as well.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| inefficient loops | nested loops | row-by-row queries | cell-by-cell formulas |
| optimized operations | vectorization | set-based queries | array formulas |
| performance tuning | profiling | query optimization | workbook performance tuning |

Example SQL optimization:

Inefficient query:

```sql
SELECT *
FROM sales
WHERE YEAR(order_date) = 2024
```

Optimized query:

```sql
SELECT *
FROM sales
WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31'
```

Efficient logic improves performance across many tools.

---

# Practice Exercises

### Exercise 1

Tags: range(), Lists, Loops, Iteration

Rewrite this loop using a list comprehension.

```python
result = []

for i in range(100):
    result.append(i * 3)
```

---

### Exercise 2

Tags: Lists, Arithmetic, Performance

Create a Pandas column using vectorization.

```python
data["discount_price"] = data["price"] * 0.9
```

---

### Exercise 3

Tags: Lists, Loops, Iteration, Aggregations

Identify unnecessary repeated computations in the following code:

```python
for row in data:
    total = data["sales"].sum()
```

Rewrite the code to improve performance.

---

### Exercise 4

Tags: Performance, Best Practices

Experiment with large datasets and compare performance between loops and vectorized operations.

---

# Common Mistakes

### Optimizing Too Early

Premature optimization can complicate code unnecessarily.

Better approach:

```text
Measure first
Optimize later
```

---

### Ignoring Efficient Libraries

Python’s standard loops may be slower than specialized libraries.

Using libraries like:

```text
NumPy
Pandas
Polars
```

can significantly improve performance.

---

### Loading Too Much Data

Loading extremely large datasets into memory can slow applications.

Better approaches include:

```text
data chunking
database queries
distributed processing
```

---

# Real-World Use

Performance optimization is essential for data-intensive systems.

Example analytics pipeline:

```text
Raw Data
    ↓
Python Processing
    ↓
Data Warehouse
    ↓
Dashboard
```

If processing is inefficient, pipelines may take hours instead of minutes.

Performance optimization techniques are commonly used in:

• data engineering pipelines  
• large-scale analytics systems  
• machine learning workflows  
• real-time data processing.

Optimizing bottlenecks ensures that applications scale as datasets grow.

---

# Lesson Recap

In this lesson you learned:

• why performance optimization matters  
• how inefficient loops slow down programs  
• how vectorization improves performance  
• how profiling identifies bottlenecks.

Efficient code helps Python applications **scale to larger datasets and workloads**.

---

# Next Lesson

Next we will learn:

# Lesson 10 — Packaging and Distributing Python Projects

You will learn:

• how Python projects are packaged  
• how applications are distributed  
• how Python packages are shared with other developers  
• how professional teams manage internal libraries.
