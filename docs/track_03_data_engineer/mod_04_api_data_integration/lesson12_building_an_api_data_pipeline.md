# Module 17 — APIs & Data Integration  
## Lesson 12 — Building an API Data Pipeline

---

# Lesson Objective

By the end of this lesson you will understand:

- What an **API data pipeline** is  
- How to combine API requests, data processing, and storage  
- How to structure a Python script that retrieves and processes API data  
- How API pipelines are used in automated analytics systems

API pipelines are a core component of modern **data engineering and analytics workflows**.

---

# Overview

So far in this module you have learned how to:

- send API requests  
- authenticate with APIs  
- parse JSON responses  
- handle pagination  
- manage rate limits  
- convert API data into DataFrames  
- store API data in databases  

The next step is combining these pieces into a **complete pipeline**.

Example workflow:

```text
API Request
      ↓
Retrieve JSON Data
      ↓
Parse and Clean Data
      ↓
Convert to DataFrame
      ↓
Store in Database
```

This process is called a **data pipeline**.

A pipeline automatically moves data from a source to a destination.

---

# Key Concepts

## What is a Data Pipeline?

A data pipeline is a process that moves data from one system to another.

Typical pipeline stages:

```text
Data Source → Data Processing → Data Storage
```

Example API pipeline:

```text
API
 ↓
Python Script
 ↓
Data Processing
 ↓
Database
```

Pipelines automate data movement and transformation.

---

## Pipeline Components

Most API pipelines contain several components.

| Component | Purpose |
|------|------|
| API Request | Retrieve data |
| Parsing | Extract relevant fields |
| Transformation | Clean and structure data |
| Storage | Save data to database or files |

These steps form a repeatable workflow.

---

## Automation

API pipelines are often scheduled to run automatically.

Examples:

```text
Hourly data updates
Daily report refresh
Real-time monitoring
```

Automation ensures data stays current.

---

# Decision Flow

When building an API pipeline:

```text
Retrieve API data
        ↓
Parse JSON response
        ↓
Transform data
        ↓
Convert to DataFrame
        ↓
Store data in database or file
```

This pattern forms the foundation of many analytics systems.

---

# Code Examples

## Example 1 — Basic API Pipeline

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

This pipeline retrieves data and converts it into a table.

---

## Example 2 — API Pipeline with Database Storage

```python
import requests
import pandas as pd
from sqlalchemy import create_engine

url = "https://api.example.com/data"

response = requests.get(url)

data = response.json()

records = data["results"]

df = pd.DataFrame(records)

engine = create_engine("sqlite:///example.db")

df.to_sql("api_data", engine, if_exists="append", index=False)
```

This pipeline retrieves API data and stores it in a database.

---

## Example 3 — Structured Pipeline Function

In production systems, pipelines are often organized into functions.

```python
def fetch_api_data(url):

    response = requests.get(url)

    return response.json()
```

```python
def transform_data(data):

    records = data["results"]

    return pd.DataFrame(records)
```

```python
def run_pipeline():

    data = fetch_api_data("https://api.example.com/data")

    df = transform_data(data)

    print(df.head())
```

This structure improves readability and maintainability.

---

# SQL / Excel Comparison

Traditional workflow:

```text
Download data
Open Excel
Update report manually
```

Pipeline workflow:

```text
API
 ↓
Python Pipeline
 ↓
Database
 ↓
Dashboard
```

This allows automated data processing.

---

# Practice Exercises

## Exercise 1

Tags: SELECT, APIs, HTTP Methods, CI/CD

Write a script that retrieves API data and prints the results.

Example:

```python
response = requests.get(url)
```

---

## Exercise 2

Tags: DataFrames, APIs, CI/CD

Convert the API response into a DataFrame.

Example:

```python
df = pd.DataFrame(records)
```

---

## Exercise 3

Tags: Tuples, DataFrames, Databases, APIs

Save the DataFrame to a database table.

Example:

```python
df.to_sql("api_data", engine)
```

---

# Common Mistakes

## Mistake 1 — Building Monolithic Scripts

Large scripts are difficult to maintain.

Use functions to separate pipeline steps.

---

## Mistake 2 — Not Handling Errors

API pipelines should handle:

- failed requests
- missing data
- rate limits

---

## Mistake 3 — Ignoring Data Validation

Data retrieved from APIs should be validated before storage.

---

# Real-World Use

API pipelines are used across many industries.

Examples include:

---

### Financial Data Systems

Pipelines retrieve:

```text
market prices
economic indicators
trading data
```

---

### Marketing Analytics

Marketing platforms provide APIs for campaign data.

Example pipeline:

```text
Marketing API → Database → Dashboard
```

---

### Operational Systems

Companies integrate multiple systems through APIs.

Example:

```text
CRM API → Data Warehouse → Business Reports
```

---

# Key Idea Cards

### Card 1

API pipelines automate the movement of data between systems.

---

### Card 2

Most pipelines follow the pattern: **retrieve → process → store**.

---

### Card 3

Structuring pipelines with functions improves maintainability.

---

# Lesson Recap

In this lesson you learned:

- what API data pipelines are  
- how to combine API requests, parsing, and storage  
- how to structure Python scripts for pipelines  
- how pipelines automate data workflows

API pipelines are foundational for **modern data integration systems**.

---

# Next Lesson

Next you will learn:

**Module 17 — Lesson 13: Real-World API Integration Project**

You will apply everything learned in this module to:

- build a complete API data pipeline  
- retrieve live data from an API  
- process and store the data for analysis.