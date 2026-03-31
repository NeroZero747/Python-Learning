# Module 17 — APIs & Data Integration  
## Lesson 4 — Working with JSON Data

---

# Lesson Objective

By the end of this lesson you will understand:

- What **JSON (JavaScript Object Notation)** is  
- Why JSON is the most common format used by APIs  
- How JSON data is structured  
- How Python reads and processes JSON data

JSON is one of the most important data formats in **modern APIs and data pipelines**.

---

# Overview

When an API responds to a request, it usually returns data in a structured format.

The most common format is:

```text
JSON
```

JSON is a lightweight format used to represent structured data.

Example JSON response:

```json
{
  "city": "Los Angeles",
  "temperature": 72,
  "conditions": "Sunny"
}
```

Python programs can easily convert JSON data into Python objects.

Example workflow:

```text
API Request
      ↓
JSON Response
      ↓
Python Dictionary
      ↓
Data Processing
```

Understanding JSON is essential for **working with APIs**.

---

# Key Concepts

## What is JSON?

JSON (JavaScript Object Notation) is a format used to represent structured data.

It is commonly used for:

- APIs
- web applications
- configuration files
- data exchange between systems

JSON is easy for both **humans and machines to read**.

---

## JSON Structure

JSON data is built from two primary structures.

### Objects

Objects store key-value pairs.

Example:

```json
{
  "name": "Alice",
  "age": 30
}
```

Python equivalent:

```python
{
  "name": "Alice",
  "age": 30
}
```

This is a **Python dictionary**.

---

### Arrays

Arrays store lists of values.

Example:

```json
{
  "cities": ["Los Angeles", "New York", "Chicago"]
}
```

Python equivalent:

```python
["Los Angeles", "New York", "Chicago"]
```

This becomes a **Python list**.

---

# Decision Flow

When retrieving data from APIs:

```text
Does the API return JSON?
        |
       Yes
        |
Convert JSON to Python objects
        |
Process the data
```

Python provides tools that make JSON processing very simple.

---

# Code Examples

## Example 1 — Reading JSON from an API

```python
import requests

url = "https://api.github.com"

response = requests.get(url)

data = response.json()

print(data)
```

The `.json()` method converts the response into a Python dictionary.

---

## Example 2 — Accessing JSON Fields

```python
import requests

url = "https://api.github.com"

response = requests.get(url)

data = response.json()

print(data["current_user_url"])
```

This retrieves a specific value from the JSON response.

---

## Example 3 — Working with Nested JSON

Many APIs return nested structures.

Example JSON:

```json
{
  "user": {
    "name": "Alice",
    "location": "California"
  }
}
```

Python access:

```python
data["user"]["name"]
```

---

## Example 4 — Converting JSON to a DataFrame

JSON responses often contain lists of records.

Example:

```python
import pandas as pd

records = [
    {"name": "Alice", "sales": 100},
    {"name": "Bob", "sales": 200}
]

df = pd.DataFrame(records)

print(df)
```

This converts JSON-style data into a Pandas DataFrame.

---

# SQL / Excel Comparison

Without APIs:

```text
Download CSV file
Import into Excel
Process rows manually
```

With JSON APIs:

```text
API Request
      ↓
JSON Data
      ↓
Convert to DataFrame
```

This allows automated data ingestion.

---

# Practice Exercises

## Exercise 1

Tags: print(), requests, Imports, JSON

Send a request to the GitHub API and print the JSON response.

```python
import requests

response = requests.get("https://api.github.com")

data = response.json()

print(data)
```

---

## Exercise 2

Tags: print(), Lists

Extract specific values from the JSON data.

Example:

```python
print(data["current_user_url"])
```

---

## Exercise 3

Tags: print(), Dictionaries, pandas, Imports

Create a DataFrame from a JSON dataset.

```python
import pandas as pd

data = [
    {"city": "Los Angeles", "sales": 100},
    {"city": "New York", "sales": 200}
]

df = pd.DataFrame(data)

print(df)
```

---

# Common Mistakes

## Mistake 1 — Misunderstanding JSON Structure

APIs often return **nested JSON objects**.

Carefully inspect the structure before extracting values.

---

## Mistake 2 — Assuming JSON is Always Flat

Many APIs return hierarchical data structures.

Example:

```text
User
 └─ Address
 └─ Orders
```

These must be parsed carefully.

---

## Mistake 3 — Ignoring Missing Keys

Not every record may contain every field.

Scripts should handle missing values safely.

---

# Real-World Use

JSON is widely used across modern systems.

Examples include:

---

### APIs

Most web APIs return JSON responses.

Examples include:

```text
GitHub API
Twitter API
Weather APIs
```

---

### Configuration Files

Many applications use JSON files for configuration.

Example:

```text
config.json
```

---

### Data Pipelines

Automation pipelines frequently ingest JSON data from APIs.

Example pipeline:

```text
API → JSON Data → Data Processing → Database
```

---

# Key Idea Cards

### Card 1

JSON is the most common format used by modern APIs.

---

### Card 2

JSON objects convert directly into Python dictionaries.

---

### Card 3

JSON arrays convert into Python lists.

---

# Lesson Recap

In this lesson you learned:

- what JSON is  
- how JSON structures store data  
- how Python converts JSON into dictionaries and lists  
- how JSON data can be converted into DataFrames

JSON is the **primary data format used in modern APIs**.

---

# Next Lesson

Next you will learn:

**Module 17 — Lesson 5: Parsing API Responses**

You will learn how to:

- extract specific data from API responses  
- handle nested JSON structures  
- transform API data into structured datasets.