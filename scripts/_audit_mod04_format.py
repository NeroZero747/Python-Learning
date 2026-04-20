"""
Cross-lesson format audit for mod_04_data_engineering.

Checks every section in every lesson against the canonical template rules
defined in copilot-instructions.md and reports deviations.
"""

import re, os, sys
from collections import defaultdict

LESSON_DIR = os.path.join(os.path.dirname(__file__), "..", "pages", "mod_04_data_engineering")

LESSONS = sorted(f for f in os.listdir(LESSON_DIR) if f.startswith("lesson") and f.endswith(".html"))

SECTION_IDS = [
    "objective", "overview", "key-ideas", "key-concepts", "code-examples",
    "comparison", "mistakes", "practice", "real-world", "recap",
    "knowledge-check", "next-lesson",
]

SECTION_ICONS = {
    "objective": "fa6-solid:bullseye",
    "overview": "fa6-solid:binoculars",
    "key-ideas": "fa6-solid:lightbulb",
    "key-concepts": "fa6-solid:book-open",
    "code-examples": "fa6-solid:code",
    "comparison": "fa6-solid:scale-balanced",
    "mistakes": "fa6-solid:triangle-exclamation",
    "practice": "fa6-solid:pencil",
    "real-world": "fa6-solid:briefcase",
    "recap": "fa6-solid:list-check",
    "knowledge-check": "fa6-solid:brain",
    "next-lesson": "fa6-solid:circle-arrow-right",
}

TAB_SYSTEMS = {
    "code-examples": {"step": "ce-step", "active": "ce-step-active", "panel": "ce-panel", "fn": "switchCeTab"},
    "mistakes":      {"step": "mk-step", "active": "mk-step-active", "panel": "mk-panel", "fn": "switchMkTab"},
    "practice":      {"step": "pe-step", "active": "pe-step-active", "panel": "pe-panel", "fn": "switchPeTab"},
    "knowledge-check": {"step": "qz-step", "active": "qz-step-active", "panel": "qz-panel", "fn": "switchQzTab"},
    "key-concepts":  {"step": "kc-tab", "active": "kc-tab-active", "panel": "kc-panel", "fn": "switchKcTab"},
}

TAB_ICONS = {
    "code-examples": "fa6-solid:code",
    "mistakes": "fa6-solid:bug",
    "practice": "fa6-solid:pencil",
    "knowledge-check": "fa6-solid:circle-question",
}

# ---------------------------------------------------------------------------

def extract_section(content, sec_id):
    """Extract the HTML block for a given section id."""
    pattern = re.compile(
        rf'<section\s+id="{sec_id}"[^>]*>(.*?)</section>',
        re.DOTALL
    )
    m = pattern.search(content)
    return m.group(0) if m else None


def check_section_header(section_html, sec_id, issues):
    """Check section header structure."""
    prefix = f"[{sec_id}] header"

    # Check for section-header pattern: border-l-4 border-l-[#CB187D]
    if 'border-l-4 border-l-[#CB187D]' not in section_html and 'border-l-[#CB187D]' not in section_html:
        # Also accept the section-header class pattern
        if 'section-header' not in section_html:
            issues.append(f"{prefix}: missing pink left border (border-l-4 border-l-[#CB187D])")

    # Check icon
    expected_icon = SECTION_ICONS.get(sec_id, "")
    if expected_icon and expected_icon not in section_html:
        # Find what icon IS used
        header_match = re.search(r'<span class="iconify text-white[^"]*"[^>]*data-icon="([^"]+)"', section_html)
        actual = header_match.group(1) if header_match else "none found"
        issues.append(f"{prefix}: expected icon '{expected_icon}', found '{actual}'")

    # Check for h2 section title
    if '<h2' not in section_html:
        issues.append(f"{prefix}: missing <h2> section title")

    # Check for subtitle
    subtitle_pat = re.compile(r'<p class="[^"]*text-sm text-gray-400[^"]*"')
    if not subtitle_pat.search(section_html):
        # Also accept section-subtitle class
        if 'section-subtitle' not in section_html:
            issues.append(f"{prefix}: missing subtitle paragraph")


