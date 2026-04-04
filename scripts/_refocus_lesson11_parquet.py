"""
Refocus lesson11 to Parquet-only: remove profiling KC tabs 8-11, update hero title,
trim kcColors, fix module complete banner.
"""
import re

filepath = r"c:\Users\nightwolf\Projects\Python-Learning\pages\mod_03_python_for_data_analysts\lesson11_parquet_and_performance_profiling.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

original_lines = content.count('\n') + 1
changes = []

# ═══ 1. Hero title ═══
old = 'Parquet Files &amp; Performance Profiling'
new = 'Working with Parquet Files'
if old in content:
    content = content.replace(old, new)
    changes.append(f"Hero title: '{old}' -> '{new}'")

# ═══ 2. Hero subtitle — make it Parquet-focused ═══
old_sub = "Understand why columnar storage formats are dramatically faster for analytical queries than row-based CSVs, and learn how to work with them directly in Python."
new_sub = "Learn why columnar storage formats like Parquet are dramatically faster for analytical queries than row-based CSVs, and start using them in your Python workflows."
if old_sub in content:
    content = content.replace(old_sub, new_sub)
    changes.append("Hero subtitle: updated")
# If old subtitle isn't found, try a broader match
elif "learn how to work with them directly in Python" in content:
    content = content.replace(
        "learn how to work with them directly in Python",
        "start using them in your Python workflows"
    )
    changes.append("Hero subtitle: partial update")

# ═══ 3. TOC sidebar label ═══
old_toc = '>11. Parquet &amp; Performance Profiling<'
new_toc = '>11. Working with Parquet Files<'
if old_toc in content:
    content = content.replace(old_toc, new_toc)
    changes.append("TOC label: updated")

# ═══ 4. Remove KC tab buttons 8-11 ═══
# These are the 4 buttons for timeit, cProfile, line_profiler, Bottleneck Patterns
for tab_idx in [8, 9, 10, 11]:
    pattern = (
        r'\n?<button onclick="switchKcTab\(' + str(tab_idx) + r'\)"'
        r'[^<]*<[^<]*<[^<]*</span>\s*'
        r'<span class="kc-tab-label[^<]*</span>\s*'
        r'</button>'
    )
    content, count = re.subn(pattern, '', content, flags=re.DOTALL)
    if count:
        changes.append(f"Removed KC button {tab_idx}")

# ═══ 5. Remove KC panels 8-11 ═══
# Panels are: timeit (data-color=pink), cProfile (violet), line_profiler (blue), Bottleneck Patterns (emerald)
# They are the 9th-12th kc-panel divs. We need to remove them by matching after the 8th panel.

# Strategy: find all kc-panel divs and remove the last 4
panel_starts = []
for m in re.finditer(r'<div class="kc-panel kc-panel-anim[^"]*"[^>]*role="tabpanel">', content):
    panel_starts.append(m.start())

if len(panel_starts) >= 12:
    # Find the start of panel 8 (index 8)
    remove_start = panel_starts[8]
    # Find the end of panel 11 — it's the last panel before </div><!-- /panels -->
    end_marker = '</div><!-- /panels -->'
    remove_end = content.find(end_marker, remove_start)
    if remove_end > 0:
        # Get the content between panel 8 start and the panels end marker
        removed_text = content[remove_start:remove_end]
        content = content[:remove_start] + content[remove_end:]
        removed_lines = removed_text.count('\n')
        changes.append(f"Removed KC panels 8-11 ({removed_lines} lines)")

# Also remove trailing blank line for panel 7 end
panel_end_pattern = r'(</div>\n          </div>\n)\n+(\n        </div><!-- /panels -->)'
content = re.sub(panel_end_pattern, r'\1\2', content)

