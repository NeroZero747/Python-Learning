# Module 8 — Building Data Applications

# Lesson 7 — Shiny for Python

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **Shiny for Python** is  
• how Shiny applications differ from Streamlit applications  
• how **reactive programming** works in data applications  
• how to build a basic Shiny dashboard in Python  
• how reactive functions trigger UI updates automatically  

Shiny for Python is a framework for building **interactive web applications** that automatically update when inputs change. It is designed to create **highly reactive dashboards**, making it ideal for complex data applications.

---

# Overview

Most data dashboards rely on **user inputs**.

Examples include:

• dropdown filters  
• sliders  
• date ranges  
• search fields  

These inputs determine what data is displayed.

In many frameworks, updating a dashboard requires manually refreshing the interface.

Shiny uses a **reactive programming model**, which means the application automatically updates when inputs change.

Example reactive workflow:

```text
User changes filter
        ↓
Reactive system detects change
        ↓
Data recalculates
        ↓
Charts update automatically
```

This allows developers to build highly responsive applications.

Shiny applications are widely used for:

• analytics dashboards  
• scientific applications  
• interactive data tools  
• enterprise reporting systems.

Originally created for the R programming language, Shiny now supports **Python-based applications**.

---

# Key Idea Cards (3 Cards)

## Shiny Uses Reactive Programming

Reactive programming means that outputs automatically update when inputs change.

Example:

```text
Input changes
       ↓
Calculation updates
       ↓
Chart refreshes automatically
```

Developers do not need to manually trigger updates.

---

## Shiny Separates Interface and Logic

Shiny applications typically include two parts:

```text
User Interface (UI)
Application Logic (Server)
```

The UI defines the layout of the application.

The server contains the data processing logic.

---

## Shiny Supports Complex Applications

Shiny is often used for larger analytics systems because it allows developers to build:

• multi-page dashboards  
• complex reactive workflows  
• advanced visualizations.

This makes Shiny a powerful tool for enterprise data applications.

---

# Key Concepts

## Reactive Inputs

Inputs allow users to control application behavior.

Examples include:

• dropdown menus  
• sliders  
• text inputs  
• date pickers.

These inputs trigger updates throughout the application.

---

## Reactive Outputs

Outputs display results in the dashboard.

Examples include:

• charts  
• tables  
• metrics  
• text.

When inputs change, outputs automatically update.

---

## Reactive Functions

Reactive functions calculate values based on inputs.

Example workflow:

```text
Input value changes
       ↓
Reactive function recalculates
       ↓
Output updates
```

This system ensures dashboards stay synchronized with user selections.

---

# Decision Flow

Choosing between Streamlit and Shiny often follows this logic:

```text
Need simple dashboard quickly?
         ↓
       YES
         ↓
     Use Streamlit

Need highly reactive complex app?
         ↓
       YES
         ↓
      Use Shiny
```

Both tools are powerful, but they serve slightly different use cases.

---

# Code Examples

## Example 1 — Basic Shiny App

```python
from shiny import App, ui

app_ui = ui.page_fluid(
    ui.h2("My Shiny App"),
    ui.p("Welcome to Shiny for Python")
)

def server(input, output, session):
    pass

app = App(app_ui, server)
```

This creates a simple Shiny application.

---

## Example 2 — Adding a Slider Input

```python
ui.input_slider("num", "Select a number", 1, 100, 50)
```

This creates an interactive slider.

---

## Example 3 — Displaying Text Output

```python
@output
@render.text
def result():
    return f"Selected value: {input.num()}"
```

The output updates automatically when the slider changes.

---

## Example 4 — Full Reactive Example

```python
from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.input_slider("num", "Select number", 1, 100, 10),
    ui.output_text("result")
)

def server(input, output, session):

    @output
    @render.text
    def result():
        return f"You selected {input.num()}"

app = App(app_ui, server)
```

This application updates automatically when the slider value changes.

---

# SQL / Excel Comparison

Reactive behavior exists in other tools as well.

| Feature | Shiny | SQL | Excel |
|------|------|------|------|
| filtering | reactive inputs | WHERE clause | filter |
| calculations | reactive functions | queries | formulas |
| visualization | dashboards | BI tools | charts |

Example SQL query:

```sql
SELECT *
FROM sales
WHERE region = 'West'
```

In Shiny, filters trigger this logic automatically.

---

# Practice Exercises

## Exercise 1

Tags: Imports, Shiny

Create a simple Shiny app.

```python
from shiny import App, ui
```

Define a UI layout.

---

## Exercise 2

Tags: Tuples, HTTP Methods, Shiny

Add a slider input.

```python
ui.input_slider("num", "Choose number", 1, 100, 50)
```

---

## Exercise 3

Tags: HTTP Methods, Shiny

Create a reactive output.

Display the slider value dynamically.

---

# Common Mistakes

## Confusing UI and Server Logic

Shiny separates interface and logic.

Incorrect structure:

```text
UI and data processing mixed together
```

Correct structure:

```text
UI layout
Server logic
```

---

## Overusing Reactive Functions

Too many reactive calculations can slow applications.

Best practice:

• cache results  
• limit unnecessary recalculations.

---

## Ignoring Application Structure

Large Shiny apps should use clear organization:

```text
UI components
server functions
data logic
```

This improves maintainability.

---

# Real-World Use

Shiny applications are widely used for complex analytics systems.

Examples include:

• healthcare analytics platforms  
• financial risk dashboards  
• scientific research tools  
• enterprise data portals.

Example architecture:

```text
Database
     ↓
Python Data Processing
     ↓
Shiny Application
     ↓
User Interaction
     ↓
Reactive Charts
```

These systems allow organizations to build highly interactive analytics platforms.

---

# Lesson Recap

In this lesson you learned:

• what Shiny for Python is  
• how reactive programming works  
• how Shiny applications are structured  
• how Shiny dashboards update automatically  
• how reactive functions trigger UI recalculations  

Shiny enables developers to build **highly interactive and reactive data applications**.

---

# Next Lesson

Next we will learn:

# Lesson 8 — Streamlit vs Shiny

You will learn:

• how Streamlit and Shiny compare  
• when to use each framework  
• how to choose the best tool for your project.
