# Weekly lexicon decision digest — Friday 2026-11-13

Today: HN −2 (n=30, 1 neg / 0 pos / 29 neutral), Guardian −2 (n=25, 5 fear / 4 hope / 16 neutral).
7-day trajectory: HN flat around zero (5, −2, 8, −2, −2, 2, −2; mean +1.0 vs +3.0 the prior week);
Guardian fear run easing sharply (−12, −8, −14, −27, −8, −4, −2; mean −10.7 vs −21.0 the prior
week; today −2 ties the least-fearful readings of the past month — Oct 10 and Oct 15 also −2).

## Status of the last digest

The 2026-11-06 digest got no line-number reply, so nothing was applied or cleared since.
Everything still open is re-presented below, re-verified against the current tree this
morning, plus the 13 new items from 2026-11-07 → 2026-11-13 (worry, fall, defeat, faces
paradigm extension, ebola, uncertainty, exposes, crashes ×2 spectra, loom, rebuke,
showdown, surge removal, negation-scope extension).

## How this was verified

Every open backlog item (2026-10-17 → 2026-11-13) was checked for membership against
the current dashboard tree (`~/workspace/your_files/daily-briefing/src/server.ts`) and
re-staged against the real scorer (research.py, which mirrors scoreHeadline). No open
proposal conflicts with an already-applied word, and no proposed neutralizer eats an
approved word: `drone` and `body` appear in no scored set, so their exclusions are pure
no-ops. Cross-spectrum duplicates are normal, not conflicts: `dying` is already
PESSIMISM tier 3 (this digest proposes only its FEAR side), `hacked` is already FEAR
tier 1 (PESSIMISM side only), `worst` is already PESSIMISM (FEAR side only),
`breach`/`breached` are already FEAR tier 1 (PESSIMISM side only), `uncertainty` is
already PESSIMISM (FEAR side only), and `crash` is already dual-listed — doom/scam/fraud
are already dual-listed the same way.

## ⚠️ Batch 0 first: approved 2026-10-16, never landed

You approved all 10 items on 2026-10-16 ("all"), but a membership check of the current
tree finds NONE of them present. The 20:41 run applied them to a staging tree
(`hidden_files/push-staging-2026-10-16/`) whose push was blocked in the background-run
context, and the live tree has since moved on (OPML wiring, 2026-10-26) — so the staging
tree is stale and these need a fresh patch against the current tree, not the old staging
copy. (One nuance: the live tree DOES contain the 2026-10-16 procedural fear words
`allegations`/`deny`, tier 1 — those landed by another route; only the 10 approved items
below are missing.) Batch 0 is re-presented for re-approval below; it is not assumed
approved twice over.

## The apply-list — reply with line numbers: any, all, or none

### Batch 0 — approved 2026-10-16, missing from tree (re-apply fresh)
1. `wins` hope intensity 2 → 1 (demotion; invisible on lone-word headlines, bites in mixed ones — verified 2026-10-16: −41 → −66 on a mixed headline)
2. `surge` hope intensity 2 → 1 (same caveat as 1) — MOOT if line 55 (removal) is picked; removal subsumes demotion
3. `self-replicate` → PESSIMISM_WORDS (default tier; evidence headline 0 → −50)
4. `power`, `legal`, `action` → EXCLUDED_WORDS (preventive no-op; none scored today)
5. `death threats` MWE, weight 2 → FEAR_MWES (adds on top of single-word hits — verified 2026-10-16: mixed headline −33 → −47)
6. `backdoor`/`backdoors` → PESSIMISM_WORDS + `spy chip`/`spy-chip` MWEs → PESSIMISM_MWES (new list + wiring on the HN spectrum; 0 → −50)
7. `arrests` → FEAR_WORDS, tier 1 (0 → −50)
8. `trial` → EXCLUDED_WORDS (preventive no-op; decided 2026-10-16 so `controversial` in Batch 1 can carry trial headlines)
9. `poisoning` → FEAR_WORDS, tier 2 (default; 0 → −50)
10. `betrayal` → FEAR_WORDS, tier 2 (default; 0 → −50)

