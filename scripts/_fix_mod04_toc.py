import os

BASE = "pages/track_01_python_foundation/mod_04_python_best_practices"

LESSONS = [
    ("lesson01_creating_your_own_modules.html",          "1. Creating Your Own Modules"),
    ("lesson02_project_folder_structure.html",           "2. Project Folder Structure"),
    ("lesson03_introduction_to_git_simple_workflow.html","3. Introduction to Git (Simple Workflow)"),
    ("lesson04_git_in_vs_code.html",                     "4. Git in VS Code"),
    ("lesson05_logging_basics.html",                     "5. Logging Basics"),
]

ACTIVE_LINK  = 'bg-[#fdf0f7] border-[#CB187D] text-[#CB187D]'
INACTIVE_LINK = 'bg-white border-gray-100 text-gray-600 hover:border-gray-200'
ACTIVE_DOT   = 'bg-[#CB187D]'
INACTIVE_DOT = 'bg-gray-300'

def make_toc_list(active_file):
    items = []
    for filename, label in LESSONS:
        is_active = (filename == active_file)
        link_cls  = ACTIVE_LINK  if is_active else INACTIVE_LINK
        dot_cls   = ACTIVE_DOT   if is_active else INACTIVE_DOT
        items.append(
            f'<a href="{filename}" class="flex items-center gap-2 px-3 py-2 rounded-lg border {link_cls} text-xs font-medium no-underline transition-colors">\n'
            f'  <span class="w-2 h-2 rounded-full {dot_cls} shrink-0"></span>\n'
            f'  <span class="truncate">{label}</span>\n'
            f'</a>'
        )
    return '<div class="space-y-1">' + '\n'.join(items) + '\n</div>'

MARKER = '<div class="space-y-1">'

for filename, _ in LESSONS:
    path = os.path.join(BASE, filename)
    html = open(path).read()

    if MARKER not in html:
        print(f'❌ {filename} — marker not found')
        continue

    start = html.index(MARKER)
    # Find the closing </div> — no nested <div>s inside, so first </div> is correct
    end = html.index('</div>', start + len(MARKER)) + len('</div>')

    old_block = html[start:end]
    new_block = make_toc_list(filename)
    new_html  = html[:start] + new_block + html[end:]

    open(path, 'w').write(new_html)
    print(f'✅ {filename}')
    # Show the active entry for confirmation
    for fn, label in LESSONS:
        marker = ACTIVE_LINK
        if fn == filename and marker in new_block:
            print(f'   active → {label}')

print('\nDone.')
