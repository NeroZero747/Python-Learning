#!/usr/bin/env python3
"""Rebuild lesson07_streamlit_vs_shiny.html — Module 5, Lesson 7 (final lesson)."""

import os
import html as htmlmod

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = os.path.join(BASE, "pages", "mod_05_data_application", "lesson07_streamlit_vs_shiny.html")

# ═══════════════════════════════════════════════════════════
# METADATA
# ═══════════════════════════════════════════════════════════
LESSON_NUM = 7
LESSON_TITLE = "Streamlit vs Shiny"
MODULE_NUM = 5
MODULE_TITLE = "Building Data Applications"
TRACK_LABEL = "Track 04 — Data Application"
PROGRESS = "7/7"
PREV_LESSON = ("lesson06_shiny_for_python.html", "Shiny for Python")
# No NEXT_LESSON — this is the last lesson in the module

# ═══════════════════════════════════════════════════════════
# CONTENT DATA
# ═══════════════════════════════════════════════════════════

HOOK_QUOTE = "Streamlit and Shiny for Python both turn a Python script into a live web application — but they take fundamentally different approaches to how your code runs, how state is managed, and how much control you have over the final result."

ANALOGY_INTRO = 'Think of choosing between Streamlit and Shiny like choosing between an automatic and a manual transmission car — Streamlit is the automatic that lets you press the gas and go with minimal setup, while Shiny is the manual that gives you precise gear control for demanding road conditions at the cost of a steeper learning curve.'

OVERVIEW_TIP = 'Neither framework is universally better — the right choice depends on your project\'s complexity, your team\'s experience, and how much control you need over the user interface and reactive behavior.'

overview_cards = [
    ("fa6-solid:bolt",          "Execution Model",  "The engine — automatic vs manual",                   "Streamlit re-runs your entire script from top to bottom every time a widget changes. Shiny only re-executes the specific outputs that depend on the changed input, leaving everything else untouched."),
    ("fa6-solid:arrows-spin",   "Reactivity",       "The gearbox — shifts for you or you decide",         "Streamlit handles reactivity implicitly — change a slider and the whole page refreshes. Shiny uses an explicit reactive graph where you define which computations depend on which inputs."),
    ("fa6-solid:palette",       "Layout Control",   "The dashboard — preset gauges or custom panel",       "Streamlit auto-arranges widgets top-to-bottom with minimal layout code. Shiny gives you full control over sidebars, tabs, columns, and card placement through dedicated layout functions."),
    ("fa6-solid:cloud-arrow-up","Deployment",       "The garage — cloud-hosted or self-managed",           "Streamlit Community Cloud offers free one-click deployment for public apps. Shiny apps typically deploy to Posit Connect, ShinyApps.io, or self-hosted servers for production use."),
    ("fa6-solid:puzzle-piece",  "Ecosystem",        "The road network — community routes and shortcuts",   "Streamlit has a large library of community components and a built-in sharing platform. Shiny benefits from Posit's enterprise ecosystem and deep integration with R-based tools."),
]

objectives = [
    ("fa6-solid:code-branch",   "Architectural Differences",  "Understand how Streamlit's script-based model differs from Shiny's UI/server architecture"),
    ("fa6-solid:arrows-spin",   "Reactivity Models",          "Compare Streamlit's full re-run approach with Shiny's targeted reactive graph"),
    ("fa6-solid:palette",       "Layout and Customization",   "Evaluate the layout and theming tradeoffs between both frameworks"),
    ("fa6-solid:cloud-arrow-up","Deployment Options",         "Identify deployment and scaling options available for each framework"),
    ("fa6-solid:scale-balanced","Framework Selection",         "Apply a decision framework to choose the right tool for a given project"),
]

takeaways = [
    ("pink",    "fa6-solid:code-branch",    "Script vs Architecture",
     "Streamlit runs your entire Python script from top to bottom on every interaction — simple to reason about, but every line executes again. Shiny separates the UI definition from the server logic with explicit reactive connections, so only the affected outputs re-execute.",
     ["Top-to-Bottom", "UI / Server", "Re-run Model"]),
    ("violet",  "fa6-solid:arrows-spin",    "Implicit vs Explicit Reactivity",
     "Streamlit handles reactivity implicitly — change a slider and the whole script re-runs automatically. Shiny tracks which inputs each output reads and only invalidates the specific functions that depend on the changed input, leaving everything else cached.",
     ["Implicit Re-run", "Reactive Graph", "Dependency Tracking"]),
    ("blue",    "fa6-solid:gauge-high",     "Speed to Prototype vs Depth of Control",
     "Streamlit gets a working dashboard on screen in minutes with almost no boilerplate. Shiny requires more upfront structure but gives you fine-grained control over layout, theming, and reactive flow — essential for complex production dashboards.",
     ["Quick Prototype", "Production Control", "Boilerplate"]),
    ("emerald", "fa6-solid:cloud-arrow-up", "Deployment Ecosystems",
     "Streamlit Community Cloud offers free one-click deployment for public apps and integrates directly with GitHub repositories. Shiny apps deploy to Posit Connect, ShinyApps.io, or self-hosted infrastructure — more setup, but better suited for enterprise environments.",
     ["Streamlit Cloud", "Posit Connect", "Self-Hosted"]),
    ("amber",   "fa6-solid:compass",        "Decision Framework",
     "Choose Streamlit when you need a quick prototype, a data exploration tool, or a demo for stakeholders. Choose Shiny when you need custom layouts, efficient reactivity for large datasets, or enterprise-grade deployment with access controls.",
     ["Prototyping", "Enterprise", "Use-Case Fit"]),
]

kc_tabs = [
    {
        "label": "Execution Model",
        "icon": "fa6-solid:bolt",
        "badge": "Architecture",
        "intro": "The fundamental difference between Streamlit and Shiny is how they run your code. Streamlit treats your Python file as a script that executes top-to-bottom on every user interaction. Shiny separates the interface definition (UI) from the business logic (server) and only re-runs the specific render functions whose inputs have changed.",
        "code": """# ── Streamlit: script re-runs top-to-bottom ──
import streamlit as st

st.title("My App")                       # runs every time
n = st.slider("Pick a number", 1, 100)   # runs every time
st.write(f"You picked: {n}")             # runs every time
# Change the slider → ALL lines above execute again

# ── Shiny: only affected outputs re-run ──
from shiny import App, ui, render

app_ui = ui.page_sidebar(
    ui.sidebar(ui.input_slider("n", "Pick a number", 1, 100, 50)),
    ui.card(ui.output_text("result")),    # placeholder
)

def server(input, output, session):
    @render.text
    def result():                         # only THIS re-runs
        return f"You picked: {input.n()}"

app = App(app_ui, server)""",
        "params": [
            ("st.title()", "function", "Writes a title — re-executes on every script re-run"),
            ("st.slider()", "function", "Creates a slider and returns its current value inline"),
            ("ui.input_slider()", "function", "Declares a slider in the UI — value read separately in server"),
            ("@render.text", "decorator", "Binds a server function to a text output placeholder"),
        ],
        "tip": "Streamlit's re-run model is simpler to learn, but for apps with expensive computations, Shiny's targeted re-execution avoids unnecessary work.",
    },
    {
        "label": "State Management",
        "icon": "fa6-solid:database",
        "badge": "Persistence",
        "intro": "Because Streamlit re-runs the entire script on every interaction, local variables reset each time. To persist values across re-runs, you must store them in <code>st.session_state</code>. Shiny uses <code>reactive.value()</code> objects that persist naturally within the server function's lifetime and only trigger updates when explicitly set.",
        "code": """# ── Streamlit: session_state for persistence ──
import streamlit as st

if "count" not in st.session_state:
    st.session_state.count = 0           # initialize once

if st.button("Add one"):
    st.session_state.count += 1          # mutate the state

st.write(f"Count: {st.session_state.count}")

# ── Shiny: reactive.value for persistence ──
from shiny import App, ui, render, reactive

app_ui = ui.page_sidebar(
    ui.sidebar(ui.input_action_button("add", "Add one")),
    ui.card(ui.output_text("count")),
)

def server(input, output, session):
    val = reactive.value(0)              # persists in server scope

    @reactive.effect
    @reactive.event(input.add)
    def _():
        val.set(val() + 1)              # update on button click

    @render.text
    def count():
        return f"Count: {val()}"

app = App(app_ui, server)""",
        "params": [
            ("st.session_state", "dict-like", "A per-session dictionary that survives Streamlit script re-runs"),
            ("reactive.value()", "function", "Creates a reactive container whose changes trigger downstream updates"),
            ("@reactive.event()", "decorator", "Limits a reactive effect to fire only when a specific input changes"),
            ("val.set()", "method", "Updates the reactive value and invalidates any outputs that read it"),
        ],
        "tip": "In Streamlit, forgetting <code>st.session_state</code> means your counter resets on every click. In Shiny, <code>reactive.value()</code> handles persistence automatically — but you must call <code>val()</code> with parentheses to read it.",
    },
    {
        "label": "Widget System",
        "icon": "fa6-solid:sliders",
        "badge": "Inputs &amp; Outputs",
        "intro": "Streamlit widgets return their current value inline — you call <code>st.slider()</code> and immediately get a number. Shiny separates widget declaration (in the UI) from value reading (in the server), which means the UI can be defined once while the server logic reacts to changes independently.",
        "code": """# ── Streamlit: widgets return values inline ──
import streamlit as st

name = st.text_input("Name", "World")     # returns string
color = st.selectbox("Color", ["Red", "Blue"])  # returns choice
n = st.slider("Amount", 1, 100, 50)       # returns int
st.write(f"Hello {name}, {color} x {n}")

# ── Shiny: declare in UI, read in server ──
from shiny import App, ui, render

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_text("name", "Name", "World"),
        ui.input_select("color", "Color", ["Red", "Blue"]),
        ui.input_slider("n", "Amount", 1, 100, 50),
    ),
    ui.card(ui.output_text("greeting")),
)

def server(input, output, session):
    @render.text
    def greeting():
        return f"Hello {input.name()}, {input.color()} x {input.n()}"

app = App(app_ui, server)""",
        "params": [
            ("st.text_input()", "function", "Renders a text box and returns the current string value"),
            ("st.selectbox()", "function", "Renders a dropdown and returns the selected option"),
            ("ui.input_text()", "function", "Declares a text input in Shiny's UI — read via input.id()"),
            ("input.name()", "method", "Reads the current value with parentheses — triggers reactive dependency"),
        ],
        "tip": "Streamlit's inline return is faster to write, but Shiny's separation means you can reorganize the UI layout without touching any server logic.",
    },
    {
        "label": "Layout &amp; Theming",
        "icon": "fa6-solid:table-columns",
        "badge": "Structure",
        "intro": "Streamlit arranges elements top-to-bottom by default and provides <code>st.columns()</code>, <code>st.tabs()</code>, and <code>st.sidebar</code> for basic layouts. Shiny offers a richer set of layout primitives — <code>ui.page_navbar()</code>, <code>ui.layout_sidebar()</code>, <code>ui.layout_columns()</code>, and <code>ui.card()</code> — giving you precise control over how every panel is sized and placed.",
        "code": """# ── Streamlit: quick layout helpers ──
import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide")

tab1, tab2 = st.tabs(["Chart", "Data"])
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Revenue", "$12,400", "+8%")
    with col2:
        st.metric("Users", "1,024", "+12%")
with tab2:
    st.dataframe(df)

# ── Shiny: explicit layout functions ──
from shiny import App, ui

app_ui = ui.page_navbar(
    ui.nav_panel("Chart",
        ui.layout_columns(
            ui.value_box("Revenue", "$12,400"),
            ui.value_box("Users", "1,024"),
        ),
    ),
    ui.nav_panel("Data",
        ui.card(ui.output_table("tbl")),
    ),
    title="Dashboard",
)""",
        "params": [
            ("st.columns()", "function", "Creates side-by-side columns — widths can be equal or custom ratios"),
            ("st.tabs()", "function", "Creates tabbed sections — content goes inside with-blocks"),
            ("ui.page_navbar()", "function", "Creates a top nav bar with multiple tab panels in Shiny"),
            ("ui.layout_columns()", "function", "Arranges child elements in responsive columns with gap control"),
        ],
        "tip": "Streamlit's layout is good enough for most prototypes. Switch to Shiny when you need pixel-level control, nested layouts, or value boxes with conditional theming.",
    },
    {
        "label": "Caching &amp; Performance",
        "icon": "fa6-solid:bolt-lightning",
        "badge": "Speed",
        "intro": "Both frameworks provide caching, but the mechanisms are different. Streamlit uses the <code>@st.cache_data</code> decorator to memoize function results based on input arguments. Shiny uses <code>@reactive.calc</code>, which automatically caches the result and only re-computes when the reactive inputs it reads have changed.",
        "code": """# ── Streamlit: decorator-based caching ──
import streamlit as st
import pandas as pd

@st.cache_data                    # cached across re-runs
def load_data():
    return pd.read_csv("sales.csv")

df = load_data()                  # instant after first call
dept = st.selectbox("Dept", df["dept"].unique())
st.dataframe(df[df["dept"] == dept])

# ── Shiny: reactive calc (auto-caches) ──
from shiny import App, ui, render, reactive
import pandas as pd

app_ui = ui.page_sidebar(
    ui.sidebar(ui.input_select("dept", "Dept", [])),
    ui.card(ui.output_table("tbl")),
)

def server(input, output, session):
    @reactive.calc               # re-runs only when inputs change
    def data():
        return pd.read_csv("sales.csv")

    @render.table
    def tbl():
        return data()[data()["dept"] == input.dept()]

app = App(app_ui, server)""",
        "params": [
            ("@st.cache_data", "decorator", "Caches the return value — subsequent calls with same args skip execution"),
            ("@st.cache_resource", "decorator", "Like cache_data but for non-serializable objects like DB connections"),
            ("@reactive.calc", "decorator", "Shiny's auto-cache — re-runs only when upstream reactive inputs change"),
            ("data()", "call", "Reading a reactive.calc result with parentheses registers the dependency"),
        ],
        "tip": "Streamlit caching is argument-based (same args &rarr; cached result). Shiny caching is dependency-based (same upstream inputs &rarr; cached result). For large datasets, both eliminate redundant computation.",
    },
]

