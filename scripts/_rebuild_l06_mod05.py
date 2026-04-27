#!/usr/bin/env python3
"""Rebuild lesson 06 — Shiny for Python (Module 05)."""

import os, html as htmlmod

# ═══════════════════════════════════════════════════════════
# METADATA
# ═══════════════════════════════════════════════════════════
LESSON_NUM   = 6
LESSON_TITLE = "Shiny for Python"
MODULE_NUM   = 5
MODULE_TITLE = "Building Data Applications"
TRACK_LABEL  = "Track 01 — Python Foundations"
PROGRESS     = "6/7"
PREV_LESSON  = ("lesson05_deploying_data_applications.html", "Deploying Data Applications")
NEXT_LESSON  = ("lesson07_streamlit_vs_shiny.html", "Streamlit vs Shiny")
TARGET       = os.path.join(os.path.dirname(__file__), "..", "pages", "mod_05_data_application", "lesson06_shiny_for_python.html")

# ═══════════════════════════════════════════════════════════
# CONTENT DATA
# ═══════════════════════════════════════════════════════════

HOOK_QUOTE = "Shiny for Python is a reactive web framework that automatically keeps your dashboard's outputs in sync with user inputs — you describe <em>what</em> to display and Shiny figures out <em>when</em> to update it."

ANALOGY_INTRO = 'Think of a Shiny app like a <strong>puppet theater</strong>: the stage is the user interface your audience sees, the puppeteer backstage is the server logic that decides what happens, and the strings connecting the two are reactive expressions that transmit every audience request to the puppeteer and send the response back to the stage instantly.'

OVERVIEW_TIP = 'Shiny&#39;s reactive model means you never write manual "on-click" callbacks to refresh charts — describe the relationship between inputs and outputs once, and the framework handles every update automatically.'

overview_cards = [
    ("fa6-solid:display",        "UI (User Interface)",  "The stage — what the audience sees",
     "The UI is a Python function that returns a layout of input widgets (sliders, dropdowns, text fields) and output placeholders (plots, tables, text). You build it by nesting Shiny's ui.* functions, much like arranging set pieces on a theater stage before the curtain rises."),
    ("fa6-solid:gears",          "Server Function",      "The puppeteer — decides what happens backstage",
     "The server function contains all the logic that reads user inputs, runs calculations, and sends results back to the UI. You define it as a regular Python function that Shiny calls automatically whenever an input changes — you never have to wire up event listeners yourself."),
    ("fa6-solid:arrows-spin",    "Reactive Expressions", "The strings — transmit signals between stage and puppeteer",
     "A reactive expression is a cached computation that Shiny re-runs only when its upstream inputs change. You create one with @reactive.calc, and any output that reads it will update automatically — this avoids redundant recalculations when multiple outputs share the same filtered dataset."),
    ("fa6-solid:arrow-right-to-bracket", "Inputs &amp; Outputs", "The script — tells each puppet what to do",
     "Inputs are the widgets your users interact with (input.slider(), input.select()), and outputs are the rendered results they see (@render.plot, @render.table). Shiny tracks which outputs depend on which inputs and re-renders only the outputs whose inputs actually changed."),
    ("fa6-solid:layer-group",    "Layouts &amp; Panels",  "The set design — arranges everything on stage",
     "Shiny provides layout functions like ui.layout_sidebar(), ui.nav_panel(), and ui.card() to organize your UI into sidebars, tabbed navigation, and card grids. These composable building blocks let you create professional dashboard layouts without writing any CSS."),
]

objectives = [
    ("fa6-solid:display",              "Understand Shiny's UI/Server Architecture",   "Learn how the UI function and server function work together to create a reactive application."),
    ("fa6-solid:arrows-spin",          "Write Reactive Expressions",                  "Use @reactive.calc to create cached computations that update automatically when inputs change."),
    ("fa6-solid:sliders",              "Create Interactive Input Widgets",             "Add sliders, dropdowns, checkboxes, and text inputs that drive your dashboard's behavior."),
    ("fa6-solid:chart-line",           "Render Dynamic Outputs",                      "Use @render.plot, @render.table, and @render.text to display results that stay in sync with user inputs."),
    ("fa6-solid:layer-group",          "Build Dashboard Layouts",                     "Organize your app with sidebars, cards, tabs, and value boxes using Shiny's layout functions."),
]

takeaways = [
    ("pink",    "fa6-solid:display",     "The UI and Server Are Separate by Design",
     "Shiny splits every app into a UI function that defines what the user sees and a server function that defines what happens behind the scenes. This separation means you can redesign the layout without touching your data logic, and you can swap out a calculation without breaking the interface.",
     ["UI function", "server function", "separation of concerns"]),
    ("violet",  "fa6-solid:arrows-spin", "Reactive Expressions Eliminate Redundant Work",
     "When multiple outputs need the same filtered dataset, a @reactive.calc computes it once and caches the result until an upstream input changes. Without reactive expressions, every output would re-filter the raw data independently, slowing your app and creating subtle bugs if the filter logic drifts between outputs.",
     ["@reactive.calc", "caching", "shared computation"]),
    ("blue",    "fa6-solid:sliders",     "Inputs Are Accessed as Properties, Not Function Calls",
     "You read an input's current value with input.widget_id() — note the parentheses — inside the server function. Forgetting the parentheses returns the reactive object itself instead of its value, which causes silent type errors that are easy to miss during testing.",
     ["input.id()", "reactive read", "parentheses"]),
    ("emerald", "fa6-solid:chart-line",  "Decorators Wire Outputs to the Render Pipeline",
     "You attach a render function to an output by decorating it with @render.plot, @render.table, or @render.text — the decorator's name tells Shiny how to display the return value. If you forget the decorator, Shiny never registers the function as an output and nothing appears on the page.",
     ["@render.plot", "@render.table", "@render.text"]),
    ("amber",   "fa6-solid:layer-group", "Layout Functions Replace Manual CSS",
     "Shiny's ui.layout_sidebar(), ui.card(), and ui.nav_panel() generate responsive HTML containers without you writing any CSS. Relying on these built-in layouts keeps your app consistent and mobile-friendly, whereas hand-rolling CSS in a Shiny app often breaks the reactive resize behavior.",
     ["ui.layout_sidebar()", "ui.card()", "ui.nav_panel()"]),
]

