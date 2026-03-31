# Module 1 — Getting Started

## Lesson 2 — How to Request Access & Software

### Lesson Objective

By the end of this lesson learners will understand:

• what tools are required to start working with Python  
• how to request or obtain access to Python in their organization  
• what software is typically installed for Python development  
• the difference between the Python language and the development tools used with it  

Before writing Python code, it is important to ensure the **correct tools and environment are available**.

### Overview

Python itself is simply a programming language. In order to write and run Python programs, several supporting tools are typically required.

These tools help developers:

• write code  
• run programs  
• manage libraries  
• debug errors  
• organize projects  

In most organizations, Python development requires a few standard components:

```text
Python interpreter
Code editor or IDE
Package manager
Environment management
```

The **Python interpreter** is the program that actually runs Python code.

A **code editor** allows developers to write and organize their scripts.

A **package manager** installs additional libraries that extend Python’s capabilities.

Together, these tools form the **Python development environment**.

In some companies, these tools are pre-installed or provided through internal systems. In other cases, developers install them themselves.

Understanding how these components work together is an important first step before writing Python code.

### Key Idea Cards (Cards)

#### Python Requires a Development Environment (Card 1)

Python code cannot run by itself. It must be executed by the **Python interpreter**.

Example:

```python
print("Hello World")
```

The interpreter reads this instruction and executes it.

Without the interpreter, Python code is simply text.

#### Development Tools Make Coding Easier (Card 2)

Writing code in a plain text editor is possible, but modern development tools provide many helpful features:

• syntax highlighting  
• error detection  
• debugging tools  
• code completion  

These features improve productivity and reduce mistakes.

#### Libraries Extend Python’s Capabilities (Card 3)

Python’s core language is small, but its power comes from libraries.

Examples include:

| Library | Purpose |
|------|------|
| Pandas | data analysis |
| NumPy | numerical calculations |
| Requests | API communication |
| Matplotlib | data visualization |

Installing these libraries allows Python to perform advanced tasks.

### Key Concepts (Tabs)

#### Python Interpreter (Tab 1)

The Python interpreter is the program that runs Python code.

When a Python script runs, the interpreter reads each line of code and executes it.

Example script:

```python
print("Starting program")
```

The interpreter processes the instruction and displays the output.

#### Integrated Development Environment (Tab 2)

An IDE or code editor is where developers write and manage their code.

Common Python editors include:

| Tool | Description |
|------|-------------|
| VS Code | Lightweight, popular editor |
| PyCharm | Full-featured Python IDE |
| Jupyter Notebook | Interactive environment for data work |

For many data teams, **VS Code and Jupyter Notebooks** are common choices.

#### Package Manager (Tab 3)

Python uses a tool called **pip** to install libraries.

Example command:

```bash
pip install pandas
```

This installs the Pandas library so it can be used in Python scripts.

Libraries allow Python to perform complex operations without writing everything from scratch.

### Decision Flow

Before writing Python code, the environment must be prepared.

Typical setup process:

```text
Request access to development environment
        ↓
Install Python interpreter
        ↓
Install development editor
        ↓
Install required libraries
        ↓
Begin writing Python programs
```

Once the environment is ready, Python development becomes much easier.

### Code Examples (Tabs)

#### Example 1 — Testing Python Installation (Tab 1)

After Python is installed, run the following command in a terminal:

```bash
python --version
```

Output might look like:

```text
Python 3.11.4
```

This confirms that Python is installed correctly.

#### Example 2 — Running Python in the Terminal (Tab 2)

You can run a Python command directly from the terminal:

```bash
python
```

This starts the Python interpreter.

Example session:

```python
>>> print("Hello Python")
Hello Python
```

The `>>>` symbol indicates the interactive Python prompt.

#### Example 3 — Running a Python Script (Tab 3)

Create a file called:

```text
hello.py
```

Add the following code:

```python
print("Python is working")
```

Run the script:

```bash
python hello.py
```

Output:

```text
Python is working
```

### SQL / Excel Comparison

If you already work with SQL or Excel, Python development tools serve a similar purpose.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| execution engine | Python interpreter | database engine | Excel calculation engine |
| script | Python file | SQL script | workbook |
| development tool | VS Code | SQL client | Excel interface |

Each system provides tools that allow users to write instructions and run them.

### Practice Exercises (Tabs)

#### Exercise 1 (Tab 1)

Tags: Terminal, Python Version, Setup

Check whether Python is installed by running:

```bash
python --version
```

Write down the version number.

#### Exercise 2 (Tab 2)

Tags: Python Interpreter, print(), Testing

Open the Python interpreter and run the following:

```python
print("My Python environment is ready")
```

Observe the output.

#### Exercise 3 (Tab 3)

Tags: Scripts, Terminal, print()

Create a file called:

```text
test_script.py
```

Add the following code:

```python
print("This script is running successfully")
```

Run the script using the terminal.

### Common Mistakes (Tabs)

#### Installing the wrong Python version (Tab 1)

Some older tutorials may reference outdated Python versions.

Always install **Python 3.x**, not Python 2.

#### Confusing Python with development tools (Tab 2)

Python itself is the language. Tools like VS Code are simply editors used to write Python code.

#### Missing environment permissions (Tab 3)

In corporate environments, access may require:

• administrator approval  
• internal software portals  
• VPN or network permissions  

If Python cannot be installed locally, contact your IT support team.

### Real-World Use

In professional environments, Python development environments are often used for:

• building analytics pipelines  
• creating automation scripts  
• processing large datasets  
• building dashboards or applications  

Example workflow:

```text
Open VS Code
        ↓
Write Python script
        ↓
Run script in terminal
        ↓
Process data
        ↓
Export results
```

Having a properly configured development environment ensures these workflows run smoothly.

### Lesson Recap

In this lesson you learned:

• Python development requires several tools  
• the Python interpreter runs Python code  
• editors such as VS Code help write and manage scripts  
• libraries extend Python’s capabilities  

Setting up the correct tools ensures that Python programs can run successfully.

### Next Lesson

Next you will learn:

**Lesson 3 — How to Install Extensions in VS Code**

This lesson will explain:

• how VS Code supports Python development  
• which extensions improve productivity  
• how extensions provide debugging and code assistance  

These tools make Python development **much easier and more efficient**.