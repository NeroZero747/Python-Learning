# Module 8 — Building Data Applications

# Lesson 10 — Streamlit vs Shiny

---

# Lesson Objective

By the end of this lesson learners will understand:

• the main differences between Streamlit and Shiny  
• the strengths and trade-offs of each framework  
• when Streamlit is a better fit  
• when Shiny is a better fit  

Choosing the right framework matters because different tools are better suited for different types of dashboards and applications.

---

# Overview

Both **Streamlit** and **Shiny for Python** allow developers to build interactive data applications using Python.

They have similar goals:

• create dashboards  
• add filters and charts  
• allow user interaction  
• display analytics results in the browser  

However, they differ in design philosophy.

**Streamlit** focuses on:

• simplicity  
• fast development  
• minimal code  
• easy dashboard creation  

**Shiny** focuses on:

• explicit reactivity  
• structured app design  
• more control over interactions  
• complex reactive workflows  

A simplified comparison looks like this:

```text
Need quick simple dashboard?
        ↓
    Streamlit

Need more controlled reactivity?
        ↓
      Shiny
```

Both are powerful, but they serve somewhat different development styles.

---

# Key Idea Cards (3 Cards)

## Streamlit Is Simpler to Start

Streamlit allows users to build dashboards quickly with minimal code.

Example:

```python
st.title("Sales Dashboard")
st.write(data)
```

This makes it great for rapid prototyping.

---

## Shiny Provides More Reactive Control

Shiny gives more control over how inputs and outputs interact.

Example:

```text
Input changes
     ↓
Reactive function reruns
     ↓
Specific outputs update
```

This makes Shiny useful for more complex applications.

---

## The Best Tool Depends on the Use Case

There is no single “best” tool for every situation.

The right choice depends on:

• app complexity  
• team skill set  
• need for reactive behavior  
• speed of development.

---

# Key Concepts

## Development Speed

Streamlit is generally faster for building a simple dashboard.

Example workflow:

```text
Write Python script
      ↓
Run Streamlit
      ↓
Dashboard available
```

---

## Reactive Model

Shiny uses a more explicit reactive model.

This means developers define:

• inputs  
• reactive calculations  
• outputs  

This structure can be more powerful for advanced dashboards.

---

## Application Complexity

Simple dashboards may fit Streamlit well.

Complex dashboards with many dependent interactions may fit Shiny better.

---

# Decision Flow

Choosing between Streamlit and Shiny often follows this logic:

```text
Need fast prototype?
      ↓
    YES
      ↓
 Use Streamlit

Need complex reactive interactions?
      ↓
    YES
      ↓
   Use Shiny
```

This is not a strict rule, but it is a useful guideline.

---

# Code Examples

## Example 1 — Streamlit Example

```python
import streamlit as st
import pandas as pd

data = pd.read_csv("sales.csv")

st.title("Sales Dashboard")
st.write(data.head())
```

This quickly produces a working dashboard.

---

## Example 2 — Shiny Example

```python
from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.h2("Sales Dashboard"),
    ui.output_text("message")
)

def server(input, output, session):

    @output
    @render.text
    def message():
        return "Welcome to Shiny"

app = App(app_ui, server)
```

This requires more structure but gives more control.

---

## Example 3 — Comparison of Style

Streamlit style:

```python
st.selectbox("Region", ["West", "East"])
```

Shiny style:

```python
ui.input_select("region", "Region", ["West", "East"])
```

Both create input controls, but the framework structure differs.

---

## Example 4 — Comparison Summary

```text
Streamlit:
- faster to build
- simpler syntax
- great for internal tools

Shiny:
- stronger reactive model
- more structured architecture
- better for complex interactions
```

---

# SQL / Excel Comparison

Both frameworks support workflows familiar to analysts.

| Feature | Streamlit | Shiny | SQL / Excel Analogy |
|------|------|------|------|
| filtering | simple widgets | reactive inputs | WHERE / filter |
| dashboard creation | very fast | more structured | BI dashboard |
| reactivity | reruns script | dependency-based updates | formulas recalculating |

Example Excel analogy:

```text
Simple worksheet dashboard → Streamlit feel
Complex workbook with dependent formulas → Shiny feel
```

---

# Practice Exercises

## Exercise 1

Tags: Data Processing, Streamlit, Shiny, Dashboards

Write a simple Streamlit dashboard.

Use:

• title  
• data table  
• dropdown filter  

---

## Exercise 2

Tags: HTTP Methods, Data Processing, Streamlit, Shiny

Write a simple Shiny app.

Use:

• title  
• one input  
• one reactive output  

---

## Exercise 3

Tags: Data Processing, Streamlit, Shiny

Compare the experience.

Ask yourself:

• Which was faster to build?  
• Which was easier to understand?  
• Which gave more control?

---

# Common Mistakes

## Assuming One Tool Is Always Better

Both tools are useful.

The correct choice depends on the application requirements.

---

## Choosing Complexity Too Early

For quick internal dashboards, starting with Streamlit may be more practical.

For advanced reactivity, Shiny may be better.

---

## Ignoring Team Familiarity

The best framework is also influenced by what the team can maintain.

A slightly less powerful tool may still be the better choice if the team can support it effectively.

---

# Real-World Use

A practical comparison:

**Use Streamlit for:**

• quick internal dashboards  
• prototypes  
• data exploration tools  
• fast business apps  

**Use Shiny for:**

• highly reactive apps  
• complex dashboards  
• apps with many dependent interactions  
• enterprise-style analytical tools  

Example decision:

```text
Need dashboard by tomorrow? → Streamlit
Need controlled reactive workflow for long-term app? → Shiny
```

---

# Lesson Recap

In this lesson you learned:

• how Streamlit and Shiny differ  
• what each framework does well  
• when Streamlit is a good choice  
• when Shiny is a good choice  

Both frameworks are excellent options for Python data apps, but they are optimized for **different development styles and application needs**.

---

# Next Module

You have now completed:

# Module 8 — Building Data Applications

You learned:

• why data apps matter  
• how Streamlit works  
• how to build dashboards and filters  
• how exporting and deployment work  
• how Shiny works  
• how reactive programming powers Shiny  
• how to build a Shiny dashboard  
• how Streamlit and Shiny compare  

These concepts provide a strong foundation for building **interactive Python analytics applications**.

---

# Next Module

Next we will begin:

# Module 9 — Professional Python Practices

In the next module you will learn:

• clean code principles  
• modular architecture  
• dependency management  
• testing and performance optimization for production systems.
