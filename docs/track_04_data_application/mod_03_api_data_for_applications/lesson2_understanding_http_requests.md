# Module 17 — APIs & Data Integration  
## Lesson 2 — Understanding HTTP Requests

---

# Lesson Objective

By the end of this lesson you will understand:

- What **HTTP requests** are  
- How applications communicate over the internet  
- The most common **HTTP request methods** used by APIs  
- How Python sends HTTP requests to retrieve data

Understanding HTTP is essential because **all web APIs communicate using HTTP**.

---

# Overview

When a Python script interacts with an API, it sends an **HTTP request** to a server.

The server processes the request and sends back a **response**.

Example workflow:

```text
Python Script
      ↓
HTTP Request
      ↓
API Server
      ↓
HTTP Response
      ↓
Python Script Receives Data
```

This communication model is called a **client–server architecture**.

- The **client** sends the request (Python program)
- The **server** processes the request and returns data (API)

---

# Key Concepts

## HTTP (Hypertext Transfer Protocol)

HTTP is the protocol used for communication between web clients and servers.

Every time you open a website, your browser sends an HTTP request.

Example:

```text
Browser → HTTP Request → Web Server
```

The server responds with data such as:

- HTML
- images
- JSON data

APIs use the same mechanism.

---

## HTTP Request Structure

An HTTP request typically contains:

```text
Request Method
URL
Headers
Body (optional)
```

Example:

```text
GET https://api.example.com/users
```

This tells the server to return user data.

---

## HTTP Response Structure

The server responds with:

```text
Status Code
Headers
Response Body
```

Example response:

```text
Status Code: 200
Response Body: JSON data
```

Python then processes the returned data.

---

# Common HTTP Methods

APIs use several HTTP methods depending on the operation.

| Method | Purpose |
|------|------|
| GET | Retrieve data |
| POST | Send data to server |
| PUT | Update existing data |
| DELETE | Remove data |

For data analysis workflows, the most common method is:

```text
GET
```

Because analysts typically **retrieve data from APIs**.

---

# Decision Flow

When interacting with an API:

```text
Do you need data from the server?
        |
       Yes
        |
Use GET request
```

If you need to send data to the server:

```text
Use POST request
```

---

# Code Examples

## Example 1 — Sending a GET Request

```python
import requests

url = "https://api.github.com"

response = requests.get(url)

print(response.status_code)
```

This sends a request to the GitHub API.

---

## Example 2 — Viewing the Response

```python
import requests

url = "https://api.github.com"

response = requests.get(url)

print(response.text)
```

The response contains data returned by the server.

---

## Example 3 — Reading JSON Response

Most APIs return JSON data.

```python
import requests

url = "https://api.github.com"

response = requests.get(url)

data = response.json()

print(data)
```

This converts the API response into a Python dictionary.

---

# SQL / Excel Comparison

Without APIs:

```text
Login to system
Export CSV file
Download file
Load into Excel
```

With APIs:

```text
Python Script
      ↓
API Request
      ↓
Data retrieved automatically
```

This allows automated data retrieval for pipelines and reports.

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

Tags: print(), JSON, APIs, HTTP Methods

Print the returned JSON data.

```python
data = response.json()

print(data)
```

---

## Exercise 3

Tags: Error Handling, APIs, HTTP Methods

Try sending requests to different public APIs such as:

- NASA API
- OpenWeather API
- GitHub API

---

# Common Mistakes

## Mistake 1 — Ignoring Status Codes

Always check if the request succeeded.

Example:

```python
if response.status_code == 200:
    print("Success")
```

---

## Mistake 2 — Assuming All APIs Return JSON

Some APIs return:

- XML
- plain text
- binary files

Always check the response format.

---

## Mistake 3 — Sending Too Many Requests

APIs often limit request frequency.

This is called a **rate limit**.

Sending too many requests may block access.

---

# Real-World Use

HTTP requests power most modern applications.

Examples include:

---

### Data Integration

Applications communicate through APIs using HTTP requests.

Examples include:

```text
CRM systems
financial platforms
marketing analytics tools
```

---

### Data Pipelines

Many pipelines retrieve data through APIs.

Example pipeline:

```text
API Request → Data Processing → Database Storage
```

---

### Analytics Platforms

Analytics tools often provide APIs for retrieving reports and metrics.

---

# Key Idea Cards

### Card 1

HTTP is the protocol used for communication between clients and servers.

---

### Card 2

API requests are sent using HTTP methods such as **GET**.

---

### Card 3

The server responds with a **status code and data**.

---

# Lesson Recap

In this lesson you learned:

- how HTTP requests work  
- how clients communicate with servers  
- common HTTP methods used by APIs  
- how Python sends requests using the `requests` library

HTTP requests are the **foundation of API communication**.

---

# Next Lesson

Next you will learn:

**Module 17 — Lesson 3: Using the Python `requests` Library**

You will learn how to:

- install and use the `requests` library  
- send API requests  
- process responses efficiently.