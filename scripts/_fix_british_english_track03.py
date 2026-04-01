#!/usr/bin/env python3
"""
Convert British English spellings to American English across all
track_03_data_engineering HTML files.
"""

import re, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
TRACK = BASE / "pages" / "track_03_data_engineering"

# ── (british_lowercase, american_lowercase) ────────────────────────────
# Longer forms FIRST so compound words match before base forms.
PAIRS = [
    # -isation / -ization
    ("synchronisation",  "synchronization"),
    ("customisation",    "customization"),
    ("optimisations",    "optimizations"),
    ("optimisation",     "optimization"),
    ("serialisation",    "serialization"),
    ("summarisation",    "summarization"),
    ("organisations",    "organizations"),
    ("organisation",     "organization"),
    ("authorisation",    "authorization"),

    # de- / des- prefixed forms
    ("deserialises",  "deserializes"),
    ("deserialise",   "deserialize"),
    ("denormalised",  "denormalized"),
    ("denormalise",   "denormalize"),

    # -ising / -izing
    ("optimising",    "optimizing"),
    ("normalising",   "normalizing"),
    ("serialising",   "serializing"),
    ("summarising",   "summarizing"),
    ("organising",    "organizing"),
    ("recognising",   "recognizing"),
    ("analysing",     "analyzing"),
    ("categorising",  "categorizing"),
    ("visualising",   "visualizing"),
    ("customising",   "customizing"),
    ("standardising", "standardizing"),
    ("synchronising", "synchronizing"),
    ("authorising",   "authorizing"),

    # -ised / -ized
    ("optimised",     "optimized"),
    ("normalised",    "normalized"),
    ("serialised",    "serialized"),
    ("summarised",    "summarized"),
    ("organised",     "organized"),
    ("recognised",    "recognized"),
    ("analysed",      "analyzed"),
    ("categorised",   "categorized"),
    ("visualised",    "visualized"),
    ("customised",    "customized"),
    ("specialised",   "specialized"),
    ("standardised",  "standardized"),
    ("practised",     "practiced"),
    ("authorised",    "authorized"),

    # -ises / -izes
    ("optimises",     "optimizes"),
    ("serialises",    "serializes"),
    ("summarises",    "summarizes"),
    ("normalises",    "normalizes"),
    ("organises",     "organizes"),
    ("recognises",    "recognizes"),
    ("materialises",  "materializes"),
    ("authorises",    "authorizes"),

    # -iser / -izer
    ("optimiser",     "optimizer"),
    ("serialiser",    "serializer"),
    ("organiser",     "organizer"),

    # -ise / -ize (base forms — last so longer forms above match first)
    ("optimise",    "optimize"),
    ("normalise",   "normalize"),
    ("serialise",   "serialize"),
    ("summarise",   "summarize"),
    ("organise",    "organize"),
    ("recognise",   "recognize"),
    ("analyse",     "analyze"),
    ("categorise",  "categorize"),
    ("visualise",   "visualize"),
    ("customise",   "customize"),
    ("materialise", "materialize"),
    ("standardise", "standardize"),
    ("synchronise", "synchronize"),
    ("memorise",    "memorize"),
    ("practise",    "practice"),
    ("authorise",   "authorize"),

    # -our / -or
    ("behaviours",  "behaviors"),
    ("behaviour",   "behavior"),
    ("colours",     "colors"),
    ("colour",      "color"),
    ("favours",     "favors"),
    ("favour",      "favor"),
    ("honours",     "honors"),
    ("honour",      "honor"),
    ("labours",     "labors"),
    ("labour",      "labor"),

    # -lling / -ling
    ("labelling",   "labeling"),

    # Other
    ("defence",     "defense"),
    ("catalogues",  "catalogs"),
    ("catalogue",   "catalog"),
    ("cheque",      "check"),
    ("afterwards",  "afterward"),
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
    """Apply all British->American replacements. Return (new_text, total_subs)."""
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
