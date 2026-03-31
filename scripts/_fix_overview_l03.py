"""Replace the #overview section body in lesson03_attributes_methods.html."""

TARGET = "pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson03_attributes_methods.html"

OLD = """    <div class="bg-white px-8 py-7 space-y-5"><div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
  <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Py</span>
  <div class="relative flex items-start gap-4">
    <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0 mt-0.5">
      <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>
    </span>
    <p class="text-base text-gray-800 leading-relaxed font-medium">In the previous lesson, you learned how to create a class and initialize it using the constructor <code class="text-[11px] bg-white px-1.5 py-0.5 rounded font-mono border border-gray-100">__init__</code>.</p>
  </div>
</div>
<p class="text-sm text-gray-600 leading-relaxed">Example class:</p>
<div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
  <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
    <div class="flex items-center gap-3">
      <div class="flex gap-1.5">
        <span class="w-2.5 h-2.5 rounded-full bg-red-400/80"></span>
        <span class="w-2.5 h-2.5 rounded-full bg-amber-400/80"></span>
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-400/80"></span>
      </div>
      <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
        <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
        <span class="text-[11px] font-semibold text-gray-400">script.py</span>
      </div>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
  </div>
  <div class="bg-code">
    <pre class="overflow-x-auto pre-reset"><code class="language-python">class Customer:

    def __init__(self, name, city):
        self.name = name
        self.city = city</code></pre>
  </div>
</div>
<p class="text-sm text-gray-600 leading-relaxed">Here the class stores attributes:</p>
<div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5"><div class="flex items-center gap-2.5 rounded-lg bg-gray-50 border border-gray-100 px-3 py-2.5">
  <span class="iconify text-brand text-sm shrink-0" data-icon="fa6-solid:table"></span>
  <span class="text-xs text-gray-600">name</span>
</div>
<div class="flex items-center gap-2.5 rounded-lg bg-gray-50 border border-gray-100 px-3 py-2.5">
  <span class="iconify text-brand text-sm shrink-0" data-icon="fa6-solid:robot"></span>
  <span class="text-xs text-gray-600">city</span>
</div>
</div>
<p class="text-sm text-gray-600 leading-relaxed">Attributes represent <strong>data stored inside an object</strong>.</p>
<p class="text-sm text-gray-600 leading-relaxed">Now we can add <strong>methods</strong>, which are functions that operate on that data.</p>
<p class="text-sm text-gray-600 leading-relaxed">Example:</p>
<div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
  <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
    <div class="flex items-center gap-3">
      <div class="flex gap-1.5">
        <span class="w-2.5 h-2.5 rounded-full bg-red-400/80"></span>
        <span class="w-2.5 h-2.5 rounded-full bg-amber-400/80"></span>
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-400/80"></span>
      </div>
      <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
        <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
        <span class="text-[11px] font-semibold text-gray-400">script.py</span>
      </div>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
  </div>
  <div class="bg-code">
    <pre class="overflow-x-auto pre-reset"><code class="language-python">class Customer:

    def __init__(self, name, city):
        self.name = name
        self.city = city

    def greet(self):
        return f&quot;Hello {self.name}&quot;</code></pre>
  </div>
</div>
<p class="text-sm text-gray-600 leading-relaxed">Now objects created from this class can run methods.</p>
<p class="text-sm text-gray-600 leading-relaxed">Example:</p>
<div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
  <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
    <div class="flex items-center gap-3">
      <div class="flex gap-1.5">
        <span class="w-2.5 h-2.5 rounded-full bg-red-400/80"></span>
        <span class="w-2.5 h-2.5 rounded-full bg-amber-400/80"></span>
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-400/80"></span>
      </div>
      <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
        <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
        <span class="text-[11px] font-semibold text-gray-400">script.py</span>
      </div>
    </div>
    <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
  </div>
  <div class="bg-code">
    <pre class="overflow-x-auto pre-reset"><code class="language-python">customer = Customer(&quot;Alice&quot;, &quot;Los Angeles&quot;)

print(customer.greet())</code></pre>
  </div>
</div>
<p class="text-sm text-gray-600 leading-relaxed">Output:</p>
<div class="flex flex-wrap items-center gap-2 py-3"><span class="inline-flex items-center gap-1 px-3 py-1.5 rounded-full text-xs font-medium bg-[#fdf0f7] text-[#CB187D] border border-[#f5c6e0]">Hello Alice</span></div>
<p class="text-sm text-gray-600 leading-relaxed">Attributes store information, while methods allow objects to <strong>perform actions</strong>.</p></div>
  </div>
</section>"""

