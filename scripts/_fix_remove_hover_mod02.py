"""
Remove all hover effects from mod_02_python_foundations lesson files,
preserving only bottom-nav (lesson-nav-link) hovers.

Targets:
  1. Inline Tailwind  hover:xxx  classes  (NOT group-hover:)
  2. CSS :hover rules inside the <style> block  (NOT lesson-nav-link)
  3. CSS :hover rules inside @media blocks      (NOT lesson-nav-link)
"""

import re, pathlib

FOLDER = pathlib.Path("pages/mod_02_python_foundations")
FILES = sorted(FOLDER.glob("lesson*.html"))


# ── CSS parser helpers ──────────────────────────────────────────

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
    """Remove :hover rules except those whose selector contains lesson-nav-link."""
    blocks = parse_css_blocks(css)
    out = []
    for kind, sel, body in blocks:
        if kind == 'tail':
            out.append(sel)
        elif sel.lstrip().startswith('@'):
            # @-rule (media, keyframes): recurse into inner content
            inner = strip_css_hover(body)
            if inner.strip():
                out.append(f'{sel}{{{inner}}}')
            # else: drop empty @-rule
        elif ':hover' in sel:
            if 'lesson-nav-link' in sel:
                out.append(f'{sel}{{{body}}}')
            # else: drop hover rule
        else:
            out.append(f'{sel}{{{body}}}')
    return ''.join(out)


# ── Inline Tailwind hover class remover ─────────────────────────

def clean_class_attr(m):
    """Remove  hover:xxx  tokens from a class attribute value.
    Keeps  group-hover:xxx  (used by bottom-nav children)."""
    val = m.group(1)
    if 'hover:' not in val:
        return m.group(0)  # fast-path: nothing to change
    val = re.sub(r'(?<!-)hover:\S+', '', val)
    val = re.sub(r' +', ' ', val).strip()
    return f'class="{val}"'


# ── Main loop ───────────────────────────────────────────────────

for fpath in FILES:
    text = fpath.read_text(encoding='utf-8')
    orig = text

    # 1. Strip :hover rules from the <style> block
    def style_sub(m):
        return '<style>' + strip_css_hover(m.group(1)) + '</style>'

    text = re.sub(r'<style>(.*?)</style>', style_sub, text, flags=re.DOTALL)

    # 2. Strip inline Tailwind  hover:  classes (not group-hover:)
    text = re.sub(r'class="([^"]*)"', clean_class_attr, text)

    # 3. Collapse runs of 3+ blank lines to 2
    text = re.sub(r'\n{3,}', '\n\n', text)

    if text != orig:
        fpath.write_text(text, encoding='utf-8')
        delta = len(orig) - len(text)
        print(f"  ✅ {fpath.name}  ({delta:+d} chars)")
    else:
        print(f"  ⚠️  {fpath.name}: no changes")

print(f"\nDone — processed {len(FILES)} files.")