code_examples = [
    {
        "title": "Streamlit Hello World",
        "desc": "The simplest possible Streamlit app — a title, a text input, and a greeting. Streamlit renders widgets top-to-bottom and re-runs the entire script whenever the text input changes.",
        "code": """import streamlit as st

st.title("Hello, World!")
st.write("This is my first Streamlit app.")

name = st.text_input("What is your name?", "World")
st.write(f"Hello, {name}!")""",
        "terminal_cmd": "streamlit run hello_streamlit.py",
        "terminal_out": "  You can now view your Streamlit app in your browser.\n  Local URL: http://localhost:8501",
        "tip": "Streamlit apps are plain Python scripts — no class definitions, no decorators, no constructor. Just write top-to-bottom and Streamlit turns it into a web page.",
    },
    {
        "title": "Shiny Hello World",
        "desc": "The same greeting app built with Shiny for Python. Notice the explicit separation between the UI (what the user sees) and the server (what happens when inputs change).",
        "code": """from shiny import App, ui, render

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_text("name", "What is your name?", "World"),
    ),
    ui.card(
        ui.h2("Hello, World!"),
        ui.p("This is my first Shiny app."),
        ui.output_text("greeting"),
    ),
)

def server(input, output, session):
    @render.text
    def greeting():
        return f"Hello, {input.name()}!"

app = App(app_ui, server)""",
        "terminal_cmd": "shiny run hello_shiny.py",
        "terminal_out": "  Uvicorn running on http://127.0.0.1:8000",
        "tip": "Shiny requires more structure upfront — a UI object, a server function, and an App constructor — but this separation pays off as your app grows more complex.",
    },
    {
        "title": "Streamlit Reactive Filter",
        "desc": "A Streamlit app that loads data, adds a dropdown filter, and displays a filtered table and metric. The entire script re-runs whenever the dropdown changes, but <code>@st.cache_data</code> prevents the CSV reload.",
        "code": """import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.DataFrame({
        "name": ["Alice", "Bob", "Carol", "Dave", "Eve"],
        "dept": ["Sales", "Eng", "Sales", "HR", "Eng"],
        "salary": [72000, 95000, 68000, 61000, 88000],
    })

df = load_data()

st.title("Employee Dashboard")
dept = st.selectbox("Department", ["All"] + sorted(df["dept"].unique()))

if dept == "All":
    filtered = df
else:
    filtered = df[df["dept"] == dept]

st.metric("Employees", len(filtered))
st.dataframe(filtered, use_container_width=True)""",
        "terminal_cmd": "streamlit run filter_streamlit.py",
        "terminal_out": "  You can now view your Streamlit app in your browser.\n  Local URL: http://localhost:8501",
        "tip": "Without <code>@st.cache_data</code>, the DataFrame would be recreated on every interaction. Caching keeps the app fast even when loading large files.",
    },
    {
        "title": "Shiny Reactive Filter",
        "desc": "The same employee dashboard built with Shiny. The <code>@reactive.calc</code> caches the filtered result, and both the table and the text output share it without redundant computation.",
        "code": """from shiny import App, ui, render, reactive
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "dept": ["Sales", "Eng", "Sales", "HR", "Eng"],
    "salary": [72000, 95000, 68000, 61000, 88000],
})

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select("dept", "Department",
                        ["All"] + sorted(df["dept"].unique().tolist())),
    ),
    ui.card(ui.output_text("count")),
    ui.card(ui.output_table("tbl")),
)

def server(input, output, session):
    @reactive.calc
    def filtered():
        if input.dept() == "All":
            return df
        return df[df["dept"] == input.dept()]

    @render.text
    def count():
        return f"{len(filtered())} employees"

    @render.table
    def tbl():
        return filtered()

app = App(app_ui, server)""",
        "terminal_cmd": "shiny run filter_shiny.py",
        "terminal_out": "  Uvicorn running on http://127.0.0.1:8000",
        "tip": "Both <code>count</code> and <code>tbl</code> call <code>filtered()</code>, but Shiny only runs the filter once per dropdown change — the second call gets the cached result. This is the key performance advantage of Shiny's reactive graph.",
    },
    {
        "title": "Side-by-Side Reference",
        "desc": "A reference file showing equivalent patterns in both frameworks. Use this as a quick-lookup when converting between Streamlit and Shiny or deciding which framework fits your project.",
        "code": """# ═══════════════════════════════════════════════════
# Streamlit vs Shiny — Quick Reference
# ═══════════════════════════════════════════════════

# ── App entry point ──────────────────────────────
# Streamlit: just run the script
#   streamlit run app.py
# Shiny: create App object, then run
#   shiny run app.py

# ── Read user input ──────────────────────────────
# Streamlit:  value = st.slider("Age", 0, 100)
# Shiny:      value = input.age()  # inside server

# ── Display output ───────────────────────────────
# Streamlit:  st.dataframe(df)
# Shiny:      @render.table + ui.output_table("id")

# ── Cache data ───────────────────────────────────
# Streamlit:  @st.cache_data
# Shiny:      @reactive.calc

# ── Multi-page layout ───────────────────────────
# Streamlit:  tab1, tab2 = st.tabs(["A", "B"])
# Shiny:      ui.page_navbar(ui.nav_panel("A"), ...)

# ── When to choose ──────────────────────────────
# Streamlit → quick prototypes, demos, exploration
# Shiny     → production dashboards, complex reactivity""",
        "terminal_cmd": "python decision_guide.py",
        "terminal_out": "# This file is a reference guide — no executable output.",
        "tip": "Keep this reference handy when starting a new project. The framework choice should match your project's complexity and deployment requirements, not personal preference.",
    },
]

# Comparison rows: (icon, label, st_code, st_desc, sh_code, sh_desc, diff_code, diff_desc)
comparison_rows = [
    ("fa6-solid:play",          "App Entry Point",
     "streamlit run app.py",       "Script executes top-to-bottom — no constructor needed",
     "App(app_ui, server)",        "Explicit UI + server constructor passed to App()",
     "Script vs Object",           "Streamlit is a script; Shiny is an application object"),
    ("fa6-solid:sliders",       "Read User Input",
     "st.slider('Age', 0, 100)",   "Returns the value inline where you call it",
     "input.age()",                "Read inside server with parentheses — registers dependency",
     "Inline vs Reactive",         "Streamlit returns immediately; Shiny tracks dependencies"),
    ("fa6-solid:display",       "Display Output",
     "st.dataframe(df)",           "Call a display function anywhere in the script",
     "@render.table",              "Decorator binds function to a UI placeholder by name",
     "Direct vs Bound",            "Streamlit prints inline; Shiny links function to placeholder"),
    ("fa6-solid:bolt-lightning", "Cache Data",
     "@st.cache_data",             "Decorator memoizes by function arguments across re-runs",
     "@reactive.calc",             "Auto-caches result until upstream reactive inputs change",
     "Args vs Dependencies",       "Streamlit keys on args; Shiny keys on reactive reads"),
    ("fa6-solid:layer-group",   "Multi-Page Layout",
     "st.tabs(['A', 'B'])",        "Built-in tabs — content goes inside with-blocks",
     "ui.page_navbar()",           "Layout function with explicit nav panels",
     "Built-in vs Composable",     "Streamlit uses context managers; Shiny uses nested functions"),
]

practice_exercises = [
    {
        "title": "Streamlit Counter App",
        "tasks": [
            "Create a new file called <code>counter_st.py</code> and import <code>streamlit as st</code>.",
            "Add a title with <code>st.title('Counter')</code>.",
            "Initialize <code>st.session_state.count</code> to <code>0</code> if it does not already exist.",
            "Add a button with <code>st.button('Add one')</code> that increments the counter.",
            "Display the current count with <code>st.metric('Count', st.session_state.count)</code>.",
        ],
        "solution": """import streamlit as st

st.title("Counter")

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Add one"):
    st.session_state.count += 1

st.metric("Count", st.session_state.count)""",
        "why": "This exercise shows why <code>st.session_state</code> is essential in Streamlit — without it, the count resets to zero on every button click because the script re-runs from scratch.",
    },
    {
        "title": "Shiny Counter App",
        "tasks": [
            "Create a new file called <code>counter_shiny.py</code> and import <code>App</code>, <code>ui</code>, <code>render</code>, and <code>reactive</code> from shiny.",
            "Define <code>app_ui</code> with an action button (<code>ui.input_action_button('add', 'Add one')</code>) and a text output.",
            "In the server function, create a <code>reactive.value(0)</code> to hold the count.",
            "Add a <code>@reactive.effect</code> decorated with <code>@reactive.event(input.add)</code> that increments the value.",
            "Add a <code>@render.text</code> function that displays the current count.",
        ],
        "solution": """from shiny import App, ui, render, reactive

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_action_button("add", "Add one"),
    ),
    ui.card(ui.output_text("count")),
)

def server(input, output, session):
    val = reactive.value(0)

    @reactive.effect
    @reactive.event(input.add)
    def _():
        val.set(val() + 1)

    @render.text
    def count():
        return f"Count: {val()}"

app = App(app_ui, server)""",
        "why": "Compare this with the Streamlit version — Shiny does not need <code>session_state</code> because <code>reactive.value()</code> persists naturally inside the server function. The tradeoff is more boilerplate code.",
    },
    {
        "title": "Cached Data Loading",
        "tasks": [
            "Create a Streamlit app that defines a <code>load_data()</code> function decorated with <code>@st.cache_data</code>.",
            "Inside the function, create and return a sample DataFrame with columns: product, region, and revenue.",
            "Add a <code>st.selectbox()</code> filter for the region column with an \"All\" option.",
            "Display the filtered DataFrame with <code>st.dataframe()</code> and a row-count metric with <code>st.metric()</code>.",
        ],
        "solution": """import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.DataFrame({
        "product": ["Widget", "Gadget", "Widget", "Gizmo", "Gadget"],
        "region": ["North", "South", "South", "North", "North"],
        "revenue": [1200, 3400, 1800, 2200, 2900],
    })

df = load_data()

st.title("Sales Dashboard")
region = st.selectbox("Region", ["All"] + sorted(df["region"].unique()))

filtered = df if region == "All" else df[df["region"] == region]

st.metric("Total Revenue", f"${filtered['revenue'].sum():,}")
st.dataframe(filtered, use_container_width=True)""",
        "why": "The <code>@st.cache_data</code> decorator ensures the DataFrame is created once and reused across every script re-run. Without it, even a small DataFrame would be rebuilt on every slider or dropdown change.",
    },
    {
        "title": "Convert Streamlit to Shiny",
        "tasks": [
            "Take the cached data loading app from Exercise 3 and rewrite it in Shiny.",
            "Replace <code>@st.cache_data</code> with a module-level DataFrame (static data does not need reactive caching).",
            "Replace <code>st.selectbox()</code> with <code>ui.input_select()</code> in the sidebar.",
            "Add a <code>@reactive.calc</code> for the filtered DataFrame.",
            "Add <code>@render.text</code> for the revenue metric and <code>@render.table</code> for the table.",
        ],
        "solution": """from shiny import App, ui, render, reactive
import pandas as pd

df = pd.DataFrame({
    "product": ["Widget", "Gadget", "Widget", "Gizmo", "Gadget"],
    "region": ["North", "South", "South", "North", "North"],
    "revenue": [1200, 3400, 1800, 2200, 2900],
})

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select("region", "Region",
                        ["All"] + sorted(df["region"].unique().tolist())),
    ),
    ui.card(ui.output_text("revenue")),
    ui.card(ui.output_table("tbl")),
)

def server(input, output, session):
    @reactive.calc
    def filtered():
        if input.region() == "All":
            return df
        return df[df["region"] == input.region()]

    @render.text
    def revenue():
        total = filtered()["revenue"].sum()
        return f"Total Revenue: ${total:,}"

    @render.table
    def tbl():
        return filtered()

app = App(app_ui, server)""",
        "why": "Converting between frameworks is a valuable skill. Notice how Streamlit's inline <code>st.selectbox()</code> becomes a separate UI declaration and server read in Shiny — this is the core architectural difference you will encounter on every conversion.",
    },
    {
        "title": "Multi-Tab Dashboard",
        "tasks": [
            "Choose either Streamlit or Shiny and build a two-tab dashboard.",
            "Tab 1 (\"Summary\") should display two metric cards: total revenue and average revenue.",
            "Tab 2 (\"Details\") should display the full DataFrame as a table.",
            "Add a filter (selectbox or input_select) for the region column that affects both tabs.",
            "If using Streamlit, use <code>st.tabs()</code>. If using Shiny, use <code>ui.page_navbar()</code>.",
        ],
        "solution": """import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.DataFrame({
        "product": ["Widget", "Gadget", "Widget", "Gizmo", "Gadget"],
        "region": ["North", "South", "South", "North", "North"],
        "revenue": [1200, 3400, 1800, 2200, 2900],
    })

df = load_data()

st.title("Sales Dashboard")
region = st.selectbox("Region", ["All"] + sorted(df["region"].unique()))

filtered = df if region == "All" else df[df["region"] == region]

tab1, tab2 = st.tabs(["Summary", "Details"])

with tab1:
    col1, col2 = st.columns(2)
    col1.metric("Total Revenue", f"${filtered['revenue'].sum():,}")
    col2.metric("Avg Revenue", f"${filtered['revenue'].mean():,.0f}")

with tab2:
    st.dataframe(filtered, use_container_width=True)""",
        "why": "Building a multi-tab dashboard is where you feel the difference between frameworks. Streamlit's <code>st.tabs()</code> with context managers is quick to write. Shiny's <code>ui.page_navbar()</code> with <code>ui.nav_panel()</code> is more verbose but scales better when you add five or more tabs.",
    },
]

