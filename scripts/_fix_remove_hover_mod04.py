"""
Remove all hover effects from lesson*.html files in mod_04_data_engineering,
EXCEPT bottom navigation links (lesson-nav-link / group-hover).
"""

import glob
import os
import re

TARGET_FOLDER = os.path.join("pages", "mod_04_data_engineering")
TARGET_FILES = sorted(glob.glob(os.path.join(TARGET_FOLDER, "lesson*.html")))


# ── Operation 1: CSS :hover rule removal ─────────────────────────────────────

def parse_css_blocks(css):
    """Split CSS into (kind, selector, body) tuples."""
    blocks = []
    i = 0
    n = len(css)
    while i < n:
        brace = css.find("{", i)
        if brace == -1:
            blocks.append(("tail", css[i:], ""))
            break
        sel = css[i:brace]
        depth = 1
        j = brace + 1
        while j < n and depth > 0:
            if css[j] == "{":
                depth += 1
            elif css[j] == "}":
                depth -= 1
            j += 1
        blocks.append(("rule", sel, css[brace + 1 : j - 1]))
        i = j
    return blocks


def strip_css_hover(css):
    """Remove :hover rules from CSS, preserving lesson-nav-link:hover."""
    blocks = parse_css_blocks(css)
    out = []
    for kind, sel, body in blocks:
        if kind == "tail":
            out.append(sel)
            continue

        sel_stripped = sel.strip()

        # @-rules: recurse into body
        if sel_stripped.startswith("@"):
            inner = strip_css_hover(body)
            inner_clean = inner.strip()
            if inner_clean:
                out.append(f"{sel}{{{inner}}}")
            # else: drop empty @-rule
            continue

        # :hover selectors — keep only lesson-nav-link ones
        if ":hover" in sel_stripped:
            if "lesson-nav-link" in sel_stripped:
                out.append(f"{sel}{{{body}}}")
            # else: drop the rule
            continue

        # Everything else: keep
        out.append(f"{sel}{{{body}}}")

    return "".join(out)


def process_style_block(html):
    """Find <style>…</style>, run strip_css_hover on its contents."""
    pattern = re.compile(r"(<style[^>]*>)(.*?)(</style>)", re.DOTALL)
    def replacer(m):
        open_tag = m.group(1)
        css = m.group(2)
        close_tag = m.group(3)
        cleaned = strip_css_hover(css)
        return f"{open_tag}{cleaned}{close_tag}"
    return pattern.sub(replacer, html)


# ── Operation 2: Inline Tailwind hover: class removal ───────────────────────

def clean_class_attr(m):
    val = m.group(1)
    if "hover:" not in val:
        return m.group(0)
    # Remove hover:xxx tokens but NOT group-hover:xxx (preceded by -)
    val = re.sub(r"(?<!-)hover:\S+", "", val)
    val = re.sub(r" +", " ", val).strip()
    return f'class="{val}"'


def strip_inline_hover(html):
    return re.sub(r'class="([^"]*)"', clean_class_attr, html)


# ── Operation 3: Targeted @media print cleanup ──────────────────────────────

def strip_media_print_hover(text):
    # Multi-line variant
    text = text.replace(
        "      .obj-card:hover { transform: none; box-shadow: none; }\n", ""
    )
    # Single-line variant
    text = re.sub(
        r"(\.hero-container \{ display: none; \})\s*\.obj-card:hover \{ transform: none; box-shadow: none; \}\s*(\})",
        r"\1 \2",
        text,
    )
    return text


# ── Operation 4: Collapse blank lines ───────────────────────────────────────

def collapse_blank_lines(text):
    return re.sub(r"\n{3,}", "\n\n", text)


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    if not TARGET_FILES:
        print("❌ No lesson files found!")
        return

    print(f"Processing {len(TARGET_FILES)} lesson files in {TARGET_FOLDER}\n")

    for fpath in TARGET_FILES:
        fname = os.path.basename(fpath)
        original = open(fpath, "r", encoding="utf-8").read()

        text = process_style_block(original)
        text = strip_inline_hover(text)
        text = strip_media_print_hover(text)
        text = collapse_blank_lines(text)

        if text != original:
            diff = len(original) - len(text)
            open(fpath, "w", encoding="utf-8").write(text)
            print(f"  ✅ {fname} (−{diff} chars)")
        else:
            print(f"  ⚠️  {fname}: no changes")

    print("\nDone.")


if __name__ == "__main__":
    main()
