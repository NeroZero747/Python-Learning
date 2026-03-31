"""Replace #next-lesson section and bottom nav in lesson02 with prompt-compliant templates."""

filepath = "pages/track_01/mod_02_programming_foundations/lesson02_variables_data_types.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Find the #next-lesson section start
nl_pos = content.find('<section id="next-lesson">')
# Find the body div inside it
body_start = content.find('    <div class="bg-white px-8 py-7 space-y-4">', nl_pos)
# Find the END of the section
section_end = content.find('</section>', body_start) + len('</section>')

# Find the old bottom nav div (immediately after next-lesson section)
old_nav_start = content.find('\n\n\n        <div class="flex flex-col sm:flex-row gap-3 mt-6">', section_end)
if old_nav_start == -1:
    old_nav_start = content.find('\n\n        <div class="flex flex-col sm:flex-row gap-3 mt-6">', section_end)
if old_nav_start == -1:
    old_nav_start = content.find('<div class="flex flex-col sm:flex-row gap-3 mt-6">', section_end)

old_nav_end_tag = '</div>'
old_nav_end = content.find('      </main>', old_nav_start)

print("nl_pos:", nl_pos)
print("body_start:", body_start)
print("section_end:", section_end)
print("old_nav_start:", old_nav_start)
print("old_nav_end:", old_nav_end)

# --- NEW #next-lesson section body ---
NEW_SECTION_BODY = """    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Lesson badge -->
      <div class="flex items-center gap-4 rounded-xl border border-gray-100 bg-[#fdf0f7] px-5 py-4">
        <span class="inline-flex items-center justify-center w-12 h-12 rounded-xl bg-[#CB187D] shrink-0">
          <span class="text-white font-bold text-lg">3</span>
        </span>
        <div class="min-w-0">
          <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-0.5">Module 2 &middot; Lesson 3</p>
          <h3 class="text-base font-bold text-gray-800">Additional Python Data Types</h3>
          <p class="text-sm text-gray-500 mt-0.5">Next you will learn:</p>
        </div>
      </div>

      <!-- Preview card grid -->
      <div>
        <p class="text-xs font-bold uppercase tracking-widest text-brand mb-3">What You Will Learn</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:list-ol"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Tuples &amp; Ordered Fixed Collections</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:layer-group"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">Sets &amp; Unique Value Groups</p>
            </div>
          </div>

          <div class="obj-card flex items-center gap-3 rounded-xl border border-gray-100 px-4 py-3 bg-gray-50">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#CB187D] shrink-0">
              <span class="iconify text-white text-sm" data-icon="fa6-solid:circle-xmark"></span>
            </span>
            <div>
              <p class="text-sm font-semibold text-gray-700">The None Type &amp; What It Represents</p>
            </div>
          </div>

        </div>
      </div>

    </div>
  </div>
</section>"""

# --- NEW bottom nav section ---
NEW_NAV = """
<section>
  <div class="flex flex-col sm:flex-row gap-3">

    <!-- Previous lesson -->
    <a href="lesson01_what_is_programming.html" class="lesson-nav-link group flex-1 flex items-center gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all">
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-left"></span>
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Previous</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">What Is Programming?</p>
      </div>
    </a>

    <!-- All Lessons -->
    <a href="../../../hub_home_page.html" class="lesson-nav-link group flex items-center justify-center gap-2 rounded-2xl bg-transparent px-6 py-5 transition-all sm:w-auto w-full">
      <span class="iconify text-gray-400 text-base group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:table-cells-large"></span>
      <span class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors whitespace-nowrap">All Lessons</span>
    </a>

    <!-- Next lesson -->
    <a href="lesson03_additional_python_data_types.html" class="lesson-nav-link group flex-1 flex items-center justify-end gap-4 rounded-2xl bg-transparent px-6 py-5 transition-all text-right">
      <div class="min-w-0">
        <p class="text-xs font-semibold uppercase tracking-widest text-gray-400 group-hover:text-[#CB187D] transition-colors mb-0.5">Next</p>
        <p class="text-sm font-bold text-gray-700 group-hover:text-[#CB187D] transition-colors truncate">Additional Python Data Types</p>
      </div>
      <span class="iconify text-gray-300 text-xl shrink-0 group-hover:text-[#CB187D] transition-colors" data-icon="fa6-solid:arrow-right"></span>
    </a>

  </div>
</section>
"""

# Splice: replace section body + kill old section end, then replace old nav
# Step 1: replace the next-lesson body and close the section
new_content = content[:body_start] + NEW_SECTION_BODY

# Step 2: find where the old nav div ends (just before </main>)
remainder = content[section_end:]
main_pos = remainder.find('      </main>')
old_nav_block = remainder[:main_pos]  # this is the old nav + whitespace
new_content += "\n\n" + NEW_NAV + "\n      </main>" + content[section_end + main_pos + len('      </main>'):]

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

# Verify
with open(filepath, "r", encoding="utf-8") as f:
    v = f.read()

ok = (
    'scroll-mt-24' not in v[v.find('<section id="next-lesson"'):v.find('<section id="next-lesson"')+50]  # section exists
    and "Module 2 &middot; Lesson 3" in v
    and "Tuples &amp; Ordered Fixed Collections" in v
    and "Sets &amp; Unique Value Groups" in v
    and "The None Type &amp; What It Represents" in v
    and "fa6-solid:table-cells-large" in v
    and "fa6-solid:arrow-left" in v
    and "fa6-solid:arrow-right" in v
    and "What Is Programming?" in v
    and "hub_home_page.html" in v
    and "mt-6" not in v[v.find('</section>\n\n<section>\n'):v.find('</section>\n\n<section>\n')+200]
)

print("SUCCESS" if ok else "NEEDS CHECK")
print("  lesson badge:", "Module 2 &middot; Lesson 3" in v)
print("  card 1 (tuples):", "Tuples &amp;" in v)
print("  card 2 (sets):", "Sets &amp;" in v)
print("  card 3 (none):", "None Type &amp;" in v)
print("  hub link:", "hub_home_page.html" in v)
print("  prev arrow:", "fa6-solid:arrow-left" in v)
print("  next arrow:", "fa6-solid:arrow-right" in v)
print("  all lessons:", "fa6-solid:table-cells-large" in v)
print("  old mt-6 nav gone:", 'mt-6">' not in v)
