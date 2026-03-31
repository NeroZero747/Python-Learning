"""Replace the #decision-flow body div in lesson03_attributes_methods.html."""
import re, pathlib

TARGET = pathlib.Path(
    "pages/track_01_python_foundation/mod_03_object_oriented_programming/"
    "lesson03_attributes_methods.html"
)

NEW_BODY = '''    <div class="bg-white px-8 py-7 space-y-6">

      <!-- Block 1: Intro paragraph -->
      <p class="text-sm text-gray-600 leading-relaxed">When you write your first Python class, three things happen in a strict, fixed order: you define the blueprint, you create objects from it, and then you call methods on those objects. This sequence — <strong class="text-gray-800">define → create → call</strong> — never changes, and Python reads it top to bottom, like a technician following a step-by-step protocol.</p>

      <!-- Block 2: Flowchart -->
      <div class="rounded-2xl border border-gray-100 bg-gray-50 px-5 pt-4 pb-6 overflow-x-auto">
        <p class="text-[10px] font-bold uppercase tracking-widest text-gray-400 mb-4">How Python Reads a Class — Top to Bottom</p>
        <div class="flex items-start gap-0 min-w-[640px]">

          <!-- Node 1: Program Starts -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-14 h-14 rounded-full bg-gradient-to-br from-pink-500 to-rose-600 flex items-center justify-center shadow-lg ring-4 ring-pink-100">
              <span class="iconify text-white text-lg" data-icon="fa6-solid:play"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-2 text-center leading-tight">Program<br>Starts</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">Python begins at line 1</p>
          </div>

          <!-- Arrow 1 → 2 -->
          <div class="flex-1 flex items-center" style="padding-top:28px;">
            <div class="h-0.5 flex-1 bg-gradient-to-r from-pink-300 to-violet-300"></div>
            <span class="iconify text-violet-300 text-xs -ml-px" data-icon="fa6-solid:chevron-right"></span>
          </div>

          <!-- Node 2: Define the Class (violet rounded square) -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-violet-500 to-purple-600 flex items-center justify-center shadow-lg ring-4 ring-violet-100">
              <span class="iconify text-white text-lg" data-icon="fa6-solid:pen-to-square"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-2 text-center leading-tight">Define<br>the Class</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">class HealthRecord:</p>
          </div>

          <!-- Arrow 2 → 3 -->
          <div class="flex-1 flex items-center" style="padding-top:28px;">
            <div class="h-0.5 flex-1 bg-gradient-to-r from-violet-300 to-blue-300"></div>
            <span class="iconify text-blue-300 text-xs -ml-px" data-icon="fa6-solid:chevron-right"></span>
          </div>

          <!-- Node 3: Create an Object (blue diamond) -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-12 h-12 rounded-xl rotate-45 bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center shadow-lg ring-4 ring-blue-100" style="margin-top:4px;">
              <span class="iconify text-white text-base -rotate-45" data-icon="fa6-solid:cube"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-3 text-center leading-tight">Create<br>an Object</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">__init__ runs automatically</p>
          </div>

          <!-- Arrow 3 → 4 -->
          <div class="flex-1 flex items-center" style="padding-top:28px;">
            <div class="h-0.5 flex-1 bg-gradient-to-r from-blue-300 to-emerald-300"></div>
            <span class="iconify text-emerald-300 text-xs -ml-px" data-icon="fa6-solid:chevron-right"></span>
          </div>

          <!-- Node 4: Call a Method (emerald rounded square) -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-emerald-500 to-teal-600 flex items-center justify-center shadow-lg ring-4 ring-emerald-100">
              <span class="iconify text-white text-lg" data-icon="fa6-solid:bolt"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-2 text-center leading-tight">Call<br>a Method</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">reads self to do its job</p>
          </div>

          <!-- Arrow 4 → 5 -->
          <div class="flex-1 flex items-center" style="padding-top:28px;">
            <div class="h-0.5 flex-1 bg-gradient-to-r from-emerald-300 to-gray-300"></div>
            <span class="iconify text-gray-300 text-xs -ml-px" data-icon="fa6-solid:chevron-right"></span>
          </div>

          <!-- Node 5: Program Ends -->
          <div class="flex flex-col items-center shrink-0" style="width:115px;">
            <div class="w-14 h-14 rounded-full bg-gradient-to-br from-gray-400 to-gray-600 flex items-center justify-center shadow-lg ring-4 ring-gray-100">
              <span class="iconify text-white text-lg" data-icon="fa6-solid:flag-checkered"></span>
            </div>
            <p class="text-[10px] font-bold text-gray-800 mt-2 text-center leading-tight">Program<br>Ends</p>
            <p class="text-[9px] text-gray-400 text-center mt-1 leading-tight">Result is shown</p>
          </div>

        </div>
      </div>

      <!-- Block 3: Sequential explanation -->
      <div class="space-y-2">
        <p class="text-sm font-semibold text-gray-800">Class-First Order — Python Reads the Blueprint Before Using It</p>
        <p class="text-sm text-gray-600 leading-relaxed">Python reads your class definition the instant your file runs, before any object is created. That means the <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">class</code> block at the top of your file must exist before you can write <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">HealthRecord(...)</code> below it. If you try to create an object before defining its class, Python stops immediately with a <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">NameError</code>.</p>
      </div>

      <!-- Block 4: Code block -->
      <div class="space-y-2">
        <p class="text-sm text-gray-600 leading-relaxed">Read the comment on every line — each one labels exactly which step in the diagram above is happening at that moment:</p>
        <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
          <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
            <div class="flex items-center gap-3">
              <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                <span class="text-[11px] font-semibold text-gray-400">healthcare.py</span>
              </div>
            </div>
            <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
          </div>
          <div class="bg-code">
            <pre class="overflow-x-auto pre-reset"><code class="language-python">class HealthRecord:                           # Step 1 — define the blueprint
    def __init__(self, member_id, plan_type): # Step 2 — set starting values for every new object
        self.member_id = member_id            # attach member_id to this specific object
        self.plan_type = plan_type            # attach plan_type to this specific object
        self.is_active = True                 # every new record starts as active

    def check_eligibility(self):              # Step 3 — write a method (defined, not called yet)
        return self.is_active                 # reads this object's own is_active value

record = HealthRecord("M-001", "Gold")        # Step 4 — create one object; __init__ runs now
print(record.check_eligibility())             # Step 5 — call the method; returns True</code></pre>
          </div>
          <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
            <div class="flex items-center gap-2 mb-1.5">
              <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
              <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
              <span class="text-[10px] text-gray-600 font-mono">$ python healthcare.py</span>
            </div>
            <div class="font-mono text-xs text-emerald-400 leading-relaxed">True</div>
          </div>
        </div>
      </div>

      <!-- Block 5: Three concept cards -->
      <div class="space-y-3">
        <p class="text-xs font-bold uppercase tracking-widest text-brand">The Three Building Blocks of Every Class</p>
        <p class="text-sm text-gray-600 leading-relaxed">Every Python class uses these three ideas together — none of them works correctly without the other two.</p>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">

          <!-- Card 1: Attributes (blue) -->
          <div class="rounded-xl border border-blue-100 bg-white overflow-hidden shadow-sm hover:shadow-md hover:border-blue-200 transition-all">
            <div class="h-1 bg-gradient-to-r from-blue-500 to-blue-400"></div>
            <div class="px-4 py-4">
              <div class="flex items-center gap-2.5 mb-2.5">
                <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-blue-50 shrink-0">
                  <span class="iconify text-blue-500 text-base" data-icon="fa6-solid:database"></span>
                </span>
                <div>
                  <p class="text-sm font-bold text-gray-800 leading-tight">Attributes</p>
                  <p class="text-[10px] text-gray-400 italic leading-tight">The object's memory</p>
                </div>
              </div>
              <p class="text-xs text-gray-500 leading-relaxed">An attribute is a variable that belongs to one specific object. You create every attribute by writing <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">self.name = value</code> inside <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">__init__</code>, and each object remembers its own separate copy forever.</p>
            </div>
          </div>

          <!-- Card 2: Methods (emerald) -->
          <div class="rounded-xl border border-emerald-100 bg-white overflow-hidden shadow-sm hover:shadow-md hover:border-emerald-200 transition-all">
            <div class="h-1 bg-gradient-to-r from-emerald-500 to-emerald-400"></div>
            <div class="px-4 py-4">
              <div class="flex items-center gap-2.5 mb-2.5">
                <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-emerald-50 shrink-0">
                  <span class="iconify text-emerald-500 text-base" data-icon="fa6-solid:bolt"></span>
                </span>
                <div>
                  <p class="text-sm font-bold text-gray-800 leading-tight">Methods</p>
                  <p class="text-[10px] text-gray-400 italic leading-tight">The built-in actions</p>
                </div>
              </div>
              <p class="text-xs text-gray-500 leading-relaxed">A method is a function defined inside a class. It always receives <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">self</code> as its first parameter so it can read and update the object's stored attributes whenever it runs.</p>
            </div>
          </div>

          <!-- Card 3: Objects (violet) -->
          <div class="rounded-xl border border-violet-100 bg-white overflow-hidden shadow-sm hover:shadow-md hover:border-violet-200 transition-all">
            <div class="h-1 bg-gradient-to-r from-violet-500 to-violet-400"></div>
            <div class="px-4 py-4">
              <div class="flex items-center gap-2.5 mb-2.5">
                <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-violet-50 shrink-0">
                  <span class="iconify text-violet-500 text-base" data-icon="fa6-solid:box"></span>
                </span>
                <div>
                  <p class="text-sm font-bold text-gray-800 leading-tight">Objects</p>
                  <p class="text-[10px] text-gray-400 italic leading-tight">One filled-in copy of the blueprint</p>
                </div>
              </div>
              <p class="text-xs text-gray-500 leading-relaxed">An object is one live instance of your class, created by calling the class name like a function: <code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">record = HealthRecord(...)</code>. Each object holds its own independent data and can call any method the class defines.</p>
            </div>
          </div>

        </div>
      </div>

      <!-- Block 6: Amber tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">Every class you write follows three layers: the blueprint (<code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">class</code>), the data setup (<code class="text-xs font-mono px-1 py-0.5 rounded bg-gray-100 text-gray-700">__init__</code>), and the actions (methods). Build these three layers in order and your code will always be easy to read, test, and reuse.</p>
      </div>

    </div>'''

