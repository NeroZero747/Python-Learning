#!/usr/bin/env python3
"""Sync mod03/lesson01 structure and CSS to match mod02/lesson01 (reference)."""

import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "pages" / "track_01"
REFERENCE = BASE / "mod_02_programming_foundations" / "lesson01_what_is_programming.html"
TARGET = BASE / "mod_03_object_oriented_programming" / "lesson01_why_classes_help_data_projects.html"


def extract_style_block(text: str) -> str:
    """Return the full <style>…</style> block (inclusive)."""
    m = re.search(r"<style>.*?</style>", text, re.DOTALL)
    if not m:
        raise ValueError("No <style> block found")
    return m.group(0)


def strip_html_shell(text: str) -> str:
    """Remove forbidden shell tags: DOCTYPE, html, head, meta, title, body."""
    # Remove lines at the top before the first <link rel="preconnect">
    lines = text.split("\n")
    start_idx = None
    for i, line in enumerate(lines):
        if '<link rel="preconnect"' in line:
            start_idx = i
            break
    if start_idx is None:
        raise ValueError("Could not find <link rel='preconnect'> line")

    # Remove </head> and <body> lines
    kept = []
    for line in lines[start_idx:]:
        stripped = line.strip()
        if stripped in ("</head>", "<body>", "</body>", "</html>", "</body></html>"):
            continue
        if stripped.startswith("<!DOCTYPE") or stripped.startswith("<html"):
            continue
        kept.append(line)

    # Strip trailing blank lines, ensure file ends with </script>
    while kept and kept[-1].strip() == "":
        kept.pop()

    return "\n".join(kept)


def add_hub_root_id(text: str) -> str:
    """Add id='hub-root' to the outer wrapper div if not present."""
    if 'id="hub-root"' in text:
        print("  ⏭  id=\"hub-root\" already present — skipping")
        return text
    old = '<div class="bg-gray-50 min-h-screen">'
    new = '<div id="hub-root" class="bg-gray-50 min-h-screen">'
    if old not in text:
        raise ValueError(f"Could not find wrapper div: {old}")
    # Only replace the first occurrence
    return text.replace(old, new, 1)


def verify(text: str, label: str) -> None:
    """Run the verification checklist."""
    errors = []
    lines = text.split("\n")

    # Starts with <link rel="preconnect">
    first_non_empty = next((l for l in lines if l.strip()), "")
    if '<link rel="preconnect"' not in first_non_empty:
        errors.append(f"File does not start with <link rel='preconnect'>: {first_non_empty[:80]}")

    # Ends with </script>
    last_non_empty = next((l for l in reversed(lines) if l.strip()), "")
    if last_non_empty.strip() != "</script>":
        errors.append(f"File does not end with </script>: {last_non_empty.strip()[:80]}")

    # No forbidden tags
    for tag in ["<!DOCTYPE", "<html", "<head>", "<body>", "</body>", "</html>"]:
        if tag.lower() in text.lower():
            errors.append(f"Forbidden tag found: {tag}")

    # id="hub-root" present exactly once
    count = text.count('id="hub-root"')
    if count != 1:
        errors.append(f'id="hub-root" appears {count} times (expected 1)')

    # obj-card hover rules include background-color: #ffffff
    for cls in ["obj-card-kt", "obj-card-violet", "obj-card-blue"]:
        pattern = rf"\.{cls}:hover\s*\{{[^}}]*\}}"
        m = re.search(pattern, text)
        if m:
            if "background-color: #ffffff" not in m.group(0):
                errors.append(f".{cls}:hover missing background-color: #ffffff")
        else:
            errors.append(f".{cls}:hover rule not found")

    if errors:
        print(f"  ❌ {label} VERIFICATION FAILED:")
        for e in errors:
            print(f"     • {e}")
    else:
        print(f"  ✅ {label} — all checks passed")


def main():
    print(f"Reference: {REFERENCE.name}")
    print(f"Target:    {TARGET.name}\n")

    ref_text = REFERENCE.read_text(encoding="utf-8")
    tgt_text = TARGET.read_text(encoding="utf-8")

    # Step 1: Strip HTML shell
    print("Step 1 — Strip forbidden HTML shell tags")
    tgt_text = strip_html_shell(tgt_text)
    print("  ✅ Shell tags stripped")

    # Step 2: Replace style block
    print("Step 2 — Replace <style> block with reference")
    ref_style = extract_style_block(ref_text)
    tgt_style = extract_style_block(tgt_text)
    tgt_text = tgt_text.replace(tgt_style, ref_style, 1)
    ref_lines = ref_style.count("\n")
    print(f"  ✅ Style block replaced ({ref_lines} lines)")

    # Step 3: Add id="hub-root"
    print("Step 3 — Add id=\"hub-root\" to outer wrapper")
    tgt_text = add_hub_root_id(tgt_text)
    print("  ✅ hub-root id added")

    # Step 4: Verify obj-card hover rules (should already be correct from ref)
    print("Step 4 — Verify key takeaway card white-hover fix")
    for cls in ["obj-card-kt", "obj-card-violet", "obj-card-blue"]:
        pattern = rf"\.{cls}:hover\s*\{{[^}}]*background-color:\s*#ffffff[^}}]*\}}"
        if re.search(pattern, tgt_text):
            print(f"  ✅ .{cls}:hover already has background-color: #ffffff")
        else:
            print(f"  ⚠️  .{cls}:hover needs patching (not expected with current ref)")

    # Write back
    TARGET.write_text(tgt_text, encoding="utf-8")
    print(f"\n💾 Written: {TARGET}")

    # Final verification
    print("\n── Verification ──")
    verify(tgt_text, TARGET.name)


if __name__ == "__main__":
    main()
