#!/usr/bin/env python3
"""Quick structural verification for rebuilt L07."""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE, "pages", "mod_05_data_application", "lesson07_streamlit_vs_shiny.html")
html = open(path, encoding="utf-8").read()

checks = [
    ("No DOCTYPE",          "<!DOCTYPE" not in html),
    ("No <html> tag",       "<html" not in html),
    ("No <head> tag",       "<head" not in html),
    ("No <body> tag",       "<body" not in html),
    ("Starts with <link",   html.lstrip().startswith("<link")),
    ("Has #hub-root",       'id="hub-root"' in html),
    ("Module Complete!",    "Module Complete!" in html),
    ("Has prev link",       "lesson06_shiny_for_python.html" in html),
    ("Has hub link",        "hub_home_page.html" in html),
    ("Ends with </script>", html.rstrip().endswith("</script>")),
    ("Has trophy icon",     "fa6-solid:trophy" in html),
    ("Has graduation-cap",  "fa6-solid:graduation-cap" in html),
    ("Framework Comparison","Framework Comparison" in html),
    ("Streamlit column",    ">Streamlit<" in html),
    ("Shiny column",        ">Shiny<" in html),
    ("Key Difference col",  ">Key Difference<" in html),
    ("mod-lesson-active",   "mod-lesson-active" in html),
    ("No arrow-right icon", "fa6-solid:arrow-right" not in html),
    ("Has spacer div",      '<div class="flex-1"></div>' in html),
    ("lesson07 active",     "lesson07_streamlit_vs_shiny" in html and "mod-lesson-active" in html),
]

all_pass = True
for label, result in checks:
    status = "PASS" if result else "FAIL"
    if not result:
        all_pass = False
    print(f"  {status}  {label}")

print()
print("All checks passed!" if all_pass else "Some checks FAILED.")