content = TARGET.read_text(encoding="utf-8")

# Match the body div of #decision-flow only, stopping before </div>\n  </div>\n</section>
pattern = re.compile(
    r'(?<=<section id="decision-flow">\n  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">\n)'
    r'.*?'              # section header (non-greedy)
    r'(<div class="bg-white px-8 py-7 space-y-5">.*?</div>)\s*\n'
    r'(?=  </div>\n</section>)',
    re.DOTALL,
)

# Simpler approach: find decision-flow section and replace its body div
section_pat = re.compile(
    r'(<section id="decision-flow">.*?)'           # opening + header
    r'<div class="bg-white px-8 py-7[^"]*">.*?</div>'  # old body div (innermost close)
    r'(\s*\n\s*</div>\s*\n</section>)',            # outer wrapper close + section close
    re.DOTALL,
)

match = section_pat.search(content)
if not match:
    print("❌ Could not locate #decision-flow body div — pattern did not match")
    exit(1)

# Validate we matched the right section
if 'Define class' not in match.group(0) and 'customer = Customer' not in match.group(0):
    print("⚠️  Match did not contain expected old content — proceeding cautiously")

old_len = len(match.group(0))
new_section = match.group(1) + NEW_BODY + match.group(2)
content_new = content[:match.start()] + new_section + content[match.end():]

TARGET.write_text(content_new, encoding="utf-8")
print(f"✅ Replaced #decision-flow body div ({old_len} chars → {len(new_section)} chars)")

# Verify
if 'Define the Class' in content_new and 'Create an Object' in content_new:
    print("✅ Flowchart nodes verified in output")
if 'healthcare.py' in content_new:
    print("✅ Code block filename verified")