kc_tabs = [
    {
        "label": "UI / Server Split",
        "icon": "fa6-solid:display",
        "badge": "Architecture",
        "intro": "Every Shiny for Python app is built from two pieces: a <code>ui</code> object that describes the page layout and a <code>server</code> function that contains the logic. The <code>shiny.App()</code> constructor ties them together and starts the reactive engine.",
        "code": """from shiny import App, ui, render

# --- UI: describe what the user sees ---
app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_slider("n", "Sample size", 10, 200, 50),  # slider widget
    ),
    ui.card(
        ui.output_text("result"),  # placeholder for server output
    ),
)

# --- Server: define what happens ---
def server(input, output, session):
    @render.text
    def result():                       # function name matches output id
        return f"You selected {input.n()} items"

# --- Tie UI + server together ---
app = App(app_ui, server)""",
        "params": [
            ("App(ui, server)", "constructor", "Creates the Shiny application from a UI object and a server function."),
            ("ui.page_sidebar()", "layout", "Top-level page with a collapsible sidebar on the left and a main panel on the right."),
            ("input.n()", "reactive read", "Returns the current value of the widget whose id is \"n\". The parentheses trigger a reactive dependency."),
        ],
        "tip": "The function name inside the server (<code>result</code>) must exactly match the output id you pass to <code>ui.output_text(\"result\")</code>. A mismatch means the output slot stays empty with no error message.",
    },
    {
        "label": "Reactive Expressions",
        "icon": "fa6-solid:arrows-spin",
        "badge": "Core Concept",
        "intro": "A reactive expression is a computation that Shiny caches and re-runs only when one of its upstream inputs changes. You create one with the <code>@reactive.calc</code> decorator, and any output or other reactive expression that calls it automatically subscribes to its updates.",
        "code": """from shiny import App, ui, render, reactive
import pandas as pd

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select("dept", "Department", ["Sales", "Engineering", "HR"]),
    ),
    ui.card(ui.output_table("table")),
    ui.card(ui.output_text("count")),
)

def server(input, output, session):
    # --- Shared reactive expression (runs once per input change) ---
    @reactive.calc
    def filtered():
        df = pd.read_csv("employees.csv")      # load data
        return df[df["dept"] == input.dept()]    # filter by selection

    @render.table
    def table():
        return filtered()   # reads the cached result

    @render.text
    def count():
        return f"{len(filtered())} employees"   # same cache, no re-filter

app = App(app_ui, server)""",
        "params": [
            ("@reactive.calc", "decorator", "Marks a function as a reactive expression whose result is cached until an upstream input changes."),
            ("filtered()", "call syntax", "Calling the reactive expression with parentheses reads its cached value and creates a dependency."),
        ],
        "tip": "Never put expensive I/O (like <code>pd.read_csv()</code>) at the top level of your script — place it inside a <code>@reactive.calc</code> so Shiny can control when it runs and cache the result between renders.",
    },
    {
        "label": "Input Widgets",
        "icon": "fa6-solid:sliders",
        "badge": "UI Components",
        "intro": "Shiny provides a library of input widgets that capture user choices and feed them into the server function as reactive values. Every widget takes an <code>id</code> string as its first argument — this is the name you use to read the value with <code>input.id()</code> inside the server.",
        "code": """from shiny import ui

# Numeric slider — returns an int or float
ui.input_slider("sample_size", "Sample Size", min=10, max=500, value=100)

# Dropdown selector — returns the selected string
ui.input_select("region", "Region", choices=["North", "South", "East", "West"])

# Checkbox — returns True or False
ui.input_checkbox("show_trend", "Show trend line", value=False)

# Text input — returns a string
ui.input_text("search", "Search term", placeholder="Type to filter...")

# Date range — returns a tuple of (start_date, end_date)
ui.input_date_range("dates", "Date range")""",
        "params": [
            ("input_slider(id, label, min, max, value)", "numeric", "Renders a draggable slider for selecting a number within a range."),
            ("input_select(id, label, choices)", "categorical", "Renders a dropdown menu populated from a list or dictionary of options."),
            ("input_checkbox(id, label, value)", "boolean", "Renders a single checkbox that returns True when checked and False when unchecked."),
            ("input_text(id, label)", "free-text", "Renders a single-line text field for arbitrary user input."),
            ("input_date_range(id, label)", "date pair", "Renders two date pickers and returns a (start, end) tuple."),
        ],
        "tip": "Always read input values with parentheses: <code>input.sample_size()</code>, not <code>input.sample_size</code>. Without parentheses you get the reactive signal object, not the actual number — and comparisons like <code>if input.sample_size > 100</code> will silently evaluate to <code>True</code> every time.",
    },
    {
        "label": "Render Decorators",
        "icon": "fa6-solid:chart-line",
        "badge": "Outputs",
        "intro": "Render decorators tell Shiny how to display the value your server function returns. You place the decorator above a function whose name matches the output id in the UI, and Shiny calls that function whenever an upstream input changes.",
        "code": """from shiny import App, ui, render
import matplotlib.pyplot as plt

app_ui = ui.page_fillable(
    ui.layout_columns(
        ui.card(ui.output_plot("chart")),      # plot placeholder
        ui.card(ui.output_table("summary")),   # table placeholder
        ui.card(ui.output_text("headline")),   # text placeholder
    ),
)

def server(input, output, session):
    @render.plot                        # returns a matplotlib Figure
    def chart():
        fig, ax = plt.subplots()
        ax.bar(["Q1", "Q2", "Q3", "Q4"], [120, 90, 150, 110])
        ax.set_title("Quarterly Revenue")
        return fig

    @render.table                       # returns a DataFrame
    def summary():
        import pandas as pd
        return pd.DataFrame({"Quarter": ["Q1","Q2","Q3","Q4"],
                              "Revenue": [120, 90, 150, 110]})

    @render.text                        # returns a string
    def headline():
        return "Total revenue: $470K"

app = App(app_ui, server)""",
        "params": [
            ("@render.plot", "matplotlib/plotly", "Expects the function to return a matplotlib Figure or a plotly Figure object."),
            ("@render.table", "DataFrame", "Expects the function to return a pandas DataFrame, which Shiny renders as an HTML table."),
            ("@render.text", "string", "Expects the function to return a plain string, which Shiny displays as text content."),
            ("@render.ui", "UI elements", "Expects the function to return Shiny UI elements — useful for dynamic UI that changes based on input."),
        ],
        "tip": "If your plot appears blank, make sure you <code>return fig</code> at the end of the function — just calling <code>plt.show()</code> does not work inside Shiny because there is no interactive matplotlib window.",
    },
    {
        "label": "Layouts &amp; Panels",
        "icon": "fa6-solid:layer-group",
        "badge": "Page Design",
        "intro": "Shiny's layout functions let you arrange widgets and outputs into professional dashboard structures without writing CSS. You nest layout calls inside your UI definition to create sidebars, card grids, tabbed navigation, and full-height pages.",
        "code": """from shiny import ui

app_ui = ui.page_navbar(                    # top navigation bar
    ui.nav_panel("Overview",                # first tab
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_select("metric", "Metric", ["Revenue", "Users"]),
            ),
            ui.layout_columns(              # responsive column grid
                ui.value_box("Total", "$1.2M", showcase=ui.output_plot("spark1")),
                ui.value_box("Growth", "+12%", showcase=ui.output_plot("spark2")),
                col_widths=[6, 6],          # 2 equal columns (12-grid)
            ),
            ui.card(ui.output_plot("main_chart")),
        ),
    ),
    ui.nav_panel("Data Table",              # second tab
        ui.card(ui.output_table("raw_data")),
    ),
    title="Sales Dashboard",
)""",
        "params": [
            ("ui.page_navbar()", "page", "Creates a full page with a top navigation bar and multiple tab panels."),
            ("ui.layout_sidebar()", "layout", "Adds a collapsible sidebar to the left with a main content area on the right."),
            ("ui.layout_columns()", "grid", "Arranges children in a responsive column grid; use col_widths=[6,6] for two equal columns."),
            ("ui.card()", "container", "Wraps content in a bordered card with padding — the standard container for plots and tables."),
            ("ui.value_box()", "KPI", "Displays a headline metric with a title, value, and optional mini-chart (showcase)."),
        ],
        "tip": "Use <code>ui.page_fillable()</code> instead of <code>ui.page_sidebar()</code> when you want the page to fill the entire browser window — this is essential for full-screen dashboards where the chart should stretch to the available height.",
    },
]

