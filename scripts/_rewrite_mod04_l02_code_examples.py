"""Rewrite the #code-examples section body in lesson02_project_folder_structure.html.

Examples:
  1. Create Project Folders  — os.makedirs() to scaffold the standard layout  (Reports)
  2. Write a Module          — def + return inside modules/cleaning.py          (Sales)
  3. Connect with main.py    — import + pipeline in the entry point             (Products)
"""

from pathlib import Path

TARGET = Path(
    "pages/track_01_python_foundation/mod_04_python_best_practices"
    "/lesson02_project_folder_structure.html"
)

NEW_BODY = """\
<div class="bg-white px-8 py-7 space-y-6">

<!-- ── Tab pill row ─────────────────────────────────────────── -->
<div class="flex items-center gap-2 mb-6" role="tablist">

  <button onclick="switchCeTab(0)" class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
    <span class="ce-step-label text-xs font-bold">Create Project Folders</span>
  </button>

  <button onclick="switchCeTab(1)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
    <span class="ce-step-label text-xs font-bold">Write a Module</span>
  </button>

  <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
    <span class="iconify text-[13px]" data-icon="fa6-solid:code"></span>
    <span class="ce-step-label text-xs font-bold">Connect with main.py</span>
  </button>

</div>

<!-- ════════════════════════════════════════════════════════════ -->
<!-- Panel 1 — Create Project Folders (visible)                  -->
<!-- ════════════════════════════════════════════════════════════ -->
<div class="ce-panel ce-panel-anim" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

    <!-- Panel header -->
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:code"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Create Project Folders</h3>
          <div class="flex items-center gap-2 mt-1">
            <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
              <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
            </span>
            <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Reports</span>
            <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">os.makedirs()</span>
            <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Project Setup</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Panel body -->
    <div class="px-6 py-5 space-y-4">

      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
          <p class="text-sm text-gray-600">This script uses Python&apos;s built-in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">os</code> module to create the standard project folders in one go. Run it once at the start of any new project and the structure is ready before you write a single line of analysis code.</p>
        </div>
      </div>

      <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
        <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
          <div class="flex items-center gap-3">
            <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
              <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
              <span class="text-[11px] font-semibold text-gray-400">setup_project.py</span>
            </div>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-python">import os                                        # os gives Python access to your file system

os.makedirs("data/raw", exist_ok=True)          # creates data/ then raw/ inside it
os.makedirs("data/processed", exist_ok=True)    # creates processed/ alongside raw/
os.makedirs("modules", exist_ok=True)           # creates the modules/ folder

print("Folders created successfully!")           # confirm the setup worked
print("Project root now contains:", os.listdir("."))  # list everything in the root</code></pre>
        </div>
        <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
          <div class="flex items-center gap-2 mb-1.5">
            <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
            <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
            <span class="text-[10px] text-gray-600 font-mono">$ python setup_project.py</span>
          </div>
          <div class="font-mono text-xs text-emerald-400 leading-relaxed">Folders created successfully!<br>Project root now contains: [&apos;data&apos;, &apos;modules&apos;, &apos;setup_project.py&apos;]</div>
        </div>
      </div>

      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">The <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">exist_ok=True</code> argument makes it safe to run this script again any time — Python won&apos;t raise an error if the folders already exist.</p>
      </div>

    </div>
  </div>
</div><!-- /panel 1 -->

<!-- ════════════════════════════════════════════════════════════ -->
<!-- Panel 2 — Write a Module (hidden)                           -->
<!-- ════════════════════════════════════════════════════════════ -->
<div class="ce-panel ce-panel-anim hidden" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

    <!-- Panel header -->
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:code"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Write a Module</h3>
          <div class="flex items-center gap-2 mt-1">
            <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
              <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
            </span>
            <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Sales</span>
            <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">def</span>
            <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">return</span>
            <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">modules/</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Panel body -->
    <div class="px-6 py-5 space-y-4">

      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
          <p class="text-sm text-gray-600">This script defines a reusable function and saves it as a <strong class="text-gray-800">module</strong> — a single file that handles one kind of task. Storing it in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">modules/</code> means any script in your project can import it without copy-pasting the code.</p>
        </div>
      </div>

      <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
        <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
          <div class="flex items-center gap-3">
            <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
              <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
              <span class="text-[11px] font-semibold text-gray-400">modules/cleaning.py</span>
            </div>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-python"># modules/cleaning.py — data-cleaning tasks for the whole project

def remove_blanks(data):                         # define a function that accepts a list
    clean_data = []                              # start with an empty list
    for value in data:                           # go through every item
        if value != "":                          # skip anything empty
            clean_data.append(value)             # keep the non-empty items
    return clean_data                            # send the cleaned list back to the caller

# --- quick test: only runs when this file is opened directly ---
sample = ["Alice", "", "Bob", "", "Carol"]       # test data with two blanks
print(remove_blanks(sample))                     # expected: [&apos;Alice&apos;, &apos;Bob&apos;, &apos;Carol&apos;]</code></pre>
        </div>
        <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
          <div class="flex items-center gap-2 mb-1.5">
            <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
            <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
            <span class="text-[10px] text-gray-600 font-mono">$ python modules/cleaning.py</span>
          </div>
          <div class="font-mono text-xs text-emerald-400 leading-relaxed">[&apos;Alice&apos;, &apos;Bob&apos;, &apos;Carol&apos;]</div>
        </div>
      </div>

      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">This function works on any list — swap the sample names for order IDs, product codes, or email addresses and it cleans them just the same.</p>
      </div>

    </div>
  </div>
</div><!-- /panel 2 -->

<!-- ════════════════════════════════════════════════════════════ -->
<!-- Panel 3 — Connect with main.py (hidden)                     -->
<!-- ════════════════════════════════════════════════════════════ -->
<div class="ce-panel ce-panel-anim hidden" role="tabpanel">
  <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

    <!-- Panel header -->
    <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
      <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
      <div class="relative flex items-center gap-3">
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
          <span class="iconify text-base" data-icon="fa6-solid:code"></span>
        </span>
        <div>
          <h3 class="font-bold text-gray-800">Connect with main.py</h3>
          <div class="flex items-center gap-2 mt-1">
            <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
              <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
            </span>
            <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Products</span>
            <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">import</span>
            <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Entry Point</span>
            <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Pipeline</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Panel body -->
    <div class="px-6 py-5 space-y-4">

      <div class="flex items-start gap-3 rounded-xl p-4 task-box">
        <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
          <p class="text-sm text-gray-600">This script shows how <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">main.py</code> imports the cleaning function from <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">modules/cleaning.py</code> and runs the full pipeline. You only ever run <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">main.py</code> — it handles every step in order.</p>
        </div>
      </div>

      <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
        <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
          <div class="flex items-center gap-3">
            <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
              <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
              <span class="text-[11px] font-semibold text-gray-400">main.py</span>
            </div>
          </div>
          <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
        </div>
        <div class="bg-code">
          <pre class="overflow-x-auto pre-reset"><code class="language-python"># main.py — the entry point; run this file to start the whole pipeline

from modules.cleaning import remove_blanks       # import the function from your module

product_names = ["Apples", "", "Bananas", "", "Cherries"]  # raw list with blank entries

clean_names = remove_blanks(product_names)       # clean the list using the module

print("Products ready:", clean_names)            # show the cleaned result
print("Count:", len(clean_names))                # count how many remain</code></pre>
        </div>
        <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
          <div class="flex items-center gap-2 mb-1.5">
            <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
            <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
            <span class="text-[10px] text-gray-600 font-mono">$ python main.py</span>
          </div>
          <div class="font-mono text-xs text-emerald-400 leading-relaxed">Products ready: [&apos;Apples&apos;, &apos;Bananas&apos;, &apos;Cherries&apos;]<br>Count: 3</div>
        </div>
      </div>

      <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
        <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
        <p class="text-sm text-gray-600">If the cleaning logic ever changes, update it once in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">modules/cleaning.py</code> — every script that imports it gets the fix automatically, with no copy-pasting required.</p>
      </div>

    </div>
  </div>
</div><!-- /panel 3 -->

</div>"""


def main():
    html = TARGET.read_text(encoding="utf-8")

    # Locate the code-examples section
    ce_start = html.index('id="code-examples"')
    ce_start = html.rindex("<section", 0, ce_start)
    ce_end   = html.index("</section>", ce_start) + len("</section>")

    # Locate the body div inside the section (after the header)
    body_open = '<div class="bg-white px-8 py-7 space-y-6">'
    body_open_pos = html.index(body_open, ce_start)

    # Find the closing structure: body </div> → card </div> → </section>
    closing = "\n  </div>\n</section>"
    closing_pos = html.rindex(closing, body_open_pos, ce_end)

    old_body = html[body_open_pos:closing_pos]
    old_len = len(old_body)

    html = html[:body_open_pos] + NEW_BODY + html[closing_pos:]

    TARGET.write_text(html, encoding="utf-8")
    print(f"✅  #code-examples body replaced  ({old_len:,} chars → {len(NEW_BODY):,} chars)")
    print(f"File size: {len(html):,} chars")


if __name__ == "__main__":
    main()