mistakes = [
    {
        "title": "Forgetting st.session_state in Streamlit",
        "why_happens": "Beginners expect local variables to persist across re-runs, but Streamlit re-executes the entire script on every interaction.",
        "wrong": """import streamlit as st

count = 0                           # resets to 0 every re-run

if st.button("Add one"):
    count += 1                      # increments to 1...
                                    # then script re-runs and count = 0 again
st.write(f"Count: {count}")         # always shows 0 or 1""",
        "correct": """import streamlit as st

if "count" not in st.session_state:
    st.session_state.count = 0      # initialize once

if st.button("Add one"):
    st.session_state.count += 1     # persists across re-runs

st.write(f"Count: {st.session_state.count}")""",
        "fix": "Use <code>st.session_state</code> for any value that must survive across widget interactions. Initialize it with an <code>if not in</code> guard to avoid resetting on every re-run.",
    },
    {
        "title": "Calling input.n Instead of input.n() in Shiny",
        "why_happens": "Shiny inputs are reactive objects, not plain values. Without parentheses, you get the signal object instead of the actual number.",
        "wrong": """# Shiny server
@render.text
def result():
    return f"Value: {input.n}"      # BUG: prints <reactive object>""",
        "correct": """# Shiny server
@render.text
def result():
    return f"Value: {input.n()}"    # Correct: returns the number""",
        "fix": "Always call Shiny inputs with parentheses — <code>input.n()</code> not <code>input.n</code>. The parentheses trigger the reactive read and return the current value.",
    },
    {
        "title": "Using plt.show() in Either Framework",
        "why_happens": "In Jupyter notebooks, plt.show() displays the chart. But in both Streamlit and Shiny, you need to pass or return the figure object instead.",
        "wrong": """import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.bar(["A", "B"], [10, 20])
plt.show()                        # BUG: no output in the web app
# Streamlit needs st.pyplot(fig)
# Shiny needs return fig inside @render.plot""",
        "correct": """# Streamlit — pass figure to st.pyplot()
fig, ax = plt.subplots()
ax.bar(["A", "B"], [10, 20])
st.pyplot(fig)                    # Correct for Streamlit

# Shiny — return fig from @render.plot
@render.plot
def chart():
    fig, ax = plt.subplots()
    ax.bar(["A", "B"], [10, 20])
    return fig                    # Correct for Shiny""",
        "fix": "In Streamlit, pass the figure to <code>st.pyplot(fig)</code>. In Shiny, <code>return fig</code> from a <code>@render.plot</code> function. Never call <code>plt.show()</code> in either framework.",
    },
    {
        "title": "Caching Functions with Side Effects",
        "why_happens": "Decorating a function with @st.cache_data that modifies external state means the side effect only happens on the first call — cached calls skip the function body entirely.",
        "wrong": """import streamlit as st
import pandas as pd

@st.cache_data
def load_and_log(path):
    df = pd.read_csv(path)
    with open("log.txt", "a") as f:     # side effect!
        f.write(f"Loaded {path}\\n")     # only logs ONCE
    return df                            # cached — never runs again""",
        "correct": """import streamlit as st
import pandas as pd

@st.cache_data
def load_data(path):
    return pd.read_csv(path)             # pure function — safe to cache

def log_access(path):                    # separate, non-cached function
    with open("log.txt", "a") as f:
        f.write(f"Loaded {path}\\n")

df = load_data("sales.csv")
log_access("sales.csv")                  # runs every time""",
        "fix": "Keep cached functions pure — they should only compute and return a value. Move side effects (logging, file writes, API calls) into separate non-cached functions that run on every script execution.",
    },
    {
        "title": "Mixing Up Framework Patterns",
        "why_happens": "After learning both frameworks, it is easy to accidentally use Streamlit syntax inside a Shiny app or vice versa.",
        "wrong": """# Accidentally using Streamlit syntax in Shiny
from shiny import App, ui, render

def server(input, output, session):
    @render.text
    def result():
        import streamlit as st          # BUG: wrong framework
        return st.write(input.n())      # st.write does not work here""",
        "correct": """# Correct Shiny pattern — no Streamlit imports
from shiny import App, ui, render

def server(input, output, session):
    @render.text
    def result():
        return f"Value: {input.n()}"    # plain return, Shiny renders it""",
        "fix": "Never import one framework inside the other. If your file starts with <code>from shiny import</code>, use <code>@render.*</code> decorators. If it starts with <code>import streamlit as st</code>, use <code>st.*</code> functions.",
    },
]

real_world = [
    ("fa6-solid:chart-line",     "Quick Executive Dashboards",     "Streamlit excels at rapid prototyping — data analysts build revenue dashboards in under an hour and share them via Streamlit Community Cloud for immediate stakeholder feedback."),
    ("fa6-solid:building",       "Enterprise Production Apps",      "Large organizations choose Shiny when they need role-based access controls, custom theming, and deployment on Posit Connect with IT-managed infrastructure."),
    ("fa6-solid:flask",          "Data Science Exploration",        "Research teams use Streamlit to quickly visualize model outputs, compare experiment results, and share interactive reports with colleagues via a simple URL."),
    ("fa6-solid:hospital",       "Regulated Industry Dashboards",   "Healthcare and finance companies prefer Shiny's server-side rendering because sensitive data never reaches the browser — only the rendered output is sent to the client."),
    ("fa6-solid:users",          "Customer-Facing Portals",         "Both frameworks power customer portals — Streamlit for simpler self-service tools and Shiny for complex multi-tab applications that require precise layout control."),
    ("fa6-solid:graduation-cap", "Teaching and Training Tools",     "Educators build interactive coding exercises with Streamlit for its low learning curve, while university departments use Shiny for advanced statistical visualization labs."),
]

quiz = [
    {
        "type": "tf",
        "stem": "Streamlit re-runs your entire Python script from top to bottom every time a widget value changes.",
        "answer": True,
        "fb_correct": "Correct! Streamlit's execution model re-runs the full script on every interaction — that is why caching and session_state are important.",
        "fb_wrong": "Not quite — Streamlit does re-run the entire script on every widget change. This is the fundamental difference from Shiny's targeted reactive model.",
    },
    {
        "type": "tf",
        "stem": "In Shiny for Python, you must manually tell the framework which outputs depend on which inputs by writing explicit dependency declarations.",
        "answer": False,
        "fb_correct": "Correct! Shiny automatically tracks dependencies — when a render function calls input.n(), Shiny records that dependency and re-runs the function when n changes.",
        "fb_wrong": "Not quite — Shiny infers dependencies automatically. When your render function reads input.n(), Shiny knows to re-run it when n changes. No manual declarations needed.",
    },
    {
        "type": "mc",
        "stem": "Which Streamlit function caches a DataFrame so it is not rebuilt on every script re-run?",
        "options": [
            ("st.session_state", False),
            ("@st.cache_data", True),
            ("@reactive.calc", False),
            ("st.write()", False),
        ],
        "fb_correct": "Correct! @st.cache_data memoizes the return value based on the function's input arguments, so subsequent calls skip the computation.",
        "fb_wrong": "Not quite — @st.cache_data is Streamlit's caching decorator. st.session_state stores state but does not cache function results. @reactive.calc is Shiny, not Streamlit.",
    },
    {
        "type": "mc",
        "stem": "In Shiny, you have a slider with <code>id='sample_size'</code>. Which expression correctly reads its current value inside the server function?",
        "options": [
            ("input.sample_size", False),
            ("input.sample_size()", True),
            ("st.slider('sample_size')", False),
            ("ui.input_slider('sample_size')", False),
        ],
        "fb_correct": "Correct! input.sample_size() with parentheses returns the current value and registers a reactive dependency.",
        "fb_wrong": "Not quite — you must call input.sample_size() with parentheses. Without them, you get the reactive signal object, not the actual value.",
    },
    {
        "type": "mc",
        "stem": "When would Shiny be a better choice than Streamlit for a new project?",
        "options": [
            ("When you need a quick one-page prototype for a demo", False),
            ("When the app has complex reactivity and needs fine-grained layout control", True),
            ("When you want the simplest possible code with no boilerplate", False),
            ("When you only need to display a static DataFrame", False),
        ],
        "fb_correct": "Correct! Shiny's explicit reactive graph and layout system give you the control needed for complex production dashboards.",
        "fb_wrong": "Not quite — Shiny shines when you need complex reactivity and precise layout control. For quick prototypes, Streamlit is usually faster.",
    },
]

sidebar_lessons = [
    ("lesson01_why_build_data_apps.html",         "Why Build Data Apps?"),
    ("lesson02_introduction_to_streamlit.html",   "Introduction to Streamlit"),
    ("lesson03_interactive_filters.html",         "Interactive Filters"),
    ("lesson04_exporting_data.html",              "Exporting Data"),
    ("lesson05_deploying_data_applications.html", "Deploying Data Applications"),
    ("lesson06_shiny_for_python.html",            "Shiny for Python"),
    ("lesson07_streamlit_vs_shiny.html",          "Streamlit vs Shiny"),
]

# ═══════════════════════════════════════════════════════════
# BUILDER — CSS, HERO, Helpers, Sections, JS, Assembly
# ═══════════════════════════════════════════════════════════

def e(s):
    """HTML-escape helper."""
    return htmlmod.escape(s)

def indent(html, n=6):
    pad = " " * n
    return "\n".join(pad + line if line.strip() else line for line in html.split("\n"))

