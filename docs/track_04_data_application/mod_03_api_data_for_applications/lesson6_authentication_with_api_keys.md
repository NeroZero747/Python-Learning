# Module 17 — APIs & Data Integration  
## Lesson 6 — Authentication with API Keys

---

# Lesson Objective

By the end of this lesson you will understand:

- Why many APIs require **authentication**
- What an **API key** is
- How to include an API key in API requests
- How to securely store and manage API keys

Authentication ensures that APIs can **control access and monitor usage**.

---

# Overview

Many public APIs allow basic access without authentication, but most professional APIs require credentials.

These credentials typically come in the form of:

```text
API Keys
```

An API key is a unique identifier that allows the API provider to:

- track usage
- control access
- enforce rate limits
- prevent abuse

Example workflow:

```text
Python Script
      ↓
API Request + API Key
      ↓
API Server
      ↓
Authenticated Response
```

Without the API key, the request may fail.

---

# Key Concepts

## What is an API Key?

An API key is a **unique string provided by the API provider** that identifies your application.

Example API key:

```text
abc123xyz789apikey
```

This key is included in API requests.

---

## Why APIs Require Keys

API providers use keys for several reasons.

| Reason | Description |
|------|------|
| Security | Prevent unauthorized access |
| Usage Tracking | Monitor how often APIs are used |
| Rate Limits | Restrict excessive usage |
| Access Control | Restrict certain features |

---

## Where API Keys Are Used

API keys can be included in requests in several ways:

| Method | Example |
|------|------|
| URL Parameter | `?apikey=KEY` |
| HTTP Header | `Authorization: KEY` |
| Request Body | JSON payload |

The exact method depends on the API documentation.

---

# Decision Flow

When using an API:

```text
Does the API require authentication?
        |
       Yes
        |
Retrieve API key from provider
        |
Include API key in request
        |
Send authenticated request
```

Always check the API documentation.

---

# Code Examples

## Example 1 — API Key in URL

Some APIs include the key directly in the URL.

```python
import requests

api_key = "YOUR_API_KEY"

url = f"https://api.example.com/data?apikey={api_key}"

response = requests.get(url)

print(response.status_code)
```

---

## Example 2 — API Key in Headers

Some APIs require the key to be passed in request headers.

```python
import requests

url = "https://api.example.com/data"

headers = {
    "Authorization": "YOUR_API_KEY"
}

response = requests.get(url, headers=headers)

print(response.json())
```

---

## Example 3 — Using API Keys with Parameters

```python
import requests

url = "https://api.example.com/data"

params = {
    "apikey": "YOUR_API_KEY"
}

response = requests.get(url, params=params)

print(response.json())
```

Using `params` automatically constructs the URL query string.

---

# SQL / Excel Comparison

Without APIs:

```text
Download dataset manually
Import into Excel
Update reports manually
```

With authenticated APIs:

```text
Python script
      ↓
API request with authentication
      ↓
Data retrieved automatically
```

This allows automated pipelines to retrieve protected data.

---

# Practice Exercises

## Exercise 1

Tags: Dictionaries, APIs, Authentication

Modify a request to include a parameter called:

```text
apikey
```

Example:

```python
params = {"apikey": "YOUR_KEY"}
```

---

## Exercise 2

Tags: Dictionaries, APIs, Authentication

Send a request with headers.

```python
headers = {"Authorization": "YOUR_KEY"}
```

---

## Exercise 3

Tags: APIs, Authentication, Documentation

Find a public API that requires authentication and review its documentation.

Examples include:

- OpenWeather
- Alpha Vantage
- Google Maps APIs

---

# Common Mistakes

## Mistake 1 — Hardcoding API Keys

Avoid storing API keys directly in scripts.

Example (not recommended):

```python
api_key = "abc123xyz"
```

Instead, store keys in configuration files or environment variables.

---

## Mistake 2 — Sharing API Keys Publicly

API keys should never be shared publicly or committed to Git repositories.

This can expose your account to misuse.

---

## Mistake 3 — Ignoring API Documentation

Different APIs require keys to be passed in different ways.

Always check the documentation.

---

# Real-World Use

Authentication is required for many professional APIs.

Examples include:

---

### Financial Data APIs

Examples:

```text
stock market data
currency exchange rates
financial analytics
```

---

### Cloud Platforms

Examples:

```text
AWS services
Google Cloud APIs
Azure APIs
```

---

### Business Applications

Examples:

```text
CRM systems
marketing platforms
analytics tools
```

---

# Key Idea Cards

### Card 1

API keys authenticate requests and identify your application.

---

### Card 2

API keys may be passed through URLs, headers, or request parameters.

---

### Card 3

API keys should always be stored securely.

---

# Lesson Recap

In this lesson you learned:

- what API keys are  
- why APIs require authentication  
- how to include API keys in requests  
- how to securely manage API credentials

Authentication is an essential component of **professional API integration**.

---

# Next Lesson

Next you will learn:

**Module 17 — Lesson 7: OAuth Authentication**

You will learn how to:

- authenticate with APIs that require OAuth  
- understand tokens and authorization flows  
- connect to modern APIs securely.