# Module 19 — Large Scale Data Processing  
## Lesson 13 — Performance Profiling

---

# Lesson Objective

By the end of this lesson you will understand:

- What **performance profiling** is
- How to identify **slow operations in Python workflows**
- How to measure execution time for data processing tasks
- How to optimize code based on performance insights

You will learn how analysts and engineers diagnose **performance bottlenecks when processing large datasets**.

---

# Overview

When working with large datasets, performance problems often appear.

Examples include:

```text id="sxm2gd"
Long processing times
Slow queries
High memory usage
Unresponsive notebooks
```

These problems usually come from **inefficient code or workflows**.

Performance profiling is the process of **measuring how long different parts of a program take to run**.

This allows analysts to identify **bottlenecks**.

A bottleneck is the part of a program that **limits overall performance**.

Example workflow:

```text id="j811pa"
Load dataset
Calculate revenue
Group by region
Write results
```

If the grouping operation takes the most time, it becomes the bottleneck.

Profiling tools help identify exactly where time is spent.

---

# Key Idea Cards

### Card 1 — Profiling Measures Performance

Profiling tools measure how long different parts of a program take to run.

---

### Card 2 — Bottlenecks Limit Performance

The slowest part of a workflow determines the overall runtime.

---

### Card 3 — Optimization Requires Measurement

You should measure performance before attempting optimization.

---

# Key Concepts

## Execution Time

Execution time refers to how long a program or operation takes to run.

Example:

```text id="z04keh"
Load data → 2 seconds
Calculate column → 1 second
Group data → 8 seconds
```

The group operation is the bottleneck.

---

## Profiling

Profiling analyzes the performance of code.

Profiling tools show:

```text id="9kh93y"
Which functions run
How often they run
How long they take
```

This information helps identify inefficient parts of a workflow.

---

## Micro vs Macro Profiling

### Micro Profiling

Measures performance of **small code sections**.

Example:

```text id="092cfd"
Testing one function
```

### Macro Profiling

Measures performance of **entire workflows**.

Example:

```text id="rnpnek"
Full data pipeline
```

Both are useful when optimizing large data systems.

---

# Decision Flow

Use profiling when workflows become slow.

```text id="40qd3i"
Workflow runs quickly
        │
        ▼
No profiling needed
```

If performance issues appear:

```text id="dmpvxm"
Slow runtime
High CPU usage
Memory problems
```

Then:

```text id="atnok0"
Use profiling tools
Identify bottleneck
Optimize slow operations
```

---

# Code Examples

## Example 1 — Measuring Execution Time

Python provides tools to measure runtime.

```python id="yhof7a"
import time

start = time.time()

total = sum(range(1000000))

end = time.time()

print("Execution time:", end - start)
```

This measures how long the calculation took.

---

## Example 2 — Timing Data Processing

Measure processing time for a dataset.

```python id="krkp6v"
import pandas as pd
import time

start = time.time()

df = pd.read_csv("sales_data.csv")

result = df.groupby("region")["revenue"].sum()

end = time.time()

print("Execution time:", end - start)
```

This reveals how long the operation takes.

---

## Example 3 — Using Jupyter Timing Tools

In Jupyter notebooks, timing can be measured using special commands.

```python id="ri6ebr"
%%time

df.groupby("region")["revenue"].sum()
```

This displays execution time for the cell.

---

## Example 4 — Comparing Tools

Profiling allows comparison between different approaches.

Example:

```python id="fx0xuk"
import pandas as pd
import polars as pl
```

Compare Pandas vs Polars performance.

This helps determine which tool performs better for a specific task.

---

# SQL / Excel Comparison

Understanding performance profiling becomes easier when comparing tools.

---

## Excel

Excel provides limited performance insight.

Users often detect slow performance through:

```text id="p0tkdp"
Slow recalculation
Unresponsive spreadsheets
```

However, Excel provides limited profiling capabilities.

---

## SQL Databases

SQL engines often provide execution plans.

Example:

```sql id="nfqm9l"
EXPLAIN SELECT SUM(revenue)
FROM sales;
```

Execution plans show how queries are processed.

---

## Python

Python profiling tools provide insights into code performance.

Example workflow:

```text id="2uand0"
Measure execution time
Identify slow functions
Optimize slow operations
```

This approach helps improve performance for large datasets.

---

# Practice Exercises

## Exercise 1 — Measure Runtime

Tags: range(), Arithmetic, Performance Profiling, Performance

Write code that measures the runtime of a calculation.

Example:

```python id="k130ic"
sum(range(1000000))
```

Record the execution time.

---

## Exercise 2 — Profile a Data Operation

Tags: File I/O, Performance, Lists, groupby()

Measure the runtime of a Pandas groupby operation.

Example:

```python id="fmd7bs"
df.groupby("region")["revenue"].sum()
```

---

## Exercise 3 — Compare Tools

Tags: Loops, Databases, Polars, DuckDB

Measure execution time for the same operation using:

```text id="wlzwiv"
Pandas
Polars
DuckDB
```

Compare results.

---

# Common Mistakes

## Mistake 1 — Optimizing Without Measurement

Always measure performance before optimizing code.

---

## Mistake 2 — Ignoring Data Size

Small datasets may not reveal performance problems.

Large datasets often expose inefficiencies.

---

## Mistake 3 — Over-Optimizing

Some optimizations add unnecessary complexity.

Focus on improving the biggest bottlenecks.

---

# Real-World Use

Performance profiling is widely used in analytics and data engineering.

Examples include:

---

## Data Pipelines

Engineers measure pipeline stages to identify slow tasks.

---

## Machine Learning

Profiling helps optimize training pipelines.

---

## Financial Systems

Performance analysis ensures large transaction datasets process quickly.

---

## Web Analytics

Profiling improves the performance of large-scale event processing systems.

---

Performance profiling ensures data workflows remain efficient as datasets grow.

---

# Lesson Recap

In this lesson you learned:

- what performance profiling is
- how to measure execution time
- how to identify performance bottlenecks
- how profiling helps optimize large data workflows

Profiling is an essential skill when working with large-scale data systems.

---

# Next Lesson

Module 19 — Lesson 14

**Real Large Data Project**

You will apply the techniques learned in this module to process a **large dataset using modern data tools**.

---

When you're ready, say:

``` id="vfmzqm"
next lesson
```