CSS = """<style>
/* ── CSS Variables — font tokens (:root) ──────────────────── */
:root { --font-body: 'Inter', -apple-system, 'Segoe UI', Roboto, sans-serif; --font-mono: 'Fira Code', monospace; }

/* ── Global reset — smooth scroll ─────────────────────────── */
* { scroll-behavior: smooth; }

/* ── Prism.js — syntax highlighted code blocks ────────────── */
pre[class*="language-"], code[class*="language-"] { font-family: var(--font-mono); font-size: 0.82rem; line-height: 1.7; }
pre[class*="language-"] { margin: 0; padding: 1.1rem 1.25rem; border-radius: 0; background: #1e1e2e; }

/* ── Heading resets — strip Confluence default margins ────── */
h1, h2, h3, h4, h5, h6 { margin: 0; padding: 0; font-family: var(--font-body); }

/* ── Brand utility classes ────────────────────────────────── */
.text-brand { color: #CB187D; }
.bg-brand { background-color: #CB187D; }
.bg-brand-soft { background-color: #fdf0f7; }
.brand-soft-panel { background: #fdf0f7; border: 1px solid #f5c6e0; border-radius: 0.75rem; padding: 1rem 1.25rem; }
.bg-amber-tip { background: #fffbeb; border-color: #fde68a; }
.bg-code { background: #1e1e2e; }
.border-code-sep { border-color: rgba(255,255,255,0.06); }
.pre-reset { margin: 0; padding: 1rem 1.25rem; background: transparent; }

/* ── Key Concepts sidebar tabs (.kc-tab / .kc-tab-active) ── */
.kc-tab-active { background: #fdf0f7; }
.kc-tab:not(.kc-tab-active):hover { background: #f9fafb; }
.kc-panel-anim { animation: kcFadeIn 0.25s ease; }
@keyframes kcFadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

/* ── Code Examples pill tabs (.ce-step / .ce-step-active) ── */
.ce-step:not(.ce-step-active):hover { background: #374151 !important; color: #d1d5db !important; }
.ce-panel-anim { animation: kcFadeIn 0.25s ease; }

/* ── Common Mistakes pill tabs (.mk-step / .mk-step-active) */
.mk-step:not(.mk-step-active):hover { background: #374151 !important; color: #d1d5db !important; }
.mk-panel-anim { animation: kcFadeIn 0.25s ease; }

/* ── Knowledge Check quiz tabs (.qz-step / .qz-step-active) */
.qz-step:not(.qz-step-active):hover { background: #374151 !important; color: #d1d5db !important; }
.qz-panel-anim { animation: kcFadeIn 0.25s ease; }

/* ── Practice Exercise tabs (.pe-step / .pe-step-active) ── */
.pe-step:not(.pe-step-active):hover { background: #374151 !important; color: #d1d5db !important; }
.pe-panel-anim { animation: kcFadeIn 0.25s ease; }
.task-box { background: #fdf0f7; border: 1px solid #f5c6e0; border-radius: 0.75rem; }

/* ── Accordion — used in Overview & Key Ideas sections ──── */
.accordion-body { display: none !important; }
.accordion-body.open { display: block !important; }
.accordion-toggle { display: inline-flex; align-items: center; gap: 8px; padding: 8px 18px; font-size: 0.82rem; font-weight: 600; cursor: pointer; border: 1.5px solid #e5e7eb; border-radius: 999px; color: #6b7280; background: #fff; transition: color 0.15s, background 0.15s, border-color 0.15s; }
.accordion-toggle:hover, .accordion-toggle.open { color: #CB187D; border-color: #CB187D; background: #fdf0f7; }
.accordion-chevron { transition: transform 0.2s ease; }
.accordion-toggle.open .accordion-chevron { transform: rotate(180deg); }

/* ── Hero banner — full-width gradient header ─────────────── */
.hero-container { position: relative; border-radius: 1.5rem; overflow: hidden; background: linear-gradient(135deg, #0f0518 0%, #1a0a2e 25%, #2d1143 50%, #1e0830 75%, #0a0312 100%); min-height: 340px; }
.hero-dots { position: absolute; inset: 0; background-image: radial-gradient(rgba(255,255,255,0.04) 1px, transparent 1px); background-size: 20px 20px; }
.hero-glow { position: absolute; border-radius: 50%; filter: blur(100px); pointer-events: none; }
.hero-pill { background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.08); color: #f5c6e0; pointer-events: none; cursor: default; }
.hero-abstract-card { position: absolute; right: 5%; top: 12%; width: 240px; border-radius: 1rem; padding: 1.25rem; background: rgba(255,255,255,0.03); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.06); }
.hero-cta { display: inline-flex; align-items: center; gap: 8px; padding: 10px 26px; border-radius: 999px; background: linear-gradient(135deg, #CB187D, #e84aad); color: #fff; font-weight: 700; font-size: 0.85rem; text-decoration: none; transition: transform 0.2s, box-shadow 0.2s; box-shadow: 0 6px 24px rgba(203,24,125,0.35); }
.hero-cta:hover { transform: translateY(-2px); box-shadow: 0 8px 30px rgba(203,24,125,0.5); }
.stat-card { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.06); border-radius: 0.75rem; padding: 0.75rem 1rem; }

/* ── Scroll progress bar — fixed top-of-page indicator ──── */
.scroll-progress { position: fixed; top: 0; left: 0; height: 3px; background: linear-gradient(90deg, #CB187D, #e84aad, #CB187D); background-size: 200% 100%; animation: scrollGradient 2s linear infinite; z-index: 9999; transition: width 0.15s ease-out; }
@keyframes scrollGradient { 0% { background-position: 0% 0; } 100% { background-position: 200% 0; } }

/* ── Page layout — two-column: TOC sidebar + main content ── */
.lesson-layout { display: flex; gap: 1.75rem; align-items: flex-start; }
.lesson-toc-sidebar { width: 240px; flex-shrink: 0; position: sticky; top: 1.5rem; max-height: calc(100vh - 2rem); overflow-y: auto; transition: width 0.25s ease, opacity 0.25s ease; }
.lesson-toc-sidebar.toc-collapsed { width: 0; opacity: 0; overflow: hidden; }
.toc-toggle-btn { margin-left: auto; background: none; border: none; cursor: pointer; color: #9ca3af; transition: color 0.15s; display: flex; align-items: center; }
.toc-toggle-btn:hover { color: #CB187D; }
.toc-link { transition: color 0.15s, background 0.15s; }
.toc-link.active { color: #CB187D; font-weight: 600; border-left: 3px solid #CB187D; padding-left: 8px; background-color: #fdf0f7; }

/* ── Objective cards (.obj-card) ──────────────────────────── */
.obj-card { transition: box-shadow 0.22s cubic-bezier(.4,0,.2,1), border-color 0.22s ease, background-color 0.22s ease; }
.obj-card:hover { box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08); border-color: #f5c6e0; background-color: #ffffff; }
.obj-card .obj-icon { transition: transform 0.22s cubic-bezier(.4,0,.2,1), background-color 0.22s ease; }
.obj-card:hover .obj-icon { transform: scale(1.1); background-color: #CB187D; }
.obj-card:hover .obj-icon .iconify { color: white !important; }
#key-ideas .obj-card:hover { border-color: #f3f4f6; background-color: #ffffff; box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08); }
#key-ideas .obj-card:hover .obj-icon { transform: scale(1.1); background-color: revert; }

/* ── Generic outline tab buttons (.tab-btn / .tab-panel) ── */
.tab-btn { display:inline-flex; align-items:center; gap:6px; padding:7px 18px; font-size:0.82rem; font-weight:600; cursor:pointer; border:1.5px solid #e5e7eb; border-radius:999px; color:#6b7280; background:#fff; line-height:1.2; transition:color 0.15s, background 0.15s, border-color 0.15s; }
.tab-btn:hover { color:#CB187D; border-color:#CB187D; background:#fdf0f7; }
.tab-btn.active { color:#fff; background:#CB187D; border-color:#CB187D; }
.tab-panel { display:none; } .tab-panel.active { display:block; }

/* ── Code block copy button (.copy-btn) ───────────────────── */
.copy-btn { position:absolute; top:10px; right:12px; display:inline-flex; align-items:center; background:rgba(203,24,125,0.15); border:1px solid rgba(203,24,125,0.3); color:#CB187D; border-radius:6px; padding:3px 8px; font-size:0.65rem; font-weight:600; cursor:pointer; transition:background 0.2s; white-space:nowrap; }
.copy-btn:hover { background:rgba(203,24,125,0.3); }
.copy-btn-light { position:static; color:#fff; border-color:rgba(255,255,255,0.25); background:rgba(255,255,255,0.1); }
.copy-btn-light:hover { background:rgba(255,255,255,0.2); }

/* ── Bottom lesson navigation — Previous / All Lessons / Next */
.lesson-nav-link:hover p, .lesson-nav-link:hover span, .lesson-nav-link:hover svg { color:#CB187D; transition:color 0.15s; }

/* ── Back-to-top floating button ──────────────────────────── */
.back-to-top { position:fixed; bottom:2rem; right:2rem; width:44px; height:44px; border-radius:50%; background:#CB187D; color:white; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(203,24,125,0.3); cursor:pointer; opacity:0; transform:translateY(10px); transition:opacity 0.3s, transform 0.3s; z-index:50; border:none; }
.back-to-top.visible { opacity:1; transform:translateY(0); }
.back-to-top:hover { background:#7F004C; }

/* ── Quiz answer feedback buttons (.quiz-btn.correct / .incorrect) */
.quiz-btn.correct { background:#f0fdf4; border-color:#22c55e; color:#16a34a; }
.quiz-btn.incorrect { background:#fef2f2; border-color:#ef4444; color:#dc2626; }

/* ── Card hover animations — Mistake, Flow, Recap, Overview cards */
.mistake-card { transition: transform 0.18s ease, box-shadow 0.18s ease; }
.mistake-card:hover { transform: translateY(-2px); box-shadow: 0 8px 25px -5px rgba(0,0,0,0.08); }

/* ── Responsive — mobile breakpoint (<768px) ──────────────── */
@media (max-width: 767px) { .lesson-toc-sidebar { display:none; } .lesson-layout { display:block; } .hero-container { min-height:auto; } .hero-split { flex-direction:column !important; } }

/* ── Print styles — hide interactive chrome when printing ─── */
@media print { .lesson-toc-sidebar, .back-to-top, .scroll-progress, .copy-btn, .hero-container { display:none; } .obj-card:hover { transform:none; box-shadow:none; } }

/* ── Iconify icon alignment utility ───────────────────────── */
.iconify { vertical-align: middle; flex-shrink: 0; }

/* ═══ Confluence Hub-Root Isolation Block ═══════════════════ */
#hub-root a.hero-pill { color: #CB187D !important; }
#hub-root .hero-pill .opacity-55 { opacity: 1 !important; }
#hub-root .hero-pill .opacity-50 { opacity: 1 !important; }
#hub-root .toc-link:hover { color: #CB187D !important; }
#hub-root .toc-link.active { color: #CB187D !important; font-weight: 600 !important; border-left: 3px solid #CB187D !important; padding-left: 8px !important; background-color: #fdf0f7 !important; }
#hub-root .mod-lesson-active { background-color: #fdf0f7 !important; border-color: #CB187D !important; color: #CB187D !important; }
#hub-root .mod-lesson-active .lesson-dot { background-color: #CB187D !important; }
#hub-root .ce-step, #hub-root .mk-step, #hub-root .qz-step, #hub-root .pe-step { display:inline-flex !important; align-items:center !important; gap:0.5rem !important; padding:0.375rem 1rem !important; border-radius:9999px !important; font-size:0.75rem !important; font-weight:700 !important; line-height:1.2 !important; white-space:nowrap !important; border:none !important; cursor:pointer !important; }
#hub-root .ce-step:not(.ce-step-active), #hub-root .mk-step:not(.mk-step-active), #hub-root .qz-step:not(.qz-step-active), #hub-root .pe-step:not(.pe-step-active) { background-color:#1f2937 !important; color:#ffffff !important; box-shadow:none !important; }
#hub-root .ce-step-active, #hub-root .mk-step-active, #hub-root .qz-step-active, #hub-root .pe-step-active { background:linear-gradient(to right,#CB187D,#e84aad) !important; color:#ffffff !important; box-shadow:0 10px 25px -5px rgba(203,24,125,0.3) !important; }
#hub-root .obj-card:hover { border-color: #f5c6e0 !important; box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08) !important; background-color: #ffffff !important; }
#hub-root .obj-card:hover .obj-icon { background: #CB187D !important; }
#hub-root .obj-card:hover .obj-icon .iconify { color: #ffffff !important; }
/* ── Key Takeaway cards — keep border gray and icon gradient on hover ── */
#hub-root #key-ideas .obj-card:hover { border-color: #f3f4f6 !important; background-color: #ffffff !important; box-shadow: 0 4px 12px -2px rgba(0,0,0,0.08) !important; }
#hub-root #key-ideas .obj-card:hover .obj-icon { background: revert !important; }
#hub-root .section-header { display:flex !important; align-items:center !important; gap:1rem !important; padding:1.25rem 2rem 1.25rem 1rem !important; background:#ffffff !important; border-bottom:1px solid #f3f4f6 !important; border-left:4px solid #CB187D !important; }
#hub-root .section-icon { display:inline-flex !important; align-items:center !important; justify-content:center !important; width:2.75rem !important; height:2.75rem !important; border-radius:0.75rem !important; background:#CB187D !important; flex-shrink:0 !important; }
#hub-root .section-title { font-size:1.25rem !important; font-weight:700 !important; color:#111827 !important; }
#hub-root .section-subtitle { font-size:0.875rem !important; color:#9ca3af !important; }
#hub-root .lesson-nav-link:hover p, #hub-root .lesson-nav-link:hover span, #hub-root .lesson-nav-link:hover svg { color: #CB187D !important; transition: color 0.15s !important; }
</style>"""

