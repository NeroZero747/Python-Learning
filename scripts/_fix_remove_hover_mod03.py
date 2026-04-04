"""
Remove all hover effects from mod_03 lesson files,
preserving bottom-nav .lesson-nav-link:hover and group-hover: classes.
"""
import re, glob, os

TARGET = r"pages/mod_03_python_for_data_analysts"
files = sorted(glob.glob(os.path.join(TARGET, "lesson*.html")))
print(f"Found {len(files)} lesson files in {TARGET}\n")


# ── Operation 1: CSS :hover rule stripping ──────────────────────────

def parse_css_blocks(css):
    """Split CSS into (kind, selector, body) tuples."""
    blocks = []
    i = 0; n = len(css)
    while i < n:
        brace = css.find('{', i)
        if brace == -1:
            blocks.append(('tail', css[i:], '')); break
        sel = css[i:brace]
        depth = 1; j = brace + 1
        while j < n and depth > 0:
            if css[j] == '{': depth += 1
            elif css[j] == '}': depth -= 1
            j += 1
        blocks.append(('rule', sel, css[brace+1:j-1])); i = j
    return blocks


def strip_css_hover(css):
    """Remove :hover rules from CSS, preserving lesson-nav-link:hover."""
    blocks = parse_css_blocks(css)
    out = []
    for kind, sel, body in blocks:
        if kind == 'tail':
            out.append(sel); continue
        # @-rules: recurse into body
        if sel.strip().startswith('@'):
            inner = strip_css_hover(body)
            # If inner body is empty (only whitespace), drop entire @-rule
            if inner.strip():
                out.append(f"{sel}{{{inner}}}")
            continue
        # :hover selectors — drop unless lesson-nav-link
        if ':hover' in sel:
            if 'lesson-nav-link' in sel:
                out.append(f"{sel}{{{body}}}")
            # else: drop it
            continue
        # Everything else: keep
        out.append(f"{sel}{{{body}}}")
    return ''.join(out)


# ── Operation 2: Inline Tailwind hover: class stripping ─────────────

def clean_class_attr(m):
    val = m.group(1)
    if 'hover:' not in val:
        return m.group(0)
    val = re.sub(r'(?<!-)hover:\S+', '', val)
    val = re.sub(r' +', ' ', val).strip()
    return f'class="{val}"'


# ── Process each file ───────────────────────────────────────────────

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as fh:
        text = fh.read()
    original = text

    # Op 1 — Strip CSS :hover from <style> block
    def process_style(m):
        return '<style>' + strip_css_hover(m.group(1)) + '</style>'
    text = re.sub(r'<style>(.*?)</style>', process_style, text, flags=re.DOTALL)

    # Op 2 — Strip inline Tailwind hover: classes (but not group-hover:)
    text = re.sub(r'class="([^"]*)"', clean_class_attr, text)

    # Op 3 — Targeted cleanup of :hover inside @media print
    text = text.replace(
        '      .obj-card:hover { transform: none; box-shadow: none; }\n',
        ''
    )
    text = re.sub(
        r'(\.hero-container \{ display: none; \})\s*\.obj-card:hover \{ transform: none; box-shadow: none; \}\s*(\})',
        r'\1 \2',
        text
    )

    # Op 4 — Collapse 3+ blank lines to 2
    text = re.sub(r'\n{3,}', '\n\n', text)

    fname = os.path.basename(fpath)
    if text != original:
        with open(fpath, 'w', encoding='utf-8') as fh:
            fh.write(text)
        diff = len(original) - len(text)
        print(f"  ✅ {fname} (-{diff} chars)")
    else:
        print(f"  ⚠️  {fname}: no changes")

print("\nDone.")
