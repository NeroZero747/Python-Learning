# Module 18 — Data Pipelines & Orchestration  
## Lesson 3 — Pipeline Design Patterns

---

# Lesson Objective

By the end of this lesson you will understand:

- What **pipeline design patterns** are  
- The difference between **batch pipelines and streaming pipelines**  
- Common pipeline architectures used in real systems  
- How to design pipelines that are **scalable and maintainable**

Design patterns help engineers build **reliable and reusable data pipelines**.

---

# Overview

A **pipeline design pattern** is a common structure used to organize how data flows through a system.

Instead of building pipelines randomly, engineers use **well-known patterns** that make systems easier to maintain.

Example pipeline:

```text
Data Source
     ↓
Extraction
     ↓
Processing
     ↓
Storage
     ↓
Analytics
```

The structure of these steps determines the **pipeline design pattern**.

---

# Why Pipeline Design Patterns Matter

Good pipeline design makes systems:

```text
Reliable
Scalable
Maintainable
Easier to debug
```

Poorly designed pipelines often become:

```text
Fragile
Hard to modify
Difficult to scale
```

Using design patterns helps avoid these issues.

---

# Common Pipeline Design Patterns

There are several pipeline patterns used in modern data systems.

The most common include:

```text
Batch Pipelines
Streaming Pipelines
Layered Pipelines
Event-Driven Pipelines
```

In this lesson we will focus on the two most common:

```text
Batch pipelines
Streaming pipelines
```

---

# Batch Pipelines

A **batch pipeline** processes data in scheduled groups.

Example:

```text
Data generated during the day
      ↓
Pipeline runs at midnight
      ↓
Data processed in a batch
```

Batch pipelines are extremely common in analytics systems.

Example schedule:

```text
Hourly
Daily
Weekly
```

---

# Batch Pipeline Example

Example batch workflow:

```text
Sales Database
      ↓
Nightly Python Pipeline
      ↓
Data Warehouse
      ↓
Dashboard Update
```

Batch pipelines work well for **reporting and analytics**.

---

# Python Batch Example

Example Python batch pipeline:

```python
import pandas as pd

df = pd.read_csv("sales.csv")

df["revenue"] = df["price"] * df["quantity"]

df.to_sql("sales_data")
```

This script could run **once per day**.

---

# Streaming Pipelines

A **streaming pipeline** processes data continuously as it arrives.

Example:

```text
Incoming transactions
      ↓
Pipeline processes events immediately
      ↓
System updates in real time
```

Streaming pipelines are used when **real-time processing is required**.

---

# Streaming Pipeline Example

Example architecture:

```text
User Activity Events
      ↓
Streaming Pipeline
      ↓
Real-Time Dashboard
```

Streaming systems are common in:

```text
fraud detection
IoT systems
real-time analytics
financial trading systems
```

---

# Visual Comparison

### Batch Pipeline

```text
Data
 ↓
Store
 ↓
Process later
```

### Streaming Pipeline

```text
Data arrives
 ↓
Process immediately
```

---

# Pipeline Layers

Many pipelines are designed using **layers**.

Example layered pipeline:

```text
Raw Data Layer
       ↓
Clean Data Layer
       ↓
Aggregated Data Layer
       ↓
Analytics Layer
```

This layered structure improves organization and data quality.

---

# Layered Pipeline Example

Example structure:

```text
API
 ↓
Raw Table
 ↓
Clean Table
 ↓
Analytics Table
```

Each layer improves the dataset.

---

# Decision Flow

When choosing pipeline design:

```text
Do you need real-time data?
        |
       Yes
        |
Use streaming pipeline
```

Otherwise:

```text
Use batch pipeline
```

Most analytics systems use **batch pipelines**.

---

# Code Example — Layered Pipeline

Example Python structure:

```python
raw_df = pd.read_csv("sales.csv")

clean_df = raw_df.dropna()

clean_df["revenue"] = clean_df["price"] * clean_df["quantity"]
```

Then load the result:

```python
clean_df.to_sql("sales_clean")
```

---

# SQL / Excel Comparison

Excel workflow often resembles a layered pipeline:

```text
Raw spreadsheet
 ↓
Clean spreadsheet
 ↓
Summary table
```

Modern pipelines follow a similar pattern.

---

# Practice Exercises

### Exercise 1

Tags: CI/CD, Data Processing

Identify whether this pipeline is **batch or streaming**.

```text
Sales data collected all day
 ↓
Pipeline runs nightly
```

Answer: **Batch pipeline**

---

### Exercise 2

Tags: CI/CD, Data Processing

Identify whether this pipeline is **batch or streaming**.

```text
Credit card transactions
 ↓
Fraud detection immediately
```

Answer: **Streaming pipeline**

---

### Exercise 3

Tags: Aggregations, CI/CD

Draw a layered pipeline for a dataset you use.

Example:

```text
Raw data
 ↓
Clean data
 ↓
Aggregated data
```

---

# Common Mistakes

### Mistake 1 — Mixing Pipeline Stages

Keep extraction, transformation, and storage **clearly separated**.

---

### Mistake 2 — Overengineering Early

Many pipelines begin as simple scripts.

Complex architectures should evolve gradually.

---

### Mistake 3 — Ignoring Data Layers

Raw data should always be preserved before transformations.

---

# Real-World Use

Pipeline design patterns appear across many industries.

Examples include:

---

### Analytics Systems

```text
Marketing Data
      ↓
Batch Pipeline
      ↓
Data Warehouse
```

---

### Fraud Detection

```text
Transactions
      ↓
Streaming Pipeline
      ↓
Fraud Detection Model
```

---

### Healthcare Systems

```text
Claims Data
      ↓
Batch Pipeline
      ↓
Reporting Systems
```

---

# Key Idea Cards

### Card 1

Pipeline design patterns organize how data flows through a system.

---

### Card 2

Batch pipelines process data on a schedule.

---

### Card 3

Streaming pipelines process data in real time.

---

# Lesson Recap

In this lesson you learned:

- what pipeline design patterns are  
- the difference between **batch and streaming pipelines**  
- how pipelines are structured using layers  
- how engineers design maintainable pipelines

Understanding pipeline design patterns helps you build **scalable and reliable data systems**.

---

# Next Lesson

Next you will learn:

**Module 18 — Lesson 4: Working with Large Data Files**

You will learn:

- how pipelines handle **large datasets**
- strategies for processing **millions of records**
- techniques for efficient file processing.