"""
Rewrites <section id="key-concepts"> in lesson04_logging_basics.html.
CSS and JS are already correct — only the section HTML needs replacing.
"""

TARGET = r'pages\track_01_python_foundation\mod_04_python_best_practices\lesson04_logging_basics.html'

# ── New section ───────────────────────────────────────────────────────────────
NEW_SECTION = '''\
<section id="key-concepts" class="scroll-mt-24">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">

    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:book-open"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Key Concepts</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">The logging module, severity levels, basicConfig(), and log handlers.</p>
      </div>
    </div>

    <div class="bg-white px-6 py-7">
      <div class="flex flex-col md:flex-row gap-0">

        <!-- ── Sidebar ── -->
        <div class="relative md:w-52 shrink-0 flex md:flex-col gap-1 md:border-r border-gray-100 md:pr-5 pb-4 md:pb-0" role="tablist">

          <div class="kc-indicator hidden md:block absolute right-0 top-0 w-[3px] rounded-full transition-all duration-300" style="height:68px;background:#CB187D;"></div>

          <!-- Tab 0 — ACTIVE -->
          <button onclick="switchKcTab(0)" class="kc-tab kc-tab-active group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#CB187D;color:#fff;box-shadow:0 2px 8px rgba(203,24,125,0.25)"><span class="iconify text-[11px]" data-icon="fa6-solid:code"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-900">The logging Module</span>
          </button>

          <!-- Tab 1 — INACTIVE -->
          <button onclick="switchKcTab(1)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:layer-group"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Severity Levels</span>
          </button>

          <!-- Tab 2 — INACTIVE -->
          <button onclick="switchKcTab(2)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:sliders"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">basicConfig()</span>
          </button>

          <!-- Tab 3 — INACTIVE -->
          <button onclick="switchKcTab(3)" class="kc-tab group flex items-center gap-3 w-full px-3 py-3 rounded-xl text-left transition-all duration-200" role="tab">
            <span class="kc-tab-num inline-flex items-center justify-center w-7 h-7 rounded-full shrink-0 transition-all duration-200" style="background:#f3f4f6;color:#9ca3af"><span class="iconify text-[11px]" data-icon="fa6-solid:folder-open"></span></span>
            <span class="kc-tab-label text-xs font-bold leading-tight text-gray-400">Log Handlers</span>
          </button>

        </div><!-- /sidebar -->

        <!-- ── Panels ── -->
        <div class="flex-1 min-w-0 md:pl-5">

          <!-- Panel 0 — Pink — ACTIVE -->
          <div class="kc-panel kc-panel-anim" data-color="pink" role="tabpanel">
            <div class="rounded-2xl border border-pink-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-[#CB187D] via-pink-400 to-rose-300"></div>
              <div class="bg-gradient-to-br from-pink-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:code"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">The logging Module</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Python\u2019s built-in recording system</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-pink-100 to-rose-100 text-[#CB187D] border border-pink-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> Built-in
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">The <strong>logging module</strong> is Python\u2019s built-in tool for recording events in your script. You add <code class="font-mono bg-pink-100 text-pink-800 border border-pink-200 px-1 rounded text-[10px]">import logging</code> at the top once \u2014 no installation needed.</p>

                <!-- Widget: comparison-strip — print() vs logging -->
                <div class="rounded-xl overflow-hidden border border-pink-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-pink-50 to-rose-50 border-b border-pink-100">
                    <span class="iconify text-pink-500 text-xs" data-icon="fa6-solid:arrow-right-arrow-left"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-pink-500">print() vs logging</p>
                  </div>
                  <div class="flex gap-0 bg-white">
                    <div class="flex-1 flex flex-col items-center justify-center px-3 py-3 border-r border-pink-50">
                      <code class="text-sm font-mono font-bold text-pink-700 bg-pink-100 border border-pink-200 px-2 py-0.5 rounded mb-1">print()</code>
                      <span class="text-[10px] font-semibold text-pink-600 bg-pink-100 border border-pink-200 px-2 py-0.5 rounded-full">Terminal only</span>
                    </div>
                    <div class="flex items-center justify-center px-3 text-pink-300 text-base font-black">\u2192</div>
                    <div class="flex-1 flex flex-col items-center justify-center px-3 py-3 border-r border-pink-50">
                      <code class="text-sm font-mono font-bold text-pink-700 bg-pink-100 border border-pink-200 px-2 py-0.5 rounded mb-1">logging</code>
                      <span class="text-[10px] font-semibold text-pink-600 bg-pink-100 border border-pink-200 px-2 py-0.5 rounded-full">File + terminal</span>
                    </div>
                    <div class="flex items-center justify-center px-3 text-pink-300 text-base font-black">\u2192</div>
                    <div class="flex-1 flex flex-col items-center justify-center px-3 py-3">
                      <span class="iconify text-xl text-green-500 mb-1" data-icon="fa6-solid:circle-check"></span>
                      <span class="text-[10px] font-bold text-green-700 bg-green-100 border border-green-200 px-2 py-0.5 rounded-full">Audit trail</span>
                    </div>
                  </div>
                </div>

                <!-- Code block — Style B -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Python</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">import logging                               # built-in \u2014 no pip install needed
logging.basicConfig(level=logging.DEBUG)     # configure once, before any log call
logging.info("Script started")               # record a routine event
logging.warning("Config file missing")       # record a concern worth noting
logging.error("File not found")              # record a failure that needs attention</code></pre>
                </div>

                <!-- Tip -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-pink-50 border border-pink-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-[#CB187D] shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Call basicConfig() before your first log call.</strong> If you skip it, Python uses silent defaults and your <code class="bg-pink-200 border border-pink-300 text-pink-800 px-1 rounded font-mono text-[10px]">DEBUG</code> and <code class="bg-pink-200 border border-pink-300 text-pink-800 px-1 rounded font-mono text-[10px]">INFO</code> messages will never appear.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 0 -->

          <!-- Panel 1 — Violet — INACTIVE -->
          <div class="kc-panel kc-panel-anim hidden" data-color="violet" role="tabpanel">
            <div class="rounded-2xl border border-violet-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-violet-500 via-purple-400 to-fuchsia-300"></div>
              <div class="bg-gradient-to-br from-violet-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500 to-purple-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:layer-group"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Severity Levels</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Five levels, least to most urgent</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-violet-100 to-purple-100 text-violet-600 border border-violet-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> 5 Levels
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">A <strong>severity level</strong> labels how urgent a message is. You set a minimum level when configuring logging \u2014 only messages at that level or above get recorded.</p>

                <!-- Widget: operators-table adapted as level reference -->
                <div class="rounded-xl overflow-hidden border border-violet-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-violet-50 to-fuchsia-50 border-b border-violet-100">
                    <span class="iconify text-violet-500 text-xs" data-icon="fa6-solid:layer-group"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-violet-500">Severity Levels Reference</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-violet-50">
                        <th class="py-2 px-3 text-left font-bold text-violet-600 w-24">Level</th>
                        <th class="py-2 px-3 text-left font-bold text-violet-600">When to use</th>
                        <th class="py-2 px-3 text-left font-bold text-violet-600 w-12">Rank</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3"><code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">DEBUG</code></td>
                        <td class="py-2 px-3 text-gray-500">Detailed steps \u2014 for diagnosing problems</td>
                        <td class="py-2 px-3 text-gray-400">10</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">INFO</code></td>
                        <td class="py-2 px-3 text-gray-500">Normal progress \u2014 everything is working</td>
                        <td class="py-2 px-3 text-gray-400">20</td>
                      </tr>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3"><code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">WARNING</code></td>
                        <td class="py-2 px-3 text-gray-500">Unexpected \u2014 script still runs but watch out</td>
                        <td class="py-2 px-3 text-gray-400">30</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3"><code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">ERROR</code></td>
                        <td class="py-2 px-3 text-gray-500">A failure occurred \u2014 something needs fixing</td>
                        <td class="py-2 px-3 text-gray-400">40</td>
                      </tr>
                      <tr>
                        <td class="py-2 px-3"><code class="font-mono bg-violet-100 text-violet-800 border border-violet-200 px-1.5 py-0.5 rounded-full text-[11px] font-bold">CRITICAL</code></td>
                        <td class="py-2 px-3 text-gray-500">Serious failure \u2014 the program may not continue</td>
                        <td class="py-2 px-3 text-gray-400">50</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block — Style B -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Python</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">logging.debug("Checking row count: %d", len(df))    # dev only \u2014 very detailed
logging.info("Dataset loaded successfully")           # normal progress
logging.warning("Missing values in column 'price'")  # something to watch
logging.error("Could not connect to database")        # a real failure
logging.critical("Out of memory \u2014 stopping run")      # the program cannot continue</code></pre>
                </div>

                <!-- Tip -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-violet-50 border border-violet-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-violet-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:triangle-exclamation"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>WARNING is the default minimum level.</strong> If you don\u2019t call <code class="bg-violet-200 border border-violet-300 text-violet-800 px-1 rounded font-mono text-[10px]">basicConfig()</code> first, your <code class="bg-violet-200 border border-violet-300 text-violet-800 px-1 rounded font-mono text-[10px]">DEBUG</code> and <code class="bg-violet-200 border border-violet-300 text-violet-800 px-1 rounded font-mono text-[10px]">INFO</code> messages are silently discarded.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 1 -->

          <!-- Panel 2 — Blue — INACTIVE -->
          <div class="kc-panel kc-panel-anim hidden" data-color="blue" role="tabpanel">
            <div class="rounded-2xl border border-blue-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-blue-500 via-cyan-400 to-teal-300"></div>
              <div class="bg-gradient-to-br from-blue-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:sliders"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">basicConfig()</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">One function call to set up logging</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-blue-100 to-indigo-100 text-blue-600 border border-blue-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> Setup
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed"><strong>basicConfig()</strong> is the function that configures your logging. You pass it the minimum level, the file to write to, and the message layout \u2014 all in a single call at the top of your script.</p>

                <!-- Widget: rules-table — key parameters -->
                <div class="rounded-xl overflow-hidden border border-blue-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-blue-50 to-indigo-50 border-b border-blue-100">
                    <span class="iconify text-blue-500 text-xs" data-icon="fa6-solid:list-check"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-blue-500">Key Parameters</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap w-1/3"><code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">level=</code></td>
                        <td class="py-2 px-3 text-gray-500"><code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">logging.DEBUG</code> shows all messages \u2713</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap"><code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">filename=</code></td>
                        <td class="py-2 px-3 text-gray-500"><code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">"app.log"</code> writes messages to a file \u2713</td>
                      </tr>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap"><code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">format=</code></td>
                        <td class="py-2 px-3 text-gray-500">add <code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded text-[10px]">%(asctime)s</code> for timestamps \u2713</td>
                      </tr>
                      <tr class="bg-gray-50/50">
                        <td class="py-2 px-3 font-semibold text-gray-700 whitespace-nowrap"><code class="font-mono bg-blue-100 text-blue-700 border border-blue-200 px-1 rounded">filemode=</code></td>
                        <td class="py-2 px-3 text-gray-500"><code class="font-mono bg-green-100 text-green-800 border border-green-200 px-1.5 py-0.5 rounded-full text-[10px]">"a"</code> keeps old entries \u2713 &nbsp;<code class="font-mono bg-red-100 text-red-700 border border-red-200 px-1.5 py-0.5 rounded-full text-[10px]">"w"</code> overwrites \u2717</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block — Style B -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Python</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">logging.basicConfig(
    level=logging.DEBUG,                         # record all messages
    filename="pipeline.log",                     # write to this file
    filemode="a",                                # append \u2014 keeps previous entries
    format="%(asctime)s %(levelname)s: %(message)s"  # timestamp + level + text
)
logging.info("Pipeline started")                 # test that the setup works</code></pre>
                </div>

                <!-- Tip -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-blue-50 border border-blue-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-blue-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Call basicConfig() once, at the very top of your script.</strong> Calling it a second time has no effect \u2014 Python ignores repeated calls because logging is already configured.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 2 -->

          <!-- Panel 3 — Emerald — INACTIVE -->
          <div class="kc-panel kc-panel-anim hidden" data-color="emerald" role="tabpanel">
            <div class="rounded-2xl border border-emerald-100 overflow-hidden">
              <div class="h-1 bg-gradient-to-r from-emerald-500 via-teal-400 to-cyan-300"></div>
              <div class="bg-gradient-to-br from-emerald-50/60 to-white p-5 space-y-4">

                <!-- Header row -->
                <div class="flex items-center justify-between">
                  <div class="flex items-center gap-3">
                    <span class="inline-flex items-center justify-center w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500 to-teal-600 shadow-md shrink-0">
                      <span class="iconify text-white text-sm" data-icon="fa6-solid:folder-open"></span>
                    </span>
                    <div>
                      <h3 class="text-sm font-bold text-gray-900 leading-tight">Log Handlers</h3>
                      <p class="text-[10px] text-gray-400 leading-none mt-0.5">Control where messages are sent</p>
                    </div>
                  </div>
                  <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-[10px] font-bold bg-gradient-to-r from-emerald-100 to-teal-100 text-emerald-600 border border-emerald-200 shadow-sm">
                    <span class="iconify text-[10px]" data-icon="fa6-solid:code"></span> Output
                  </span>
                </div>

                <!-- Definition -->
                <p class="text-xs text-gray-600 leading-relaxed">A <strong>handler</strong> decides where your log messages go. Python gives you two main options: the terminal (<code class="font-mono bg-emerald-100 text-emerald-800 border border-emerald-200 px-1 rounded text-[10px]">StreamHandler</code>) and a file on disk (<code class="font-mono bg-emerald-100 text-emerald-800 border border-emerald-200 px-1 rounded text-[10px]">FileHandler</code>). You can attach both to the same logger.</p>

                <!-- Widget: comparison-table — StreamHandler vs FileHandler -->
                <div class="rounded-xl overflow-hidden border border-emerald-100">
                  <div class="flex items-center gap-2 px-3 py-2 bg-gradient-to-r from-emerald-50 to-teal-50 border-b border-emerald-100">
                    <span class="iconify text-emerald-500 text-xs" data-icon="fa6-solid:scale-balanced"></span>
                    <p class="text-[10px] font-bold uppercase tracking-widest text-emerald-500">StreamHandler vs FileHandler</p>
                  </div>
                  <table class="w-full text-xs border-collapse bg-white">
                    <thead>
                      <tr class="border-b border-emerald-50">
                        <th class="py-2 px-3 text-left font-bold text-gray-400 w-1/3"></th>
                        <th class="py-2 px-3 text-left"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-blue-100 text-blue-700 border border-blue-200 text-[10px] font-bold">StreamHandler</span></th>
                        <th class="py-2 px-3 text-left"><span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-700 border border-emerald-200 text-[10px] font-bold">FileHandler</span></th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr class="border-b border-gray-50">
                        <td class="py-2 px-3 font-semibold text-gray-600">Destination</td>
                        <td class="py-2 px-3 text-gray-500">Terminal screen</td>
                        <td class="py-2 px-3 text-gray-500">File on disk</td>
                      </tr>
                      <tr class="border-b border-gray-50 bg-gray-50/40">
                        <td class="py-2 px-3 font-semibold text-gray-600">Survives close</td>
                        <td class="py-2 px-3"><span class="text-red-400 font-bold">\u2717</span> <span class="text-gray-400">Gone on close</span></td>
                        <td class="py-2 px-3"><span class="text-green-500 font-bold">\u2713</span> <span class="text-gray-400">Stays on disk</span></td>
                      </tr>
                      <tr>
                        <td class="py-2 px-3 font-semibold text-gray-600">Good for</td>
                        <td class="py-2 px-3 text-gray-500">Live debugging</td>
                        <td class="py-2 px-3 text-gray-500">Production audits</td>
                      </tr>
                    </tbody>
                  </table>
                </div>

                <!-- Code block — Style B -->
                <div class="rounded-xl overflow-hidden bg-code shadow-md">
                  <div class="flex items-center justify-between px-4 py-2 border-b border-code-sep">
                    <div class="flex items-center gap-2">
                      <span class="iconify" data-icon="logos:python" data-width="14" data-height="14"></span>
                      <span class="text-[11px] font-semibold text-gray-400">Python</span>
                    </div>
                    <button class="copy-btn copy-btn-light" onclick="copyCode(this)">
                      <span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy
                    </button>
                  </div>
                  <pre class="overflow-x-auto pre-reset"><code class="language-python">logger = logging.getLogger(__name__)          # named logger for this file
logger.setLevel(logging.DEBUG)                # accept all messages
stream_h = logging.StreamHandler()            # sends messages to the terminal
file_h   = logging.FileHandler("app.log")     # writes messages to a file

logger.addHandler(stream_h)                   # attach the terminal handler
logger.addHandler(file_h)                     # attach the file handler

logger.info("Handlers attached")              # appears in terminal AND in app.log</code></pre>
                </div>

                <!-- Tip -->
                <div class="rounded-xl p-3 flex items-start gap-2.5 bg-emerald-50 border border-emerald-100">
                  <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-emerald-500 shrink-0 mt-0.5">
                    <span class="iconify text-white text-[10px]" data-icon="fa6-solid:lightbulb"></span>
                  </span>
                  <p class="text-xs text-gray-600"><strong>Use <code class="bg-emerald-200 border border-emerald-300 text-emerald-800 px-1 rounded font-mono text-[10px]">logging.getLogger(__name__)</code> instead of the root logger</strong> in any file others might import. It keeps each module\u2019s logs separate and easier to trace.</p>
                </div>

              </div>
            </div>
          </div><!-- /panel 3 -->

        </div><!-- /panels -->
      </div>
    </div>
  </div>
</section>'''

