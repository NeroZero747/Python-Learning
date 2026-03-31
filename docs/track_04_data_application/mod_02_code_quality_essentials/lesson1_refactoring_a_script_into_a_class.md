# Module 6 — Object-Oriented Programming

# Lesson 4 — Refactoring a Script into a Class

---

# Lesson Objective

By the end of this lesson learners will understand:

• how to convert a traditional Python script into a class  
• why refactoring improves code organization  
• how object-oriented design helps manage complex workflows  
• how classes can structure data processing pipelines  

Refactoring is an important development practice because it improves **code structure without changing the behavior of the program**.

---

# Overview

Many beginners start writing Python programs as simple scripts.

Example script:

```python
def load_data():
    print("Loading data")

def clean_data():
    print("Cleaning data")

def export_data():
    print("Exporting results")

load_data()
clean_data()
export_data()
```

This script works well for small programs.

However, as programs grow larger, scripts often become difficult to manage.

Instead of leaving functions loosely organized, we can group them into a **class that represents a workflow**.

Refactored version:

```python
class DataPipeline:

    def load_data(self):
        print("Loading data")

    def clean_data(self):
        print("Cleaning data")

    def export_data(self):
        print("Exporting results")
```

Now we create an object from the class:

```python
pipeline = DataPipeline()

pipeline.load_data()
pipeline.clean_data()
pipeline.export_data()
```

This structure makes the workflow clearer and easier to expand.

---

# Key Idea Cards (3 Cards)

## Refactoring Improves Code Organization

Refactoring means improving code structure without changing its behavior.

Example improvement:

```text
Loose functions → structured class
```

The program still works the same way, but the code becomes easier to maintain.

---

## Classes Group Related Logic

When functions belong to the same workflow, they can be grouped inside a class.

Example workflow:

```text
DataPipeline
│
├── load_data()
├── clean_data()
└── export_data()
```

This keeps related operations together.

---

## Refactoring Helps Large Projects

Large projects often involve many operations.

Classes allow developers to structure workflows logically.

Example:

```text
ClaimsPipeline
SalesPipeline
MemberPipeline
```

Each pipeline can be represented as a class.

---

# Key Concepts

## Refactoring

Refactoring is the process of improving code structure without changing what the program does.

Example:

```text
messy script → organized class
```

---

## Workflow Class

A workflow class represents a process that includes multiple steps.

Example:

```python
class DataPipeline:
```

Each step becomes a method inside the class.

---

## Method Execution

Once the class is created, an object runs the workflow.

Example:

```python
pipeline = DataPipeline()
pipeline.load_data()
```

---

# Decision Flow

Refactoring a script into a class usually follows this pattern:

```text
Identify related functions
      ↓
Create a class
      ↓
Move functions into methods
      ↓
Create object
      ↓
Run methods
```

Example:

```python
pipeline = DataPipeline()
pipeline.run()
```

---

# Code Examples

## Example 1 — Original Script

```python
def load_data():
    print("Loading data")

def process_data():
    print("Processing data")

def export_data():
    print("Exporting results")

load_data()
process_data()
export_data()
```

---

## Example 2 — Refactored Class

```python
class DataPipeline:

    def load_data(self):
        print("Loading data")

    def process_data(self):
        print("Processing data")

    def export_data(self):
        print("Exporting results")
```

---

## Example 3 — Running the Pipeline

```python
pipeline = DataPipeline()

pipeline.load_data()
pipeline.process_data()
pipeline.export_data()
```

---

## Example 4 — Adding a Run Method

Classes often include a method that executes the workflow.

```python
class DataPipeline:

    def load_data(self):
        print("Loading data")

    def process_data(self):
        print("Processing data")

    def export_data(self):
        print("Exporting results")

    def run(self):
        self.load_data()
        self.process_data()
        self.export_data()
```

Usage:

```python
pipeline = DataPipeline()
pipeline.run()
```

Output:

```text
Loading data
Processing data
Exporting results
```

---

# SQL / Excel Comparison

Refactoring concepts exist in other tools.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| workflow | class | stored procedure | macro |
| steps | methods | SQL statements | macro steps |
| execution | object.run() | procedure call | macro execution |

Example SQL stored procedure:

```sql
CREATE PROCEDURE process_sales
AS
BEGIN
    SELECT * FROM sales
END
```

This procedure groups multiple operations together.

Python classes provide a similar structure.

---

# Practice Exercises

## Exercise 1

Tags: print(), Functions, Scripts, Refactoring

Convert the following script into a class.

```python
def load():
    print("Load data")

def analyze():
    print("Analyze data")
```

---

## Exercise 2

Tags: Classes, CI/CD, Scripts, Refactoring

Create a class called `AnalysisPipeline`.

```python
class AnalysisPipeline:
```

Move the functions into methods.

---

## Exercise 3

Tags: Functions, OOP, Scripts, Refactoring

Add a `run()` method that executes the steps.

```python
def run(self):
    self.load()
    self.analyze()
```

---

# Common Mistakes

## Moving Functions Without Adding self

Incorrect:

```python
def load_data():
```

Correct:

```python
def load_data(self):
```

Methods must include `self`.

---

## Forgetting to Create an Object

Incorrect:

```python
DataPipeline.run()
```

Correct:

```python
pipeline = DataPipeline()
pipeline.run()
```

---

## Refactoring Too Early

For very small scripts, classes may not be necessary.

Classes are most useful when:

• workflows grow larger  
• multiple steps exist  
• code must scale.

---

# Real-World Use

Refactoring scripts into classes is common in professional projects.

Example data pipeline:

```python
class ClaimsPipeline:

    def load(self):
        pass

    def clean(self):
        pass

    def calculate_metrics(self):
        pass

    def export(self):
        pass
```

Usage:

```python
pipeline = ClaimsPipeline()

pipeline.load()
pipeline.clean()
pipeline.calculate_metrics()
pipeline.export()
```

This structure organizes complex workflows into a maintainable system.

---

# Lesson Recap

In this lesson you learned:

• what refactoring means  
• how to convert scripts into classes  
• how classes organize workflows  
• how object-oriented design improves maintainability  

Refactoring helps transform simple scripts into **structured Python systems**.

---

# Next Module

You have now completed:

# Module 6 — Object-Oriented Programming

You learned:

• what classes are  
• how objects are created  
• how attributes and methods work  
• how scripts can be refactored into classes  

These concepts introduce **object-oriented design**, which is widely used in professional Python development.

---

# Next Module

Next we will begin:

# Module 7 — Data Engineering Foundations

First lesson:

**What Is Data Engineering?**

This module will introduce concepts such as:

• ETL vs ELT  
• working with large datasets  
• pipeline design  
• efficient data storage.
