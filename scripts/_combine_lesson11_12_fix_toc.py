"""Patch up TOC sidebars in remaining lessons that had different filename prefixes."""
from pathlib import Path
import re

DIR = Path(r'c:\Users\nightwolf\Projects\Python-Learning\pages\mod_06a_sql_foundation\mod_05_sql_foundations')

NEW_BLOCK = (
    '<a href="lesson11_case_statements.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">\n'
    '  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>\n'
    '  <span class="truncate">7. CASE Statements &amp; NULL Handling</span>\n'
    '</a>\n'
    '<a href="lesson12_query_optimization.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">\n'
    '  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>\n'
    '  <span class="truncate">8. Query Optimization</span>\n'
    '</a>\n'
    '<a href="lesson13_sql_for_analytics_workflows.html" class="flex items-center gap-2 px-3 py-2 rounded-lg border bg-white border-gray-100 text-gray-600 hover:border-gray-200 text-xs font-medium no-underline transition-colors">\n'
    '  <span class="w-2 h-2 rounded-full bg-gray-300 shrink-0"></span>\n'
    '  <span class="truncate">9. SQL for Analytics Workflows</span>\n'
    '</a>'
)

# Tolerant pattern: match the four <a> entries 7/8/9/10 regardless of filename prefix
old_block_re = re.compile(
    r'<a href="lesson\d+_case_statements\.html"[\s\S]*?<span class="truncate">7\. CASE Statements</span>\s*</a>\s*'
    r'<a href="lesson\d+_null_handling\.html"[\s\S]*?<span class="truncate">8\. NULL Handling</span>\s*</a>\s*'
    r'<a href="lesson\d+_query_optimization\.html"[\s\S]*?<span class="truncate">9\. Query Optimization</span>\s*</a>\s*'
    r'<a href="lesson\d+_sql_for_analytics_workflows\.html"[\s\S]*?<span class="truncate">10\. SQL for Analytics Workflows</span>\s*</a>'
)

for f in sorted(DIR.glob('lesson*.html')):
    text = f.read_text(encoding='utf-8')
    new = old_block_re.sub(NEW_BLOCK, text)
    if new != text:
        f.write_text(new, encoding='utf-8')
        print(f"[OK] Updated TOC in {f.name}")

# Re-apply self-active highlighting
ACTIVE_CLASS = 'bg-[#fdf0f7] border-[#CB187D] text-[#CB187D]'
INACTIVE_CLASS = 'bg-white border-gray-100 text-gray-600 hover:border-gray-200'
ACTIVE_DOT = 'bg-[#CB187D]'
INACTIVE_DOT = 'bg-gray-300'

for f in sorted(DIR.glob('lesson*.html')):
    text = f.read_text(encoding='utf-8')
    own = f.name
    pattern = re.compile(
        r'(<a href="' + re.escape(own) + r'" class="flex items-center gap-2 px-3 py-2 rounded-lg border )' +
        re.escape(INACTIVE_CLASS) +
        r'(" [^>]*>\s*<span class="w-2 h-2 rounded-full )' +
        re.escape(INACTIVE_DOT),
    )
    new = pattern.sub(
        r'\g<1>' + ACTIVE_CLASS + r'\g<2>' + ACTIVE_DOT,
        text,
    )
    if new != text:
        f.write_text(new, encoding='utf-8')
        print(f"[OK] Marked self-active in {f.name}")

# Sanity check — show any remaining broken references
print("\nRemaining references to old filenames (should be empty):")
import subprocess
for needle in ['lesson12_null_handling', 'lesson13_query_optimization', 'lesson14_sql_for_analytics_workflows']:
    for f in sorted(DIR.glob('lesson*.html')):
        text = f.read_text(encoding='utf-8')
        if needle in text:
            print(f"  {f.name}: still references {needle}")