# ── HERO SVG ──────────────────────────────────────────────
HERO_SVG = """<svg viewBox="0 0 280 324" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-full h-auto" style="max-height:320px;" aria-hidden="true">
  <defs>
    <linearGradient id="hexFill" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1a0a12"/><stop offset="45%" stop-color="#2d0a1e"/><stop offset="100%" stop-color="#0d0610"/></linearGradient>
    <linearGradient id="hexBorder" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#CB187D"/><stop offset="50%" stop-color="#e84aad"/><stop offset="100%" stop-color="#CB187D"/></linearGradient>
    <radialGradient id="hexGlow" cx="50%" cy="38%" r="45%"><stop offset="0%" stop-color="#CB187D" stop-opacity="0.18"/><stop offset="100%" stop-color="#CB187D" stop-opacity="0"/></radialGradient>
    <radialGradient id="pyGlow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#FFD43B" stop-opacity="0.12"/><stop offset="100%" stop-color="#FFD43B" stop-opacity="0"/></radialGradient>
    <clipPath id="hexClip"><polygon points="140,14 268,88 268,236 140,310 12,236 12,88"/></clipPath>
  </defs>
  <polygon points="140,14 268,88 268,236 140,310 12,236 12,88" fill="url(#hexFill)"/>
  <polygon points="140,14 268,88 268,236 140,310 12,236 12,88" fill="url(#hexGlow)"/>
  <g clip-path="url(#hexClip)" opacity="1">
    <g opacity="0.06"><circle cx="40" cy="100" r="1.2" fill="white"/><circle cx="60" cy="100" r="1.2" fill="white"/><circle cx="80" cy="100" r="1.2" fill="white"/><circle cx="100" cy="100" r="1.2" fill="white"/><circle cx="120" cy="100" r="1.2" fill="white"/><circle cx="160" cy="100" r="1.2" fill="white"/><circle cx="180" cy="100" r="1.2" fill="white"/><circle cx="200" cy="100" r="1.2" fill="white"/><circle cx="220" cy="100" r="1.2" fill="white"/><circle cx="240" cy="100" r="1.2" fill="white"/></g>
    <g opacity="0.08" fill="white" font-family="'Fira Code',monospace" font-size="7"><text x="42" y="145">&gt;&gt;&gt; import pandas</text><text x="185" y="92">def main():</text><text x="38" y="92">class Data:</text></g>
    <g opacity="0.15" stroke="#FFD43B" stroke-width="1.5" fill="none" stroke-linecap="round"><polyline points="52,72 42,72 42,85"/><polyline points="228,72 238,72 238,85"/><polyline points="52,252 42,252 42,239"/><polyline points="228,252 238,252 238,239"/></g>
    <circle cx="140" cy="145" r="55" fill="url(#pyGlow)"/>
  </g>
  <polygon points="140,14 268,88 268,236 140,310 12,236 12,88" fill="none" stroke="url(#hexBorder)" stroke-width="4" stroke-linejoin="round"/>
  <foreignObject x="95" y="85" width="90" height="90"><div xmlns="http://www.w3.org/1999/xhtml" style="display:flex;align-items:center;justify-content:center;width:100%;height:100%;"><span class="iconify" data-icon="logos:python" style="font-size:70px;filter:drop-shadow(0 0 14px rgba(255,212,59,0.25));"></span></div></foreignObject>
  <text x="140" y="205" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-weight="800" font-size="30" letter-spacing="4" opacity="0.95">PYTHON</text>
  <text x="140" y="230" text-anchor="middle" fill="#f5c6e0" font-family="Inter,sans-serif" font-weight="600" font-size="14" letter-spacing="5" opacity="0.8">LEARNING HUB</text>
  <line x1="85" y1="185" x2="195" y2="185" stroke="#CB187D" stroke-width="1" stroke-opacity="0.35" stroke-linecap="round"/>
</svg>"""

# ═══════════════════════════════════════════════════════════
# HTML generation helpers
# ═══════════════════════════════════════════════════════════

def section_header(icon, title, subtitle):
    return f"""<div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
  <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
    <span class="iconify text-white text-base" data-icon="{icon}"></span>
  </span>
  <div class="min-w-0">
    <h2 class="text-xl font-bold text-gray-900 leading-tight">{title}</h2>
    <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">{subtitle}</p>
  </div>
</div>"""

def amber_tip(text):
    return f"""<div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
  <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
  <p class="text-sm text-gray-600">{text}</p>
</div>"""

def style_a_code(filename, code, terminal_cmd=None, terminal_out=None):
    """Style A dark-chrome code block with optional terminal pane."""
    lang = "bash" if filename.endswith(".sh") else "python"
    icon = "fa6-solid:terminal" if lang == "bash" else "logos:python"
    terminal_html = ""
    if terminal_cmd and terminal_out:
        terminal_html = f"""
  <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
    <div class="flex items-center gap-2 mb-1.5">
      <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
      <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
      <span class="text-[10px] text-gray-600 font-mono">$ {terminal_cmd}</span>
    </div>
    <div class="font-mono text-xs text-emerald-400 leading-relaxed">{terminal_out}</div>
  </div>"""
    return f"""<div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
  <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
    <div class="flex items-center gap-3">
      <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
        <span class="iconify text-yellow-400 text-xs" data-icon="{icon}" data-width="12" data-height="12"></span>
        <span class="text-[11px] font-semibold text-gray-400">{filename}</span>
      </div>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
  </div>
  <div class="bg-code">
    <pre class="overflow-x-auto pre-reset"><code class="language-{lang}">{htmlmod.escape(code)}</code></pre>
  </div>{terminal_html}
</div>"""

def style_b_code(label, code, lang="python"):
    """Style B simple-dark code block — for #key-concepts."""
    icon = "fa6-solid:terminal" if lang == "bash" else "logos:python"
    display = "Bash" if lang == "bash" else "Python"
    return f"""<div class="rounded-xl overflow-hidden bg-code shadow-md">
  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
    <div class="flex items-center gap-2">
      <span class="iconify" data-icon="{icon}" data-width="14" data-height="14"></span>
      <span class="text-[11px] font-semibold text-gray-400">{display}</span>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
  </div>
  <pre class="overflow-x-auto pre-reset"><code class="language-{lang}">{htmlmod.escape(code)}</code></pre>
</div>"""

# ═══════════════════════════════════════════════════════════
# BUILD SECTIONS
# ═══════════════════════════════════════════════════════════

# ── TOC links (12 canonical sections) ─────────────────────
toc_sections = [
    ("objective",       "fa6-solid:bullseye",          "Lesson Objective"),
    ("overview",        "fa6-solid:binoculars",        "Overview"),
    ("key-ideas",       "fa6-solid:lightbulb",         "Key Takeaways"),
    ("key-concepts",    "fa6-solid:book-open",         "Key Concepts"),
    ("code-examples",   "fa6-solid:code",              "Code Examples"),
    ("comparison",      "fa6-solid:scale-balanced",    "Framework Comparison"),
    ("practice",        "fa6-solid:pencil",            "Practice Exercises"),
    ("mistakes",        "fa6-solid:triangle-exclamation","Common Mistakes"),
    ("real-world",      "fa6-solid:briefcase",         "Real-World Use"),
    ("recap",           "fa6-solid:list-check",        "Lesson Recap"),
    ("knowledge-check", "fa6-solid:brain",             "Knowledge Check"),
    ("next-lesson",     "fa6-solid:trophy",            "Module Complete"),
]

def build_toc_links():
    lines = []
    for sid, icon, label in toc_sections:
        lines.append(f'<a href="#{sid}" class="toc-link flex items-center gap-2 text-xs text-gray-600 py-1.5 px-2 rounded-lg no-underline"><span class="iconify text-brand shrink-0" data-icon="{icon}"></span> {label}</a>')
    return "\n".join(lines)

def build_sidebar_lessons():
    lines = []
    for href, label in sidebar_lessons:
        is_active = (f"lesson{LESSON_NUM:02d}_" in href)
        if is_active:
            lines.append(f'<a href="{href}" class="mod-lesson-active flex items-center gap-2 px-3 py-2 rounded-lg border bg-[#fdf0f7] border-[#CB187D] text-[#CB187D] text-xs font-medium no-underline transition-colors"><span class="lesson-dot w-2 h-2 rounded-full bg-[#CB187D] shrink-0"></span><span class="truncate">{label}</span></a>')
        else:
            lines.append(f'<a href="{href}" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors"><span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span><span class="truncate">{label}</span></a>')
    return "\n".join(lines)

# ── Objective section ─────────────────────────────────────
def build_objective():
    cards = []
    for icon, title, desc in objectives:
        cards.append(f"""<div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
  <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
    <span class="iconify text-brand text-lg" data-icon="{icon}"></span>
  </span>
  <div>
    <p class="text-sm font-semibold text-gray-800">{title}</p>
    <p class="text-xs text-gray-500 mt-0.5">{desc}</p>
  </div>
</div>""")
    n = len(objectives)
    return f"""<section id="objective">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:bullseye", "Lesson Objective", "The goal and expected outcome of this lesson")}
    <div class="bg-white px-8 py-7">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        {"".join(cards)}
      </div>
      <div class="mt-5">
        {amber_tip(f'This lesson covers <strong>{n} key concepts</strong> for comparing Streamlit and Shiny &mdash; architectural differences, reactivity models, layout control, deployment options, and a decision framework for choosing the right tool.')}
      </div>
    </div>
  </div>
</section>"""

# ── Overview section ──────────────────────────────────────
def build_overview():
    cards = []
    for icon, title, subtitle, desc in overview_cards:
        cards.append(f"""<div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
  <div class="flex items-center gap-3 mb-2.5">
    <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
      <span class="iconify text-brand text-base" data-icon="{icon}"></span>
    </span>
    <div>
      <p class="text-sm font-bold text-gray-800 leading-tight">{title}</p>
      <p class="text-[10px] text-gray-400 italic leading-tight">{subtitle}</p>
    </div>
  </div>
  <p class="text-xs text-gray-500 leading-relaxed">{desc}</p>
</div>""")
    return f"""<section id="overview">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:binoculars", "Overview", "A high-level introduction to Streamlit vs Shiny")}
    <div class="bg-white px-8 py-7 space-y-5">
      <div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
        <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Py</span>
        <div class="relative flex items-start gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
            <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>
          </span>
          <p class="text-base text-gray-800 leading-relaxed font-medium">{HOOK_QUOTE}</p>
        </div>
      </div>
      <p class="text-sm text-gray-600 leading-relaxed">{ANALOGY_INTRO}</p>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        {"".join(cards)}
      </div>
      {amber_tip(OVERVIEW_TIP)}
    </div>
  </div>
</section>"""

# ── Key Takeaways ─────────────────────────────────────────
KT_COLORS = {
    "pink":    {"border": "border-pink-100",   "bar": "from-[#CB187D] to-[#e84aad]", "icon": "from-[#CB187D] to-[#e84aad]", "pill_bg": "bg-pink-50",    "pill_text": "text-[#CB187D]",   "pill_border": "border-pink-100"},
    "violet":  {"border": "border-violet-100", "bar": "from-violet-500 to-purple-400","icon": "from-violet-500 to-purple-600","pill_bg": "bg-violet-50",  "pill_text": "text-violet-600",  "pill_border": "border-violet-100"},
    "blue":    {"border": "border-blue-100",   "bar": "from-blue-500 to-indigo-400",  "icon": "from-blue-500 to-indigo-600",  "pill_bg": "bg-blue-50",    "pill_text": "text-blue-600",    "pill_border": "border-blue-100"},
    "emerald": {"border": "border-emerald-100","bar": "from-emerald-500 to-teal-400", "icon": "from-emerald-500 to-teal-600", "pill_bg": "bg-emerald-50", "pill_text": "text-emerald-600", "pill_border": "border-emerald-100"},
    "amber":   {"border": "border-amber-100",  "bar": "from-amber-500 to-orange-400", "icon": "from-amber-500 to-orange-600", "pill_bg": "bg-amber-50",   "pill_text": "text-amber-600",   "pill_border": "border-amber-100"},
}

