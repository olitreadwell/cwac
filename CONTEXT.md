# GOVTNZ/cwac context
> refreshed 2026-10-02 | upstream default: main @ 0c9fb18

## Identity & policies
- upstream: GOVTNZ/cwac, default branch main, primary language Python (JS for axe-core), English-first (yes)
- CLA/DCO: none (no CLA bot, no DCO, no contributor signup)
- AI-assisted PR policy: unstated (no ban, no disclosure required)
- signed commits required: no
- PR template: none (no .github/PULL_REQUEST_TEMPLATE.md; use pipeline fallback body)
- external tracker: github

## Conventions (verified from merged PRs)
- branch naming: mixed — `CWAC-<issue>/<desc>` (e.g. CWAC-327/make-optional), `fix/...`, `docs/...`, `chore/...`, `refactor/...`, `feat/...`, `perf/...`; Conventional Commits style
- commit style: Conventional Commits (`fix:`, `docs:`, `chore:`, `refactor:`, `feat:`, `perf:`)
- test command: pytest; lint: ruff, mypy, flake8, pylint, bandit; CI gates merge
- how outside PRs get merged: responsive — G-Rath + eoinkelly merge external PRs within days; 67 external merges in 60d

## Maintainer picture
- active maintainers: G-Rath (very active, many merged PRs), eoinkelly (Web Standards team, GDDA)
- areas actively worked: browser/selenium internals (Firefox support removed in #380, browser options cleaned up in #381), sitemap de-duplication (#389-#392), ruff linting, CSV writer, axe-core animations — avoid overlapping in-flight work

## Issue-area health
- max_links_per_domain logic in flux (issue #213, team redesigning; AVOID further picks there)
- language audit (issue #212) already staged in fork PR #3
- 13 open issues + 12 open PRs (2026-10-02); fork PR #25 still open (trivial-typos-and-broken-link); scanner rule/reporting bugs are the tractable area

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

## Mined gaps (discovered, not yet attempted)
- none yet
