# Module 17 — APIs & Data Integration  
## Lesson 5 — Parsing API Responses

---

# Lesson Objective

By the end of this lesson you will understand:

- How to **extract useful information from API responses**  
- How to work with **nested JSON structures**  
- How to convert API responses into structured datasets  
- How to prepare API data for analysis

Retrieving API data is only the first step. The next step is **parsing the response to extract the fields you need**.

---

# Overview

When you send a request to an API, the server usually returns a **large JSON response**.

Example:

```json
{
  "user": {
    "id": 123,
    "name": "Alice",
    "location": "California"
  },
  "repositories": 45,
  "followers": 210
}
```

However, analysts often only need a **subset of this data**.

Example:

```text
Name
Location
Followers
```

Parsing means **extracting the specific values you want from the API response**.

Workflow:

```text
API Request
      ↓
JSON Response
      ↓
Parse JSON Data
      ↓
Extract Relevant Fields
      ↓
Structured Dataset
```

---

# Key Concepts

## Parsing

Parsing means interpreting structured data and extracting values from it.

For API responses, this typically involves:

- accessing dictionary keys
- navigating nested objects
- selecting specific fields

Example:

```python
data["user"]["name"]
```

---

## Nested JSON

Many APIs return nested data structures.

Example JSON:

```json
{
  "user": {
    "name": "Alice",
    "address": {
      "city": "Los Angeles",
      "state": "CA"
    }
  }
}
```

Python access:

```python
data["user"]["address"]["city"]
```

Understanding nested JSON is essential for parsing API responses.

---

## Extracting Lists of Records

Some APIs return lists of records.

Example:

```json
{
  "users": [
    {"name": "Alice", "sales": 100},
    {"name": "Bob", "sales": 200}
  ]
}
```

This structure is common for datasets retrieved from APIs.

Python can convert these records into tabular data.

---

# Decision Flow

When processing API responses:

```text
Retrieve API response
        ↓
Convert response to JSON
        ↓
Inspect JSON structure
        ↓
Extract required fields
        ↓
Convert data into dataset
```

Inspecting the JSON structure is often the most important step.

---

# Code Examples

## Example 1 — Parsing JSON Fields

```python
import requests

url = "https://api.github.com/users/octocat"

response = requests.get(url)

data = response.json()

print(data["login"])
print(data["followers"])
```

This extracts specific fields from the API response.

---

## Example 2 — Navigating Nested JSON

Example JSON structure:

```json
{
  "company": {
    "name": "Example Corp",
    "location": {
      "city": "Los Angeles"
    }
  }
}
```

Python access:

```python
data["company"]["location"]["city"]
```

---

## Example 3 — Extracting Lists of Records

Example API response:

```json
{
  "users": [
    {"name": "Alice", "sales": 100},
    {"name": "Bob", "sales": 200}
  ]
}
```

Python code:

```python
records = data["users"]

for record in records:
    print(record["name"], record["sales"])
```

---

## Example 4 — Converting API Data into a DataFrame

```python
import pandas as pd

records = data["users"]

df = pd.DataFrame(records)

print(df)
```

This converts the parsed data into a structured table.

---

# SQL / Excel Comparison

Without APIs:

```text
Download CSV
Open Excel
Clean data
Create report
```

With APIs:

```text
API request
      ↓
Parse JSON
      ↓
Create DataFrame
```

This enables automated data ingestion.

---

# Practice Exercises

## Exercise 1

Tags: print(), Lists, SELECT, APIs

Retrieve data from the GitHub API and print specific fields.

Example:

```python
print(data["login"])
print(data["public_repos"])
```

---

## Exercise 2

Tags: print(), APIs

Inspect a JSON response and identify nested fields.

Example:

```python
print(data.keys())
```

---

## Exercise 3

Tags: Lists, DataFrames, APIs

Convert a list of API records into a Pandas DataFrame.

```python
df = pd.DataFrame(records)
```

---

# Common Mistakes

## Mistake 1 — Not Inspecting the JSON Structure

Always inspect the structure before extracting fields.

Example:

```python
print(data)
```

---

## Mistake 2 — Accessing Keys That Do Not Exist

Some records may not contain every field.

Always check keys carefully.

---

## Mistake 3 — Forgetting to Convert Lists to DataFrames

Lists of records should usually be converted into tabular format.

Example:

```python
df = pd.DataFrame(records)
```

---

# Real-World Use

Parsing API responses is essential in many real-world systems.

Examples include:

---

### Data Pipelines

Pipelines retrieve API data and transform it into structured datasets.

Example:

```text
API → JSON Response → Parsed Data → Database
```

---

### Analytics Systems

Analytics teams parse API data to retrieve metrics from:

```text
marketing platforms
financial services
analytics tools
```

---

### Automation

Automation scripts retrieve API data and update dashboards automatically.

---

# Key Idea Cards

### Card 1

Parsing means extracting specific values from structured data.

---

### Card 2

Most API responses contain nested JSON structures.

---

### Card 3

Lists of API records can be converted into DataFrames.

---

# Lesson Recap

In this lesson you learned:

- how to parse API responses  
- how to navigate nested JSON structures  
- how to extract specific fields from responses  
- how to convert API data into structured datasets

Parsing API responses is a critical step in **data integration workflows**.

---

# Next Lesson

Next you will learn:

**Module 17 — Lesson 6: Authentication with API Keys**

You will learn how to:

- access APIs that require authentication  
- securely use API keys  
- send authenticated requests.