"""Rewrite #practice section in lesson04 per lesson-practice-exercises.prompt.md."""
import pathlib, sys

TARGET = pathlib.Path("pages/track_01_python_foundation/mod_03_object_oriented_programming/lesson04_refactoring_a_script_into_a_class.html")

NEW_BODY = '''

      <!-- ── Tab pill row ──────────────────────────────────────── -->
      <div class="flex items-center gap-2 mb-6" role="tablist">

        <button onclick="switchPeTab(0)" class="pe-step pe-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Build the Class</span>
        </button>

        <button onclick="switchPeTab(1)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Add a run() Method</span>
        </button>

        <button onclick="switchPeTab(2)" class="pe-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-gray-400 transition-all duration-250" role="tab">
          <span class="iconify text-[13px]" data-icon="fa6-solid:pencil"></span>
          <span class="pe-step-label text-xs font-bold">Two Reports, One Class</span>
        </button>

      </div>

      <!-- ── Panel 1 — Build the Class ──────────────────────────── -->
      <div class="pe-panel pe-panel-anim" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Build the Class</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Reports</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">class</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">def</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">self</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">

            <!-- Task box -->
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">Your team runs a data pipeline every morning to load, clean, and save a report. Create a class called <code class="font-mono text-[11px]">ReportRunner</code> with three methods: <code class="font-mono text-[11px]">load_data(self)</code>, <code class="font-mono text-[11px]">clean_data(self)</code>, and <code class="font-mono text-[11px]">save_report(self)</code>. Each method should print one short confirmation message. Then create a <code class="font-mono text-[11px]">ReportRunner</code> object and call all three methods in order — you should see three lines of output.</p>
              </div>
            </div>

            <!-- Show Answer accordion -->
            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>

            <div class="accordion-body">

              <!-- Code block -->
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">report_runner.py</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:              # define the class
    def load_data(self):         # step one — load the raw data
        print("Loading data...")     # confirm the step ran

    def clean_data(self):        # step two — clean the loaded data
        print("Cleaning data...")    # confirm the step ran

    def save_report(self):       # step three — save the final output
        print("Report saved!")       # confirm the step ran

report = ReportRunner()          # create one instance of the class
report.load_data()               # call the first method
report.clean_data()              # call the second method
report.save_report()             # call the third method</code></pre>
                </div>
                <!-- Terminal output pane -->
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ python report_runner.py</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">Loading data...<br>Cleaning data...<br>Report saved!</div>
                </div>
              </div>

              <!-- Amber tip -->
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">You just turned three separate function calls into three organised methods on one object. If the team ever needs to run this pipeline again, you create another <code class="font-mono text-[11px]">ReportRunner()</code> object — the logic stays in one place and never needs to be rewritten.</p>
              </div>

            </div>
          </div>

        </div>
      </div>

      <!-- ── Panel 2 — Add a run() Method ───────────────────────── -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Add a run() Method</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Pipelines</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">run()</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">self.method()</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">

            <!-- Task box -->
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">The <code class="font-mono text-[11px]">ReportRunner</code> class has three methods, but you still need to call them one by one. Add a fourth method called <code class="font-mono text-[11px]">run(self)</code> that calls each of the three steps in order using <code class="font-mono text-[11px]">self</code>. Then create one object and trigger the whole pipeline with a single <code class="font-mono text-[11px]">report.run()</code> call — the output should still be the same three lines.</p>
              </div>
            </div>

            <!-- Show Answer accordion -->
            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>

            <div class="accordion-body">

              <!-- Code block -->
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">report_runner_run.py</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:              # the class with all four methods
    def load_data(self):         # step one
        print("Loading data...")

    def clean_data(self):        # step two
        print("Cleaning data...")

    def save_report(self):       # step three
        print("Report saved!")

    def run(self):               # coordinator — runs every step in order
        self.load_data()         # call step one via self
        self.clean_data()        # call step two via self
        self.save_report()       # call step three via self

report = ReportRunner()          # create one object
report.run()                     # one call runs the entire pipeline</code></pre>
                </div>
                <!-- Terminal output pane -->
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ python report_runner_run.py</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">Loading data...<br>Cleaning data...<br>Report saved!</div>
                </div>
              </div>

              <!-- Amber tip -->
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">The <code class="font-mono text-[11px]">run()</code> method turns the class into a one-call pipeline — you no longer need to remember the order of three separate calls. This is the same idea as a SQL stored procedure: call one name and all the steps fire in the right sequence.</p>
              </div>

            </div>
          </div>

        </div>
      </div>

      <!-- ── Panel 3 — Two Reports, One Class ───────────────────── -->
      <div class="pe-panel pe-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">

          <!-- Panel header -->
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:pencil"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Two Reports, One Class</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner
                  </span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Finance</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">objects</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">instances</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Panel body -->
          <div class="px-6 py-5 space-y-4">

            <!-- Task box -->
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">Your Task</p>
                <p class="text-sm text-gray-600">Your finance team runs two separate reports each day — one for sales and one for inventory. Create a <code class="font-mono text-[11px]">ReportRunner</code> class with a single <code class="font-mono text-[11px]">run(self)</code> method that prints "Running report…". Then create two separate objects — one called <code class="font-mono text-[11px]">sales_report</code> and one called <code class="font-mono text-[11px]">inventory_report</code> — and call <code class="font-mono text-[11px]">run()</code> on each. Your output should show two separate lines.</p>
              </div>
            </div>

            <!-- Show Answer accordion -->
            <button class="accordion-toggle w-full" onclick="toggleAccordion(this)">
              <span class="iconify text-xs" data-icon="fa6-solid:key"></span> Show Answer
              <span class="iconify text-xs accordion-chevron" data-icon="fa6-solid:chevron-down"></span>
            </button>

            <div class="accordion-body">

              <!-- Code block -->
              <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
                <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                  <div class="flex items-center gap-3">
                    <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                      <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                      <span class="text-[11px] font-semibold text-gray-400">two_reports.py</span>
                    </div>
                  </div>
                  <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
                </div>
                <div class="bg-code">
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">class ReportRunner:                   # define the class once
    def run(self):                    # one run method reused by every object
        print("Running report...")    # confirm the pipeline started

sales_report = ReportRunner()         # first object — the sales report
sales_report.run()                    # run the sales pipeline

inventory_report = ReportRunner()     # second object — the inventory report
inventory_report.run()                # run the inventory pipeline</code></pre>
                </div>
                <!-- Terminal output pane -->
                <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                  <div class="flex items-center gap-2 mb-1.5">
                    <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                    <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                    <span class="text-[10px] text-gray-600 font-mono">$ python two_reports.py</span>
                  </div>
                  <div class="font-mono text-xs text-emerald-400 leading-relaxed">Running report...<br>Running report...</div>
                </div>
              </div>

              <!-- Amber tip -->
              <div class="mt-3 rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
                <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
                <p class="text-sm text-gray-600">Each object is completely independent — calling <code class="font-mono text-[11px]">sales_report.run()</code> does not affect <code class="font-mono text-[11px]">inventory_report</code> at all. This is the same idea as running the same SQL stored procedure on two different database tables — the logic is identical, but each run operates on its own data.</p>
              </div>

            </div>
          </div>

        </div>
      </div>

    '''