code_examples = [
    {
        "title": "Minimal Shiny App",
        "desc": "This example shows the simplest possible Shiny for Python application — a slider input connected to a text output. It demonstrates the fundamental UI/server split and how Shiny automatically re-renders the output whenever the slider moves.",
        "code": """from shiny import App, ui, render

# UI: one slider + one text output
app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_slider("n", "Pick a number", 1, 100, 25),  # id="n"
    ),
    ui.card(
        ui.output_text_verbatim("result"),  # id="result"
    ),
)

# Server: read input.n(), return formatted string
def server(input, output, session):
    @render.text
    def result():                      # name must match "result" in UI
        return f"The square of {input.n()} is {input.n() ** 2}"

app = App(app_ui, server)""",
        "terminal_cmd": "shiny run app.py",
        "terminal_out": "INFO:     Uvicorn running on http://127.0.0.1:8000\nINFO:     Application startup complete.\n\n(Open browser → move slider to 7)\nThe square of 7 is 49",
        "tip": "Run a Shiny app from the terminal with <code>shiny run app.py</code>. The development server auto-reloads when you save changes — add <code>--reload</code> if it does not.",
    },
    {
        "title": "Reactive Filtering",
        "desc": "This example demonstrates how a @reactive.calc expression filters a DataFrame once and shares the result between a table output and a text summary — avoiding redundant computation.",
        "code": """from shiny import App, ui, render, reactive
import pandas as pd

# Sample data
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "dept": ["Sales", "Engineering", "Sales", "HR", "Engineering"],
    "salary": [72000, 95000, 68000, 61000, 88000],
})

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select("dept", "Department", ["All"] + df["dept"].unique().tolist()),
    ),
    ui.card(ui.output_table("tbl")),
    ui.card(ui.output_text("summary")),
)

def server(input, output, session):
    @reactive.calc
    def filtered():                              # cached reactive expression
        if input.dept() == "All":
            return df
        return df[df["dept"] == input.dept()]     # filter once

    @render.table
    def tbl():
        return filtered()                         # read cached result

    @render.text
    def summary():
        data = filtered()                         # same cache — no re-filter
        return f"{len(data)} employees, avg salary ${data['salary'].mean():,.0f}"

app = App(app_ui, server)""",
        "terminal_cmd": "shiny run reactive_filter.py",
        "terminal_out": "INFO:     Uvicorn running on http://127.0.0.1:8000\n\n(Select \"Sales\" from dropdown)\n2 employees, avg salary $70,000",
        "tip": "The <code>@reactive.calc</code> decorator caches the result, so calling <code>filtered()</code> from two different outputs does not run the filter twice — Shiny returns the cached DataFrame instantly on the second call.",
    },
    {
        "title": "Dynamic Plot Output",
        "desc": "This example shows how to render a matplotlib chart that updates reactively when the user selects a different column to plot. The @render.plot decorator expects the function to return a matplotlib Figure object.",
        "code": """from shiny import App, ui, render
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "revenue": [120, 135, 150, 142, 168],
    "users": [800, 920, 1050, 1100, 1250],
})

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select("metric", "Metric", ["revenue", "users"]),
        ui.input_checkbox("show_grid", "Show grid lines", value=True),
    ),
    ui.card(ui.output_plot("chart")),        # plot placeholder
)

def server(input, output, session):
    @render.plot
    def chart():
        fig, ax = plt.subplots(figsize=(8, 4))
        col = input.metric()                  # reactive read
        ax.bar(df["month"], df[col], color="#CB187D")
        ax.set_title(f"Monthly {col.title()}")
        ax.set_ylabel(col.title())
        if input.show_grid():                 # reactive read
            ax.grid(axis="y", alpha=0.3)
        return fig                            # must return the Figure

app = App(app_ui, server)""",
        "terminal_cmd": "shiny run plot_app.py",
        "terminal_out": "INFO:     Uvicorn running on http://127.0.0.1:8000\n\n(Select \"users\", check \"Show grid lines\")\n→ Bar chart updates to show monthly users with grid",
        "tip": "Always <code>return fig</code> at the end of a <code>@render.plot</code> function. Calling <code>plt.show()</code> alone does nothing inside Shiny — the framework needs the Figure object to embed it in the page.",
    },
    {
        "title": "Multi-Tab Dashboard",
        "desc": "This example builds a two-tab dashboard using ui.page_navbar(). Each tab has its own layout — the first tab uses a sidebar with value boxes, and the second tab displays a full-width data table.",
        "code": """from shiny import App, ui, render

app_ui = ui.page_navbar(
    ui.nav_panel("Dashboard",                   # Tab 1
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_select("region", "Region", ["North", "South", "East", "West"]),
            ),
            ui.layout_columns(
                ui.value_box("Revenue", ui.output_text("rev_val")),
                ui.value_box("Orders", ui.output_text("ord_val")),
                col_widths=[6, 6],              # two equal columns
            ),
            ui.card(ui.output_plot("trend")),
        ),
    ),
    ui.nav_panel("Raw Data",                    # Tab 2
        ui.card(
            ui.card_header("Full Dataset"),
            ui.output_table("raw"),
        ),
    ),
    title="Regional Sales",                     # navbar title
)

def server(input, output, session):
    @render.text
    def rev_val():
        totals = {"North": "$320K", "South": "$280K", "East": "$410K", "West": "$195K"}
        return totals.get(input.region(), "$0")

    @render.text
    def ord_val():
        counts = {"North": "1,240", "South": "980", "East": "1,580", "West": "720"}
        return counts.get(input.region(), "0")

    @render.plot
    def trend():
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3, 4], [100, 120, 115, 130], marker="o", color="#CB187D")
        ax.set_title(f"{input.region()} Quarterly Trend")
        return fig

    @render.table
    def raw():
        import pandas as pd
        return pd.DataFrame({"Region": ["North","South","East","West"],
                              "Revenue": [320, 280, 410, 195],
                              "Orders": [1240, 980, 1580, 720]})

app = App(app_ui, server)""",
        "terminal_cmd": "shiny run dashboard.py",
        "terminal_out": "INFO:     Uvicorn running on http://127.0.0.1:8000\n\n(Select \"East\" → Dashboard tab)\nRevenue: $410K  |  Orders: 1,580\n\n(Click \"Raw Data\" tab)\nRegion   Revenue   Orders\nNorth    320       1,240\n...",
        "tip": "Use <code>ui.page_navbar()</code> when your app needs multiple pages — each <code>ui.nav_panel()</code> becomes a top-level tab. This keeps complex dashboards organized without building a custom router.",
    },
    {
        "title": "Dynamic UI with render.ui",
        "desc": "This example demonstrates @render.ui, which lets the server generate UI elements dynamically based on user input. Here, selecting a department changes the available metric choices — something you cannot do with static UI alone.",
        "code": """from shiny import App, ui, render, reactive

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select("dept", "Department", ["Sales", "Engineering"]),
        ui.output_ui("dynamic_metric"),      # placeholder for dynamic widget
    ),
    ui.card(ui.output_text("selection")),
)

def server(input, output, session):
    @render.ui
    def dynamic_metric():
        if input.dept() == "Sales":
            choices = ["Revenue", "Deals Closed", "Pipeline"]
        else:
            choices = ["Commits", "Pull Requests", "Deployments"]
        return ui.input_select("metric", "Metric", choices)  # new widget

    @render.text
    def selection():
        return f"Showing {input.metric()} for {input.dept()}"

app = App(app_ui, server)""",
        "terminal_cmd": "shiny run dynamic_ui.py",
        "terminal_out": "INFO:     Uvicorn running on http://127.0.0.1:8000\n\n(Select \"Engineering\")\nDropdown changes to: Commits, Pull Requests, Deployments\nShowing Commits for Engineering",
        "tip": "<code>@render.ui</code> is powerful but should be used sparingly — every time the upstream input changes, Shiny destroys and recreates the dynamic widget, which resets its state. If you need the widget to remember its previous value, store it in a <code>reactive.value()</code> first.",
    },
]

