# Module 3 — Data Analysis with Pandas

# Lesson 4 — Selecting Columns

---

# Lesson Objective

By the end of this lesson learners will understand:

• how to select a single column from a DataFrame  
• how to select multiple columns  
• how to create a subset of a dataset  
• how column selection works in Pandas  

Selecting columns is one of the **most common operations in data analysis**, because analysts rarely work with every column in a dataset.

---

# Overview

Most datasets contain **many columns**, but analysts usually work with only a few.

Example dataset:

| Customer | City | Product | Sales |
|------|------|------|------|
| Alice | Los Angeles | Laptop | 1200 |
| Bob | Chicago | Phone | 800 |
| Maria | New York | Tablet | 600 |

In many situations, you may only want specific columns.

For example:

• analyze only **Sales**  
• view only **Customer and Sales**  
• extract columns for a report  

Pandas makes column selection simple.

Example selecting one column:

```python
df["Sales"]
```

Example selecting multiple columns:

```python
df[["Customer", "Sales"]]
```

Selecting columns allows analysts to **focus only on the data needed for analysis**.

---

# Key Idea Cards (3 Cards)

## Columns Represent Data Fields

Each column in a DataFrame represents a **type of information**.

Example dataset:

```text
Customer | City | Sales
```

Each column stores values for that field.

Example:

```python
df["Sales"]
```

This selects the **Sales column**.

---

## Selecting One Column Returns a Series

When selecting a single column, Pandas returns a **Series**.

Example:

```python
df["Sales"]
```

Output:

```text
0    120
1    200
2    150
```

A Series represents a **single column of data**.

---

## Selecting Multiple Columns Returns a DataFrame

When selecting multiple columns, Pandas returns a **DataFrame**.

Example:

```python
df[["Customer", "Sales"]]
```

Output:

```text
Customer   Sales
Alice      120
Bob        200
Maria      150
```

This creates a **subset of the original dataset**.

---

# Key Concepts

## Selecting a Single Column

To select a column, use the column name inside brackets.

Example:

```python
df["Sales"]
```

This returns a **Series object** containing the column values.

Example output:

```text
0    120
1    200
2    150
Name: Sales
```

This structure behaves similarly to a **list of values**.

---

## Selecting Multiple Columns

To select multiple columns, provide a list of column names.

Example:

```python
df[["Customer", "Sales"]]
```

Output:

```text
Customer   Sales
Alice      120
Bob        200
Maria      150
```

Notice the **double brackets**.

The inner brackets represent the list of column names.

---

## Creating a Subset of a Dataset

Selecting columns creates a **subset DataFrame**.

Example:

```python
sales_data = df[["Customer", "Sales"]]
```

Now the new dataset contains only two columns.

This is useful when:

• preparing data for analysis  
• exporting specific columns  
• creating reports  

---

# Decision Flow

Column selection usually happens early in analysis.

Typical workflow:

```text
Load dataset
      ↓
Inspect columns
      ↓
Select relevant columns
      ↓
Perform analysis
```

Example workflow:

```python
df = pd.read_csv("sales.csv")

sales_data = df[["Customer", "Sales"]]
```

This extracts only the relevant data.

---

# Code Examples

## Example 1 — Selecting One Column

```python
import pandas as pd

data = {
    "Customer": ["Alice", "Bob", "Maria"],
    "City": ["LA", "Chicago", "NY"],
    "Sales": [120, 200, 150]
}

df = pd.DataFrame(data)

print(df["Sales"])
```

Output:

```text
0    120
1    200
2    150
```

This returns a **Series**.

---

## Example 2 — Selecting Multiple Columns

```python
print(df[["Customer", "Sales"]])
```

Output:

```text
Customer   Sales
Alice      120
Bob        200
Maria      150
```

This returns a **DataFrame**.

---

## Example 3 — Storing Selected Columns

```python
sales_data = df[["Customer", "Sales"]]

print(sales_data)
```

Output:

```text
Customer   Sales
Alice      120
Bob        200
Maria      150
```

Now `sales_data` contains only two columns.

---

## Example 4 — Viewing Column Names

Sometimes you need to see all column names.

```python
print(df.columns)
```

Output:

```text
Index(['Customer', 'City', 'Sales'], dtype='object')
```

This helps identify available columns.

---

# SQL / Excel Comparison

Column selection works similarly across Pandas, SQL, and Excel.

| Concept | Pandas | SQL | Excel |
|------|------|------|------|
| select column | df["Sales"] | SELECT Sales | select column |
| select multiple columns | df[["A","B"]] | SELECT A,B | highlight columns |
| dataset subset | new DataFrame | result table | filtered sheet |

Example SQL query:

```sql
SELECT Customer, Sales
FROM customers
```

Equivalent Pandas command:

```python
df[["Customer", "Sales"]]
```

Excel equivalent:

Select only the relevant columns.

---

# Practice Exercises

## Exercise 1

Tags: print(), Lists, SELECT, HTTP Methods

Select a single column.

```python
print(df["City"])
```

Observe the output.

---

## Exercise 2

Tags: print(), Lists, Tuples, SELECT

Select two columns.

```python
print(df[["Customer", "City"]])
```

---

## Exercise 3

Tags: print(), Lists, DataFrames, SELECT

Create a new DataFrame containing only **Sales**.

```python
sales_data = df[["Sales"]]

print(sales_data)
```

---

# Common Mistakes

## Using Single Brackets for Multiple Columns

Incorrect:

```python
df["Customer", "Sales"]
```

Correct:

```python
df[["Customer", "Sales"]]
```

Multiple columns require **double brackets**.

---

## Misspelling Column Names

Incorrect:

```python
df["sale"]
```

Correct:

```python
df["Sales"]
```

Column names must match exactly.

---

## Forgetting That Column Names Are Case Sensitive

Incorrect:

```python
df["sales"]
```

Correct:

```python
df["Sales"]
```

Python distinguishes uppercase and lowercase.

---

# Real-World Use

Column selection is extremely common in analytics.

Examples include:

• extracting metrics columns  
• preparing data for dashboards  
• exporting specific fields  
• reducing dataset size  

Example analytics workflow:

```python
df = pd.read_csv("sales.csv")

metrics = df[["Customer", "Sales"]]

print(metrics.head())
```

This selects only the columns needed for analysis.

---

# Lesson Recap

In this lesson you learned:

• how to select a single column  
• how to select multiple columns  
• how to create subset datasets  
• the difference between Series and DataFrames  

Column selection is one of the **most frequently used Pandas operations**.

---

# Next Lesson

Next we will learn:

# Lesson 5 — Filtering Rows

You will learn:

• how to filter datasets using conditions  
• how to apply multiple conditions  
• how filtering works in Pandas  

Filtering rows is equivalent to a **SQL WHERE clause**, making it one of the most important data analysis operations.