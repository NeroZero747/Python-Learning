#!/usr/bin/env python3
"""Rewrite #real-world section for all 28 track_02 lessons."""

import re, os, sys

ROOT = r"c:\Users\nightwolf\Projects\Python-Learning\pages\track_02_data_analytics"
PATTERN = re.compile(r'<section id="real-world">.*?</section>', re.DOTALL)

MOD01 = "mod_01_data_analysis_with_pandas"
MOD02 = "mod_02_working_with_data_sources"
MOD03 = "mod_03_python_for_analysts"
MOD04 = "mod_04_handling_large_data"

# ── Color token map ────────────────────────────────────────────────────────────
COLOR = {
    "violet": dict(
        border="border-violet-100",
        bg="from-violet-50 via-white to-purple-50",
        icon_from="from-violet-500", icon_to="to-purple-600",
        shadow="shadow-violet-200",
        pill_bg="bg-violet-100", pill_border="border-violet-200", pill_text="text-violet-700",
        code="text-violet-700",
    ),
    "pink": dict(
        border="border-pink-100",
        bg="from-pink-50 via-white to-rose-50",
        icon_from="from-[#CB187D]", icon_to="to-[#e84aad]",
        shadow="shadow-pink-200",
        pill_bg="bg-pink-100", pill_border="border-pink-200", pill_text="text-[#CB187D]",
        code="text-[#CB187D]",
    ),
    "emerald": dict(
        border="border-emerald-100",
        bg="from-emerald-50 via-white to-teal-50",
        icon_from="from-emerald-500", icon_to="to-teal-600",
        shadow="shadow-emerald-200",
        pill_bg="bg-emerald-100", pill_border="border-emerald-200", pill_text="text-emerald-700",
        code="text-emerald-700",
    ),
    "blue": dict(
        border="border-blue-100",
        bg="from-blue-50 via-white to-indigo-50",
        icon_from="from-blue-500", icon_to="to-indigo-600",
        shadow="shadow-blue-200",
        pill_bg="bg-blue-100", pill_border="border-blue-200", pill_text="text-blue-700",
        code="text-blue-700",
    ),
    "amber": dict(
        border="border-amber-100",
        bg="from-amber-50 via-white to-orange-50",
        icon_from="from-amber-400", icon_to="to-orange-500",
        shadow="shadow-amber-200",
        pill_bg="bg-amber-100", pill_border="border-amber-200", pill_text="text-amber-700",
        code="text-amber-700",
    ),
}


# ── HTML builders ──────────────────────────────────────────────────────────────

def card_html(icon, color, headline, body, returns):
    c = COLOR[color]
    return (
        f'<div class="relative rounded-2xl overflow-hidden border {c["border"]} bg-gradient-to-br {c["bg"]} px-6 py-6 text-center">\n'
        '  <div class="flex flex-col items-center gap-3">\n'
        f'    <span class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-gradient-to-br {c["icon_from"]} {c["icon_to"]} shadow-lg {c["shadow"]}">\n'
        f'      <span class="iconify text-white text-2xl" data-icon="{icon}"></span>\n'
        '    </span>\n'
        f'    <h3 class="text-sm font-bold text-gray-800 leading-snug">{headline}</h3>\n'
        f'    <p class="text-xs text-gray-500 leading-relaxed">{body}</p>\n'
        f'    <div class="flex items-center gap-1.5 mt-1 px-3 py-1.5 rounded-full border {c["pill_bg"]} {c["pill_border"]}">\n'
        f'      <span class="iconify {c["pill_text"]} text-[11px]" data-icon="fa6-solid:arrow-right-from-bracket"></span>\n'
        f'      <span class="text-[11px] font-semibold {c["pill_text"]}">returns <code class="font-mono">{returns}</code></span>\n'
        '    </div>\n'
        '  </div>\n'
        '</div>'
    )


def table_html(topic, without_rows, with_rows):
    def without_row(text):
        return (
            '<div class="flex items-start gap-2.5">\n'
            '  <span class="iconify text-red-300 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:xmark"></span>\n'
            f'  <p class="text-xs text-gray-500 leading-relaxed">{text}</p>\n'
            '</div>'
        )
    def with_row(text):
        return (
            '<div class="flex items-start gap-2.5">\n'
            '  <span class="iconify text-emerald-400 text-sm shrink-0 mt-0.5" data-icon="fa6-solid:check"></span>\n'
            f'  <p class="text-xs text-gray-500 leading-relaxed">{text}</p>\n'
            '</div>'
        )
    wo = "\n        ".join(without_row(r) for r in without_rows)
    wi = "\n        ".join(with_row(r) for r in with_rows)
    return (
        '<div class="rounded-xl border border-gray-100 overflow-hidden">\n'
        '  <div class="grid grid-cols-2">\n'
        '    <div class="border-r border-gray-100">\n'
        '      <div class="flex items-center gap-2 px-4 py-3 bg-red-50 border-b border-red-100">\n'
        '        <span class="iconify text-red-400 text-sm shrink-0" data-icon="fa6-solid:circle-xmark"></span>\n'
        f'        <p class="text-xs font-bold text-red-500 uppercase tracking-wide">Without {topic}</p>\n'
        '      </div>\n'
        '      <div class="px-4 py-4 space-y-3">\n'
        f'        {wo}\n'
        '      </div>\n'
        '    </div>\n'
        '    <div>\n'
        '      <div class="flex items-center gap-2 px-4 py-3 bg-[#fdf0f7] border-b border-[#f5c6e0]">\n'
        '        <span class="iconify text-[#CB187D] text-sm shrink-0" data-icon="fa6-solid:circle-check"></span>\n'
        f'        <p class="text-xs font-bold text-[#CB187D] uppercase tracking-wide">With {topic}</p>\n'
        '      </div>\n'
        '      <div class="px-4 py-4 space-y-3">\n'
        f'        {wi}\n'
        '      </div>\n'
        '    </div>\n'
        '  </div>\n'
        '</div>'
    )


def build_section(intro, subtitle, topic, cards, without_rows, with_rows):
    grid = (
        '<div class="grid grid-cols-1 md:grid-cols-3 gap-4">\n'
        + "\n".join(card_html(*c) for c in cards)
        + '\n</div>'
    )
    tbl = table_html(topic, without_rows, with_rows)
    return (
        '<section id="real-world">\n'
        '  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">\n'
        '    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">\n'
        '      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">\n'
        '        <span class="iconify text-white text-base" data-icon="fa6-solid:briefcase"></span>\n'
        '      </span>\n'
        '      <div class="min-w-0">\n'
        '        <h2 class="text-xl font-bold text-gray-900 leading-tight">Real-World Use</h2>\n'
        f'        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">How {subtitle} is used across real-world workflows</p>\n'
        '      </div>\n'
        '    </div>\n'
        '    <div class="bg-white px-8 py-7 space-y-5">\n'
        f'      <p class="text-sm text-gray-600 leading-relaxed">{intro}</p>\n'
        f'      {grid}\n'
        f'      {tbl}\n'
        '    </div>\n'
        '  </div>\n'
        '</section>'
    )


# ── Lesson data ────────────────────────────────────────────────────────────────
# Each entry:
#   (intro, subtitle, table_topic, cards, without_rows, with_rows)
#   cards: list of 3x (icon, color, headline, body_html, returns)
#   body_html may include <code class="font-mono COLOR">text</code> inline
#   with_rows may include <strong class="text-gray-700">...</strong>