comparison_rows = [
    ("fa6-solid:display", "UI / Server Split",
     "App(app_ui, server)",   "Separate UI layout object and server function joined by App() constructor.",
     "N/A",                   "SQL has no built-in UI layer — results are returned to a client application.",
     "VBA UserForm + Module", "Excel separates form design (UserForm) from logic (VBA Module), but wiring is manual."),
    ("fa6-solid:arrows-spin", "Reactive Updates",
     "@reactive.calc",        "Shiny auto-tracks dependencies and re-runs only when inputs change.",
     "Stored Procedure",      "SQL stored procedures run on demand — there is no automatic re-execution on data change.",
     "INDIRECT() / OFFSET()", "Excel formulas recalculate automatically, but there is no caching or dependency graph control."),
    ("fa6-solid:sliders", "Input Widgets",
     "ui.input_slider()",     "Built-in widgets capture user choices and feed them reactively to the server.",
     "WHERE clause",          "SQL filters are typed into the query text — there are no interactive widgets.",
     "Data Validation list",  "Excel dropdown lists provide input, but connecting them to charts requires manual VBA."),
    ("fa6-solid:chart-line", "Rendering Outputs",
     "@render.plot / .table", "Decorators bind a function to an output slot; Shiny handles rendering and updates.",
     "SELECT ... INTO",       "SQL outputs go to result sets or temp tables — formatting is the client's job.",
     "Chart object / PivotTable", "Excel charts update when source data changes, but creating them is a manual process."),
    ("fa6-solid:layer-group", "Page Layouts",
     "ui.page_navbar()",      "Composable layout functions create sidebars, tabs, and card grids with no CSS.",
     "N/A",                   "SQL has no layout concept — presentation is handled by the frontend application.",
     "Sheet tabs / Slicers",  "Excel uses sheet tabs for navigation and slicers for filtering, but layout options are limited."),
]

