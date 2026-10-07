# GOVTNZ/cwac context
> refreshed 2026-10-07 | upstream default: main @ 25f3dcf

## Identity & policies
- upstream: GOVTNZ/cwac, default branch main, primary language Python (JS for axe-core), English-first (yes)
- CLA/DCO: none (no CLA bot, no DCO, no contributor signup)
- AI-assisted PR policy: unstated (no ban, no disclosure required)
- signed commits required: no
- PR template: none (no .github/PULL_REQUEST_TEMPLATE.md; use pipeline fallback body)
- external tracker: github

## Conventions (verified from merged PRs)
- branch naming: mixed — `CWAC-<issue>/<desc>` (e.g. CWAC-327/make-optional), `fix/...`, `docs/...`, `chore/...`, `refactor/...`, `feat/...`, `perf/...`; Conventional Commits style
- commit style: Conventional Commits (`fix:`, `docs:`, `chore:`, `refactor:`, `feat:`, `perf:`); short imperative subject, body as plain prose (e.g. #395, #392)
- test command: pytest; lint: ruff, mypy, flake8, pylint, bandit; CI gates merge
- how outside PRs get merged: responsive — G-Rath + eoinkelly merge external PRs within days; 67 external merges in 60d

## Maintainer picture
- active maintainers: G-Rath (very active, many merged PRs), eoinkelly (Web Standards team, GDDA)
- areas actively worked (2026-10-04): browser lifecycle (#384, #397), URL sanitising / double-encoding (#396), random queue picking (#386), results-merge script (#383), logging format (#358). Recently landed: sitemap de-duplication (#389-#392), ruff linting, CSV writer. Avoid overlapping in-flight work

## Issue-area health
- max_links_per_domain logic in flux (issue #213, team redesigning; AVOID further picks there)
- language audit (issue #212) already staged in fork PR #3
- merging scan results / page_id actively being worked by G-Rath (issue #160 + PR #383) — AVOID
- scope/boundary matching in flux (issue #372 + external PR #373; scope logic moved crawler.py -> crawlable_page_validator.py in #374) — AVOID
- 13 open issues + 11 open PRs (2026-10-04); scanner rule/reporting bugs are the tractable area

## Gap ledger (dedupe — READ FIRST, never re-pick)
- 2026-08-05 test-coverage — pr-opened (fork PR #1, folded into #2) — filetype coverage
- 2026-08-05 issue #212 language audit — pr-opened-green (fork PR #3) — te-reo-Maori lang=mi readability
- 2026-08-05 bug-fix url_filter_whitelist case — pr-opened-green (fork PR #2) — mixed-case host
- 2026-08-24 issue #213 max_links_per_domain:0 — pr-opened (fork PR #15) — promoted upstream #355, closed; area in flux, avoid
- 2026-08-24 issue #212 dup — closed-superseded (fork PR #17) — dedupe must match repo+issue
- 2026-08-26 test-coverage — pr-closed-ci-blocked (fork PR #11) — mypy/pylint/ruff red
- 2026-09-09 trivial-fix pass — pr-opened (fork PR #24) — 7 typo/stale-path fixes across 4 docs (README, audit-config, audit-results, reflow-audit); fork CI 9/9 green
- 2026-09-24 trivial-fix pass — pr-opened (fork PR #25) — 5 genuine fixes across 5 files: broken LICENSE link in CONTRIBUTING.md, typos pacakge.json/CWAC-307, mertrics/output.py, indiactor/focus-indicator, horisontal/reflow-audit; fork CI 9/9 green, mergeable_state=clean

- 2026-09-25 issue #164 filter log base/filtered_url labels — pr-opened (fork PR #26) — 3 log lines prefixed base_url:/filtered_url: + 5 unit tests; fork CI 9/9 green, mergeable_state=clean; no AI in body/commits
- 2026-10-01 issue #337 credentialed scan / scan with cookie — pr-opened (fork PR #28) — G-Rath suggested a `CHROME_EXTRA_ARGS`-style env var for arbitrary headers; added `EXTRA_HEADERS` (browser via CDP `Network.setExtraHTTPHeaders`, header checks + robots.txt via requests, forwarded by `bin/run`, documented); 8 new tests, lint clean, 186/4 lines; fork CI 9/9 green, mergeable_state=clean
- 2026-10-02 trivial-fix pass — pr-opened (fork PR #29) — 6 genuine fixes across 5 files: `Unforuntately` typo + stale 1280px/zoom `ReflowAudit.run()` docstring (reflow_audit.py), focus-indicator settings marked required + body fallback (doc/audits/focus-indicator-audit.md), `fulfilment` NZ spelling (README.md), Chrome for Testing version in local-dev-setup.md, axe-core rule example 4.12->4.13 (doc/audits/axe-core-audit.md); fork CI 9/9 green, mergeable_state=clean

- 2026-10-04 self-found gap `_url_sanitise` empty path — pr-opened (fork PR #30) — `posixpath.normpath('')` returned `.`, so a URL with no path (`https://example.com`) sanitised to `https://example.com/.` and was recorded/audited under that string; guard only runs `normpath` when there is a path, +2 regression tests; dedupe: the only related PR is open #396 (touches `_url_sanitise` for double-encoding/encoded dot segments) and it does NOT cover the empty-path case (verified by running its head); fork CI 9/9 green, mergeable_state=clean
- 2026-10-04 trivial-fix pass — pr-opened (fork PR #31) — 4 genuine docstring/comment fixes across 2 files: `True of URL is valid` -> `True if URL is valid` and doubled colon `url (str)::` -> `url (str):` and stale `# Try to get the headers 2 times` -> `3 times` (filters.py), Flesch-Kincaid Grade Level return type `float` -> `dict[Any, Any]` (language_audit.py); exhaustive codespell + live URL re-check found nothing else (re-use/re-used valid NZ house style); no overlap with the still-open same-kind PR #29 (9 files) or upstream #398/#399; fork CI 9/9 green, mergeable_state=clean
- 2026-10-05 trivial-fix pass — pr-opened (fork PR #32) — 6 genuine typo/stale-reference fixes across 5 files: unmatched `Browser` code span + `its` -> `it's` (cwac.py), stale `subject (AuditSubject)` docstring -> `row (SiteData)` (config.py), `register_test` -> `register_audit` (src/audit_plugins/default_audit.py), misplaced html-truncation comment moved next to `node['html'][:100]` (src/audit_plugins/axe_core_audit.py), `no ways` -> `no way` (doc/plans/CWAC-327.md); dedupe: none of these files are touched by the still-open same-kind PRs #29/#31 (verified `gh pr diff --name-only`), and `drivers/` in CWAC-307.md was NOT changed because that directory genuinely existed historically (removed in 0328d1d) — not a stale reference; exhaustive codespell (builtins clear,rare,informal,usage,code,names) + relative-link/anchor checks + a live re-check of all external URLs found only valid NZ/UK spellings and live links; fork CI 9/9 green, mergeable_state=clean
- 2026-10-06 trivial-fix pass — pr-opened (fork PR #33) — 6 genuine meaning-preserving fixes across 6 files: wrong `Args` in `_url_filter_prevent_intersections` docstring documented a non-existent `url` param instead of the real `current_base_url`/`current_url` (src/crawlable_page_validator.py), `url_filter_same_protocol` return described a domain check instead of a protocol check (src/filters.py), stray comma `The primary standard, is the` (README.md), subject-verb agreement `details ... is` -> `are` (doc/audits/language-audit.md, plus the prettier reflow that fix required), `URls` -> `URLs` (base_urls/visit/example.txt) and stray `the CWAC` -> `CWAC` (base_urls/nohead/example.txt); dedupe: the still-open same-kind PRs #29/#31 do not touch any of these files/lines (#30 only edits `_url_sanitise`), and #29's README hunk is the `fulfillment` line not the intro comma; exhaustive codespell (builtins clear,rare,informal,usage,code,names), a live re-check of all repo URLs (only illustrative example.org placeholders 404), doubled-word scan and a relative-link check found nothing else; upstream re-verified live at 25f3dcf; fork CI 9/9 running (ruff + schemas green at time of writing)

- 2026-10-06 fork PR #33 — closed (superseded): folded into still-open fork PR #29, which carries the same hunks; no separate action needed
- 2026-10-07 trivial-fix pass — pr-opened (fork PR #34) — 7 genuine meaning-preserving doc/comment fixes across 6 files: `It's value` -> `Its value` (src/output.py), `URls` -> `URLs` comment (src/crawler.py), `read_config` docstring named non-existent `test_config.json` -> `config_default.json` (config.py), animation-wait docstring `after 3 seconds` -> `after 15 seconds` (src/audit_plugins/focus_indicator_audit.py), the repo's only `WCAG21` link -> `WCAG22` for the SC 2.2.2 helpUrl (same file), docstring listed a `'Blocked'` anti-bot status the code never returns (src/audit_manager.py), missing `for` in `add support for Intel based macs` (doc/plans/CWAC-307.md); dedupe: none of these files/lines are in the open same-kind PRs #29 (config.py L190, output.py L282, focus_indicator L25, CWAC-307 L38), #26 (crawler L188/206), #28, #30, #2, #3 — verified per-hunk (`gh pr diff`); exhaustive codespell (builtins clear,rare,informal,usage,code,names) + doubled-word + lowercase-after-sentence + WCAG-version scan across the whole repo found only these; upstream re-verified live at 25f3dcf; fork CI 9/9 running

## Mined gaps (discovered, not yet attempted)
- 2026-10-04 clean-code `CrawlablePageValidator._url_sanitise('https://example.com')` -> `https://example.com/.`; repro `validator.validate(SITE_DATA, 'https://example.com', ..., 'https://example.com')`; expected `https://example.com`; proposed test parametrises path-less root URLs; dedupe: no matching issue, open PR #396 does not fix it — status: attempted (fork PR #30)
