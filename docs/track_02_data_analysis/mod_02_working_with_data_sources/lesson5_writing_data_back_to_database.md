# Module 4 — Working with Data Sources

# Lesson 5 — Writing Data Back to a Database

---

# Lesson Objective

By the end of this lesson learners will understand:

• how to write data from a Pandas DataFrame into a database  
• how to create or replace database tables using Python  
• how database inserts work in data pipelines  
• how writing data compares to SQL insert operations  

Writing data back to a database is important for **data pipelines, reporting tables, and automated workflows**.

---

# Overview

In previous lessons we learned how to **read data from databases**.

However, many workflows also require **writing data back to the database**.

Common examples include:

• saving cleaned datasets  
• storing aggregated results  
• creating reporting tables  
• loading pipeline outputs  

Example analysis result:

| City | Total_Sales |
|------|------|
| Chicago | 300 |
| LA | 270 |
| NY | 180 |

Instead of exporting this as a file, we might store it in a **database table**.

Example using Pandas:

```python
df.to_sql("sales_summary", engine)
```

This creates a table called **sales_summary** in the database.

After writing the data, other systems can access it using SQL.

Example SQL query:

```sql
SELECT *
FROM sales_summary
```

Writing data to databases is an important step in **data engineering pipelines**.

---

# Key Idea Cards (3 Cards)

## DataFrames Can Be Saved to Database Tables

Pandas allows DataFrames to be written directly to database tables.

Example:

```python
df.to_sql("sales_summary", engine)
```

This creates a table containing the DataFrame data.

---

## Writing Data Enables Data Pipelines

Many data pipelines follow this workflow:

```text
Extract data
Transform data
Load results into database
```

This process is called **ETL (Extract, Transform, Load)**.

---

## Databases Store Final Analytical Results

Instead of sending files, many organizations store final results in database tables.

Example reporting table:

| City | Total_Sales |
|------|------|
| Chicago | 300 |
| LA | 270 |

This table can power dashboards and reports.

---

# Key Concepts

## to_sql()

The `to_sql()` function writes a DataFrame to a database.

Example:

```python
df.to_sql("table_name", engine)
```

Parameters include:

| Parameter | Purpose |
|------|------|
| table_name | name of database table |
| engine | database connection |
| index | include DataFrame index |

Example:

```python
df.to_sql("sales_summary", engine, index=False)
```

---

## Replacing Existing Tables

If a table already exists, you may want to replace it.

Example:

```python
df.to_sql(
    "sales_summary",
    engine,
    if_exists="replace",
    index=False
)
```

Options for `if_exists`:

| Option | Meaning |
|------|------|
| fail | stop if table exists |
| replace | overwrite table |
| append | add new rows |

---

## Appending Data

Sometimes pipelines add new rows instead of replacing tables.

Example:

```python
df.to_sql(
    "sales_summary",
    engine,
    if_exists="append",
    index=False
)
```

This adds records to the existing table.

---

# Decision Flow

Writing data to a database usually follows this workflow:

```text
Retrieve data
      ↓
Transform data
      ↓
Store results in DataFrame
      ↓
Write DataFrame to database
      ↓
Database table updated
```

Example:

```python
summary_df.to_sql("sales_summary", engine)
```

---

# Code Examples

## Example 1 — Writing a DataFrame to a Database

```python
import pandas as pd

summary = pd.DataFrame({
    "City": ["Chicago", "LA", "NY"],
    "Total_Sales": [300, 270, 180]
})

summary.to_sql(
    "sales_summary",
    engine,
    index=False
)
```

This creates a database table.

---

## Example 2 — Replacing an Existing Table

```python
summary.to_sql(
    "sales_summary",
    engine,
    if_exists="replace",
    index=False
)
```

The table will be recreated.

---

## Example 3 — Appending New Data

```python
summary.to_sql(
    "sales_summary",
    engine,
    if_exists="append",
    index=False
)
```

New rows will be added to the table.

---

## Example 4 — Verifying the Table

After writing the table, it can be queried.

```python
df = pd.read_sql("SELECT * FROM sales_summary", engine)

print(df)
```

---

# SQL / Excel Comparison

Writing data to databases exists in SQL and Excel workflows.

| Concept | Pandas | SQL | Excel |
|------|------|------|------|
| insert data | to_sql() | INSERT INTO | copy table |
| create table | automatic | CREATE TABLE | new worksheet |
| append rows | append | INSERT | paste rows |

Example SQL insert:

```sql
INSERT INTO sales_summary (City, Total_Sales)
VALUES ('Chicago', 300)
```

Equivalent Pandas:

```python
df.to_sql("sales_summary", engine)
```

Excel equivalent:

Paste rows into a worksheet.

---

# Practice Exercises

## Exercise 1

Tags: Lists, DataFrames, Databases

Create a DataFrame.

```python
data = {
    "City": ["Chicago","LA","NY"],
    "Sales": [300,270,180]
}

df = pd.DataFrame(data)
```

---

## Exercise 2

Tags: Booleans, Tuples, DataFrames, Indexes

Write the DataFrame to a database table.

```python
df.to_sql("sales_summary", engine, index=False)
```

---

## Exercise 3

Tags: Tuples, Databases

Append additional rows.

```python
df.to_sql("sales_summary", engine, if_exists="append")
```

---

# Common Mistakes

## Forgetting to Disable Index Column

Default behavior includes the index column.

Example:

```python
df.to_sql("table", engine)
```

Better:

```python
df.to_sql("table", engine, index=False)
```

---

## Accidentally Replacing Tables

Using:

```python
if_exists="replace"
```

will overwrite the table.

This can delete existing data.

---

## Large Inserts Without Batching

Very large datasets may insert slowly.

Some pipelines use **batch inserts or bulk loading**.

---

# Real-World Use

Writing results to databases is common in many systems.

Examples include:

• creating tables for dashboards  
• storing ETL pipeline outputs  
• loading transformed datasets into warehouses  
• updating operational databases  

Example workflow:

```python
summary = df.groupby("City")["Sales"].sum()

summary.to_sql("sales_summary", engine, index=False)
```

This creates a reporting table used by dashboards.

---

# Lesson Recap

In this lesson you learned:

• how to write DataFrames to database tables  
• how the `to_sql()` function works  
• how to replace or append tables  
• how data pipelines store processed results  

Writing data to databases allows analysts to **store results in systems that power dashboards and reporting tools**.

---

# Next Lesson

Next we will learn:

# Lesson 6 — Managing Credentials (.env)

You will learn:

• how to store database credentials securely  
• why environment variables are used in data pipelines  
• how `.env` files improve security  

This is an important best practice for **secure and maintainable data workflows**.
