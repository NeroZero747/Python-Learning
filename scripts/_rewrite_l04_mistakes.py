"""Rewrite #mistakes section in lesson04 per lesson-common-mistakes.prompt.md."""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_BODY = '''

      <!-- ── Tab pill row ─────────────────────────────────────── -->
      <div class="flex items-center gap-2 mb-6" role="tablist">

        <button onclick="switchMkTab(0)" class="mk-step mk-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Missing self</span>
        </button>

        <button onclick="switchMkTab(1)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Class, Not Object</span>
        </button>

        <button onclick="switchMkTab(2)" class="mk-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>
          <span class="mk-step-label text-xs font-bold">Missing self.</span>
        </button>

      </div>

      <!-- ── Panel 1 — Missing self ────────────────────────────── -->
      <div class="mk-panel mk-panel-anim" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <!-- Card header -->
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Defining a Method Without the self Parameter</h4>
              <p class="text-xs text-gray-500 mt-0.5">Python passes the object automatically — writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">def load_data():</code> raises a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">TypeError</code> when the method is called.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <!-- Explanation paragraph -->
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Every method inside a class must have <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">self</code> as its first parameter — Python uses it to pass the object reference automatically when you call <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">report.load_data()</code>. Without it, Python raises <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">TypeError: load_data() takes 0 positional arguments but 1 was given</code>. Add <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">self</code> as the first parameter of every method definition.</p>
          </div>

          <!-- Wrong / Correct split panel -->
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — no self parameter
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">class ReportRunner:
    def load_data():
        print("Loading data...")</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — self as first parameter
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">class ReportRunner:
    def load_data(self):       # self receives the object
        print("Loading data...")</code></pre>
              </div>
            </div>
          </div>

          <!-- Amber tip footer -->
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Think of <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">self</code> as the method's name tag — it tells Python which object the method belongs to. Every method in a class needs it, and Python always passes it silently for you when you call <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">report.load_data()</code>.</p>
          </div>

        </div>
      </div>

      <!-- ── Panel 2 — Class, Not Object ──────────────────────── -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <!-- Card header -->
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Calling a Method on the Class Instead of an Object</h4>
              <p class="text-xs text-gray-500 mt-0.5"><code class="font-mono bg-gray-100 px-1 rounded text-[11px]">ReportRunner.load_data()</code> calls the class directly — Python raises a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">TypeError</code> because there is no object to pass as <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">self</code>.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <!-- Explanation paragraph -->
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">ReportRunner.load_data()</code> calls the method on the class blueprint rather than on a real object, so Python has nothing to pass as <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">self</code> and raises <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">TypeError: load_data() missing 1 required positional argument: 'self'</code>. Create an object first with <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">report = ReportRunner()</code>, then call <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">report.load_data()</code>.</p>
          </div>

          <!-- Wrong / Correct split panel -->
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — calling on the class
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python"># no object created
ReportRunner.load_data()</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — calling on an object
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">report = ReportRunner()  # build the object
report.load_data()       # call the method on it</code></pre>
              </div>
            </div>
          </div>

          <!-- Amber tip footer -->
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">A class is a blueprint, not a usable thing. You have to build something from the blueprint first — <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">report = ReportRunner()</code> is that building step. Only then can you call its methods.</p>
          </div>

        </div>
      </div>

      <!-- ── Panel 3 — Missing self. ───────────────────────────── -->
      <div class="mk-panel mk-panel-anim hidden" role="tabpanel">
        <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

          <!-- Card header -->
          <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
            <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
              <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
            </span>
            <div class="min-w-0 flex-1">
              <h4 class="font-bold text-gray-800 text-sm">Calling Another Method Inside run() Without self.</h4>
              <p class="text-xs text-gray-500 mt-0.5">Writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">load_data()</code> inside <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">run()</code> raises a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">NameError</code> — Python looks for a global function, not a method on the object.</p>
            </div>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
              <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
            </span>
          </div>

          <!-- Explanation paragraph -->
          <div class="px-6 py-5">
            <p class="text-sm text-gray-600 leading-relaxed">Inside <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">run(self)</code>, writing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">load_data()</code> tells Python to search for a standalone global function — which does not exist — and raises <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">NameError: name 'load_data' is not defined</code>. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">self.load_data()</code> so Python knows to look for the method on the same object.</p>
          </div>

          <!-- Wrong / Correct split panel -->
          <div class="relative grid grid-cols-1 sm:grid-cols-2">
            <div class="p-5 bg-red-50/30">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong — missing self. prefix
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">def run(self):
    load_data()    # NameError
    clean_data()   # NameError
    save_report()  # NameError</code></pre>
              </div>
            </div>
            <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
              <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
                <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
              </span>
            </div>
            <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
              <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
                <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct — self. on every call
              </p>
              <div class="rounded-xl overflow-hidden bg-code">
                <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">def run(self):
    self.load_data()    # call the method on this object
    self.clean_data()   # call the method on this object
    self.save_report()  # call the method on this object</code></pre>
              </div>
            </div>
          </div>

          <!-- Amber tip footer -->
          <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
            <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
            <p class="text-xs text-gray-600 leading-relaxed">Inside a class, <code class="font-mono bg-amber-100 px-1 rounded text-[11px]">self.</code> is always the prefix when one method needs to call another — it scopes the call to the current object. Think of it as saying "run the version of this method that belongs to me, not someone else's".</p>
          </div>

        </div>
      </div>

    '''

# ── Replace body ──────────────────────────────────────────────────────────────
html = TARGET.read_text(encoding='utf-8')

idx = html.find('id="mistakes"')
BODY_OPEN = '<div class="bg-white px-8 py-7 space-y-6">'
body_start = html.find(BODY_OPEN, idx)
if body_start == -1:
    print('❌ Body div not found'); sys.exit(1)

