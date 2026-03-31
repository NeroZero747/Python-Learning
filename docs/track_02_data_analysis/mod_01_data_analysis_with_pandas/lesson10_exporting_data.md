# Module 3 — Data Analysis with Pandas

# Lesson 10 — Exporting Data

---

# Lesson Objective

By the end of this lesson learners will understand:

• how to export a DataFrame to a CSV file  
• how to export a DataFrame to an Excel file  
• how analysts deliver processed data to other systems  
• how exporting data fits into the analytics workflow  

Exporting data allows analysts to **share results with reports, dashboards, and downstream systems**.

---

# Overview

After analyzing and transforming data, the final step is often to **export the results**.

Examples of export scenarios:

• exporting a cleaned dataset for reporting  
• saving aggregated metrics  
• sending processed data to another system  
• generating files for dashboards or analysts  

Example processed dataset:

| City | Total_Sales |
|------|------|
| Chicago | 300 |
| LA | 270 |
| NY | 180 |

We may want to export this dataset as a **CSV file**.

Example:

```python
summary.to_csv("sales_summary.csv")
```

This saves the DataFrame to a file that can be opened in:

• Excel  
• BI tools  
• other Python programs  
• SQL ingestion pipelines  

Exporting data is the **final step in many analytics workflows**.

---

# Key Idea Cards (3 Cards)

## DataFrames Can Be Saved to Files

Pandas allows DataFrames to be saved to many formats.

Common examples include:

• CSV  
• Excel  
• JSON  
• Parquet  

Example:

```python
df.to_csv("output.csv")
```

---

## CSV Files Are the Most Common Export Format

CSV files are widely used because they are:

• simple  
• lightweight  
• supported by most tools  

Example export:

```python
df.to_csv("data_export.csv")
```

The file can be opened in Excel or loaded into databases.

---

## Exporting Is Often the Final Step in Data Pipelines

Typical analytics workflow:

```text
Load data
Clean data
Analyze data
Export results
```

The exported file becomes the **deliverable dataset**.

---

# Key Concepts

## Exporting to CSV

The `to_csv()` function saves a DataFrame to a CSV file.

Example:

```python
df.to_csv("output.csv")
```

This creates a file named **output.csv** in the working directory.

---

## Removing the Index Column

By default, Pandas includes the index column in exports.

Example:

```python
df.to_csv("output.csv", index=False)
```

This prevents the index from appearing in the exported file.

---

## Exporting to Excel

Pandas can export data to Excel files.

Example:

```python
df.to_excel("output.xlsx", index=False)
```

This creates an Excel spreadsheet containing the dataset.

---

## Exporting Specific Columns

Sometimes only specific columns should be exported.

Example:

```python
df[["City", "Sales"]].to_csv("city_sales.csv", index=False)
```

This exports only the selected columns.

---

# Decision Flow

Exporting data usually follows this workflow:

```text
Load dataset
      ↓
Clean and analyze data
      ↓
Generate summary results
      ↓
Export dataset
```

Example:

```python
summary.to_csv("sales_summary.csv", index=False)
```

This saves the results for external use.

---

# Code Examples

## Example 1 — Exporting to CSV

```python
import pandas as pd

data = {
    "City": ["LA", "Chicago", "NY"],
    "Sales": [270, 300, 180]
}

df = pd.DataFrame(data)

df.to_csv("sales_summary.csv", index=False)
```

This creates a file named **sales_summary.csv**.

---

## Example 2 — Exporting to Excel

```python
df.to_excel("sales_summary.xlsx", index=False)
```

The file can be opened in Excel.

---

## Example 3 — Exporting Selected Columns

```python
df[["City"]].to_csv("cities.csv", index=False)
```

Only the **City column** will be exported.

---

## Example 4 — Exporting Aggregated Results

```python
sales_summary = df.groupby("City")["Sales"].sum()

sales_summary.to_csv("sales_by_city.csv")
```

This exports aggregated results.

---

# SQL / Excel Comparison

Exporting data exists in SQL and Excel workflows as well.

| Concept | Pandas | SQL | Excel |
|------|------|------|------|
| export dataset | to_csv() | EXPORT / COPY | Save As |
| file output | CSV | CSV | XLSX |
| export subset | column selection | SELECT columns | copy sheet |

Example SQL export:

```sql
SELECT *
INTO OUTFILE 'sales.csv'
FROM sales_table;
```

Equivalent Pandas:

```python
df.to_csv("sales.csv")
```

Excel equivalent:

File → **Save As → CSV**

---

# Practice Exercises

## Exercise 1

Tags: Booleans, Tuples, to_csv(), DataFrames

Export a DataFrame to CSV.

```python
df.to_csv("data_export.csv", index=False)
```

---

## Exercise 2

Tags: Booleans, Tuples, to_excel(), DataFrames

Export a DataFrame to Excel.

```python
df.to_excel("data_export.xlsx", index=False)
```

---

## Exercise 3

Tags: Booleans, Lists, Tuples, to_csv()

Export only one column.

```python
df[["City"]].to_csv("cities.csv", index=False)
```

---

# Common Mistakes

## Forgetting to Remove the Index

Default export includes an index column.

Example:

```python
df.to_csv("output.csv")
```

This may produce an extra column.

Better:

```python
df.to_csv("output.csv", index=False)
```

---

## Overwriting Existing Files

Exporting with the same filename replaces existing files.

Example:

```python
df.to_csv("sales.csv")
```

If the file already exists, it will be overwritten.

---

## Exporting Large Datasets Without Compression

Large exports can produce very large files.

Example:

```python
df.to_csv("data.csv")
```

Sometimes compression or Parquet is better.

---

# Real-World Use

Exporting data is common in many workflows.

Examples include:

• exporting sales summaries for management  
• exporting cleaned datasets for BI tools  
• generating files for automated pipelines  
• sending results to data warehouses  

Example workflow:

```python
df = pd.read_csv("sales_data.csv")

summary = df.groupby("City")["Sales"].sum()

summary.to_csv("sales_summary.csv")
```

This creates a summary dataset ready for reporting.

---

# Lesson Recap

In this lesson you learned:

• how to export DataFrames to CSV files  
• how to export DataFrames to Excel  
• how exporting fits into analytics workflows  
• how analysts share processed data with other tools  

Exporting data is typically the **final step in many data analysis processes**.

---

# Next Module

You have now completed:

# Module 3 — Data Analysis with Pandas

You learned how to:

• load datasets  
• inspect DataFrames  
• select and filter data  
• create calculated columns  
• aggregate data  
• join datasets  
• handle missing values  
• export results  

---

# Next Module

# Module 4 — Working with Data Sources

In the next module you will learn:

• how to work with JSON files  
• how to connect to databases  
• how to run SQL queries inside Python  
• how to write data back to databases  
• how to manage credentials using `.env` files  

This module focuses on **real-world data engineering workflows** where Python interacts with external systems.