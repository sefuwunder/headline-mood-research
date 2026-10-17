# Weekly lexicon decision — 2026-10-16 (Friday)

User reply (13:58 EDT) to the consolidated apply-list: **"all & lets research daily,
but the decision is weekly"** — approved all 10 re-staged items, death-threats MWE
included at weight 2. Cadence going forward: research stays daily (07:24 EDT),
lexicon decision asks arrive in the Friday morning edition only (already codified
in the mood-scoring-research cron body, step 6 — no schedule change needed).

## Applied (patch + one manual addition, verified with the real scorer)

Against `sefuwunder/daily-briefing@916ff6e` via
`hidden_files/lexicon-consolidated-2026-10-16.patch`:

1. `wins` hope intensity 2 → 1
2. `surge` hope intensity 2 → 1
3. `self-replicate` → PESSIMISM_WORDS
4. `power`, `legal`, `action` → EXCLUDED_WORDS (preventive; no current scoring change)
5. `death threats` MWE at weight 2 → FEAR_MWES (manual addition, not in patch)
6. `backdoor`/`backdoors` → PESSIMISM_WORDS; `spy chip` + `spy-chip` MWEs → PESSIMISM_MWES (new list, wired as negMwes on the HN spectrum)
7. `arrests` → FEAR_WORDS, tier 1
8. `trial` → EXCLUDED_WORDS (preventive)
9. `poisoning` → FEAR_WORDS, tier 2
10. `betrayal` → FEAR_WORDS, tier 2

Deliberately NOT applied: item 11 (deny/denies/denied as DENIAL_VERBS neutralizers —
conflicts with the approved tier-1 fear treatment; would gut "denies allegations").
Held: ×0.7 downtoner (cited paper still unread).

## Verified effects (real scorer, before → after, bun)

- poisoning / betrayal / arrests / backdoor / spy chip / spy-chip / self-replicate: 0 → −50
- death-threats MWE fires on top of single-word hits; mixed headline −33 → −47 (fear pts 6 → 8.4)
- wins demotion: −41 → −66 on mixed headline; invisible on lone-word headlines (±50 cap), as documented
- power/legal/action/trial exclusions: zero scoring change (preventive no-ops)
- denies/allegations morning approval intact (−100 unchanged)
- Project checks: 31/31 drag-order tests pass; patched server boots and /api/mood → 200
- Pre-push hash audit: only src/server.ts differs from remote tree (16/16 files accounted for)

## Status: PUSH PENDING

The 20:41 EDT proactivity run completed the apply and verification but could not
push: GitHub write API calls are denied from the background-run context
(deterministic 403 with empty body on POST /user/repos; git protocol also blocked).
Staged tree preserved at:
`hidden_files/push-staging-2026-10-16/` (complete repo tree, patch + MWE applied).
Next normal user turn: run gh_push.py --repo daily-briefing --dir <staging> and
verify remote HEAD. No re-verification needed — tree is final.
