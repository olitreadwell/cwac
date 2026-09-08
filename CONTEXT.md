# GOVTNZ/cwac context
> refreshed 2026-09-09 | upstream default: main @ 7a1e38a

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
- areas actively worked: ruff linting, bin scripts, lockfile, CSV writer, axe-core animations — avoid overlapping in-flight work

## Issue-area health
- max_links_per_domain logic in flux (issue #213, team redesigning; AVOID further picks there)
- language audit (issue #212) already staged in fork PR #3
- 27 open issues; scanner rule/reporting bugs are the tractable area

## Gap ledger (dedupe — READ FIRST, never re-pick)
- 2026-08-05 test-coverage — pr-opened (fork PR #1, folded into #2) — filetype coverage
- 2026-08-05 issue #212 language audit — pr-opened-green (fork PR #3) — te-reo-Maori lang=mi readability
- 2026-08-05 bug-fix url_filter_whitelist case — pr-opened-green (fork PR #2) — mixed-case host
- 2026-08-24 issue #213 max_links_per_domain:0 — pr-opened (fork PR #15) — promoted upstream #355, closed; area in flux, avoid
- 2026-08-24 issue #212 dup — closed-superseded (fork PR #17) — dedupe must match repo+issue
- 2026-08-26 test-coverage — pr-closed-ci-blocked (fork PR #11) — mypy/pylint/ruff red
- 2026-09-09 trivial-fix pass — pr-opened (fork PR #24) — 7 typo/stale-path fixes across 4 docs (README, audit-config, audit-results, reflow-audit); fork CI 9/9 green

## Mined gaps (discovered, not yet attempted)
- none yet
