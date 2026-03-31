# Module 9 — Professional Python Practices

# Lesson 5 — Dependency Management

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **dependencies** are in Python projects  
• how Python manages external libraries  
• how `requirements.txt` works  
• how **virtual environments** isolate project dependencies  

Dependency management is critical for professional Python development because most real-world projects rely on **external libraries** such as pandas, numpy, requests, or scikit-learn.

Managing these libraries correctly ensures that applications run consistently across different machines and environments.

---

# Overview

Most Python programs use external libraries.

Example:

```python
import pandas as pd
import numpy as np
```

These libraries are not built into Python. They must be installed separately.

Example installation:

```bash
pip install pandas
pip install numpy
```

However, as projects grow, managing libraries manually becomes difficult.

Example project dependencies:

```text
pandas
numpy
requests
sqlalchemy
streamlit
```

If another developer tries to run your project, they must install **the exact same libraries**.

This is where dependency management tools help.

Common tools include:

• `requirements.txt`  
• `pip`  
• `virtual environments`  
• `poetry`  
• `pipenv`.

In most Python projects, dependencies are stored in a file called:

```text
requirements.txt
```

---

# Key Idea Cards (3 Cards)

### Dependencies Are External Libraries

Dependencies are packages that your code relies on.

Examples:

```text
pandas
numpy
streamlit
sqlalchemy
```

Without installing these libraries, the program will not run.

---

### requirements.txt Tracks Project Libraries

A `requirements.txt` file lists the libraries required by the project.

Example:

```text
pandas
numpy
streamlit
```

This allows developers to install all dependencies at once.

---

### Virtual Environments Isolate Projects

Virtual environments create a **separate Python environment** for each project.

Example:

```text
Project A → pandas 1.5
Project B → pandas 2.0
```

This prevents library conflicts between projects.

---

# Key Concepts

## Pip

`pip` is Python’s package manager used to install libraries.

Example:

```bash
pip install pandas
```

This installs pandas from the Python Package Index (PyPI).

---

## requirements.txt

A `requirements.txt` file lists all libraries required for a project.

Example:

```text
pandas
numpy
streamlit
requests
```

To install all dependencies:

```bash
pip install -r requirements.txt
```

This installs every library listed in the file.

---

## Virtual Environments

A virtual environment creates an isolated Python environment for a project.

Example command:

```bash
python -m venv venv
```

This creates a new environment folder.

Activate environment:

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Once activated, installed libraries only affect that environment.

---

# Decision Flow

Developers usually manage dependencies using this workflow:

```text
Create project
      ↓
Create virtual environment
      ↓
Install libraries
      ↓
Generate requirements.txt
      ↓
Share project with team
```

This ensures consistent environments.

---

# Code Examples

### Example 1 — Installing Libraries

```bash
pip install pandas
pip install numpy
```

This installs the required libraries.

---

### Example 2 — Creating requirements.txt

Example file:

```text
pandas
numpy
streamlit
requests
```

---

### Example 3 — Installing Project Dependencies

Install dependencies using:

```bash
pip install -r requirements.txt
```

This installs all required libraries automatically.

---

### Example 4 — Freezing Installed Libraries

Python can automatically generate a requirements file.

```bash
pip freeze > requirements.txt
```

Example output:

```text
pandas==2.0.3
numpy==1.24.4
streamlit==1.29.0
```

This records exact library versions.

---

# SQL / Excel Comparison

Dependency management concepts also exist in other tools.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| external tools | libraries | extensions | add-ins |
| environment consistency | virtual environments | database versions | workbook versions |
| dependency tracking | requirements.txt | schema dependencies | plugin lists |

Example SQL equivalent:

A database application may depend on:

```text
database version
extensions
stored procedures
```

Similarly, Python projects depend on libraries.

---

# Practice Exercises

### Exercise 1

Tags: Environment Variables, venv, Dependencies

Create a virtual environment.

```bash
python -m venv venv
```

---

### Exercise 2

Tags: Environment Variables, venv, Dependencies

Activate the environment.

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

### Exercise 3

Tags: pip install, Dependencies

Install a library.

```bash
pip install pandas
```

---

### Exercise 4

Tags: Dependencies, Best Practices

Create a requirements file.

```bash
pip freeze > requirements.txt
```

---

# Common Mistakes

### Installing Libraries Globally

Installing libraries globally can cause conflicts between projects.

Better approach:

```text
Use virtual environments
```

---

### Forgetting to Include requirements.txt

Without this file, other developers cannot easily install dependencies.

Always include:

```text
requirements.txt
```

in your project repository.

---

### Ignoring Version Numbers

Library versions can change behavior.

Example:

```text
pandas==2.0.3
```

Pinning versions ensures consistent environments.

---

# Real-World Use

Dependency management is essential in production systems.

Example project structure:

```text
analytics_app/
│
├── app.py
├── requirements.txt
├── src/
│   ├── data_loader.py
│   └── analytics.py
└── data/
    └── sales.csv
```

Workflow:

```text
Developer clones repository
        ↓
Creates virtual environment
        ↓
Runs pip install -r requirements.txt
        ↓
Application runs successfully
```

Without dependency management, projects would fail when moved between machines.

---

# Lesson Recap

In this lesson you learned:

• what dependencies are in Python projects  
• how `pip` installs external libraries  
• how `requirements.txt` tracks dependencies  
• how virtual environments isolate project libraries.

Proper dependency management ensures that **Python applications run consistently across different environments**.

---

# Next Lesson

Next we will learn:

# Lesson 6 — Configuration & Environment Variables

You will learn:

• how Python applications manage configuration  
• why environment variables are used for secrets  
• how `.env` files work  
• how to securely store credentials for databases and APIs.