practice_exercises = [
    {
        "title": "Build a Minimal App",
        "tasks": [
            "Create a new file called <code>app.py</code> and import <code>App</code>, <code>ui</code>, and <code>render</code> from shiny.",
            "Define a UI with <code>ui.page_sidebar()</code> containing one <code>ui.input_slider()</code> (id=\"n\", range 1–50) and one <code>ui.output_text(\"greeting\")</code>.",
            "Write a server function with a <code>@render.text</code> function named <code>greeting</code> that returns <code>f\"Hello! You picked {input.n()}\"</code>.",
            "Create the app with <code>App(app_ui, server)</code> and run it with <code>shiny run app.py</code>.",
        ],
        "solution": """from shiny import App, ui, render

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_slider("n", "Pick a number", 1, 50, 10),
    ),
    ui.card(
        ui.output_text("greeting"),
    ),
)

def server(input, output, session):
    @render.text
    def greeting():
        return f"Hello! You picked {input.n()}"

app = App(app_ui, server)""",
        "why": "This exercise reinforces the core pattern every Shiny app follows: define UI → define server → connect them with App(). Once you can build this, every other feature is just adding more inputs and outputs to the same structure.",
    },
    {
        "title": "Add a Reactive Filter",
        "tasks": [
            "Start from the minimal app and add a <code>ui.input_select()</code> for choosing a department (Sales, Engineering, HR).",
            "Create a <code>@reactive.calc</code> function called <code>filtered</code> that filters a sample DataFrame by the selected department.",
            "Add a <code>@render.table</code> output that displays <code>filtered()</code>.",
            "Add a <code>@render.text</code> output that shows the row count: <code>f\"{len(filtered())} employees\"</code>.",
        ],
        "solution": """from shiny import App, ui, render, reactive
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "dept": ["Sales", "Engineering", "Sales", "HR", "Engineering"],
    "salary": [72000, 95000, 68000, 61000, 88000],
})

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select("dept", "Department", df["dept"].unique().tolist()),
    ),
    ui.card(ui.output_table("tbl")),
    ui.card(ui.output_text("count")),
)

def server(input, output, session):
    @reactive.calc
    def filtered():
        return df[df["dept"] == input.dept()]

    @render.table
    def tbl():
        return filtered()

    @render.text
    def count():
        return f"{len(filtered())} employees"

app = App(app_ui, server)""",
        "why": "This exercise shows why reactive expressions matter — <code>filtered()</code> runs the filter once and both outputs share the cached result. This is the pattern you will use in every real Shiny dashboard.",
    },
    {
        "title": "Render a Matplotlib Chart",
        "tasks": [
            "Add <code>import matplotlib.pyplot as plt</code> to your app.",
            "Add a <code>ui.output_plot(\"chart\")</code> placeholder to the UI.",
            "Write a <code>@render.plot</code> function named <code>chart</code> that creates a bar chart of the filtered data (department names on x-axis, salaries on y-axis).",
            "Make sure the function ends with <code>return fig</code> — do not call <code>plt.show()</code>.",
        ],
        "solution": """from shiny import App, ui, render, reactive
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "dept": ["Sales", "Engineering", "Sales", "HR", "Engineering"],
    "salary": [72000, 95000, 68000, 61000, 88000],
})

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select("dept", "Department", ["All"] + df["dept"].unique().tolist()),
    ),
    ui.card(ui.output_plot("chart")),
)

def server(input, output, session):
    @reactive.calc
    def filtered():
        if input.dept() == "All":
            return df
        return df[df["dept"] == input.dept()]

    @render.plot
    def chart():
        data = filtered()
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.bar(data["name"], data["salary"], color="#CB187D")
        ax.set_ylabel("Salary ($)")
        ax.set_title(f"Salaries — {input.dept()}")
        return fig  # return the Figure object, not plt.show()

app = App(app_ui, server)""",
        "why": "Returning a Figure object instead of calling plt.show() is the most common stumbling block for beginners coming from Jupyter notebooks. This exercise builds the muscle memory for the correct Shiny pattern.",
    },
    {
        "title": "Create a Tabbed Layout",
        "tasks": [
            "Replace <code>ui.page_sidebar()</code> with <code>ui.page_navbar()</code> to create a multi-tab app.",
            "Add two <code>ui.nav_panel()</code> tabs: \"Chart\" (with the plot) and \"Data\" (with the table).",
            "Move the sidebar inside the first tab using <code>ui.layout_sidebar()</code>.",
            "Set the navbar title to \"Employee Dashboard\".",
        ],
        "solution": """from shiny import App, ui, render, reactive
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "dept": ["Sales", "Engineering", "Sales", "HR", "Engineering"],
    "salary": [72000, 95000, 68000, 61000, 88000],
})

app_ui = ui.page_navbar(
    ui.nav_panel("Chart",
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_select("dept", "Department", ["All"] + df["dept"].unique().tolist()),
            ),
            ui.card(ui.output_plot("chart")),
        ),
    ),
    ui.nav_panel("Data",
        ui.card(ui.output_table("tbl")),
    ),
    title="Employee Dashboard",
)

def server(input, output, session):
    @reactive.calc
    def filtered():
        if input.dept() == "All":
            return df
        return df[df["dept"] == input.dept()]

    @render.plot
    def chart():
        data = filtered()
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.bar(data["name"], data["salary"], color="#CB187D")
        ax.set_ylabel("Salary ($)")
        ax.set_title(f"Salaries — {input.dept()}")
        return fig

    @render.table
    def tbl():
        return filtered()

app = App(app_ui, server)""",
        "why": "Multi-tab layouts are how real dashboards are organized — separating visualization from raw data keeps each view focused. The <code>ui.page_navbar()</code> pattern scales cleanly to 5+ tabs.",
    },
    {
        "title": "Add Dynamic UI",
        "tasks": [
            "Add a <code>ui.output_ui(\"dynamic_widget\")</code> placeholder inside the sidebar.",
            "Write a <code>@render.ui</code> server function that returns different <code>ui.input_select()</code> choices based on the selected department.",
            "For Sales, offer choices [\"Revenue\", \"Deals\"]; for Engineering, offer [\"Commits\", \"PRs\"]; for HR, offer [\"Headcount\", \"Turnover\"].",
            "Display the selected metric in a <code>@render.text</code> output.",
        ],
        "solution": """from shiny import App, ui, render, reactive

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_select("dept", "Department", ["Sales", "Engineering", "HR"]),
        ui.output_ui("dynamic_widget"),
    ),
    ui.card(ui.output_text("result")),
)

def server(input, output, session):
    @render.ui
    def dynamic_widget():
        dept = input.dept()
        metrics = {
            "Sales": ["Revenue", "Deals"],
            "Engineering": ["Commits", "PRs"],
            "HR": ["Headcount", "Turnover"],
        }
        return ui.input_select("metric", "Metric", metrics.get(dept, []))

    @render.text
    def result():
        return f"Viewing {input.metric()} for {input.dept()}"

app = App(app_ui, server)""",
        "why": "Dynamic UI is essential when the available options in one widget depend on the value of another widget. The <code>@render.ui</code> pattern lets you build cascading dropdowns — a common requirement in business dashboards.",
    },
]

