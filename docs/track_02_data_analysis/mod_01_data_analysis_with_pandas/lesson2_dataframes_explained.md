# Module 3 — Data Analysis with Pandas

# Lesson 2 — DataFrames Explained

---

# Lesson Objective

By the end of this lesson learners will understand:

• what a Pandas DataFrame is  
• how rows and columns are organized in a DataFrame  
• what the DataFrame index represents  
• how to inspect the structure of a dataset  

This lesson focuses on understanding **how Pandas stores tabular data**, which is the foundation of almost every data analysis task.

---

# Overview

In Pandas, most datasets are stored in a structure called a **DataFrame**.

A DataFrame is a **two-dimensional table of data**, similar to:

• an Excel spreadsheet  
• a SQL table  
• a CSV file  

Example dataset:

| Customer | City | Sales |
|------|------|------|
| Alice | Los Angeles | 120 |
| Bob | Chicago | 200 |
| Maria | New York | 150 |

In Pandas, this dataset would look like:

```text
   Customer       City  Sales
0     Alice  Los Angeles    120
1       Bob      Chicago    200
2     Maria     New York    150
```

This structure has three major components:

• **columns** — labeled data fields  
• **rows** — individual records  
• **index** — the row identifier  

Understanding this structure is essential because **almost all Pandas operations interact with these components**.

---

# Key Idea Cards (3 Cards)

## A DataFrame Is a Table of Data

A DataFrame represents structured data arranged in rows and columns.

Example structure:

```text
Customer   City          Sales
Alice      Los Angeles   120
Bob        Chicago       200
Maria      New York      150
```

This structure allows Pandas to perform operations such as:

• filtering rows  
• selecting columns  
• grouping data  
• joining datasets

---

## Columns Contain Data Fields

Each column represents a **type of information**.

Example dataset:

| Customer | City | Sales |
|------|------|------|

Each column stores values for that field.

Example:

```python
df["Sales"]
```

This selects the **Sales column**.

---

## The Index Identifies Rows

Every DataFrame has an **index**.

The index labels each row.

Example:

```text
Index
0
1
2
```

Indexes help Pandas keep track of rows when data is filtered, sorted, or merged.

---

# Key Concepts

## DataFrame Structure

A DataFrame consists of:

| Component | Description |
|------|------|
| rows | individual records |
| columns | data fields |
| index | row identifiers |

Example DataFrame:

```text
Index  Customer   Sales
0      Alice      120
1      Bob        200
2      Maria      150
```

This structure allows Pandas to perform operations efficiently.

---

## Column Labels

Column labels define the **names of each data field**.

Example:

```python
df.columns
```

Output:

```text
Index(['Customer', 'Sales'], dtype='object')
```

These labels allow easy column selection.

Example:

```python
df["Customer"]
```

---

## Index

The **index** identifies each row.

Example:

```python
df.index
```

Output:

```text
RangeIndex(start=0, stop=3, step=1)
```

Indexes help Pandas track rows during operations like filtering or sorting.

Indexes can also be customized.

Example:

```python
df.set_index("Customer")
```

This sets the Customer column as the index.

---

# Decision Flow

When working with a dataset, analysts usually inspect the structure first.

Typical workflow:

```text
Load dataset
      ↓
Inspect DataFrame structure
      ↓
Check columns
      ↓
Check rows
      ↓
Understand dataset before analysis
```

Example:

```python
df = pd.read_csv("sales.csv")

print(df.head())
```

This shows the first rows of the dataset.

---

# Code Examples

## Example 1 — Creating a DataFrame

```python
import pandas as pd

data = {
    "Customer": ["Alice", "Bob", "Maria"],
    "City": ["LA", "Chicago", "NY"],
    "Sales": [120, 200, 150]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
  Customer     City  Sales
0    Alice       LA    120
1      Bob  Chicago    200
2    Maria       NY    150
```

---

## Example 2 — Viewing DataFrame Columns

```python
print(df.columns)
```

Output:

```text
Index(['Customer', 'City', 'Sales'], dtype='object')
```

This shows all column names.

---

## Example 3 — Viewing DataFrame Index

```python
print(df.index)
```

Output:

```text
RangeIndex(start=0, stop=3, step=1)
```

The index represents row identifiers.

---

## Example 4 — Viewing DataFrame Shape

```python
print(df.shape)
```

Output:

```text
(3, 3)
```

This means:

```text
3 rows
3 columns
```

---

# SQL / Excel Comparison

DataFrame structures are very similar to SQL tables and Excel worksheets.

| Concept | Pandas | SQL | Excel |
|------|------|------|------|
| dataset | DataFrame | table | worksheet |
| column | column | column | column |
| row | row | row | row |
| row identifier | index | primary key | row number |

Example SQL table:

```text
Customer | Sales
Alice    | 120
Bob      | 200
```

Equivalent Pandas structure:

```python
df = pd.DataFrame({
    "Customer": ["Alice", "Bob"],
    "Sales": [120, 200]
})
```

Excel worksheet behaves similarly.

---

# Practice Exercises

## Exercise 1

Tags: print(), Lists, pandas, Imports

Create a DataFrame with three columns.

Example:

```python
import pandas as pd

data = {
    "City": ["LA", "NY", "Chicago"],
    "Population": [4, 8, 2],
    "State": ["CA", "NY", "IL"]
}

df = pd.DataFrame(data)

print(df)
```

Observe the rows and columns.

---

## Exercise 2

Tags: print(), DataFrames

View the columns of the DataFrame.

```python
print(df.columns)
```

---

## Exercise 3

Tags: print(), DataFrames

Check the shape of the dataset.

```python
print(df.shape)
```

Identify the number of rows and columns.

---

# Common Mistakes

## Confusing Index With a Column

The index is not a regular column.

Example:

```python
df.index
```

It represents row labels.

---

## Forgetting to Inspect Dataset Structure

Before performing analysis, always check:

```python
df.head()
df.columns
df.shape
```

This prevents many errors later.

---

## Misinterpreting Data Types

Columns can contain different data types.

Example:

```python
df.dtypes
```

This shows the data type of each column.

---

# Real-World Use

DataFrames are used in almost every Python data workflow.

Examples include:

• analyzing business metrics  
• processing healthcare claims data  
• transforming datasets for dashboards  
• preparing machine learning datasets  

Example workflow:

```python
df = pd.read_csv("claims_data.csv")

print(df.head())
```

This loads and inspects the dataset.

Analysts typically inspect a DataFrame before performing transformations.

---

# Lesson Recap

In this lesson you learned:

• a DataFrame is a table of rows and columns  
• columns represent data fields  
• rows represent records  
• the index identifies rows  
• Pandas provides tools to inspect dataset structure  

Understanding DataFrames is essential because **almost every Pandas operation works with DataFrames**.

---

# Next Lesson

Next we will learn:

# Lesson 3 — Reading Data (CSV / Excel)

You will learn:

• how to load CSV files  
• how to load Excel files  
• how to inspect datasets after loading  

This is one of the **most common tasks in data analysis workflows**.