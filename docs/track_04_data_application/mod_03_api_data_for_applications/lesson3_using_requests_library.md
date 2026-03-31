# Module 17 — APIs & Data Integration  
## Lesson 3 — Using the Python `requests` Library

---

# Lesson Objective

By the end of this lesson you will understand:

- What the **`requests` library** is  
- How Python sends API requests using `requests`  
- How to retrieve and inspect API responses  
- How to convert API responses into usable Python data structures

The `requests` library is the **most common tool for interacting with APIs in Python**.

---

# Overview

In the previous lesson you learned how **HTTP requests** allow applications to communicate with APIs.

Python needs a library that can send these requests.

The most commonly used library for this is:

```python
requests
```

The `requests` library simplifies sending HTTP requests and receiving responses.

Example workflow:

```text
Python Script
      ↓
requests library
      ↓
API Request
      ↓
API Server
      ↓
Response returned
```

This allows Python programs to **retrieve data from web services automatically**.

---

# Key Concepts

## The `requests` Library

The `requests` library allows Python to send HTTP requests.

Common request types include:

| Request | Purpose |
|------|------|
| GET | Retrieve data |
| POST | Send data |
| PUT | Update data |
| DELETE | Remove data |

Most analytics workflows primarily use:

```text
GET requests
```

Because analysts typically **retrieve data from APIs**.

---

## Installing the `requests` Library

If the library is not installed, it can be installed using `pip`.

```bash
pip install requests
```

This makes the library available for Python scripts.

---

## Importing the Library

Once installed, the library can be imported into Python.

```python
import requests
```

---

# Decision Flow

When retrieving data from an API:

```text
Do you need data from an external service?
        |
       Yes
        |
Use the requests library
        |
Send HTTP request
        |
Receive API response
```

---

# Code Examples

## Example 1 — Basic API Request

```python
import requests

url = "https://api.github.com"

response = requests.get(url)

print(response.status_code)
```

This sends a request to the GitHub API and prints the response status.

---

## Example 2 — Viewing Response Content

```python
import requests

url = "https://api.github.com"

response = requests.get(url)

print(response.text)
```

The `text` attribute returns the raw response content.

---

## Example 3 — Working with JSON Responses

Many APIs return JSON data.

```python
import requests

url = "https://api.github.com"

response = requests.get(url)

data = response.json()

print(data)
```

The `.json()` method converts the response into a Python dictionary.

---

## Example 4 — Extracting Values from API Data

```python
import requests

url = "https://api.github.com"

response = requests.get(url)

data = response.json()

print(data["current_user_url"])
```

This accesses a specific field from the JSON response.

---

# SQL / Excel Comparison

Traditional workflow without APIs:

```text
Login to website
Download CSV
Import into Excel
Analyze data
```

Python API workflow:

```text
Python script
      ↓
API request
      ↓
Data returned
      ↓
Load into DataFrame
```

This allows automated data pipelines.

---

# Practice Exercises

## Exercise 1

Tags: print(), requests, Imports, APIs

Send a GET request to the GitHub API.

```python
import requests

response = requests.get("https://api.github.com")

print(response.status_code)
```

---

## Exercise 2

Tags: print(), JSON, APIs

Convert the response into JSON.

```python
data = response.json()

print(data)
```

---

## Exercise 3

Tags: print(), Lists, APIs

Extract a specific field from the JSON data.

Example:

```python
print(data["current_user_url"])
```

---

# Common Mistakes

## Mistake 1 — Forgetting to Check Status Codes

Always verify that the request succeeded.

Example:

```python
if response.status_code == 200:
    print("Request successful")
```

---

## Mistake 2 — Assuming All Responses Are JSON

Some APIs return:

- text
- XML
- files

Always verify the format before calling `.json()`.

---

## Mistake 3 — Not Handling Connection Errors

API requests can fail due to network problems.

Scripts should include error handling.

---

# Real-World Use

The `requests` library is widely used in modern data systems.

Examples include:

---

### Data Integration

Python scripts retrieve data from external services such as:

```text
financial market data
CRM platforms
marketing analytics tools
```

---

### Data Pipelines

Many ETL pipelines retrieve data from APIs before processing it.

Example:

```text
API → Data Processing → Database → Dashboard
```

---

### Automation

Automation systems regularly call APIs to refresh data or trigger processes.

---

# Key Idea Cards

### Card 1

The `requests` library allows Python to send HTTP requests.

---

### Card 2

GET requests retrieve data from APIs.

---

### Card 3

The `.json()` method converts API responses into Python dictionaries.

---

# Lesson Recap

In this lesson you learned:

- how the `requests` library works  
- how Python sends API requests  
- how to retrieve API responses  
- how to convert responses into Python data structures

The `requests` library is the **primary tool used to interact with APIs in Python**.

---

# Next Lesson

Next you will learn:

**Module 17 — Lesson 4: Working with JSON Data**

You will learn how to:

- understand JSON structures  
- parse JSON data  
- convert JSON data into Python objects and DataFrames.