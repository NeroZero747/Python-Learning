"""Remove bottom nav div and <footer> element from all 5 mod_04 lesson files."""
import pathlib, re

FILES = [
    "pages/track_01_python_foundation/mod_04_python_best_practices/lesson01_creating_your_own_modules.html",
    "pages/track_01_python_foundation/mod_04_python_best_practices/lesson02_project_folder_structure.html",
    "pages/track_01_python_foundation/mod_04_python_best_practices/lesson03_introduction_to_git_simple_workflow.html",
    "pages/track_01_python_foundation/mod_04_python_best_practices/lesson04_git_in_vs_code.html",
    "pages/track_01_python_foundation/mod_04_python_best_practices/lesson05_logging_basics.html",
]

# Pattern 1: bottom nav div — from the opening div to </a></div> immediately before </main>
BOTTOM_NAV_RE = re.compile(
    r'\n\n[ \t]*<div class="flex flex-col sm:flex-row gap-3 mt-6">.*?</a></div>\n',
    re.DOTALL,
)

# Pattern 2: <footer>...</footer> (including surrounding whitespace/newlines)
FOOTER_RE = re.compile(
    r'\n[ \t]*<footer\b.*?</footer>\n',
    re.DOTALL,
)

for path_str in FILES:
    p = pathlib.Path(path_str)
    html = p.read_text(encoding="utf-8")
    original_len = len(html)

    # Remove bottom nav
    html, n1 = BOTTOM_NAV_RE.subn("", html)
    # Remove footer
    html, n2 = FOOTER_RE.subn("", html)

    if n1 == 0 and n2 == 0:
        print(f"⚠️  {p.name}: nothing matched")
    else:
        p.write_text(html, encoding="utf-8")
        print(f"✅  {p.name}: removed {n1} bottom-nav + {n2} footer  ({original_len:,} → {len(html):,} chars)")
