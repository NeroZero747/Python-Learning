# Module 9 — Professional Python Practices

# Lesson 10 — Packaging and Distributing Python Projects

---

# Lesson Objective

By the end of this lesson learners will understand:

• how Python projects are **packaged for distribution**  
• how developers share Python code as **reusable libraries**  
• how Python packages are installed using **pip**  
• how teams create **internal Python packages** for shared functionality  

Packaging allows developers to turn Python code into reusable libraries that can be installed and used in other projects.

This is how tools like **Pandas, NumPy, and Streamlit** are distributed.

---

# Overview

In earlier lessons we organized code into **modules and project structures**.

Example project:

```text
analytics_project/
│
├── app.py
├── src/
│   ├── data_loader.py
│   ├── analytics.py
│   └── metrics.py
└── data/
```

However, sometimes code needs to be reused across **multiple projects**.

Example situation:

```text
Project A → data processing logic
Project B → same processing logic
Project C → same processing logic
```

Instead of copying the code repeatedly, developers create a **Python package**.

Example:

```text
analytics_tools/
```

This package can then be installed and used by many projects.

Example workflow:

```text
Package created
      ↓
Published or shared
      ↓
Installed using pip
      ↓
Imported into projects
```

Packaging makes Python code **portable and reusable**.

---

# Key Idea Cards (3 Cards)

### Python Packages Contain Reusable Code

A Python package groups related modules together.

Example package:

```text
analytics_tools/
│
├── data_loader.py
├── analytics.py
└── metrics.py
```

Other projects can install and use this package.

---

### Packages Can Be Installed with pip

Once packaged, Python libraries can be installed using pip.

Example:

```bash
pip install analytics_tools
```

After installation, the package becomes available in Python.

---

### Packaging Enables Code Sharing

Packages allow developers to share code across teams and organizations.

Examples:

```text
Open source packages → PyPI
Internal packages → company repositories
```

Packaging promotes code reuse and collaboration.

---

# Key Concepts

## Python Package Structure

A typical Python package looks like this:

```text
analytics_tools/
│
├── analytics_tools/
│   ├── __init__.py
│   ├── data_loader.py
│   └── analytics.py
│
├── pyproject.toml
├── README.md
└── requirements.txt
```

Important components include:

• source code  
• package configuration  
• documentation.

---

## __init__.py

The `__init__.py` file marks a directory as a Python package.

Example:

```python
# analytics_tools/__init__.py
```

This file may contain initialization code or simply be empty.

---

## pyproject.toml

Modern Python packaging uses a configuration file called:

```text
pyproject.toml
```

Example configuration:

```toml
[project]
name = "analytics_tools"
version = "0.1.0"
description = "Reusable analytics utilities"
```

This file defines package metadata.

---

# Decision Flow

Developers decide to create packages using the following logic:

```text
Is the code reused across projects?
        ↓
       YES
        ↓
Create a Python package
```

Packaging improves maintainability and reuse.

---

# Code Examples

### Example 1 — Package Folder Structure

```text
analytics_tools/
│
├── analytics_tools/
│   ├── __init__.py
│   ├── data_loader.py
│   └── analytics.py
│
└── pyproject.toml
```

This structure defines a Python package.

---

### Example 2 — Package Module

Example module inside the package:

```python
# analytics_tools/data_loader.py

import pandas as pd

def load_sales_data(file_path):
    return pd.read_csv(file_path)
```

---

### Example 3 — Using the Package

After installation, the package can be imported:

```python
from analytics_tools.data_loader import load_sales_data

data = load_sales_data("sales.csv")
```

The function is now available in the project.

---

### Example 4 — Installing Local Packages

A local package can be installed using pip.

```bash
pip install -e .
```

The `-e` flag installs the package in **editable mode**, allowing developers to modify it during development.

---

# SQL / Excel Comparison

Packaging concepts also exist in other tools.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| reusable code | packages | stored procedures | VBA modules |
| code distribution | PyPI packages | shared database scripts | macro-enabled workbooks |
| shared libraries | internal packages | database libraries | Excel templates |

Example SQL shared library:

```text
Company database functions
```

These reusable database functions are similar to Python packages.

---

# Practice Exercises

### Exercise 1

Tags: Constructors, Scripts

Create a simple package structure.

```text
my_package/
│
├── my_package/
│   ├── __init__.py
│   └── utilities.py
```

---

### Exercise 2

Tags: String Formatting, Functions, Scripts

Add a function inside `utilities.py`.

```python
def greet(name):
    return f"Hello {name}"
```

---

### Exercise 3

Tags: print(), Imports, Scripts

Import the function in another script.

```python
from my_package.utilities import greet

print(greet("Python"))
```

---

### Exercise 4

Tags: Lists, Configuration, Dependencies

Create a `pyproject.toml` file defining package metadata.

Example:

```toml
[project]
name = "my_package"
version = "0.1.0"
```

---

# Common Mistakes

### Copying Code Between Projects

Copying code leads to inconsistencies and maintenance issues.

Better approach:

```text
Create reusable packages
```

---

### Poor Package Structure

Packages should have clear organization.

Example:

```text
package_name/
modules
configuration
documentation
```

Avoid mixing unrelated functionality.

---

### Missing Documentation

Packages should include documentation explaining how they work.

Example:

```text
README.md
```

Documentation helps other developers use the package correctly.

---

# Real-World Use

Python packaging is widely used in software development.

Examples of popular packages:

```text
pandas
numpy
scikit-learn
streamlit
```

Organizations also create **internal packages**.

Example internal tools:

```text
company_data_tools
analytics_framework
data_pipeline_utils
```

Benefits include:

• consistent code across teams  
• faster development  
• easier maintenance.

Packaging enables Python projects to grow from **small scripts to full software ecosystems**.

---

# Lesson Recap

In this lesson you learned:

• how Python projects are packaged  
• how reusable libraries are distributed  
• how pip installs packages  
• how teams create shared internal libraries.

Packaging allows Python developers to **share reusable functionality across projects and teams**.

---

# Module 9 Complete

In this module you learned professional Python development practices including:

• clean coding standards  
• project structure  
• reusable modules  
• dependency management  
• configuration management  
• logging  
• testing  
• performance optimization  
• packaging and distribution.

These practices form the foundation of **production-ready Python systems**.
