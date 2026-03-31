"""Verify #recap mirrors the #objective section exactly."""
import re, pathlib

html = pathlib.Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices/"
    "lesson01_creating_your_own_modules.html"
).read_text()

m = re.search(r'<section id="recap">(.*?)</section>', html, re.DOTALL)
sec = m.group(1)

obj_labels = ["What a Module Is", "Splitting Code into Files",
              "Organizing Larger Projects", "Importing from a Module"]
obj_icons  = ["fa6-solid:cube", "fa6-solid:file-code",
              "fa6-solid:folder-tree", "fa6-solid:arrow-right-to-bracket"]

checks = [
    ("section id recap",          'id="recap"' in html),
    ("header icon list-check",    'fa6-solid:list-check' in sec),
    ("header title Lesson Recap", '>Lesson Recap<' in sec),
    ("body class space-y-6",      'bg-white px-8 py-7 space-y-6' in sec),

    ("card1 label exact",         obj_labels[0] in sec),
    ("card2 label exact",         obj_labels[1] in sec),
    ("card3 label exact",         obj_labels[2] in sec),
    ("card4 label exact",         obj_labels[3] in sec),

    ("card1 icon cube",                       obj_icons[0] in sec),
    ("card2 icon file-code",                  obj_icons[1] in sec),
    ("card3 icon folder-tree",                obj_icons[2] in sec),
    ("card4 icon arrow-right-to-bracket",     obj_icons[3] in sec),

    ("watermark 01",              '>01<' in sec),
    ("watermark 02",              '>02<' in sec),
    ("watermark 03",              '>03<' in sec),
    ("watermark 04",              '>04<' in sec),

    ("label style uppercase",     'text-xs font-bold uppercase tracking-widest text-[#CB187D]' in sec),
    ("sentence style text-11px",  'text-[11px] text-gray-600 leading-snug' in sec),
    ("inline code used",          '<code class="font-mono">' in sec),
    ("4 gradient icon badges",    sec.count('from-[#CB187D] to-[#e84aad] text-white shadow-md') == 4),

    ("completion banner trophy",  'fa6-solid:trophy' in sec),
    ("covered 4 key concepts",    "You&#39;ve covered 4 key concepts" in sec),
    ("no old check icons",        sec.count('data-icon="fa6-solid:check"') == 0),
]

passed = sum(1 for _, v in checks if v)
total = len(checks)
print(f"Recap verify — {passed}/{total} checks\n")
for name, ok in checks:
    print(f"  {'OK' if ok else 'FAIL'} {name}")
print(f"\n{'All checks passed.' if passed == total else str(total - passed) + ' failed.'}")
