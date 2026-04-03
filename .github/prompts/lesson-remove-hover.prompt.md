---
mode: "agent"
description: "Remove all hover effects from every lesson HTML file in a target folder — strips inline Tailwind hover: classes and CSS :hover rules from the <style> block, while preserving bottom-nav (Previous / All Lessons / Next) hovers. Creates and runs a Python script to apply changes across all files at once."
---

Remove all hover effects from every `lesson*.html` file inside the target folder, except the bottom navigation links (Previous / All Lessons / Next).

---

## Required Input

| Variable | Value |
|---|---|
| `TARGET_FOLDER` | Relative path from workspace root to the folder containing the lesson files (e.g. `pages/mod_01_getting_started`) |

---

## What Gets Removed

| Type | Example | Removed? |
|---|---|---|
| Inline Tailwind `hover:` classes | `hover:bg-pink-50`, `hover:border-[#CB187D]`, `hover:shadow-md` | **Yes** |
| CSS `:hover` rules in `<style>` | `.obj-card:hover { … }`, `.copy-btn:hover { … }` | **Yes** |
| CSS `:hover` inside `@media` blocks | `.obj-card:hover` inside `@media print { … }` | **Yes** |

## What Gets Preserved

| Type | Example | Why |
|---|---|---|
| Inline `group-hover:` classes | `group-hover:text-[#CB187D]` on bottom nav child elements | Bottom nav uses Tailwind `group` pattern for hover color |
| CSS `.lesson-nav-link:hover` rules | `.lesson-nav-link:hover p, span, svg { color: #CB187D; }` | Bottom nav hover color (Layer 2 CSS) |
| CSS `#hub-root .lesson-nav-link:hover` rules | Confluence override for bottom nav hover | Bottom nav hover color (Confluence isolation block) |

---

## Step-by-Step Instructions

### Step 1 — Identify target files

List all `lesson*.html` files inside `TARGET_FOLDER`. Confirm the file count with the user before proceeding.

### Step 2 — Create the removal script

Create a Python script at `scripts/_fix_remove_hover_<FOLDER_SUFFIX>.py` where `<FOLDER_SUFFIX>` is a short name derived from `TARGET_FOLDER` (e.g. `mod01` for `mod_01_getting_started`, `mod02` for `mod_02_python_foundations`).

The script must implement these three operations in order:

#### Operation 1 — Strip CSS `:hover` rules from `<style>` block

Parse the CSS inside `<style>…</style>` using a brace-depth tracker:

```python
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
```

Use `strip_css_hover(css)` to walk the parsed blocks:
- **`@`-rules** (e.g. `@media print`, `@media (max-width: 767px)`): recurse into their body. If the inner body is empty after recursion, drop the entire `@`-rule.
- **`:hover` selectors**: drop the rule **unless** the selector contains `lesson-nav-link`.
- **Everything else**: keep as-is.

#### Operation 2 — Strip inline Tailwind `hover:` classes

Use a regex to find all `class="…"` attributes and remove any `hover:\S+` token that is **not** preceded by a hyphen (which would make it `group-hover:`):

```python
def clean_class_attr(m):
    val = m.group(1)
    if 'hover:' not in val:
        return m.group(0)
    val = re.sub(r'(?<!-)hover:\S+', '', val)
    val = re.sub(r' +', ' ', val).strip()
    return f'class="{val}"'

text = re.sub(r'class="([^"]*)"', clean_class_attr, text)
```

#### Operation 3 — Targeted removal of `:hover` inside `@media print`

The CSS parser may not fully recurse into multi-line `@media print` blocks. After Operations 1–2, do a direct string replacement to remove any surviving `.obj-card:hover` rule inside `@media print`:

```python
# Remove multi-line variant
text = text.replace(
    '      .obj-card:hover { transform: none; box-shadow: none; }\n',
    ''
)
# Remove single-line variant (rule embedded in one-line @media print)
text = re.sub(
    r'(\.hero-container \{ display: none; \})\s*\.obj-card:hover \{ transform: none; box-shadow: none; \}\s*(\})',
    r'\1 \2',
    text
)
```

#### Operation 4 — Clean up blank lines

Collapse any runs of 3+ consecutive blank lines down to 2:

```python
text = re.sub(r'\n{3,}', '\n\n', text)
```

### Step 3 — Run the script

Execute the script and confirm each file is patched. The script should print per-file status:
- `✅ filename.html (+N chars)` — successfully patched
- `⚠️ filename.html: no changes` — already clean

### Step 4 — Verify with grep

Run a grep across all target files to confirm only `lesson-nav-link:hover` references remain:

```bash
grep -rn ":hover" <TARGET_FOLDER>/lesson*.html
```

**Expected result:** Every remaining `:hover` line must contain `lesson-nav-link`. If any other `:hover` rule or inline `hover:` class survives, fix it with a targeted `multi_replace_string_in_file`.

Also check for surviving inline `hover:` classes:

```bash
grep -rn "hover:" <TARGET_FOLDER>/lesson*.html | grep -v "group-hover:" | grep -v ":hover"
```

**Expected result:** No output. If any inline `hover:` tokens remain, apply a targeted fix.

### Step 5 — Report

Summarize what was removed:
- Number of files patched
- Types of hovers removed (inline Tailwind classes, CSS rules, @media-nested rules)
- Confirmation that bottom-nav hovers are intact
