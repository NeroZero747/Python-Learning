#!/usr/bin/env python3
"""
Convert British English spellings to American English across all
track_02_data_analytics HTML files.

Handles: -ise→-ize, -isation→-ization, -our→-or, maths→math,
         programme→program, catalogue→catalog, enrolment→enrollment,
         travelling→traveling, etc.

Each replacement uses word boundaries (\b) so function names,
HTML classes, and other non-prose tokens are untouched.
"""

import re, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
TRACK = BASE / "pages" / "track_02_data_analytics"

# ── (british_lowercase, american_lowercase) ────────────────────────────
# Longer forms FIRST so "optimisation" is matched before "optimise".
PAIRS = [
    # -isation / -ization
    ("optimisation",   "optimization"),
    ("summarisation",  "summarization"),
    ("serialisation",  "serialization"),
    ("visualisations", "visualizations"),
    ("visualisation",  "visualization"),
    ("organisations",  "organizations"),
    ("organisation",   "organization"),

    # -ising / -izing
    ("optimising",   "optimizing"),
    ("normalising",  "normalizing"),
    ("serialising",  "serializing"),
    ("summarising",  "summarizing"),
    ("organising",   "organizing"),
    ("recognising",  "recognizing"),
    ("analysing",    "analyzing"),
    ("categorising", "categorizing"),
    ("visualising",  "visualizing"),

    # -ised / -ized
    ("optimised",   "optimized"),
    ("normalised",  "normalized"),
    ("serialised",  "serialized"),
    ("summarised",  "summarized"),
    ("organised",   "organized"),
    ("recognised",  "recognized"),
    ("analysed",    "analyzed"),
    ("categorised", "categorized"),
    ("visualised",  "visualized"),

    # -ises / -izes
    ("optimises",   "optimizes"),
    ("serialises",  "serializes"),
    ("summarises",  "summarizes"),
    ("normalises",  "normalizes"),
    ("organises",   "organizes"),
    ("recognises",  "recognizes"),

    # -iser / -izer
    ("serialiser", "serializer"),
    ("organiser",  "organizer"),

    # -ise / -ize (base forms — last so longer forms above match first)
    ("optimise",   "optimize"),
    ("normalise",  "normalize"),
    ("serialise",  "serialize"),
    ("summarise",  "summarize"),
    ("organise",   "organize"),
    ("recognise",  "recognize"),
    ("analyse",    "analyze"),
    ("categorise", "categorize"),
    ("visualise",  "visualize"),

    # -our / -or
    ("behaviours", "behaviors"),
    ("behaviour",  "behavior"),
    ("colours",    "colors"),
    ("colour",     "color"),
    ("favours",    "favors"),
    ("favour",     "favor"),

    # Other
    ("programmes",  "programs"),
    ("programme",   "program"),
    ("catalogues",  "catalogs"),
    ("catalogue",   "catalog"),
    ("enrolments",  "enrollments"),
    ("enrolment",   "enrollment"),
    ("travelling",  "traveling"),
    ("travelled",   "traveled"),
    ("maths",       "math"),
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
    """Apply all British→American replacements. Return (new_text, total_subs)."""
    total = 0
    for regex, replacement in PATTERNS:
        text, n = regex.subn(replacement, text)
        total += n
    return text, total


# ── Main ───────────────────────────────────────────────────────────────
files = sorted(TRACK.rglob("*.html"))
grand_total = 0

for path in files:
    original = path.read_text(encoding="utf-8")
    updated, count = convert(original)
    if count > 0:
        path.write_text(updated, encoding="utf-8")
        print(f"✅ {count:3d} changes  {path.relative_to(BASE)}")
        grand_total += count
    else:
        print(f"   —  no changes  {path.relative_to(BASE)}")

print(f"\n{grand_total} total replacements across {len(files)} files")