### Batch 1 — Guardian fear, tier 1 (mild)
11. `controversial` → FEAR_WORDS, tier 1 — "Controversial vaccine trial…" 0 → −33 (re-staged: `denies` already fires, so two neg hits lift past the single-hit cap)
12. `protests` → FEAR_WORDS, tier 1 — "Arrests over France protests…" 0 → −50 (recurred 10-21, 10-25, 11-01, 11-05)
13. `referendum` → FEAR_WORDS, tier 1 — Alberta referendum headline 0 → −50
14. `deforestation` → FEAR_WORDS, tier 1 — "…destructive deforestation…" 0 → −50. DEPENDENCY: land together with line 50 (`lowest on record` hope MWE), or "deforestation falls to lowest on record" flips to fear.
15. `fall`/`falls` → FEAR_WORDS, tier 1 — "Global stocks fall amid 'big worries over AI'…" — fall alone does not move the evidence headline (+50 stays +50: a tier-1 hit cannot outweigh tier-3 `triumph`); judge together with line 36.
16. `uncertainty` → FEAR_WORDS, tier 1 — "New Zealand faces weeks of uncertainty…" 0 → −50; with line 33 on the same headline 0 → −100. Cross-spectrum port: already PESSIMISM_WORDS.
17. `exposes`/`expose` → FEAR_WORDS, tier 1 — "exposes passwords in 1,122 public GitHub files" (HN) and "yells and exposes himself in Melbourne court" (Guardian) both 0 → −50.
18. `loom`/`looms`/`looming` → FEAR_WORDS, tier 1 — "…year that 'feels like a recession' looms" −50 → −100 (cap lift).

### Batch 2 — Guardian death family, tier 3 (same weight as dead/death/kills)
19. `dies`/`died`/`dying` → FEAR_WORDS, tier 3 — "British woman dies trying to save sons…" +50 → −20 (research.py; dashboard ≈−29 with the 1.2× fear weight); "…Australians dying of dementia…" −50 → −100 (cap lift, second hit).

### Batch 3 — Guardian fear, tier 2 (default)
20. `hostile`/`hostility` → FEAR_WORDS, tier 2 — "Falklands again face a hostile Argentina" 0 → −50
21. `menace`/`menaces` → FEAR_WORDS, tier 2 — "Hurricane Trudy menaces Mexico…" −50 → −100 (cap lift)
22. `targeted` → FEAR_WORDS, tier 2 — "…targeted with spyware" 0 → −50
23. `injures`/`injured`/`injure`/`injuries` → FEAR_WORDS, tier 2 — "Typhoon Champi kills one and injures more than 500…" −50 → −100 (cap lift)
24. `weaponise`/`weaponising`/`weaponize`/`weaponizing` → FEAR_WORDS, tier 2 — "…weaponising Somalia's floods…" −50 → −100 (cap lift; recurred 10-28, 10-29)
25. `loss`/`losses` → FEAR_WORDS, tier 2 — "Slovenia mourns loss of glacier…" 0 → −50
26. `victims`/`victim` → FEAR_WORDS, tier 2 — Spain train-crash headline −50 → −100 (cap lift); each of lines 26/27 alone lifts it
27. `mourning`/`mourns`/`mourn` → FEAR_WORDS, tier 2 — same Spain headline −50 → −100 (cap lift); pairs with line 25's grief frame
28. `disquiet` → FEAR_WORDS, tier 2 — "Disquiet grows in Albanese's back yard…" +50 → 0 (research.py; dashboard ≈−9 — corrects a hope misfire: lone `unite` fired while `disquiet` was unscored)
29. `jailed`/`jail` → FEAR_WORDS, tier 2 — "…children's author … jailed over child exploitation material" +50 → 0 (research.py; dashboard ≈−9); recurred in the Kenyan sect-leader headline 11-07, 11-08, 11-09, 11-10, 11-12, 11-13 — six recurrences, still −50 off `murder` alone
30. `ban`/`bans` → FEAR_WORDS, tier 2 — "Australia's social media ban…" / "Denmark pushes for EU ban…" 0 → −50 each
31. `worst` → FEAR_WORDS, tier 2 — judge with line 32; either alone leaves the Aukus headline positive on the fuller version with `deal`
32. `riskiest` → FEAR_WORDS, tier 2 — same Aukus headline; superlative paradigm gap (`risky`/`risks` already listed); together lines 31+32 re-stage 0 → −100 on the headline as recorded
33. `face`/`faces`/`facing`/`faced` → FEAR_WORDS, tier 2 — "ANC faces anger over poor services…" / "Australia faces same issues…" / "Falkland Islanders face 'devastating consequences'…" 0 → −50 each; with line 37 on the ANC headline 0 → −100
34. `plunge` → FEAR_WORDS, tier 2 — "Global stocks plunge amid AI slowdown fears…" +20 → −14 (research.py; dashboard ≈−9)
35. `smuggled`/`smuggle`/`smuggling` → FEAR_WORDS, tier 2 — "…3,000 tarantulas smuggled inside dirty socks" +50 → 0 (research.py; dashboard ≈−9 — lone `discover` fired while `smuggled` was unscored)
36. `worry`/`worries`/`worried` → FEAR_WORDS, tier 2 — "Global stocks fall amid 'big worries over AI'…" alone +50 → +20 (research.py; dashboard ≈+11); with line 15 +50 → 0 (research.py; dashboard ≈−9). Judge with line 15.
37. `defeat`/`defeats` → FEAR_WORDS, tier 2 — "ANC faces bruising defeat…" 0 → −50; with line 33 on the same headline 0 → −100
38. `ebola` → FEAR_WORDS, tier 2 — "British healthcare worker with Ebola evacuated from DR Congo to UK" −50 → −100 (cap lift). Caveat: single-story evidence (same story across two days, not independent occurrences).
39. `rebuke` → FEAR_WORDS, tier 2 — "Pope Leo delivers stinging rebuke of Milei's austerity measures…" 0 → −50
40. `showdown` → FEAR_WORDS, tier 2 — "Pope's visit to Argentina sets up showdown with 'hyper-capitalist' Milei" 0 → −50
41. `crashes` → FEAR_WORDS at the `crash` tier — "Mortgage holders' confidence crashes to lowest level since 1994…" −50 → −100 (cap lift). Pairs with line 49 (same word, HN spectrum).

