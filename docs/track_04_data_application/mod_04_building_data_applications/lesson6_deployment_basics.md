# Module 8 — Building Data Applications

# Lesson 6 — Deployment Basics

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **deployment** means for data applications  
• how users access deployed dashboards  
• different ways to deploy Streamlit applications  
• common deployment environments used in organizations  

Deployment is the process of making a data application **available to other users**, allowing teams across an organization to access dashboards through a web interface.

---

# Overview

During development, a Streamlit application usually runs on a developer’s computer.

Example workflow:

```text
Developer Laptop
       ↓
streamlit run app.py
       ↓
Local Web App
```

However, this means **only the developer can access the dashboard**.

To allow others to use the application, it must be **deployed to a shared environment**.

Example deployment workflow:

```text
Python App
      ↓
Server / Cloud Platform
      ↓
Web URL
      ↓
Users Access Dashboard
```

Once deployed, users can access the dashboard through a browser without installing Python.

Common deployment options include:

• cloud platforms  
• internal servers  
• analytics platforms  
• containerized environments.

---

# Key Idea Cards (3 Cards)

## Deployment Makes Apps Accessible

Without deployment:

```text
App runs on developer computer
```

With deployment:

```text
App hosted on server
        ↓
Users access via URL
```

This allows teams across an organization to use the application.

---

## Deployment Environments Host Applications

Data applications are typically hosted on servers or cloud platforms.

Examples include:

• AWS  
• Azure  
• Google Cloud  
• internal enterprise servers.

These environments run the application continuously.

---

## Deployment Enables Collaboration

Once deployed, multiple users can interact with the dashboard simultaneously.

Example workflow:

```text
User A filters data
User B exports data
User C views charts
```

All users access the same application.

---

# Key Concepts

## Application Hosting

Hosting means running an application on a server so it remains available.

Example architecture:

```text
Streamlit App
      ↓
Server
      ↓
Browser Interface
```

Users connect to the server through the browser.

---

## Application URL

When deployed, applications are accessed using a URL.

Example:

```text
https://analytics.company.com/sales-dashboard
```

Users open the URL to access the dashboard.

---

## Deployment Environments

Common environments for deploying data apps include:

• cloud platforms  
• container platforms  
• analytics hosting platforms  
• internal infrastructure.

Each environment manages application resources and security.

---

# Decision Flow

Choosing a deployment method typically follows this logic:

```text
Internal tool?
      ↓
    YES
      ↓
Deploy on internal server

Public application?
      ↓
    YES
      ↓
Deploy on cloud platform
```

This ensures applications are hosted in appropriate environments.

---

# Code Examples

## Example 1 — Running a Streamlit App Locally

```bash
streamlit run app.py
```

This launches the application locally.

---

## Example 2 — Creating a Requirements File

```text
streamlit
pandas
numpy
```

A `requirements.txt` file lists dependencies needed to run the application.

---

## Example 3 — Installing Dependencies

```bash
pip install -r requirements.txt
```

This installs required libraries before deployment.

---

## Example 4 — Running on a Server

```bash
streamlit run app.py --server.port 8501
```

This command launches the application on a specified port.

---

# SQL / Excel Comparison

Deployment concepts also exist in other tools.

| Feature | Streamlit | SQL | Excel |
|------|------|------|------|
| deployment | web server | database server | shared workbook |
| access | URL | database connection | shared file |
| updates | redeploy app | update query | save workbook |

Example shared Excel workflow:

```text
Excel file
      ↓
Shared network drive
      ↓
Multiple users open file
```

Deployment achieves a similar effect for dashboards.

---

# Practice Exercises

## Exercise 1

Tags: Scripts, Data Processing, Streamlit, Deployment

Run a Streamlit app locally.

```bash
streamlit run app.py
```

Observe how the application launches in the browser.

---

## Exercise 2

Tags: Data Processing, Streamlit, Deployment, Dependencies

Create a requirements file.

```text
streamlit
pandas
```

Save this as `requirements.txt`.

---

## Exercise 3

Tags: pip install, Deployment, Dependencies

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Common Mistakes

## Forgetting Dependencies

Applications may fail if required libraries are missing.

Always include a `requirements.txt` file.

---

## Hardcoding File Paths

Applications should not depend on local file paths.

Incorrect:

```text
C:/Users/data.csv
```

Better:

```text
data/sales.csv
```

---

## Ignoring Security

Deployment environments must manage:

• authentication  
• data access permissions  
• network security.

Sensitive data must be protected.

---

# Real-World Use

Deployment allows organizations to distribute analytics tools.

Examples include:

• internal reporting dashboards  
• machine learning monitoring apps  
• data exploration tools  
• operational analytics systems.

Example deployment workflow:

```text
Python Dashboard
       ↓
Hosted on Analytics Platform
       ↓
Users Access via Browser
       ↓
Business Teams Explore Data
```

This allows data teams to deliver analytics tools across an organization.

---

# Lesson Recap

In this lesson you learned:

• what deployment means for data applications  
• how dashboards are hosted on servers  
• how users access deployed applications  
• how dependencies and infrastructure support applications  

Deployment transforms a local prototype into a **shared analytics platform**.

---

# Next Lesson

Next we will learn:

# Lesson 7 — Introduction to Shiny for Python

You will learn:

• how Shiny for Python works  
• how it differs from Streamlit  
• how reactive programming powers interactive dashboards  
• how to build Shiny data applications.
