# Module 9 — Professional Python Practices

# Lesson 6 — Configuration & Secrets Management

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **configuration management** is in Python applications  
• why credentials and secrets should not be hardcoded  
• how **environment variables** work  
• how `.env` files manage configuration settings securely  
• how CI/CD pipelines manage secrets securely  

In professional systems, applications must often connect to **databases, APIs, or external services**. These systems require configuration values such as passwords, connection strings, and API keys. Managing these values correctly is essential for **security and maintainability**.

---

# Overview

A beginner might write code like this:

```python
import psycopg2

connection = psycopg2.connect(
    host="database.company.com",
    user="admin",
    password="mypassword123",
    database="sales_db"
)
```

While this code works, it creates serious problems:

• passwords are exposed in the code  
• credentials may be uploaded to version control  
• changing environments becomes difficult  
• secrets cannot be rotated easily.

Professional applications store configuration **outside the code**.

Instead of hardcoding credentials:

```text
Database Host
Database User
Database Password
API Keys
File Paths
```

These values are stored in **environment variables** or configuration files.

Example workflow:

```text
Application Code
      ↓
Reads Environment Variables
      ↓
Connects to Database
```

This keeps sensitive information separate from the codebase.

---

# Key Idea Cards (3 Cards)

### Never Store Secrets in Code

Credentials should never be written directly in source code.

Bad example:

```python
password = "mypassword123"
```

Better approach:

```python
password = os.getenv("DB_PASSWORD")
```

Secrets should always be stored securely.

---

### Environment Variables Store Configuration

Environment variables store configuration outside the application.

Examples:

```text
DB_HOST
DB_USER
DB_PASSWORD
API_KEY
```

The application reads these variables at runtime.

---

### Configuration Enables Multiple Environments

Applications often run in multiple environments:

```text
Development
Testing
Production
```

Each environment can use different configuration values without changing the code.

---

# Key Concepts

## Environment Variables

Environment variables are key-value pairs stored in the system environment.

Example variables:

```text
DB_HOST=database.company.com
DB_USER=analytics_user
DB_PASSWORD=securepassword
```

Python can read these values using the `os` module.

---

## Reading Environment Variables in Python

Example:

```python
import os

database_host = os.getenv("DB_HOST")
database_user = os.getenv("DB_USER")
database_password = os.getenv("DB_PASSWORD")
```

If the environment variables are defined, Python retrieves their values.

---

## .env Files

A `.env` file stores environment variables locally.

Example `.env` file:

```text
DB_HOST=database.company.com
DB_USER=analytics_user
DB_PASSWORD=securepassword
API_KEY=12345ABCDE
```

These values are loaded into the application environment.

The **python-dotenv** library is commonly used to load `.env` files.

---

# Decision Flow

Developers typically follow this process when managing configuration:

```text
Does the application require configuration values?
            ↓
           YES
            ↓
Store values in environment variables
            ↓
Load variables in application
```

This approach keeps configuration separate from code.

---

# Code Examples

### Example 1 — Hardcoded Credentials (Bad Practice)

```python
import psycopg2

connection = psycopg2.connect(
    host="database.company.com",
    user="admin",
    password="mypassword123"
)
```

Problems:

• insecure  
• difficult to maintain  
• cannot support multiple environments.

---

### Example 2 — Environment Variable Approach

```python
import os
import psycopg2

connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)
```

This keeps credentials outside the code.

---

### Example 3 — Using a `.env` File

Install the dotenv library:

```bash
pip install python-dotenv
```

Example code:

```python
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
```

This loads environment variables from the `.env` file.

---

### Example 4 — Configuration Module

Many projects create a configuration module.

Example:

**config/settings.py**

```python
import os

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
```

Usage:

```python
from config.settings import DB_HOST
```

This centralizes configuration management.

---

# SQL / Excel Comparison

Configuration management concepts exist in other tools as well.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| configuration | environment variables | connection strings | workbook settings |
| secrets management | .env files | database credentials | protected files |
| environment separation | dev/test/prod | database environments | different workbooks |

Example SQL connection:

```text
Server
Database
User
Password
```

These parameters must be managed securely, similar to Python configuration.

---

# Practice Exercises

### Exercise 1

Tags: Environment Variables, Variables

Create a `.env` file:

```text
DB_HOST=localhost
DB_USER=myuser
DB_PASSWORD=mypassword
```

---

### Exercise 2

Tags: Environment Variables, pip install, Variables

Install the dotenv library:

```bash
pip install python-dotenv
```

---

### Exercise 3

Tags: os Module, Imports, Environment Variables, HTTP Methods

Load environment variables in Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv("DB_HOST")
```

Print the variable to confirm it loads correctly.

---

### Exercise 4

Tags: Environment Variables, Scripts, Variables

Create a configuration module.

Example:

```python
config/settings.py
```

Store environment variables there.

---

# Common Mistakes

### Hardcoding Credentials

Never store secrets in code repositories.

This creates security risks.

---

### Committing `.env` Files to Git

`.env` files should not be committed to version control.

Add them to `.gitignore`.

Example:

```text
.env
```

---

### Forgetting Environment Variables in Deployment

Production environments must define the required environment variables.

If they are missing, applications will fail to run.

---

# Real-World Use

Configuration management is essential in production systems.

Example architecture:

```text
Python Application
       ↓
Reads Environment Variables
       ↓
Connects to Database / API
```

Example enterprise workflow:

```text
Developer writes application
       ↓
Secrets stored in environment variables
       ↓
Application deployed to server
       ↓
Server provides environment configuration
```

This approach protects sensitive data while keeping applications flexible.

---

# Secrets in CI/CD Pipelines

When applications are deployed through CI/CD pipelines, secrets must be managed carefully.

CI/CD systems like GitLab CI/CD, GitHub Actions, and Jenkins provide **secure variable storage** that injects secrets into pipelines at runtime.

Example deployment workflow:

```text
Application deployed
       ↓
CI/CD pipeline retrieves secrets
       ↓
Application authenticates services
       ↓
Operations monitor system
```

Best practices for CI/CD secrets:

• never store secrets in source code or version control  
• use the CI/CD platform's built-in secrets manager  
• rotate credentials regularly  
• limit access to production secrets  
• use different credentials for each environment (dev, staging, production).

---

# Lesson Recap

In this lesson you learned:

• why configuration values should not be hardcoded  
• how environment variables store application settings  
• how `.env` files manage configuration locally  
• how Python applications read configuration values  
• how CI/CD pipelines manage secrets securely.

Proper configuration management ensures **secure and flexible Python applications**.

---

# Next Lesson

Next we will learn:

# Lesson 7 — Logging Instead of Print Statements

You will learn:

• why professional applications use logging  
• how Python’s `logging` module works  
• how logs help debug production systems  
• how to structure logs in Python applications.
