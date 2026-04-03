
FILE = r"pages\mod_03_python_for_data_analysts\lesson03_selecting_and_filtering_data.html"
with open(FILE, encoding="utf-8") as f:
    html = f.read()
orig = len(html)
patches = []

def patch(name, old, new):
    global html
    c = html.count(old)
    if c == 1:
        html = html.replace(old, new); patches.append("OK  " + name)
    elif c == 0:
        patches.append("MISS " + name)
    else:
        html = html.replace(old, new, 1); patches.append(f"DUP({c}) " + name)

# CHECK 2: Hero pill
patch("Check 2",
    '<span class="font-extrabold">4</span>',
    '<span class="font-extrabold">6</span>')

# CHECK 8: Banner
patch("Check 8",
    "You&#39;ve covered 4 key concepts.",
    "You&#39;ve covered 6 key concepts.")

# CHECK 14: CE tab5 button
patch("Check 11a",
    'class="ce-step-label text-xs font-bold">Filter with a List</span>
</button>
</div>
<div class="ce-panel ce-panel-anim" role="tabpanel">',
    '</div>
<div class="ce-panel ce-panel-anim" role="tabpanel">')

# CHECK 15: PE tab5 button
patch("Check 11b",
    'class="pe-step-label text-xs font-bold">Filter with a List</span>
</button>
</div>
<div class="pe-panel pe-panel-anim" role="tabpanel">',
    '</div>
<div class="pe-panel pe-panel-anim" role="tabpanel">')

with open(FILE, "w", encoding="utf-8") as f:
    f.write(html)
print(f"orig={orig} new={len(html)}")
for p in patches: print(p)
