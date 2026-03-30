---
mode: "agent"
description: "Sync a lesson HTML file to match lesson01's exact format — strips forbidden HTML shell tags, replaces the style block with lesson01's complete style block, ensures id=\"hub-root\" is on the outer wrapper, and applies the key takeaway card white-hover fix. Run this on any new or out-of-sync lesson before publishing to Confluence."
---

Sync the target lesson file so its structure and CSS match `lesson01_what_is_programming.html` exactly. This is required before any lesson can be embedded in Confluence via the HTML macro.

---

## Input

| Variable | Value |
|---|---|
| `TARGET_FILE` | Absolute path to the lesson HTML file to sync (e.g. `/Users/graywolf/Documents/Project/Python-Learning/pages/track_01/mod_02_programming_foundations/lesson07_loops.html`) |

---

## What This Prompt Fixes

The following four problems are fixed in order:

| # | Problem | Fix |
|---|---|---|
| 1 | File contains `<!DOCTYPE html>`, `<html>`, `<head>`, `<meta>`, `<title>`, `</head>`, `<body>`, `</body>`, `</html>` tags | Strip all of them — Confluence embeds fragment HTML only |
| 2 | Style block is shorter than lesson01's (missing hundreds of CSS rules — hero, tabs, TOC, `#hub-root` overrides, etc.) | Replace entire `<style>…</style>` block with lesson01's exact block |
| 3 | Outer wrapper `<div class="bg-gray-50 min-h-screen">` is missing `id="hub-root"` | Add `id="hub-root"` so all `#hub-root` CSS selectors apply |
| 4 | Key Takeaway card variants (`.obj-card-kt`, `.obj-card-violet`, `.obj-card-blue`) show pink background on hover | Add `background-color: #ffffff` to each variant's `:hover` rule |

---

## Step-by-Step Instructions

### Step 1 — Strip forbidden HTML shell tags

The file must start with the first `<link rel="preconnect">` tag and end with `</script>`. Remove these tags if present:

- **Top of file:** `<!DOCTYPE html>`, `<html lang="en">`, `<head>`, and all `<meta>` / `<title>` lines that appear before the first `<link rel="preconnect">`
- **Middle of file:** `</head>` and `<body>` (the blank line between them too)
- **End of file:** `</body>` and `</html>`

After stripping, the file must:
- **Start with:** `  <link rel="preconnect" href="https://fonts.googleapis.com">`
- **End with:** `</script>` (no trailing blank lines)

### Step 2 — Replace the style block

Extract the entire `<style>…</style>` block from `lesson01_what_is_programming.html` (same directory as the target file). Replace the target file's existing `<style>…</style>` block with the exact content from lesson01. Do not modify lesson01.

The replacement is a verbatim copy — do not alter any selectors, values, or comments.

### Step 3 — Add `id="hub-root"` to the outer wrapper

Find the line:
```html
<div class="bg-gray-50 min-h-screen">
```

Replace it with:
```html
<div id="hub-root" class="bg-gray-50 min-h-screen">
```

Only replace the **first** occurrence. Do not change any other `div` elements.

If `id="hub-root"` is already present, skip this step.

### Step 4 — Apply the key takeaway card white-hover fix

In the `<style>` block (which was just synced from lesson01), find these three lines:

```css
    .obj-card-kt:hover { box-shadow: none; }
    .obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; }
    .obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; }
```

Replace them with:

```css
    .obj-card-kt:hover { box-shadow: none; background-color: #ffffff; }
    .obj-card-violet:hover { border-color: #8b5cf6; box-shadow: none; background-color: #ffffff; }
    .obj-card-blue:hover { border-color: #3b82f6; box-shadow: none; background-color: #ffffff; }
```

> **Note:** If the style block was already synced from a version of lesson01 that already contains `background-color: #ffffff` in these rules, skip this step — it is already correct.

---

## Verification Checklist

After all steps are complete, verify the following:

- [ ] File starts with `  <link rel="preconnect" href="https://fonts.googleapis.com">`
- [ ] File ends with `</script>` — no `</body>` or `</html>` after it
- [ ] No `<!DOCTYPE`, `<html`, `<head>`, `<body>`, `</body>`, `</html>` tags anywhere in the file
- [ ] `id="hub-root"` is present exactly once, on the `<div class="bg-gray-50 min-h-screen">` element
- [ ] The `<style>` block contains the same number of lines as lesson01's style block
- [ ] `.obj-card-kt:hover`, `.obj-card-violet:hover`, and `.obj-card-blue:hover` all include `background-color: #ffffff`

---

## Important Rules

- **Do not** change any lesson-specific content — the hero title, lesson number, subtitle, pill stats, section content, quiz questions, code examples, etc. are all unique per lesson and must not be touched.
- **Do not** modify `lesson01_what_is_programming.html` — it is the reference source only.
- **Do not** create any summary or documentation files after completing the sync.
- Apply all four steps using a Python script if multiple files need syncing simultaneously, rather than editing files one at a time.
- Re-run the verification checklist after every sync and fix any failures before reporting completion.
