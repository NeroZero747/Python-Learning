# Module 3 — Data Analysis with Pandas

# Lesson 3 — Reading Data (CSV / Excel)

---

# Lesson Objective

By the end of this lesson learners will understand:

• how to load datasets into Python using Pandas  
• how to read CSV files  
• how to read Excel files  
• how to inspect a dataset after loading it  

This lesson teaches one of the **most common tasks in data analysis: loading data into Python**.

---

# Overview

Before analyzing data, we first need to **load the dataset into Python**.

Most datasets are stored in files such as:

• CSV files  
• Excel spreadsheets  
• database tables  
• JSON files  

The most common file format in data analytics is **CSV (Comma-Separated Values)**.

Example CSV file:

```text
Customer,City,Sales
Alice,Los Angeles,120
Bob,Chicago,200
Maria,New York,150
```

Pandas provides built-in functions to read these files and convert them into **DataFrames**.

Example:

```python
import pandas as pd

df = pd.read_csv("sales.csv")

print(df)
```

Output:

```text
  Customer          City  Sales
0    Alice   Los Angeles    120
1      Bob       Chicago    200
2    Maria      New York    150
```

Once the data is loaded into a DataFrame, we can begin:

• filtering  
• analyzing  
• transforming  
• exporting results  

Loading data correctly is the **first step in every data analysis workflow**.

---

# Key Idea Cards (3 Cards)

## Pandas Can Load Many File Types

Pandas supports many data formats.

Common examples include:

• CSV files  
• Excel spreadsheets  
• JSON files  
• SQL databases  

Each format has its own Pandas function.

Example:

```python
pd.read_csv()
pd.read_excel()
```

---

## CSV Files Are the Most Common Data Format

CSV stands for **Comma-Separated Values**.

Example file:

```text
Customer,Sales
Alice,120
Bob,200
Maria,150
```

CSV files are widely used because they are:

• simple  
• lightweight  
• compatible with many tools  

---

## Data Is Loaded Into a DataFrame

When a dataset is loaded using Pandas, it becomes a **DataFrame**.

Example:

```python
df = pd.read_csv("sales.csv")
```

Now the dataset can be manipulated using Pandas operations.

---

# Key Concepts

## read_csv()

The `read_csv()` function loads a CSV file into a DataFrame.

Example:

```python
import pandas as pd

df = pd.read_csv("sales.csv")
```

This reads the file and converts it into a structured table.

---

## read_excel()

The `read_excel()` function loads Excel files.

Example:

```python
df = pd.read_excel("sales.xlsx")
```

Excel files may contain multiple sheets.

You can specify a sheet name:

```python
df = pd.read_excel("sales.xlsx", sheet_name="Sheet1")
```

---

## Inspecting a Dataset

After loading data, analysts typically inspect the dataset.

Common inspection commands include:

```python
df.head()
df.columns
df.shape
df.info()
```

These commands help understand the dataset before performing analysis.

---

# Decision Flow

Typical data analysis workflow:

```text
Locate dataset file
      ↓
Load file with Pandas
      ↓
Inspect dataset structure
      ↓
Begin data analysis
```

Example workflow:

```python
import pandas as pd

df = pd.read_csv("sales.csv")

print(df.head())
```

This displays the first rows of the dataset.

---

# Code Examples

## Example 1 — Reading a CSV File

```python
import pandas as pd

df = pd.read_csv("sales.csv")

print(df)
```

Output:

```text
  Customer          City  Sales
0    Alice   Los Angeles    120
1      Bob       Chicago    200
2    Maria      New York    150
```

---

## Example 2 — Viewing First Rows

```python
print(df.head())
```

Output:

```text
  Customer          City  Sales
0    Alice   Los Angeles    120
1      Bob       Chicago    200
2    Maria      New York    150
```

`head()` helps inspect datasets quickly.

---

## Example 3 — Viewing Dataset Information

```python
print(df.info())
```

Output:

```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries
Columns: 3
```

This shows:

• number of rows  
• column names  
• data types  

---

## Example 4 — Reading Excel Files

```python
import pandas as pd

df = pd.read_excel("sales.xlsx")

print(df.head())
```

Pandas automatically loads the spreadsheet into a DataFrame.

---

# SQL / Excel Comparison

Loading data in Pandas is similar to retrieving data in SQL or opening a file in Excel.

| Concept | Pandas | SQL | Excel |
|------|------|------|------|
| load data | read_csv() | SELECT | open file |
| dataset | DataFrame | table | worksheet |
| preview rows | head() | LIMIT | first rows |

Example SQL query:

```sql
SELECT *
FROM sales
LIMIT 5
```

Equivalent Pandas command:

```python
df.head()
```

Excel equivalent:

Open the spreadsheet and view the first rows.

---

# Practice Exercises

## Exercise 1

Tags: print(), Context Managers, pandas, Imports

Create a CSV file with this content:

```text
City,Population
LA,4
NY,8
Chicago,2
```

Load it into Python.

```python
import pandas as pd

df = pd.read_csv("cities.csv")

print(df)
```

---

## Exercise 2

Tags: print(), Excel

Display the first rows of the dataset.

```python
print(df.head())
```

---

## Exercise 3

Tags: print(), Excel

Inspect dataset structure.

```python
print(df.info())
```

Observe the number of rows and columns.

---

# Common Mistakes

## Incorrect File Path

Incorrect:

```python
df = pd.read_csv("sales.csv")
```

If the file is not in the working directory, Python cannot find it.

Correct:

```python
df = pd.read_csv("data/sales.csv")
```

Specify the correct path.

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

Always import Pandas first.

---

## Confusing CSV and Excel Functions

Incorrect:

```python
pd.read_excel("sales.csv")
```

Correct:

```python
pd.read_csv("sales.csv")
```

Each file type has its own function.

---

# Real-World Use

Loading data is the first step in most analytics workflows.

Examples include:

• loading sales reports  
• loading healthcare claims datasets  
• loading API exports  
• loading survey data  

Example workflow:

```python
import pandas as pd

df = pd.read_csv("claims_data.csv")

print(df.head())
```

Once the data is loaded, analysts begin:

• filtering records  
• calculating metrics  
• creating reports  

---

# Lesson Recap

In this lesson you learned:

• how to load datasets using Pandas  
• how to read CSV files with `read_csv()`  
• how to read Excel files with `read_excel()`  
• how to inspect datasets after loading them  

Loading data is the **first step in nearly every data analysis project**.

---

# Next Lesson

Next we will learn:

# Lesson 4 — Selecting Columns

You will learn:

• how to select one column from a DataFrame  
• how to select multiple columns  
• how to view subsets of a dataset  

Selecting columns is one of the **most common operations in data analysis**.