mistakes = [
    {
        "title": "Forgetting Parentheses on Input Reads",
        "why_happens": "Beginners treat input.n as a regular variable instead of a reactive signal that must be called.",
        "wrong": """# input.n without parentheses returns the reactive object
@render.text
def result():
    return f"Value: {input.n}"   # BUG: prints <reactive object>""",
        "correct": """# input.n() with parentheses returns the actual value
@render.text
def result():
    return f"Value: {input.n()}"  # Correct: returns the number""",
        "fix": "Always call input values with parentheses — <code>input.n()</code> not <code>input.n</code>. The parentheses trigger the reactive read and return the current value.",
    },
    {
        "title": "Output Name Mismatch Between UI and Server",
        "why_happens": "The output id in the UI does not match the function name in the server, so Shiny silently ignores the function.",
        "wrong": """# UI says "result" but server function is named "output_text"
app_ui = ui.page_sidebar(
    ui.card(ui.output_text("result")),   # id = "result"
)

def server(input, output, session):
    @render.text
    def output_text():           # BUG: name is "output_text", not "result"
        return "Hello"           # nothing appears in the UI""",
        "correct": """# Server function name matches the UI output id exactly
app_ui = ui.page_sidebar(
    ui.card(ui.output_text("result")),   # id = "result"
)

def server(input, output, session):
    @render.text
    def result():                # Correct: matches "result" in UI
        return "Hello"           # text appears in the card""",
        "fix": "The server function name must exactly match the <code>id</code> string you passed to the output placeholder in the UI. If nothing renders, check for typos in both places.",
    },
    {
        "title": "Calling plt.show() Instead of Returning the Figure",
        "why_happens": "In Jupyter notebooks, plt.show() displays the chart — but inside Shiny, there is no interactive matplotlib window.",
        "wrong": """@render.plot
def chart():
    fig, ax = plt.subplots()
    ax.bar(["A", "B"], [10, 20])
    plt.show()   # BUG: shows nothing in Shiny
    # no return statement""",
        "correct": """@render.plot
def chart():
    fig, ax = plt.subplots()
    ax.bar(["A", "B"], [10, 20])
    return fig   # Correct: Shiny embeds the Figure object""",
        "fix": "Replace <code>plt.show()</code> with <code>return fig</code> at the end of every <code>@render.plot</code> function. Shiny needs the Figure object to convert it into an image for the browser.",
    },
    {
        "title": "Expensive Computation Outside a Reactive Context",
        "why_happens": "Placing pd.read_csv() or a database query at the module level means it runs once at startup and never updates when inputs change.",
        "wrong": """# Data loaded once at import time — never refreshes
df = pd.read_csv("sales.csv")

def server(input, output, session):
    @render.table
    def tbl():
        return df[df["region"] == input.region()]  # stale data""",
        "correct": """def server(input, output, session):
    @reactive.calc
    def data():
        return pd.read_csv("sales.csv")  # re-reads when invalidated

    @render.table
    def tbl():
        return data()[data()["region"] == input.region()]""",
        "fix": "Wrap data loading inside a <code>@reactive.calc</code> if the data can change, or keep it at module level only for truly static lookup tables. For most dashboards, loading inside a reactive expression is safer.",
    },
    {
        "title": "Forgetting the @render Decorator",
        "why_happens": "The function looks correct but Shiny never registers it as an output because the decorator is missing.",
        "wrong": """def server(input, output, session):
    # Missing @render.text decorator
    def result():
        return f"Total: {input.n()}"
    # Shiny never calls this function — output stays blank""",
        "correct": """def server(input, output, session):
    @render.text              # decorator tells Shiny this is an output
    def result():
        return f"Total: {input.n()}"
    # Shiny calls result() whenever input.n() changes""",
        "fix": "Every output function needs a <code>@render.*</code> decorator. Without it, Shiny treats the function as a regular helper and never connects it to the UI placeholder.",
    },
]

