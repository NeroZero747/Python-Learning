"""
Replace the #code-examples body in lesson06_shiny_for_python.html
with the canonical structure per lesson-code-examples.prompt.md.
"""

import re
from pathlib import Path

TARGET = Path(__file__).parent.parent / "pages/mod_05_data_application/lesson06_shiny_for_python.html"

NEW_BODY = """    <div class="bg-white px-8 py-7 space-y-6">
      <div class="flex items-center gap-2 mb-6 flex-wrap" role="tablist">
        <button onclick="switchCeTab(0)" class="ce-step ce-step-active flex items-center gap-2 px-4 py-2 rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] text-white shadow-lg shadow-pink-200/50 transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code"></span><span class="ce-step-label text-xs font-bold">Minimal Shiny App</span></button>
        <button onclick="switchCeTab(1)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-white transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code"></span><span class="ce-step-label text-xs font-bold">Reactive Filtering</span></button>
        <button onclick="switchCeTab(2)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-white transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code"></span><span class="ce-step-label text-xs font-bold">Dynamic Plot Output</span></button>
        <button onclick="switchCeTab(3)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-white transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code"></span><span class="ce-step-label text-xs font-bold">Multi-Tab Dashboard</span></button>
        <button onclick="switchCeTab(4)" class="ce-step flex items-center gap-2 px-4 py-2 rounded-full bg-gray-800 text-white transition-all duration-250" role="tab"><span class="iconify text-[13px]" data-icon="fa6-solid:code"></span><span class="ce-step-label text-xs font-bold">Dynamic UI</span></button>
      </div>

      <!-- PANEL 1: Minimal Shiny App -->
      <div class="ce-panel ce-panel-anim" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">01</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Minimal Shiny App</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200"><span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">General</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">App()</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">@render.text</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This script creates a Shiny app with one slider input and one text output. Every Shiny app has the same two-part structure: a <strong class="text-gray-800">UI</strong> object that defines the layout and a <strong class="text-gray-800">server</strong> function that reacts to input changes.</p>
              </div>
            </div>
            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">minimal_app.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">from shiny import App, ui, render              # import the three core pieces
app_ui = ui.page_fixed(                        # ui: define the page layout
    ui.input_slider(&quot;n&quot;, &quot;Number&quot;, 1, 10, 5),  # slider input, starts at 5
    ui.output_text_verbatim(&quot;result&quot;),         # placeholder for the output
)
def server(input, output, session):            # server: react when inputs change
    @render.text
    def result():                              # name must match &quot;result&quot; in app_ui
        return f&quot;You chose: {input.n()}&quot;      # reads the slider value reactively
app = App(app_ui, server)                      # connect ui and server</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ shiny run minimal_app.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">INFO:     Uvicorn running on http://127.0.0.1:8000<br>You chose: 5</div>
              </div>
            </div>
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">The function name inside <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">@render.text</code> must exactly match the output id in <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">app_ui</code> — a typo here is the most common reason an output stays blank.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- PANEL 2: Reactive Filtering -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">02</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Reactive Filtering</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200"><span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">School</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">@reactive.calc</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">DataFrames</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This script filters a student scores DataFrame based on a slider and displays the results as a table. The <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">@reactive.calc</code> decorator caches the filtered result so any output that calls <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">passing()</code> gets the same cached data without re-running the filter.</p>
              </div>
            </div>
            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">reactive_filter.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">from shiny import App, ui, render, reactive    # add reactive for caching
import pandas as pd
scores = pd.DataFrame({&quot;student&quot;:[&quot;Ana&quot;,&quot;Ben&quot;,&quot;Cara&quot;,&quot;Dan&quot;],&quot;score&quot;:[85,72,91,68]})
app_ui = ui.page_fixed(
    ui.input_slider(&quot;threshold&quot;, &quot;Min score&quot;, 0, 100, 70),  # filter slider
    ui.output_table(&quot;results&quot;),                # table placeholder
)
def server(input, output, session):
    @reactive.calc
    def passing():                             # runs once; result is cached for reuse
        return scores[scores[&quot;score&quot;] &gt;= input.threshold()]
    @render.table
    def results():  return passing()           # reads the cached DataFrame
app = App(app_ui, server)</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ shiny run reactive_filter.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">INFO:     Uvicorn running on http://127.0.0.1:8000</div>
              </div>
            </div>
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Use <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">@reactive.calc</code> whenever two or more outputs need the same filtered data — it calculates once and shares the cached result, so Shiny never runs the filter twice.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- PANEL 3: Dynamic Plot Output -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">03</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Dynamic Plot Output</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200"><span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Sales</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">@render.plot</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">matplotlib</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This script draws a bar chart that switches between two data columns when you change the dropdown. The <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">@render.plot</code> decorator wraps the function and tells Shiny to display the return value as an image.</p>
              </div>
            </div>
            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">plot_app.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">from shiny import App, ui, render
import pandas as pd, matplotlib.pyplot as plt
data = pd.DataFrame({&quot;month&quot;:[&quot;Jan&quot;,&quot;Feb&quot;,&quot;Mar&quot;],&quot;revenue&quot;:[120,135,150],&quot;units&quot;:[800,920,1050]})
app_ui = ui.page_fixed(
    ui.input_select(&quot;col&quot;, &quot;Metric&quot;, [&quot;revenue&quot;, &quot;units&quot;]),  # dropdown to pick metric
    ui.output_plot(&quot;chart&quot;),                   # plot placeholder
)
def server(input, output, session):
    @render.plot
    def chart():                               # re-runs when input.col() changes
        fig, ax = plt.subplots()
        ax.bar(data[&quot;month&quot;], data[input.col()], color=&quot;#CB187D&quot;)  # bar chart
        return fig                             # must return the Figure object
app = App(app_ui, server)</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ shiny run plot_app.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">INFO:     Uvicorn running on http://127.0.0.1:8000</div>
              </div>
            </div>
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Always return the Figure object from a <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">@render.plot</code> function — calling <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">plt.show()</code> alone does nothing because Shiny needs the object to embed the chart in the page.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- PANEL 4: Multi-Tab Dashboard -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">04</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Multi-Tab Dashboard</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200"><span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">Sales</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">ui.page_navbar</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">nav_panel</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This script builds a two-tab dashboard using <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">ui.page_navbar()</code>. The Summary tab shows a text total and the Data tab shows the full table — each tab gets its own <strong class="text-gray-800">server output</strong>.</p>
              </div>
            </div>
            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">dashboard.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">from shiny import App, ui, render
import pandas as pd
data = pd.DataFrame({&quot;region&quot;:[&quot;North&quot;,&quot;South&quot;,&quot;East&quot;],&quot;revenue&quot;:[320,280,410]})
app_ui = ui.page_navbar(                       # page_navbar creates a tabbed layout
    ui.nav_panel(&quot;Summary&quot;, ui.output_text(&quot;total&quot;)),   # tab 1: a text summary
    ui.nav_panel(&quot;Data&quot;,    ui.output_table(&quot;tbl&quot;)),     # tab 2: the full table
    title=&quot;Sales Dashboard&quot;,
)
def server(input, output, session):
    @render.text
    def total():    return f&quot;Total revenue: ${data[&apos;revenue&apos;].sum():,}K&quot;  # sum all regions
    @render.table
    def tbl():      return data                # show the full DataFrame
app = App(app_ui, server)</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ shiny run dashboard.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">INFO:     Uvicorn running on http://127.0.0.1:8000<br>Total revenue: $1,010K</div>
              </div>
            </div>
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Switch <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">ui.page_fixed()</code> to <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">ui.page_navbar()</code> to add navigation tabs — each <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">ui.nav_panel()</code> call creates one named tab in the top bar.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- PANEL 5: Dynamic UI -->
      <div class="ce-panel ce-panel-anim hidden" role="tabpanel">
        <div class="relative rounded-2xl border border-gray-100 overflow-hidden shadow-sm">
          <div class="relative bg-gradient-to-br from-[#fdf0f7] via-white to-[#fef3f9] px-6 py-5 border-b border-gray-100 overflow-hidden">
            <span class="absolute -right-4 -top-4 text-[6rem] font-black text-[#CB187D]/[0.04] leading-none select-none pointer-events-none">05</span>
            <div class="relative flex items-center gap-3">
              <span class="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-[#CB187D] to-[#e84aad] text-white text-sm font-bold shadow-md">
                <span class="iconify text-base" data-icon="fa6-solid:code"></span>
              </span>
              <div>
                <h3 class="font-bold text-gray-800">Dynamic UI</h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="flex items-center gap-1 text-[10px] font-semibold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-600 border border-emerald-200"><span class="iconify text-[10px]" data-icon="fa6-solid:leaf"></span> Beginner</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">HR</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">@render.ui</span>
                  <span class="flex items-center gap-1 text-[10px] px-2 py-0.5 rounded-full bg-gray-100 text-gray-500 font-medium">output_ui</span>
                </div>
              </div>
            </div>
          </div>
          <div class="px-6 py-5 space-y-4">
            <div class="flex items-start gap-3 rounded-xl p-4 task-box">
              <span class="iconify text-xl shrink-0 mt-0.5 text-brand" data-icon="fa6-solid:clipboard-list"></span>
              <div>
                <p class="text-xs font-bold uppercase tracking-widest mb-1 text-brand">What This Does</p>
                <p class="text-sm text-gray-600">This script generates a dropdown widget at runtime based on which department you select. The <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">@render.ui</code> decorator lets the server build and return any UI element dynamically — something a fixed UI layout cannot do.</p>
              </div>
            </div>
            <div class="rounded-xl overflow-hidden border border-gray-800 shadow-lg">
              <div class="flex items-center justify-between px-4 py-2.5 bg-[#181825]">
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-1.5 px-3 py-1 rounded-md bg-[#1e1e2e] border border-white/5">
                    <span class="iconify text-yellow-400 text-xs" data-icon="logos:python" data-width="12" data-height="12"></span>
                    <span class="text-[11px] font-semibold text-gray-400">dynamic_ui.py</span>
                  </div>
                </div>
                <button class="copy-btn copy-btn-light" onclick="copyCode(this)"><span class="iconify mr-1" data-icon="fa6-regular:copy"></span>Copy</button>
              </div>
              <div class="bg-code">
                <pre class="overflow-x-auto pre-reset"><code class="language-python">from shiny import App, ui, render
choices = {&quot;Sales&quot;: [&quot;Revenue&quot;, &quot;Deals&quot;], &quot;IT&quot;: [&quot;Tickets&quot;, &quot;Uptime&quot;]}  # per-dept options
app_ui = ui.page_fixed(
    ui.input_select(&quot;dept&quot;, &quot;Department&quot;, list(choices)),  # department dropdown
    ui.output_ui(&quot;metric_ui&quot;),                 # placeholder for the dynamic widget
    ui.output_text(&quot;result&quot;),
)
def server(input, output, session):
    @render.ui
    def metric_ui():                           # rebuilds when input.dept() changes
        return ui.input_select(&quot;metric&quot;, &quot;Metric&quot;, choices[input.dept()])
    @render.text
    def result():  return f&quot;Dept: {input.dept()}, Metric: {input.metric()}&quot;
app = App(app_ui, server)</code></pre>
              </div>
              <div class="border-t border-white/5 bg-[#11111b] px-4 py-3">
                <div class="flex items-center gap-2 mb-1.5">
                  <span class="iconify text-emerald-400 text-[10px]" data-icon="fa6-solid:terminal"></span>
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-wider">Terminal</span>
                  <span class="text-[10px] text-gray-600 font-mono">$ shiny run dynamic_ui.py</span>
                </div>
                <div class="font-mono text-xs text-emerald-400 leading-relaxed">INFO:     Uvicorn running on http://127.0.0.1:8000<br>Dept: Sales, Metric: Revenue</div>
              </div>
            </div>
            <div class="rounded-xl p-4 flex items-start gap-3 border bg-amber-tip">
              <span class="iconify text-orange-400 mt-0.5 shrink-0" data-icon="fa6-solid:circle-info"></span>
              <p class="text-sm text-gray-600">Use <code class="text-xs font-mono px-1.5 py-0.5 rounded bg-gray-100 text-gray-700">@render.ui</code> when a widget&apos;s options depend on another input — Shiny rebuilds the widget automatically whenever the upstream input changes.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""

html = TARGET.read_text(encoding="utf-8")

# Find the start: body div inside code-examples (after the section header)
# and the end: the </section> that closes code-examples
start_marker = '    <div class="bg-white px-8 py-7 space-y-6">'
end_marker = '</section>\n\n<section id="comparison">'

# Locate start and end positions
start_idx = html.find(start_marker, html.find('<section id="code-examples">'))
if start_idx == -1:
    print("❌ Start marker not found")
    exit(1)

# Find the </section> after this body div
end_idx = html.find('</section>', start_idx)
if end_idx == -1:
    print("❌ End marker not found")
    exit(1)

end_idx_full = end_idx + len('</section>')

old_block = html[start_idx:end_idx_full]
new_html = html[:start_idx] + NEW_BODY + html[end_idx_full:]

TARGET.write_text(new_html, encoding="utf-8")
print(f"✅ Replaced {len(old_block)} chars with {len(NEW_BODY)} chars")
print(f"   File size: {len(new_html)} chars")