### Batch 4 — Hacker News
42. `built` → OPTIMISM_WORDS (default tier) — "…so I built siltop" 0 → +50
43. `compromised` → PESSIMISM_WORDS (default tier) — "Compromised LiteLLM…" 0 → −50
44. `hacked` → PESSIMISM_WORDS (default tier) — "Anthropic hacked to deliver remote access trojan" 0 → −50 alone, 0 → −100 with line 45
45. `trojan` → PESSIMISM_WORDS (default tier) — same headline 0 → −50 alone, 0 → −100 with line 44
46. `breach`/`breaches`/`breached` → PESSIMISM_WORDS (default tier) — "Northflank Breached" / "Tell HN: Scribd Breached" 0 → −50 each
47. `cyber-attack`/`cyberattack` → PESSIMISM_WORDS (default tier) + FEAR_WORDS tier 1 — "Supermarket freezers … hit by suspected cyber-attack" 0 → −50; tokenization gap (scorer keeps hyphens, so `cyber-attack` never matches listed `attack`)
48. `agentic` → OPTIMISM_WORDS (default tier) — "…AI agentic setup?" / "…SOTA on Agentic Coding" 0 → +50 each
49. `crashes` → PESSIMISM_WORDS at the `crash` tier — same paradigm gap as line 41 on the HN spectrum; no HN evidence headline this week. Pick with line 41 or not at all.

### Batch 5 — Mechanisms (code changes, not just word lists)
50. `lowest on record` → HOPE_MWES, weight 2, with new posMwes wiring on the fear↔hope spectrum (dashboard has no hope-side phrase support today; the 2026-10-23 batch-4 patch drafts this wiring but predates the OPML changes — re-apply fresh). Without it, line 14 makes "deforestation falls to lowest on record" score −50 on good news; with it, fear 1 vs hope 2 → +33.
51. `slows`/`slowed` → RESOLUTION_WORDS + extend the resolution check to the pessimism↔optimism spectrum (today it is fear-pole-only — verified in scoreHeadline: `sp.id === "fear-hope"`) — "Birdwatching rewires the brain and slows cognitive decline" −50 → 0 (neutralized, never flipped; "growth slows" with no neg hit is unaffected).
52. Negation-scope extension (scorer logic, no word add) — treat cognition-verb negations ("not convinced", "no evidence", "doubts that") + a lexicon word in the same clause as a damp-to-neutral: "I'm not convinced the AI bubble exists" −50 → 0. Backed by Hogenboom et al. 2011 (fixed 2-word window + optimized inversion factor), Zhu et al. 2014 (negator-dependent sentiment), and Carrillo-de-Albornoz & Plaza 2013 (emotion-based modifier modeling — new in the bibliography this week). Caveat: narrow pattern list only; broader clause parsing is the parked NegBERT route.

