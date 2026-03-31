# Module 3 — Data Analysis with Pandas

# Lesson 5 — Filtering Rows

---

# Lesson Objective

By the end of this lesson learners will understand:

• how to filter rows in a DataFrame  
• how to apply conditional filtering  
• how to filter using multiple conditions  
• how Pandas filtering compares to SQL `WHERE` statements  

Filtering rows is one of the **most important operations in data analysis**, because analysts often need to isolate specific records from large datasets.

---

# Overview

Datasets often contain **many rows**, but analysts frequently need to view only certain records.

Example dataset:

| Customer | City | Sales |
|------|------|------|
| Alice | Los Angeles | 120 |
| Bob | Chicago | 200 |
| Maria | New York | 150 |
| James | Chicago | 90 |

Examples of filtering questions:

• Which customers have **Sales greater than 100**?  
• Which customers are located in **Chicago**?  
• Which records meet **multiple conditions**?

Pandas allows filtering rows using **boolean conditions**.

Example:

```python
df[df["Sales"] > 100]
```

This returns only rows where the **Sales column is greater than 100**.

Output:

```text
Customer   City        Sales
Alice      Los Angeles 120
Bob        Chicago     200
Maria      New York    150
```

Filtering datasets allows analysts to focus on **relevant data**.

---

# Key Idea Cards (3 Cards)

## Filtering Uses Boolean Conditions

Filtering works by applying a **True/False condition** to each row.

Example condition:

```python
df["Sales"] > 100
```

This produces a boolean result:

```text
True
True
True
False
```

Rows with `True` remain in the dataset.

---

## Filtering Returns a Subset of the Data

Filtering does not change the original dataset.

Instead, Pandas returns a **new filtered DataFrame**.

Example:

```python
high_sales = df[df["Sales"] > 100]
```

Now `high_sales` contains only rows meeting the condition.

---

## Multiple Conditions Can Be Combined

Pandas allows combining conditions using logical operators.

Example:

```python
df[(df["City"] == "Chicago") & (df["Sales"] > 100)]
```

This returns rows that meet **both conditions**.

---

# Key Concepts

## Boolean Filtering

Boolean filtering selects rows based on conditions.

Example:

```python
df[df["Sales"] > 100]
```

This keeps rows where the condition is `True`.

---

## Comparison Operators

Filtering uses comparison operators.

| Operator | Meaning |
|------|------|
| > | greater than |
| < | less than |
| == | equal |
| >= | greater or equal |
| <= | less or equal |
| != | not equal |

Example:

```python
df[df["Sales"] >= 150]
```

---

## Logical Operators

Multiple conditions can be combined.

| Operator | Meaning |
|------|------|
| & | AND |
| | | OR |
| ~ | NOT |

Example:

```python
df[(df["City"] == "Chicago") & (df["Sales"] > 100)]
```

Important: **conditions must be inside parentheses**.

---

# Decision Flow

Filtering evaluates each row.

Example:

```python
df[df["Sales"] > 100]
```

Execution flow:

```text
Check row 1
Sales > 100 ?
      ↓
True → keep row

Check row 2
Sales > 100 ?
      ↓
True → keep row

Check row 3
Sales > 100 ?
      ↓
True → keep row

Check row 4
Sales > 100 ?
      ↓
False → remove row
```

The final result contains only matching rows.

---

# Code Examples

## Example 1 — Filtering by Sales

```python
high_sales = df[df["Sales"] > 100]

print(high_sales)
```

Output:

```text
Customer   City        Sales
Alice      LA          120
Bob        Chicago     200
Maria      NY          150
```

---

## Example 2 — Filtering by City

```python
chicago_customers = df[df["City"] == "Chicago"]

print(chicago_customers)
```

Output:

```text
Customer   City     Sales
Bob        Chicago  200
James      Chicago  90
```

---

## Example 3 — Multiple Conditions

```python
df[(df["City"] == "Chicago") & (df["Sales"] > 100)]
```

Output:

```text
Customer   City     Sales
Bob        Chicago  200
```

Only rows meeting **both conditions** remain.

---

## Example 4 — OR Conditions

```python
df[(df["City"] == "Chicago") | (df["City"] == "NY")]
```

Output:

```text
Customer   City
Bob        Chicago
Maria      NY
James      Chicago
```

Rows meeting **either condition** remain.

---

# SQL / Excel Comparison

Filtering works similarly across Pandas, SQL, and Excel.

| Concept | Pandas | SQL | Excel |
|------|------|------|------|
| filtering | condition | WHERE | filter |
| multiple conditions | & / | | AND / OR | filter rules |
| subset rows | DataFrame | query result | filtered table |

Example SQL:

```sql
SELECT *
FROM sales
WHERE Sales > 100
```

Equivalent Pandas:

```python
df[df["Sales"] > 100]
```

Excel equivalent:

Apply a **column filter**.

---

# Practice Exercises

## Exercise 1

Tags: Lists, Filtering, WHERE

Filter rows where Sales is greater than 100.

```python
df[df["Sales"] > 100]
```

Observe which rows remain.

---

## Exercise 2

Tags: Lists, Filtering, WHERE

Filter rows where City equals "Chicago".

```python
df[df["City"] == "Chicago"]
```

---

## Exercise 3

Tags: Lists, Filtering, WHERE

Filter rows where Sales is greater than 100 and City is Chicago.

```python
df[(df["City"] == "Chicago") & (df["Sales"] > 100)]
```

---

# Common Mistakes

## Forgetting Parentheses Around Conditions

Incorrect:

```python
df[df["City"] == "Chicago" & df["Sales"] > 100]
```

Correct:

```python
df[(df["City"] == "Chicago") & (df["Sales"] > 100)]
```

---

## Using AND Instead of &

Incorrect:

```python
df[(df["Sales"] > 100) and (df["City"] == "Chicago")]
```

Correct:

```python
df[(df["Sales"] > 100) & (df["City"] == "Chicago")]
```

---

## Using = Instead of ==

Incorrect:

```python
df[df["City"] = "Chicago"]
```

Correct:

```python
df[df["City"] == "Chicago"]
```

---

# Real-World Use

Filtering datasets is one of the **most common analytics tasks**.

Examples include:

• finding high-value customers  
• isolating records from a specific region  
• identifying outliers  
• validating data quality  

Example analytics workflow:

```python
df = pd.read_csv("sales.csv")

high_value_sales = df[df["Sales"] > 1000]

print(high_value_sales)
```

This extracts only high-value sales records.

---

# Lesson Recap

In this lesson you learned:

• how to filter rows using conditions  
• how boolean filtering works  
• how to combine multiple conditions  
• how filtering compares to SQL WHERE clauses  

Filtering allows analysts to **focus on relevant subsets of data**.

---

# Next Lesson

Next we will learn:

# Lesson 6 — Creating Calculated Columns

You will learn:

• how to create new columns in a dataset  
• how to perform column calculations  
• how to transform existing data  

Calculated columns are commonly used to create **metrics and derived values**.