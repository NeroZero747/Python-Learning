"""Replace the #recap section body in lesson02 using positional splice."""

filepath = "pages/track_01/mod_02_programming_foundations/lesson02_variables_data_types.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

recap_pos = content.find('<section id="recap">')
body_start = content.find('    <div class="bg-white px-8 py-7 space-y-6">', recap_pos)
section_end = content.find('</section>', body_start) + len('</section>')

if body_start == -1 or section_end == len('</section>') - 1:
    print("ERROR: Could not find recap body markers")
    exit(1)

NEW = """    <div class="bg-white px-8 py-7 space-y-6">

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

        <!-- Card 01 -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:tag"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">What a variable is</p>
                <p class="text-sm text-gray-700 font-medium leading-relaxed">A named label that links a value in memory to a name you can use anywhere in your script.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 02 -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:database"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Storing values in Python</p>
                <p class="text-sm text-gray-700 font-medium leading-relaxed">Python links any value &#8212; a member ID, a claim total, a status flag &#8212; to the name on the left of the equals sign.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 03 -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:shapes"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Python&#39;s core data types</p>
                <p class="text-sm text-gray-700 font-medium leading-relaxed">Python classifies every value as text, a whole number, a decimal, or a true/false flag &#8212; each with its own behaviour.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 04 -->
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm hover:shadow-md hover:border-[#f5c6e0] transition-all duration-300">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-5 py-5 overflow-hidden">
            <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
            <div class="relative flex items-start gap-3">
              <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
                <span class="iconify text-sm" data-icon="fa6-solid:magnifying-glass"></span>
              </span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest text-[#CB187D] mb-1">Checking a value&#39;s type</p>
                <p class="text-sm text-gray-700 font-medium leading-relaxed">The type function returns what kind of value a variable holds, helping you catch mismatches before they cause errors.</p>
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- Completion banner -->
      <div class="relative rounded-2xl overflow-hidden bg-gradient-to-r from-[#CB187D] to-[#e84aad] px-6 py-5">
        <span class="absolute right-6 top-1/2 -translate-y-1/2 text-[4rem] font-black text-white/10 leading-none select-none pointer-events-none">&#10003;</span>
        <div class="relative flex items-center gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-white/20 backdrop-blur-sm shrink-0">
            <span class="iconify text-white text-lg" data-icon="fa6-solid:trophy"></span>
          </span>
          <div>
            <p class="text-sm font-bold text-white">Lesson Complete!</p>
            <p class="text-xs text-white/80 mt-0.5">You&#39;ve covered 4 key concepts. Ready for the knowledge check?</p>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>"""

new_content = content[:body_start] + NEW + content[section_end:]

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

# Verify
with open(filepath, "r", encoding="utf-8") as f:
    v = f.read()

ok = (
    "variables store values in Python" not in v
    and "What a variable is" in v
    and "Storing values in Python" in v
    and "Python&#39;s core data types" in v
    and "Checking a value&#39;s type" in v
    and "4 key concepts" in v
    and "5 key concepts" not in v
    and "fa6-solid:tag" in v
    and "fa6-solid:magnifying-glass" in v
)

if ok:
    print("SUCCESS: Recap section replaced — 4 objective-aligned cards written")
else:
    print("PARTIAL: Check individual markers below")
    print("  old card 1 gone:", "variables store values in Python" not in v)
    print("  card 1 present:", "What a variable is" in v)
    print("  card 2 present:", "Storing values in Python" in v)
    print("  card 3 present:", "Python&#39;s core data types" in v)
    print("  card 4 present:", "Checking a value&#39;s type" in v)
    print("  4 key concepts:", "4 key concepts" in v)
    print("  5 key concepts gone:", "5 key concepts" not in v)