LESSONS = {

    # ── MOD 01 ────────────────────────────────────────────────────────────────

    f"{MOD01}/lesson01_introduction_to_pandas.html": (
        "Imagine you work on a retail data team. Every month you receive dozens of store reports and need to produce one clean summary. Without a tool like pandas, that means hours of copy-pasting and manual formatting. Pandas gives you a single script that loads, combines, and exports everything in minutes.",
        "pandas", "pandas",
        [
            ("fa6-solid:shop", "violet",
             "Monthly sales across<br>50 store locations",
             'You receive 50 CSV files every month — one per store. <code class="font-mono text-violet-700">pd.read_csv()</code> and <code class="font-mono text-violet-700">pd.concat()</code> load and stack all 50 into a single DataFrame in seconds.',
             "combined_df"),
            ("fa6-solid:chart-bar", "pink",
             "Revenue trends for<br>the past 3 years",
             'Your dataset spans 3 years of daily transactions. You filter the DataFrame by date range and call <code class="font-mono text-[#CB187D]">groupby().sum()</code> to compute monthly totals — one line per step.',
             "monthly_totals"),
            ("fa6-solid:file-lines", "emerald",
             "Weekly report<br>sent to the board",
             'Every Friday the board expects a clean Excel summary. <code class="font-mono text-emerald-700">to_excel()</code> writes the formatted file automatically — no manual formatting, no missed columns.',
             "report.xlsx"),
        ],
        [
            "You open 50 spreadsheets by hand and copy-paste each store's data into a master file — every month.",
            "Filtering 3 years of rows and summing by month in Excel requires complex formulas across thousands of cells.",
            "You format and save the Excel board report by hand every Friday — a rush means wrong totals or missing columns.",
        ],
        [
            '<strong class="text-gray-700">pd.read_csv()</strong> and <strong class="text-gray-700">pd.concat()</strong> load and stack all 50 files in seconds — no copy-pasting.',
            '<strong class="text-gray-700">groupby().sum()</strong> calculates every monthly total from the full 3-year dataset in a single line.',
            '<strong class="text-gray-700">to_excel()</strong> writes the board report automatically — same format, same columns, every week.',
        ],
    ),

    f"{MOD01}/lesson02_dataframes_explained.html": (
        "Imagine you work on a human resources team. You receive a CSV export of 1,200 employee records and need to check data quality before payroll runs. A DataFrame gives you instant access to every row and column, and tells you exactly what types and gaps you are dealing with.",
        "DataFrames", "DataFrames",
        [
            ("fa6-solid:users", "violet",
             "Employee records<br>for 1,200 staff",
             'Your HR system exports a CSV of 1,200 employees every month. <code class="font-mono text-violet-700">pd.read_csv()</code> loads the whole file into a DataFrame — one table you can query from that point forward.',
             "employees_df"),
            ("fa6-solid:magnifying-glass", "pink",
             "Data quality check<br>before payroll runs",
             'Before processing payroll you need to confirm column types and spot gaps. <code class="font-mono text-[#CB187D]">df.dtypes</code> and <code class="font-mono text-[#CB187D]">df.isnull().sum()</code> give you both answers in two lines.',
             "type + null summary"),
            ("fa6-solid:chart-column", "emerald",
             "Headcount report<br>by department",
             'The monthly headcount report needs staff counts per department. <code class="font-mono text-emerald-700">df.shape</code> confirms total rows and <code class="font-mono text-emerald-700">groupby()</code> breaks them down by department.',
             "headcount_df"),
        ],
        [
            "You open the CSV in Excel to check it — but Excel doesn't tell you column types, and spotting nulls means scrolling through 1,200 rows manually.",
            "Checking for gaps before payroll means filtering each column and counting blank cells — a slow, error-prone process in Excel.",
            "Building a headcount table by department in Excel means writing COUNTIF formulas for each of the 15 departments one by one.",
        ],
        [
            '<strong class="text-gray-700">pd.read_csv()</strong> loads the file instantly and gives you a fully indexed DataFrame ready to inspect.',
            '<strong class="text-gray-700">df.dtypes</strong> and <strong class="text-gray-700">df.isnull().sum()</strong> surface all type and null issues in two lines — before a single calculation runs.',
            '<strong class="text-gray-700">groupby()</strong> counts rows per department in one call — no COUNTIF formulas, no manual updates.',
        ],
    ),

    f"{MOD01}/lesson03_reading_data_csv_excel.html": (
        "Imagine you work on a supply chain team. Every morning a warehouse CSV arrives with the day's 10,000 orders, and every month a supplier delivers stock data as a multi-sheet Excel file. Reading both correctly is the first step — if the import breaks, every downstream calculation is wrong.",
        "reading data", "reading data",
        [
            ("fa6-solid:file-arrow-down", "violet",
             "Daily order file<br>from the warehouse",
             'Your warehouse sends a CSV of 10,000 orders every morning. <code class="font-mono text-violet-700">pd.read_csv()</code> loads all rows into a DataFrame in under a second, ready for the day\'s processing.',
             "orders_df"),
            ("fa6-solid:file-lines", "pink",
             "Monthly supplier report<br>in Excel format",
             'Your supplier sends a multi-sheet xlsx file every month. <code class="font-mono text-[#CB187D]">pd.read_excel(sheet_name=)</code> opens the correct sheet by name and returns it as a DataFrame.',
             "stock_df"),
            ("fa6-solid:eye", "emerald",
             "Spot errors before<br>analysis begins",
             'After every file load you call <code class="font-mono text-emerald-700">df.head()</code> and <code class="font-mono text-emerald-700">df.info()</code> to catch column-name typos or wrong data types before any calculations run.',
             "preview + types"),
        ],
        [
            "The warehouse CSV has a tab delimiter this month — your import script silently loads one mangled column and all downstream calculations are wrong.",
            "The supplier sends the stock data on sheet 3 this month instead of sheet 1 — you load the wrong sheet and don't notice until the report is sent.",
            "You run analysis on the freshly imported file and discover halfway through that the date column was read as text — all date filters return nothing.",
        ],
        [
            '<strong class="text-gray-700">pd.read_csv(sep=)</strong> lets you specify any delimiter so the import works correctly regardless of how the file was exported.',
            '<strong class="text-gray-700">pd.read_excel(sheet_name=)</strong> loads the correct sheet by name — it never matters what position the sheet is in.',
            '<strong class="text-gray-700">df.info()</strong> shows every column type immediately after loading — you catch a text date column before touching the data.',
        ],
    ),

    f"{MOD01}/lesson04_selecting_columns.html": (
        "Imagine you work on a finance team. Your transactions table has 40 columns, but the reconciliation report needs only 3. Selecting, renaming, and dropping columns in pandas lets you work with exactly the data you need — nothing more, nothing less.",
        "selecting columns", "selecting columns",
        [
            ("fa6-solid:hand-pointer", "violet",
             "Transaction table<br>with 40 columns",
             'Your transactions table has 40 columns but reconciliation needs only date, account, and amount. Passing a list to <code class="font-mono text-violet-700">df[[\"date\",\"account\",\"amount\"]]</code> returns exactly those three — the other 37 are ignored.',
             "subset_df"),
            ("fa6-solid:pen", "pink",
             "Legacy column names<br>from the source system",
             'Your data source exports codes like ACC_NO and TRN_AMT. <code class="font-mono text-[#CB187D]">rename()</code> maps each code to a clear name so every downstream script uses consistent labels without editing the source.',
             "clean_df"),
            ("fa6-solid:shield", "emerald",
             "Audit pack before<br>sharing with partners",
             'Before sharing the dataset externally you list all columns with <code class="font-mono text-emerald-700">df.columns</code>, identify sensitive fields, and remove them with <code class="font-mono text-emerald-700">drop()</code> so no internal data leaves the business.',
             "safe_df"),
        ],
        [
            "You open the 40-column file in Excel, hide the unwanted columns, and hope the hidden columns aren't accidentally included when you share the file.",
            "Every report that uses ACC_NO breaks the moment a new team member doesn't know what the code means — and column names have to be manually cleaned in every workbook.",
            "Checking a 40-column file for sensitive data before a share means scrolling through every column header by hand — easy to miss one.",
        ],
        [
            '<strong class="text-gray-700">df[[\"col1\",\"col2\"]]</strong> returns only the columns you name — no hidden data, no accidental inclusion.',
            '<strong class="text-gray-700">rename()</strong> replaces every code with a clear label in one call — all downstream scripts get consistent names automatically.',
            '<strong class="text-gray-700">df.columns</strong> lists every field in seconds, and <strong class="text-gray-700">drop()</strong> removes sensitive ones before the file is shared.',
        ],
    ),

    f"{MOD01}/lesson05_filtering_rows.html": (
        "Imagine you work on an e-commerce operations team. Your orders table has 50,000 rows and you regularly need different slices — refunded orders, high-value orders in certain regions, orders ready to ship. Boolean filtering in pandas gives you the exact rows you need in milliseconds.",
        "filtering rows", "row filtering",
        [
            ("fa6-solid:filter", "violet",
             "50,000 orders,<br>only show refunds",
             'You need to isolate refunded orders from 50,000 rows. One boolean condition — <code class="font-mono text-violet-700">df[df[\"status\"]==\"refunded\"]</code> — returns only those rows instantly, without touching the rest.',
             "refunds_df"),
            ("fa6-solid:code-branch", "pink",
             "High-value orders<br>in two regions",
             'Your manager needs orders over £500 from the North and West regions. You combine two conditions with <code class="font-mono text-[#CB187D]">&amp;</code> and <code class="font-mono text-[#CB187D]">isin()</code> in a single filter expression.',
             "priority_df"),
            ("fa6-solid:circle-xmark", "emerald",
             "Missing address<br>blocks every shipment",
             'Orders without a delivery address cannot be shipped. <code class="font-mono text-emerald-700">dropna(subset=[\"address\"])</code> removes only those rows before the shipping file is generated — valid orders are untouched.',
             "shippable_df"),
        ],
        [
            "Filtering 50,000 rows in Excel means setting AutoFilter dropdowns manually — one mistake shows the wrong orders and the wrong team gets the wrong list.",
            "Combining two filter conditions in Excel requires an AND() or helper column — for 50,000 rows this is slow and fragile when the source data refreshes.",
            "Checking each order for a missing address in Excel means writing an ISBLANK formula and filtering by it — then deleting those rows before saving the shipping file.",
        ],
        [
            '<strong class="text-gray-700">df[df[\"status\"]==\"refunded\"]</strong> isolates refunded orders from 50,000 rows in milliseconds — no dropdown, no mistake.',
            '<strong class="text-gray-700">&amp;</strong> and <strong class="text-gray-700">isin()</strong> combine conditions in one expression that updates automatically when the source data changes.',
            '<strong class="text-gray-700">dropna(subset=)</strong> removes only incomplete rows — valid orders pass through unchanged every time the script runs.',
        ],
    ),

    f"{MOD01}/lesson06_creating_calculated_columns.html": (
        "Imagine you work on a retail pricing team. Your product catalogue has 8,000 rows and you regularly need to add tax amounts, apply sale labels, and strip internal cost data before sharing prices externally. Calculated columns in pandas let you do all three in seconds — not hours.",
        "calculated columns", "calculated columns",
        [
            ("fa6-solid:calculator", "violet",
             "Apply 15% VAT to<br>8,000 product prices",
             'Your catalogue has 8,000 products. You add a vat_amount column by writing <code class="font-mono text-violet-700">df[\"vat_amount\"] = df[\"price\"] * 0.15</code> — every row is calculated at once, with no formula dragging.',
             "vat_amount"),
            ("fa6-solid:toggle-on", "pink",
             "Label products as<br>sale or full price",
             'Each product is either on sale or full price. <code class="font-mono text-[#CB187D]">np.where()</code> writes the correct label into a new column for all 8,000 rows based on the discount flag — one line of code.',
             "price_label"),
            ("fa6-solid:trash", "emerald",
             "Remove cost data<br>before sharing externally",
             'Before sending the price list to external partners you remove cost_price and margin. <code class="font-mono text-emerald-700">drop()</code> deletes both columns instantly — no risk of accidentally sharing sensitive data.',
             "partner_df"),
        ],
        [
            "Dragging a formula down 8,000 rows in Excel works — until someone inserts a row, breaks the formula chain, and the VAT is wrong for every product below that point.",
            "Writing an IF formula for 8,000 rows to set a sale label is slow to build, and if the sale condition changes you have to update the formula in every cell.",
            "Hiding columns in Excel before sharing is fragile — a recipient can simply unhide them and see your cost data.",
        ],
        [
            '<strong class="text-gray-700">df[\"vat_amount\"] = df[\"price\"] * 0.15</strong> applies the calculation to all 8,000 rows at once — no dragging, no broken formula chains.',
            '<strong class="text-gray-700">np.where()</strong> labels all 8,000 rows in one call — change the condition once and it applies everywhere instantly.',
            '<strong class="text-gray-700">drop()</strong> permanently removes the cost columns from the DataFrame — they cannot be unhidden because they no longer exist.',
        ],
    ),

    f"{MOD01}/lesson07_aggregations_group_by.html": (
        "Imagine you work on a sales reporting team. Your transaction table has 200,000 rows and your stakeholders want summaries by region, by product category, and by week — with five different metrics each. Pandas groupby aggregations collapse all of that into a few lines of code.",
        "groupby aggregations", "groupby",
        [
            ("fa6-solid:object-group", "violet",
             "Sales across<br>12 regions",
             'Your 200,000-row transaction table spans 12 regions. <code class="font-mono text-violet-700">groupby(\"region\").sum()</code> collapses it to 12 summary rows — one per region — in a single call.',
             "regional_totals"),
            ("fa6-solid:chart-column", "pink",
             "Average order value<br>per product category",
             'Your CFO needs the average order value for each of 30 product categories. <code class="font-mono text-[#CB187D]">groupby(\"category\")[\"amount\"].mean()</code> computes all 30 averages at once.',
             "avg_by_category"),
            ("fa6-solid:sliders", "emerald",
             "Weekly KPI pack<br>with five metrics",
             'The Monday report needs total revenue, order count, average order size, max, and min per region. <code class="font-mono text-emerald-700">.agg()</code> computes all five in one grouped call.',
             "kpi_df"),
        ],
        [
            "Building a regional summary from 200,000 rows in Excel means creating a pivot table — and rebuilding it manually every time the source data refreshes.",
            "Calculating average order value for 30 categories means writing AVERAGEIF for each category — 30 separate formulas that break when a new category appears.",
            "Producing five metrics per region in Excel requires five separate pivot tables or 60 SUMIF/AVERAGEIF formulas across the report sheet.",
        ],
        [
            '<strong class="text-gray-700">groupby().sum()</strong> collapses 200,000 rows to 12 regional summaries in milliseconds — and updates automatically when rerun.',
            '<strong class="text-gray-700">groupby().mean()</strong> calculates the average for every category simultaneously — new categories appear in the output automatically.',
            '<strong class="text-gray-700">.agg()</strong> computes all five metrics in one call — one line replaces five pivot tables.',
        ],
    ),

    f"{MOD01}/lesson08_joining_data_merge.html": (
        "Imagine you work on a customer analytics team. Your orders table has 100,000 rows with customer IDs but no names, and your customer table holds the names. Joining data in pandas lets you combine them in seconds — and helps you find rows that have no match, which is where data quality problems usually hide.",
        "joining data", "data joining",
        [
            ("fa6-solid:arrows-left-right", "violet",
             "Match 100,000 orders<br>to customer records",
             'Your orders table has customer IDs but no names. <code class="font-mono text-violet-700">pd.merge(orders, customers, on=\"customer_id\")</code> joins both tables and adds the customer name to every order row.',
             "enriched_df"),
            ("fa6-solid:scale-balanced", "pink",
             "Find orders with<br>no matching product",
             'Some orders reference a product ID that no longer exists. A <code class="font-mono text-[#CB187D]">pd.merge(how=\"left\")</code> followed by a null check reveals every orphaned order before the report runs.',
             "unmatched_df"),
            ("fa6-solid:key", "emerald",
             "Link transactions<br>on two key columns",
             'Two systems each store a transaction ID and a date. Merging on both with <code class="font-mono text-emerald-700">on=[\"id\",\"date\"]</code> prevents false matches where the same ID appears on different days.',
             "matched_df"),
        ],
        [
            "VLOOKUP across 100,000 rows in Excel is slow, and it silently returns #N/A for unmatched rows — only someone scrolling through the results will notice the gaps.",
            "Spotting orders with no matching product in Excel means writing IFERROR(VLOOKUP) formulas and manually filtering for errors — easy to overlook in a large file.",
            "Joining on a single column when you need two means false matches — the same transaction ID appearing on two different dates returns the wrong row silently.",
        ],
        [
            '<strong class="text-gray-700">pd.merge()</strong> joins 100,000 rows to the customer table in under a second — no VLOOKUP, no #N/A errors, no scrolling.',
            '<strong class="text-gray-700">pd.merge(how=\"left\")</strong> exposes every unmatched order as a NaN row — data quality issues are visible before the report is sent.',
            '<strong class="text-gray-700">pd.merge(on=[\"id\",\"date\"])</strong> requires both keys to match — no false positives, no silent wrong data.',
        ],
    ),

    f"{MOD01}/lesson09_handling_missing_data.html": (
        "Imagine you work on a customer data team. Your CRM export has 80,000 records but many email addresses, postcodes, and income figures are blank. Before any analysis runs, you need to know where the gaps are, decide what to do with them, and act — so that missing values don't silently corrupt your results.",
        "missing data", "missing data handling",
        [
            ("fa6-solid:circle-question", "violet",
             "80,000 customer records<br>with unknown gaps",
             'Your CRM export has 80,000 rows but unknown numbers of missing emails and postcodes. <code class="font-mono text-violet-700">isnull().sum()</code> counts the gaps in every column in one call — no scrolling, no manual counting.',
             "null_counts"),
            ("fa6-solid:minus", "pink",
             "Remove incomplete<br>survey responses",
             'Respondents who skipped age or income cannot be used in demographic analysis. <code class="font-mono text-[#CB187D]">dropna(subset=[\"age\",\"income\"])</code> removes only those rows — respondents who answered everything pass through.',
             "clean_responses"),
            ("fa6-solid:fill", "emerald",
             "Fill missing region<br>before the report runs",
             'A blank region column breaks the regional report. <code class="font-mono text-emerald-700">fillna(df[\"region\"].mode()[0])</code> replaces every gap with the most common region — the report runs without errors.',
             "filled_df"),
        ],
        [
            "Counting blank cells across 80,000 rows and 20 columns in Excel means writing a COUNTBLANK for each column — 20 formulas before you even know the scale of the problem.",
            "Filtering out rows with missing age or income in Excel means setting multiple AutoFilter conditions — and you must remember to do it every time the file is refreshed.",
            "A missing region value causes a blank row in the pivot table — you only notice after the report has been sent to stakeholders.",
        ],
        [
            '<strong class="text-gray-700">isnull().sum()</strong> counts gaps across every column in one line — you see the full picture before touching the data.',
            '<strong class="text-gray-700">dropna(subset=)</strong> removes only incomplete rows and runs automatically every time the script executes — no manual filter needed.',
            '<strong class="text-gray-700">fillna()</strong> fills every gap before the report logic runs — blank region values never reach the output.',
        ],
    ),

    f"{MOD01}/lesson10_exporting_data.html": (
        "Imagine you work on a finance reporting team. At month end you need a plain CSV for the finance system, a four-sheet Excel board pack, and a daily log file that grows without overwriting history. Pandas export functions cover all three patterns in a few lines of script.",
        "exporting data", "data export",
        [
            ("fa6-solid:download", "violet",
             "Month-end summary<br>uploaded to finance system",
             'At month end the finance system expects a plain CSV. <code class="font-mono text-violet-700">to_csv(\"close.csv\", index=False)</code> writes the file in one line — no index column, no manual Save As.',
             "close.csv"),
            ("fa6-solid:file-lines", "pink",
             "Board pack with<br>four summary sheets",
             'The board pack needs revenue, costs, headcount, and variance on separate sheets. <code class="font-mono text-[#CB187D]">ExcelWriter</code> writes each DataFrame to its own named sheet inside a single xlsx file.',
             "board_pack.xlsx"),
            ("fa6-solid:rotate", "emerald",
             "Daily extract appended<br>without overwriting history",
             'Your downstream system reads a growing log file. <code class="font-mono text-emerald-700">to_csv(mode=\"a\", header=False)</code> appends today\'s rows to the existing file every night — history is never lost.',
             "updated log"),
        ],
        [
            "Saving the month-end file from Excel adds a row number index column that the finance system rejects — you have to open the file and delete column A before uploading.",
            "Building a four-sheet board pack in Excel means creating each sheet manually, pasting the data, formatting the headers, and saving — every single month.",
            "Appending to a CSV in Excel means opening the existing file, scrolling to the bottom, pasting the new rows, and saving — easy to overwrite the wrong range by accident.",
        ],
        [
            '<strong class="text-gray-700">to_csv(index=False)</strong> writes the file without the index column — the finance system receives exactly what it expects.',
            '<strong class="text-gray-700">ExcelWriter</strong> populates all four sheets in one script run — no manual sheet creation, no copy-pasting, no formatting by hand.',
            '<strong class="text-gray-700">to_csv(mode="a", header=False)</strong> appends rows safely every night — history is preserved and no manual file editing is needed.',
        ],
    ),

    # ── MOD 02 ────────────────────────────────────────────────────────────────

    f"{MOD02}/lesson01_reading_csv_files.html": (
        "Imagine you work on a logistics operations team. Three carriers each send a daily delivery file — pipe-delimited, with different encodings, and far too many columns for your analysis. The parameters in pd.read_csv() let you handle all of that without touching the source files.",
        "reading CSV files", "CSV reading",
        [
            ("fa6-solid:truck", "violet",
             "Shipment exports<br>from three carriers",
             'Each carrier sends a pipe-delimited file with dozens of columns. <code class="font-mono text-violet-700">pd.read_csv(sep=\"|\", usecols=[...])</code> loads only the fields you need in one call — no pre-processing of the source file required.',
             "shipments_df"),
            ("fa6-solid:language", "pink",
             "International supplier<br>CSV with accented text",
             'Your European supplier\'s file contains French and German characters that cause garbled output with a plain read. <code class="font-mono text-[#CB187D]">pd.read_csv(encoding=\"latin-1\")</code> fixes the import without editing the file.',
             "supplier_df"),
            ("fa6-solid:bolt", "emerald",
             "Test your logic on<br>the first 1,000 rows",
             'The full delivery file is 5 million rows. <code class="font-mono text-emerald-700">pd.read_csv(nrows=1000)</code> loads just enough to build and test your transformation before running it on the full dataset.',
             "sample_df"),
        ],
        [
            "When the carrier switches to a pipe delimiter your import silently creates one wide column — all downstream aggregations are wrong before you know it.",
            "A file with Latin-1 encoding raises an error or introduces garbled characters — you have to open the file in a text editor and manually re-save it with the right encoding.",
            "Testing transformation logic on 5 million rows takes several minutes per iteration — slow feedback that makes development painful and error-prone.",
        ],
        [
            '<strong class="text-gray-700">pd.read_csv(sep=, usecols=)</strong> handles any delimiter and loads only needed columns — no pre-processing of source files.',
            '<strong class="text-gray-700">pd.read_csv(encoding=)</strong> reads the file correctly the first time — no manual re-saving, no UnicodeDecodeError.',
            '<strong class="text-gray-700">pd.read_csv(nrows=)</strong> loads a small sample instantly — you develop and test at full speed without waiting for 5 million rows.',
        ],
    ),

    f"{MOD02}/lesson02_working_with_json_files.html": (
        "Imagine you work on a digital product team. Your product API returns JSON, your checkout system sends nested order objects, and your analytics platform ingests JSON records. Pandas can load, flatten, and re-export all three shapes — so you spend time on analysis, not on parsing.",
        "JSON files", "JSON handling",
        [
            ("fa6-solid:globe", "violet",
             "API response with<br>5,000 product records",
             'Your product catalogue API returns a JSON array of 5,000 records. <code class="font-mono text-violet-700">pd.read_json()</code> converts the whole array into a flat DataFrame with no manual parsing.',
             "products_df"),
            ("fa6-solid:diagram-project", "pink",
             "Nested order objects<br>from the checkout API",
             'Each order object contains a nested shipping sub-object with address fields. <code class="font-mono text-[#CB187D]">json_normalize()</code> unpacks them so shipping_city and shipping_postcode become their own columns.',
             "flat_orders_df"),
            ("fa6-solid:upload", "emerald",
             "Send processed data<br>back to the API",
             'Your analytics service reads JSON over HTTP. <code class="font-mono text-emerald-700">to_json(orient=\"records\")</code> serialises the processed DataFrame into the exact format the API expects — one call, no manual serialisation.',
             "records JSON"),
        ],
        [
            "Turning a 5,000-record JSON array into a table manually means writing a loop to extract every field from every object — slow to write and fragile when the API adds a new field.",
            "Nested JSON objects require multiple levels of manual extraction — a shipping address buried three levels deep means three nested key lookups per order.",
            "Rebuilding a DataFrame into a JSON payload manually means iterating every row and constructing dicts — duplicated effort that breaks whenever the DataFrame schema changes.",
        ],
        [
            '<strong class="text-gray-700">pd.read_json()</strong> converts a flat JSON array to a DataFrame in one call — no loops, no field extracting.',
            '<strong class="text-gray-700">json_normalize()</strong> unpacks nested keys automatically using dotted paths — nested shipping fields become flat columns instantly.',
            '<strong class="text-gray-700">to_json(orient="records")</strong> serialises the DataFrame into the exact API format in one line — no manual row iteration.',
        ],
    ),

    f"{MOD02}/lesson03_connecting_to_databases.html": (
        "Imagine you work on a business intelligence team. You need fresh database data every morning, credentials must stay out of the script, and the connection must close cleanly even if the script crashes. SQLAlchemy and pandas handle all three patterns so your pipeline is reliable and secure.",
        "database connections", "database connections",
        [
            ("fa6-solid:database", "violet",
             "Fresh sales data<br>every morning",
             'Your pipeline needs today\'s sales every morning. <code class="font-mono text-violet-700">create_engine()</code> opens the connection and <code class="font-mono text-violet-700">pd.read_sql_table()</code> loads the sales table straight into a DataFrame.',
             "sales_df"),
            ("fa6-solid:lock", "pink",
             "Credentials kept<br>outside the script",
             'Database passwords stored in a script appear in code reviews and Git history. You load them from environment variables with <code class="font-mono text-[#CB187D]">os.getenv()</code> — the script contains no sensitive data.',
             "secure engine"),
            ("fa6-solid:power-off", "emerald",
             "Connection closes<br>on every script exit",
             'A script that leaves connections open degrades performance for every other user of the database. A <code class="font-mono text-emerald-700">with engine.connect()</code> block closes the connection automatically — even if the script crashes.',
             "auto-closed"),
        ],
        [
            "A script that hard-codes the connection string breaks the moment the database password rotates — someone has to find every script file and update the string manually.",
            "A password written in a Python file gets committed to Git, appears in pull request diffs, and may end up in a shared Slack message — even if you delete it later.",
            "A script that doesn't close its connection leaves idle sessions open on the database server — over time this exhausts the connection pool and blocks other users.",
        ],
        [
            '<strong class="text-gray-700">create_engine()</strong> and <strong class="text-gray-700">pd.read_sql_table()</strong> load fresh data every run — the connection string lives in one place, easy to update.',
            '<strong class="text-gray-700">os.getenv()</strong> reads credentials at runtime — no password ever appears in a file, a code review, or a Git commit.',
            'A <strong class="text-gray-700">with engine.connect()</strong> block closes the connection when the block ends — no idle sessions, no connection pool exhaustion.',
        ],
    ),

    f"{MOD02}/lesson04_running_sql_in_python.html": (
        "Imagine you work on a finance analytics team. Your month-end query is 30 lines of SQL and different stakeholders need it filtered by different years. Running SQL in Python with pd.read_sql() keeps the query in one place, makes it safely parameterised, and puts the result straight into a DataFrame for further processing.",
        "SQL queries in Python", "SQL in Python",
        [
            ("fa6-solid:database", "violet",
             "Month-end query<br>returns 200,000 rows",
             'Your month-end SQL query is 30 lines long. <code class="font-mono text-violet-700">pd.read_sql(query, engine)</code> sends it to the database and returns the full result as a DataFrame — no copy-pasting into Excel.',
             "close_df"),
            ("fa6-solid:shield", "pink",
             "Filter by year<br>for any stakeholder",
             'Different stakeholders need different year cuts of the same report. You pass the year through <code class="font-mono text-[#CB187D]">params=(year,)</code> — the query filters safely without string concatenation.',
             "filtered_df"),
            ("fa6-solid:sitemap", "emerald",
             "Join three tables<br>in one database call",
             'Revenue, cost, and headcount live in separate tables. You write the JOIN in SQL and pass it to <code class="font-mono text-emerald-700">pd.read_sql()</code> — the database does the heavy lifting and returns one combined DataFrame.',
             "combined_df"),
        ],
        [
            "Running the month-end query in a SQL client and pasting results into Excel takes 20 minutes — repeat it for each stakeholder's cut and you've spent most of the morning on manual work.",
            "Adding the year as a string inside the query — 'WHERE year = ' + str(year) — creates an SQL injection vulnerability that a malicious value could exploit.",
            "Running three separate queries and joining the results in pandas means transferring far more data than necessary — the database can join 10x faster than a Python merge across large tables.",
        ],
        [
            '<strong class="text-gray-700">pd.read_sql()</strong> returns the query result as a DataFrame immediately — no client tool, no copy-paste, no Excel.',
            '<strong class="text-gray-700">params=</strong> passes values safely — the year is escaped by the driver before it reaches the database, eliminating injection risk.',
            '<strong class="text-gray-700">pd.read_sql()</strong> with a JOIN query lets the database combine tables efficiently — one network round trip, one DataFrame.',
        ],
    ),

    f"{MOD02}/lesson05_writing_data_back_to_a_database.html": (
        "Imagine you work on a data engineering team. Your ETL script downloads raw files, cleans them, and needs to push the results back into a database table. Pandas to_sql() handles the write — whether you're replacing stale data, appending new rows, or creating a table from scratch.",
        "writing data to databases", "writing to databases",
        [
            ("fa6-solid:upload", "violet",
             "Load cleaned data<br>into the reporting table",
             'Your ETL script produces a clean DataFrame after processing. <code class="font-mono text-violet-700">to_sql(\"results\", engine, index=False)</code> inserts every row into the reporting table in one call.',
             "rows written"),
            ("fa6-solid:rotate", "pink",
             "Replace stale data<br>on each daily run",
             'The report table holds yesterday\'s figures. <code class="font-mono text-[#CB187D]">to_sql(if_exists=\"replace\")</code> drops the old rows and loads fresh data every morning — no manual TRUNCATE.',
             "refreshed table"),
            ("fa6-solid:plus", "emerald",
             "Append new transactions<br>without losing history",
             'Your audit log must grow each day without losing past entries. <code class="font-mono text-emerald-700">to_sql(if_exists=\"append\")</code> adds today\'s rows to the bottom of the existing table every night.',
             "appended rows"),
        ],
        [
            "Inserting a 50,000-row DataFrame row by row with individual INSERT statements takes minutes and hammers the database with thousands of round trips.",
            "Manually running TRUNCATE TABLE before INSERT means two separate steps — if the truncate succeeds but the insert fails, you've deleted the data and loaded nothing.",
            "Appending rows in a SQL client means exporting the DataFrame to CSV, opening the SQL client, loading the file, and running an INSERT — four manual steps that can fail at any point.",
        ],
        [
            '<strong class="text-gray-700">to_sql()</strong> bulk-inserts the entire DataFrame in one operation — far faster than row-by-row inserts and no manual SQL needed.',
            '<strong class="text-gray-700">to_sql(if_exists="replace")</strong> handles truncate and reload atomically — if the load fails, the existing data is still intact.',
            '<strong class="text-gray-700">to_sql(if_exists="append")</strong> adds rows to the existing table in one call — no manual export, no SQL client, no multi-step process.',
        ],
    ),

    f"{MOD02}/lesson06_managing_credentials_env.html": (
        "Imagine you work on a data engineering team. Your scripts connect to production databases, and those passwords must never appear in a file, a log, or a Git repository. A .env file stores credentials outside the code so you can share the script freely — without sharing the secrets.",
        "credentials management", ".env files",
        [
            ("fa6-solid:lock", "violet",
             "Production password<br>stays out of the code",
             'Your script connects to the production database. Storing the password in a .env file and reading it with <code class="font-mono text-violet-700">os.getenv(\"DB_PASSWORD\")</code> means it never appears in the script file itself.',
             "DB_PASSWORD"),
            ("fa6-solid:code-branch", "pink",
             "Share the script<br>without sharing secrets",
             'A new team member clones the repository. The .env file is listed in <code class="font-mono text-[#CB187D]">.gitignore</code> — they receive no passwords. They create their own .env with their own credentials.',
             "no secrets leaked"),
            ("fa6-solid:gear", "emerald",
             "Switch between dev<br>and production databases",
             'You run the same script against development and production. Changing one line in the .env file swaps the target — <code class="font-mono text-emerald-700">os.getenv(\"DB_CONN\")</code> picks up the new value at runtime without editing the script.',
             "env-specific engine"),
        ],
        [
            "A password written in the script appears in every code review, every shared Slack snippet, and every Git commit — you can delete it later, but it stays in the commit history forever.",
            "Sharing a script that contains a production password forces you to manually redact the password before sending — easy to forget, and the recipient may share it further.",
            "Switching between development and production databases means finding and editing the connection string in the script every time — one mistake and production data is modified by a test script.",
        ],
        [
            '<strong class="text-gray-700">os.getenv()</strong> reads the password at runtime — it never appears in the script file, in a code review, or in Git.',
            '<strong class="text-gray-700">.gitignore</strong> keeps the .env file off the repository — share the script freely, and each recipient supplies their own credentials.',
            '<strong class="text-gray-700">os.getenv("DB_CONN")</strong> reads whichever connection string is in the current .env — swap the file to swap the database, no script edits.',
        ],
    ),

    # ── MOD 03 ────────────────────────────────────────────────────────────────

    f"{MOD03}/lesson01_why_analysts_use_python.html": (
        "Imagine you're a data analyst at a mid-size company. Every week you spend hours copying SQL results into Excel, refreshing pivot tables, and emailing reports. Python doesn't replace SQL or Excel — it connects them and automates the steps in between, so you spend time on insight, not on plumbing.",
        "Python for analysts", "Python",
        [
            ("fa6-solid:clock", "violet",
             "Monthly report that<br>takes 4 hours manually",
             'Every month you spend 4 hours querying, formatting, and emailing one report. The same pipeline written with <code class="font-mono text-violet-700">pandas</code> and <code class="font-mono text-violet-700">openpyxl</code> runs in under 2 minutes, automatically.',
             "report.xlsx"),
            ("fa6-solid:database", "pink",
             "Data from 3 different<br>database systems",
             'Your analysis spans an Oracle, SQL Server, and Postgres database. One Python script connects to all three with <code class="font-mono text-[#CB187D]">pd.read_sql()</code>, queries each, and combines the results — no switching tools.',
             "combined_df"),
            ("fa6-solid:bolt", "emerald",
             "1.2 million rows<br>that crash Excel",
             'Your transaction file has 1.2 million rows — Excel refuses to open it. <code class="font-mono text-emerald-700">pd.read_csv()</code> loads the full file in seconds and your analysis runs without hitting a row limit.',
             "full_df"),
        ],
        [
            "The 4-hour monthly report runs every time someone manually clicks through the same SQL queries, paste steps, and Excel formatting — and breaks if one step is interrupted.",
            "Querying three different databases in a single analysis means logging into three separate clients, exporting three files, and manually merging them in Excel.",
            "A file with 1.2 million rows simply cannot be opened in Excel — the analysis cannot happen until someone splits the file by hand into smaller chunks.",
        ],
        [
            '<strong class="text-gray-700">pandas</strong> and <strong class="text-gray-700">openpyxl</strong> script the entire 4-hour workflow — one command runs in under 2 minutes with no human steps.',
            '<strong class="text-gray-700">pd.read_sql()</strong> connects to any database — one script queries Oracle, SQL Server, and Postgres in sequence and combines all three results.',
            '<strong class="text-gray-700">pd.read_csv()</strong> loads 1.2 million rows in seconds — no row limit, no file splitting, no workarounds.',
        ],
    ),

    f"{MOD03}/lesson02_replacing_excel_workflows_with_python.html": (
        "Imagine you're a reporting analyst. Every week you run VLOOKUP across two large tables, rebuild the same pivot table from a fresh extract, and populate a six-sheet weekly pack by hand. Python replaces all three workflows with scripts that run in seconds — and don't break when the data changes.",
        "Python replacing Excel workflows", "Python",
        [
            ("fa6-solid:magnifying-glass", "violet",
             "VLOOKUP across two<br>100,000-row tables",
             'You VLOOKUP customer names from a 100,000-row master list into a 100,000-row orders file. In Excel this takes minutes and crashes. <code class="font-mono text-violet-700">pd.merge()</code> does the same join in under a second.',
             "enriched_df"),
            ("fa6-solid:table-cells-large", "pink",
             "Pivot table rebuilt<br>every Monday morning",
             'You delete and recreate the same pivot table every Monday from a fresh data extract. A <code class="font-mono text-[#CB187D]">groupby().agg()</code> script reads the file and writes the pivot to Excel automatically — no clicking.',
             "pivot_df"),
            ("fa6-solid:layer-group", "emerald",
             "Weekly pack with<br>six summary sheets",
             'Your weekly pack has six sheets: revenue, refunds, new customers, churn, top products, and targets. <code class="font-mono text-emerald-700">ExcelWriter</code> populates all six in one script run — each from its own DataFrame.',
             "weekly_pack.xlsx"),
        ],
        [
            "VLOOKUP across two 100,000-row tables in Excel is slow, crashes on some machines, and silently returns #N/A for unmatched rows without warning you.",
            "Rebuilding the Monday pivot table by hand means deleting the old one, refreshing the source, and recreating it — 15 minutes of clicking before analysis can start.",
            "Populating six summary sheets in Excel means copying data into each tab manually — one mistake on the wrong sheet and the wrong stakeholder sees the wrong figures.",
        ],
        [
            '<strong class="text-gray-700">pd.merge()</strong> joins 100,000-row tables in under a second — no crashes, no #N/A, no scrolling through errors.',
            '<strong class="text-gray-700">groupby().agg()</strong> runs the full pivot computation on a fresh file automatically — no manual delete, no rebuild, no Monday clicking.',
            '<strong class="text-gray-700">ExcelWriter</strong> writes all six sheets in one run — the right data lands on the right sheet every time.',
        ],
    ),

    f"{MOD03}/lesson03_using_python_with_sql_queries.html": (
        "Imagine you're a BI analyst. Your data warehouse holds half a million rows of sales data, and stakeholders want the same report filtered by different months, enriched with calculations SQL can't do natively. Running SQL through Python lets you use the best of both tools in one script.",
        "Python with SQL queries", "Python + SQL",
        [
            ("fa6-solid:database", "violet",
             "500,000 rows from<br>the data warehouse",
             'You pull half a million rows from the warehouse with SQL, then apply rolling averages and custom string logic that SQL can\'t handle. <code class="font-mono text-violet-700">pd.read_sql()</code> bridges both — SQL filters at source, pandas enriches the result.',
             "enriched_df"),
            ("fa6-solid:shield", "pink",
             "Same query for<br>any month requested",
             'Every stakeholder wants the same report for a different month. You pass the month safely through <code class="font-mono text-[#CB187D]">params=</code> — the query filters correctly without rewriting or concatenating the SQL string.',
             "monthly_df"),
            ("fa6-solid:folder", "emerald",
             "Library of named<br>SQL query strings",
             'You store each query in a named variable at the top of the script. Any team member can open the file, update one variable, and rerun the correct query — <code class="font-mono text-emerald-700">clean, reusable code</code> that reads like documentation.',
             "reusable queries"),
        ],
        [
            "Running queries in a SQL client and pasting results into Python or Excel manually means a multi-step handoff — and any change to the query means repeating every step.",
            "Building a parameterised query by concatenating strings — 'WHERE month = ' + str(month) — creates an SQL injection risk and breaks on values like \"March '25\".",
            "SQL queries scattered as inline strings inside Python logic are hard to read, hard to test, and invisible to any team member who only knows SQL.",
        ],
        [
            '<strong class="text-gray-700">pd.read_sql()</strong> connects SQL filtering to pandas enrichment in one call — no manual handoff, no copy-pasting.',
            '<strong class="text-gray-700">params=</strong> passes filter values safely — the month is escaped automatically, eliminating injection risk and quoting edge cases.',
            'Named query variables act as <strong class="text-gray-700">self-documenting code</strong> — any team member reads the query name and knows exactly what it does.',
        ],
    ),

    f"{MOD03}/lesson04_automating_repetitive_data_tasks.html": (
        "Imagine you're a reporting analyst who processes 20 regional CSV files every Monday morning. The same steps repeat every week — load, transform, export. Python automation does all 20 files in 10 seconds, schedules the run before you arrive, and logs every outcome so you can prove it ran.",
        "Python automation", "automation",
        [
            ("fa6-solid:folder", "violet",
             "20 regional files<br>processed every Monday",
             'Every Monday you receive 20 CSV files, one per region. A <code class="font-mono text-violet-700">for file in Path(...).glob(\"*.csv\")</code> loop reads, transforms, and exports each one automatically — 2 hours of work in 10 seconds.',
             "20 processed files"),
            ("fa6-solid:clock", "pink",
             "Report delivered before<br>the team arrives",
             'A Task Scheduler entry runs your Python script at 6 AM. The report is waiting in everyone\'s inbox when they arrive — <code class="font-mono text-[#CB187D]">Task Scheduler / cron</code> triggers the run without any action from you.',
             "scheduled delivery"),
            ("fa6-solid:list", "emerald",
             "Audit trail for<br>every automated run",
             'Your manager asks whether last Tuesday\'s report ran. Your <code class="font-mono text-emerald-700">log file</code> shows a timestamped entry confirming it completed with 20 files processed and 0 errors — no guessing.',
             "audit trail"),
        ],
        [
            "Processing 20 files manually every Monday takes 2 hours — open, transform, export, repeat — and a single interruption means starting from where you left off.",
            "A report that only runs when you manually trigger it is late whenever you're in a meeting, travelling, or dealing with something more urgent.",
            "Without a log, proving that last Tuesday's automated run completed means checking email receipts, file modification dates, and your own memory.",
        ],
        [
            'A <strong class="text-gray-700">for loop over Path().glob()</strong> processes all 20 files automatically — 2 hours of Monday work runs in 10 seconds.',
            '<strong class="text-gray-700">Task Scheduler</strong> or <strong class="text-gray-700">cron</strong> triggers the script at a fixed time — the report runs whether you are at your desk or not.',
            'A <strong class="text-gray-700">log file</strong> records each run with a timestamp and file count — you can prove any run completed without checking email or memory.',
        ],
    ),

    f"{MOD03}/lesson05_building_a_simple_reporting_script.html": (
        "Imagine you work on a sales operations team. Every month you produce an Excel report with formatted revenue figures, a multi-sheet layout, and a KPI summary on the cover. A well-structured Python reporting script produces the same output automatically — readable by your team and reproducible every run.",
        "reporting scripts", "reporting scripts",
        [
            ("fa6-solid:sitemap", "violet",
             "Three-step script<br>load, calculate, export",
             'Your report has three clear steps. Splitting them into named functions — <code class="font-mono text-violet-700">load()</code>, <code class="font-mono text-violet-700">calculate()</code>, <code class="font-mono text-violet-700">export()</code> — makes the logic visible and easy for any team member to maintain.',
             "report.xlsx"),
            ("fa6-solid:pen", "pink",
             "Board-ready numbers<br>in the right format",
             'Executives want revenue rounded to the nearest pound and dates as "April 2025". You apply <code class="font-mono text-[#CB187D]">round()</code> and <code class="font-mono text-[#CB187D]">strftime()</code> before writing — the xlsx needs no manual formatting after the script runs.',
             "formatted_df"),
            ("fa6-solid:chart-bar", "emerald",
             "KPI summary on<br>the cover sheet",
             'Your report opens with total revenue, average order size, and the single largest transaction. <code class="font-mono text-emerald-700">describe()</code> and <code class="font-mono text-emerald-700">sum()</code> feed those numbers directly into the cover sheet DataFrame.',
             "kpi_summary"),
        ],
        [
            "A script with all logic inline in one long block is hard to read, impossible to test in parts, and breaks in ways that are difficult to diagnose — you have to read 200 lines to find one mistake.",
            "Formatting numbers and dates manually after the report is written means opening the Excel file every month, reformatting two columns, and saving before sending.",
            "Calculating KPI figures manually — total revenue, average order, max transaction — means writing three separate formulas or running three separate queries before typing the numbers into the cover sheet.",
        ],
        [
            'Named functions — <strong class="text-gray-700">load()</strong>, <strong class="text-gray-700">calculate()</strong>, <strong class="text-gray-700">export()</strong> — make the script readable and testable independently.',
            '<strong class="text-gray-700">round()</strong> and <strong class="text-gray-700">strftime()</strong> format every value before writing — the xlsx is ready to send without any manual touch-up.',
            '<strong class="text-gray-700">describe()</strong> and <strong class="text-gray-700">sum()</strong> compute all KPI figures in one call — the cover sheet populates automatically every run.',
        ],
    ),

    f"{MOD03}/lesson06_automating_reports_end_to_end.html": (
        "Imagine you run a data analytics team. Your weekly report involves extracting data, cleaning it, building a summary, and emailing it to 15 people — every Friday. An end-to-end pipeline does all four steps automatically, handles failures gracefully, and delivers the report before anyone asks for it.",
        "end-to-end automation", "automation",
        [
            ("fa6-solid:link", "violet",
             "Pipeline of four<br>connected steps",
             'Your report has four steps: extract, clean, summarise, and email. Each function passes its output to the next — <code class="font-mono text-violet-700">run_pipeline()</code> runs the entire chain with one call.',
             "delivered report"),
            ("fa6-solid:shield", "pink",
             "Script fails at 3 AM<br>nobody notices",
             'A database outage at 3 AM causes the extraction step to fail. <code class="font-mono text-[#CB187D]">try / except</code> catches the error, writes it to the log, and sends you an alert — the team\'s inbox is not flooded with a Python traceback.',
             "error logged"),
            ("fa6-solid:envelope", "emerald",
             "Report in 15 inboxes<br>without opening Outlook",
             'After the xlsx is written, <code class="font-mono text-emerald-700">smtplib.sendmail()</code> attaches it and delivers it to all 15 distribution list recipients — no one has to open Outlook, find the file, and click send.',
             "email sent"),
        ],
        [
            "A four-step manual workflow means four points of failure — someone runs step 1, forgets step 2, and the report that reaches the team is based on last week's data.",
            "A script without error handling crashes with a traceback at 3 AM — you wake to a flood of automated error emails and have to investigate a cold trail hours later.",
            "Emailing the report manually means opening Outlook, finding the file, attaching it, addressing it to 15 people, and clicking send — every single Friday.",
        ],
        [
            '<strong class="text-gray-700">run_pipeline()</strong> chains all four steps — one call runs extract, clean, summarise, and email with no human involvement.',
            '<strong class="text-gray-700">try / except</strong> catches failures silently, logs the error, and sends a targeted alert — no traceback flood, clear failure record.',
            '<strong class="text-gray-700">smtplib.sendmail()</strong> delivers to all 15 recipients automatically — no Outlook, no attachment hunting, no Friday manual send.',
        ],
    ),

    # ── MOD 04 ────────────────────────────────────────────────────────────────

    f"{MOD04}/lesson02_memory_optimization.html": (
        "Imagine you work on a data engineering team. Your 30-million-row production export loads into 4 GB of RAM and the pipeline crashes before it finishes. Memory optimisation in pandas cuts that footprint dramatically — by choosing the smallest type that can hold each column's values.",
        "memory optimisation", "memory optimisation",
        [
            ("fa6-solid:memory", "violet",
             "30-column table<br>uses 4 GB of RAM",
             'A 30-million-row export loads into 4 GB. Passing two numeric columns through <code class="font-mono text-violet-700">pd.to_numeric(downcast=\"integer\")</code> drops them from int64 to int16 — RAM use falls below 1 GB.',
             "reduced_df"),
            ("fa6-solid:tags", "pink",
             "Region column repeated<br>30 million times",
             'The region column contains 12 unique strings repeated 30 million times. Calling <code class="font-mono text-[#CB187D]">astype(\"category\")</code> stores each string once and maps rows to an integer — memory drops from 480 MB to 6 MB.',
             "category_series"),
            ("fa6-solid:magnifying-glass", "emerald",
             "Measure the saving<br>before the next step",
             'Before passing the optimised DataFrame downstream you call <code class="font-mono text-emerald-700">memory_usage(deep=True)</code> to confirm the saving. You only proceed when total memory is inside the pipeline budget.',
             "bytes_per_column"),
        ],
        [
            "Loading a 30-million-row file into a pandas DataFrame with default int64 types uses 4 GB of RAM — the pipeline crashes on a server with less than 5 GB available.",
            "A string column with 12 unique values repeated 30 million times stores 30 million full string objects in memory — with no optimisation the column alone can use hundreds of megabytes.",
            "Passing a DataFrame to the next pipeline step without checking its size risks a MemoryError at a later stage — the optimisation work was wasted and the pipeline still crashes.",
        ],
        [
            '<strong class="text-gray-700">pd.to_numeric(downcast=)</strong> shrinks each column to the smallest fitting type — the same data uses a fraction of the original memory.',
            '<strong class="text-gray-700">astype("category")</strong> stores 30 million strings as integers pointing to 12 unique values — memory drops from hundreds of MB to single digits.',
            '<strong class="text-gray-700">memory_usage(deep=True)</strong> measures the actual footprint after optimisation — you confirm the saving before the pipeline continues.',
        ],
    ),

    f"{MOD04}/lesson03_chunk_processing.html": (
        "Imagine you work on a data team at a financial services firm. Your server log file is 8 GB — loading it in one go crashes Python with MemoryError. Chunk processing reads the file in fixed-size batches so the pipeline completes without ever holding more than a fraction of the data in memory.",
        "chunk processing", "chunk processing",
        [
            ("fa6-solid:triangle-exclamation", "violet",
             "8 GB log file<br>that crashes Python",
             'Your server log is 8 GB. Loading it at once raises MemoryError. <code class="font-mono text-violet-700">pd.read_csv(chunksize=500_000)</code> returns an iterator that reads 500,000 rows at a time — the process never needs more than 300 MB.',
             "chunked iterator"),
            ("fa6-solid:rotate", "pink",
             "Running total across<br>200 million rows",
             'You need total transaction value across 200 million rows. A <code class="font-mono text-[#CB187D]">for chunk in reader</code> loop accumulates a running sum from each batch — same result as loading everything, using a fraction of the RAM.',
             "running total"),
            ("fa6-solid:object-group", "emerald",
             "Combine flagged rows<br>into one output file",
             'Each chunk produces a small subset of flagged transactions. <code class="font-mono text-emerald-700">pd.concat(results)</code> at the end merges all subsets into one complete output file — without ever holding all 200 million rows at once.',
             "flagged_df"),
        ],
        [
            "Loading an 8 GB file triggers MemoryError before a single row is processed — the script crashes, the server is locked, and no results are produced.",
            "Calculating a running total over 200 million rows is impossible in a single DataFrame load on most analyst laptops — the task simply cannot run.",
            "Collecting filtered rows from each batch manually — appending to a list inside a loop, then rebuilding a CSV manually — is error-prone and misses pandas' optimised concat pathway.",
        ],
        [
            '<strong class="text-gray-700">pd.read_csv(chunksize=)</strong> reads the 8 GB file in 300 MB batches — MemoryError never happens, the script completes.',
            'A <strong class="text-gray-700">for chunk in reader</strong> loop accumulates results incrementally — 200 million rows are processed with the memory of a single chunk.',
            '<strong class="text-gray-700">pd.concat()</strong> merges all partial results at the end — one clean output file, assembled efficiently from all batches.',
        ],
    ),

    f"{MOD04}/lesson04_processing_millions_of_rows.html": (
        "Imagine you work on a data team processing e-commerce transactions. Your Black Friday script must apply a 20% discount to 5 million prices, and your pipeline budget is 3 minutes. A for loop takes 8 minutes. A vectorised expression takes under 100 milliseconds. The difference is whether the sale goes live on time.",
        "vectorised processing", "vectorised processing",
        [
            ("fa6-solid:bolt", "violet",
             "5 million prices<br>discounted for Black Friday",
             'Your sale script must apply 20% off to 5 million product prices. The vectorised expression <code class="font-mono text-violet-700">df[\"price\"] * 0.8</code> finishes in under 100 ms — a row-by-row for loop takes 8 minutes.',
             "discounted_prices"),
            ("fa6-solid:stopwatch", "pink",
             "14-minute script<br>with a 3-minute budget",
             'Your processing script runs for 14 minutes but costs 3 minutes in the pipeline budget. <code class="font-mono text-[#CB187D]">cProfile.run()</code> ranks every function call by time — it reveals that 11 minutes is in one slow apply() you can replace.',
             "time ranking"),
            ("fa6-solid:gauge-high", "emerald",
             "Verify the fix before<br>it reaches production",
             'After replacing the slow loop with a vectorised expression you time both on the real dataset. <code class="font-mono text-emerald-700">time.time()</code> measurements confirm the fix before it is deployed — no guessing, no surprises in production.',
             "elapsed seconds"),
        ],
        [
            "A for loop that processes 5 million rows one at a time takes 8 minutes in Python — if the sale goes live at midnight, you're still waiting at 00:08 for the prices to update.",
            "A 14-minute script that you haven't profiled could be spending 90% of its time in one fixable step — but without profiling you don't know which step to fix.",
            "Replacing a slow loop with a vectorised expression and deploying without measuring first means you don't know whether the fix actually improved things until the next production run.",
        ],
        [
            '<strong class="text-gray-700">df[\"price\"] * 0.8</strong> applies the discount to all 5 million rows in compiled NumPy — from 8 minutes to under 100 ms.',
            '<strong class="text-gray-700">cProfile.run()</strong> identifies the bottleneck function in one run — you fix the right line, not a random guess.',
            '<strong class="text-gray-700">time.time()</strong> before and after measures the real improvement — the fix is confirmed before it reaches production.',
        ],
    ),

    f"{MOD04}/lesson05_columnar_storage.html": (
        "Imagine you work on a data platform team. Your fact table has 80 columns and analysts consistently query only 3 of them — date, region, and revenue. A CSV reads all 80 columns every time. A columnar format physically skips the other 77 on every read — the query finishes in a fraction of the time.",
        "columnar storage", "columnar storage",
        [
            ("fa6-solid:bars", "violet",
             "Analysts query 3 of<br>80 columns every time",
             'Your fact table has 80 columns. Analysts need only date, region, and revenue. <code class="font-mono text-violet-700">pd.read_parquet(columns=[\"date\",\"region\",\"revenue\"])</code> physically skips the other 77 — CSV reads all 80 every single time.',
             "3-column df"),
            ("fa6-solid:scale-balanced", "pink",
             "2 GB CSV compressed<br>to 410 MB Parquet",
             'Your transaction CSV is 2 GB. <code class="font-mono text-[#CB187D]">df.to_parquet()</code> writes the same data as a 410 MB Parquet file — smaller to store, faster to read, and every column type is preserved.',
             "410 MB file"),
            ("fa6-solid:compress", "emerald",
             "Column types preserved<br>across pipeline restarts",
             'When you reload the Parquet file tomorrow, every date is still a datetime and every integer is still an int. <code class="font-mono text-emerald-700">pd.read_parquet()</code> restores all types from the file\'s metadata — no dtype= parameters needed.',
             "typed_df"),
        ],
        [
            "A CSV that holds 80 columns reads all 80 on every load — even a query that needs only 3 columns pays the cost of reading and parsing the other 77.",
            "A 2 GB CSV takes longer to read, costs more to store, and requires re-specifying dtype= parameters every time it is loaded — because CSV stores no type information.",
            "A DataFrame saved as CSV and reloaded tomorrow has all date columns parsed as strings — you add dtype= and parse_dates= parameters every time and still sometimes get it wrong.",
        ],
        [
            '<strong class="text-gray-700">pd.read_parquet(columns=)</strong> reads only the 3 columns requested — the other 77 are physically skipped on disk.',
            '<strong class="text-gray-700">df.to_parquet()</strong> writes 410 MB instead of 2 GB — smaller, faster to read, and no type information is lost.',
            '<strong class="text-gray-700">pd.read_parquet()</strong> restores every column type from the file metadata — no dtype= parameters, no re-parsing, no surprises.',
        ],
    ),

    f"{MOD04}/lesson06_parquet_files.html": (
        "Imagine you work as a data platform engineer. Your ETL writes 2 million transaction rows every night, your BI dashboard reads only 2 columns of a 50-column fact table, and different consumers need different file formats. Parquet handles the internal pipeline efficiently — CSV handles external sharing where anyone needs to open the file.",
        "Parquet files", "Parquet",
        [
            ("fa6-solid:file-lines", "violet",
             "Nightly 2-million-row<br>transaction export",
             'Every night your ETL writes 2 million transactions. <code class="font-mono text-violet-700">to_parquet()</code> writes a compressed, typed binary file in under 30 seconds — half the time of an equivalent CSV write.',
             "transactions.parquet"),
            ("fa6-solid:filter", "pink",
             "Dashboard reads 2 of<br>50 fact table columns",
             'Your BI dashboard queries only region and revenue from a 50-column fact table. <code class="font-mono text-[#CB187D]">pd.read_parquet(columns=[\"region\",\"revenue\"])</code> skips the other 48 at the file level — the read is vastly faster than CSV.',
             "2-column df"),
            ("fa6-solid:scale-balanced", "emerald",
             "Right format for<br>each audience",
             'Internal analytics pipelines use Parquet for speed and size. External partner shares use CSV because anyone can open it. You pick the right tool for each audience — <code class="font-mono text-emerald-700">to_parquet()</code> or <code class="font-mono text-emerald-700">to_csv()</code> — with one line.',
             "format decision"),
        ],
        [
            "Writing 2 million rows to CSV every night produces a large plain-text file — slow to write, slow to read, and it loses all column type information that the next step must re-infer.",
            "Reading all 50 columns of a fact table when only 2 are needed wastes IO bandwidth, increases load time, and uses far more memory than the query actually requires.",
            "Using only one file format for every audience means internal pipelines pay the CSV performance penalty, or external partners receive a binary file they cannot open in Excel.",
        ],
        [
            '<strong class="text-gray-700">to_parquet()</strong> writes compressed binary in under 30 seconds — types are preserved, size is halved, and every read is faster.',
            '<strong class="text-gray-700">pd.read_parquet(columns=)</strong> skips 48 columns at the file level — only the 2 you requested arrive in memory.',
            '<strong class="text-gray-700">to_parquet()</strong> for internal speed and <strong class="text-gray-700">to_csv()</strong> for external sharing — one line each, right format for each audience.',
        ],
    ),

    f"{MOD04}/lesson13_performance_profiling.html": (
        "Imagine you work on a data engineering team. Your daily pipeline runs for 45 minutes and the SLA is 5. Without profiling you're guessing which step to fix. With profiling tools you know exactly which function to look at, which line inside it to change, and whether the fix actually worked.",
        "performance profiling", "profiling",
        [
            ("fa6-solid:stopwatch", "violet",
             "45-minute pipeline<br>with a 5-minute SLA",
             'Your pipeline misses its SLA by 40 minutes. <code class="font-mono text-violet-700">cProfile.run()</code> ranks every function by total time — it shows 38 minutes is in one function processing a lookup join. You fix that function and the pipeline drops to 4 minutes.',
             "per-function times"),
            ("fa6-solid:magnifying-glass", "pink",
             "Which line inside<br>the slow function?",
             'cProfile shows total function time but not which line. <code class="font-mono text-[#CB187D]">line_profiler</code> with the <code class="font-mono text-[#CB187D]">@profile</code> decorator times every line individually — you see that a Python for loop on line 47 takes 11 of the 14 minutes.',
             "per-line times"),
            ("fa6-solid:list-check", "emerald",
             "Prove the gain<br>before closing the ticket",
             'Your team requires before-and-after evidence in every optimisation ticket. <code class="font-mono text-emerald-700">time.time()</code> measurements taken before and after the fix give you the seconds elapsed — attached as proof the change is safe to deploy.',
             "before / after seconds"),
        ],
        [
            "Optimising a 45-minute pipeline without profiling means guessing which step is slow — you might spend a day speeding up a step that took 30 seconds while the real bottleneck remains untouched.",
            "Knowing a function takes 14 minutes but not which line means reading through hundreds of lines of logic to find the slow part — profiling that takes minutes, not days.",
            "Fixing a bottleneck and deploying without measuring means you don't know whether the fix helped until the next production run — and you have no evidence to share with the team.",
        ],
        [
            '<strong class="text-gray-700">cProfile.run()</strong> ranks every function by total elapsed time — the bottleneck is visible in seconds, not after days of guesswork.',
            '<strong class="text-gray-700">line_profiler</strong> with <strong class="text-gray-700">@profile</strong> times every line inside a function — the exact slow statement is visible without reading all the code.',
            '<strong class="text-gray-700">time.time()</strong> before and after the fix measures the real improvement — you have the numbers to prove the optimisation worked.',
        ],
    ),
}


# ── Apply ──────────────────────────────────────────────────────────────────────

ok = fail = 0

for rel_path, (intro, subtitle, topic, cards, without_rows, with_rows) in LESSONS.items():
    abs_path = os.path.join(ROOT, rel_path.replace("/", os.sep))
    if not os.path.exists(abs_path):
        print(f"  ❌ FILE NOT FOUND: {rel_path}")
        fail += 1
        continue

    html = open(abs_path, encoding="utf-8").read()
    new_section = build_section(intro, subtitle, topic, cards, without_rows, with_rows)
    new_html, count = PATTERN.subn(new_section, html, count=1)

    if count == 0:
        print(f"  ⚠️  PATTERN NOT FOUND: {rel_path}")
        fail += 1
        continue

    open(abs_path, "w", encoding="utf-8").write(new_html)
    print(f"  ✅ {rel_path}")
    ok += 1

print(f"\n{ok}/{ok+fail} files updated.")
if fail:
    sys.exit(1)