def check_tab_system(section_html, sec_id, issues):
    """Check tab pill system for tabbed sections."""
    if sec_id not in TAB_SYSTEMS:
        return
    ts = TAB_SYSTEMS[sec_id]
    prefix = f"[{sec_id}] tabs"

    # Count tab buttons
    tab_count = len(re.findall(rf'class="[^"]*{ts["step"]}[ "]', section_html))
    if tab_count == 0:
        issues.append(f"{prefix}: no tab buttons found (expected class '{ts['step']}')")
        return

    # Count panels
    panel_count = len(re.findall(rf'class="[^"]*{ts["panel"]}[ "]', section_html))
    if tab_count != panel_count:
        issues.append(f"{prefix}: tab/panel mismatch — {tab_count} tabs vs {panel_count} panels")

    # Check active class exists on first tab
    first_tab_pat = re.compile(rf'{ts["fn"]}\(0\)[^>]*class="[^"]*{ts["active"]}')
    alt_pat = re.compile(rf'class="[^"]*{ts["active"]}[^"]*"[^>]*{ts["fn"]}\(0\)')
    if not first_tab_pat.search(section_html) and not alt_pat.search(section_html):
        # Looser check: is the active class present at all?
        if ts["active"] in section_html:
            pass  # active exists somewhere, acceptable
        else:
            issues.append(f"{prefix}: first tab missing '{ts['active']}' class")

    # Check hidden class on non-first panels
    panels = re.findall(rf'class="[^"]*{ts["panel"]}[^"]*"', section_html)
    for i, p in enumerate(panels):
        if i == 0 and 'hidden' in p:
            issues.append(f"{prefix}: first panel should NOT have 'hidden' class")
        if i > 0 and 'hidden' not in p:
            issues.append(f"{prefix}: panel {i} missing 'hidden' class")

    # Check tab icons
    if sec_id in TAB_ICONS:
        expected_icon = TAB_ICONS[sec_id]
        # Find all icons inside tab buttons
        tab_region = section_html.split('role="tablist"')[0] if 'role="tablist"' in section_html else ""
        if 'role="tablist"' in section_html:
            tablist_match = re.search(r'role="tablist".*?</div>', section_html, re.DOTALL)
            if tablist_match:
                tab_region = tablist_match.group(0)
                tab_icons = re.findall(r'data-icon="([^"]+)"', tab_region)
                wrong_icons = [ic for ic in tab_icons if ic != expected_icon]
                if wrong_icons:
                    issues.append(f"{prefix}: wrong tab icons {set(wrong_icons)}, expected all '{expected_icon}'")


def check_code_blocks(section_html, sec_id, issues):
    """Check code block styles match the section requirements."""
    prefix = f"[{sec_id}] code"

    # Sections that should use Style A (dark-chrome)
    style_a_sections = {"code-examples", "practice"}
    # Sections that should use Style B
    style_b_sections = {"key-concepts", "comparison"}
    # Mistakes split panels use Style B-lite

    code_blocks = re.findall(r'<pre[^>]*>.*?</pre>', section_html, re.DOTALL)
    if not code_blocks:
        return  # no code blocks is ok for some sections

    if sec_id in style_a_sections:
        # Should have bg-[#181825] header
        if 'bg-[#181825]' not in section_html:
            issues.append(f"{prefix}: Style A expected — missing bg-[#181825] header bar")
        # Should have copy-btn-light
        if code_blocks and 'copy-btn' not in section_html:
            issues.append(f"{prefix}: Style A — missing copy buttons")
        # Should NOT have traffic-light dots
        if 'rounded-full bg-red' in section_html and 'rounded-full bg-yellow' in section_html:
            issues.append(f"{prefix}: Style A — has traffic-light dots (forbidden)")

    if sec_id in style_b_sections:
        # Should have border-code-sep
        if 'border-code-sep' not in section_html:
            issues.append(f"{prefix}: Style B expected — missing border-code-sep")

    if sec_id == "comparison":
        # Should have flex flex-col flex-1 on code outer divs
        if 'flex flex-col flex-1' not in section_html:
            issues.append(f"{prefix}: comparison code blocks missing 'flex flex-col flex-1'")


