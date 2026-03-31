# Module 3 — Data Analysis with Pandas

# Lesson 8 — Joining Data (Merge)

---

# Lesson Objective

By the end of this lesson learners will understand:

• how to combine multiple datasets using Pandas  
• how the `merge()` function works  
• different types of joins (inner, left, right)  
• how Pandas joins compare to SQL `JOIN` statements  

Joining datasets allows analysts to **combine information from multiple tables**, which is essential in real-world data workflows.

---

# Overview

In many data environments, information is stored across **multiple datasets**.

Example:

**Customer Table**

| Customer_ID | Name |
|------|------|
| 1 | Alice |
| 2 | Bob |
| 3 | Maria |

**Sales Table**

| Customer_ID | Sales |
|------|------|
| 1 | 120 |
| 2 | 200 |
| 3 | 150 |

To analyze this data, we often need to **combine these tables**.

Example result:

| Customer_ID | Name | Sales |
|------|------|------|
| 1 | Alice | 120 |
| 2 | Bob | 200 |
| 3 | Maria | 150 |

In Pandas, we combine datasets using the **`merge()` function**.

Example:

```python
pd.merge(customers, sales, on="Customer_ID")
```

This merges both datasets using the **Customer_ID column**.

Joining data is essential for:

• combining lookup tables  
• enriching datasets  
• integrating multiple data sources  

---

# Key Idea Cards (3 Cards)

## Merging Combines Two Datasets

Merging combines rows from two DataFrames based on a **common column**.

Example:

```python
pd.merge(df1, df2, on="Customer_ID")
```

The `on` parameter specifies the column used to match rows.

---

## Joins Match Rows Across Tables

During a merge, Pandas matches rows where values in the join column are equal.

Example:

```text
Customer_ID = 1
```

Rows with the same value are combined.

---

## Pandas Merge Works Like SQL JOIN

The merge operation behaves very similarly to SQL joins.

Example SQL:

```sql
SELECT *
FROM customers
JOIN sales
ON customers.Customer_ID = sales.Customer_ID
```

Equivalent Pandas:

```python
pd.merge(customers, sales, on="Customer_ID")
```

---

# Key Concepts

## merge()

The `merge()` function combines two DataFrames.

Example:

```python
pd.merge(df1, df2, on="column_name")
```

Parameters:

| Parameter | Purpose |
|------|------|
| df1 | first DataFrame |
| df2 | second DataFrame |
| on | column used for matching |

Example:

```python
pd.merge(customers, sales, on="Customer_ID")
```

---

## Inner Join

An **inner join** keeps only rows that exist in both tables.

Example:

```python
pd.merge(df1, df2, on="Customer_ID", how="inner")
```

Result includes only matching records.

---

## Left Join

A **left join** keeps all rows from the first table.

Example:

```python
pd.merge(df1, df2, on="Customer_ID", how="left")
```

If a match is missing in the second table, values become **NaN**.

---

## Right Join

A **right join** keeps all rows from the second table.

Example:

```python
pd.merge(df1, df2, on="Customer_ID", how="right")
```

---

# Decision Flow

Joining datasets follows this process:

```text
Load dataset A
      ↓
Load dataset B
      ↓
Identify common column
      ↓
Merge datasets
      ↓
Analyze combined data
```

Example workflow:

```python
merged_df = pd.merge(customers, sales, on="Customer_ID")
```

This creates a combined dataset.

---

# Code Examples

## Example 1 — Basic Merge

```python
import pandas as pd

customers = pd.DataFrame({
    "Customer_ID": [1,2,3],
    "Name": ["Alice","Bob","Maria"]
})

sales = pd.DataFrame({
    "Customer_ID": [1,2,3],
    "Sales": [120,200,150]
})

merged = pd.merge(customers, sales, on="Customer_ID")

print(merged)
```

Output:

```text
Customer_ID  Name   Sales
1            Alice  120
2            Bob    200
3            Maria  150
```

---

## Example 2 — Left Join

```python
pd.merge(customers, sales, on="Customer_ID", how="left")
```

If a record is missing in the second dataset, it appears as **NaN**.

---

## Example 3 — Right Join

```python
pd.merge(customers, sales, on="Customer_ID", how="right")
```

All rows from the second dataset remain.

---

## Example 4 — Multiple Columns

Merges can also use multiple columns.

Example:

```python
pd.merge(df1, df2, on=["Customer_ID", "City"])
```

Both columns must match.

---

# SQL / Excel Comparison

Joining datasets is similar across Pandas, SQL, and Excel.

| Concept | Pandas | SQL | Excel |
|------|------|------|------|
| join datasets | merge() | JOIN | VLOOKUP/XLOOKUP |
| join key | on= | ON | lookup column |
| inner join | how="inner" | INNER JOIN | exact match |
| left join | how="left" | LEFT JOIN | lookup retaining left table |

Example SQL query:

```sql
SELECT *
FROM customers
INNER JOIN sales
ON customers.Customer_ID = sales.Customer_ID
```

Equivalent Pandas:

```python
pd.merge(customers, sales, on="Customer_ID")
```

Excel equivalent:

```text
VLOOKUP(Customer_ID, table, column)
```

---

# Practice Exercises

## Exercise 1

Tags: Lists, Tuples, DataFrames, Merging Data

Create two datasets.

```python
customers = pd.DataFrame({
    "Customer_ID":[1,2,3],
    "Name":["Alice","Bob","Maria"]
})

sales = pd.DataFrame({
    "Customer_ID":[1,2,3],
    "Sales":[120,200,150]
})
```

Merge them.

```python
pd.merge(customers, sales, on="Customer_ID")
```

---

## Exercise 2

Tags: Tuples, Merging Data, JOIN

Perform a left join.

```python
pd.merge(customers, sales, on="Customer_ID", how="left")
```

---

## Exercise 3

Tags: pandas, Data Analysis

Add a new customer to the first dataset and observe the merge results.

---

# Common Mistakes

## Using Incorrect Join Column

Incorrect:

```python
pd.merge(df1, df2, on="customer")
```

If the column name does not match, the merge fails.

Always check:

```python
df.columns
```

---

## Forgetting the Join Type

Example:

```python
pd.merge(df1, df2, on="Customer_ID")
```

Default join type is **inner join**.

This may remove unmatched rows.

---

## Duplicate Rows After Merge

If the join column contains duplicates, the merge may produce multiple matches.

Example:

```text
Customer_ID appears multiple times
```

This can increase the number of rows.

---

# Real-World Use

Merging datasets is extremely common in analytics.

Examples include:

• joining sales data with product tables  
• linking customer data with transaction data  
• combining healthcare claims with provider information  
• integrating lookup tables  

Example workflow:

```python
claims = pd.read_csv("claims.csv")
providers = pd.read_csv("providers.csv")

merged_data = pd.merge(claims, providers, on="Provider_ID")
```

This enriches claims data with provider details.

---

# Lesson Recap

In this lesson you learned:

• how to combine datasets using `merge()`  
• how join keys match rows between tables  
• how inner and left joins work  
• how Pandas merges compare to SQL joins  

Merging allows analysts to **combine information from multiple datasets into a single view**.

---

# Next Lesson

Next we will learn:

# Lesson 9 — Handling Missing Data

You will learn:

• how to detect missing values  
• how to remove missing data  
• how to fill missing values  

Handling missing data is critical because **real-world datasets almost always contain incomplete records**.