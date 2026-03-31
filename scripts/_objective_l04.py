TARGET = r'c:\Users\nightwolf\Projects\Python-Learning\pages\track_01_python_foundation\mod_04_python_best_practices\lesson04_logging_basics.html'

NEW_SECTION = '''<section id="objective">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:bullseye"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Lesson Objective</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">The goal and expected outcome of this lesson</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">

        <!-- Card 1 -->
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:scroll"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">What logging is</p>
            <p class="text-xs text-gray-500 mt-0.5">Logging records events inside your program so you can review what happened after the fact.</p>
          </div>
        </div>

        <!-- Card 2 -->
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:triangle-exclamation"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Logging levels explained</p>
            <p class="text-xs text-gray-500 mt-0.5">You will set severity levels — DEBUG, INFO, WARNING, ERROR, CRITICAL — to control which messages appear.</p>
          </div>
        </div>

        <!-- Card 3 -->
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:file-lines"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Writing logs to a file</p>
            <p class="text-xs text-gray-500 mt-0.5">You will configure Python's logging module to save messages to a file your team can inspect later.</p>
          </div>
        </div>

        <!-- Card 4 -->
        <div class="obj-card flex items-start gap-4 rounded-xl border border-gray-100 bg-gray-50 px-4 py-4">
          <span class="obj-icon inline-flex items-center justify-center w-10 h-10 rounded-xl bg-brand-soft shrink-0">
            <span class="iconify text-brand text-lg" data-icon="fa6-solid:bug-slash"></span>
          </span>
          <div>
            <p class="text-sm font-semibold text-gray-800">Replacing print with logging</p>
            <p class="text-xs text-gray-500 mt-0.5">You will swap ad-hoc print statements for structured log calls that are easier to filter and turn off.</p>
          </div>
        </div>

      </div>
      <div class="mt-5">
        <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
          <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
          <p class="text-sm text-gray-600">This lesson gives you a practical logging setup you can drop into any Python script to make debugging and monitoring straightforward from day one.</p>
        </div>
      </div>
    </div>
  </div>
</section>'''

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('<section id="objective">')
end   = content.find('</section>', start) + len('</section>')

if start == -1:
    print('ERROR: #objective section not found')
else:
    new_content = content[:start] + NEW_SECTION + content[end:]
    with open(TARGET, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Written successfully.')

    # Verify
    with open(TARGET, 'r', encoding='utf-8') as f:
        result = f.read()
    s2 = result.find('<section id="objective">')
    e2 = result.find('</section>', s2) + len('</section>')
    section = result[s2:e2]
    checks = [
        ('4 obj-cards', section.count('obj-card') == 4),
        ('4 descriptions', section.count('text-xs text-gray-500 mt-0.5') == 4),
        ('fa6-solid:scroll', 'fa6-solid:scroll' in section),
        ('fa6-solid:triangle-exclamation', 'fa6-solid:triangle-exclamation' in section),
        ('fa6-solid:file-lines', 'fa6-solid:file-lines' in section),
        ('fa6-solid:bug-slash', 'fa6-solid:bug-slash' in section),
        ('Amber tip present', 'bg-amber-tip' in section),
        ('Amber starts with This lesson', 'This lesson gives you' in section),
        ('No broken tip text', 'By the end of this lesson' not in section),
    ]
    print()
    all_ok = True
    for label, ok in checks:
        print(f'  {"OK  " if ok else "FAIL"}: {label}')
        if not ok: all_ok = False
    print('\n' + ('All checks passed.' if all_ok else 'Some checks FAILED.'))