def check_mistakes_format(section_html, issues):
    """Check mistakes section canonical format."""
    prefix = "[mistakes]"

    # Card header with gradient
    if 'bg-gradient-to-r from-red-50' not in section_html:
        issues.append(f"{prefix}: missing card header gradient (from-red-50)")

    # Pitfall badge
    pitfall_count = section_html.lower().count('pitfall')
    panel_count = len(re.findall(r'class="[^"]*mk-panel[ "]', section_html))
    if pitfall_count < panel_count and panel_count > 0:
        issues.append(f"{prefix}: only {pitfall_count} 'Pitfall' badges for {panel_count} panels")

    # Arrow divider between wrong/correct
    arrow_count = section_html.count('fa6-solid:arrow-right')
    if arrow_count < panel_count and panel_count > 0:
        issues.append(f"{prefix}: only {arrow_count} arrow dividers for {panel_count} panels")

    # Amber tips
    amber_count = section_html.count('bg-amber-50')
    if amber_count < panel_count and panel_count > 0:
        issues.append(f"{prefix}: only {amber_count} amber tips for {panel_count} panels")

    # Wrong/correct badge format
    if '&#10007;' in section_html or '&#10003;' in section_html:
        issues.append(f"{prefix}: old ✗/✓ HTML entities found — should use icon badges")

    # Card border
    if 'border-gray-100' in section_html:
        # Check if it's on mistake cards specifically
        mk_cards = re.findall(r'mistake-card[^"]*"[^>]*', section_html)
        for mc in mk_cards:
            if 'border-gray-100' in mc:
                issues.append(f"{prefix}: mistake cards use border-gray-100 (should be border-gray-200)")
                break


def check_practice_format(section_html, issues):
    """Check practice section canonical format."""
    prefix = "[practice]"

    # Panel headers with gradient + watermark
    watermarks = re.findall(r'text-\[(?:5|6)rem\].*?leading-none.*?>(\d{2})<', section_html, re.DOTALL)
    panel_count = len(re.findall(r'class="[^"]*pe-panel[ "]', section_html))

    if len(watermarks) < panel_count and panel_count > 0:
        issues.append(f"{prefix}: only {len(watermarks)} watermarks for {panel_count} panels")

    # Task box
    task_count = section_html.count('task-box') if 'task-box' in section_html else 0
    if task_count < panel_count and panel_count > 0:
        issues.append(f"{prefix}: only {task_count} task-box elements for {panel_count} panels")

    # Show Answer accordion with key icon
    key_icons = section_html.count('fa6-solid:key')
    if key_icons < panel_count and panel_count > 0:
        issues.append(f"{prefix}: only {key_icons} key icons for {panel_count} panels (accordion)")

    # Amber tips
    amber_count = section_html.count('bg-amber-tip') + section_html.count('bg-amber-50')
    if amber_count < panel_count and panel_count > 0:
        issues.append(f"{prefix}: only {amber_count} amber tips for {panel_count} panels")

    # Terminal output panes should NOT be in practice (only in code-examples)
    # Actually practice uses Style A without terminal — so no terminal pane
    # But let's not flag this since some might have it legitimately


