# Weekly lexicon decision digest — Friday 2026-10-30

Today: HN 0 (n=32, 2 neg / 2 pos / 28 neutral), Guardian −22 (n=25, 9 fear / 1 hope / 15 neutral).
7-day trajectory: HN flat at ~0 (0, 0, 0, 3, 2, −3, 0; mean +0.3); Guardian on a fear run
easing off its peak (−10, −12, −8, −14, −28, −28, −22; mean −17.4, vs −17.1 the prior 7 days).

## How this was verified

Every open backlog item (2026-10-17 → 2026-10-30) was checked for membership against
the current dashboard tree (`~/workspace/your_files/daily-briefing/src/server.ts`) and
re-staged against the real scorer logic (research.py, which mirrors scoreHeadline).
No open proposal conflicts with an already-applied word, and no proposed neutralizer
eats an approved word: `drone` and `body` appear in no scored set, so their exclusions
are pure no-ops. Two cross-spectrum duplicates are normal, not conflicts: `dying` is
already PESSIMISM tier 3 (this digest proposes only its FEAR side) and `hacked` is
already FEAR tier 1 (this digest proposes only its PESSIMISM side) — doom/scam/fraud
are already dual-listed the same way.

## ⚠️ Batch 0 first: approved 2026-10-16, never landed

You approved all 10 items on 2026-10-16 ("all"), but a membership check of the current
tree finds NONE of them present. The 20:41 run applied them to a staging tree
(`hidden_files/push-staging-2026-10-16/`) whose push was blocked in the background-run
context, and the live tree has since moved on (OPML wiring, 2026-10-26) — so the staging
tree is stale and these need a fresh patch against the current tree, not the old staging
copy. Today's corpus proves the gap is live: "Backdoors in official Claude Code
extensions" still scores 0. Batch 0 is re-presented for re-approval below; it is not
assumed approved twice over.

## The apply-list — reply with line numbers: any, all, or none