def build_key_ideas():
    cards = []
    for color, icon, heading, explanation, keywords in takeaways:
        c = KT_COLORS[color]
        pills = "".join(f'<span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[11px] font-semibold {c["pill_bg"]} {c["pill_text"]} border {c["pill_border"]}">{kw}</span>' for kw in keywords)
        cards.append(f"""<div class="obj-card rounded-2xl border {c["border"]} bg-white overflow-hidden shadow-sm">
  <div class="h-1 bg-gradient-to-r {c["bar"]}"></div>
  <div class="px-5 py-5 space-y-3 bg-white">
    <div class="flex items-center gap-3">
      <span class="obj-icon inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br {c["icon"]} shrink-0 shadow-md">
        <span class="iconify text-white text-sm" data-icon="{icon}"></span>
      </span>
      <h3 class="text-sm font-bold text-gray-900">{heading}</h3>
    </div>
    <p class="text-sm text-gray-600 leading-relaxed">{explanation}</p>
    <div class="flex flex-wrap gap-2">{pills}</div>
  </div>
</div>""")
    return f"""<section id="key-ideas">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:lightbulb", "Key Takeaways", "The most important ideas to remember")}
    <div class="bg-white px-8 py-7">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        {"".join(cards)}
      </div>
    </div>
  </div>
</section>"""

# ── Key Concepts (KC tabs) ────────────────────────────────
KC_COLORS_MAP = [
    {"name":"pink",    "border":"pink-100",   "bar":"from-[#CB187D] via-pink-400 to-rose-300",        "bg":"from-pink-50/60",    "icon":"from-[#CB187D] to-[#e84aad]", "badge_from":"from-pink-100","badge_to":"to-rose-100","badge_text":"text-[#CB187D]","table_bg":"bg-pink-50","table_text":"text-[#CB187D]","code_bg":"bg-pink-50","code_text":"text-pink-700"},
    {"name":"violet",  "border":"violet-100", "bar":"from-violet-500 via-purple-400 to-fuchsia-300",  "bg":"from-violet-50/60",  "icon":"from-violet-500 to-purple-600","badge_from":"from-violet-100","badge_to":"to-purple-100","badge_text":"text-violet-600","table_bg":"bg-violet-50","table_text":"text-violet-600","code_bg":"bg-violet-50","code_text":"text-violet-700"},
    {"name":"blue",    "border":"blue-100",   "bar":"from-blue-500 via-cyan-400 to-teal-300",          "bg":"from-blue-50/60",    "icon":"from-blue-500 to-indigo-600",  "badge_from":"from-blue-100","badge_to":"to-indigo-100","badge_text":"text-blue-600","table_bg":"bg-blue-50","table_text":"text-blue-600","code_bg":"bg-blue-50","code_text":"text-blue-700"},
    {"name":"emerald", "border":"emerald-100","bar":"from-emerald-500 via-teal-400 to-cyan-300",       "bg":"from-emerald-50/60", "icon":"from-emerald-500 to-teal-600", "badge_from":"from-emerald-100","badge_to":"to-teal-100","badge_text":"text-emerald-600","table_bg":"bg-emerald-50","table_text":"text-emerald-600","code_bg":"bg-emerald-50","code_text":"text-emerald-700"},
    {"name":"orange",  "border":"orange-100", "bar":"from-orange-500 via-amber-400 to-yellow-300",     "bg":"from-orange-50/60",  "icon":"from-orange-500 to-red-600",   "badge_from":"from-orange-100","badge_to":"to-amber-100","badge_text":"text-orange-600","table_bg":"bg-orange-50","table_text":"text-orange-600","code_bg":"bg-orange-50","code_text":"text-orange-700"},
]

def build_key_concepts():
    tabs_html = []
    panels_html = []
    for i, kc in enumerate(kc_tabs):
        c = KC_COLORS_MAP[i]
        active_cls = " kc-tab-active" if i == 0 else ""
        hidden_cls = "" if i == 0 else " hidden"
        # Tab button
        tabs_html.append(f"""<button onclick="switchKcTab({i})" class="kc-tab{active_cls} group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
  <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200 {'bg-[#CB187D] text-white shadow-sm shadow-pink-200' if i==0 else 'bg-gray-100 text-gray-400'}"><span class="iconify text-[11px]" data-icon="{kc['icon']}"></span></span>
  <span class="kc-tab-label text-xs font-bold leading-tight {'text-gray-900' if i==0 else 'text-gray-400'}">{kc['label']}</span>
</button>""")
        # Panel
        params_html = ""
        if kc.get("params"):
            rows = "".join(f'<tr class="border-t border-gray-100"><td class="py-2 pr-3 align-top"><code class="text-xs font-mono font-semibold px-1.5 py-0.5 rounded {c["code_bg"]} {c["code_text"]}">{p[0]}</code></td><td class="py-2 pr-3 align-top text-[11px] text-gray-400 font-mono">{p[1]}</td><td class="py-2 align-top text-xs text-gray-600">{p[2]}</td></tr>' for p in kc["params"])
            params_html = f"""<table class="w-full text-left mt-3"><thead><tr class="{c['table_bg']}"><th class="py-1.5 px-2 text-[11px] font-bold uppercase tracking-wider {c['table_text']} rounded-tl-lg">Parameter</th><th class="py-1.5 px-2 text-[11px] font-bold uppercase tracking-wider {c['table_text']}">Type</th><th class="py-1.5 px-2 text-[11px] font-bold uppercase tracking-wider {c['table_text']} rounded-tr-lg">Description</th></tr></thead><tbody>{rows}</tbody></table>"""
        tip_html = amber_tip(kc["tip"]) if kc.get("tip") else ""
        panels_html.append(f"""<div class="kc-panel kc-panel-anim{hidden_cls}" data-color="{c['name']}" role="tabpanel">
  <div class="rounded-2xl border border-{c['border']} overflow-hidden">
    <div class="h-1 bg-gradient-to-r {c['bar']}"></div>
    <div class="bg-gradient-to-br {c['bg']} to-white p-5 space-y-4">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3">
          <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br {c['icon']} shrink-0 shadow-md">
            <span class="iconify text-white text-sm" data-icon="{kc['icon']}"></span>
          </span>
          <div>
            <h3 class="text-sm font-bold text-gray-900 leading-tight">{kc['label']}</h3>
            <p class="text-[10px] text-gray-400 mt-0.5">Concept {i+1} of {len(kc_tabs)}</p>
          </div>
        </div>
        <span class="inline-flex items-center px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r {c['badge_from']} {c['badge_to']} {c['badge_text']}">{kc['badge']}</span>
      </div>
      <p class="text-sm text-gray-600 leading-relaxed">{kc['intro']}</p>
      {style_b_code(kc['label'], kc['code'])}
      {params_html}
      {tip_html}
    </div>
  </div>
</div>""")
    return f"""<section id="key-concepts">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:book-open", "Key Concepts", "Core terms and definitions for this topic")}
    <div class="bg-white px-6 py-7">
      <div class="flex flex-col md:flex-row gap-0">
        <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">
          <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full bg-[#CB187D] transition-all duration-300" style="height:68px;"></div>
          {"".join(tabs_html)}
        </div>
        <div class="flex-1 min-w-0 md:pl-5">
          {"".join(panels_html)}
        </div>
      </div>
    </div>
  </div>
</section>"""

# ── Code Examples ─────────────────────────────────────────
def build_code_examples():
    tab_buttons = []
    panels = []
    for i, ce in enumerate(code_examples):
        active = "ce-step-active" if i == 0 else ""
        bg = "bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50" if i == 0 else "bg-gray-800 text-gray-400"
        tab_buttons.append(f'<button onclick="switchCeTab({i})" class="ce-step {active} flex items-center gap-2 px-4 py-2 rounded-full {bg} transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code"></span><span class="ce-step-label text-xs font-bold">{ce["title"]}</span></button>')
        hidden = "" if i == 0 else " hidden"
        fname = ce["title"].lower().replace(" ", "_").replace("'","").replace("/","_") + ".py"
        term_out = ce.get("terminal_out","").replace("\n", "<br>")
        panels.append(f"""<div class="ce-panel ce-panel-anim{hidden}" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{i+1:02d}</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:code"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Example {i+1} &mdash; {ce["title"]}</h3>
          <div class="flex items-center gap-2 mt-1">
            <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200"><span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner</span>
          </div>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <p class="text-sm text-gray-600 leading-relaxed">{ce["desc"]}</p>
      {style_a_code(fname, ce["code"], ce.get("terminal_cmd"), ce.get("terminal_out"))}
      {amber_tip(ce["tip"])}
    </div>
  </div>
</div>""")
    return f"""<section id="code-examples">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:code", "Code Examples", "Hands-on code snippets to explore the concepts")}
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        {"".join(tab_buttons)}
      </div>
      {"".join(panels)}
    </div>
  </div>
</section>"""

# ── Comparison (Streamlit / Shiny / Key Difference) ──────
def build_comparison():
    rows_html = []
    for i, (icon, label, st_code, st_desc, sh_code, sh_desc, diff_code, diff_desc) in enumerate(comparison_rows):
        if i > 0:
            rows_html.append("""<div class="flex items-center gap-3 mb-4">
  <span class="flex-1 h-px bg-gray-100"></span>
  <span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-[#fdf0f7] shrink-0">
    <span class="iconify text-[#CB187D] text-xs" data-icon="fa6-solid:scale-balanced"></span>
  </span>
  <span class="flex-1 h-px bg-gray-100"></span>
</div>""")
        rows_html.append(f"""<div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
  <div class="px-5 py-2 flex items-center gap-2 border-b border-gray-100 bg-gray-50">
    <span class="inline-flex items-center justify-center w-5 h-5 rounded bg-indigo-50 shrink-0">
      <span class="iconify text-indigo-400 text-[11px]" data-icon="{icon}"></span>
    </span>
    <span class="text-xs font-bold uppercase tracking-widest text-gray-400">{label}</span>
  </div>
  <div class="grid grid-cols-3 divide-x divide-gray-100">
    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">Streamlit</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">{st_code}</code>
      <p class="text-xs text-gray-500 leading-relaxed">{st_desc}</p>
    </div>
    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">Shiny</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-violet-50 text-violet-700">{sh_code}</code>
      <p class="text-xs text-gray-500 leading-relaxed">{sh_desc}</p>
    </div>
    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">Key Difference</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-amber-50 text-amber-700">{diff_code}</code>
      <p class="text-xs text-gray-500 leading-relaxed">{diff_desc}</p>
    </div>
  </div>
</div>""")
    return f"""<section id="comparison">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:scale-balanced", "Framework Comparison", "How Streamlit and Shiny compare side by side")}
    <div class="bg-white px-8 py-7 space-y-5">
      {"".join(rows_html)}
    </div>
  </div>
</section>"""

# ── Practice ──────────────────────────────────────────────
def build_practice():
    tab_buttons = []
    panels = []
    for i, pe in enumerate(practice_exercises):
        active = "pe-step-active" if i == 0 else ""
        bg = "bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50" if i == 0 else "bg-gray-800 text-gray-400"
        tab_buttons.append(f'<button onclick="switchPeTab({i})" class="pe-step {active} flex items-center gap-2 px-4 py-2 rounded-full {bg} transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span><span class="pe-step-label text-xs font-bold">{pe["title"]}</span></button>')
        hidden = "" if i == 0 else " hidden"
        task_items = "".join(f'<li class="text-sm text-gray-600">{t}</li>' for t in pe["tasks"])
        fname = f"solution_{i+1}.py"
        panels.append(f"""<div class="pe-panel pe-panel-anim{hidden}" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{i+1:02d}</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Exercise {i+1} &mdash; {pe["title"]}</h3>
          <div class="flex items-center gap-2 mt-1">
            <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200"><span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner</span>
          </div>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
          <ol class="list-decimal list-inside space-y-1">{task_items}</ol>
        </div>
      </div>
      <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
        <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Solution
        <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
      </button>
      <div class="accordion-body">
        {style_a_code(fname, pe["solution"])}
        <div class="mt-3">{amber_tip(pe["why"])}</div>
      </div>
    </div>
  </div>
</div>""")
    return f"""<section id="practice">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:pencil", "Practice Exercises", "Guided exercises to reinforce your learning")}
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        {"".join(tab_buttons)}
      </div>
      {"".join(panels)}
    </div>
  </div>
</section>"""

