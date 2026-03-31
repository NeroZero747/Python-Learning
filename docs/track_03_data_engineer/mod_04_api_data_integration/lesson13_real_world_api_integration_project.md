# Module 17 — APIs & Data Integration  
## Lesson 13 — Real-World API Integration Project

---

# Lesson Objective

By the end of this lesson you will:

- Build a **complete API data pipeline**
- Retrieve real data from an API
- Parse JSON responses
- Convert API data into a DataFrame
- Store the data for analysis

This lesson combines everything learned in this module into a **practical real-world workflow**.

---

# Overview

Many modern analytics systems retrieve data directly from APIs and integrate it into internal systems.

Example workflow:

```text
External API
      ↓
Python Script
      ↓
JSON Data
      ↓
Data Processing
      ↓
Database / File Storage
      ↓
Analytics & Dashboards
```

In this project you will create a script that:

1. Sends an API request  
2. Retrieves data  
3. Parses the JSON response  
4. Converts the data into a DataFrame  
5. Stores the results  

This mirrors how real data pipelines operate.

---

# Project Scenario

Imagine your analytics team needs to retrieve **GitHub repository information**.

You will use the GitHub API to retrieve repository data.

Example API endpoint:

```text
https://api.github.com/users/octocat/repos
```

This endpoint returns information about repositories.

---

# Step 1 — Send an API Request

First retrieve data from the API.

```python
import requests

url = "https://api.github.com/users/octocat/repos"

response = requests.get(url)

data = response.json()

print(len(data))
```

The API returns a list of repositories.

---

# Step 2 — Inspect the JSON Structure

Always inspect the structure of the response.

```python
print(data[0])
```

Example response structure:

```text
{
  'name': 'Hello-World',
  'language': 'Python',
  'stargazers_count': 120
}
```

---

# Step 3 — Extract Relevant Fields

Next extract useful fields.

Example fields:

```text
Repository Name
Programming Language
Star Count
```

Example code:

```python
records = []

for repo in data:

    records.append({
        "repo_name": repo["name"],
        "language": repo["language"],
        "stars": repo["stargazers_count"]
    })
```

Now we have a structured dataset.

---

# Step 4 — Convert Data into a DataFrame

```python
import pandas as pd

df = pd.DataFrame(records)

print(df.head())
```

Example output:

```text
      repo_name language  stars
0  Hello-World   Python    120
1  Project-A     JavaScript 85
2  Data-App      Python     60
```

Now the data is ready for analysis.

---

# Step 5 — Save the Data

The dataset can be saved to a file or database.

Example saving to CSV:

```python
df.to_csv("github_repos.csv", index=False)
```

Example saving to database:

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///github_data.db")

df.to_sql("repos", engine, if_exists="replace", index=False)
```

---

# Complete Pipeline Script

```python
import requests
import pandas as pd
from sqlalchemy import create_engine

url = "https://api.github.com/users/octocat/repos"

response = requests.get(url)

data = response.json()

records = []

for repo in data:

    records.append({
        "repo_name": repo["name"],
        "language": repo["language"],
        "stars": repo["stargazers_count"]
    })

df = pd.DataFrame(records)

engine = create_engine("sqlite:///github_data.db")

df.to_sql("repos", engine, if_exists="replace", index=False)

print("Pipeline completed successfully")
```

This script:

```text
Retrieves API data
Processes the data
Stores the results
```

---

# SQL / Excel Comparison

Traditional workflow:

```text
Download CSV
Open Excel
Clean data
Create reports
```

API pipeline workflow:

```text
API Request
      ↓
Python Processing
      ↓
Database Storage
      ↓
Analytics Queries
```

This allows automated data retrieval.

---

# Practice Exercises

## Exercise 1

Tags: SELECT, APIs, HTTP Methods, Scripts

Modify the script to retrieve repository data from another GitHub user.

Example:

```text
https://api.github.com/users/{username}/repos
```

---

## Exercise 2

Tags: APIs, HTTP Methods

Add additional fields such as:

```text
created_at
forks_count
watchers_count
```

---

## Exercise 3

Tags: groupby(), GROUP BY, APIs

Perform analysis on the dataset.

Example:

```python
df.groupby("language").size()
```

---

# Common Mistakes

## Mistake 1 — Not Inspecting the API Response

Always inspect the JSON structure before extracting fields.

Example:

```python
print(data)
```

---

## Mistake 2 — Extracting Missing Fields

Some repositories may have missing values.

Example:

```text
language may be null
```

Scripts should handle missing data.

---

## Mistake 3 — Not Handling Errors

API requests can fail.

Always check the response status code.

Example:

```python
if response.status_code != 200:
    print("Request failed")
```

---

# Real-World Use

API integration pipelines are used across many industries.

Examples include:

---

### Financial Data Systems

Retrieve:

```text
market prices
economic indicators
trading data
```

---

### Marketing Platforms

Retrieve campaign data from:

```text
Google Ads
Facebook Ads
LinkedIn Ads
```

---

### SaaS Platforms

Companies integrate systems through APIs.

Example:

```text
CRM API → Data Warehouse → Business Dashboard
```

---

# Key Idea Cards

### Card 1

API integration pipelines retrieve, process, and store data automatically.

---

### Card 2

JSON API responses can be converted into structured datasets.

---

### Card 3

Python pipelines can automate external data ingestion.

---

# Lesson Recap

In this lesson you built a complete API pipeline that:

- retrieves API data  
- parses JSON responses  
- converts data into DataFrames  
- stores the results  

This workflow mirrors how many **real-world data systems integrate external data sources**.

---

# Next Lesson

Next you will learn:

**Module 17 — Lesson 14: API Best Practices**

This final lesson will cover:

- designing reliable API integrations  
- error handling strategies  
- building production-ready API pipelines.