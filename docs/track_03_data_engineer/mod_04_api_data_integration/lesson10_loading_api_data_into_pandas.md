# Module 17 — APIs & Data Integration  
## Lesson 10 — Loading API Data into Pandas

---

# Lesson Objective

By the end of this lesson you will understand:

- How to **convert API responses into Pandas DataFrames**
- How to work with **lists of API records**
- How to structure API data for analysis
- How APIs can serve as **data sources for analytics workflows**

Many API responses contain **tabular data**, which can be easily converted into DataFrames for analysis.

---

# Overview

Most APIs return data as **JSON objects or lists of records**.

Example API response:

```json
{
  "users": [
    {"name": "Alice", "sales": 120},
    {"name": "Bob", "sales": 150},
    {"name": "Charlie", "sales": 200}
  ]
}
```

This structure can be converted directly into a table.

Example workflow:

```text
API Request
      ↓
JSON Response
      ↓
Extract Records
      ↓
Create DataFrame
      ↓
Data Analysis
```

This allows APIs to become **live data sources for analytics pipelines**.

---

# Key Concepts

## Tabular API Data

Many APIs return data as **lists of records**.

Example JSON structure:

```json
{
  "data": [
    {"city": "Los Angeles", "sales": 100},
    {"city": "New York", "sales": 200}
  ]
}
```

Each record contains fields representing columns.

This structure maps naturally to a DataFrame.

---

## Converting JSON to DataFrames

Pandas can convert lists of dictionaries into tables.

Example:

```python
import pandas as pd

records = [
    {"city": "Los Angeles", "sales": 100},
    {"city": "New York", "sales": 200}
]

df = pd.DataFrame(records)

print(df)
```

Result:

```text
           city  sales
0  Los Angeles    100
1     New York    200
```

---

## API Data Processing Workflow

Many Python pipelines follow this pattern:

```text
API Request
      ↓
JSON Response
      ↓
Parse JSON
      ↓
Convert to DataFrame
      ↓
Data Processing
```

This enables automated data analysis.

---

# Decision Flow

When retrieving API data:

```text
Retrieve API response
        ↓
Convert response to JSON
        ↓
Extract list of records
        ↓
Convert records into DataFrame
```

This allows the data to be processed using Pandas tools.

---

# Code Examples

## Example 1 — API Request and DataFrame Conversion

```python
import requests
import pandas as pd

url = "https://api.example.com/data"

response = requests.get(url)

data = response.json()

records = data["results"]

df = pd.DataFrame(records)

print(df.head())
```

This converts API records into a table.

---

## Example 2 — Inspecting API Data

Before creating a DataFrame, inspect the JSON structure.

```python
print(data.keys())
```

This helps identify where the records are stored.

---

## Example 3 — Selecting Columns

Once data is in a DataFrame, columns can be selected.

```python
df = df[["name", "sales"]]

print(df)
```

This prepares the dataset for analysis.

---

## Example 4 — Aggregating API Data

After loading data into Pandas, analytics can be performed.

```python
total_sales = df["sales"].sum()

print(total_sales)
```

This demonstrates how API data integrates into analysis workflows.

---

# SQL / Excel Comparison

Without APIs:

```text
Download CSV
Open Excel
Import data
Perform calculations
```

With APIs:

```text
Python script
      ↓
API request
      ↓
Convert JSON to DataFrame
      ↓
Run analysis
```

This allows fully automated data pipelines.

---

# Practice Exercises

## Exercise 1

Tags: Lists, Dictionaries, DataFrames, APIs

Create a DataFrame from a list of dictionaries.

```python
records = [
    {"city": "Los Angeles", "sales": 100},
    {"city": "New York", "sales": 200}
]
```

---

## Exercise 2

Tags: DataFrames, APIs, Data I/O

Write code to convert API records into a DataFrame.

```python
df = pd.DataFrame(records)
```

---

## Exercise 3

Tags: Lists, DataFrames, Aggregations, APIs

Perform a basic aggregation on the DataFrame.

Example:

```python
df["sales"].sum()
```

---

# Common Mistakes

## Mistake 1 — Not Inspecting the JSON Structure

Always inspect the response before extracting records.

Example:

```python
print(data)
```

---

## Mistake 2 — Extracting the Wrong Field

Records are often nested inside a specific key such as:

```text
data
results
items
```

Check the structure carefully.

---

## Mistake 3 — Ignoring Missing Values

Some API responses may contain missing fields.

Pandas handles these values as:

```text
NaN
```

---

# Real-World Use

Loading API data into DataFrames is common in analytics systems.

Examples include:

---

### Marketing Analytics

APIs retrieve metrics from platforms such as:

```text
Google Analytics
Facebook Ads
HubSpot
```

---

### Financial Data

Financial APIs provide data such as:

```text
stock prices
exchange rates
market indicators
```

---

### Business Applications

Companies retrieve data from APIs for reporting.

Example pipeline:

```text
API → DataFrame → Data Processing → Dashboard
```

---

# Key Idea Cards

### Card 1

Many APIs return data as lists of records.

---

### Card 2

Lists of dictionaries can be converted directly into Pandas DataFrames.

---

### Card 3

API data can be integrated directly into data analysis workflows.

---

# Lesson Recap

In this lesson you learned:

- how API responses can be converted into DataFrames  
- how to extract lists of records from JSON responses  
- how to prepare API data for analysis  
- how APIs integrate with Pandas workflows

APIs often serve as **live data sources for analytics pipelines**.

---

# Next Lesson

Next you will learn:

**Module 17 — Lesson 11: Saving API Data to Databases**

You will learn how to:

- store API data in databases  
- integrate APIs with SQL workflows  
- build automated data ingestion pipelines.