NEW = """    <div class="bg-white px-8 py-7 space-y-5">

      <!-- Part 1 — Hook quote banner -->
      <div class="relative rounded-2xl border border-[#f5c6e0] bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 overflow-hidden">
        <span class="absolute -right-3 -top-3 text-[5rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">Py</span>
        <div class="relative flex items-center gap-4">
          <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white shadow-md shrink-0">
            <span class="iconify text-base" data-icon="fa6-solid:quote-left"></span>
          </span>
          <p class="text-base text-gray-800 leading-relaxed font-medium">Every object in Python has two things: data it remembers and actions it can perform.</p>
        </div>
      </div>

      <!-- Part 2 — Analogy intro paragraph -->
      <p class="text-sm text-gray-600 leading-relaxed">Think of a vending machine: each one stores its own data — the item name, the price, how many are left — and it knows how to do things, like dispense an item or calculate your change. In Python, stored data is called an <strong>attribute</strong> and a built-in action is called a <strong>method</strong>.</p>

      <!-- Part 3 — Analogy card grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">

        <!-- Card 1 — pink accent: Attribute -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-[#f5c6e0] hover:bg-[#fdf0f7]/40 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-[#fdf0f7] shrink-0">
              <span class="iconify text-brand text-base" data-icon="fa6-solid:database"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Attribute</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The display screen — shows what this machine stores</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">The screen shows only this machine's own name, price, and stock count.</p>
        </div>

        <!-- Card 2 — violet accent: Method -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-violet-100 hover:bg-violet-50/30 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-violet-50 shrink-0">
              <span class="iconify text-violet-500 text-base" data-icon="fa6-solid:wrench"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Method</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">The button panel — each button triggers one action</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">Each button makes the machine carry out exactly one specific job.</p>
        </div>

        <!-- Card 3 — blue accent: Object Memory -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-blue-100 hover:bg-blue-50/30 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-blue-50 shrink-0">
              <span class="iconify text-blue-500 text-base" data-icon="fa6-solid:box-archive"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Object Memory</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">Each machine stands alone — its own stock, its own data</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">Two machines of the same model can hold completely different item counts.</p>
        </div>

        <!-- Card 4 — emerald accent: Data-driven actions -->
        <div class="rounded-xl border border-gray-100 bg-gray-50 px-4 py-4 hover:border-emerald-100 hover:bg-emerald-50/30 transition-colors">
          <div class="flex items-center gap-3 mb-2.5">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-emerald-50 shrink-0">
              <span class="iconify text-emerald-500 text-base" data-icon="fa6-solid:gears"></span>
            </span>
            <div>
              <p class="text-sm font-bold text-gray-800 leading-tight">Methods Use Data</p>
              <p class="text-[10px] text-gray-400 italic leading-tight">Press buy — the machine checks its own screen first</p>
            </div>
          </div>
          <p class="text-xs text-gray-500 leading-relaxed">Every action the machine takes pulls from its own stored figures.</p>
        </div>

      </div>

      <!-- Part 4 — Amber tip -->
      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">If you already use Excel, think of attributes as the values in a row and methods as the formulas that calculate with them — Python bundles both together inside one object.</p>
      </div>

    </div>
  </div>
</section>"""

with open(TARGET, "r", encoding="utf-8") as f:
    content = f.read()

if OLD in content:
    content = content.replace(OLD, NEW, 1)
    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ #overview section replaced successfully")
else:
    print("❌ OLD string not found — check for whitespace or encoding differences")
