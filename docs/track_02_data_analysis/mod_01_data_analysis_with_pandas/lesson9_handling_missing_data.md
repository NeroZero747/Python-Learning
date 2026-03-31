# Module 3 — Data Analysis with Pandas

# Lesson 9 — Handling Missing Data

---

# Lesson Objective

By the end of this lesson learners will understand:

• how to detect missing values in a dataset  
• how Pandas represents missing data  
• how to remove rows containing missing values  
• how to fill missing values with replacement data  

Handling missing data is critical because **real-world datasets almost always contain incomplete records**.

---

# Overview

In real-world datasets, it is common for some values to be missing.

Example dataset:

| Customer | City | Sales |
|------|------|------|
| Alice | Los Angeles | 120 |
| Bob | Chicago | NaN |
| Maria | New York | 150 |
| James | NaN | 90 |

Missing data can occur for many reasons:

• incomplete data entry  
• system errors  
• missing survey responses  
• unavailable information  

In Pandas, missing values are represented as:

```text
NaN
```

NaN stands for **Not a Number**, and it represents a missing value.

Before analyzing a dataset, analysts must decide how to handle missing values.

Common approaches include:

• removing rows with missing values  
• replacing missing values with a default value  
• replacing missing values with averages or other statistics  

Proper handling of missing data is essential to ensure **accurate analysis results**.

---

# Key Idea Cards (3 Cards)

## Missing Values Are Represented as NaN

In Pandas, missing values appear as:

```text
NaN
```

Example:

```python
df["Sales"]
```

Output:

```text
120
NaN
150
```

NaN indicates that the value is missing.

---

## Missing Data Must Be Addressed Before Analysis

Missing values can cause problems such as:

• incorrect calculations  
• errors in statistical models  
• inaccurate reporting  

Analysts must either **remove or replace missing values**.

---

## Pandas Provides Tools for Handling Missing Data

Pandas includes built-in functions to manage missing values.

Common functions include:

```python
df.isnull()
df.dropna()
df.fillna()
```

These tools allow flexible handling of incomplete data.

---

# Key Concepts

## Detecting Missing Values

The `isnull()` function detects missing values.

Example:

```python
df.isnull()
```

Output:

```text
Customer   City    Sales
False      False   False
False      False   True
False      False   False
False      True    False
```

True indicates a missing value.

---

## Counting Missing Values

To count missing values:

```python
df.isnull().sum()
```

Example output:

```text
Customer    0
City        1
Sales       1
```

This shows how many missing values exist in each column.

---

## Removing Missing Data

Rows with missing values can be removed using:

```python
df.dropna()
```

Example:

```python
clean_df = df.dropna()
```

Rows containing NaN values are removed.

---

## Filling Missing Values

Missing values can be replaced using `fillna()`.

Example:

```python
df["Sales"] = df["Sales"].fillna(0)
```

This replaces missing sales values with **0**.

Other replacements may include:

• mean values  
• median values  
• default values  

---

# Decision Flow

Handling missing data typically follows this process:

```text
Load dataset
      ↓
Detect missing values
      ↓
Decide strategy
      ↓
Remove or fill missing values
      ↓
Continue analysis
```

Example:

```python
df.isnull().sum()
```

This identifies columns with missing data.

---

# Code Examples

## Example 1 — Detecting Missing Values

```python
import pandas as pd

data = {
    "Customer": ["Alice", "Bob", "Maria", "James"],
    "City": ["LA", "Chicago", "NY", None],
    "Sales": [120, None, 150, 90]
}

df = pd.DataFrame(data)

print(df.isnull())
```

Output:

```text
Customer   City   Sales
False      False  False
False      False  True
False      False  False
False      True   False
```

---

## Example 2 — Counting Missing Values

```python
print(df.isnull().sum())
```

Output:

```text
Customer    0
City        1
Sales       1
```

---

## Example 3 — Removing Missing Rows

```python
clean_df = df.dropna()

print(clean_df)
```

Rows containing missing values are removed.

---

## Example 4 — Filling Missing Values

```python
df["Sales"] = df["Sales"].fillna(0)

print(df)
```

Missing sales values become **0**.

---

# SQL / Excel Comparison

Handling missing values exists in SQL and Excel as well.

| Concept | Pandas | SQL | Excel |
|------|------|------|------|
| missing value | NaN | NULL | blank cell |
| detect missing | isnull() | IS NULL | conditional check |
| replace value | fillna() | COALESCE | IF formula |
| remove rows | dropna() | WHERE NOT NULL | filter rows |

Example SQL:

```sql
SELECT *
FROM sales
WHERE Sales IS NOT NULL
```

Equivalent Pandas:

```python
df.dropna()
```

Excel equivalent:

Filter rows where the cell is **not blank**.

---

# Practice Exercises

## Exercise 1

Tags: Missing Data, NULL Handling

Check for missing values.

```python
df.isnull()
```

---

## Exercise 2

Tags: Missing Data, Aggregations, NULL Handling

Count missing values per column.

```python
df.isnull().sum()
```

---

## Exercise 3

Tags: Lists, Missing Data, Arithmetic

Replace missing sales values with **0**.

```python
df["Sales"] = df["Sales"].fillna(0)
```

---

# Common Mistakes

## Ignoring Missing Data

Some analysts forget to check for missing values.

Always inspect data with:

```python
df.isnull().sum()
```

---

## Dropping Too Much Data

Using:

```python
df.dropna()
```

may remove many rows.

Sometimes filling values is better.

---

## Using Incorrect Replacement Values

Example:

```python
df["Sales"].fillna(0)
```

If zero is not meaningful, it may distort analysis.

Choosing the correct replacement strategy is important.

---

# Real-World Use

Handling missing data is critical in many industries.

Examples include:

• healthcare claims datasets with missing provider IDs  
• survey data with unanswered questions  
• financial reports with incomplete values  
• operational logs with missing timestamps  

Example workflow:

```python
df = pd.read_csv("claims_data.csv")

df["Cost"] = df["Cost"].fillna(df["Cost"].mean())
```

This replaces missing costs with the **average value**.

---

# Lesson Recap

In this lesson you learned:

• how Pandas represents missing values using NaN  
• how to detect missing values with `isnull()`  
• how to remove missing rows with `dropna()`  
• how to replace missing values using `fillna()`  

Handling missing data is essential for **clean and reliable datasets**.

---

# Next Lesson

Next we will learn:

# Lesson 10 — Exporting Data

You will learn:

• how to export DataFrames to CSV  
• how to export data to Excel  
• how analysts share processed data with other tools  

Exporting data allows analysts to **deliver results for reports, dashboards, and downstream systems**.