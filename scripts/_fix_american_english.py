"""Fix all British English spellings to American English in all .github prompt/instruction files."""

import re
from pathlib import Path

PROMPT_DIR = Path(".github")

# Collect all markdown files under .github/
files = list(PROMPT_DIR.rglob("*.md"))

# Ordered replacement pairs: (pattern, replacement)
# Using case-preserving substitution where needed via regex with IGNORECASE + repl function.
REPLACEMENTS = [
    # colour/coloured/colourful/colour-matched/colour-coded → color/…
    (r'\bColour\b', 'Color'),
    (r'\bcolour\b', 'color'),
    (r'\bColoured\b', 'Colored'),
    (r'\bcoloured\b', 'colored'),
    (r'\bColours\b', 'Colors'),
    (r'\bcolours\b', 'colors'),
    # behaviour/behaviour → behavior
    (r'\bBehaviour\b', 'Behavior'),
    (r'\bbehaviour\b', 'behavior'),
    (r'\bBehaviours\b', 'Behaviors'),
    (r'\bbehaviours\b', 'behaviors'),
    # recognise/recognises/recognised/recognising → recognize/…
    (r'\brecognise\b', 'recognize'),
    (r'\brecognises\b', 'recognizes'),
    (r'\brecognised\b', 'recognized'),
    (r'\brecognising\b', 'recognizing'),
    (r'\bRecognise\b', 'Recognize'),
    (r'\bRecognises\b', 'Recognizes'),
    (r'\bRecognised\b', 'Recognized'),
    # centre/centred/centres/centring → center/centered/centers/centering
    (r'\bcentre\b', 'center'),
    (r'\bcentred\b', 'centered'),
    (r'\bcentres\b', 'centers'),
    (r'\bcentring\b', 'centering'),
    (r'\bCentre\b', 'Center'),
    (r'\bCentred\b', 'Centered'),
    (r'\bCentres\b', 'Centers'),
    # favour/favours/favourite/favourites → favor/…
    (r'\bfavour\b', 'favor'),
    (r'\bFavour\b', 'Favor'),
    (r'\bfavours\b', 'favors'),
    (r'\bfavourite\b', 'favorite'),
    (r'\bFavourite\b', 'Favorite'),
    (r'\bfavourites\b', 'favorites'),
    # practise (verb) → practice
    (r'\bpractised\b', 'practiced'),
    (r'\bpractising\b', 'practicing'),
    (r'\bpractise\b', 'practice'),
    (r'\bPractise\b', 'Practice'),
    (r'\bpractises\b', 'practices'),
    # sanitisation → sanitization
    (r'\bsanitisation\b', 'sanitization'),
    (r'\bSanitisation\b', 'Sanitization'),
    # organise/organised/organisation/organising → organize/…
    (r'\borganise\b', 'organize'),
    (r'\borganised\b', 'organized'),
    (r'\borganises\b', 'organizes'),
    (r'\borganising\b', 'organizing'),
    (r'\borganisation\b', 'organization'),
    (r'\borganisations\b', 'organizations'),
    (r'\bOrganise\b', 'Organize'),
    (r'\bOrganised\b', 'Organized'),
    (r'\bOrganises\b', 'Organizes'),
    (r'\bOrganising\b', 'Organizing'),
    (r'\bOrganisation\b', 'Organization'),
    (r'\bOrganisations\b', 'Organizations'),
    # realise/realised → realize/realized
    (r'\brealise\b', 'realize'),
    (r'\brealised\b', 'realized'),
    (r'\bRealise\b', 'Realize'),
    (r'\bRealised\b', 'Realized'),
    # minimise/maximise/optimise/normalise/standardise/serialise/centralise/utilise/specialise/initialise
    (r'\bminimise\b', 'minimize'),
    (r'\bmaximise\b', 'maximize'),
    (r'\boptimise\b', 'optimize'),
    (r'\bnormalise\b', 'normalize'),
    (r'\bstandardise\b', 'standardize'),
    (r'\bserialise\b', 'serialize'),
    (r'\bcentralise\b', 'centralize'),
    (r'\butilise\b', 'utilize'),
    (r'\bspecialise\b', 'specialize'),
    (r'\binitialise\b', 'initialize'),
    (r'\bMinimise\b', 'Minimize'),
    (r'\bMaximise\b', 'Maximize'),
    (r'\bOptimise\b', 'Optimize'),
    (r'\bNormalise\b', 'Normalize'),
    (r'\bStandardise\b', 'Standardize'),
    (r'\bSerialise\b', 'Serialize'),
    (r'\bCentralise\b', 'Centralize'),
    (r'\bUtilise\b', 'Utilize'),
    (r'\bSpecialise\b', 'Specialize'),
    (r'\bInitialise\b', 'Initialize'),
    # analyse/analysed/analyses/analysing → analyze/…
    (r'\banalyse\b', 'analyze'),
    (r'\banalysed\b', 'analyzed'),
    (r'\banalyses\b(?!.*\bstat)', 'analyzes'),  # careful: "analyses" can be noun plural too
    (r'\banalysing\b', 'analyzing'),
    (r'\bAnalyse\b', 'Analyze'),
    (r'\bAnalysed\b', 'Analyzed'),
    (r'\bAnalysing\b', 'Analyzing'),
    # customise/customised → customize/customized
    (r'\bcustomise\b', 'customize'),
    (r'\bcustomised\b', 'customized'),
    (r'\bCustomise\b', 'Customize'),
    (r'\bCustomised\b', 'Customized'),
]

total_changes = 0

for fpath in sorted(files):
    original = fpath.read_text(encoding="utf-8")
    updated = original
    file_changes = 0

    for pattern, replacement in REPLACEMENTS:
        new_text = re.sub(pattern, replacement, updated)
        count = len(re.findall(pattern, updated))
        if count:
            file_changes += count
            total_changes += count
        updated = new_text

    if updated != original:
        fpath.write_text(updated, encoding="utf-8")
        print(f"  ✅  {fpath}  ({file_changes} change{'s' if file_changes != 1 else ''})")
    else:
        print(f"  —   {fpath}  (no changes)")

print(f"\nTotal changes: {total_changes}")
