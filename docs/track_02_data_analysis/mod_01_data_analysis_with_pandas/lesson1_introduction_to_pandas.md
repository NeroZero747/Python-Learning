# Module 3 — Data Analysis with Pandas

# Lesson 1 — Introduction to Pandas

---

# Lesson Objective

By the end of this lesson learners will understand:

• what the Pandas library is  
• why Pandas is widely used for data analysis  
• how Pandas fits into the Python data ecosystem  
• how Pandas compares to tools like SQL and Excel  

This lesson introduces **the core library used for data analysis in Python**.

---

# Overview

In previous modules, you learned how Python handles:

• variables  
• lists and dictionaries  
• loops and conditions  
• functions  

These tools allow Python programs to process data.

However, working with real datasets often requires a more structured approach. Data analysts frequently work with datasets that look like this:

| Customer | City | Sales |
|------|------|------|
| Alice | Los Angeles | 120 |
| Bob | Chicago | 200 |
| Maria | New York | 150 |

This structure contains **rows and columns**, similar to:

• Excel spreadsheets  
• SQL database tables  

The Python library that makes working with this type of data easy is **Pandas**.

Pandas is a powerful data analysis library that provides tools for:

• reading datasets  
• filtering data  
• performing calculations  
• grouping data  
• joining datasets  
• exporting results  

Pandas introduces an object called a **DataFrame**, which represents a structured table of data.

Example Pandas program:

```python
import pandas as pd

data = {
    "Customer": ["Alice", "Bob", "Maria"],
    "Sales": [120, 200, 150]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
  Customer  Sales
0   Alice    120
1     Bob    200
2   Maria    150
```

This table-like structure is the **foundation of most Python data analysis workflows**.

---

# Key Idea Cards (3 Cards)

## Pandas Is a Data Analysis Library

Pandas is a Python library designed for working with **structured data**.

It provides tools for:

• loading datasets  
• manipulating tables  
• analyzing data  
• exporting results  

It is one of the **most widely used libraries in data science and analytics**.

---

## DataFrames Represent Tables of Data

The primary object used in Pandas is the **DataFrame**.

A DataFrame represents a dataset with rows and columns.

Example structure:

```text
Customer   Sales
Alice      120
Bob        200
Maria      150
```

This structure is similar to:

• Excel worksheets  
• SQL tables  

---

## Pandas Is Built on Top of NumPy

Pandas uses another library called **NumPy** internally.

NumPy provides high-performance numeric operations.

Pandas builds on top of NumPy to add features for:

• labeled columns  
• row indexing  
• data manipulation  

This combination makes Pandas both **powerful and efficient**.

---

# Key Concepts

## Pandas Library

Pandas is a Python library used for **data manipulation and analysis**.

To use Pandas in Python, we import the library:

```python
import pandas as pd
```

The alias `pd` is the standard convention used by Python developers.

Once imported, Pandas provides many functions for working with data.

---

## DataFrame

A **DataFrame** is the central data structure in Pandas.

A DataFrame contains:

• rows  
• columns  
• labeled column names  

Example DataFrame:

```text
Index  Name   Age
0      Alice   30
1      Bob     28
2      Maria   35
```

This structure is similar to a **table in a relational database**.

---

## Series

A **Series** represents a single column of data.

Example:

```python
import pandas as pd

ages = pd.Series([30, 28, 35])

print(ages)
```

Output:

```text
0    30
1    28
2    35
```

A DataFrame is essentially **multiple Series combined together**.

---

# Decision Flow

When analyzing data with Pandas, workflows usually follow this pattern:

```text
Load dataset
      ↓
Inspect dataset structure
      ↓
Select relevant columns
      ↓
Filter rows
      ↓
Perform calculations
      ↓
Export results
```

Example workflow in Python:

```python
import pandas as pd

df = pd.read_csv("sales.csv")

print(df.head())
```

This loads the dataset and shows the first rows.

---

# Code Examples

## Example 1 — Creating a DataFrame

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Maria"],
    "Sales": [120, 200, 150]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
    Name  Sales
0  Alice    120
1    Bob    200
2  Maria    150
```

Pandas automatically formats the data into a table.

---

## Example 2 — Viewing Dataset Structure

The `head()` function shows the first rows of a dataset.

```python
print(df.head())
```

Output:

```text
    Name  Sales
0  Alice    120
1    Bob    200
2  Maria    150
```

This is commonly used to inspect datasets.

---

## Example 3 — Selecting a Column

```python
print(df["Sales"])
```

Output:

```text
0    120
1    200
2    150
Name: Sales, dtype: int64
```

Selecting a column returns a **Series object**.

---

# SQL / Excel Comparison

Pandas concepts map closely to SQL and Excel concepts.

| Concept | Pandas | SQL | Excel |
|------|------|------|------|
| dataset | DataFrame | table | worksheet |
| column | Series | column | column |
| row | row | row | row |
| filtering | condition | WHERE | filter |
| grouping | groupby() | GROUP BY | pivot table |

Example SQL query:

```sql
SELECT name, sales
FROM customers
WHERE sales > 100
```

Equivalent Pandas concept:

```python
df[df["Sales"] > 100]
```

Excel equivalent:

Apply a **filter** to the Sales column.

---

# Practice Exercises

## Exercise 1

Tags: print(), Lists, pandas, Imports

Create a simple DataFrame.

```python
import pandas as pd

data = {
    "City": ["LA", "NY", "Chicago"],
    "Population": [4, 8, 2]
}

df = pd.DataFrame(data)

print(df)
```

Observe the table structure.

---

## Exercise 2

Tags: print(), Lists, DataFrames, SELECT

Select a column from the DataFrame.

```python
print(df["City"])
```

Observe how Pandas returns a **Series**.

---

## Exercise 3

Tags: print(), pandas

Display the first rows of a dataset.

```python
print(df.head())
```

This command is commonly used when exploring data.

---

# Common Mistakes

## Forgetting to Import Pandas

Incorrect:

```python
df = pd.DataFrame(data)
```

Error occurs because Pandas is not imported.

Correct:

```python
import pandas as pd
```

---

## Misspelling the Pandas Alias

Incorrect:

```python
import pandas as pandas
```

The common convention is:

```python
import pandas as pd
```

This keeps code concise.

---

## Treating a DataFrame Like a List

Beginners sometimes try to use list syntax.

Incorrect:

```python
df[0]
```

Correct:

```python
df["column_name"]
```

DataFrames use **column labels**, not list indexes.

---

# Real-World Use

Pandas is used in many real-world workflows.

Examples include:

• analyzing business metrics  
• cleaning datasets  
• preparing data for machine learning  
• building automated reports  
• transforming data pipelines  

Example analytics workflow:

```python
import pandas as pd

df = pd.read_csv("sales.csv")

high_sales = df[df["Sales"] > 100]

print(high_sales)
```

This program filters a dataset to show only high-sales records.

---

# Lesson Recap

In this lesson you learned:

• Pandas is the primary Python library for data analysis  
• Pandas introduces the DataFrame structure  
• DataFrames represent tables of rows and columns  
• Pandas workflows often resemble SQL and Excel operations  

Pandas is the **foundation of Python-based analytics workflows**.

---

# Next Lesson

Next we will learn:

# Lesson 2 — DataFrames Explained

You will learn:

• how DataFrames store rows and columns  
• how indexes work  
• how to inspect dataset structure  

Understanding DataFrames is essential because **almost all Pandas operations operate on DataFrames**.