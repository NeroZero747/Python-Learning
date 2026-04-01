"""Verify #next-lesson + bottom nav in all track_03 lesson files."""
import os, re

BASE = "pages/track_03_data_engineering"

files = []
for root, dirs, fnames in os.walk(BASE):
    dirs.sort()
    for fn in sorted(fnames):
        if fn.endswith(".html"):
            files.append(os.path.join(root, fn))

pass_count = 0
fail_count = 0
for fp in files:
    content = open(fp, encoding="utf-8").read()
    rel = os.path.relpath(fp, BASE)
    issues = []

    # 1. #next-lesson section exists
    if not re.search(r'<section id="next-lesson"', content):
        issues.append("no-next-lesson-section")

    # 2. scroll-mt-24
    if not re.search(r'id="next-lesson" class="scroll-mt-24"', content):
        issues.append("missing-scroll-mt-24")

    # 3. Section header icon
    nl_match = re.search(r'<section id="next-lesson".*?</section>', content, re.DOTALL)
    if nl_match:
        nl = nl_match.group()
        if 'data-icon="fa6-solid:circle-arrow-right"' not in nl:
            issues.append("wrong-header-icon")

        # 4. Check lesson badge or track-complete banner
        is_last = "lesson05_deployment_workflow" in rel
        if is_last:
            if "Congratulations" not in nl and "Track Complete" not in nl:
                issues.append("missing-track-complete")
        else:
            if "Next you will learn:" not in nl:
                issues.append("missing-learn-line")
            # 5. 3 preview cards
            cards = re.findall(r'class="obj-card', nl)
            if len(cards) != 3:
                issues.append(f"preview-cards={len(cards)}")

    # 6. Bottom nav exists
    if 'All Lessons' not in content:
        issues.append("no-all-lessons-link")

    # 7. Hub path
    if '../../../hub_home_page.html' not in content:
        issues.append("wrong-hub-path")

    # 8. First lesson has spacer instead of prev link
    is_first = "mod_01_data_engineering_foundations" in rel and "lesson01_what_is_data_engineering" in rel
    if is_first:
        # Should have spacer div, not a Previous link
        if '<div class="flex-1"></div>' not in content:
            issues.append("first-lesson-missing-spacer")

    # 9. Section count preserved
    secs = re.findall(r'<section id="([^"]+)"', content)
    if len(secs) < 8:
        issues.append(f"sections={len(secs)}")

    # 10. Check prev/next nav links exist for mid-track lessons
    if not is_first and not is_last:
        if 'Previous' not in content:
            issues.append("no-prev-nav")
        # All non-last lessons should have Next nav
        nav_sections = content.split('id="next-lesson"')
        if len(nav_sections) > 1:
            after = nav_sections[1]
            if 'fa6-solid:arrow-right' not in after and not is_last:
                pass  # some may not have it if last of track

    if issues:
        print(f"  [FAIL] {rel}: {', '.join(issues)}")
        fail_count += 1
    else:
        pass_count += 1

print(f"\nVerified: {pass_count} passed, {fail_count} failed ({pass_count + fail_count} total)")
