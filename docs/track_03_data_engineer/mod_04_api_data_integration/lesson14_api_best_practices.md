# Module 17 — APIs & Data Integration  
## Lesson 14 — API Best Practices

---

# Lesson Objective

By the end of this lesson you will understand:

- Best practices for building **reliable API integrations**
- How to design **robust API scripts**
- How to structure API pipelines for maintainability
- How professional data teams manage API integrations in production

This lesson summarizes the most important practices for working with APIs in **real-world systems**.

---

# Overview

Working with APIs in small scripts is relatively simple.

However, production systems must handle challenges such as:

```text
Network failures
Authentication issues
Rate limits
Changing API responses
Large datasets
```

Without proper design, API scripts can become unreliable.

Best practices help ensure that API integrations are:

```text
Reliable
Maintainable
Secure
Scalable
```

---

# Key Concepts

## Validate API Responses

Always check whether a request succeeded before processing the data.

Example:

```python
if response.status_code == 200:
    data = response.json()
else:
    print("API request failed")
```

Ignoring response codes may cause scripts to process invalid data.

---

## Handle Errors Gracefully

APIs may fail for many reasons:

```text
Network outages
Server errors
Authentication failures
Rate limits
```

Scripts should handle these situations safely.

Example:

```python
try:
    response = requests.get(url)
    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
```

This prevents scripts from crashing unexpectedly.

---

## Respect Rate Limits

Sending too many requests too quickly may cause the API to block access.

Best practices include:

```text
Add delays between requests
Implement retry logic
Monitor API usage
```

Example:

```python
import time

time.sleep(1)
```

---

## Store API Credentials Securely

Never store credentials directly in scripts.

Avoid this:

```python
api_key = "123abc"
```

Instead use:

```text
Environment variables
Configuration files
Secrets management tools
```

Example:

```python
import os

api_key = os.getenv("API_KEY")
```

---

## Inspect API Responses Carefully

Always inspect the structure of API responses before extracting fields.

Example:

```python
print(data)
```

This prevents errors caused by incorrect assumptions about the data structure.

---

## Modularize API Code

Large scripts become difficult to maintain.

Instead, break pipelines into smaller functions.

Example structure:

```text
Fetch Data
Process Data
Store Data
```

Example implementation:

```python
def fetch_data(url):
    response = requests.get(url)
    return response.json()
```

```python
def transform_data(data):
    return pd.DataFrame(data["results"])
```

This improves code readability and reuse.

---

# Decision Flow

When designing an API integration:

```text
Does the API require authentication?
        |
       Yes
        ↓
Securely store credentials
        ↓
Send API request
        ↓
Validate response
        ↓
Parse data
        ↓
Store results
```

Following a structured workflow improves reliability.

---

# Code Example — Production-Style API Script

```python
import requests
import pandas as pd

def fetch_api_data(url):

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("API request failed")

    return response.json()

def transform_data(data):

    return pd.DataFrame(data["results"])

def run_pipeline():

    url = "https://api.example.com/data"

    data = fetch_api_data(url)

    df = transform_data(data)

    print(df.head())

run_pipeline()
```

This structure separates responsibilities across functions.

---

# SQL / Excel Comparison

Manual workflow:

```text
Download CSV
Open Excel
Clean data
Generate report
```

API workflow:

```text
API Request
      ↓
Python Processing
      ↓
Database Storage
      ↓
Analytics Dashboard
```

This enables fully automated data systems.

---

# Practice Exercises

## Exercise 1

Tags: Conditionals, APIs, Scripts

Modify a script to check the response status code before processing data.

Example:

```python
if response.status_code == 200:
```

---

## Exercise 2

Tags: Functions, SELECT, APIs

Create a function that retrieves API data.

Example:

```python
def fetch_data(url):
```

---

## Exercise 3

Tags: Error Handling, APIs, HTTP Methods, Streamlit

Add error handling to an API request.

Example:

```python
try:
    response = requests.get(url)
```

---

# Common Mistakes

## Mistake 1 — Ignoring Error Handling

Scripts should anticipate possible failures.

---

## Mistake 2 — Hardcoding Credentials

Credentials should never be stored directly in scripts.

---

## Mistake 3 — Writing Large Monolithic Scripts

Break pipelines into smaller functions.

---

# Real-World Use

API integrations are widely used in modern systems.

Examples include:

---

### Data Engineering Pipelines

Example:

```text
API → Data Processing → Data Warehouse
```

---

### Analytics Systems

Example:

```text
Marketing API → Database → Dashboard
```

---

### Automation Systems

Example:

```text
API → Automated Reports → Business Intelligence Tools
```

---

# Key Idea Cards

### Card 1

Always validate API responses before processing data.

---

### Card 2

Securely store API credentials using environment variables.

---

### Card 3

Organize API pipelines into modular functions.

---

# Lesson Recap

In this lesson you learned:

- best practices for API integrations  
- how to design reliable API pipelines  
- how to handle errors and rate limits  
- how to structure maintainable API code

Following these practices helps build **production-ready API workflows**.

---

# Module Complete

You have completed **Module 17 — APIs & Data Integration**.

In this module you learned how to:

- retrieve data from APIs  
- authenticate requests  
- parse JSON responses  
- handle pagination and rate limits  
- convert API data into DataFrames  
- build complete API pipelines

---

# Next Module

Next you will begin:

```text
Module 18 — Data Pipelines & Orchestration
```

In this module you will learn how to:

- design **data pipelines**
- schedule automated workflows
- build **ETL pipelines**
- manage production data workflows.