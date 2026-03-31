# Module 3 — Data Analysis with Pandas

# Lesson 7 — Aggregations (GROUP BY)

---

# Lesson Objective

By the end of this lesson learners will understand:

• how to group data by categories  
• how to perform aggregations on grouped data  
• how to calculate summary statistics such as totals and averages  
• how Pandas `groupby()` compares to SQL `GROUP BY`  

Aggregation allows analysts to **summarize large datasets into meaningful insights**.

---

# Overview

When analyzing datasets, we often want to **summarize data by categories**.

Example dataset:

| City | Sales |
|------|------|
| LA | 120 |
| Chicago | 200 |
| LA | 150 |
| Chicago | 100 |
| NY | 180 |

Instead of viewing every row individually, we may want to answer questions such as:

• What is the **total sales by city**?  
• What is the **average sales per city**?  
• How many **transactions occurred in each city**?

To answer these questions, we **group the data**.

Example using Pandas:

```python
df.groupby("City")["Sales"].sum()
```

Output:

```text
City
Chicago    300
LA         270
NY         180
```

This summarizes sales **by city**.

Aggregation helps convert **raw data into summarized insights**.

---

# Key Idea Cards (3 Cards)

## Grouping Organizes Data by Categories

Grouping allows Pandas to organize data by a category.

Example:

```python
df.groupby("City")
```

This groups all rows with the same city together.

Once grouped, we can apply calculations to each group.

---

## Aggregations Calculate Summary Values

Aggregations compute summary statistics.

Common aggregations include:

• sum  
• average  
• count  
• minimum  
• maximum  

Example:

```python
df.groupby("City")["Sales"].mean()
```

This calculates the **average sales per city**.

---

## GroupBy Is Similar to SQL GROUP BY

Pandas grouping works similarly to SQL queries.

Example SQL:

```sql
SELECT City, SUM(Sales)
FROM sales
GROUP BY City
```

Equivalent Pandas:

```python
df.groupby("City")["Sales"].sum()
```

Both produce summarized data.

---

# Key Concepts

## groupby()

The `groupby()` function groups rows based on column values.

Example:

```python
df.groupby("City")
```

This creates grouped data based on city.

---

## Aggregation Functions

After grouping data, aggregation functions can be applied.

Common functions include:

| Function | Purpose |
|------|------|
| sum() | total value |
| mean() | average value |
| count() | number of rows |
| min() | smallest value |
| max() | largest value |

Example:

```python
df.groupby("City")["Sales"].sum()
```

---

## Multiple Aggregations

Pandas allows multiple summary calculations.

Example:

```python
df.groupby("City")["Sales"].agg(["sum", "mean", "count"])
```

Output:

```text
City      sum   mean  count
Chicago   300   150     2
LA        270   135     2
NY        180   180     1
```

This produces multiple statistics simultaneously.

---

# Decision Flow

Aggregation typically follows this workflow:

```text
Load dataset
      ↓
Select grouping column
      ↓
Group rows
      ↓
Apply aggregation function
      ↓
Return summarized dataset
```

Example:

```python
df.groupby("City")["Sales"].sum()
```

This groups rows and calculates total sales per city.

---

# Code Examples

## Example 1 — Grouping by City

```python
import pandas as pd

data = {
    "City": ["LA", "Chicago", "LA", "Chicago", "NY"],
    "Sales": [120, 200, 150, 100, 180]
}

df = pd.DataFrame(data)

print(df.groupby("City")["Sales"].sum())
```

Output:

```text
City
Chicago    300
LA         270
NY         180
```

---

## Example 2 — Average Sales

```python
print(df.groupby("City")["Sales"].mean())
```

Output:

```text
City
Chicago    150
LA         135
NY         180
```

This calculates average sales by city.

---

## Example 3 — Counting Records

```python
print(df.groupby("City")["Sales"].count())
```

Output:

```text
City
Chicago    2
LA         2
NY         1
```

This counts the number of rows in each group.

---

## Example 4 — Multiple Aggregations

```python
print(df.groupby("City")["Sales"].agg(["sum", "mean", "count"]))
```

Output:

```text
City      sum  mean  count
Chicago   300  150   2
LA        270  135   2
NY        180  180   1
```

---

# SQL / Excel Comparison

Aggregation works similarly across Pandas, SQL, and Excel.

| Concept | Pandas | SQL | Excel |
|------|------|------|------|
| grouping | groupby() | GROUP BY | pivot table |
| sum | sum() | SUM() | SUM |
| average | mean() | AVG() | AVERAGE |
| count | count() | COUNT() | COUNT |

Example SQL query:

```sql
SELECT City, SUM(Sales)
FROM sales
GROUP BY City
```

Equivalent Pandas:

```python
df.groupby("City")["Sales"].sum()
```

Excel equivalent:

Create a **pivot table grouped by City**.

---

# Practice Exercises

## Exercise 1

Tags: Lists, groupby(), Aggregations, GROUP BY

Calculate total sales by city.

```python
df.groupby("City")["Sales"].sum()
```

---

## Exercise 2

Tags: Lists, groupby(), Aggregations, GROUP BY

Calculate average sales by city.

```python
df.groupby("City")["Sales"].mean()
```

---

## Exercise 3

Tags: Lists, Tuples, groupby(), Aggregations

Calculate multiple summary statistics.

```python
df.groupby("City")["Sales"].agg(["sum", "mean", "count"])
```

Observe the results.

---

# Common Mistakes

## Forgetting the Aggregation Step

Incorrect:

```python
df.groupby("City")
```

This only groups the data but does not calculate anything.

Correct:

```python
df.groupby("City")["Sales"].sum()
```

---

## Grouping Without Selecting a Column

Incorrect:

```python
df.groupby("City").sum()
```

This may produce unexpected results if multiple numeric columns exist.

Better approach:

```python
df.groupby("City")["Sales"].sum()
```

---

## Misinterpreting Aggregation Results

Aggregation returns a **summarized dataset**, not the original rows.

Example:

```python
df.groupby("City")["Sales"].sum()
```

This returns **one row per city**.

---

# Real-World Use

Aggregation is used frequently in data analysis.

Examples include:

• total revenue by region  
• average patient cost by hospital  
• number of customers by segment  
• total claims by provider  

Example workflow:

```python
df = pd.read_csv("sales_data.csv")

sales_summary = df.groupby("City")["Sales"].sum()

print(sales_summary)
```

This produces a **summary table for reporting**.

---

# Lesson Recap

In this lesson you learned:

• how to group data using `groupby()`  
• how to apply aggregation functions  
• how to calculate summary statistics  
• how grouping compares to SQL `GROUP BY`  

Aggregation helps transform **raw data into meaningful summaries**.

---

# Next Lesson

Next we will learn:

# Lesson 8 — Joining Data (Merge)

You will learn:

• how to combine multiple datasets  
• how Pandas performs joins  
• how merges compare to SQL `JOIN` statements  

Joining datasets is essential when **data is stored across multiple tables**.