def check_quiz_format(section_html, issues):
    """Check knowledge-check section canonical format."""
    prefix = "[knowledge-check]"

    # Q watermarks
    q_watermarks = re.findall(r'>Q\d<', section_html)
    panel_count = len(re.findall(r'class="[^"]*qz-panel[ "]', section_html))

    if len(q_watermarks) < panel_count and panel_count > 0:
        issues.append(f"{prefix}: only {len(q_watermarks)} Q-watermarks for {panel_count} panels")

    # checkQuiz function calls
    check_calls = len(re.findall(r'checkQuiz\(', section_html))
    if check_calls == 0 and panel_count > 0:
        issues.append(f"{prefix}: no checkQuiz() calls found")

    # Quiz feedback elements
    feedback_count = section_html.count('quiz-feedback')
    if feedback_count < panel_count and panel_count > 0:
        issues.append(f"{prefix}: only {feedback_count} quiz-feedback elements for {panel_count} panels")


def check_recap_format(section_html, issues):
    """Check recap section format."""
    prefix = "[recap]"

    # Numbered watermarks (01, 02, etc.)
    watermarks = re.findall(r'>0[1-9]<', section_html)
    if len(watermarks) < 4:
        issues.append(f"{prefix}: only {len(watermarks)} numbered watermarks (expected 4)")

    # Completion banner
    if 'Lesson Complete' not in section_html:
        issues.append(f"{prefix}: missing 'Lesson Complete!' banner")

    # Trophy icon
    if 'fa6-solid:trophy' not in section_html:
        issues.append(f"{prefix}: missing trophy icon in completion banner")


def check_objective_format(section_html, issues):
    """Check objective section format."""
    prefix = "[objective]"

    # obj-card elements
    obj_cards = section_html.count('obj-card')
    if obj_cards < 4:
        issues.append(f"{prefix}: only {obj_cards} obj-card elements (expected 4)")

    # Amber tip
    if 'bg-amber-tip' not in section_html:
        issues.append(f"{prefix}: missing amber tip box")


def check_overview_format(section_html, issues):
    """Check overview section format."""
    prefix = "[overview]"

    # Hook quote card with gradient
    if 'fa6-solid:quote-left' not in section_html:
        issues.append(f"{prefix}: missing hook quote icon (fa6-solid:quote-left)")

    # Analogy pattern — "Think of"
    if 'Think of' not in section_html and 'think of' not in section_html:
        issues.append(f"{prefix}: missing 'Think of...' analogy paragraph")

    # Card grid
    if 'grid grid-cols-1 sm:grid-cols-2' not in section_html:
        issues.append(f"{prefix}: missing 2-column analogy card grid")

    # Closing amber tip
    if 'bg-amber-tip' not in section_html:
        issues.append(f"{prefix}: missing closing amber tip box")


def check_key_ideas_format(section_html, issues):
    """Check key-ideas section format."""
    prefix = "[key-ideas]"

    # Color gradient cards
    gradient_bars = len(re.findall(r'class="h-1 bg-gradient-to-r', section_html))
    if gradient_bars < 2:
        issues.append(f"{prefix}: only {gradient_bars} gradient top bars (expected 3+)")

    # Keyword pills
    if 'rounded-full text-[11px] font-semibold' not in section_html:
        issues.append(f"{prefix}: missing keyword pills")


def check_next_lesson_format(section_html, issues):
    """Check next-lesson section format."""
    prefix = "[next-lesson]"

    # Lesson badge
    if 'Module' not in section_html and 'module' not in section_html:
        issues.append(f"{prefix}: missing Module label")

    # 3-card preview grid
    if 'sm:grid-cols-3' not in section_html:
        issues.append(f"{prefix}: missing 3-column preview grid")


def check_bottom_nav(content, issues):
    """Check bottom navigation bar."""
    prefix = "[bottom-nav]"

    if 'lesson-nav-link' not in content:
        issues.append(f"{prefix}: missing bottom navigation (lesson-nav-link)")
        return

    # All Lessons link
    if 'All Lessons' not in content:
        issues.append(f"{prefix}: missing 'All Lessons' hub link")

    # Hub path
    if 'hub_home_page.html' not in content:
        issues.append(f"{prefix}: missing hub_home_page.html link")


