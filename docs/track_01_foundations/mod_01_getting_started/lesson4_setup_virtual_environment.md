# Module 1 — Getting Started

## Lesson 4 — How to Setup a Virtual Environment

### Lesson Objective

By the end of this lesson learners will understand:

• what a virtual environment is  
• why virtual environments are important in Python development  
• how to create a virtual environment  
• how to activate and deactivate a virtual environment  

Virtual environments help developers **manage project dependencies and avoid conflicts between libraries**.

### Overview

As Python projects grow, they often require many external libraries such as:

• Pandas  
• NumPy  
• Requests  
• Matplotlib  

Different projects may require **different versions of these libraries**.

For example:

Project A might require:

```text
pandas 1.5
```

Project B might require:

```text
pandas 2.0
```

If both projects use the same Python installation, library conflicts can occur.

A **virtual environment** solves this problem.

A virtual environment creates an **isolated Python environment** where libraries are installed only for that specific project.

This means:

• each project has its own dependencies  
• library versions do not conflict  
• environments remain organized  

This is considered a **best practice for Python development**.

### Key Idea Cards (Cards)

#### Virtual Environments Isolate Projects (Card 1)

A virtual environment creates a separate workspace for a Python project.

This workspace contains:

• its own Python interpreter  
• its own installed libraries  

This ensures that projects do not interfere with each other.

#### Each Project Should Have Its Own Environment (Card 2)

A common development workflow looks like this:

```text
Project A
    virtual environment A

Project B
    virtual environment B
```

Each project manages its own dependencies independently.

#### Virtual Environments Prevent Dependency Conflicts (Card 3)

Without virtual environments, installing a library globally may break other projects.

Virtual environments allow developers to safely install different library versions without affecting other projects.

### Key Concepts (Tabs)

#### Dependency (Tab 1)

A dependency is a library that a program requires in order to function.

Example dependencies:

| Library | Purpose |
|------|------|
| Pandas | data analysis |
| NumPy | numerical computing |
| Requests | API communication |

Projects often depend on multiple libraries.

#### Virtual Environment (Tab 2)

A virtual environment is an isolated Python environment created specifically for a project.

It contains:

• Python interpreter  
• installed packages  
• configuration settings  

Virtual environments ensure reproducible environments across systems.

#### Environment Activation (Tab 3)

Before using a virtual environment, it must be **activated**.

Activating an environment tells the system to use the environment’s Python interpreter and libraries.

Once activated, any installed libraries will belong to that environment.

### Decision Flow

The process of using a virtual environment follows these steps:

```text
Create project folder
        ↓
Create virtual environment
        ↓
Activate virtual environment
        ↓
Install required libraries
        ↓
Run Python scripts
```

When the environment is active, Python commands use that environment’s libraries.

### Code Examples (Tabs)

#### Example 1 — Creating a Virtual Environment (Tab 1)

Navigate to your project folder and run:

```bash
python -m venv venv
```

Explanation:

| Part | Meaning |
|------|------|
| python | Python interpreter |
| -m venv | run the virtual environment module |
| venv | name of the environment |

This creates a folder containing the virtual environment.

#### Example 2 — Activating the Virtual Environment (Tab 2)

On **Windows**:

```bash
venv\Scripts\activate
```

On **Mac/Linux**:

```bash
source venv/bin/activate
```

When activated, the terminal prompt will look like this:

```text
(venv) C:\project_folder>
```

This indicates the environment is active.

#### Example 3 — Installing Libraries (Tab 3)

Once the environment is activated, install libraries using pip:

```bash
pip install pandas
```

The library will be installed **inside the virtual environment only**.

### SQL / Excel Comparison

Virtual environments are conceptually similar to **isolated workspaces**.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| environment | virtual environment | database schema | workbook |
| dependency | library | extension/plugin | add-in |
| isolation | project environment | database instance | file |

Just as Excel workbooks isolate data, virtual environments isolate Python dependencies.

### Practice Exercises (Tabs)

#### Exercise 1 (Tab 1)

Tags: venv, Terminal, Project Setup

Create a new project folder.

Example:

```text
python_project
```

Inside the folder, create a virtual environment.

```bash
python -m venv venv
```

#### Exercise 2 (Tab 2)

Tags: venv, Activation, Terminal

Activate the environment.

Confirm activation by checking if the terminal shows:

```text
(venv)
```

#### Exercise 3 (Tab 3)

Tags: pip install, pandas, pip list

Install a library.

```bash
pip install pandas
```

Verify installation:

```bash
pip list
```

### Common Mistakes (Tabs)

#### Forgetting to Activate the Environment (Tab 1)

If the environment is not activated, packages may install globally.

Always activate the environment before installing libraries.

#### Deleting the Environment Folder (Tab 2)

The virtual environment folder contains installed packages.

Deleting it removes the environment.

If necessary, it can be recreated with:

```bash
python -m venv venv
```

#### Installing Libraries Globally (Tab 3)

Installing libraries globally can cause dependency conflicts.

Always install libraries **within a virtual environment**.

### Real-World Use

In real projects, virtual environments are used to ensure that development environments remain consistent.

Typical workflow:

```text
Clone project repository
        ↓
Create virtual environment
        ↓
Install project dependencies
        ↓
Run project code
```

This workflow ensures that every developer working on the project uses the same library versions.

Virtual environments are essential in:

• data engineering pipelines  
• machine learning projects  
• production applications  
• analytics automation scripts  

### Lesson Recap

In this lesson you learned:

• what virtual environments are  
• why they are important in Python development  
• how to create and activate virtual environments  
• how environments isolate project dependencies  

Using virtual environments is a **best practice for professional Python development**.

### Next Lesson

Next you will learn:

**Lesson 5 — How to Install Libraries in a Virtual Environment**

This lesson will explain:

• how Python libraries are installed  
• how pip works  
• how to manage project dependencies  

Installing libraries allows Python programs to perform advanced tasks such as data analysis and API communication.