# Module 11 — Python Engineering Handbook

# Lesson 6 — Performance Checklist

---

# Lesson Objective

By the end of this lesson learners will understand:

• how to identify **performance bottlenecks** in Python programs  
• common causes of slow Python code  
• techniques for optimizing data processing  
• a practical **performance checklist** developers use before deploying applications  

Performance optimization ensures that Python applications run **efficiently and scale properly** when processing large datasets or handling many users.

---

# Overview

In small scripts, performance is usually not a major concern.

However, in real-world systems Python programs may need to process:

```text
Millions of records
Large datasets
High-frequency API calls
Real-time analytics
```

Poorly optimized code can slow down systems significantly.

Example inefficient code:

```python
result = []

for value in data:
    result.append(value * 2)
```

Although this works, there may be faster approaches depending on the context.

Professional developers follow **performance best practices** to improve speed and efficiency.

Example optimized approach:

```python
result = [value * 2 for value in data]
```

Performance improvements often come from:

• better algorithms  
• efficient data structures  
• minimizing unnecessary computations  
• using optimized libraries.

---

# Key Idea Cards (3 Cards)

### Performance Problems Often Come From Algorithms

The biggest performance improvements usually come from better algorithms.

Example:

```text
O(n²) algorithm
↓
Replace with O(n)
```

Choosing efficient algorithms dramatically improves performance.

---

### Built-In Libraries Are Highly Optimized

Many Python libraries are written in optimized C code.

Examples include:

```text
NumPy
Pandas
Polars
```

Using optimized libraries can dramatically improve performance.

---

### Measure Performance Before Optimizing

Developers should measure performance before attempting optimization.

Example tools:

```text
time module
cProfile
line_profiler
```

Profiling helps identify real bottlenecks.

---

# Key Concepts

## Time Complexity

Time complexity describes how algorithm speed changes as input size increases.

Example complexity types:

| Complexity | Description |
|------|------|
| O(1) | constant time |
| O(n) | linear time |
| O(n²) | quadratic time |

Efficient algorithms scale better with large datasets.

---

## Memory Usage

Large datasets may consume significant memory.

Example problem:

```python
data = load_large_dataset()
```

If the dataset is very large, it may exceed system memory.

Solutions include:

• streaming data  
• processing in chunks  
• using efficient file formats.

---

## Vectorized Operations

Vectorized operations process entire datasets at once instead of using loops.

Example using pandas:

```python
df["total"] = df["price"] * df["quantity"]
```

Vectorized operations are often much faster than loops.

---

# Decision Flow

Developers usually approach performance optimization using the following process:

```text
Code runs slowly
      ↓
Profile application
      ↓
Identify bottleneck
      ↓
Optimize algorithm or data structure
      ↓
Test performance improvement
```

Optimization should focus on **real bottlenecks**, not assumptions.

---

# Code Examples

### Example 1 — Inefficient Loop

```python
result = []

for number in numbers:
    result.append(number * 2)
```

This approach may be slower than alternatives.

---

### Example 2 — List Comprehension

```python
result = [number * 2 for number in numbers]
```

List comprehensions are often faster and more readable.

---

### Example 3 — Measuring Execution Time

```python
import time

start = time.time()

process_data()

end = time.time()

print("Execution time:", end - start)
```

This measures how long a function takes to run.

---

### Example 4 — Using cProfile

```python
import cProfile

cProfile.run("process_data()")
```

Profiling tools help identify slow sections of code.

---

# SQL / Excel Comparison

Performance optimization also exists in other data tools.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| performance tuning | algorithm optimization | query optimization | formula optimization |
| indexing | data structures | database indexes | lookup tables |
| profiling | performance profiling tools | query execution plans | workbook analysis |

Example SQL optimization:

```sql
CREATE INDEX idx_customer_id
ON customers(customer_id);
```

Indexes significantly improve query performance.

---

# Practice Exercises

### Exercise 1

Tags: Lists, List Comprehensions, Performance

Rewrite a loop using a list comprehension.

Example:

```python
numbers = [1, 2, 3, 4]
```

Double each value.

---

### Exercise 2

Tags: Performance, Data Engineering

Measure execution time for a Python function.

Use the `time` module.

---

### Exercise 3

Tags: Scripts, Performance Profiling, Performance

Run `cProfile` on a script to identify slow functions.

---

### Exercise 4

Tags: Loops, Scripts, Arithmetic, Performance

Identify potential performance improvements in a data processing script.

Look for:

```text
nested loops
repeated calculations
inefficient data structures
```

---

# Common Mistakes

### Premature Optimization

Developers sometimes optimize code before measuring performance.

Always profile first.

---

### Ignoring Algorithm Efficiency

Small code improvements cannot compensate for inefficient algorithms.

Choosing the right algorithm is critical.

---

### Processing Large Data in Memory

Large datasets may cause memory issues.

Consider processing data in chunks.

---

# Real-World Use

Performance optimization is essential in large data systems.

Example data pipeline:

```text
Extract large dataset
        ↓
Transform millions of rows
        ↓
Load results into database
```

Optimized pipelines allow organizations to process data efficiently.

Performance techniques are used in:

• data engineering pipelines  
• analytics platforms  
• machine learning systems  
• high-traffic web services.

---

# Performance Checklist

Before deploying a Python application, developers often review a performance checklist.

Example checklist:

```text
Profile application
Use efficient algorithms
Avoid unnecessary loops
Use vectorized operations
Limit memory usage
Cache repeated computations
```

Following a checklist helps ensure applications run efficiently.

---

# Lesson Recap

In this lesson you learned:

• how to identify performance bottlenecks  
• how algorithms affect performance  
• how to measure execution time  
• techniques for optimizing Python applications.

Performance optimization ensures Python systems remain **efficient, scalable, and reliable**.

---

# Next Lesson

Next we will complete Module 11 with:

# Lesson 7 — SQL-to-Python Cheat Sheet

You will learn:

• how common SQL operations translate into Python code  
• how pandas replicates SQL queries  
• how analysts can transition from SQL to Python  
• quick reference patterns for common data operations.
