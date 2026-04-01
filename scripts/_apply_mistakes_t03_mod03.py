#!/usr/bin/env python3
"""
Rewrite <section id="mistakes"> for all 14 lessons in
track_03 / mod_03_api_data_integration.
"""

import re, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
MOD = BASE / "pages" / "track_03_data_engineering" / "mod_03_api_data_integration"

SECTION_RE = re.compile(
    r'(<section id="mistakes">).*?(</section>)',
    re.DOTALL,
)

LESSONS = {
    # ── Lesson 01: What Is an API ──
    "lesson01_what_is_an_api.html": {
        "topic": "API fundamentals",
        "mistakes": [
            {
                "tab": "Calling Without Reading Docs",
                "title": "Calling an API Endpoint Without Reading the Documentation First",
                "subtitle": "Blind requests return confusing errors or unexpected data shapes.",
                "explanation": 'Every API has its own URL structure, required parameters, and response format. Guessing the endpoint path or skipping the docs means you waste time debugging 404 and 400 errors that the documentation answers in seconds.',
                "wrong_label": "guessing the endpoint",
                "wrong_code": 'import requests\n# Guessing the URL\nresp = requests.get("https://api.example.com/data")\nprint(resp.json())  # 404 — endpoint does not exist',
                "correct_label": "check the docs first",
                "correct_code": 'import requests\n# URL from the API documentation\nurl = "https://api.example.com/v2/users"\nresp = requests.get(url)\nprint(resp.json())  # correct endpoint, clean data',
                "tip": "Bookmark the API documentation page before writing any code. Ten minutes of reading saves hours of trial and error.",
            },
            {
                "tab": "Ignoring Status Codes",
                "title": "Ignoring the HTTP Status Code in the Response",
                "subtitle": "Your code processes garbage data when the request actually failed.",
                "explanation": 'A response with status <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">200</code> means success. Anything else — <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">401</code>, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">404</code>, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">500</code> — means something went wrong. Always check the status code before processing the body.',
                "wrong_label": "skip status check",
                "wrong_code": 'resp = requests.get(url)\ndata = resp.json()  # crashes if response is an error page',
                "correct_label": "check status first",
                "correct_code": 'resp = requests.get(url)\nresp.raise_for_status()  # raises an exception on 4xx/5xx\ndata = resp.json()       # safe to parse',
                "tip": "Call <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">raise_for_status()</code> immediately after every request. It turns silent failures into clear error messages.",
            },
            {
                "tab": "Hardcoding URLs",
                "title": "Hardcoding the Full API URL in Every Request",
                "subtitle": "Changing the base URL later means editing every line that makes a call.",
                "explanation": 'If the API version changes from <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">v1</code> to <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">v2</code>, you need to update every hardcoded URL. Store the base URL in a variable or config file and build endpoints from it.',
                "wrong_label": "hardcoded everywhere",
                "wrong_code": 'resp1 = requests.get("https://api.example.com/v1/users")\nresp2 = requests.get("https://api.example.com/v1/orders")\n# version changes → edit every line',
                "correct_label": "base URL variable",
                "correct_code": 'BASE = "https://api.example.com/v1"\nresp1 = requests.get(f"{BASE}/users")\nresp2 = requests.get(f"{BASE}/orders")\n# version changes → edit one line',
                "tip": "Store the base URL at the top of your script or in an environment variable. One change point is always better than many.",
            },
        ],
    },

    # ── Lesson 02: Understanding HTTP Requests ──
    "lesson02_understanding_http_requests.html": {
        "topic": "HTTP requests",
        "mistakes": [
            {
                "tab": "GET for Side Effects",
                "title": "Using GET Requests to Create or Modify Data",
                "subtitle": "GET should only read data — using it to write violates HTTP conventions and can cause accidental changes.",
                "explanation": 'HTTP methods have meanings: <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">GET</code> reads, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">POST</code> creates, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">PUT</code> updates, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">DELETE</code> removes. Sending data in a GET query string to create a record breaks caching, bookmarking, and browser behaviour.',
                "wrong_label": "GET to create data",
                "wrong_code": '# Sending data via GET query string\nrequests.get(url, params={"name": "Alice", "action": "create"})\n# Not idempotent — browser prefetch could trigger it',
                "correct_label": "POST to create data",
                "correct_code": '# POST with a JSON body\nrequests.post(url, json={"name": "Alice"})\n# clearly signals a write operation',
                "tip": "If the request changes anything on the server, use POST, PUT, or DELETE — never GET. GET requests should be safe to repeat without side effects.",
            },
            {
                "tab": "Not Setting Timeout",
                "title": "Making Requests Without a Timeout",
                "subtitle": "Your script hangs forever if the server does not respond.",
                "explanation": 'By default, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">requests.get()</code> waits indefinitely. If the server is slow or unreachable, your program freezes. Always pass a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">timeout</code> parameter.',
                "wrong_label": "no timeout",
                "wrong_code": 'resp = requests.get(url)  # hangs if server is down',
                "correct_label": "set a timeout",
                "correct_code": 'resp = requests.get(url, timeout=10)  # fails after 10s\n# your script stays responsive',
                "tip": "A timeout of 10–30 seconds is a safe default for most APIs. For slow endpoints, increase it — but never leave it out entirely.",
            },
            {
                "tab": "Ignoring Response Headers",
                "title": "Ignoring Response Headers That Carry Important Metadata",
                "subtitle": "Headers tell you the content type, rate limit status, and pagination links.",
                "explanation": 'The response body is not the only useful part. Headers like <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">Content-Type</code>, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">X-RateLimit-Remaining</code>, and <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">Link</code> tell you how to parse the data, when to slow down, and where the next page is.',
                "wrong_label": "ignore headers",
                "wrong_code": 'resp = requests.get(url)\ndata = resp.json()  # works, but misses rate-limit info',
                "correct_label": "read useful headers",
                "correct_code": 'resp = requests.get(url)\nremaining = resp.headers.get("X-RateLimit-Remaining")\nprint(f"Calls left: {remaining}")\ndata = resp.json()',
                "tip": "Print <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">resp.headers</code> once during development to see what the API sends back. You may find pagination links, cache hints, and rate-limit counters.",
            },
        ],
    },

    # ── Lesson 03: Using the Python Requests Library ──
    "lesson03_using_the_python_requests_library.html": {
        "topic": "the Python requests library",
        "mistakes": [
            {
                "tab": "Not Installing requests",
                "title": "Trying to Import requests Without Installing It First",
                "subtitle": "requests is not part of the Python standard library — it needs pip install.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">requests</code> must be installed separately via <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pip install requests</code>. Beginners often assume it comes with Python and get a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">ModuleNotFoundError</code>.',
                "wrong_label": "import without install",
                "wrong_code": 'import requests  # ModuleNotFoundError\nresp = requests.get("https://api.example.com")',
                "correct_label": "install first",
                "correct_code": '# In terminal: pip install requests\nimport requests\nresp = requests.get("https://api.example.com")',
                "tip": "Add <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">requests</code> to your project's <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">requirements.txt</code> so teammates can install all dependencies with one command.",
            },
            {
                "tab": "String Concatenation for Params",
                "title": "Building Query Strings by Concatenating Strings Manually",
                "subtitle": "Manual concatenation breaks when values contain special characters like spaces or ampersands.",
                "explanation": 'The <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">params</code> argument handles URL-encoding automatically. Manually gluing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">?key=value&amp;key2=val</code> into the URL skips encoding and can produce invalid URLs.',
                "wrong_label": "manual concatenation",
                "wrong_code": 'url = "https://api.example.com/search?q=" + query\n# breaks if query contains & or spaces',
                "correct_label": "use params argument",
                "correct_code": 'resp = requests.get(\n    "https://api.example.com/search",\n    params={"q": query}  # auto-encoded\n)',
                "tip": "Never build query strings by hand. The <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">params</code> dict handles encoding, spaces, and special characters for you.",
            },
            {
                "tab": "POST With params Instead of json",
                "title": "Sending POST Data as Query Parameters Instead of a JSON Body",
                "subtitle": "Most APIs expect POST data in the request body, not the URL.",
                "explanation": 'Using <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">params</code> in a POST request puts data in the URL query string. Most APIs expect the data in the body as JSON. Use the <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">json</code> keyword to send a proper request body.',
                "wrong_label": "data in query string",
                "wrong_code": 'requests.post(url, params={"name": "Alice"})\n# data goes in URL, not body — API ignores it',
                "correct_label": "data in JSON body",
                "correct_code": 'requests.post(url, json={"name": "Alice"})\n# data goes in body — API processes it',
                "tip": "Use <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">json=</code> for POST payloads. It sets the <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">Content-Type</code> header to <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">application/json</code> automatically.",
            },
        ],
    },

    # ── Lesson 04: Working With JSON Data ──
    "lesson04_working_with_json_data.html": {
        "topic": "JSON data",
        "mistakes": [
            {
                "tab": "Accessing Nested Keys Blindly",
                "title": "Accessing Nested JSON Keys Without Checking They Exist",
                "subtitle": "A missing key raises a KeyError and crashes your script.",
                "explanation": 'API responses often have optional fields. Accessing <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">data["user"]["email"]</code> fails when <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">"user"</code> is missing. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.get()</code> with a default value to handle absent keys safely.',
                "wrong_label": "direct key access",
                "wrong_code": 'data = resp.json()\nemail = data["user"]["email"]  # KeyError if "user" missing',
                "correct_label": "safe .get() access",
                "correct_code": 'data = resp.json()\nuser = data.get("user", {})\nemail = user.get("email", "N/A")  # safe fallback',
                "tip": "Chain <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.get()</code> calls when navigating nested JSON. A missing key returns the default instead of crashing.",
            },
            {
                "tab": "Parsing JSON Twice",
                "title": "Calling json.loads() on a Response That Is Already Parsed",
                "subtitle": "resp.json() returns a Python dict — calling json.loads() on it raises a TypeError.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">resp.json()</code> already deserialises the JSON string into a dict. Passing that dict to <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">json.loads()</code> is double-parsing and throws an error because <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">loads()</code> expects a string, not a dict.',
                "wrong_label": "double-parse",
                "wrong_code": 'import json\ndata = resp.json()             # already a dict\nparsed = json.loads(data)      # TypeError',
                "correct_label": "parse once",
                "correct_code": 'data = resp.json()  # returns a Python dict\nprint(data["name"]) # use directly',
                "tip": "Use <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">resp.json()</code> to parse and <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">json.loads()</code> only when you have a raw JSON string from a file or a non-requests source.",
            },
            {
                "tab": "Printing the Whole Response",
                "title": "Printing the Entire JSON Response Instead of Extracting What You Need",
                "subtitle": "Large API responses produce walls of text that hide the fields you actually need.",
                "explanation": 'Dumping the entire response is fine for one-time debugging, but in production code you should extract specific fields. This makes logs cleaner and exposes only the data your downstream code depends on.',
                "wrong_label": "print everything",
                "wrong_code": 'data = resp.json()\nprint(data)  # 500 lines of nested JSON',
                "correct_label": "extract what you need",
                "correct_code": 'data = resp.json()\nprint(data["name"], data["status"])  # just two fields',
                "tip": "During development, use <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">json.dumps(data, indent=2)</code> to pretty-print. In production, extract only the fields you process.",
            },
        ],
    },

    # ── Lesson 05: Parsing API Responses ──
    "lesson05_parsing_api_responses.html": {
        "topic": "parsing API responses",
        "mistakes": [
            {
                "tab": "Assuming JSON Format",
                "title": "Assuming Every API Returns JSON Without Checking Content-Type",
                "subtitle": "Some APIs return XML, plain text, or HTML — calling .json() on those crashes.",
                "explanation": 'Not all APIs return JSON. The <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">Content-Type</code> header tells you the format. Calling <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.json()</code> on an XML or HTML response throws a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">JSONDecodeError</code>.',
                "wrong_label": "assume JSON",
                "wrong_code": 'resp = requests.get(url)\ndata = resp.json()  # JSONDecodeError if response is XML',
                "correct_label": "check Content-Type first",
                "correct_code": 'resp = requests.get(url)\nif "application/json" in resp.headers.get("Content-Type", ""):\n    data = resp.json()\nelse:\n    data = resp.text  # handle non-JSON',
                "tip": "Always check the <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">Content-Type</code> header before parsing. It takes one line and prevents cryptic decode errors.",
            },
            {
                "tab": "Ignoring Empty Responses",
                "title": "Trying to Parse an Empty Response Body",
                "subtitle": "Some successful responses (204 No Content) have no body to parse.",
                "explanation": 'A <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">204</code> status means the server processed your request but has nothing to send back. Calling <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.json()</code> on an empty body raises a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">JSONDecodeError</code>. Check the status code first.',
                "wrong_label": "parse empty body",
                "wrong_code": 'resp = requests.delete(url)\ndata = resp.json()  # JSONDecodeError — body is empty',
                "correct_label": "check before parsing",
                "correct_code": 'resp = requests.delete(url)\nif resp.status_code == 204:\n    print("Deleted successfully")  # no body expected\nelse:\n    data = resp.json()',
                "tip": "After DELETE and some PUT requests, a 204 response is normal and means success. Do not try to parse what is not there.",
            },
            {
                "tab": "Flat Parsing of Nested Data",
                "title": "Treating Nested API Data as Flat When Extracting Fields",
                "subtitle": "The data you need is often inside a nested key like \"results\" or \"data\".",
                "explanation": 'Many APIs wrap results in an envelope: <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">{"data": [...], "meta": {...}}</code>. Treating the top-level object as the list itself gives you a dict instead of rows, breaking downstream loops.',
                "wrong_label": "wrong level",
                "wrong_code": 'data = resp.json()\nfor item in data:          # iterates over keys, not records\n    print(item["name"])    # KeyError',
                "correct_label": "navigate to the list",
                "correct_code": 'data = resp.json()\nfor item in data["results"]:  # correct nested key\n    print(item["name"])',
                "tip": "Print the top-level keys of the response once to see the structure. Most APIs use <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">\"data\"</code>, <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">\"results\"</code>, or <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">\"items\"</code> as the list wrapper.",
            },
        ],
    },

    # ── Lesson 06: Authentication With API Keys ──
    "lesson06_authentication_with_api_keys.html": {
        "topic": "API key authentication",
        "mistakes": [
            {
                "tab": "Key in Source Code",
                "title": "Hardcoding the API Key Directly in Your Script",
                "subtitle": "Anyone who sees your code — including version control — gets your key.",
                "explanation": 'Pushing a script with a hardcoded API key to GitHub exposes it to the public. Bots scan public repositories and exploit leaked keys within minutes. Store keys in environment variables or a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.env</code> file that is git-ignored.',
                "wrong_label": "key in source code",
                "wrong_code": 'API_KEY = "sk-abc123secret"  # exposed in Git\nresp = requests.get(url, headers={"Authorization": API_KEY})',
                "correct_label": "key from environment variable",
                "correct_code": 'import os\nAPI_KEY = os.getenv("API_KEY")  # loaded at runtime\nresp = requests.get(url, headers={"Authorization": API_KEY})',
                "tip": "Add your <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.env</code> file to <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.gitignore</code> immediately after creating it. Once a key is in Git history, rotating it is the only safe option.",
            },
            {
                "tab": "Key in Query String",
                "title": "Sending the API Key as a Query Parameter When Headers Are Supported",
                "subtitle": "Query parameters appear in browser history, server logs, and proxy logs.",
                "explanation": 'Some APIs accept keys in the URL like <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">?api_key=XYZ</code>, but headers are more secure because they are not logged by default. If the API supports header-based auth, always prefer it.',
                "wrong_label": "key in URL",
                "wrong_code": 'resp = requests.get(f"{url}?api_key={API_KEY}")\n# key visible in logs and browser history',
                "correct_label": "key in header",
                "correct_code": 'resp = requests.get(url, headers={\n    "X-API-Key": API_KEY   # not logged by default\n})',
                "tip": "Check the API docs for the recommended authentication method. Most modern APIs prefer the <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">Authorization</code> or a custom header over query parameters.",
            },
            {
                "tab": "No Key Rotation Plan",
                "title": "Using the Same API Key Indefinitely Without a Rotation Plan",
                "subtitle": "A compromised key stays valid forever if you never rotate it.",
                "explanation": 'API keys should be rotated periodically — at minimum once a quarter — and immediately after any suspected leak. Without a rotation plan, a stolen key gives an attacker permanent access.',
                "wrong_label": "same key forever",
                "wrong_code": '# Key created in 2022, never changed\nAPI_KEY = os.getenv("API_KEY")  # same key for 3 years',
                "correct_label": "rotation schedule",
                "correct_code": '# .env file — rotate every 90 days\nAPI_KEY = os.getenv("API_KEY")  # updated on schedule\n# Old key: revoked in the API dashboard',
                "tip": "Set a calendar reminder to rotate API keys every 90 days. When you rotate, revoke the old key in the provider dashboard to confirm it is no longer valid.",
            },
        ],
    },

    # ── Lesson 07: OAuth Authentication ──
    "lesson07_oauth_authentication.html": {
        "topic": "OAuth authentication",
        "mistakes": [
            {
                "tab": "Token in Source Code",
                "title": "Hardcoding OAuth Tokens in Your Script",
                "subtitle": "OAuth tokens are credentials — treat them exactly like passwords.",
                "explanation": 'An OAuth access token grants the same access as a password for the duration of its validity. Hardcoding it in source code or committing it to version control exposes your account to anyone who can read the repository.',
                "wrong_label": "token in code",
                "wrong_code": 'TOKEN = "ya29.a0Af...long_token_here"\nresp = requests.get(url, headers={\n    "Authorization": f"Bearer {TOKEN}"\n})',
                "correct_label": "token from environment",
                "correct_code": 'import os\nTOKEN = os.getenv("OAUTH_TOKEN")\nresp = requests.get(url, headers={\n    "Authorization": f"Bearer {TOKEN}"\n})',
                "tip": "Store the token in an environment variable or a secret manager. Never commit tokens to Git — even in private repositories.",
            },
            {
                "tab": "Ignoring Token Expiry",
                "title": "Not Handling Token Expiry and Refresh",
                "subtitle": "Access tokens expire — your script breaks silently when they do.",
                "explanation": 'Most OAuth access tokens expire after 30–60 minutes. If your script runs longer than that, subsequent requests fail with a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">401 Unauthorized</code>. Check for expiry and use the refresh token to get a new access token.',
                "wrong_label": "no expiry handling",
                "wrong_code": 'resp = requests.get(url, headers=headers)\n# 401 after token expires — script crashes',
                "correct_label": "refresh on expiry",
                "correct_code": 'resp = requests.get(url, headers=headers)\nif resp.status_code == 401:\n    token = refresh_access_token(refresh_token)\n    headers["Authorization"] = f"Bearer {token}"\n    resp = requests.get(url, headers=headers)',
                "tip": "Always store the refresh token alongside the access token. When you get a 401, refresh automatically instead of failing.",
            },
            {
                "tab": "Too Many Scopes",
                "title": "Requesting All Available OAuth Scopes Instead of the Minimum Needed",
                "subtitle": "Broad scopes give your application more access than it needs, increasing risk.",
                "explanation": 'OAuth scopes limit what your token can do. Requesting <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">read write admin</code> when you only need <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">read</code> means a leaked token can modify or delete data. Follow the principle of least privilege.',
                "wrong_label": "all scopes",
                "wrong_code": '# Requesting every scope available\nscope = "read write admin delete"\nauth_url = f"{base}/authorize?scope={scope}"',
                "correct_label": "minimum scopes",
                "correct_code": '# Only request what you need\nscope = "read"\nauth_url = f"{base}/authorize?scope={scope}"',
                "tip": "Start with the narrowest scope and add more only when you actually need them. A read-only token cannot accidentally delete data.",
            },
        ],
    },

    # ── Lesson 08: Handling Pagination in APIs ──
    "lesson08_handling_pagination_in_apis.html": {
        "topic": "API pagination",
        "mistakes": [
            {
                "tab": "Only First Page",
                "title": "Fetching Only the First Page and Missing the Rest of the Data",
                "subtitle": "Most APIs return a limited number of results per request and paginate the rest.",
                "explanation": 'If an API returns 20 items per page and the dataset has 200 records, a single request gives you only 10% of the data. You must loop through pages until there are no more results.',
                "wrong_label": "one page only",
                "wrong_code": 'resp = requests.get(url)\ndata = resp.json()["results"]  # only first 20 items\n# 180 records missing',
                "correct_label": "loop through all pages",
                "correct_code": 'all_data = []\npage = 1\nwhile True:\n    resp = requests.get(url, params={"page": page})\n    items = resp.json()["results"]\n    if not items:\n        break\n    all_data.extend(items)\n    page += 1',
                "tip": "Check the API docs for pagination style: page numbers, cursors, or next-page links. Each style needs a slightly different loop.",
            },
            {
                "tab": "Ignoring next Link",
                "title": "Ignoring the next URL Provided in the Response",
                "subtitle": "Many APIs include a ready-made URL for the next page — rebuilding it manually is error-prone.",
                "explanation": 'APIs that return a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">"next"</code> link in the response body or headers have already built the correct URL for you. Manually incrementing page numbers can drift out of sync with the API\u2019s actual cursor position.',
                "wrong_label": "ignore next link",
                "wrong_code": 'page = 1\nwhile True:\n    resp = requests.get(url, params={"page": page})\n    page += 1  # may skip or repeat pages',
                "correct_label": "follow next link",
                "correct_code": 'next_url = url\nwhile next_url:\n    resp = requests.get(next_url)\n    data = resp.json()\n    process(data["results"])\n    next_url = data.get("next")  # None when done',
                "tip": "Using the API\u2019s own next link is idiomatic and avoids off-by-one errors. Always prefer it when available.",
            },
            {
                "tab": "No Delay Between Pages",
                "title": "Requesting Pages as Fast as Possible Without Any Delay",
                "subtitle": "Rapid-fire pagination triggers rate limits and blocks your IP.",
                "explanation": 'Looping through hundreds of pages at full speed floods the API with requests. Many APIs will return a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">429 Too Many Requests</code> error and temporarily block you. Add a small delay between page fetches.',
                "wrong_label": "no delay",
                "wrong_code": 'while next_url:\n    resp = requests.get(next_url)\n    # fires as fast as possible — gets rate-limited',
                "correct_label": "add a delay",
                "correct_code": 'import time\nwhile next_url:\n    resp = requests.get(next_url)\n    process(resp.json())\n    next_url = resp.json().get("next")\n    time.sleep(0.5)  # polite half-second pause',
                "tip": "A <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">time.sleep(0.5)</code> between pages is usually enough to stay under rate limits. Check the API\u2019s rate-limit headers to tune the delay.",
            },
        ],
    },

    # ── Lesson 09: Handling API Rate Limits ──
    "lesson09_handling_api_rate_limits.html": {
        "topic": "API rate limits",
        "mistakes": [
            {
                "tab": "Ignoring 429 Responses",
                "title": "Continuing to Send Requests After Receiving a 429 Status",
                "subtitle": "Ignoring 429 means every subsequent request also fails — and may extend the block.",
                "explanation": 'A <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">429 Too Many Requests</code> means the API is telling you to stop. Continuing to send requests wastes time and can extend the cool-down period or get your key permanently banned.',
                "wrong_label": "ignore 429",
                "wrong_code": 'for item in items:\n    resp = requests.get(url)\n    # 429 returned — loop keeps going anyway\n    data = resp.json()  # error response, not data',
                "correct_label": "detect and wait",
                "correct_code": 'for item in items:\n    resp = requests.get(url)\n    if resp.status_code == 429:\n        wait = int(resp.headers.get("Retry-After", 60))\n        time.sleep(wait)\n        resp = requests.get(url)  # retry after waiting\n    data = resp.json()',
                "tip": "Always check the <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">Retry-After</code> header in a 429 response. It tells you exactly how long to wait before sending the next request.",
            },
            {
                "tab": "Fixed Sleep Instead of Backoff",
                "title": "Using a Fixed Sleep Time Instead of Exponential Backoff",
                "subtitle": "A fixed delay does not adapt when the API needs more recovery time.",
                "explanation": 'Sleeping for exactly 1 second every time may not be enough when the API is under heavy load. Exponential backoff doubles the wait after each consecutive failure, giving the server time to recover without wasting yours.',
                "wrong_label": "fixed delay",
                "wrong_code": 'while resp.status_code == 429:\n    time.sleep(1)  # same wait every time\n    resp = requests.get(url)',
                "correct_label": "exponential backoff",
                "correct_code": 'wait = 1\nwhile resp.status_code == 429:\n    time.sleep(wait)\n    wait = min(wait * 2, 60)  # double, cap at 60s\n    resp = requests.get(url)',
                "tip": "Start with a 1-second wait and double it on each failure. Cap the maximum at 60 seconds to avoid waiting forever.",
            },
            {
                "tab": "Not Checking Rate-Limit Headers",
                "title": "Not Proactively Checking Rate-Limit Headers Before Hitting the Limit",
                "subtitle": "You can slow down before getting blocked instead of reacting after the fact.",
                "explanation": 'Most APIs return <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">X-RateLimit-Remaining</code> and <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">X-RateLimit-Reset</code> headers on every response. Checking them lets you throttle proactively ​— slowing down before you hit the wall instead of crashing into it.',
                "wrong_label": "react after 429",
                "wrong_code": '# Only notices the limit after being blocked\nresp = requests.get(url)\nif resp.status_code == 429:\n    time.sleep(60)',
                "correct_label": "throttle proactively",
                "correct_code": 'resp = requests.get(url)\nremaining = int(resp.headers.get("X-RateLimit-Remaining", 100))\nif remaining < 5:\n    time.sleep(10)  # slow down before hitting the limit',
                "tip": "Log the <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">X-RateLimit-Remaining</code> value during development. It tells you how close you are to the limit before you are actually blocked.",
            },
        ],
    },

    # ── Lesson 10: Loading API Data Into Pandas ──
    "lesson10_loading_api_data_into_pandas.html": {
        "topic": "loading API data into pandas",
        "mistakes": [
            {
                "tab": "Passing Raw Response",
                "title": "Passing the Raw Response Object to pd.DataFrame Instead of the JSON Data",
                "subtitle": "pd.DataFrame needs a list of dicts, not a requests Response object.",
                "explanation": '<code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.DataFrame()</code> expects a list of dictionaries or a dict of lists. Passing the raw <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">Response</code> object creates a single-row DataFrame with useless columns. Call <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.json()</code> first.',
                "wrong_label": "raw response object",
                "wrong_code": 'import pandas as pd\nresp = requests.get(url)\ndf = pd.DataFrame(resp)  # wrong input type',
                "correct_label": "parsed JSON data",
                "correct_code": 'resp = requests.get(url)\ndata = resp.json()["results"]  # list of dicts\ndf = pd.DataFrame(data)         # correct input',
                "tip": "Always extract the list of records from the JSON before creating the DataFrame. Print the top-level keys first to find where the records live.",
            },
            {
                "tab": "Not Flattening Nested JSON",
                "title": "Loading Nested JSON Directly Without Flattening It",
                "subtitle": "Nested dicts become single cells in the DataFrame instead of separate columns.",
                "explanation": 'When a JSON record contains nested objects like <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">{"user": {"name": "Alice"}}</code>, <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.DataFrame()</code> puts the entire nested dict into one cell. Use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">pd.json_normalize()</code> to flatten it into proper columns.',
                "wrong_label": "nested dicts in cells",
                "wrong_code": 'df = pd.DataFrame(data)\n# df["user"] contains {\"name\": \"Alice\"} in each cell',
                "correct_label": "flatten with json_normalize",
                "correct_code": 'df = pd.json_normalize(data)\n# df["user.name"] = "Alice" — proper flat columns',
                "tip": "Use <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">pd.json_normalize()</code> whenever the JSON has nested objects. It creates dot-separated column names like <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">user.name</code>.",
            },
            {
                "tab": "Loading Incomplete Pages",
                "title": "Building a DataFrame From Only the First Page of a Paginated API",
                "subtitle": "Your DataFrame contains a fraction of the total records.",
                "explanation": 'If you call the API once and convert to a DataFrame, you get only the first page. Collect all pages into a list first, then build the DataFrame from the combined data.',
                "wrong_label": "first page only",
                "wrong_code": 'resp = requests.get(url)\ndf = pd.DataFrame(resp.json()["results"])  # one page',
                "correct_label": "all pages combined",
                "correct_code": 'all_records = []\npage = 1\nwhile True:\n    resp = requests.get(url, params={"page": page})\n    items = resp.json()["results"]\n    if not items:\n        break\n    all_records.extend(items)\n    page += 1\ndf = pd.DataFrame(all_records)  # complete dataset',
                "tip": "Collect all pages into a plain list, then create the DataFrame once at the end. Creating a DataFrame per page and concatenating is slower and uses more memory.",
            },
        ],
    },

    # ── Lesson 11: Saving API Data to Databases ──
    "lesson11_saving_api_data_to_databases.html": {
        "topic": "saving API data to databases",
        "mistakes": [
            {
                "tab": "Appending Duplicates",
                "title": "Appending API Records to the Database Without Checking for Duplicates",
                "subtitle": "Rerunning your script creates duplicate rows in the table.",
                "explanation": 'Using <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">if_exists="append"</code> without deduplication means every run adds another copy of the same records. Check for existing keys or use <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">if_exists="replace"</code> for small tables, or implement an upsert for large ones.',
                "wrong_label": "blind append",
                "wrong_code": 'df.to_sql("orders", engine, if_exists="append")\n# rerun → duplicate rows',
                "correct_label": "replace or upsert",
                "correct_code": '# Simple approach — replace entire table\ndf.to_sql("orders", engine, if_exists="replace", index=False)\n# Or deduplicate first\ndf = df.drop_duplicates(subset=["order_id"])',
                "tip": "For small datasets, <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">if_exists=\"replace\"</code> is the simplest solution. For large tables, implement an upsert using a staging table and SQL MERGE.",
            },
            {
                "tab": "No Error Handling on Write",
                "title": "Writing to the Database Without Try/Except",
                "subtitle": "A database connection error or constraint violation crashes your pipeline silently.",
                "explanation": 'Database writes can fail for many reasons: connection timeouts, unique constraint violations, disk full. Without <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">try/except</code>, your script crashes and you lose the data you just fetched from the API.',
                "wrong_label": "no error handling",
                "wrong_code": 'df.to_sql("orders", engine, if_exists="append")\n# IntegrityError → script crashes, data lost',
                "correct_label": "catch and log errors",
                "correct_code": 'try:\n    df.to_sql("orders", engine, if_exists="append", index=False)\nexcept Exception as err:\n    print(f"DB write failed: {err}")\n    df.to_csv("fallback_orders.csv", index=False)',
                "tip": "Always save a fallback copy (CSV or JSON) when the database write fails. You can retry the load later without re-fetching from the API.",
            },
            {
                "tab": "Wrong Data Types",
                "title": "Letting Pandas Guess the SQL Column Types Instead of Specifying Them",
                "subtitle": "Pandas defaults to TEXT for strings and REAL for numbers, which may not match your schema.",
                "explanation": 'When <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">to_sql()</code> creates a table automatically, it picks generic types. Dates become TEXT, integers become REAL, and you lose indexing efficiency. Specify <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">dtype</code> to control the SQL types.',
                "wrong_label": "auto types",
                "wrong_code": 'df.to_sql("orders", engine, if_exists="replace")\n# date column stored as TEXT — cannot sort by date',
                "correct_label": "explicit types",
                "correct_code": 'from sqlalchemy import types\ndf.to_sql("orders", engine, if_exists="replace",\n          dtype={"order_date": types.Date(),\n                 "amount": types.Float()},\n          index=False)',
                "tip": "Define your table schema once with explicit types. It makes queries faster and prevents silent type mismatches.",
            },
        ],
    },

    # ── Lesson 12: Building an API Data Pipeline ──
    "lesson12_building_an_api_data_pipeline.html": {
        "topic": "API data pipelines",
        "mistakes": [
            {
                "tab": "No Separation of Stages",
                "title": "Writing Extract, Transform, and Load in One Monolithic Block",
                "subtitle": "A single block is hard to test, debug, and rerun partially.",
                "explanation": 'When extract, transform, and load are tangled together, a bug in the transform step forces you to re-fetch all data from the API. Separate each stage into its own function so you can test and rerun them independently.',
                "wrong_label": "all in one block",
                "wrong_code": 'resp = requests.get(url)\ndata = resp.json()["results"]\ndf = pd.DataFrame(data)\ndf["total"] = df["price"] * df["qty"]\ndf.to_sql("sales", engine)',
                "correct_label": "separate functions",
                "correct_code": 'def extract():\n    resp = requests.get(url)\n    return resp.json()["results"]\ndef transform(data):\n    df = pd.DataFrame(data)\n    df["total"] = df["price"] * df["qty"]\n    return df\ndef load(df):\n    df.to_sql("sales", engine, if_exists="replace")',
                "tip": "Each pipeline stage should be a function you can call and test on its own. If extract fails, you should not have to rewrite transform and load.",
            },
            {
                "tab": "No Logging",
                "title": "Not Logging Pipeline Progress or Errors",
                "subtitle": "When the pipeline fails at 3 AM, you have no record of what happened.",
                "explanation": 'Print statements disappear when a script runs as a scheduled job. Use Python\u2019s <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">logging</code> module to record timestamps, row counts, and errors to a log file.',
                "wrong_label": "no logging",
                "wrong_code": 'data = extract()\ndf = transform(data)\nload(df)\n# fails silently at 3 AM — no trace',
                "correct_label": "with logging",
                "correct_code": 'import logging\nlogging.basicConfig(filename="pipeline.log", level=logging.INFO)\ndata = extract()\nlogging.info(f"Extracted {len(data)} records")\ndf = transform(data)\nlogging.info(f"Transformed — {len(df)} rows")\nload(df)\nlogging.info("Load complete")',
                "tip": "Log the row count after every stage. A sudden drop or zero tells you exactly where the pipeline broke.",
            },
            {
                "tab": "No Retry on Failure",
                "title": "Letting the Pipeline Fail on the First API Error Without Retrying",
                "subtitle": "Transient network errors are common — one failure should not kill the whole run.",
                "explanation": 'APIs occasionally return 500 errors or timeout. A single retry with a short wait often succeeds. Without retry logic, your pipeline fails and needs manual intervention for a temporary blip.',
                "wrong_label": "no retries",
                "wrong_code": 'resp = requests.get(url)\nresp.raise_for_status()  # 500 → pipeline dies',
                "correct_label": "retry with backoff",
                "correct_code": 'for attempt in range(3):\n    resp = requests.get(url, timeout=10)\n    if resp.status_code == 200:\n        break\n    time.sleep(2 ** attempt)  # 1s, 2s, 4s\nresp.raise_for_status()',
                "tip": "Three retries with exponential backoff handle most transient failures. If all three fail, the error is genuine and should be logged.",
            },
        ],
    },

    # ── Lesson 13: Real-World API Integration Project ──
    "lesson13_real_world_api_integration_project.html": {
        "topic": "real-world API integration",
        "mistakes": [
            {
                "tab": "Skipping Error Handling",
                "title": "Skipping Error Handling Because It Is 'Just a Project'",
                "subtitle": "Even project code should handle errors gracefully to produce reliable results.",
                "explanation": 'A project pipeline that crashes on the first bad record teaches you nothing about recovery. Adding try/except and fallback logic is part of the learning objective — it mirrors what you will do in every production pipeline.',
                "wrong_label": "no error handling",
                "wrong_code": 'for endpoint in endpoints:\n    resp = requests.get(endpoint)\n    data.append(resp.json())  # crashes on any failure',
                "correct_label": "handle errors per request",
                "correct_code": 'for endpoint in endpoints:\n    try:\n        resp = requests.get(endpoint, timeout=10)\n        resp.raise_for_status()\n        data.append(resp.json())\n    except requests.RequestException as err:\n        logging.warning(f"Skipped {endpoint}: {err}")',
                "tip": "Treat project code as production code. The habits you build now — error handling, logging, retries — carry over to every pipeline you write at work.",
            },
            {
                "tab": "Credentials in the Repo",
                "title": "Committing API Credentials to the Project Repository",
                "subtitle": "Even private repos can be shared or forked, exposing your keys.",
                "explanation": 'Storing credentials in a Python file or config that gets committed to Git is a security risk. Use a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.env</code> file, add it to <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">.gitignore</code>, and load values with <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">os.getenv()</code>.',
                "wrong_label": "credentials in code",
                "wrong_code": 'config = {\n    "api_key": "sk-secret123",\n    "db_password": "admin123"\n}  # committed to Git',
                "correct_label": "credentials from .env",
                "correct_code": 'import os\nconfig = {\n    "api_key": os.getenv("API_KEY"),\n    "db_password": os.getenv("DB_PASS")\n}  # .env file in .gitignore',
                "tip": "Create the <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.gitignore</code> entry before creating the <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">.env</code> file. That way the secret file is never tracked, even accidentally.",
            },
            {
                "tab": "No Data Validation",
                "title": "Loading API Data Into the Database Without Validating It First",
                "subtitle": "Null values, wrong types, and duplicates slip into your tables unnoticed.",
                "explanation": 'APIs can return unexpected data: missing fields, empty strings, or changed formats. Validate records before writing them to the database to keep your tables clean and your downstream queries reliable.',
                "wrong_label": "load without checks",
                "wrong_code": 'df = pd.DataFrame(api_data)\ndf.to_sql("records", engine, if_exists="append")\n# nulls and duplicates are now in the table',
                "correct_label": "validate before loading",
                "correct_code": 'df = pd.DataFrame(api_data)\ndf = df.dropna(subset=["id", "date"])     # remove nulls\ndf = df.drop_duplicates(subset=["id"])     # remove dupes\nassert len(df) > 0, "No valid records"\ndf.to_sql("records", engine, if_exists="append", index=False)',
                "tip": "Add at least three checks before any database write: no nulls in key columns, no duplicate keys, and at least one record remaining. These catch the most common data problems.",
            },
        ],
    },

    # ── Lesson 14: API Best Practices ──
    "lesson14_api_best_practices.html": {
        "topic": "API best practices",
        "mistakes": [
            {
                "tab": "No Timeout on Requests",
                "title": "Leaving the Default Infinite Timeout on Every Request",
                "subtitle": "A hung request blocks your pipeline forever.",
                "explanation": 'The <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">requests</code> library waits indefinitely by default. In a pipeline, a single stuck request halts everything. Always set a <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">timeout</code> so the script can recover and retry.',
                "wrong_label": "no timeout",
                "wrong_code": 'resp = requests.get(url)  # waits forever if server hangs',
                "correct_label": "explicit timeout",
                "correct_code": 'resp = requests.get(url, timeout=15)  # fails after 15s',
                "tip": "Set timeout on every request, not just the ones you think might be slow. Any server can hang at any time.",
            },
            {
                "tab": "Logging Secrets",
                "title": "Logging Full Request Headers That Contain API Keys",
                "subtitle": "Your log file becomes a plaintext copy of your credentials.",
                "explanation": 'Logging <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">resp.request.headers</code> for debugging captures the <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">Authorization</code> header, which contains your API key or token. Log the URL and status code instead.',
                "wrong_label": "log everything",
                "wrong_code": 'logging.debug(f"Headers: {resp.request.headers}")\n# log file: Authorization: Bearer sk-secret...',
                "correct_label": "log safely",
                "correct_code": 'logging.info(f"{resp.status_code} {resp.url}")\n# log file: 200 https://api.example.com/users',
                "tip": "Never log objects that might contain credentials. Log the HTTP method, URL (without query keys), and status code — that is enough for debugging.",
            },
            {
                "tab": "No Session Reuse",
                "title": "Creating a New Connection for Every Request Instead of Reusing a Session",
                "subtitle": "Each new connection adds a TCP handshake and TLS negotiation — slow and wasteful.",
                "explanation": 'When you call <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">requests.get()</code> in a loop, each call opens and closes a new connection. A <code class="font-mono bg-gray-100 px-1 rounded text-[11px]">requests.Session()</code> reuses the same connection, which is significantly faster for multiple calls to the same host.',
                "wrong_label": "new connection each time",
                "wrong_code": 'for page in range(100):\n    resp = requests.get(url, params={"page": page})\n    # 100 separate TCP connections',
                "correct_label": "reuse a session",
                "correct_code": 'session = requests.Session()\nsession.headers["Authorization"] = f"Bearer {token}"\nfor page in range(100):\n    resp = session.get(url, params={"page": page})\n    # one persistent connection',
                "tip": "Use <code class=\"font-mono bg-amber-100 px-1 rounded text-[11px]\">requests.Session()</code> whenever you make more than a handful of calls. It also lets you set default headers — like authentication — once.",
            },
        ],
    },
}


