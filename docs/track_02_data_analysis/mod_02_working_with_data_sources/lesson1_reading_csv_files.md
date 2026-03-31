# Module 4 — Working with Data Sources

# Lesson 1 — Reading CSV Files

---

# Lesson Objective

By the end of this lesson learners will understand:

• what a CSV file is  
• how to load CSV files using Pandas  
• how to inspect the dataset after loading it  
• how CSV data relates to Excel tables and SQL tables  

CSV files are one of the **most common ways data is stored and shared**, so learning how to read them is an essential skill for analysts.

---

# Overview

Most real-world datasets are stored outside Python in files such as:

• CSV files  
• Excel files  
• databases  
• APIs  

One of the most common formats is **CSV (Comma Separated Values)**.

Example CSV file:

```text
Customer,City,Sales
Alice,Los Angeles,120
Bob,Chicago,200
Maria,New York,150
James,Chicago,90
```

Each row represents a record and each column represents a field.

When loading a CSV file into Pandas, it becomes a **DataFrame**, which allows us to analyze the data.

Example:

```python
import pandas as pd

df = pd.read_csv("sales.csv")

print(df)
```

Output:

```text
Customer   City        Sales
Alice      Los Angeles 120
Bob        Chicago     200
Maria      New York    150
James      Chicago     90
```

Once the file is loaded into a DataFrame, analysts can perform operations such as:

• filtering data  
• calculating metrics  
• aggregating results  
• exporting summaries  

Reading data from files is usually the **first step in a data analysis workflow**.

---

# Key Idea Cards (3 Cards)

## CSV Files Store Tabular Data

CSV files store data using rows and columns separated by commas.

Example:

```text
Customer,City,Sales
Alice,Los Angeles,120
Bob,Chicago,200
```

Each line represents one record.

---

## Pandas Converts CSV Files into DataFrames

When a CSV file is loaded with Pandas, it becomes a DataFrame.

Example:

```python
df = pd.read_csv("sales.csv")
```

The DataFrame structure makes it easy to analyze the dataset.

---

## Reading Data Is Usually the First Step in Analysis

Most analytics workflows follow this pattern:

```text
Load data
Clean data
Analyze data
Export results
```

Reading CSV files is typically the **starting point**.

---

# Key Concepts

## read_csv()

The `read_csv()` function loads a CSV file into a DataFrame.

Example:

```python
df = pd.read_csv("sales.csv")
```

This reads the file and creates a DataFrame.

---

## Viewing the First Rows

Large datasets may contain thousands or millions of rows.

To preview the data:

```python
df.head()
```

Example output:

```text
Customer   City        Sales
Alice      Los Angeles 120
Bob        Chicago     200
Maria      New York    150
James      Chicago     90
```

This displays the first **5 rows**.

---

## Inspecting Dataset Structure

To understand the dataset structure:

```python
df.info()
```

Example output:

```text
Data columns (total 3 columns):
Customer    object
City        object
Sales       int64
```

This shows:

• column names  
• data types  
• number of rows  

---

# Decision Flow

Loading a CSV dataset typically follows this workflow:

```text
Locate CSV file
      ↓
Load file using Pandas
      ↓
Preview dataset
      ↓
Inspect structure
      ↓
Begin analysis
```

Example workflow:

```python
df = pd.read_csv("sales.csv")

df.head()
df.info()
```

This verifies the dataset loaded correctly.

---

# Code Examples

## Example 1 — Loading a CSV File

```python
import pandas as pd

df = pd.read_csv("sales.csv")

print(df)
```

---

## Example 2 — Viewing First Rows

```python
df.head()
```

This helps verify that the dataset loaded correctly.

---

## Example 3 — Checking Dataset Information

```python
df.info()
```

This shows column types and dataset size.

---

## Example 4 — Viewing Column Names

```python
df.columns
```

Output:

```text
Index(['Customer','City','Sales'])
```

---

# SQL / Excel Comparison

Reading data in Pandas is similar to loading data in SQL or opening a file in Excel.

| Concept | Pandas | SQL | Excel |
|------|------|------|------|
| load dataset | read_csv() | SELECT FROM table | open workbook |
| table structure | DataFrame | table | worksheet |
| preview data | head() | SELECT LIMIT | scroll first rows |

Example SQL:

```sql
SELECT *
FROM sales
LIMIT 5
```

Equivalent Pandas:

```python
df.head()
```

Excel equivalent:

Open the CSV file in Excel.

---

# Practice Exercises

## Exercise 1

Tags: read_csv(), CSV, File I/O

Load a CSV file.

```python
df = pd.read_csv("sales.csv")
```

---

## Exercise 2

Tags: File I/O, Data Sources

Display the first rows.

```python
df.head()
```

---

## Exercise 3

Tags: File I/O, Data Sources

Inspect the dataset structure.

```python
df.info()
```

Observe the column types.

---

# Common Mistakes

## Incorrect File Path

Example error:

```python
pd.read_csv("data.csv")
```

If the file does not exist in the working directory, Python will raise an error.

Use the correct path:

```python
pd.read_csv("data/sales.csv")
```

---

## Forgetting to Import Pandas

Incorrect:

```python
df = pd.read_csv("sales.csv")
```

Correct:

```python
import pandas as pd
```

---

## Large Files Causing Memory Issues

Very large CSV files can consume a lot of memory.

In those cases analysts may use:

• chunk processing  
• Parquet files  
• database queries  

---

# Real-World Use

Reading CSV files is extremely common in analytics workflows.

Examples include:

• loading exported reports  
• analyzing transaction logs  
• processing survey responses  
• importing healthcare claim datasets  

Example workflow:

```python
df = pd.read_csv("claims_data.csv")

print(df.head())
```

This loads a healthcare claims dataset for analysis.

---

# Lesson Recap

In this lesson you learned:

• what CSV files are  
• how to load CSV files using Pandas  
• how to inspect datasets after loading them  
• how CSV workflows compare to SQL and Excel  

Reading CSV files is a fundamental skill because most datasets originate from **external files**.

---

# Next Lesson

Next we will learn:

# Lesson 2 — Working with JSON Files

You will learn:

• how JSON data is structured  
• how to load JSON files into Pandas  
• how JSON differs from tabular data  

JSON is widely used for **APIs and modern data systems**.
