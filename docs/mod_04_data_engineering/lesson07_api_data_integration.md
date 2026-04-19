# Lesson 07 — API Data Integration with Python

**Track:** Data Engineering for Analysts  
**Module:** Module 3 — Data Collection  
**Difficulty:** Beginner → Intermediate | **Duration:** 14 min  
**Sources:** M3-L01 (What Is an API?) · M3-L02 (HTTP Requests) · M3-L03 (Python Requests Library) · M3-L04 (Working with JSON) · M3-L05 (Parsing API Responses) · M3-L06 (Auth with API Keys) · M3-L07 (OAuth — trimmed) · M3-L08 (Pagination) · M3-L09 (Rate Limits) · M3-L10 (Loading API Data into Pandas — closing section)

---

## Learning Objectives

1. **API mental model** — Explain what an API endpoint is, what a request/response cycle looks like, and what JSON is.
2. **Make requests with Python** — Use the `requests` library to call a REST API and handle the response.
3. **Authentication** — Add API keys to headers and understand the basic concept of OAuth.
4. **Resilience patterns** — Handle pagination, rate limits, and network errors without crashing the pipeline.
5. **Load into a DataFrame** — Convert a full paginated API response into a clean pandas DataFrame.

> By the end of this lesson you'll be able to build a complete API data collection script that handles real-world complications.

---

## Overview

### Hook
Almost every modern data source — Salesforce, Stripe, Google Analytics, Jira, Slack, weather services, financial data — exposes its data through an API. If you can call APIs from Python, you can build pipelines that pull fresh data from any of them.

### Analogy: The Restaurant Menu System
Think of an API like a restaurant's ordering system. The **menu** (API documentation) lists everything available. You place an **order** (HTTP request) by telling the waiter what you want, including any special instructions (parameters). The kitchen processes it and the waiter brings back your **order** (the response) in a standard container (JSON). You don't need to know how the kitchen works — just what to order and how to read the menu.

| API Concept | Restaurant Analogy |
|------------|-------------------|
| **Endpoint** | A specific menu item — it has a name and price (URL and method) |
| **Request** | Placing your order — you specify what you want |
| **Response** | The dish that arrives — structured data in a predictable format |
| **API key** | Your membership card — proves you're allowed to order |
| **Rate limit** | "One at a time, please" — the kitchen can only handle so many orders |

> **Key takeaway:** An API is just a formalized way to request data from a remote system. Once you understand the pattern, every API works the same way.

---

## Key Takeaways

### 1. REST APIs Speak HTTP and Return JSON
The vast majority of data APIs are REST APIs — they accept standard HTTP methods (GET to fetch, POST to create) and return responses in JSON format. JSON is essentially a Python dictionary — once you parse it with `response.json()`, it's just nested dicts and lists.  
**Keywords:** REST · HTTP GET · JSON · response.json()

### 2. Pagination Means Data Arrives in Pages
APIs rarely return all results at once. A search for 10,000 orders might come back 100 at a time across 100 pages. Your pipeline must follow pagination links (or increment page numbers) until all data is collected, or you'll silently miss records.  
**Keywords:** Pagination · next_page · while loop · complete collection

### 3. Rate Limits Are Enforced — Handle Them Gracefully
Every API restricts how many requests you can make per minute or per day. Exceeding the limit returns a 429 Too Many Requests error. A resilient pipeline waits (using the `Retry-After` header or exponential backoff) rather than crashing.  
**Keywords:** Rate limit · 429 status · time.sleep() · Retry-After · Backoff

---

## Key Concepts

### HTTP Request/Response Cycle
```python
import requests

# A GET request to an API endpoint
response = requests.get(
    url="https://api.example.com/orders",   # the endpoint
    params={"status": "completed"},          # query parameters (?status=completed)
    headers={"Authorization": "Bearer TOKEN"}  # authentication
)

# Check if the request succeeded
print(response.status_code)   # 200 = success, 404 = not found, 429 = rate limited

# Parse the JSON response into a Python dictionary
data = response.json()
print(type(data))   # <class 'dict'> or <class 'list'>
```