# ── Mistakes ──────────────────────────────────────────────
def build_mistakes():
    tab_buttons = []
    panels = []
    for i, mk in enumerate(mistakes):
        active = "mk-step-active" if i == 0 else ""
        bg = "bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50" if i == 0 else "bg-gray-800 text-gray-400"
        tab_buttons.append(f'<button onclick="switchMkTab({i})" class="mk-step {active} flex items-center gap-2 px-4 py-2 rounded-full {bg} transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span><span class="mk-step-label text-xs font-bold">{mk["title"]}</span></button>')
        hidden = "" if i == 0 else " hidden"
        panels.append(f"""<div class="mk-panel mk-panel-anim{hidden}" role="tabpanel">
  <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">
    <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
        <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
      </span>
      <div class="min-w-0 flex-1">
        <h4 class="font-bold text-gray-800 text-sm">{mk["title"]}</h4>
        <p class="text-xs text-gray-500 mt-0.5">{mk["why_happens"]}</p>
      </div>
    </div>
    <div class="px-6 py-5 space-y-3">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <div>
          <p class="text-xs font-bold text-red-500 mb-2 flex items-center gap-1"><span class="iconify" data-icon="fa6-solid:xmark"></span> Wrong</p>
          <div class="rounded-xl overflow-hidden bg-code">
            <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">{htmlmod.escape(mk["wrong"])}</code></pre>
          </div>
        </div>
        <div>
          <p class="text-xs font-bold text-emerald-500 mb-2 flex items-center gap-1"><span class="iconify" data-icon="fa6-solid:check"></span> Correct</p>
          <div class="rounded-xl overflow-hidden bg-code">
            <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">{htmlmod.escape(mk["correct"])}</code></pre>
          </div>
        </div>
      </div>
    </div>
    <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
      <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
      <p class="text-xs text-gray-600 leading-relaxed">{mk["fix"]}</p>
    </div>
  </div>
</div>""")
    return f"""<section id="mistakes">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:triangle-exclamation", "Common Mistakes", "Frequent errors and how to avoid them")}
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        {"".join(tab_buttons)}
      </div>
      {"".join(panels)}
    </div>
  </div>
</section>"""

# ── Real-World ────────────────────────────────────────────
def build_real_world():
    cards = []
    for icon, title, desc in real_world:
        cards.append(f"""<div class="group flex items-start gap-3 rounded-xl border border-gray-100 bg-gray-50 px-4 py-3.5 transition-all duration-200 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/50 hover:shadow-sm">
  <div class="w-9 h-9 rounded-lg flex items-center justify-center bg-[#fdf0f7] shrink-0 transition-colors group-hover:bg-[#CB187D]">
    <span class="iconify text-sm text-[#CB187D] group-hover:text-white" data-icon="{icon}"></span>
  </div>
  <div>
    <p class="text-sm font-semibold text-gray-700">{title}</p>
    <p class="text-xs text-gray-500 mt-0.5 leading-relaxed">{desc}</p>
  </div>
</div>""")
    return f"""<section id="real-world">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:briefcase", "Real-World Use", "Practical applications in real-world workflows")}
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="rounded-xl p-5 flex items-start gap-4 border border-[#f5c6e0] bg-[#fdf0f7]">
        <span class="iconify mt-0.5 shrink-0 text-xl text-[#CB187D]" data-icon="fa6-solid:earth-americas"></span>
        <p class="text-sm text-gray-700 leading-relaxed">Streamlit and Shiny for Python are both used across industries &mdash; from quick data exploration tools to enterprise dashboards. The choice between them often comes down to project complexity, deployment requirements, and how much control you need over the reactive behavior and layout.</p>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
        {"".join(cards)}
      </div>
    </div>
  </div>
</section>"""

# ── Recap ─────────────────────────────────────────────────
recap_items = [
    ("fa6-solid:code-branch",    "Script vs Architecture",    "You learned that Streamlit re-runs your entire script top-to-bottom on every interaction, while Shiny separates the UI definition from the server logic and only re-executes affected outputs."),
    ("fa6-solid:arrows-spin",    "Reactivity Models",         "You learned that Streamlit handles reactivity implicitly through full re-runs, while Shiny builds an explicit reactive graph that tracks which outputs depend on which inputs."),
    ("fa6-solid:palette",        "Layout and Customization",  "You learned that Streamlit auto-arranges widgets top-to-bottom with minimal code, while Shiny provides <code>ui.page_navbar()</code> and <code>ui.layout_sidebar()</code> for precise layout control."),
    ("fa6-solid:cloud-arrow-up", "Deployment Ecosystems",     "You learned that Streamlit Community Cloud offers one-click deployment for public apps, while Shiny uses Posit Connect or self-hosted infrastructure for enterprise production."),
    ("fa6-solid:scale-balanced", "Decision Framework",        "You learned to choose Streamlit for quick prototypes and data exploration, and Shiny when you need complex reactivity, custom layouts, or enterprise-grade deployment."),
]

def build_recap():
    cards = []
    for i, (icon, title, desc) in enumerate(recap_items):
        cards.append(f"""<div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
  <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
    <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">{i+1:02d}</span>
    <div class="relative flex items-start gap-3">
      <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
        <span class="iconify text-sm" data-icon="{icon}"></span>
      </span>
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">{title}</p>
        <p class="text-[11px] text-gray-600 leading-snug">{desc}</p>
      </div>
    </div>
  </div>
</div>""")
    n = len(recap_items)
    return f"""<section id="recap">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:list-check", "Lesson Recap", "A quick summary of what you learned")}
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        {"".join(cards)}
      </div>
      <div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">
        <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">&#10003;</span>
        <div class="relative flex items-center gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">
            <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>
          </span>
          <div>
            <p class="text-sm font-bold text-white">Lesson Complete!</p>
            <p class="text-xs text-white/80 mt-0.5">You&#39;ve covered {n} key concepts. Ready for the knowledge check?</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""

# ── Knowledge Check ───────────────────────────────────────
def build_knowledge_check():
    tab_buttons = []
    panels = []
    for i, q in enumerate(quiz):
        active = "qz-step-active" if i == 0 else ""
        bg = "bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50" if i == 0 else "bg-gray-800 text-gray-400"
        tab_buttons.append(f'<button onclick="switchQzTab({i})" class="qz-step {active} flex items-center gap-2 px-4 py-2 rounded-full {bg} transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:circle-question"></span><span class="qz-step-label text-xs font-bold">Question {i+1}</span></button>')
        hidden = "" if i == 0 else " hidden"
        if q["type"] == "tf":
            answers_html = f"""<div class="flex gap-3">
            <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-[#CB187D] hover:bg-[#fdf0f7] transition-colors" onclick="checkQuiz(this, {str(q['answer']).lower()})"><span class="iconify mr-1.5" data-icon="fa6-solid:check"></span> True</button>
            <button class="quiz-btn px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 hover:border-red-400 hover:bg-red-50 transition-colors" onclick="checkQuiz(this, {str(not q['answer']).lower()})"><span class="iconify mr-1.5" data-icon="fa6-solid:xmark"></span> False</button>
          </div>"""
            q_type_label = "True or False"
        else:
            opts = []
            for label, correct in q["options"]:
                hover_cls = "hover:border-[#CB187D] hover:bg-[#fdf0f7]" if correct else "hover:border-gray-300 hover:bg-gray-50"
                opts.append(f'<button class="quiz-btn w-full text-left px-5 py-2.5 rounded-xl border border-gray-200 bg-white text-sm font-medium text-gray-600 {hover_cls} transition-colors" onclick="checkQuiz(this, {str(correct).lower()})">{htmlmod.escape(label)}</button>')
            answers_html = f'<div class="grid gap-2">{"".join(opts)}</div>'
            q_type_label = "Multiple Choice"
        panels.append(f"""<div class="qz-panel qz-panel-anim{hidden}" role="tabpanel">
  <div class="rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Q{i+1}</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:circle-question"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">{q_type_label}</h3>
          <p class="text-xs text-gray-500 mt-0.5">Select the correct answer</p>
        </div>
      </div>
    </div>
    <div class="px-6 py-5 space-y-4">
      <div class="quiz-question" data-qid="quiz-q{i}" data-fb-correct="{q['fb_correct']}" data-fb-wrong="{q['fb_wrong']}">
        <p class="text-sm font-semibold text-gray-800 mb-4">{q['stem']}</p>
        {answers_html}
        <p class="quiz-feedback mt-3 text-sm font-medium hidden"></p>
      </div>
    </div>
  </div>
</div>""")
    return f"""<section id="knowledge-check">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:brain", "Knowledge Check", "Test your understanding before moving on")}
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        {"".join(tab_buttons)}
      </div>
      {"".join(panels)}
    </div>
  </div>
</section>"""

# ── Module Complete (replaces Next Lesson for final lesson) ──
def build_next_lesson():
    complete_cards = [
        ("fa6-solid:house",              "Return to Learning Hub",  "Head back to the main page to explore other tracks and modules."),
        ("fa6-solid:database",           "SQL Foundations",         "Continue your learning journey with SQL — the language of data."),
        ("fa6-solid:arrow-rotate-left",  "Review Module 5",        "Revisit any lesson in this module to strengthen your understanding."),
    ]
    cards_html = []
    for icon, title, desc in complete_cards:
        cards_html.append(f"""<div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
  <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0"><span class="iconify text-white text-sm" data-icon="{icon}"></span></span>
  <div>
    <p class="text-sm font-semibold text-gray-700">{title}</p>
    <p class="text-xs text-gray-500 mt-0.5">{desc}</p>
  </div>
</div>""")
    return f"""<section id="next-lesson" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:trophy", "Module Complete!", "You have finished all 7 lessons in this module")}
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">
        <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">
          <span class="iconify" data-icon="fa6-solid:graduation-cap"></span>
        </span>
        <div class="relative flex items-center gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">
            <span class="iconify text-white text-lg" data-icon="fa6-solid:graduation-cap"></span>
          </span>
          <div>
            <p class="text-sm font-bold text-white">{MODULE_TITLE} &mdash; Complete!</p>
            <p class="text-xs text-white/80 mt-0.5">You have finished all 7 lessons in Module {MODULE_NUM}. Head back to the Learning Hub to continue your journey.</p>
          </div>
        </div>
      </div>
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">Continue Learning</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
          {"".join(cards_html)}
        </div>
      </div>
    </div>
  </div>
</section>"""

# ── Bottom Nav (no Next link — last lesson) ───────────────
def build_bottom_nav():
    prev_html = f"""<a href="{PREV_LESSON[0]}" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{PREV_LESSON[1]}</p>
      </div>
    </a>"""
    return f"""<section>
  <div class="flex flex-col sm:flex-row gap-3">
    {prev_html}
    <a href="../../hub_home_page.html" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>
    <div class="flex-1"></div>
  </div>
</section>"""

# ── JavaScript ────────────────────────────────────────────
SCRIPT = r"""<script>
function toggleToc(){const s=document.querySelector('.lesson-toc-sidebar'),i=document.getElementById('toc-toggle-icon'),c=s.classList.toggle('toc-collapsed');i.setAttribute('data-icon',c?'fa6-solid:angles-right':'fa6-solid:angles-left');if(window.Iconify)Iconify.scan();}
const tocLinks=document.querySelectorAll('.toc-link');const sections=[...tocLinks].map(l=>document.getElementById(l.getAttribute('href').replace('#',''))).filter(Boolean);
function updateScrollSpy(){let id='';sections.forEach(s=>{if(window.scrollY>=s.offsetTop-120)id=s.id;});tocLinks.forEach(l=>l.classList.toggle('active',l.getAttribute('href')==='#'+id));}
function updateScrollProgress(){const w=document.documentElement.scrollTop||document.body.scrollTop;const h=document.documentElement.scrollHeight-document.documentElement.clientHeight;document.getElementById('scroll-progress').style.width=(h>0?(w/h)*100:0)+'%';}
function updateBackToTop(){document.getElementById('back-to-top').classList.toggle('visible',window.scrollY>400);}
window.addEventListener('scroll',()=>{updateScrollSpy();updateScrollProgress();updateBackToTop();});
function copyCode(btn){const c=btn.closest('.relative')||btn.parentElement.closest('div');const pre=c?c.querySelector('pre'):null;const text=pre?pre.innerText:'';function fb(){const o=btn.innerHTML;btn.innerHTML='<span class="iconify mr-1" data-icon="fa6-solid:check"></span>Copied!';btn.style.background='rgba(34,197,94,0.2)';btn.style.borderColor='rgba(34,197,94,0.5)';btn.style.color='#4ade80';setTimeout(()=>{btn.innerHTML=o;btn.style.background='';btn.style.borderColor='';btn.style.color='';},2000);}function fc(){const t=document.createElement('textarea');t.value=text;t.style.position='fixed';t.style.opacity='0';document.body.appendChild(t);t.select();try{document.execCommand('copy');}catch(e){}document.body.removeChild(t);fb();}if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(text).then(fb).catch(fc);}else{fc();}}
function toggleAccordion(btn){const b=btn.nextElementSibling;const o=b.classList.contains('open');btn.classList.toggle('open',!o);b.classList.toggle('open',!o);if(!o&&window.Prism)Prism.highlightAllUnder(b);}
const kcColors=[{num:'#CB187D',numShadow:'rgba(203,24,125,0.25)',activeBg:'#fdf0f7'},{num:'#7c3aed',numShadow:'rgba(124,58,237,0.25)',activeBg:'#f5f3ff'},{num:'#2563eb',numShadow:'rgba(37,99,235,0.25)',activeBg:'#eff6ff'},{num:'#059669',numShadow:'rgba(5,150,105,0.25)',activeBg:'#ecfdf5'},{num:'#c74905',numShadow:'rgba(199,73,5,0.25)',activeBg:'#ffddb3'}];
function switchKcTab(idx){const c=kcColors[idx%kcColors.length];const tabs=document.querySelectorAll('.kc-tab');const panels=document.querySelectorAll('.kc-panel');const ind=document.querySelector('.kc-indicator');tabs.forEach((t,i)=>{const n=t.querySelector('.kc-tab-num'),l=t.querySelector('.kc-tab-label');if(i===idx){t.classList.add('kc-tab-active');t.style.background=c.activeBg;if(n){n.style.background=c.num;n.style.color='#fff';n.style.boxShadow='0 2px 8px '+c.numShadow;}if(l)l.style.color='#111827';}else{t.classList.remove('kc-tab-active');t.style.background='';if(n){n.style.background='#f3f4f6';n.style.color='#9ca3af';n.style.boxShadow='none';}if(l)l.style.color='#9ca3af';}});if(ind&&tabs[idx]){ind.style.top=tabs[idx].offsetTop+'px';ind.style.height=tabs[idx].offsetHeight+'px';ind.style.background=c.num;}panels.forEach((p,i)=>{if(i===idx){p.classList.remove('hidden');p.classList.remove('kc-panel-anim');void p.offsetWidth;p.classList.add('kc-panel-anim');}else{p.classList.add('hidden');}});const v=panels[idx];if(v&&window.Prism)Prism.highlightAllUnder(v);}
function _switchDarkPills(pfx,idx){document.querySelectorAll('.'+pfx+'-step').forEach((s,i)=>{if(i===idx){s.classList.add(pfx+'-step-active');s.style.background='linear-gradient(to right,#CB187D,#e84aad)';s.style.color='#fff';s.style.boxShadow='0 10px 25px -5px rgba(203,24,125,0.3)';}else{s.classList.remove(pfx+'-step-active');s.style.background='#1f2937';s.style.color='#9ca3af';s.style.boxShadow='none';}});document.querySelectorAll('.'+pfx+'-panel').forEach((p,i)=>{if(i===idx){p.classList.remove('hidden');p.classList.remove(pfx+'-panel-anim');void p.offsetWidth;p.classList.add(pfx+'-panel-anim');}else{p.classList.add('hidden');}});const v=document.querySelectorAll('.'+pfx+'-panel:not(.hidden)')[0];if(v&&window.Prism)Prism.highlightAllUnder(v);}
function switchCeTab(i){_switchDarkPills('ce',i);}
function switchMkTab(i){_switchDarkPills('mk',i);}
function switchPeTab(i){_switchDarkPills('pe',i);}
function switchQzTab(i){_switchDarkPills('qz',i);}
function checkQuiz(btn,answer){const q=btn.closest('.quiz-question');const fb=q.querySelector('.quiz-feedback');const btns=q.querySelectorAll('.quiz-btn');const fbC=q.getAttribute('data-fb-correct');const fbW=q.getAttribute('data-fb-wrong');btns.forEach(b=>{b.disabled=true;b.style.opacity='0.6';});if(answer===true){btn.classList.add('correct');btn.style.opacity='1';fb.textContent=fbC||'\u2713 Correct!';fb.className='quiz-feedback mt-2 text-sm font-medium text-green-600';}else{btn.classList.add('incorrect');btn.style.opacity='1';fb.textContent=fbW||'\u2717 Not quite \u2014 review the lesson above.';fb.className='quiz-feedback mt-2 text-sm font-medium text-red-500';}}
document.addEventListener('DOMContentLoaded',()=>{if(window.Prism)Prism.highlightAll();});
</script>"""

# ═══════════════════════════════════════════════════════════
# ASSEMBLE FULL FILE
# ═══════════════════════════════════════════════════════════

NUM_OBJ = len(objectives)

HTML = f"""<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap">
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://code.iconify.design/3/3.1.0/iconify.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" crossorigin="anonymous">
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-sql.min.js" crossorigin="anonymous"></script>

