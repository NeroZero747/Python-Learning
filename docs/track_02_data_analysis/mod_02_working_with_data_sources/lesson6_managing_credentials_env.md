# Module 4 — Working with Data Sources

# Lesson 6 — Managing Credentials (.env)

---

# Lesson Objective

By the end of this lesson learners will understand:

• why database credentials should not be stored directly in code  
• how environment variables protect sensitive information  
• how `.env` files store credentials securely  
• how Python loads environment variables for database connections  

Managing credentials properly is critical for **security, maintainability, and production-ready data pipelines**.

---

# Overview

When connecting to databases or APIs, programs often require **credentials**, such as:

• usernames  
• passwords  
• API keys  
• database connection strings  

A beginner might write code like this:

```python
engine = sqlalchemy.create_engine(
"postgresql://username:password@server/database"
)
```

This approach is dangerous because the credentials are **visible in the code**.

Problems with this approach include:

• credentials exposed in Git repositories  
• credentials shared accidentally  
• security risks in production environments  

Instead, best practice is to store credentials in **environment variables**.

Example:

```text
DB_USER=my_username
DB_PASSWORD=my_password
DB_HOST=server
DB_NAME=database
```

Python can then read these values securely.

Example:

```python
import os

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
```

This method keeps credentials **separate from the code**.

---

# Key Idea Cards (3 Cards)

## Credentials Should Not Be Hardcoded

Hardcoding credentials means storing them directly in code.

Example:

```python
password = "mypassword123"
```

This is insecure because anyone who sees the code can access the credentials.

---

## Environment Variables Store Secrets

Environment variables store configuration values outside the code.

Example:

```text
DB_USER=analytics_user
DB_PASSWORD=secure_password
```

Python can read these values when the program runs.

---

## .env Files Simplify Local Development

A `.env` file stores environment variables locally.

Example:

```text
DB_USER=myuser
DB_PASSWORD=mypassword
```

Libraries such as **python-dotenv** can load these variables automatically.

---

# Key Concepts

## Environment Variables

Environment variables are values stored in the system environment.

Example in Python:

```python
import os

user = os.getenv("DB_USER")
```

This retrieves the value of the variable.

---

## .env Files

A `.env` file stores environment variables in a simple format.

Example `.env` file:

```text
DB_USER=my_user
DB_PASSWORD=my_password
DB_HOST=localhost
DB_NAME=sales_db
```

These values are loaded when the program runs.

---

## Loading .env Files

Python can load environment variables using the **dotenv library**.

Install the library:

```python
pip install python-dotenv
```

Load the variables:

```python
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
```

---

# Decision Flow

Managing credentials typically follows this workflow:

```text
Create .env file
      ↓
Store credentials securely
      ↓
Load environment variables in Python
      ↓
Use variables in database connection
```

Example:

```python
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
```

---

# Code Examples

## Example 1 — Creating a .env File

Create a file called `.env`.

Example content:

```text
DB_USER=analytics_user
DB_PASSWORD=my_secure_password
DB_HOST=localhost
DB_NAME=sales_db
```

---

## Example 2 — Loading Environment Variables

```python
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
```

---

## Example 3 — Using Credentials in a Connection

```python
import sqlalchemy

connection_string = f"postgresql://{user}:{password}@localhost/sales_db"

engine = sqlalchemy.create_engine(connection_string)
```

---

## Example 4 — Checking Variables

```python
print(os.getenv("DB_USER"))
```

This verifies that the variable loaded successfully.

---

# SQL / Excel Comparison

Credential management also exists in database tools and Excel workflows.

| Concept | Python | SQL Tool | Excel |
|------|------|------|------|
| credentials | .env variables | login settings | data source connection |
| secure storage | environment variables | credential manager | saved connection |
| connection config | connection string | connection profile | Power Query settings |

Example connection workflow:

```text
Credentials → Connection → Query Data
```

---

# Practice Exercises

## Exercise 1

Tags: Environment Variables, Databases, Variables, Testing

Create a `.env` file with the following variables.

```text
DB_USER=test_user
DB_PASSWORD=test_password
DB_HOST=localhost
DB_NAME=test_db
```

---

## Exercise 2

Tags: print(), os Module, Imports, Environment Variables

Load the environment variables in Python.

```python
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("DB_USER"))
```

---

## Exercise 3

Tags: String Formatting, Strings, Dictionaries, Environment Variables

Create a database connection string using environment variables.

```python
connection = f"{user}:{password}@localhost/test_db"
```

---

# Common Mistakes

## Committing .env Files to Git

`.env` files should **never be uploaded to version control**.

Instead add them to `.gitignore`.

Example:

```text
.env
```

---

## Using Incorrect Variable Names

Example:

```python
os.getenv("DB_PASSWORD")
```

If the variable name is wrong, Python returns **None**.

---

## Forgetting to Load the .env File

Example:

```python
os.getenv("DB_USER")
```

Without `load_dotenv()`, the variable may not exist.

---

# Real-World Use

Credential management is essential in real data pipelines.

Examples include:

• database connections  
• API authentication  
• cloud service credentials  
• secure application configuration  

Example workflow:

```python
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
```

This securely loads credentials without exposing them in code.

---

# Lesson Recap

In this lesson you learned:

• why credentials should not be hardcoded  
• how environment variables store secrets securely  
• how `.env` files simplify credential management  
• how Python loads environment variables  

Secure credential management is essential for **professional data engineering and analytics workflows**.

---

# Next Module

You have now completed:

# Module 4 — Working with Data Sources

You learned how to:

• load CSV files  
• load JSON data  
• connect to databases  
• run SQL queries in Python  
• write data back to databases  
• manage credentials securely  

---

# Next Module

# Module 5 — Writing Cleaner Python Code

You will learn:

• writing reusable functions  
• creating Python modules  
• structuring projects properly  
• logging basics  
• version control with Git  

These practices help turn scripts into **professional, maintainable codebases**.