### Common HTTP Status Codes
| Code | Meaning | Action |
|------|---------|--------|
| `200 OK` | Request succeeded | Parse the response |
| `201 Created` | Resource created (POST) | Continue |
| `400 Bad Request` | Your request had errors | Check parameters |
| `401 Unauthorized` | Missing or invalid credentials | Check API key |
| `404 Not Found` | Endpoint or resource doesn't exist | Check URL |
| `429 Too Many Requests` | Rate limit exceeded | Wait and retry |
| `500 Server Error` | The API has a problem | Retry with backoff |

### API Key Authentication
```python
# Method 1: API key in headers (most common)
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}
response = requests.get(url, headers=headers)

# Method 2: API key as a query parameter
response = requests.get(url, params={"api_key": "YOUR_API_KEY"})
```

### OAuth in Brief
OAuth is a protocol that lets users grant your application access to their accounts without sharing their password. The common pattern:
1. Your app redirects the user to the provider's login page
2. The user approves access
3. The provider returns a temporary `access_token`
4. Your app uses that token in API headers (same as an API key bearer token)

For most data engineering tasks, you'll use a service account with a long-lived API key, not interactive OAuth flows.

---

## Code Examples

### Example 1: Basic GET request with error checking
```python
import requests

API_KEY = "your_api_key_here"
BASE_URL = "https://api.example.com"

def get_orders(status: str = "completed") -> list:
    """Fetch orders from the API with basic error handling."""
    response = requests.get(
        url=f"{BASE_URL}/orders",
        params={"status": status, "limit": 100},
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=10   # fail after 10 seconds instead of hanging forever
    )

    # Raise an exception for 4xx and 5xx status codes
    response.raise_for_status()

    return response.json()["orders"]

orders = get_orders()
print(f"Retrieved {len(orders)} orders")
```

### Example 2: Handling all pages of a paginated API
```python
import requests, time

def get_all_orders(api_key: str) -> list:
    """Collect every order across all pages."""
    all_orders = []
    page = 1

    while True:
        response = requests.get(
            url="https://api.example.com/orders",
            params={"page": page, "per_page": 100},
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        orders = data.get("orders", [])
        all_orders.extend(orders)

        # Check if there are more pages
        if not data.get("has_next_page", False):
            break            # no more pages — we're done
        
        page += 1
        time.sleep(0.2)      # small pause between requests (polite and safe)

    print(f"Collected {len(all_orders)} total orders across {page} pages")
    return all_orders
```

### Example 3: Rate limit handling with retry logic
```python
import requests, time

def request_with_retry(url: str, headers: dict, max_retries: int = 3) -> dict:
    """Make a request and retry on rate limit or server errors."""
    for attempt in range(max_retries):
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 429:
            # Rate limited — respect the Retry-After header if present
            wait = int(response.headers.get("Retry-After", 60))
            print(f"Rate limited. Waiting {wait}s before retry...")
            time.sleep(wait)

        elif response.status_code >= 500:
            # Server error — exponential backoff
            wait = 2 ** attempt   # 1s, 2s, 4s
            print(f"Server error {response.status_code}. Retrying in {wait}s...")
            time.sleep(wait)

        else:
            # Client error (4xx) — don't retry
            response.raise_for_status()

    raise RuntimeError(f"Request failed after {max_retries} attempts")
```

### Example 4: Full pipeline — API → pandas DataFrame
```python
import requests, pandas as pd, os, time

def fetch_all_pages(api_key: str) -> list:
    """Retrieve all order records with pagination."""
    all_records, page = [], 1
    while True:
        resp = requests.get(
            "https://api.example.com/orders",
            params={"page": page, "per_page": 200},
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=10
        )
        resp.raise_for_status()
        data = resp.json()
        all_records.extend(data["orders"])
        if not data.get("has_next_page"):
            break
        page += 1
        time.sleep(0.1)
    return all_records

def normalize_orders(records: list) -> pd.DataFrame:
    """Flatten nested JSON records into a clean DataFrame."""
    df = pd.json_normalize(records)            # handles nested dicts
    df["created_at"] = pd.to_datetime(df["created_at"])
    df["amount"] = df["amount"].astype("float32")
    df["region"] = df["region"].astype("category")
    return df[["order_id", "created_at", "amount", "region", "status"]]

# Run it
api_key = os.environ["ORDERS_API_KEY"]       # never hard-code credentials
records  = fetch_all_pages(api_key)
df       = normalize_orders(records)

print(df.shape)
print(df.dtypes)
print(df.head())
```
**Terminal output:**
```
(8420, 5)
order_id       int32
created_at    datetime64[ns]
amount        float32
region        category
status        object
             order_id created_at  amount region    status
0           1001  2024-01-03   129.99   EMEA completed
```