# ── HTML builders ──────────────────────────────────────────────────────

def _tab_btn(index: int, label: str, *, active: bool) -> str:
    if active:
        cls = (
            'mk-step mk-step-active flex items-center gap-2 px-4 py-2 '
            'rounded-full bg-gradient-to-r from-[#CB187D] to-[#e84aad] '
            'text-white shadow-lg shadow-pink-200/50 transition-all duration-250'
        )
    else:
        cls = (
            'mk-step flex items-center gap-2 px-4 py-2 '
            'rounded-full bg-gray-800 text-gray-400 transition-all duration-250'
        )
    return (
        f'<button onclick="switchMkTab({index})" '
        f'class="{cls}" role="tab">\n'
        f'  <span class="iconify text-[13px]" data-icon="fa6-solid:bug"></span>\n'
        f'  <span class="mk-step-label text-xs font-bold">{label}</span>\n'
        f'</button>'
    )


def _panel(mk: dict, *, hidden: bool) -> str:
    hide = " hidden" if hidden else ""
    return f'''\
<div class="mk-panel mk-panel-anim{hide}" role="tabpanel">
  <div class="mistake-card rounded-2xl border border-gray-200 overflow-hidden shadow-sm">

    <!-- Card header -->
    <div class="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-50/60 to-white border-b border-gray-200">
      <span class="inline-flex items-center justify-center w-9 h-9 rounded-lg bg-red-100 shrink-0">
        <span class="iconify text-red-500 text-base" data-icon="fa6-solid:bug"></span>
      </span>
      <div class="min-w-0 flex-1">
        <h4 class="font-bold text-gray-800 text-sm">{mk["title"]}</h4>
        <p class="text-xs text-gray-500 mt-0.5">{mk["subtitle"]}</p>
      </div>
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider bg-red-100 text-red-600 shrink-0">
        <span class="iconify text-[10px]" data-icon="fa6-solid:terminal"></span> Pitfall
      </span>
    </div>

    <!-- Explanation paragraph -->
    <div class="px-6 py-5">
      <p class="text-sm text-gray-600 leading-relaxed">{mk["explanation"]}</p>
    </div>

    <!-- Wrong / Correct split panel -->
    <div class="relative grid grid-cols-1 sm:grid-cols-2">
      <div class="p-5 bg-red-50/30">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-red-500 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-red-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:xmark"></span></span> Wrong \u2014 {mk["wrong_label"]}
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">{mk["wrong_code"]}</code></pre>
        </div>
      </div>
      <div class="absolute inset-y-0 left-1/2 -translate-x-1/2 hidden sm:flex items-center z-10 pointer-events-none">
        <span class="w-7 h-7 rounded-full flex items-center justify-center shadow-md bg-white ring-2 ring-gray-200">
          <span class="iconify text-xs text-[#CB187D]" data-icon="fa6-solid:arrow-right"></span>
        </span>
      </div>
      <div class="p-5 bg-emerald-50/30 border-t sm:border-t-0 sm:border-l border-gray-200">
        <p class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-emerald-600 mb-3">
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-emerald-500"><span class="iconify text-white text-[10px]" data-icon="fa6-solid:check"></span></span> Correct \u2014 {mk["correct_label"]}
        </p>
        <div class="rounded-xl overflow-hidden bg-code">
          <pre class="overflow-x-auto pre-reset px-4 py-3"><code class="language-python">{mk["correct_code"]}</code></pre>
        </div>
      </div>
    </div>

    <!-- Amber tip footer -->
    <div class="flex items-start gap-3 px-5 py-3.5 border-t border-gray-200 bg-amber-50/40">
      <span class="iconify text-orange-400 text-base shrink-0 mt-0.5" data-icon="fa6-solid:lightbulb"></span>
      <p class="text-xs text-gray-600 leading-relaxed">{mk["tip"]}</p>
    </div>

  </div>
</div>'''