### Batch 0 — approved 2026-10-16, missing from tree (re-apply fresh)
1. `wins` hope intensity 2 → 1 (demotion; invisible on lone-word headlines, bites in mixed ones)
2. `surge` hope intensity 2 → 1 (same caveat as 1)
3. `self-replicate` → PESSIMISM_WORDS (default tier; evidence headline 0 → −50)
4. `power`, `legal`, `action` → EXCLUDED_WORDS (preventive no-op; none scored today)
5. `death threats` MWE, weight 2 → FEAR_MWES (adds on top of single-word hits)
6. `backdoor`/`backdoors` → PESSIMISM_WORDS + `spy chip`/`spy-chip` MWEs → PESSIMISM_MWES (new list + wiring on the HN spectrum; today's "Backdoors…" headline 0 → −50)
7. `arrests` → FEAR_WORDS, tier 1
8. `trial` → EXCLUDED_WORDS (preventive no-op; decided 2026-10-16 so `controversial` in Batch 1 can carry trial headlines)
9. `poisoning` → FEAR_WORDS, tier 2 (default)
10. `betrayal` → FEAR_WORDS, tier 2 (default)

### Batch 1 — Guardian fear, tier 1 (mild)
11. `controversial` → FEAR_WORDS, tier 1 — "Controversial vaccine trial…" 0 → −50
12. `protests` → FEAR_WORDS, tier 1 — "Arrests over France protests…" 0 → −50 (recurred 10-21, 10-25)
13. `referendum` → FEAR_WORDS, tier 1 — Alberta referendum headline 0 → −50
14. `deforestation` → FEAR_WORDS, tier 1 — "…destructive deforestation…" 0 → −50. DEPENDENCY: land together with line 28 (`lowest on record` hope MWE), or "deforestation falls to lowest on record" flips to fear.

### Batch 2 — Guardian death family, tier 3 (same weight as dead/death/kills)
15. `dies`/`died`/`dying` → FEAR_WORDS, tier 3 — "British woman dies trying to save sons…" +50 → −20 (fixes a hope misfire: lone `save` fired while `dies` was unscored); "…Australians dying of dementia…" −50 → −100 (cap lift, second hit).

### Batch 3 — Guardian fear, tier 2 (default)
16. `hostile`/`hostility` → FEAR_WORDS, tier 2 — "Falklands again face a hostile Argentina" 0 → −50
17. `menace`/`menaces` → FEAR_WORDS, tier 2 — "Hurricane Trudy menaces Mexico…" −50 → −100 (cap lift)
18. `targeted` → FEAR_WORDS, tier 2 — "…targeted with spyware" 0 → −50
19. `injures`/`injured`/`injure`/`injuries` → FEAR_WORDS, tier 2 — "Typhoon Champi kills one and injures more than 500…" −50 → −100 (cap lift)
20. `weaponise`/`weaponising`/`weaponize`/`weaponizing` → FEAR_WORDS, tier 2 — "…weaponising Somalia's floods…" −50 → −100 (cap lift; recurred 10-28, 10-29)
21. `loss`/`losses` → FEAR_WORDS, tier 2 — "Slovenia mourns loss of glacier…" 0 → −50
22. `victims`/`victim` → FEAR_WORDS, tier 2 — Spain train-crash headline −50 → −100 (cap lift)
23. `mourning`/`mourns`/`mourn` → FEAR_WORDS, tier 2 — same Spain headline −50 → −100 (cap lift); pairs with line 21's grief frame

### Batch 4 — Hacker News
24. `built` → OPTIMISM_WORDS (default tier) — "…so I built siltop" 0 → +50
25. `compromised` → PESSIMISM_WORDS (default tier) — "Compromised LiteLLM…" 0 → −50
26. `hacked` → PESSIMISM_WORDS (default tier) — today: "Anthropic hacked to deliver remote access trojan" 0 → −50
27. `trojan` → PESSIMISM_WORDS (default tier) — same headline 0 → −50 alone, 0 → −100 with line 26

### Batch 5 — Mechanisms (code changes, not just word lists)
28. `lowest on record` → HOPE_MWES, weight 2, with new posMwes wiring on the fear↔hope spectrum (dashboard has no hope-side phrase support today; the 2026-10-23 batch-4 patch drafts this wiring but predates the OPML changes — re-apply fresh). Without it, line 14 makes "deforestation falls to lowest on record" score −50 on good news; with it, fear 1 vs hope 2 → +33.
29. `slows`/`slowed` → RESOLUTION_WORDS + extend the resolution check to the pessimism↔optimism spectrum (today it is fear-pole-only) — "Birdwatching rewires the brain and slows cognitive decline" −50 → 0 (neutralized, never flipped; "growth slows" with no neg hit is unaffected).

### Batch 6 — Exclusions (preventive no-ops; neither word is in any scored set today)
30. `drone` → EXCLUDED_WORDS (maker-neutral "I built a drone…" stays 0; attack headlines already score via attack/kills)
31. `body` → EXCLUDED_WORDS (high-ambivalence noun; fear frames already carried by murder/kills/attack)

## Dropped in re-verification (not pickable)
- `tariffs` tier 2 → tier 1 demotion (2026-10-21): ALREADY tier 1 in the current FEAR_INTENSITY table. Nothing to apply; the lone-hit −50 it complained about is the ±50 cap, not the tier.

## Not pickable (no dashboard change)
- Read the 7-day moving average instead of the single-day index (2026-10-18; Guardian −17.4 this week vs −17.1 prior — the fear run is flat, not worsening).
- VADER-compound cross-check column in daily research output (2026-10-19; not implemented).

## Standard caveats
- The ±50 cap means lone-word demotions (lines 1–2) barely move anything: they are invisible on lone-word headlines and bite only in mixed headlines.
- Second hits lift caps rather than deepen a lone score: lines 15, 17, 19, 20, 22, 23 move their evidence headlines −50 → −100, which is a cap lift, not a lone-word demotion.
- research.py does not model the dashboard's Guardian 1.2× fear multiplier, so re-staged Guardian mixed-headline numbers will read slightly milder than the live widget's.
- The 2026-10-23 Friday patches (batches 1–4 drafts) still exist in hidden_files but were written against the pre-OPML tree; if any batch above is approved, apply fresh rather than applying those hunks blindly.
- Recorded skips stay recorded (vaccine, deportation, leave, exit, blast, against, march, takes, ousted, cuts, feral, and the noise words): none are re-proposed here.

## Awaiting
User's line-number reply (any, all, or none). On reply: move decided items to
`hidden_files/decisions-2026-10-30.md` and clear them from `weekly-backlog.md`;
undecided items stay flagged for the following week. Nothing was applied or cleared
in this run.
