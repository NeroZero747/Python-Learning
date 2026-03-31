# Module 1 — Getting Started

## Lesson 5 — How to Install Libraries in a Virtual Environment

### Lesson Objective

By the end of this lesson learners will understand:

• what Python libraries are  
• how libraries extend Python functionality  
• how to install libraries using pip  
• how to manage project dependencies  

Libraries allow Python programs to perform powerful tasks such as **data analysis, API communication, and visualization**.

### Overview

Python’s core language provides basic programming capabilities, but most real-world applications rely on **libraries**.

A library is a collection of pre-written code that developers can use to perform specific tasks.

Instead of writing complex functionality from scratch, developers install libraries that provide these features.

Examples of common Python libraries:

| Library | Purpose |
|------|------|
| Pandas | data analysis |
| NumPy | numerical operations |
| Requests | API communication |
| Matplotlib | data visualization |

These libraries greatly expand Python’s capabilities.

Libraries are installed using **pip**, Python’s package manager.

Example command:

```bash
pip install pandas
```

This command downloads and installs the Pandas library so it can be used in Python programs.

Installing libraries inside a **virtual environment** ensures that each project manages its own dependencies.

### Key Idea Cards (Cards)

#### Libraries Extend Python (Card 1)

Python’s core language is small, but libraries provide powerful functionality.

Example tasks enabled by libraries:

• analyzing datasets  
• building dashboards  
• interacting with APIs  
• performing statistical analysis  

Libraries make Python a versatile programming language.

#### pip Installs Libraries (Card 2)

Python libraries are installed using **pip**.

Example command:

```bash
pip install requests
```

pip downloads the library and installs it into the current Python environment.

#### Virtual Environments Manage Dependencies (Card 3)

Libraries should be installed within the project’s virtual environment.

Example workflow:

```text
Create environment
      ↓
Activate environment
      ↓
Install libraries
      ↓
Run Python code
```

This ensures projects remain organized and reproducible.

### Key Concepts (Tabs)

#### Library (Tab 1)

A library is a collection of reusable code that provides additional functionality.

Example library usage:

```python
import pandas as pd
```

This line imports the Pandas library.

Libraries allow developers to perform complex operations without writing everything themselves.

#### pip (Tab 2)

pip is Python’s package manager used to install libraries.

Common pip commands:

| Command | Purpose |
|------|------|
| pip install library | install a library |
| pip uninstall library | remove a library |
| pip list | show installed libraries |

pip communicates with the **Python Package Index (PyPI)** to download packages.

#### Dependency (Tab 3)

A dependency is a library that a project requires to function.

Example:

```text
Project dependencies
• pandas
• numpy
• requests
```

Managing dependencies ensures that the project runs correctly across different systems.

### Decision Flow

Installing libraries typically follows this process:

```text
Activate virtual environment
        ↓
Use pip to install library
        ↓
Library downloaded from PyPI
        ↓
Library installed in environment
        ↓
Python script can import the library
```

Once installed, the library can be imported and used in code.

### Code Examples (Tabs)

#### Example 1 — Installing Pandas (Tab 1)

Run the following command:

```bash
pip install pandas
```

pip will download the library and install it.

#### Example 2 — Verifying Installed Libraries (Tab 2)

To see installed libraries, run:

```bash
pip list
```

Example output:

```text
Package     Version
pandas      2.1.0
numpy       1.25.2
```

This shows the libraries available in the environment.

#### Example 3 — Using an Installed Library (Tab 3)

After installing Pandas, it can be used in Python code.

```python
import pandas as pd

data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
    Name  Age
0  Alice   25
1    Bob   30
```

This example creates a simple dataset using Pandas.

### SQL / Excel Comparison

Libraries provide capabilities similar to built-in tools in SQL or Excel.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| package | Python library | database extension | add-in |
| install tool | pip | database install | add-in installer |
| dataset tools | Pandas | SQL queries | Excel tables |

For example, Pandas can perform operations similar to SQL queries or Excel tables.

### Practice Exercises (Tabs)

#### Exercise 1 (Tab 1)

Tags: pip install, requests, pip list

Activate your virtual environment.

Install the Requests library.

```bash
pip install requests
```

Verify installation with:

```bash
pip list
```

#### Exercise 2 (Tab 2)

Tags: pip install, pandas, import

Install the Pandas library.

```bash
pip install pandas
```

Create a small script that imports Pandas.

#### Exercise 3 (Tab 3)

Tags: import, pandas, numpy, print()

Create a Python script that imports two libraries.

Example:

```python
import pandas
import numpy

print("Libraries loaded successfully")
```

Run the script to confirm it works.

### Common Mistakes (Tabs)

#### Installing Libraries Without Activating the Environment (Tab 1)

If the virtual environment is not activated, libraries may install globally.

Always activate the environment before installing packages.

#### Misspelling Library Names (Tab 2)

Incorrect:

```bash
pip install panda
```

Correct:

```bash
pip install pandas
```

Always verify the correct library name.

#### Installing Unnecessary Libraries (Tab 3)

Installing too many libraries can complicate projects.

Only install libraries required for the project.

### Real-World Use

Libraries are essential for real-world Python projects.

Examples:

| Task | Library |
|------|------|
| data analysis | Pandas |
| machine learning | Scikit-learn |
| API requests | Requests |
| data visualization | Matplotlib |

Example automation script:

```python
import pandas as pd
import requests

data = requests.get("https://api.example.com/data")

print("Data retrieved")
```

Libraries enable Python to interact with external systems and analyze complex datasets.

### Lesson Recap

In this lesson you learned:

• Python libraries extend the capabilities of the language  
• pip is used to install libraries  
• libraries should be installed within virtual environments  
• dependencies must be managed carefully in projects  

Libraries are essential for building real-world Python applications.

### Next Lesson

Next you will learn:

**Lesson 6 — How to Run a Python Notebook or Script**

In that lesson you will learn:

• how to run Python scripts  
• how Jupyter notebooks work  
• when to use scripts vs notebooks  

This will allow you to **execute Python programs and analyze results interactively**.