# ═══ 6. Trim kcColors array from 12 entries to 8 ═══
old_colors = """  const kcColors = [
    { num: '#CB187D', numShadow: 'rgba(203,24,125,0.25)', activeBg: '#fdf0f7' },
    { num: '#7c3aed', numShadow: 'rgba(124,58,237,0.25)', activeBg: '#f5f3ff' },
    { num: '#2563eb', numShadow: 'rgba(37,99,235,0.25)',  activeBg: '#eff6ff' },
    { num: '#059669', numShadow: 'rgba(5,150,105,0.25)',  activeBg: '#ecfdf5' },
    { num: '#d97706', numShadow: 'rgba(217,119,6,0.25)',  activeBg: '#fffbeb' },
    { num: '#0891b2', numShadow: 'rgba(8,145,178,0.25)',  activeBg: '#ecfeff' },
    { num: '#c2410c', numShadow: 'rgba(194,65,12,0.25)',  activeBg: '#fff7ed' },
    { num: '#0d9488', numShadow: 'rgba(13,148,136,0.25)', activeBg: '#f0fdfa' },
    { num: '#e11d48', numShadow: 'rgba(225,29,72,0.25)',  activeBg: '#fff1f2' },
    { num: '#4f46e5', numShadow: 'rgba(79,70,229,0.25)',  activeBg: '#eef2ff' },
    { num: '#65a30d', numShadow: 'rgba(101,163,13,0.25)', activeBg: '#f7fee7' },
    { num: '#475569', numShadow: 'rgba(71,85,105,0.25)',  activeBg: '#f8fafc' }
  ];"""

new_colors = """  const kcColors = [
    { num: '#CB187D', numShadow: 'rgba(203,24,125,0.25)', activeBg: '#fdf0f7' },
    { num: '#7c3aed', numShadow: 'rgba(124,58,237,0.25)', activeBg: '#f5f3ff' },
    { num: '#2563eb', numShadow: 'rgba(37,99,235,0.25)',  activeBg: '#eff6ff' },
    { num: '#059669', numShadow: 'rgba(5,150,105,0.25)',  activeBg: '#ecfdf5' },
    { num: '#d97706', numShadow: 'rgba(217,119,6,0.25)',  activeBg: '#fffbeb' },
    { num: '#0891b2', numShadow: 'rgba(8,145,178,0.25)',  activeBg: '#ecfeff' },
    { num: '#c2410c', numShadow: 'rgba(194,65,12,0.25)',  activeBg: '#fff7ed' },
    { num: '#0d9488', numShadow: 'rgba(13,148,136,0.25)', activeBg: '#f0fdfa' }
  ];"""

if old_colors in content:
    content = content.replace(old_colors, new_colors)
    changes.append("kcColors: trimmed 12 -> 8 entries")

# ═══ 7. Fix module complete banner: "all 13 lessons" -> "all 11 lessons" ═══
old_banner = "worked through all 13 lessons"
new_banner = "worked through all 11 lessons"
if old_banner in content:
    content = content.replace(old_banner, new_banner)
    changes.append("Module complete banner: 13 -> 11 lessons")

# ═══ Write ═══
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

final_lines = content.count('\n') + 1

print("=" * 60)
print("Refocused lesson11 to Parquet-only")
print("=" * 60)
print(f"\nLines: {original_lines} -> {final_lines} (removed {original_lines - final_lines})")
print(f"\nChanges applied ({len(changes)}):")
for c in changes:
    print(f"  + {c}")

# Verify KC counts
kc_buttons = len(re.findall(r'switchKcTab\(\d+\).*?<button', content))
kc_panels = len(re.findall(r'class="kc-panel', content))
print(f"\nVerification:")
btn_count = len(re.findall(r'<button onclick="switchKcTab', content))
print(f"  KC tab buttons: {btn_count}")
print(f"  KC panels: {kc_panels}")

# Check no profiling references remain
for term in ['timeit', 'cProfile', 'line_profiler', 'snakeviz', 'Bottleneck Patterns']:
    if term in content:
        # Exclude CSS/comment/variable references
        lines_with = [i+1 for i, l in enumerate(content.split('\n')) if term in l]
        print(f"  WARNING: '{term}' still found at lines: {lines_with}")