def check_hero(content, issues):
    """Check hero banner."""
    prefix = "[hero]"

    if 'hero-container' not in content and 'hero-dots' not in content:
        issues.append(f"{prefix}: missing hero banner")
        return

    # Hero pills
    if 'hero-pill' not in content:
        issues.append(f"{prefix}: missing hero pills")

    # Stat cards or hero stats
    if 'stat-card' not in content and 'hero-pill' not in content:
        issues.append(f"{prefix}: missing stat cards / pills")


def check_toc_sidebar(content, issues):
    """Check TOC sidebar."""
    prefix = "[toc]"

    if 'lesson-toc-sidebar' not in content:
        issues.append(f"{prefix}: missing TOC sidebar (lesson-toc-sidebar)")
        return

    if 'toc-link' not in content:
        issues.append(f"{prefix}: missing toc-link elements")


def check_scroll_progress(content, issues):
    """Check scroll progress bar."""
    if 'scroll-progress' not in content:
        issues.append("[scroll-progress]: missing scroll progress bar")


def check_back_to_top(content, issues):
    """Check back-to-top button."""
    if 'back-to-top' not in content:
        issues.append("[back-to-top]: missing back-to-top button")


def check_cdns(content, issues):
    """Check CDN links."""
    prefix = "[cdn]"
    required = [
        ("Google Fonts", "fonts.googleapis.com"),
        ("Tailwind", "cdn.tailwindcss.com"),
        ("Iconify", "code.iconify.design"),
        ("Prism CSS", "prism-tomorrow.min.css"),
        ("Prism JS", "prism.min.js"),
        ("Prism Python", "prism-python.min.js"),
    ]
    for name, pattern in required:
        if pattern not in content:
            issues.append(f"{prefix}: missing {name} ({pattern})")


def check_div_balance(content, issues):
    """Check div open/close balance."""
    opens = len(re.findall(r'<div[\s>]', content))
    closes = content.count('</div>')
    if opens != closes:
        issues.append(f"[html] div imbalance: {opens} opens vs {closes} closes (diff={opens-closes})")


def check_confluence_no_doctype(content, issues):
    """Check no DOCTYPE/html/head/body tags."""
    if '<!DOCTYPE' in content:
        issues.append("[confluence] has <!DOCTYPE> (forbidden)")
    if re.search(r'<html[\s>]', content):
        issues.append("[confluence] has <html> tag (forbidden)")
    if re.search(r'<head[\s>]', content):
        issues.append("[confluence] has <head> tag (forbidden)")
    if re.search(r'<body[\s>]', content):
        issues.append("[confluence] has <body> tag (forbidden)")


def check_js_functions(content, issues):
    """Check required JS functions exist."""
    prefix = "[js]"
    required = [
        "switchCeTab", "switchMkTab", "switchPeTab", "switchQzTab",
        "switchKcTab", "copyCode", "toggleToc",
    ]
    for fn in required:
        if f"function {fn}" not in content:
            issues.append(f"{prefix}: missing function {fn}()")


def check_hub_root(content, issues):
    """Check hub-root wrapper."""
    if 'id="hub-root"' not in content:
        issues.append("[structure] missing #hub-root wrapper")


# ---------------------------------------------------------------------------

