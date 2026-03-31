# Module 18 — Data Pipelines & Orchestration  
## Lesson 5 — Data Validation in Pipelines

---

# Lesson Objective

By the end of this lesson you will understand:

- Why **data validation is critical in pipelines**
- How pipelines detect **invalid or corrupted data**
- Common **data validation rules**
- How to implement **validation checks in Python pipelines**

Data validation ensures that pipelines produce **accurate and trustworthy datasets**.

---

# Overview

Data pipelines move and transform large amounts of data automatically.

However, source data is often messy or incorrect.

Examples of data problems include:

```text
Missing values
Incorrect data types
Duplicate records
Out-of-range values
Invalid IDs
```

If pipelines process bad data without validation, the result may be:

```text
Incorrect dashboards
Faulty analytics
Bad business decisions
```

For this reason, **data validation is a critical stage in most pipelines**.

---

# Where Validation Happens in a Pipeline

Validation usually occurs after data is extracted but before it is loaded into production systems.

Example pipeline:

```text
Extract Data
      ↓
Validate Data
      ↓
Transform Data
      ↓
Load Data
```

This ensures only **high-quality data enters the system**.

---

# Common Validation Checks

Pipelines commonly perform several types of validation checks.

```text
Schema validation
Missing value checks
Range validation
Duplicate detection
Referential integrity checks
```

Each check helps detect different data quality issues.

---

# Schema Validation

Schema validation checks whether the dataset contains the expected columns and data types.

Example schema:

```text
customer_id → integer
transaction_date → date
sales_amount → numeric
```

If the schema changes unexpectedly, the pipeline should detect the issue.

---

# Python Schema Validation Example

Example validation check:

```python
expected_columns = ["customer_id", "transaction_date", "sales_amount"]

for col in expected_columns:
    if col not in df.columns:
        raise Exception(f"Missing column: {col}")
```

This prevents pipelines from processing malformed datasets.

---

# Missing Value Checks

Missing values are common in many datasets.

Example:

```text
customer_id | sales
---------------------
101         | 200
102         | NULL
103         | 150
```

Missing data may indicate:

```text
Data collection issues
Pipeline errors
Incomplete records
```

---

# Python Missing Value Example

Example validation rule:

```python
if df["sales"].isnull().sum() > 0:
    print("Warning: Missing sales values detected")
```

Pipelines may either:

```text
Fill missing values
Remove invalid records
Stop the pipeline
```

---

# Range Validation

Range validation ensures numeric values fall within expected limits.

Example:

```text
age should be between 0 and 120
revenue should not be negative
```

---

# Python Range Validation Example

Example rule:

```python
if (df["sales"] < 0).any():
    raise Exception("Negative sales detected")
```

This prevents invalid values from entering analytics systems.

---

# Duplicate Detection

Duplicate records can cause inaccurate metrics.

Example dataset:

```text
order_id | sales
----------------
1001     | 200
1001     | 200
```

Duplicates may occur due to:

```text
Data ingestion errors
API retries
Pipeline reruns
```

---

# Python Duplicate Detection Example

```python
duplicates = df.duplicated()

if duplicates.any():
    print("Duplicate records detected")
```

Pipelines often remove duplicates before loading.

---

# Referential Integrity Checks

Some datasets reference other tables.

Example:

```text
orders table references customer_id
```

Validation ensures referenced IDs exist.

Example:

```text
orders.customer_id must exist in customers.customer_id
```

These checks prevent broken relationships in databases.

---

# Decision Flow

When validating pipeline data:

```text
Extract data
      ↓
Validate schema
      ↓
Check for missing values
      ↓
Validate numeric ranges
      ↓
Check duplicates
      ↓
Load validated data
```

This ensures the dataset is **clean and reliable**.

---

# Code Example — Pipeline Validation

Example validation step in a pipeline:

```python
if df.empty:
    raise Exception("Dataset is empty")

if df["sales"].isnull().any():
    raise Exception("Missing sales values detected")

if (df["sales"] < 0).any():
    raise Exception("Invalid sales value detected")
```

If any rule fails, the pipeline stops.

---

# SQL / Excel Comparison

Manual validation often occurs in Excel:

```text
Sort columns
Scan for blanks
Check totals
```

Automated pipelines perform these checks programmatically.

Example pipeline:

```text
Raw data
 ↓
Validation checks
 ↓
Clean dataset
```

Automation ensures consistent validation.

---

# Practice Exercises

### Exercise 1

Tags: Missing Data, Aggregations, NULL Handling, CI/CD

Write a validation rule that checks for missing values.

Example:

```python
df.isnull().sum()
```

---

### Exercise 2

Tags: CI/CD, Validation

Write a validation rule that detects duplicate records.

Example:

```python
df.duplicated()
```

---

### Exercise 3

Tags: Lists, CI/CD, Validation

Write a validation rule ensuring values are positive.

Example:

```python
(df["revenue"] >= 0).all()
```

---

# Common Mistakes

### Mistake 1 — Skipping Validation

Skipping validation can allow corrupted data to propagate through systems.

---

### Mistake 2 — Overly Strict Rules

Validation rules should detect errors without blocking valid records.

---

### Mistake 3 — Not Logging Validation Failures

When validation fails, pipelines should log the issue for investigation.

---

# Real-World Use

Data validation is used across many industries.

Examples include:

---

### Financial Systems

```text
Transaction validation
Fraud detection checks
Regulatory compliance rules
```

---

### Marketing Analytics

```text
Campaign metrics validation
Conversion tracking accuracy
Event data integrity
```

---

### Healthcare Systems

```text
Claims validation
Patient data integrity
Provider ID verification
```

Validation ensures critical systems rely on **accurate data**.

---

# Key Idea Cards

### Card 1

Data validation ensures pipelines produce reliable datasets.

---

### Card 2

Common validation checks include schema validation, missing values, and duplicates.

---

### Card 3

Pipelines should detect and handle invalid data automatically.

---

# Lesson Recap

In this lesson you learned:

- why validation is essential in data pipelines  
- common validation checks used in production systems  
- how Python pipelines implement validation rules  
- how validation protects data quality

Validation ensures that pipelines deliver **accurate and trustworthy data**.

---

# Next Lesson

Next you will learn:

**Module 18 — Lesson 6: Logging and Monitoring**

You will learn:

- how pipelines record activity  
- how engineers detect pipeline failures  
- how logging improves pipeline reliability.