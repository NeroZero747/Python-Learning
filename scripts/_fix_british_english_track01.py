#!/usr/bin/env python3
"""
Convert British English spellings to American English across all
track_01_python_foundation HTML files.
"""

import re, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
TRACK = BASE / "pages" / "track_01_python_foundation"

# ── (british_lowercase, american_lowercase) ────────────────────────────
# Longer forms FIRST so compound words match before base forms.
PAIRS = [
    # -isation / -ization
    ("initialisation",  "initialization"),
    ("customisation",   "customization"),
    ("organisations",   "organizations"),
    ("organisation",    "organization"),

    # -ising / -izing
    ("initialising",  "initializing"),
    ("organising",    "organizing"),
    ("recognising",   "recognizing"),
    ("customising",   "customizing"),
    ("summarising",   "summarizing"),
    ("capitalising",  "capitalizing"),

    # -ised / -ized
    ("initialised",   "initialized"),
    ("organised",     "organized"),
    ("recognised",    "recognized"),
    ("customised",    "customized"),
    ("summarised",    "summarized"),
    ("capitalised",   "capitalized"),
    ("specialised",   "specialized"),

    # -ises / -izes
    ("initialises",   "initializes"),
    ("recognises",    "recognizes"),
    ("memorises",     "memorizes"),
    ("organises",     "organizes"),
    ("summarises",    "summarizes"),

    # -ise / -ize (base forms)
    ("initialise",  "initialize"),
    ("organise",    "organize"),
    ("recognise",   "recognize"),
    ("customise",   "customize"),
    ("summarise",   "summarize"),
    ("capitalise",  "capitalize"),
    ("memorise",    "memorize"),

    # -our / -or
    ("behaviours",  "behaviors"),
    ("behaviour",   "behavior"),
    ("colours",     "colors"),
    ("colour",      "color"),

    # Other
    ("catalogues",  "catalogs"),
    ("catalogue",   "catalog"),
    ("backwards",   "backward"),
    ("maths",       "math"),

    # enrol → enroll (standalone only — "enrolled"/"enrollment" are already American)
    ("enrols",  "enrolls"),
    ("enrol",   "enroll"),
]


def _build_patterns():
    """Create compiled (regex, replacement) tuples for lower, Title, UPPER."""
    patterns = []
    for brit, amer in PAIRS:
        for b, a in [(brit, amer),
                     (brit.capitalize(), amer.capitalize()),
                     (brit.upper(), amer.upper())]:
            patterns.append((re.compile(r"\b" + re.escape(b) + r"\b"), a))
    return patterns


PATTERNS = _build_patterns()


def convert(text: str) -> tuple[str, int]:
    total = 0
    for regex, replacement in PATTERNS:
        text, n = regex.subn(replacement, text)
        total += n
    return text, total


# ── Main ───────────────────────────────────────────────────────────────
files = sorted(TRACK.rglob("*.html"))
grand_total = 0
changed_files = 0

for path in files:
    original = path.read_text(encoding="utf-8")
    updated, count = convert(original)
    if count > 0:
        path.write_text(updated, encoding="utf-8")
        print(f"\u2705 {count:3d} changes  {path.relative_to(BASE)}")
        grand_total += count
        changed_files += 1
    else:
        print(f"   \u2014  no changes  {path.relative_to(BASE)}")

print(f"\n{grand_total} total replacements across {changed_files}/{len(files)} files")