real_world = [
    ("fa6-solid:chart-pie",       "Executive Dashboards",      "Finance teams build Shiny dashboards that let executives explore revenue, expenses, and KPIs through dropdown filters and date ranges without waiting for a weekly email report."),
    ("fa6-solid:flask",           "Lab Data Monitoring",       "Research labs use Shiny apps to display real-time sensor readings from experiments — reactive expressions update charts the moment new data arrives from an instrument."),
    ("fa6-solid:hospital",        "Patient Intake Forms",      "Healthcare organizations use Shiny to build intake applications where dynamic UI shows different follow-up questions based on the patient's initial responses."),
    ("fa6-solid:graduation-cap",  "Student Grade Portals",     "Universities deploy Shiny dashboards where students select their courses from a dropdown and instantly see grade distributions and progress charts."),
    ("fa6-solid:warehouse",       "Inventory Management",      "Supply chain teams build Shiny apps that show stock levels across warehouses — managers filter by region and product category to spot low-inventory alerts."),
    ("fa6-solid:bullhorn",        "Marketing Campaign Tracker", "Marketing departments use Shiny to build campaign performance dashboards where selecting a campaign updates cost, reach, and conversion metrics simultaneously."),
]

quiz = [
    {
        "type": "tf",
        "stem": "In Shiny for Python, the server function runs once when the app starts and never runs again.",
        "answer": False,
        "fb_correct": "Correct! The server function's inner render functions re-execute automatically whenever their upstream reactive inputs change.",
        "fb_wrong": "Not quite — Shiny's reactive engine re-runs render functions whenever an input they depend on changes. That is the core of reactivity.",
    },
    {
        "type": "tf",
        "stem": "A @reactive.calc expression re-runs every time any input in the entire app changes, regardless of whether the expression reads that input.",
        "answer": False,
        "fb_correct": "Correct! A @reactive.calc only re-runs when the specific inputs it reads inside its body change — not every input in the app.",
        "fb_wrong": "Not quite — Shiny tracks which inputs a reactive expression actually reads and only invalidates it when those specific inputs change.",
    },
    {
        "type": "mc",
        "stem": "Your Shiny app has a slider with <code>id=\"sample_size\"</code>. Which line correctly reads its value inside the server function?",
        "options": [
            ("input.sample_size", False),
            ("input.sample_size()", True),
            ("input['sample_size']", False),
            ("ui.input_slider('sample_size')", False),
        ],
        "fb_correct": "Correct! input.sample_size() with parentheses returns the current value and registers a reactive dependency.",
        "fb_wrong": "Not quite — you must call input.sample_size() with parentheses. Without them, you get the reactive signal object, not the value.",
    },
    {
        "type": "mc",
        "stem": "You want a bar chart to appear in a <code>ui.output_plot(\"chart\")</code> placeholder. Which decorator and return pattern is correct?",
        "options": [
            ("@render.text, return fig", False),
            ("@render.plot, plt.show()", False),
            ("@render.plot, return fig", True),
            ("@render.table, return fig", False),
        ],
        "fb_correct": "Correct! @render.plot expects the function to return a matplotlib Figure object — never call plt.show() inside Shiny.",
        "fb_wrong": "Not quite — use @render.plot and end the function with return fig. Calling plt.show() does not work inside Shiny.",
    },
    {
        "type": "mc",
        "stem": "Which Shiny layout function creates a page with a top navigation bar and multiple tab panels?",
        "options": [
            ("ui.page_sidebar()", False),
            ("ui.page_navbar()", True),
            ("ui.layout_columns()", False),
            ("ui.page_fillable()", False),
        ],
        "fb_correct": "Correct! ui.page_navbar() creates a top nav bar where each ui.nav_panel() becomes a separate tab.",
        "fb_wrong": "Not quite — ui.page_navbar() is the function that creates a top navigation bar with tab panels. ui.page_sidebar() creates a single-page layout with a sidebar.",
    },
]

next_preview = [
    ("fa6-solid:scale-balanced", "Head-to-head comparison of Streamlit and Shiny"),
    ("fa6-solid:list-check",     "Decision framework for choosing the right tool"),
    ("fa6-solid:puzzle-piece",   "When to use each framework in practice"),
]