# ── Read & replace ────────────────────────────────────────────────────────────
with open(TARGET, encoding='utf-8') as fh:
    content = fh.read()

sec_start = content.find('<section id="key-concepts">')
if sec_start == -1:
    print('ERROR: section not found'); exit(1)

sec_end = content.find('</section>', sec_start) + len('</section>')
new_content = content[:sec_start] + NEW_SECTION + content[sec_end:]

with open(TARGET, 'w', encoding='utf-8') as fh:
    fh.write(new_content)

print('Section written successfully.')

# ── Verify ────────────────────────────────────────────────────────────────────
with open(TARGET, encoding='utf-8') as fh:
    result = fh.read()

s = result.find('<section id="key-concepts"')
e = result.find('</section>', s) + len('</section>')
sec = result[s:e]

checks = [
    ('scroll-mt-24 on section',         'class="scroll-mt-24"' in sec),
    ('Section subtitle correct',         'The logging module, severity levels' in sec),
    ('kc-indicator has inline bg style', 'style="height:68px;background:#CB187D;"' in sec),
    ('4 sidebar tabs',                   sec.count('onclick="switchKcTab(') == 4),
    ('Tab 0 active inline style',        'style="background:#CB187D;color:#fff;box-shadow' in sec),
    ('Tabs 1-3 inactive inline style',   sec.count('style="background:#f3f4f6;color:#9ca3af"') == 3),
    ('4 kc-panels',                      sec.count('class="kc-panel kc-panel-anim') == 4),
    ('3 hidden panels',                  sec.count('kc-panel kc-panel-anim hidden"') == 3),
    ('Panel 0 pink',                     'border-pink-100' in sec),
    ('Panel 1 violet',                   'border-violet-100' in sec),
    ('Panel 2 blue',                     'border-blue-100' in sec),
    ('Panel 3 emerald',                  'border-emerald-100' in sec),
    ('4 header rows',                    sec.count('flex items-center justify-between') == 4),
    ('4 definitions (bare <p>)',         sec.count('class="text-xs text-gray-600 leading-relaxed"') == 4),
    ('comparison-strip widget (Tab 0)',  'arrow-right-arrow-left' in sec),
    ('operators-table widget (Tab 1)',   'Severity Levels Reference' in sec),
    ('rules-table widget (Tab 2)',       'Key Parameters' in sec),
    ('comparison-table widget (Tab 3)', 'StreamHandler vs FileHandler' in sec),
    ('4 Style-B code blocks',            sec.count('rounded-xl overflow-hidden bg-code shadow-md') == 4),
    ('4 tip callouts',                   sec.count('class="text-xs text-gray-600"') == 4),
    ('Pink tip (lightbulb)',             'bg-[#CB187D]' in sec),
    ('Violet tip (triangle-exclamation)','triangle-exclamation' in sec),
    ('Blue tip (lightbulb)',             'bg-blue-500' in sec),
    ('Emerald tip (lightbulb)',          'bg-emerald-500' in sec),
    ('No traffic-light dots',            'bg-red-400/80' not in sec),
    ('No Style-A dark headers',          'bg-[#181825]' not in sec),
    ('px-6 py-7 on section body',        'px-6 py-7' in sec),
    ('md:pl-5 on panels col',            'md:pl-5' in sec),
]

print()
all_ok = True
for label, ok in checks:
    print(f'  {"OK  " if ok else "FAIL"}: {label}')
    if not ok:
        all_ok = False

print()
print('All checks passed.' if all_ok else 'Some checks FAILED.')
