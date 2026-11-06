# Weekly lexicon decision digest — Friday 2026-11-06

Today (corrected): HN +2 (n=30, 2 neg / 4 pos / 24 neutral), Guardian −27 (n=25, 11 fear / 3 hope / 11 neutral).
7-day trajectory: HN flat-to-mildly-up (3, 0, 3, 3, 0, 10, 2; mean +3.0 vs +0.7 the prior week —
yesterday's +10 was the spike, today back near flat); Guardian fear run deepening
(−32, −12, −22, −22, −12, −20, −27; mean −21.0 vs −17.4 the prior week; today −27 is the week's low).

## Research-tool correction — read first

research.py was parsing a phantom pessimism word. The `"hard tech"` quote inside a code
comment in the PESSIMISM_WORDS block was read as lexicon words, so `tech` scored −50 on
any HN headline containing it, from 2026-10-11 until today. Fixed this morning (comments
stripped before parsing); today's HN index corrected 0 → +2 and today's trend.jsonl line
was corrected with it. The dashboard itself never had this bug — only the research scorer.
HN trend values 2026-10-11 → 2026-11-05 may read ~0–2 points low on days a "tech"
headline appeared; Guardian was unaffected.

## Status of the last digest

The 2026-10-30 digest got no line-number reply, so nothing was applied or cleared since.
Everything still open is re-presented below, re-verified against the current tree this
morning, plus the 11 new items from 2026-10-31 → 2026-11-06.

## How this was verified

Every open backlog item (2026-10-17 → 2026-11-06) was checked for membership against
the current dashboard tree (`~/workspace/your_files/daily-briefing/src/server.ts`) and
re-staged against the real scorer logic (research.py, which mirrors scoreHeadline and
now matches the dashboard's word sets exactly after the comment-strip fix). No open
proposal conflicts with an already-applied word, and no proposed neutralizer eats an
approved word: `drone` and `body` appear in no scored set, so their exclusions are pure
no-ops. Cross-spectrum duplicates are normal, not conflicts: `dying` is already
PESSIMISM tier 3 (this digest proposes only its FEAR side), `hacked` is already FEAR
tier 1 (PESSIMISM side only), `worst` is already PESSIMISM (FEAR side only), and
`breach`/`breached` are already FEAR tier 1 (PESSIMISM side only) — doom/scam/fraud
are already dual-listed the same way.

## ⚠️ Batch 0 first: approved 2026-10-16, never landed

You approved all 10 items on 2026-10-16 ("all"), but a membership check of the current
tree finds NONE of them present. The 20:41 run applied them to a staging tree
(`hidden_files/push-staging-2026-10-16/`) whose push was blocked in the background-run
context, and the live tree has since moved on (OPML wiring, 2026-10-26) — so the staging
tree is stale and these need a fresh patch against the current tree, not the old staging
copy. Batch 0 is re-presented for re-approval below; it is not assumed approved twice over.

## The apply-list — reply with line numbers: any, all, or none

### Batch 0 — approved 2026-10-16, missing from tree (re-apply fresh)
1. `wins` hope intensity 2 → 1 (demotion; invisible on lone-word headlines, bites in mixed ones)
2. `surge` hope intensity 2 → 1 (same caveat as 1)
3. `self-replicate` → PESSIMISM_WORDS (default tier; evidence headline 0 → −50)
4. `power`, `legal`, `action` → EXCLUDED_WORDS (preventive no-op; none scored today)
5. `death threats` MWE, weight 2 → FEAR_MWES (adds on top of single-word hits)
6. `backdoor`/`backdoors` → PESSIMISM_WORDS + `spy chip`/`spy-chip` MWEs → PESSIMISM_MWES (new list + wiring on the HN spectrum)
7. `arrests` → FEAR_WORDS, tier 1
8. `trial` → EXCLUDED_WORDS (preventive no-op; decided 2026-10-16 so `controversial` in Batch 1 can carry trial headlines)
9. `poisoning` → FEAR_WORDS, tier 2 (default)
10. `betrayal` → FEAR_WORDS, tier 2 (default)

### Batch 1 — Guardian fear, tier 1 (mild)
11. `controversial` → FEAR_WORDS, tier 1 — "Controversial vaccine trial…" 0 → −50
12. `protests` → FEAR_WORDS, tier 1 — "Arrests over France protests…" 0 → −50 (recurred 10-21, 10-25, 11-01, 11-05)
13. `referendum` → FEAR_WORDS, tier 1 — Alberta referendum headline 0 → −50
14. `deforestation` → FEAR_WORDS, tier 1 — "…destructive deforestation…" 0 → −50. DEPENDENCY: land together with line 39 (`lowest on record` hope MWE), or "deforestation falls to lowest on record" flips to fear.

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
24. `disquiet` → FEAR_WORDS, tier 2 — "Disquiet grows in Albanese's back yard…" +50 → ≈−9 (corrects a hope misfire: lone `unite` fired while `disquiet` was unscored)
25. `jailed`/`jail` → FEAR_WORDS, tier 2 — "…children's author … jailed over child exploitation material" +50 → ≈−9 (lone `winning` fired while `jailed` was unscored)
26. `ban`/`bans` → FEAR_WORDS, tier 2 — "Australia's social media ban…" / "Denmark pushes for EU ban…" 0 → −50 each
27. `worst` → FEAR_WORDS, tier 2 — "Aukus is 'worst, riskiest and most costly'…" +50 → ≈−9 (lone `deal` fired); judge with line 28, either alone leaves the headline at +50
28. `riskiest` → FEAR_WORDS, tier 2 — same Aukus headline; superlative paradigm gap (`risky`/`risks` already listed)
29. `faces` → FEAR_WORDS, tier 2 — today: "ANC faces anger over poor services…" / "Australia faces same issues…" 0 → −50 each
30. `plunge` → FEAR_WORDS, tier 2 — today: "Global stocks plunge amid AI slowdown fears…" +20 → ≈−9 (lone `triumph` outweighed `fears`)
31. `smuggled`/`smuggle`/`smuggling` → FEAR_WORDS, tier 2 — today: "…3,000 tarantulas smuggled inside dirty socks" +50 → ≈−9 (lone `discover` fired)

### Batch 4 — Hacker News
32. `built` → OPTIMISM_WORDS (default tier) — "…so I built siltop" 0 → +50
33. `compromised` → PESSIMISM_WORDS (default tier) — "Compromised LiteLLM…" 0 → −50
34. `hacked` → PESSIMISM_WORDS (default tier) — "Anthropic hacked to deliver remote access trojan" 0 → −50
35. `trojan` → PESSIMISM_WORDS (default tier) — same headline 0 → −50 alone, 0 → −100 with line 34
36. `breach`/`breaches`/`breached` → PESSIMISM_WORDS (default tier) — "Northflank Breached" / "Tell HN: Scribd Breached" 0 → −50 each
37. `cyber-attack`/`cyberattack` → PESSIMISM_WORDS (default tier) + FEAR_WORDS tier 1 — "Supermarket freezers … hit by suspected cyber-attack" 0 → −50; tokenization gap (scorer keeps hyphens, so `cyber-attack` never matches listed `attack`)
38. `agentic` → OPTIMISM_WORDS (default tier) — "…AI agentic setup?" / "…SOTA on Agentic Coding" 0 → +50 each

### Batch 5 — Mechanisms (code changes, not just word lists)
39. `lowest on record` → HOPE_MWES, weight 2, with new posMwes wiring on the fear↔hope spectrum (dashboard has no hope-side phrase support today; the 2026-10-23 batch-4 patch drafts this wiring but predates the OPML changes — re-apply fresh). Without it, line 14 makes "deforestation falls to lowest on record" score −50 on good news; with it, fear 1 vs hope 2 → +33.
40. `slows`/`slowed` → RESOLUTION_WORDS + extend the resolution check to the pessimism↔optimism spectrum (today it is fear-pole-only) — "Birdwatching rewires the brain and slows cognitive decline" −50 → 0 (neutralized, never flipped; "growth slows" with no neg hit is unaffected).

### Batch 6 — Exclusions (preventive no-ops; neither word is in any scored set today)
41. `drone` → EXCLUDED_WORDS (maker-neutral "I built a drone…" stays 0; attack headlines already score via attack/kills)
42. `body` → EXCLUDED_WORDS (high-ambivalence noun; fear frames already carried by murder/kills/attack)

## Dropped in re-verification (not pickable)
- `tariffs` tier 2 → tier 1 demotion (2026-10-21): ALREADY tier 1 in the current FEAR_INTENSITY table. Nothing to apply; the lone-hit −50 it complained about is the ±50 cap, not the tier.

## Not pickable (no dashboard change)
- Read the 7-day moving average instead of the single-day index (2026-10-18; Guardian −21.0 this week vs −17.4 prior — the fear run is deepening, not flat).
- VADER-compound cross-check column in daily research output (2026-10-19; not implemented).

## Discussion notes (observed misfires, no proposal)
- `doom` scores −50 on "Show HN: I Turned DOOM into a Transformer" (game title, not pessimism) — load-bearing elsewhere, no removal proposed.
- `open` scores +50 on "Breaking the open web won't stop the bad bots" (pessimistic frame) — load-bearing optimism vocabulary elsewhere, no removal proposed.
- `hard` scores −50 on "…beats Fable 5 on LiveCodeBench Hard" (benchmark difficulty name) — load-bearing elsewhere, no removal proposed.
- `slow` (tier 1) dilutes "Bones may release proteins that slow aging and extend life span" (+33) — the neg hit is base-form `slow`, not the `slows`/`slowed` resolution mechanism in line 40.
- Watch: `vulnerability`/`vulnerabilities` — single occurrence today ("MS Paint Remote Code Execution Vulnerability" scored 0); needs a second occurrence before proposing.

## Standard caveats
- The ±50 cap means lone-word demotions (lines 1–2) barely move anything: they are invisible on lone-word headlines and bite only in mixed headlines.
- Second hits lift caps rather than deepen a lone score: lines 15, 17, 19, 20, 22, 23 move their evidence headlines −50 → −100, which is a cap lift, not a lone-word demotion.
- research.py does not model the dashboard's Guardian 1.2× fear multiplier, so re-staged Guardian mixed-headline numbers will read slightly milder than the live widget's. (It now matches the dashboard's word sets exactly after today's comment-strip fix; MWEs are still not modelled.)
- The 2026-10-23 Friday patches (batches 1–4 drafts) still exist in hidden_files but were written against the pre-OPML tree; if any batch above is approved, apply fresh rather than applying those hunks blindly.
- Recorded skips stay recorded (vaccine, deportation, leave, exit, blast, against, march, takes, ousted, cuts, feral, chatgpt, court, rate, efficient, job, found, code, rights, and the noise words): none are re-proposed here.

## Awaiting
User's line-number reply (any, all, or none). On reply: move decided items to
`hidden_files/decisions-2026-11-06.md` and clear them from `weekly-backlog.md`;
undecided items stay flagged for the following week. Nothing was applied or cleared
in this run.