content_start = body_start + len(BODY_OPEN)
search = html[content_start:]
depth, body_end, i = 1, -1, 0
while i < len(search):
    if search[i:].startswith('<div'):
        depth += 1; i += 4
    elif search[i:].startswith('</div>'):
        depth -= 1
        if depth == 0:
            body_end = content_start + i; break
        i += 6
    else:
        i += 1

if body_end == -1:
    print('❌ Closing </div> not found'); sys.exit(1)

old = html[content_start:body_end]
print(f'  Old body: {len(old):,} chars')
print(f'  New body: {len(NEW_BODY):,} chars')

html = html[:content_start] + NEW_BODY + html[body_end:]
TARGET.write_text(html, encoding='utf-8')
print(f'✅ Written: {len(html):,} chars total')

# ── Verification ──────────────────────────────────────────────────────────────
result = TARGET.read_text(encoding='utf-8')
idx2 = result.find('id="mistakes"')
sec_s = result.rfind('<section', 0, idx2)
search2 = result[sec_s:]
depth2, sec_e, i = 0, -1, 0
while i < len(search2):
    if search2[i:].startswith('<section'): depth2 += 1; i += len('<section')
    elif search2[i:].startswith('</section>'):
        depth2 -= 1
        if depth2 == 0: sec_e = sec_s + i + len('</section>'); break
        i += len('</section>')
    else: i += 1
s = result[sec_s:sec_e]

checks = [
    # Shell preserved
    ('Shell: id="mistakes"',                         'id="mistakes"'),
    ('Shell: triangle-exclamation icon',             'fa6-solid:triangle-exclamation'),
    ('Shell: Common Mistakes title',                 '>Common Mistakes<'),
    # Tab pills — icon
    ('Tab icons: fa6-solid:bug ×3',                  s.count('data-icon="fa6-solid:bug"') >= 3),
    # Tab labels — no "Mistake N"
    ('Tab 1: Missing self',                          '>Missing self<'),
    ('Tab 2: Class, Not Object',                     '>Class, Not Object<'),
    ('Tab 3: Missing self.',                         '>Missing self.<'),
    ('No "Mistake 1/2/3" labels',                    'Mistake 1' not in s and 'Mistake 2' not in s),
    # Tab state
    ('Tab 1: active pink gradient',                  'mk-step-active'),
    ('Tab 2: switchMkTab(1)',                        'switchMkTab(1)'),
    ('Tab 3: switchMkTab(2)',                        'switchMkTab(2)'),
    # Panels — hidden state
    ('Panel 1: no hidden class',                     'class="mk-panel mk-panel-anim"'),
    ('Panel 2: hidden',                              'class="mk-panel mk-panel-anim hidden"'),
    # Panel 3 hidden — count of hidden panels = 2
    ('Panels 2+3 hidden count = 2',                  s.count('class="mk-panel mk-panel-anim hidden"') == 2),
    # Card headers
    ('Header bg: from-red-50/60 to-white ×3',        s.count('bg-gradient-to-r from-red-50/60 to-white') == 3),
    ('Header icon: fa6-solid:bug in red-100 ×3',     s.count('bg-red-100') >= 3),
    ('Pitfall badge ×3',                             s.count('>Pitfall<') == 3),
    # Card titles
    ('M1 title: Defining a Method Without',          'Defining a Method Without the self Parameter'),
    ('M2 title: Calling a Method on the Class',      'Calling a Method on the Class Instead of an Object'),
    ('M3 title: Calling Another Method Inside run()', 'Calling Another Method Inside run() Without self.'),
    # Explanation paragraphs present ×3
    ('Explanation: TypeError for missing self',      'load_data() takes 0 positional arguments but 1 was given'),
    ('Explanation: load_data() missing 1 required',  'missing 1 required positional argument'),
    ('Explanation: NameError inside run()',          'NameError: name'),
    # Split panels — structure
    ('bg-red-50/30 ×3',                              s.count('bg-red-50/30') == 3),
    ('bg-emerald-50/30 ×3',                          s.count('bg-emerald-50/30') == 3),
    ('Arrow divider ×3',                             s.count('fa6-solid:arrow-right') == 3),
    ('Wrong label ×3',                               s.count('Wrong —') == 3),
    ('Correct label ×3',                             s.count('Correct —') == 3),
    # Code content
    ('Wrong 1: def load_data():',                    'def load_data():'),
    ('Correct 1: def load_data(self):',              'def load_data(self):'),
    ('Wrong 2: ReportRunner.load_data()',            'ReportRunner.load_data()'),
    ('Correct 2: report = ReportRunner()',           'report = ReportRunner()'),
    ('Wrong 3: load_data() no self.',                s.count('    load_data()    # NameError') == 1),
    ('Correct 3: self.load_data()',                  'self.load_data()    # call the method on this object'),
    # All code uses language-python
    ('All code: language-python ×6',                 s.count('language-python') == 6),
    # Amber tips — lightbulb icon ×3
    ('Lightbulb tip icon ×3',                        s.count('fa6-solid:lightbulb') == 3),
    ('Tip 1: name tag analogy',                      'name tag'),
    ('Tip 2: blueprint analogy',                     'blueprint'),
    ('Tip 3: self. prefix rule',                     'self.` is always the prefix'),
    # No old content (circle-1/2/3 icons gone)
    ('No circle-1 icon',                             'fa6-solid:circle-1' not in s),
    ('No old watermark structure (from-red-50 via)', 'from-red-50 via-white to-rose-50' not in s),
]

passed, failed = 0, 0
for label, check in checks:
    ok = check if isinstance(check, bool) else (check in s)
    print(f'  {"✅" if ok else "❌"} {label}')
    if ok: passed += 1
    else: failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
