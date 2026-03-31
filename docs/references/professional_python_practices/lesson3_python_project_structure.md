# Module 9 — Professional Python Practices

# Lesson 3 — Python Project Structure

---

# Lesson Objective

By the end of this lesson learners will understand:

• how professional Python projects are structured  
• why organizing code into folders improves maintainability  
• how modules and packages work in Python  
• how to structure projects for scalability and collaboration  

As Python scripts grow into larger systems, project organization becomes extremely important. A clear project structure allows developers to **manage complexity, reuse code, and collaborate efficiently**.

---

# Overview

When beginners write Python programs, they often store everything in a single script.

Example beginner structure:

```text
project/
    app.py
```

This works for small scripts, but as projects grow, this structure becomes difficult to manage.

Example problems:

• the script becomes very large  
• functions become difficult to locate  
• code cannot easily be reused  
• multiple developers cannot work efficiently.

Professional Python projects organize code into **structured folders and modules**.

Example professional project structure:

```text
project/
│
├── app.py
├── requirements.txt
├── config/
│   └── settings.py
├── data/
│   └── sales.csv
├── src/
│   ├── data_loader.py
│   ├── transformations.py
│   └── analytics.py
└── tests/
    └── test_pipeline.py
```

This structure separates responsibilities across folders.

Benefits include:

• easier navigation  
• reusable modules  
• improved collaboration  
• easier testing and deployment.

---

# Key Idea Cards (3 Cards)

### Large Projects Need Organization

As projects grow, a single script becomes difficult to maintain.

Example evolution:

```text
Small Script
     ↓
Multiple Scripts
     ↓
Organized Project Structure
```

Proper organization prevents chaos as projects expand.

---

### Modules Enable Code Reuse

Instead of repeating logic across scripts, developers create modules.

Example module:

```python
def load_data(file_path):
    return pd.read_csv(file_path)
```

This function can be reused across many parts of the project.

---

### Structure Enables Collaboration

When developers follow consistent project structures:

• new developers can quickly understand the codebase  
• responsibilities are clearly separated  
• debugging becomes easier.

This is especially important for team environments.

---

# Key Concepts

## Modules

A **module** is simply a Python file containing reusable code.

Example:

```text
data_loader.py
```

Example code inside the module:

```python
import pandas as pd

def load_sales_data(file_path):
    return pd.read_csv(file_path)
```

Modules allow logic to be reused across multiple scripts.

---

## Packages

A **package** is a folder containing multiple Python modules.

Example:

```text
src/
    data_loader.py
    analytics.py
```

Packages help organize related functionality.

---

## Separation of Responsibilities

Professional projects separate code into logical components.

Example:

```text
data loading
data processing
business logic
visualization
```

Each component is placed in its own module or folder.

---

# Decision Flow

Developers often decide how to structure projects using this logic:

```text
Is the script small and simple?
        ↓
      YES
        ↓
Use a single file

Is the project growing?
        ↓
      YES
        ↓
Create modules and folders
```

As projects scale, modular design becomes essential.

---

# Code Examples

### Example 1 — Single Script (Small Project)

```python
import pandas as pd

data = pd.read_csv("sales.csv")

filtered = data[data["region"] == "West"]

print(filtered)
```

This approach works for simple scripts but does not scale well.

---

### Example 2 — Modular Project

**data_loader.py**

```python
import pandas as pd

def load_sales_data(file_path):
    return pd.read_csv(file_path)
```

**analytics.py**

```python
def filter_region(data, region):
    return data[data["region"] == region]
```

**app.py**

```python
from data_loader import load_sales_data
from analytics import filter_region

data = load_sales_data("sales.csv")

west_sales = filter_region(data, "West")

print(west_sales)
```

This modular structure improves clarity and reuse.

---

### Example 3 — Folder-Based Structure

Example project layout:

```text
sales_analytics/
│
├── app.py
├── requirements.txt
├── src/
│   ├── data_loader.py
│   ├── transformations.py
│   └── analytics.py
└── data/
    └── sales.csv
```

Each folder has a clear purpose.

---

### Example 4 — Importing Modules

Python allows importing functions from modules.

```python
from analytics import filter_region
```

This enables code reuse across the project.

---

# SQL / Excel Comparison

Project structure concepts exist in other tools as well.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| modular logic | modules | stored procedures | VBA modules |
| project organization | folders/packages | database schemas | workbook organization |
| reusable logic | functions | views | formulas/templates |

Example SQL comparison:

```sql
CREATE VIEW west_region_sales AS
SELECT *
FROM sales
WHERE region = 'West';
```

Views provide reusable logic similar to Python modules.

---

# Practice Exercises

### Exercise 1

Tags: Scripts, Best Practices

Create a project folder structure:

```text
project/
├── app.py
├── src/
│   └── data_loader.py
```

---

### Exercise 2

Tags: pandas, Imports, read_csv(), CSV

Move the following code into a module:

```python
import pandas as pd

data = pd.read_csv("sales.csv")
```

Create a function called `load_data()` inside `data_loader.py`.

---

### Exercise 3

Tags: Imports, Scripts, Data I/O

Import your module into `app.py`.

Example:

```python
from data_loader import load_data
```

Run the script and verify it works.

---

# Common Mistakes

### Putting All Code in One File

Large scripts become difficult to maintain.

Better approach:

```text
Separate logic into modules
```

---

### Mixing Different Responsibilities

Avoid placing all logic in one file.

Example mistake:

```text
data loading
data transformation
visualization
all inside one script
```

Better approach:

```text
data_loader module
analytics module
visualization module
```

---

### Poor Folder Naming

Folder names should clearly describe their purpose.

Examples:

```text
data/
src/
tests/
config/
```

Avoid vague names like:

```text
misc/
stuff/
temp/
```

---

# Real-World Use

Professional Python projects often follow consistent structures.

Example data pipeline project:

```text
data_pipeline/
│
├── pipeline.py
├── requirements.txt
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── config/
│   └── settings.py
└── tests/
    └── test_pipeline.py
```

Benefits:

• easier debugging  
• easier scaling  
• easier onboarding for new developers.

This approach is commonly used in:

• data engineering pipelines  
• analytics platforms  
• machine learning systems  
• production software applications.

---

# Lesson Recap

In this lesson you learned:

• how professional Python projects are structured  
• how modules and packages organize code  
• how modular design improves maintainability  
• how large projects are structured for collaboration.

A well-organized project structure allows Python applications to **scale from simple scripts to full production systems**.

---

# Next Lesson

Next we will learn:

# Lesson 4 — Creating Reusable Modules

You will learn:

• how to design reusable Python modules  
• how to organize functions inside modules  
• how modules improve maintainability  
• how large projects reuse shared logic.
