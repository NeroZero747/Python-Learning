# Module 11 — Python Engineering Handbook

# Lesson 5 — Secure Credential Handling

---

# Lesson Objective

By the end of this lesson learners will understand:

• why **credentials must be protected** in software systems  
• how developers store secrets securely  
• how **environment variables** are used for credentials  
• how secret management tools are used in production environments  

Secure credential handling is critical because applications often require access to **databases, APIs, and cloud services**, and exposing credentials can lead to serious security risks.

---

# Overview

Most applications must connect to external services.

Examples include:

```text
Databases
Cloud storage
External APIs
Authentication systems
```

These connections require **credentials** such as:

```text
Passwords
API keys
Access tokens
Private keys
```

A common beginner mistake is storing credentials directly in code.

Example (bad practice):

```python
db_password = "my_password123"
```

This approach is dangerous because:

• credentials may be exposed in version control  
• secrets may be leaked to unauthorized users  
• changing credentials becomes difficult.

Professional applications store credentials **outside the source code**.

Example secure approach:

```text
Application starts
       ↓
Reads credentials from environment variables
       ↓
Uses credentials to connect to services
```

This protects sensitive information.

---

# Key Idea Cards (3 Cards)

### Credentials Should Never Be Hardcoded

Sensitive information should not appear directly in code.

Bad example:

```python
password = "secret123"
```

Better approach:

```python
password = os.getenv("DB_PASSWORD")
```

Secrets should be stored externally.

---

### Environment Variables Store Secrets

Environment variables allow credentials to be stored outside code.

Example variables:

```text
DB_HOST
DB_USER
DB_PASSWORD
API_KEY
```

Applications read these variables during runtime.

---

### Secret Managers Improve Security

Large organizations use secret management systems.

Examples include:

```text
AWS Secrets Manager
Azure Key Vault
HashiCorp Vault
Google Secret Manager
```

These systems store credentials securely and provide controlled access.

---

# Key Concepts

## Environment Variables

Environment variables allow applications to access credentials securely.

Example variable:

```text
DB_PASSWORD=super_secure_password
```

Python can read environment variables at runtime.

---

## Configuration Files

Some systems store credentials in configuration files.

Example `.env` file:

```text
DB_HOST=localhost
DB_USER=analytics_user
DB_PASSWORD=secure_password
```

This file should never be committed to version control.

---

## Secret Managers

Secret managers store and control access to sensitive credentials.

Example workflow:

```text
Application requests secret
        ↓
Secret manager authenticates request
        ↓
Credential returned securely
```

This ensures credentials remain protected.

---

# Decision Flow

Developers typically manage credentials using this workflow:

```text
Does the application require credentials?
        ↓
       YES
        ↓
Store secrets outside code
        ↓
Use environment variables or secret manager
```

This approach protects sensitive information.

---

# Code Examples

### Example 1 — Hardcoded Credential (Bad Practice)

```python
db_password = "mypassword123"
```

Problems:

• exposed credentials  
• security risk  
• difficult to rotate secrets.

---

### Example 2 — Environment Variable Credential

```python
import os

db_password = os.getenv("DB_PASSWORD")
```

The password is stored outside the application code.

---

### Example 3 — Using python-dotenv

Install library:

```bash
pip install python-dotenv
```

Example `.env` file:

```text
DB_PASSWORD=secure_password
API_KEY=my_api_key
```

Python code:

```python
from dotenv import load_dotenv
import os

load_dotenv()

db_password = os.getenv("DB_PASSWORD")
```

---

### Example 4 — Secure Database Connection

```python
import os
import psycopg2

connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database="analytics"
)
```

Credentials are loaded securely from environment variables.

---

# SQL / Excel Comparison

Credential security also appears in other systems.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| credential storage | environment variables | database authentication | workbook passwords |
| secret protection | secret managers | credential vaults | file permissions |
| authentication | API tokens | database login | user access control |

Example SQL authentication:

```text
Username
Password
Database permissions
```

These credentials must be protected just like Python credentials.

---

# Practice Exercises

### Exercise 1

Tags: Environment Variables, Variables, Secrets Management

Create an environment variable.

Example:

```text
API_KEY=my_secure_key
```

---

### Exercise 2

Tags: os Module, Imports, HTTP Methods, Variables

Write Python code that reads the variable.

```python
import os

api_key = os.getenv("API_KEY")
```

---

### Exercise 3

Tags: Environment Variables, Secrets Management

Create a `.env` file and load it using `python-dotenv`.

---

### Exercise 4

Tags: Environment Variables, Deployment, Secrets Management

Research a cloud secret manager such as:

```text
AWS Secrets Manager
Azure Key Vault
Google Secret Manager
```

Understand how they protect credentials.

---

# Common Mistakes

### Committing Credentials to Git

Never commit files containing secrets.

Example files to ignore:

```text
.env
credentials.json
config/secrets.yaml
```

Use `.gitignore` to prevent accidental commits.

---

### Sharing Credentials Between Developers

Each developer should have separate credentials whenever possible.

Shared credentials reduce accountability and security.

---

### Not Rotating Credentials

Credentials should be changed periodically.

Regular rotation reduces the risk of security breaches.

---

# Real-World Use

Secure credential handling is essential in modern software systems.

Example production workflow:

```text
Application starts
       ↓
Credentials retrieved securely
       ↓
Application connects to database
       ↓
Data processing begins
```

Secure credential handling is used in:

• cloud infrastructure  
• data pipelines  
• web applications  
• analytics platforms.

Security best practices ensure that sensitive information remains protected.

---

# Lesson Recap

In this lesson you learned:

• why credentials must be protected  
• how environment variables store secrets securely  
• how secret managers protect sensitive data  
• best practices for secure credential management.

Secure credential handling is essential for **protecting applications and data in production environments**.

---

# Next Lesson

Next we will continue Module 11 with:

# Lesson 6 — Performance Checklist

You will learn:

• how to identify performance issues in Python programs  
• how to optimize code efficiency  
• common performance pitfalls  
• practical techniques for improving performance.