### Batch 6 — Exclusions (preventive no-ops; neither word is in any scored set today)
53. `drone` → EXCLUDED_WORDS (maker-neutral "I built a drone…" stays 0; attack headlines already score via attack/kills)
54. `body` → EXCLUDED_WORDS (high-ambivalence noun; fear frames already carried by murder/kills/attack)

### Batch 7 — Removal
55. `surge`/`surging`/`surged` → REMOVE from HOPE_WORDS — magnitude word, not a valence word: its pole rides entirely on its object. Three days of fear-framed recurrences, all +50 off lone `surge`: "Ukraine captures first Indonesian prisoner of war amid surge in Russian recruitment" (11-11, 11-12, 11-13) and "What's behind Australia's surge in teen extremism?" (11-13, new story). Re-staged: +50 → 0 on removal for both. Note a tier-1 demotion would NOT fix it: the single-hit rule gives ±50 regardless of tier, so removal is the honest fix — and if picked, line 2 (demotion) is moot.

## Dropped in re-verification (not pickable)
- `tariffs` tier 2 → tier 1 demotion (2026-10-21): ALREADY tier 1 in the current FEAR_INTENSITY table (re-confirmed). Nothing to apply; the lone-hit −50 it complained about is the ±50 cap, not the tier.

## Not pickable (no dashboard change)
- Read the 7-day moving average instead of the single-day index (2026-10-18; Guardian −10.7 this week vs −21.0 prior — the fear run is easing, not flat).
- VADER-compound cross-check column in daily research output (2026-10-19; not implemented).

## Discussion notes (observed misfires, no proposal)
- `doom` scores −50 on "Show HN: I Turned DOOM into a Transformer" (game title, not pessimism) — load-bearing elsewhere, no removal proposed.
- `open` scores +50 on "Breaking the open web won't stop the bad bots" (pessimistic frame) — load-bearing optimism vocabulary elsewhere, no removal proposed.
- `hard` scores −50 on "…beats Fable 5 on LiveCodeBench Hard" (benchmark difficulty name) — load-bearing elsewhere, no removal proposed.
- `slow` (tier 1) dilutes "Bones may release proteins that slow aging and extend life span" (+33) — the neg hit is base-form `slow`, not the `slows`/`slowed` resolution mechanism in line 51.
- `abandoned` scores −50 on "Abandoned Quake 4 expansion finished by modders and now playable" (today — the expansion was abandoned, but modders finishing it is good news) — load-bearing pessimism vocabulary elsewhere, no removal proposed; same proper-noun/title class as `doom`/`hard`/`open`.
- Watch: `ransomware` (single occurrence 11-10, breach cluster), `threaten` (watch since 11-08, never recurred), `vulnerability` (watch since 11-06, never recurred), `oil` (single-story 11-12), `close` / `stop` (single occurrences 11-11, too ambivalent alone).

## Standard caveats
- The ±50 cap means lone-word demotions (lines 1–2) barely move anything: they are invisible on lone-word headlines and bite only in mixed headlines.
- Second hits lift caps rather than deepen a lone score: lines 18, 19, 21, 23, 24, 26, 27, 29, 38, 41 move their evidence headlines −50 → −100, which is a cap lift, not a lone-word demotion.
- research.py does not model the dashboard's Guardian 1.2× fear multiplier, so re-staged Guardian mixed-headline numbers read slightly milder than the live widget's; dashboard-adjusted ≈ values are given where they differ. (MWEs are still not modelled in research.py.)
- The 2026-10-23 Friday patches (batches 1–4 drafts) still exist in hidden_files but were written against the pre-OPML tree; if any batch above is approved, apply fresh rather than applying those hunks blindly.
- Recorded skips stay recorded (vaccine, deportation, leave, exit, blast, against, march, takes, ousted, cuts, feral, chatgpt, court, rate, efficient, job, found, code, rights, public, agents, likely, investigation, and the noise words): none are re-proposed here.

## Awaiting
User's line-number reply (any, all, or none). On reply: move decided items to
`hidden_files/decisions-2026-11-13.md` and clear them from `weekly-backlog.md`;
undecided items stay flagged for the following week. Nothing was applied or cleared
in this run.