def audit_lesson(filepath):
    """Run all checks on a single lesson file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    issues = []

    # Global checks
    check_cdns(content, issues)
    check_div_balance(content, issues)
    check_confluence_no_doctype(content, issues)
    check_js_functions(content, issues)
    check_hub_root(content, issues)
    check_scroll_progress(content, issues)
    check_back_to_top(content, issues)
    check_hero(content, issues)
    check_toc_sidebar(content, issues)
    check_bottom_nav(content, issues)

    # Per-section checks
    present_sections = []
    missing_sections = []

    for sec_id in SECTION_IDS:
        sec_html = extract_section(content, sec_id)
        if not sec_html:
            missing_sections.append(sec_id)
            continue
        present_sections.append(sec_id)

        # Header check
        check_section_header(sec_html, sec_id, issues)

        # Tab system check
        check_tab_system(sec_html, sec_id, issues)

        # Code block style check
        check_code_blocks(sec_html, sec_id, issues)

        # Section-specific format checks
        if sec_id == "mistakes":
            check_mistakes_format(sec_html, issues)
        elif sec_id == "practice":
            check_practice_format(sec_html, issues)
        elif sec_id == "knowledge-check":
            check_quiz_format(sec_html, issues)
        elif sec_id == "recap":
            check_recap_format(sec_html, issues)
        elif sec_id == "objective":
            check_objective_format(sec_html, issues)
        elif sec_id == "overview":
            check_overview_format(sec_html, issues)
        elif sec_id == "key-ideas":
            check_key_ideas_format(sec_html, issues)
        elif sec_id == "next-lesson":
            check_next_lesson_format(sec_html, issues)

    if missing_sections:
        issues.insert(0, f"[sections] MISSING: {', '.join(missing_sections)}")

    return present_sections, missing_sections, issues


# ---------------------------------------------------------------------------

def main():
    print("=" * 80)
    print("MOD 04 — CROSS-LESSON FORMAT AUDIT")
    print("=" * 80)

    all_results = {}
    total_issues = 0

    for lesson_file in LESSONS:
        filepath = os.path.join(LESSON_DIR, lesson_file)
        present, missing, issues = audit_lesson(filepath)
        all_results[lesson_file] = (present, missing, issues)
        total_issues += len(issues)

    # Print per-lesson results
    for lesson_file in LESSONS:
        present, missing, issues = all_results[lesson_file]
        short = lesson_file.replace("lesson", "L").replace("_", " ").replace(".html", "")
        print(f"\n{'─' * 80}")
        print(f"📄 {lesson_file}")
        print(f"   Sections: {len(present)}/12 present | Missing: {', '.join(missing) if missing else 'none'}")

        if issues:
            print(f"   Issues ({len(issues)}):")
            for issue in issues:
                print(f"     ⚠  {issue}")
        else:
            print(f"   ✅ No issues found")

    # Summary matrix
    print(f"\n{'=' * 80}")
    print("SECTION PRESENCE MATRIX")
    print("=" * 80)

    # Header
    short_names = [f"L{str(i+1).zfill(2)}" for i in range(len(LESSONS))]
    header = f"{'Section':<20}" + "".join(f"{s:>5}" for s in short_names)
    print(header)
    print("-" * len(header))

    for sec_id in SECTION_IDS:
        row = f"{sec_id:<20}"
        for lesson_file in LESSONS:
            present, _, _ = all_results[lesson_file]
            row += f"{'  ✓':>5}" if sec_id in present else f"{'  ✗':>5}"
        print(row)

    # Issue summary by category
    print(f"\n{'=' * 80}")
    print("ISSUE SUMMARY BY CATEGORY")
    print("=" * 80)

    category_counts = defaultdict(int)
    category_lessons = defaultdict(list)

    for lesson_file in LESSONS:
        _, _, issues = all_results[lesson_file]
        for issue in issues:
            cat = issue.split("]")[0] + "]" if "]" in issue else "[other]"
            category_counts[cat] += 1
            short = lesson_file.replace(".html", "")
            if short not in category_lessons[cat]:
                category_lessons[cat].append(short)

    for cat in sorted(category_counts.keys(), key=lambda x: -category_counts[x]):
        count = category_counts[cat]
        affected = category_lessons[cat]
        print(f"\n{cat} — {count} issues across {len(affected)} lessons:")
        for lesson_file in LESSONS:
            _, _, issues = all_results[lesson_file]
            for issue in issues:
                if issue.startswith(cat.rstrip("]")):
                    print(f"  {lesson_file}: {issue}")

    print(f"\n{'=' * 80}")
    print(f"TOTAL: {total_issues} issues across {len(LESSONS)} lessons")
    print("=" * 80)


if __name__ == "__main__":
    main()
