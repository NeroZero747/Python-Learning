# Module 17 — APIs & Data Integration  
## Lesson 9 — Handling API Rate Limits

---

# Lesson Objective

By the end of this lesson you will understand:

- What **API rate limits** are  
- Why APIs enforce usage limits  
- How to detect rate limit errors  
- How to implement delays and retries in Python scripts

Handling rate limits correctly is important for building **reliable API integrations**.

---

# Overview

Most APIs restrict how many requests can be sent within a specific time period.

This restriction is called a:

```text
Rate Limit
```

Example limits:

| API | Rate Limit |
|------|------|
| API A | 100 requests per minute |
| API B | 1,000 requests per hour |
| API C | 10 requests per second |

If your script sends too many requests, the API may return an error.

Example response:

```text
429 Too Many Requests
```

Proper scripts must **respect rate limits** and slow down when necessary.

---

# Key Concepts

## What is a Rate Limit?

A rate limit is a restriction on how many API requests can be made during a defined time window.

Example:

```text
100 requests per minute
```

This prevents systems from being overloaded by excessive traffic.

---

## Why APIs Use Rate Limits

APIs enforce rate limits to protect system performance.

| Reason | Description |
|------|------|
| Stability | Prevents server overload |
| Fairness | Ensures all users receive access |
| Security | Protects against abuse |

Rate limits are especially important for **public APIs**.

---

## Detecting Rate Limit Errors

When a rate limit is exceeded, the API typically returns an HTTP status code.

Common example:

```text
429 Too Many Requests
```

Your script should detect and handle this condition.

---

# Decision Flow

When sending API requests:

```text
Send API request
        ↓
Check response status
        ↓
Did request succeed?
        |
      Yes → Continue
        |
      No
        ↓
Check if rate limit exceeded
        ↓
Wait before retrying request
```

This process ensures scripts do not overwhelm APIs.

---

# Code Examples

## Example 1 — Checking Status Codes

```python
import requests

url = "https://api.example.com/data"

response = requests.get(url)

if response.status_code == 200:
    print("Request successful")

elif response.status_code == 429:
    print("Rate limit exceeded")
```

---

## Example 2 — Adding a Delay Between Requests

Python can pause execution between requests.

```python
import time
import requests

url = "https://api.example.com/data"

for i in range(5):

    response = requests.get(url)

    print(response.status_code)

    time.sleep(2)
```

This script waits **2 seconds between requests**.

---

## Example 3 — Retry Logic

Scripts can retry requests when rate limits occur.

```python
import time
import requests

url = "https://api.example.com/data"

while True:

    response = requests.get(url)

    if response.status_code == 200:
        break

    elif response.status_code == 429:
        print("Rate limit reached. Waiting...")
        time.sleep(10)
```

This script waits before retrying the request.

---

# SQL / Excel Comparison

Without APIs:

```text
Download file manually
Update report
```

With APIs:

```text
Python script
      ↓
Multiple API requests
      ↓
Rate limits must be respected
```

Proper handling ensures stable automated workflows.

---

# Practice Exercises

## Exercise 1

Tags: range(), Loops, Iteration, APIs

Send multiple API requests in a loop.

Example:

```python
for i in range(5):
```

---

## Exercise 2

Tags: APIs, Rate Limiting

Add a delay between requests.

Example:

```python
time.sleep(2)
```

---

## Exercise 3

Tags: Conditionals, APIs, Scripts, Arithmetic

Modify a script to detect status code **429**.

Example:

```python
if response.status_code == 429:
```

---

# Common Mistakes

## Mistake 1 — Ignoring Rate Limits

Sending too many requests may cause the API to block your IP address.

---

## Mistake 2 — Not Adding Delays

Scripts that request pages too quickly may exceed rate limits.

---

## Mistake 3 — Not Implementing Retry Logic

Temporary rate limits should be handled with retries.

---

# Real-World Use

Rate limits are common in many APIs.

Examples include:

---

### Financial APIs

Examples:

```text
stock market data
cryptocurrency exchanges
financial analytics platforms
```

These systems often restrict requests per second.

---

### Cloud APIs

Examples:

```text
AWS services
Google Cloud APIs
Azure APIs
```

These platforms enforce strict usage quotas.

---

### Data Pipelines

Pipelines that retrieve large datasets must manage request frequency carefully.

Example pipeline:

```text
API Requests → Rate Limit Handling → Data Processing
```

---

# Key Idea Cards

### Card 1

Rate limits restrict how many API requests can be made within a time window.

---

### Card 2

Status code **429** indicates too many requests.

---

### Card 3

Scripts should include delays and retry logic.

---

# Lesson Recap

In this lesson you learned:

- what API rate limits are  
- why APIs restrict request frequency  
- how to detect rate limit errors  
- how to implement delays and retry logic

Proper rate limit handling is essential for **stable API integrations**.

---

# Next Lesson

Next you will learn:

**Module 17 — Lesson 10: Loading API Data into Pandas**

You will learn how to:

- convert API responses into DataFrames  
- prepare API data for analysis  
- integrate API data into Python data workflows.