# Module 1 — Getting Started

## Lesson 6 — How to Run a Python Notebook or Script

### Lesson Objective

By the end of this lesson learners will understand:

• the difference between Python scripts and notebooks  
• how to run Python code in the terminal  
• how to run Python code in VS Code  
• how Jupyter Notebooks allow interactive analysis  

Running Python code is a core skill because it allows developers to **test programs, analyze results, and debug errors**.

### Overview (Cards)

Once Python and the development tools are installed, the next step is learning how to **run Python programs**.

There are two common ways to execute Python code:

```text
Python Scripts (.py files)
Jupyter Notebooks (.ipynb files)
```

Both approaches are widely used, but they serve slightly different purposes.

#### Python Scripts (Card 1)

A Python script is a file containing Python code.

Example file:

```text
analysis.py
```

Scripts are commonly used for:

• automation tasks  
• data pipelines  
• backend services  
• scheduled jobs  

Scripts run from start to finish.

#### Jupyter Notebooks (Card 2)

A Jupyter Notebook is an interactive environment that allows developers to run code **one cell at a time**.

Example notebook:

```text
analysis.ipynb
```

Notebooks are commonly used for:

• data exploration  
• visualization  
• experimentation  
• teaching and demonstrations  

Many data scientists and analysts prefer notebooks for exploratory work.

### Key Idea Cards (Cards)

#### Python Scripts Run Entire Programs (Card 1)

A script is a file containing Python instructions.

Example script:

```python
print("Start analysis")
print("Loading data")
print("Analysis complete")
```

When executed, the entire file runs from top to bottom.

#### Notebooks Run Code in Sections (Card 2)

Notebooks divide code into **cells**.

Each cell can be executed independently.

This allows developers to experiment and analyze results step by step.

#### Scripts and Notebooks Serve Different Purposes (Card 3)

Typical workflow:

```text
Exploration → Notebook
Automation → Script
```

Notebooks are great for experimentation, while scripts are better for production tasks.

### Key Concepts (Tabs)

#### Python Script (Tab 1)

A Python script is a file with the `.py` extension.

Example:

```text
sales_analysis.py
```

Scripts contain Python instructions that run sequentially.

Scripts are ideal for:

• automation  
• production pipelines  
• reusable programs  

#### Jupyter Notebook (Tab 2)

A notebook is an interactive environment for running Python code.

Notebooks allow:

• code cells  
• text documentation  
• visualizations  
• interactive exploration  

Example cell:

```python
print("Exploring dataset")
```

Notebooks are commonly used for data analysis.

#### Python Interpreter (Tab 3)

The Python interpreter reads and executes Python code.

Example command:

```bash
python script.py
```

The interpreter processes each line of the script.

### Decision Flow

Running Python code typically follows this process:

```text
Write Python code
        ↓
Save file or notebook
        ↓
Run code
        ↓
Python interpreter executes instructions
        ↓
Results displayed
```

If errors occur, the interpreter displays an error message.

### Code Examples (Tabs)

#### Example 1 — Running a Python Script (Tab 1)

Create a file called:

```text
hello.py
```

Add this code:

```python
print("Hello Python")
```

Run the script in the terminal:

```bash
python hello.py
```

Output:

```text
Hello Python
```

#### Example 2 — Running Code in VS Code (Tab 2)

Open a Python file in VS Code:

```python
print("Running Python inside VS Code")
```

Click the **Run Python File** button.

Output appears in the integrated terminal.

#### Example 3 — Running Code in a Jupyter Notebook (Tab 3)

Create a notebook and add a cell:

```python
name = "Python"

print("Learning", name)
```

Run the cell.

Output:

```text
Learning Python
```

Each cell can be executed independently.

### SQL / Excel Comparison

Running Python code has similarities with SQL queries and Excel formulas.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| execution | run script | run query | calculate sheet |
| script file | .py | .sql | workbook |
| interactive analysis | notebook | query editor | spreadsheet |

Notebooks are similar to **interactive query editors**, while scripts are more like **automated workflows**.

### Practice Exercises (Tabs)

#### Exercise 1 (Tab 1)

Tags: Scripts, Terminal, print()

Create a Python script called:

```text
test_program.py
```

Add this code:

```python
print("Python script executed successfully")
```

Run the script in the terminal.

#### Exercise 2 (Tab 2)

Tags: Notebooks, Variables, print()

Create a notebook.

Add a cell containing:

```python
x = 5
y = 10

print(x + y)
```

Run the cell.

#### Exercise 3 (Tab 3)

Tags: Notebooks, Variables, Arithmetic

Modify the notebook to calculate:

```text
price * quantity
```

Example:

```python
price = 20
quantity = 3

print(price * quantity)
```

Observe the result.

### Common Mistakes (Tabs)

#### Forgetting to Save Files (Tab 1)

If a script is not saved before running it, changes may not execute.

Always save files before running scripts.

#### Running the Wrong File (Tab 2)

Ensure the correct script is executed.

Example:

```bash
python correct_script.py
```

Running the wrong file can produce unexpected results.

#### Mixing Scripts and Notebook Workflows (Tab 3)

Scripts run sequentially.

Notebooks allow experimentation.

Understanding when to use each tool improves workflow efficiency.

### Real-World Use

Professionals often use both scripts and notebooks in data workflows.

Example workflow:

```text
Explore dataset → Jupyter Notebook
Develop analysis → Notebook
Convert analysis to automation → Python Script
Schedule script execution → Data pipeline
```

This approach allows teams to transition from **experimentation to production workflows**.

Scripts often power:

• scheduled analytics jobs  
• ETL pipelines  
• automated reporting systems  

### Lesson Recap

In this lesson you learned:

• Python code can run as scripts or notebooks  
• scripts execute entire programs sequentially  
• notebooks allow interactive code execution  
• both tools are useful in data workflows  

Understanding how to run Python code is essential for developing and testing programs.

### Next Lesson

Next we will begin **Module 2 — Programming Foundations**.

The first lesson will introduce:

**What Is Programming**

In that lesson you will learn:

• how programs give instructions to computers  
• how logic controls program behavior  
• how programming automates complex tasks  

This module introduces the **core programming concepts used in Python**.