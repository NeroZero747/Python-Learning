# Module 17 — APIs & Data Integration  
## Lesson 7 — OAuth Authentication

---

# Lesson Objective

By the end of this lesson you will understand:

- What **OAuth authentication** is  
- Why many modern APIs use OAuth instead of simple API keys  
- How OAuth uses **tokens instead of passwords**  
- How Python applications authenticate with OAuth-enabled APIs

OAuth is commonly used when an API needs **secure access to user accounts or protected resources**.

---

# Overview

In the previous lesson, you learned how APIs use **API keys** to authenticate requests.

However, some APIs require a more secure authentication method called:

```text
OAuth
```

OAuth allows applications to access data **without exposing a user's password**.

Example workflow:

```text
Application
      ↓
OAuth Authorization
      ↓
Access Token
      ↓
API Request
      ↓
Protected Data
```

OAuth is widely used by:

- Google APIs
- GitHub APIs
- Microsoft APIs
- social media platforms
- cloud services

---

# Key Concepts

## What is OAuth?

OAuth (Open Authorization) is an authentication framework that allows applications to access resources on behalf of a user.

Instead of using usernames and passwords, OAuth uses:

```text
Access Tokens
```

These tokens grant temporary permission to access specific data.

---

## OAuth Tokens

An OAuth token is a temporary credential used to access APIs.

Example token:

```text
ya29.a0AfH6SMBExampleToken123
```

Tokens typically expire after a certain time.

This improves security because compromised tokens cannot be used indefinitely.

---

## OAuth Authorization Flow

OAuth typically follows several steps.

Example flow:

```text
User
   ↓
Application requests access
   ↓
User grants permission
   ↓
API issues access token
   ↓
Application uses token for requests
```

This process ensures secure authorization.

---

# Decision Flow

When connecting to an API:

```text
Does the API require authentication?
        |
       Yes
        |
Does the API require OAuth?
        |
       Yes
        |
Obtain access token
        |
Use token in API requests
```

---

# Code Examples

OAuth implementations vary depending on the API provider.

However, the basic pattern is similar.

---

## Example 1 — Using an OAuth Token

Once an access token is obtained, it can be used in API requests.

```python
import requests

url = "https://api.example.com/data"

headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}

response = requests.get(url, headers=headers)

print(response.json())
```

The `Bearer` token authorizes the request.

---

## Example 2 — Accessing Protected Data

```python
import requests

url = "https://api.github.com/user"

headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}

response = requests.get(url, headers=headers)

data = response.json()

print(data)
```

This retrieves user information from the API.

---

# SQL / Excel Comparison

Traditional workflows often require manual access to systems.

Example:

```text
Login to platform
Download data
Import into Excel
Analyze results
```

With OAuth-enabled APIs:

```text
Python script
      ↓
OAuth authentication
      ↓
Authorized API requests
      ↓
Automated data retrieval
```

This allows automated integration with secure systems.

---

# Practice Exercises

## Exercise 1

Tags: APIs, Authentication

Create a request that includes an authorization header.

Example:

```python
headers = {
    "Authorization": "Bearer TOKEN"
}
```

---

## Exercise 2

Tags: Visualization, WHERE, APIs, Authentication

Explore documentation for an OAuth-enabled API.

Examples include:

- GitHub API
- Google APIs
- Microsoft Graph API

Identify where the **access token** is used in requests.

---

## Exercise 3

Tags: Tuples, APIs, HTTP Methods, Authentication

Modify an API request to include a token in the headers.

```python
response = requests.get(url, headers=headers)
```

---

# Common Mistakes

## Mistake 1 — Confusing API Keys with OAuth Tokens

API keys identify an application.

OAuth tokens authorize access to user data.

These two authentication methods serve different purposes.

---

## Mistake 2 — Not Refreshing Expired Tokens

OAuth tokens often expire.

Applications must refresh tokens when they expire.

---

## Mistake 3 — Hardcoding Tokens in Code

Never store tokens directly in scripts.

Instead use:

- environment variables
- secure credential storage

---

# Real-World Use

OAuth authentication is widely used across modern platforms.

Examples include:

---

### Cloud Services

Examples:

```text
Google Cloud APIs
Microsoft Graph API
AWS services
```

---

### Developer Platforms

Examples:

```text
GitHub API
GitLab API
Bitbucket API
```

---

### Social Media APIs

Examples:

```text
Twitter API
Facebook API
LinkedIn API
```

---

# Key Idea Cards

### Card 1

OAuth allows applications to access data without exposing user passwords.

---

### Card 2

OAuth uses **access tokens** instead of credentials.

---

### Card 3

OAuth tokens are typically **temporary and expire for security reasons**.

---

# Lesson Recap

In this lesson you learned:

- what OAuth authentication is  
- how OAuth tokens authorize API requests  
- how applications securely access protected APIs  
- how OAuth differs from API key authentication

OAuth is commonly used by **modern cloud platforms and secure APIs**.

---

# Next Lesson

Next you will learn:

**Module 17 — Lesson 8: Handling Pagination in APIs**

You will learn how to:

- retrieve large datasets from APIs  
- handle APIs that return results in multiple pages  
- build scripts that automatically retrieve complete datasets.