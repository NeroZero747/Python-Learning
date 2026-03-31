# Module 17 — APIs & Data Integration  
## Lesson 1 — What is an API?

---

# Lesson Objective

By the end of this lesson you will understand:

- What an **API (Application Programming Interface)** is  
- Why APIs are commonly used in modern data systems  
- How APIs allow programs to communicate with other systems  
- How Python retrieves data from APIs

APIs are one of the most common ways modern applications **exchange data**.

---

# Overview

Most modern applications expose their data through **APIs**.

Instead of downloading files manually, systems communicate directly with each other.

Examples include:

- retrieving weather data
- pulling financial market prices
- accessing company databases
- retrieving analytics metrics
- integrating with business applications

For example:

```text
Python Script
      ↓
API Request
      ↓
Remote Server
      ↓
JSON Data Response
```

This allows Python programs to automatically retrieve live data.

---

# Key Concepts

## What is an API?

An API (Application Programming Interface) allows two software systems to communicate.

It acts as a **bridge between applications**.

Example:

```text
Python program → API → Data service
```

Instead of accessing a database directly, the program requests information through the API.

---

## Real-World Example

When you open a weather app on your phone:

```text
Weather App
      ↓
Weather API
      ↓
Weather Data Server
```

The API sends weather information back to the application.

---

## APIs Return Data

Most APIs return data in structured formats such as:

```text
JSON
XML
```

JSON is the most common format used today.

Example JSON response:

```json
{
  "city": "Los Angeles",
  "temperature": 72,
  "conditions": "Sunny"
}
```

Python can easily convert this into data structures.

---

# Decision Flow

Use APIs when:

```text
Do you need data from an external system?
        |
       Yes
        |
Does the system provide an API?
        |
       Yes
        |
Use Python to retrieve data from the API
```

APIs are often used instead of:

- manual downloads
- file transfers
- manual database exports

---

# Code Examples

## Example 1 — API Request with Python

Python uses libraries to send HTTP requests.

The most common library is:

```python
requests
```

Example:

```python
import requests

url = "https://api.example.com/data"

response = requests.get(url)

print(response.status_code)
print(response.text)
```

This sends a request to the API and prints the response.

---

## Example 2 — Reading JSON from an API

Many APIs return JSON.

Example:

```python
import requests

url = "https://api.example.com/data"

response = requests.get(url)

data = response.json()

print(data)
```

This converts the JSON response into a Python dictionary.

---

# SQL / Excel Comparison

Without APIs, analysts often rely on manual downloads.

Example workflow:

```text
Log into website
Download CSV file
Import into Excel
Process data
```

With APIs:

```text
Python script
     ↓
API request
     ↓
Data returned automatically
```

This allows fully automated data retrieval.

---

# Practice Exercises

## Exercise 1

Tags: Missing Data, APIs

Identify three services that provide APIs.

Examples might include:

- weather services
- financial market data
- social media platforms

---

## Exercise 2

Tags: print(), requests, Imports, APIs

Install the `requests` library and send a test API request.

Example:

```python
import requests

response = requests.get("https://api.github.com")

print(response.status_code)
```

---

## Exercise 3

Tags: SELECT, APIs

Find a public API and retrieve data using Python.

Examples include:

- OpenWeather API
- NASA API
- GitHub API

---

# Common Mistakes

## Mistake 1 — Not Checking API Status Codes

Always check if the request succeeded.

Example:

```python
if response.status_code == 200:
    print("Request successful")
```

---

## Mistake 2 — Ignoring API Rate Limits

Many APIs restrict how many requests can be sent.

Sending too many requests may cause the API to block access.

---

## Mistake 3 — Not Handling Errors

API requests can fail due to:

- network issues
- invalid URLs
- authentication problems

Scripts should handle these cases.

---

# Real-World Use

APIs are used extensively in modern data systems.

Examples include:

---

### Data Integration

Companies use APIs to integrate systems such as:

```text
CRM systems
Financial platforms
Marketing analytics tools
```

---

### Data Pipelines

Automation pipelines often retrieve data from APIs before processing it.

Example:

```text
API → Data Processing → Database → Dashboard
```

---

### Analytics Platforms

Many analytics tools expose APIs for retrieving metrics and reports.

---

# Key Idea Cards

### Card 1

APIs allow software systems to communicate and exchange data.

---

### Card 2

Python programs can retrieve data from APIs using HTTP requests.

---

### Card 3

Most modern APIs return data in **JSON format**.

---

# Lesson Recap

In this lesson you learned:

- what an API is
- how applications communicate through APIs
- how Python retrieves data from APIs
- why APIs are important for modern data workflows

APIs are a foundational component of **modern data integration and automation systems**.

---

# Next Lesson

Next you will learn:

**Module 17 — Lesson 2: Understanding HTTP Requests**

This lesson will explain:

- how API communication works
- HTTP request methods
- how data is transmitted between systems.