sidebar_lessons = [
    ("lesson01_why_build_data_apps.html",            "Why Build Data Apps?"),
    ("lesson02_introduction_to_streamlit.html",      "Introduction to Streamlit"),
    ("lesson03_interactive_filters.html",            "Interactive Filters"),
    ("lesson04_exporting_data.html",                 "Exporting Data"),
    ("lesson05_deploying_data_applications.html",    "Deploying Data Applications"),
    ("lesson06_shiny_for_python.html",               "Shiny for Python"),
    ("lesson07_streamlit_vs_shiny.html",             "Streamlit vs Shiny"),
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

# ── TOC links (12 canonical sections, no decision-flow) ───
toc_sections = [
    ("objective",       "fa6-solid:bullseye",          "Lesson Objective"),
    ("overview",        "fa6-solid:binoculars",        "Overview"),
    ("key-ideas",       "fa6-solid:lightbulb",         "Key Takeaways"),
    ("key-concepts",    "fa6-solid:book-open",         "Key Concepts"),
    ("code-examples",   "fa6-solid:code",              "Code Examples"),
    ("comparison",      "fa6-solid:scale-balanced",    "SQL / Excel Comparison"),
    ("practice",        "fa6-solid:pencil",            "Practice Exercises"),
    ("mistakes",        "fa6-solid:triangle-exclamation","Common Mistakes"),
    ("real-world",      "fa6-solid:briefcase",         "Real-World Use"),
    ("recap",           "fa6-solid:list-check",        "Lesson Recap"),
    ("knowledge-check", "fa6-solid:brain",             "Knowledge Check"),
    ("next-lesson",     "fa6-solid:circle-arrow-right","Next Lesson"),
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
        {amber_tip(f'This lesson covers <strong>{n} key concepts</strong> for building reactive dashboards with Shiny for Python &mdash; the UI/server architecture, reactive expressions, input widgets, render decorators, and layout functions.')}
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
    {section_header("fa6-solid:binoculars", "Overview", "A high-level introduction to Shiny for Python")}
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
    n = len(code_examples)
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

# ── Comparison ────────────────────────────────────────────
def build_comparison():
    rows_html = []
    for i, (icon, label, py_code, py_desc, sql_code, sql_desc, xl_code, xl_desc) in enumerate(comparison_rows):
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
      <span class="text-xs text-gray-400">Python</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-indigo-50 text-indigo-700">{py_code}</code>
      <p class="text-xs text-gray-500 leading-relaxed">{py_desc}</p>
    </div>
    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">SQL</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-orange-50 text-orange-700">{sql_code}</code>
      <p class="text-xs text-gray-500 leading-relaxed">{sql_desc}</p>
    </div>
    <div class="px-4 py-4 flex flex-col gap-2">
      <span class="text-xs text-gray-400">Excel</span>
      <code class="text-xs font-mono font-semibold px-2 py-1 rounded-lg self-start bg-emerald-50 text-emerald-700">{xl_code}</code>
      <p class="text-xs text-gray-500 leading-relaxed">{xl_desc}</p>
    </div>
  </div>
</div>""")
    return f"""<section id="comparison">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:scale-balanced", "SQL / Excel Comparison", "How Shiny concepts compare across Python, SQL, and Excel")}
    <div class="bg-white px-8 py-7 space-y-5">
      {"".join(rows_html)}
    </div>
  </div>
</section>"""

# ── Practice ──────────────────────────────────────────────
def build_practice():
    n = len(practice_exercises)
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
    n = len(mistakes)
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
        <p class="text-sm text-gray-700 leading-relaxed">Shiny for Python is used wherever teams need reactive, server-rendered dashboards that keep data logic secure on the backend &mdash; from healthcare portals to executive KPI trackers, the reactive model handles real-time updates without exposing raw data to the browser.</p>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
        {"".join(cards)}
      </div>
    </div>
  </div>
</section>"""

# ── Recap ─────────────────────────────────────────────────
recap_items = [
    ("fa6-solid:display",        "UI / Server Architecture",  "You learned that every Shiny app splits into a UI object that describes the interface and a server function that contains the logic, connected by the <code>App()</code> constructor."),
    ("fa6-solid:arrows-spin",    "Reactive Expressions",      "You learned that <code>@reactive.calc</code> creates a cached computation that only re-runs when its upstream inputs change, eliminating redundant work."),
    ("fa6-solid:sliders",        "Input Widgets",             "You learned to add sliders, dropdowns, checkboxes, and text fields using <code>ui.input_*()</code> functions and read their values with <code>input.id()</code>."),
    ("fa6-solid:chart-line",     "Render Decorators",         "You learned that <code>@render.plot</code>, <code>@render.table</code>, and <code>@render.text</code> bind server functions to UI output placeholders."),
    ("fa6-solid:layer-group",    "Dashboard Layouts",         "You learned to organize apps with <code>ui.page_navbar()</code>, <code>ui.layout_sidebar()</code>, <code>ui.card()</code>, and <code>ui.value_box()</code>."),
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
    n = len(quiz)
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

# ── Next Lesson ───────────────────────────────────────────
def build_next_lesson():
    preview_cards = []
    for icon, text in next_preview:
        preview_cards.append(f"""<div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
  <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0"><span class="iconify text-white text-sm" data-icon="{icon}"></span></span>
  <div><p class="text-sm font-semibold text-gray-700">{text}</p></div>
</div>""")
    next_num = LESSON_NUM + 1
    return f"""<section id="next-lesson" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    {section_header("fa6-solid:circle-arrow-right", "Next Lesson", "Preview of what comes next")}
    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
          <span class="text-white font-bold text-lg">{next_num}</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module {MODULE_NUM} &middot; Lesson {next_num}</p>
          <h3 class="text-base font-bold text-gray-800">{NEXT_LESSON[1]}</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
          {"".join(preview_cards)}
        </div>
      </div>
    </div>
  </div>
</section>"""

# ── Bottom Nav ────────────────────────────────────────────
def build_bottom_nav():
    prev_html = f"""<a href="{PREV_LESSON[0]}" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{PREV_LESSON[1]}</p>
      </div>
    </a>"""
    next_html = f"""<a href="{NEXT_LESSON[0]}" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">{NEXT_LESSON[1]}</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>"""
    return f"""<section>
  <div class="flex flex-col sm:flex-row gap-3">
    {prev_html}
    <a href="../../hub_home_page.html" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>
    {next_html}
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
