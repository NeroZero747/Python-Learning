# Module 17 — APIs & Data Integration  
## Lesson 8 — Handling Pagination in APIs

---

# Lesson Objective

By the end of this lesson you will understand:

- What **pagination** is in APIs  
- Why APIs return results in **multiple pages**  
- How to retrieve **all records from paginated APIs**  
- How to build Python scripts that automatically retrieve complete datasets

Pagination is essential when working with APIs that return **large datasets**.

---

# Overview

Many APIs limit the amount of data returned in a single request.

Instead of returning thousands of records at once, the API splits the data into **multiple pages**.

Example:

```text
API Request
      ↓
Page 1 → Records 1–100
Page 2 → Records 101–200
Page 3 → Records 201–300
```

Your script must request **each page** in order to retrieve the full dataset.

This process is called:

```text
Pagination
```

---

# Key Concepts

## What is Pagination?

Pagination is a method used by APIs to divide large datasets into smaller pages.

Example:

| Page | Records |
|------|------|
| Page 1 | 1–100 |
| Page 2 | 101–200 |
| Page 3 | 201–300 |

Each request returns a portion of the dataset.

---

## Why APIs Use Pagination

Pagination improves:

| Benefit | Description |
|------|------|
| Performance | Smaller responses load faster |
| Stability | Prevents large responses from overwhelming servers |
| Network Efficiency | Reduces bandwidth usage |

Without pagination, large responses could slow down or crash systems.

---

## Common Pagination Parameters

APIs usually support parameters that specify which page to retrieve.

Examples include:

| Parameter | Purpose |
|------|------|
| page | Page number |
| limit | Number of records per page |
| offset | Starting record |

Example request:

```text
https://api.example.com/data?page=2
```

This retrieves page 2 of the dataset.

---

# Decision Flow

When retrieving API data:

```text
Does the API return paginated results?
        |
       Yes
        |
Identify pagination parameters
        |
Loop through pages
        |
Combine results into dataset
```

Pagination usually requires **looping through requests**.

---

# Code Examples

## Example 1 — Basic Pagination Request

```python
import requests

url = "https://api.example.com/data"

params = {
    "page": 1
}

response = requests.get(url, params=params)

data = response.json()

print(data)
```

This retrieves the first page.

---

## Example 2 — Looping Through Pages

```python
import requests

url = "https://api.example.com/data"

all_records = []

for page in range(1, 6):

    params = {"page": page}

    response = requests.get(url, params=params)

    data = response.json()

    all_records.extend(data["results"])

print(len(all_records))
```

This script retrieves multiple pages of results.

---

## Example 3 — Converting Paginated Data to a DataFrame

```python
import pandas as pd

df = pd.DataFrame(all_records)

print(df.head())
```

This converts the combined dataset into a table.

---

# SQL / Excel Comparison

Without APIs:

```text
Download file
Open Excel
Load data manually
```

With paginated APIs:

```text
Python script
      ↓
Request multiple pages
      ↓
Combine results
      ↓
Structured dataset
```

This enables automated ingestion of large datasets.

---

# Practice Exercises

## Exercise 1

Tags: Dictionaries, APIs, Pagination

Modify an API request to include a `page` parameter.

Example:

```python
params = {"page": 1}
```

---

## Exercise 2

Tags: range(), Tuples, Loops, Iteration

Write a loop that retrieves multiple pages from an API.

Example:

```python
for page in range(1, 5):
```

---

## Exercise 3

Tags: Lists, Pagination, Streamlit

Combine results from multiple pages into a list.

Example:

```python
all_records.extend(data["results"])
```

---

# Common Mistakes

## Mistake 1 — Retrieving Only the First Page

Some APIs return only the first page by default.

Always check the API documentation.

---

## Mistake 2 — Ignoring Pagination Limits

APIs may limit:

- number of pages
- records per request

Scripts should account for these limits.

---

## Mistake 3 — Overwriting Results

Always append results instead of replacing them.

Correct approach:

```python
all_records.extend(data["results"])
```

---

# Real-World Use

Pagination is common in many large-scale APIs.

Examples include:

---

### Social Media APIs

Example:

```text
user posts
followers
comments
```

Large datasets are divided into pages.

---

### Financial Data APIs

Example:

```text
historical prices
market transactions
trade records
```

These datasets often require multiple requests.

---

### Data Pipelines

Many pipelines retrieve paginated API data before processing it.

Example pipeline:

```text
API Pages → Combine Results → Data Processing → Database
```

---

# Key Idea Cards

### Card 1

Pagination divides large datasets into smaller pages.

---

### Card 2

Scripts must request **multiple pages** to retrieve complete datasets.

---

### Card 3

Pagination typically uses parameters such as **page, limit, or offset**.

---

# Lesson Recap

In this lesson you learned:

- what pagination is  
- why APIs return results in multiple pages  
- how to retrieve paginated data using loops  
- how to combine results into structured datasets

Pagination is essential for retrieving **large datasets from APIs**.

---

# Next Lesson

Next you will learn:

**Module 17 — Lesson 9: Handling API Rate Limits**

You will learn how to:

- avoid exceeding API usage limits  
- implement delays between requests  
- build reliable API integrations.