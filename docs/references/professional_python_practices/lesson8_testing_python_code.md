# Module 9 — Professional Python Practices

# Lesson 8 — Testing Python Code

---

# Lesson Objective

By the end of this lesson learners will understand:

• why **testing** is important in professional Python projects  
• what **unit tests** are  
• how Python testing frameworks work  
• how automated tests help prevent bugs in production systems  

Testing ensures that software behaves correctly and continues to work as expected when changes are made.

In professional environments, testing helps teams **detect bugs early and maintain reliable systems**.

---

# Overview

When developers write code, it is easy to assume the program works correctly.

Example script:

```python
def calculate_total_sales(data):
    return data["sales"].sum()
```

The developer may test this manually:

```python
print(calculate_total_sales(data))
```

However, manual testing has several problems:

• it is easy to forget edge cases  
• it is not repeatable  
• future changes may break functionality.

Professional projects use **automated tests**.

Automated tests verify that code behaves correctly every time it runs.

Example workflow:

```text
Developer writes function
        ↓
Write automated test
        ↓
Run tests automatically
        ↓
Verify function behavior
```

Testing helps ensure that code remains reliable as projects grow.

---

# Key Idea Cards (3 Cards)

### Tests Verify Code Behavior

Tests confirm that code produces expected results.

Example:

```text
Input → Function → Expected Output
```

If the output differs, the test fails.

---

### Tests Prevent Regression Bugs

A regression bug occurs when new changes break existing functionality.

Automated tests help detect these issues early.

Example workflow:

```text
Developer modifies code
        ↓
Tests run automatically
        ↓
If tests fail → bug detected
```

---

### Tests Enable Safe Refactoring

Developers often improve or restructure code.

Testing ensures these changes do not break functionality.

Example:

```text
Old code replaced
        ↓
Tests run
        ↓
Behavior verified
```

---

# Key Concepts

## Unit Tests

A **unit test** verifies the behavior of a small piece of code, usually a single function.

Example:

```python
def calculate_total_sales(data):
    return data["sales"].sum()
```

A unit test verifies that this function returns the correct result.

---

## Test Frameworks

Python includes several testing frameworks.

Common frameworks include:

```text
unittest
pytest
nose
```

The most widely used framework today is **pytest** because it is simple and powerful.

---

## Automated Testing

Automated tests can be run automatically during development.

Example:

```bash
pytest
```

This command runs all tests in the project.

Testing is often integrated into **CI/CD pipelines**.

---

# Decision Flow

Developers typically follow this testing workflow:

```text
Write function
       ↓
Write test for function
       ↓
Run tests
       ↓
Fix failures
```

This process ensures code behaves correctly before deployment.

---

# Code Examples

### Example 1 — Function to Test

```python
def add_numbers(a, b):
    return a + b
```

We want to verify that the function works correctly.

---

### Example 2 — Simple Test

Using pytest:

```python
def test_add_numbers():
    result = add_numbers(2, 3)
    assert result == 5
```

If the result is not 5, the test fails.

---

### Example 3 — Multiple Test Cases

```python
def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0
```

These tests verify different scenarios.

---

### Example 4 — Testing Data Functions

Example analytics function:

```python
def filter_region(data, region):
    return data[data["region"] == region]
```

Test:

```python
def test_filter_region():
    import pandas as pd

    data = pd.DataFrame({
        "region": ["West", "East"],
        "sales": [100, 200]
    })

    result = filter_region(data, "West")

    assert len(result) == 1
```

This confirms the filter works correctly.

---

# SQL / Excel Comparison

Testing concepts exist in other tools.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| test logic | unit tests | test queries | validation formulas |
| automation | pytest | automated scripts | macros |
| regression testing | automated tests | stored procedure tests | workbook checks |

Example SQL validation query:

```sql
SELECT COUNT(*)
FROM sales
WHERE sales < 0
```

This ensures invalid values do not exist.

Similarly, tests validate Python code.

---

# Practice Exercises

### Exercise 1

Tags: Tuples, Functions, Testing

Create a simple function:

```python
def multiply(a, b):
    return a * b
```

Write a test that verifies the function works.

---

### Exercise 2

Tags: Tuples, Testing

Write multiple test cases.

Example:

```python
assert multiply(2,3) == 6
assert multiply(0,5) == 0
```

---

### Exercise 3

Tags: pip install, Testing

Install pytest:

```bash
pip install pytest
```

Run tests using:

```bash
pytest
```

---

### Exercise 4

Tags: Scripts, Testing

Create a `tests` folder:

```text
project/
│
├── src/
│
└── tests/
    └── test_functions.py
```

Place test files inside the tests directory.

---

# Common Mistakes

### Not Writing Tests

Skipping tests may lead to hidden bugs in production systems.

Testing should be part of the development workflow.

---

### Testing Too Much at Once

Tests should focus on **small units of code**.

Example:

```text
Test individual functions
```

Avoid testing entire applications in a single test.

---

### Ignoring Edge Cases

Tests should include unusual inputs.

Examples:

```text
empty datasets
negative values
missing values
```

These cases often reveal hidden bugs.

---

# Real-World Use

Testing is essential in professional software systems.

Example workflow:

```text
Developer writes code
        ↓
Automated tests run
        ↓
Code pushed to repository
        ↓
CI/CD pipeline runs tests
        ↓
Deployment occurs if tests pass
```

Testing helps organizations maintain reliable systems such as:

• data pipelines  
• analytics platforms  
• machine learning systems  
• enterprise applications.

Without testing, software reliability decreases significantly.

---

# Lesson Recap

In this lesson you learned:

• why testing is important for reliable software  
• how unit tests verify individual functions  
• how pytest runs automated tests  
• how tests prevent regression bugs.

Testing ensures that Python applications remain **reliable and maintainable as they evolve**.

---

# Next Lesson

Next we will learn:

# Lesson 9 — Performance Optimization Basics

You will learn:

• why performance matters in Python applications  
• how inefficient code slows systems down  
• basic techniques for improving performance  
• how to identify performance bottlenecks.