{CSS}

<div class="scroll-progress" id="scroll-progress" style="width:0%;"></div>
<button class="back-to-top" id="back-to-top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">
  <span class="iconify text-lg" data-icon="fa6-solid:arrow-up"></span>
</button>

<div id="hub-root" class="bg-gray-50 min-h-screen">

<!-- HERO -->
<div class="max-w-[1280px] mx-auto px-4 pt-5 pb-0">
  <section class="hero-container">
    <div class="hero-dots"></div>
    <div class="hero-glow" style="width:350px;height:350px;top:-80px;right:0;background:rgba(255,255,255,0.12);"></div>
    <div class="hero-glow" style="width:280px;height:280px;bottom:-50px;left:5%;background:rgba(127,0,76,0.35);"></div>
    <div style="position:absolute;bottom:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent 0%,#f5c6e0 30%,#CB187D 50%,#f5c6e0 70%,transparent 100%);opacity:0.7;"></div>
    <div class="relative z-10 px-8 py-8 md:px-12 md:py-10">
      <div class="hero-split flex flex-col md:flex-row items-center gap-6 md:gap-10">
        <div class="flex-1 min-w-0">
          <div class="flex flex-wrap items-center gap-2 mb-4">
            <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs"><span class="iconify text-[10px]" data-icon="fa6-solid:window-maximize"></span> Module {MODULE_NUM}</span>
            <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs"><span class="inline-flex items-center gap-1"><span style="width:6px;height:6px;border-radius:50%;background:#22c55e;display:inline-block;"></span><span style="width:6px;height:6px;border-radius:50%;background:#22c55e;display:inline-block;"></span><span style="width:6px;height:6px;border-radius:50%;background:#d1d5db;display:inline-block;"></span></span> Intermediate</span>
            <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs"><span class="iconify text-[10px]" data-icon="fa6-regular:clock"></span> 5 min read</span>
          </div>
          <p class="text-xs font-bold uppercase tracking-[0.2em] text-white/90 mb-2">Lesson {LESSON_NUM:02d}</p>
          <h1 class="text-3xl md:text-4xl font-extrabold text-white mb-3 leading-[1.15] tracking-tight">{LESSON_TITLE}</h1>
          <p class="text-white/80 text-sm md:text-base leading-relaxed mb-4 max-w-lg">{MODULE_TITLE} &middot; {TRACK_LABEL}</p>
          <div class="flex items-center gap-4 mb-5 text-sm">
            <div class="flex items-center gap-2">
              <span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-white/15">
                <span class="iconify text-white text-[10px]" data-icon="fa6-solid:user"></span>
              </span>
              <span class="text-white/85 font-medium text-xs">Python Learning Hub</span>
            </div>
          </div>
          <div class="flex items-center gap-2 flex-wrap">
            <a href="#objective" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline"><span class="iconify text-[10px]" data-icon="fa6-solid:bullseye" style="opacity:0.5;"></span><span class="font-extrabold">{NUM_OBJ}</span><span class="font-semibold opacity-55">Goals</span></a>
            <a href="#code-examples" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline"><span class="iconify text-[10px]" data-icon="fa6-solid:code" style="opacity:0.5;"></span><span class="font-extrabold">{len(code_examples)}</span><span class="font-semibold opacity-55">Examples</span></a>
            <a href="#practice" class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs no-underline"><span class="iconify text-[10px]" data-icon="fa6-solid:dumbbell" style="opacity:0.5;"></span><span class="font-extrabold">{len(practice_exercises)}</span><span class="font-semibold opacity-55">Exercises</span></a>
            <span class="hero-pill inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full text-xs"><span class="iconify text-[10px]" data-icon="fa6-solid:layer-group" style="opacity:0.5;"></span><span class="font-extrabold">{PROGRESS}</span><span class="font-semibold opacity-55">Progress</span></span>
          </div>
        </div>
        <div class="w-full md:w-[300px] lg:w-[320px] shrink-0 self-center">
          <div style="padding:0.25rem;opacity:0.75;">
            {HERO_SVG}
          </div>
        </div>
      </div>
    </div>
  </section>
</div>

<!-- MAIN LAYOUT -->
<div class="max-w-[1280px] mx-auto px-4 pt-8 pb-12">
  <div class="lesson-layout">
    <aside class="lesson-toc-sidebar">
      <div class="rounded-2xl border border-gray-100 shadow-sm overflow-hidden bg-white">
        <div class="toc-header relative flex items-center gap-2 px-4 py-3 border-b border-gray-100">
          <span class="toc-header-label text-xs font-bold uppercase tracking-widest text-brand">On This Page</span>
          <button class="toc-toggle-btn" onclick="toggleToc()" title="Toggle navigation">
            <span class="iconify text-sm" id="toc-toggle-icon" data-icon="fa6-solid:angles-left"></span>
          </button>
        </div>
        <nav class="toc-body px-2 py-2 border-b border-gray-100" aria-label="Page sections">
          {build_toc_links()}
        </nav>
        <div class="toc-module-list px-3 py-3">
          <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-2 px-1">Module Lessons</p>
          <div class="space-y-1">
            {build_sidebar_lessons()}
          </div>
        </div>
      </div>
    </aside>

    <main class="min-w-0 flex-1 space-y-10">

{build_objective()}

{build_overview()}

{build_key_ideas()}

{build_key_concepts()}

{build_code_examples()}

{build_comparison()}

{build_practice()}

{build_mistakes()}

{build_real_world()}

{build_recap()}

{build_knowledge_check()}

{build_next_lesson()}

{build_bottom_nav()}

    </main>
  </div>
</div>

</div>

{SCRIPT}"""

# ═══════════════════════════════════════════════════════════
# WRITE & VERIFY
# ═══════════════════════════════════════════════════════════
os.makedirs(os.path.dirname(TARGET), exist_ok=True)
with open(TARGET, "w", encoding="utf-8") as f:
    f.write(HTML)

lines = HTML.split("\n")
print(f"✅ Wrote {TARGET} ({len(lines)} lines)")

# Div balance
opens = sum(l.count("<div") for l in lines)
closes = sum(l.count("</div>") for l in lines)
print(f"   Div balance: {opens - closes} (opens={opens}, closes={closes})")

# Tab / panel counts
import re as _re
for prefix, label in [("ce","CE"), ("kc","KC"), ("pe","PE"), ("mk","MK"), ("qz","QZ")]:
    tabs_count = len(_re.findall(rf'class="[^"]*{prefix}-step[ "]', HTML))
    panels_count = len(_re.findall(rf'class="[^"]*{prefix}-panel[ "]', HTML))
    print(f"   {label} tabs={tabs_count}, panels={panels_count}")

# Section balance
for sid in ["objective","overview","key-ideas","key-concepts","code-examples","comparison","practice","mistakes","real-world","recap","knowledge-check","next-lesson"]:
    pattern = rf'<section id="{sid}"[^>]*>(.*?)</section>'
    m = _re.search(pattern, HTML, _re.DOTALL)
    if m:
        block = m.group(1)
        o = block.count("<div")
        c = block.count("</div>")
        status = "✅" if o == c else f"❌ ({o-c})"
        print(f"   #{sid}: div balance {status}")
    else:
        print(f"   #{sid}: NOT FOUND ❌")