---

## Common Mistakes

### Mistake 1: Not checking status codes before parsing
```python
# WRONG — crashes with a JSON decode error if the response is an HTML error page
data = response.json()["orders"]

# RIGHT — check status first
response.raise_for_status()          # raises on 4xx/5xx
data = response.json()["orders"]
```

### Mistake 2: Stopping at page 1 (missing data silently)
```python
# WRONG — only fetches the first 100 records out of potentially thousands
response = requests.get(url, params={"page": 1, "per_page": 100})
orders = response.json()["orders"]
# Pipeline loads 100 rows but the source has 10,000 — no error, just missing data

# RIGHT — always follow pagination until has_next_page is False
```

### Mistake 3: Hard-coding API keys in source code
```python
# WRONG — key is visible in git history forever
API_KEY = "sk_live_abc123..."

# RIGHT — read from environment variable
import os
API_KEY = os.environ["MY_API_KEY"]
```

### Mistake 4: No timeout on requests
```python
# WRONG — can hang forever if the server doesn't respond
response = requests.get(url)

# RIGHT — always set a timeout (in seconds)
response = requests.get(url, timeout=10)
```

---

## Practice Exercises

### Exercise 1 — Your first API call
```python
import requests

# The Open-Meteo API is free and requires no API key
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 51.51,            # London
    "longitude": -0.13,
    "current_weather": True
}

# TODO: Make the GET request
# TODO: Check the status code
# TODO: Parse the JSON and print the current temperature
```

### Exercise 2 — Paginated collection
```python
import requests

# JSONPlaceholder is a free mock REST API
def get_all_posts():
    # The /posts endpoint returns 100 posts on one page,
    # but in a real API there might be multiple pages.
    # TODO: Fetch all posts from https://jsonplaceholder.typicode.com/posts
    # TODO: Print how many posts were returned
    # TODO: Load them into a pandas DataFrame
    pass
```

### Exercise 3 — Retry on failure
```python
# TODO: Write a function that:
# 1. Accepts a URL and headers
# 2. Makes a GET request
# 3. If status is 429, waits 5 seconds and retries (up to 3 times)
# 4. If status is 200, returns the JSON
# 5. For anything else, raises an exception with the status code
```

---

## Lesson Recap

1. **REST APIs** accept HTTP requests and return JSON responses — once you understand the pattern (endpoint + method + params + headers), every API behaves the same way.
2. **Authentication** is usually an API key sent in the `Authorization` header — never hard-code keys in source code; use environment variables.
3. **Pagination** means data is split across multiple pages — always follow all pages or you'll silently miss records.
4. **Rate limits** are enforced with 429 errors — respect `Retry-After` headers and use exponential backoff to build resilient pipelines.
5. **`pd.json_normalize()`** flattens nested JSON structures into a clean flat DataFrame, handling nested dicts automatically.

---

## Knowledge Check

**Q1.** An API call returns status code 429. What does this mean and how should your pipeline respond?  
**Answer:** 429 means the rate limit has been exceeded. The pipeline should check the `Retry-After` response header for how long to wait, sleep for that duration (or use exponential backoff), then retry the request.

**Q2.** You call an API that says it returns "up to 100 results per page" and your first response has exactly 100 results. What should you do next?  
**Answer:** Request the next page. An API returning exactly the page limit is a strong signal that more pages exist. Always check the pagination indicator (`has_next_page`, `next_cursor`, or similar) and continue requesting until the signal is false.

**Q3.** What Python function flattens a nested JSON structure like `{"customer": {"name": "Alice", "id": 1}}` into a flat DataFrame with columns `customer.name` and `customer.id`?  
**Answer:** `pd.json_normalize()` — it handles arbitrary nesting levels and creates dot-separated column names by default.

---

## Next Lesson
**Lesson 08 — Data Quality & Validation**  
You can now collect data from anywhere. But raw data is almost always messy — nulls, wrong types, duplicate records, schema drift. In this lesson you'll build the validation layer that catches bad data before it corrupts your downstream reports.
