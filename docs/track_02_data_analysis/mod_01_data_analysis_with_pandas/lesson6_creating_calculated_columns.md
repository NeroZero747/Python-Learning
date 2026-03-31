# Module 3 — Data Analysis with Pandas

# Lesson 6 — Creating Calculated Columns

---

# Lesson Objective

By the end of this lesson learners will understand:

• how to create new columns in a DataFrame  
• how to perform calculations using existing columns  
• how to transform data using column operations  
• how calculated columns are used in analytics workflows  

Calculated columns allow analysts to **derive new information from existing data**, which is one of the most common tasks in data analysis.

---

# Overview

In many datasets, important values must be **calculated from existing columns**.

Example dataset:

| Product | Price | Quantity |
|------|------|------|
| Laptop | 1200 | 2 |
| Phone | 800 | 3 |
| Tablet | 600 | 4 |

Suppose we want to calculate **Total Sales**.

Formula:

```text
Total Sales = Price × Quantity
```

In Pandas, we can create a new column:

```python
df["Total_Sales"] = df["Price"] * df["Quantity"]
```

Result:

| Product | Price | Quantity | Total_Sales |
|------|------|------|------|
| Laptop | 1200 | 2 | 2400 |
| Phone | 800 | 3 | 2400 |
| Tablet | 600 | 4 | 2400 |

Calculated columns are used for:

• financial calculations  
• KPI metrics  
• derived values  
• data transformations  

This capability allows analysts to build **custom metrics directly inside datasets**.

---

# Key Idea Cards (3 Cards)

## New Columns Can Be Created Easily

A new column can be created simply by assigning a value to a column name.

Example:

```python
df["Profit"] = df["Revenue"] - df["Cost"]
```

If the column does not exist, Pandas automatically creates it.

---

## Calculations Operate Across Entire Columns

When performing calculations in Pandas, operations apply to **every row automatically**.

Example:

```python
df["Total"] = df["Price"] * df["Quantity"]
```

Pandas performs the calculation for **each row in the dataset**.

This is called **vectorized computation**.

---

## Calculated Columns Enable Data Transformation

Calculated columns allow analysts to transform datasets.

Examples:

• calculating profit  
• computing tax  
• converting units  
• creating percentage metrics  

These transformations are fundamental in analytics workflows.

---

# Key Concepts

## Column Assignment

A new column is created using assignment syntax.

Example:

```python
df["New_Column"] = values
```

If the column does not exist, Pandas adds it to the DataFrame.

Example:

```python
df["Tax"] = df["Price"] * 0.08
```

---

## Vectorized Operations

Pandas performs operations across entire columns.

Example:

```python
df["Total"] = df["Price"] * df["Quantity"]
```

This calculation is applied to **every row automatically**.

This is much faster than looping through rows.

---

## Transforming Existing Columns

Columns can also be modified.

Example:

```python
df["Price"] = df["Price"] * 1.10
```

This increases all prices by **10%**.

---

# Decision Flow

When creating calculated columns, the process usually follows this pattern:

```text
Load dataset
      ↓
Identify columns needed for calculation
      ↓
Create new column
      ↓
Verify results
```

Example workflow:

```python
df["Total_Sales"] = df["Price"] * df["Quantity"]
```

The calculation automatically applies to every row.

---

# Code Examples

## Example 1 — Creating a New Column

```python
import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet"],
    "Price": [1200, 800, 600],
    "Quantity": [2, 3, 4]
}

df = pd.DataFrame(data)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print(df)
```

Output:

```text
Product  Price  Quantity  Total_Sales
Laptop   1200   2         2400
Phone    800    3         2400
Tablet   600    4         2400
```

---

## Example 2 — Creating a Percentage Column

```python
df["Discount"] = df["Price"] * 0.10

print(df)
```

Output:

```text
Product  Price  Discount
Laptop   1200   120
Phone    800    80
Tablet   600    60
```

---

## Example 3 — Modifying an Existing Column

```python
df["Price"] = df["Price"] * 1.05

print(df)
```

This increases prices by **5%**.

---

## Example 4 — Creating a Boolean Column

```python
df["High_Sale"] = df["Total_Sales"] > 2000

print(df)
```

Output:

```text
Product  Total_Sales  High_Sale
Laptop   2400         True
Phone    2400         True
Tablet   2400         True
```

Boolean columns are often used for **filtering or flagging records**.

---

# SQL / Excel Comparison

Calculated columns exist in SQL and Excel as well.

| Concept | Pandas | SQL | Excel |
|------|------|------|------|
| calculated column | df["C"] = A * B | SELECT A*B | =A1*B1 |
| dataset calculation | vectorized | computed column | drag formula |
| derived metrics | new column | alias | formula column |

Example SQL query:

```sql
SELECT Price * Quantity AS Total_Sales
FROM orders
```

Equivalent Pandas:

```python
df["Total_Sales"] = df["Price"] * df["Quantity"]
```

Excel equivalent:

```text
=A2 * B2
```

---

# Practice Exercises

## Exercise 1

Tags: Lists, DataFrames, Arithmetic

Create a column called **Total**.

```python
df["Total"] = df["Price"] * df["Quantity"]
```

Print the DataFrame.

---

## Exercise 2

Tags: Lists, Arithmetic

Create a column called **Tax**.

```python
df["Tax"] = df["Price"] * 0.08
```

---

## Exercise 3

Tags: Booleans, Lists, Arithmetic

Create a column indicating high sales.

```python
df["High_Sales"] = df["Total_Sales"] > 2000
```

Observe the boolean results.

---

# Common Mistakes

## Misspelling Column Names

Incorrect:

```python
df["total_sales"] = df["Price"] * df["Quantity"]
```

If the column names are incorrect, the calculation fails.

Always check column names using:

```python
df.columns
```

---

## Forgetting That Operations Apply to Entire Columns

Example:

```python
df["Price"] * df["Quantity"]
```

This operation applies to **every row**, not just one value.

---

## Overwriting Important Columns

Example:

```python
df["Price"] = df["Price"] * 0.5
```

This permanently changes the column.

Sometimes it's better to create a **new column**.

---

# Real-World Use

Calculated columns are widely used in analytics.

Examples include:

• calculating revenue  
• calculating profit margins  
• generating performance metrics  
• creating derived features  

Example workflow:

```python
df = pd.read_csv("orders.csv")

df["Total"] = df["Price"] * df["Quantity"]

df["Profit"] = df["Total"] - df["Cost"]
```

These metrics can then be used in dashboards or reports.

---

# Lesson Recap

In this lesson you learned:

• how to create new columns in a DataFrame  
• how column calculations work in Pandas  
• how vectorized operations apply to entire columns  
• how calculated columns generate derived metrics  

Calculated columns allow analysts to **transform datasets and compute important metrics**.

---

# Next Lesson

Next we will learn:

# Lesson 7 — Aggregations (GROUP BY)

You will learn:

• how to group data by categories  
• how to compute summary statistics  
• how Pandas performs operations similar to SQL `GROUP BY`  

Aggregation is essential for **summarizing large datasets into meaningful insights**.