# ── Replace body ──────────────────────────────────────────────────────────────
html = TARGET.read_text(encoding='utf-8')

idx = html.find('id="practice"')
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
idx2 = result.find('id="practice"')
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
    ('Shell: id="practice"',                   'id="practice"'),
    ('Shell: fa6-solid:pencil header icon',    'data-icon="fa6-solid:pencil"'),
    ('Shell: Practice Exercises title',        '>Practice Exercises<'),
    ('Shell: subtitle present',                'Guided exercises to reinforce your learning'),
    # Tab pills
    ('Tab 1: Build the Class',                 '>Build the Class<'),
    ('Tab 2: Add a run() Method',              '>Add a run() Method<'),
    ('Tab 3: Two Reports, One Class',          '>Two Reports, One Class<'),
    ('Tabs: all use fa6-solid:pencil',         s.count('data-icon="fa6-solid:pencil"') >= 4),  # header + 3 tabs
    ('Tab 1: active (pink gradient)',          'pe-step-active'),
    ('Tab 2: inactive (gray)',                 'switchPeTab(1)'),
    ('Tab 3: inactive (gray)',                 'switchPeTab(2)'),
    ('No "Exercise 1/2/3" labels',             'Exercise 1' not in s and 'Exercise 2' not in s),
    # Panels
    ('Panel 1: no hidden class on first',      'class="pe-panel pe-panel-anim"'),
    ('Panel 2: hidden',                        'class="pe-panel pe-panel-anim hidden"'),
    ('Panel 3: watermark 03',                  '>03<'),
    # Panel titles match tabs
    ('Panel 1 title: Build the Class',         '>Build the Class<'),
    ('Panel 2 title: Add a run() Method',      '>Add a run() Method<'),
    ('Panel 3 title: Two Reports, One Class',  '>Two Reports, One Class<'),
    # Watermarks
    ('Watermark 01 present',                   '>01<'),
    ('Watermark 02 present',                   '>02<'),
    # Badges — order: Beginner first, domain, then concept
    ('Beginner badge: fa6-solid:leaf (×3)',    s.count('data-icon="fa6-solid:leaf"') >= 3),
    ('Domain: Reports',                        '>Reports<'),
    ('Domain: Pipelines',                      '>Pipelines<'),
    ('Domain: Finance',                        '>Finance<'),
    ('Concept badge: class',                   '>class<'),
    ('Concept badge: run()',                   '>run()<'),
    ('Concept badge: objects',                 '>objects<'),
    # Task boxes
    ('Task box icon: clipboard-list (×3)',     s.count('fa6-solid:clipboard-list') == 3),
    ('Task box label: Your Task (×3)',         s.count('>Your Task<') == 3),
    # Accordions
    ('Accordion toggle × 3',                   s.count('toggleAccordion(this)') == 3),
    ('Accordion body × 3',                     s.count('class="accordion-body"') == 3),
    # Code blocks — no traffic-light dots
    ('No traffic-light dots',                  'bg-red-400/80' not in s),
    # Filenames
    ('Filename: report_runner.py',             'report_runner.py'),
    ('Filename: report_runner_run.py',         'report_runner_run.py'),
    ('Filename: two_reports.py',               'two_reports.py'),
    # Code content
    ('Code: class ReportRunner',               'class ReportRunner:'),
    ('Code: def load_data(self)',              'def load_data(self):'),
    ('Code: def run(self)',                    'def run(self):'),
    ('Code: self.load_data()',                 'self.load_data()'),
    ('Code: sales_report = ReportRunner()',    'sales_report = ReportRunner()'),
    ('Code: inventory_report = ReportRunner', 'inventory_report = ReportRunner()'),
    ('All code uses language-python (×3)',     s.count('language-python') >= 3),
    # Terminal panes
    ('Terminal pane ×3',                       s.count('fa6-solid:terminal') == 3),
    ('Terminal cmd 1',                         '$ python report_runner.py'),
    ('Terminal cmd 2',                         '$ python report_runner_run.py'),
    ('Terminal cmd 3',                         '$ python two_reports.py'),
    ('Output 1: Loading data...',              'Loading data...'),
    ('Output 2: Running report... (×2)',       s.count('Running report...') >= 2),
    # Amber tips
    ('Amber tip ×3',                           s.count('fa6-solid:circle-info') == 3),
    ('Tip 1: another ReportRunner()',          'another'),
    ('Tip 2: SQL stored procedure ref',        'stored procedure'),
    ('Tip 3: sales_report.run()',              'sales_report.run()'),
    # Copy buttons
    ('Copy button ×3',                         s.count('copy-btn copy-btn-light') == 3),
]

passed, failed = 0, 0
for label, check in checks:
    ok = check if isinstance(check, bool) else (check in s)
    print(f'  {"✅" if ok else "❌"} {label}')
    if ok: passed += 1
    else: failed += 1

print(f'\n{passed}/{passed+failed} checks passed')
