# Module 4 — Working with Data Sources

# Lesson 2 — Working with JSON Files

---

# Lesson Objective

By the end of this lesson learners will understand:

• what JSON data is  
• how JSON files are structured  
• how to load JSON files into Pandas  
• how JSON data differs from CSV or tabular data  

JSON is commonly used in **APIs, web services, and modern data platforms**, so understanding how to read JSON is an important skill for analysts.

---

# Overview

Unlike CSV files, which are structured in **rows and columns**, JSON stores data using **key-value pairs**.

Example JSON file:

```json
[
  {
    "Customer": "Alice",
    "City": "Los Angeles",
    "Sales": 120
  },
  {
    "Customer": "Bob",
    "City": "Chicago",
    "Sales": 200
  },
  {
    "Customer": "Maria",
    "City": "New York",
    "Sales": 150
  }
]
```

Each record contains **keys and values**.

Example:

```json
"Customer": "Alice"
```

• **Customer** is the key  
• **Alice** is the value  

Pandas can convert JSON data into a **DataFrame**, allowing it to be analyzed like tabular data.

Example:

```python
import pandas as pd

df = pd.read_json("sales.json")

print(df)
```

Output:

```text
Customer   City        Sales
Alice      Los Angeles 120
Bob        Chicago     200
Maria      New York    150
```

JSON is especially common when working with:

• APIs  
• web applications  
• cloud services  
• data pipelines  

---

# Key Idea Cards (3 Cards)

## JSON Stores Data as Key-Value Pairs

JSON represents data as keys and values.

Example:

```json
{
  "Customer": "Alice",
  "Sales": 120
}
```

This structure allows flexible and hierarchical data.

---

## JSON Often Comes from APIs

Many modern systems deliver data using JSON.

Examples include:

• REST APIs  
• cloud services  
• web applications  

Example API response:

```json
{
  "user_id": 101,
  "name": "Alice",
  "purchases": 5
}
```

---

## Pandas Converts JSON into DataFrames

Even though JSON is structured differently, Pandas can convert it into a table.

Example:

```python
df = pd.read_json("sales.json")
```

This allows analysts to work with JSON data just like CSV datasets.

---

# Key Concepts

## JSON Structure

JSON uses nested structures.

Example:

```json
{
  "Customer": "Alice",
  "Sales": 120
}
```

JSON can also contain arrays:

```json
{
  "Customers": [
    {"Name": "Alice"},
    {"Name": "Bob"}
  ]
}
```

This flexibility makes JSON powerful for complex data.

---

## Loading JSON Files

To read JSON files:

```python
df = pd.read_json("sales.json")
```

This converts JSON records into a DataFrame.

---

## Nested JSON

Sometimes JSON contains nested data structures.

Example:

```json
{
  "Customer": "Alice",
  "Address": {
    "City": "Los Angeles",
    "Zip": 90001
  }
}
```

Nested JSON may require **additional processing** before analysis.

---

# Decision Flow

Loading JSON data typically follows this workflow:

```text
Locate JSON file
      ↓
Load file using Pandas
      ↓
Convert JSON structure to DataFrame
      ↓
Inspect data
      ↓
Begin analysis
```

Example:

```python
df = pd.read_json("sales.json")

df.head()
```

---

# Code Examples

## Example 1 — Reading a JSON File

```python
import pandas as pd

df = pd.read_json("sales.json")

print(df)
```

---

## Example 2 — Inspecting the Dataset

```python
df.head()
```

Displays the first few records.

---

## Example 3 — Viewing Dataset Structure

```python
df.info()
```

Shows column types and record counts.

---

## Example 4 — JSON from a Dictionary

Sometimes JSON data is loaded from Python dictionaries.

```python
import pandas as pd

data = [
  {"Customer":"Alice","Sales":120},
  {"Customer":"Bob","Sales":200}
]

df = pd.DataFrame(data)

print(df)
```

---

# SQL / Excel Comparison

JSON data behaves differently from traditional tables.

| Concept | Pandas | SQL | Excel |
|------|------|------|------|
| JSON structure | nested objects | JSON column | not common |
| load JSON | read_json() | JSON functions | Power Query |
| convert to table | DataFrame | flatten JSON | transform data |

Example SQL:

```sql
SELECT JSON_VALUE(data, '$.Customer')
FROM json_table
```

Equivalent Pandas:

```python
df = pd.read_json("sales.json")
```

Excel equivalent:

Use **Power Query** to import JSON.

---

# Practice Exercises

## Exercise 1

Tags: JSON, Data I/O

Load a JSON dataset.

```python
df = pd.read_json("sales.json")
```

---

## Exercise 2

Tags: Data Sources, File I/O

Display the first rows.

```python
df.head()
```

---

## Exercise 3

Tags: Data Sources, File I/O

Check the dataset structure.

```python
df.info()
```

---

# Common Mistakes

## Assuming JSON Is Always Tabular

JSON may contain nested structures that require additional processing.

Example:

```text
Address
   └ City
   └ Zip
```

These structures may need flattening.

---

## Incorrect JSON Formatting

Example invalid JSON:

```text
Customer: Alice
Sales: 120
```

Correct JSON must include quotes:

```json
{"Customer":"Alice","Sales":120}
```

---

## Loading Large JSON Files

Large JSON files can be memory intensive.

Sometimes analysts instead:

• load JSON in chunks  
• store JSON in databases  
• convert JSON to Parquet  

---

# Real-World Use

JSON is extremely common in modern data systems.

Examples include:

• API responses  
• cloud service outputs  
• configuration files  
• application logs  

Example workflow:

```python
import pandas as pd

df = pd.read_json("api_response.json")

df.head()
```

This loads API response data into a DataFrame.

---

# Lesson Recap

In this lesson you learned:

• what JSON data is  
• how JSON files are structured  
• how to load JSON files using Pandas  
• how JSON differs from CSV data  

JSON is widely used in **modern APIs and web systems**, making it an important format for analysts to understand.

---

# Next Lesson

Next we will learn:

# Lesson 3 — Connecting to Databases

You will learn:

• how Python connects to databases  
• how to query databases using SQL inside Python  
• how analysts retrieve data from data warehouses  

This is an important step for working with **production data systems**.