def build_section(topic: str, mistakes: list[dict]) -> str:
    tabs = "\n".join(
        _tab_btn(i, m["tab"], active=(i == 0))
        for i, m in enumerate(mistakes)
    )
    tab_row = f'<div class="flex items-center gap-2 mb-6" role="tablist">\n{tabs}\n</div>'

    panels = "\n\n".join(
        _panel(m, hidden=(i > 0))
        for i, m in enumerate(mistakes)
    )

    body = f'{tab_row}\n\n{panels}'

    return f'''\
<section id="mistakes">
  <div class="rounded-2xl overflow-hidden shadow-sm border border-gray-100">
    <div class="flex items-center gap-4 pl-4 pr-8 py-5 bg-white border-b border-gray-100 border-l-4 border-l-[#CB187D]">
      <span class="inline-flex items-center justify-center w-11 h-11 rounded-xl bg-[#CB187D] shrink-0">
        <span class="iconify text-white text-base" data-icon="fa6-solid:triangle-exclamation"></span>
      </span>
      <div class="min-w-0">
        <h2 class="text-xl font-bold text-gray-900 leading-tight">Common Mistakes</h2>
        <p class="text-sm text-gray-400 leading-snug mt-0.5 line-clamp-1">Pitfalls beginners hit when working with {topic}</p>
      </div>
    </div>
    <div class="bg-white px-8 py-7 space-y-6">

{body}

    </div>
  </div>
</section>'''


# ── Main ───────────────────────────────────────────────────────────────

ok = fail = 0
for filename, lesson in LESSONS.items():
    path = MOD / filename
    if not path.exists():
        print(f"\u274c NOT FOUND  {filename}")
        fail += 1
        continue

    text = path.read_text(encoding="utf-8")
    replacement = build_section(lesson["topic"], lesson["mistakes"])
    new_text, n = SECTION_RE.subn(replacement, text, count=1)

    if n == 0:
        print(f"\u274c NO MATCH   {filename}")
        fail += 1
        continue

    path.write_text(new_text, encoding="utf-8")
    print(f"\u2705 OK         {filename}")
    ok += 1

print(f"\n{ok}/{ok + fail} mistakes sections rewritten")
