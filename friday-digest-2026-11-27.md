# Weekly lexicon decision digest — Friday 2026-11-27

Today: HN −3 (n=30, 3 neg / 1 pos / 26 neutral), Guardian −20 (n=25, 10 fear / 2 hope / 13 neutral).
7-day trajectory: HN mildly positive mid-week then dipped negative today (−2, 0, 2, 5, 5, 5, −3; mean +1.7 vs +3.1 the prior week);
Guardian fear run deepening, not easing (−18, −20, −9, −14, −16, −20, −20; mean −16.7 vs −12.1 the prior week; −20 has now
held three straight days, the joint-deepest Guardian stretch since 10-31's −32).

## Status of the last digest

The 2026-11-20 digest got no line-number reply, so nothing was applied or cleared since.
Everything still open is re-presented below, re-verified against the current tree this
morning, plus 5 new lines (64–68) from 2026-11-21 → 2026-11-27: sell-off, hospitalised,
self-hosted, strike, and protected. Line numbers 1–63 are unchanged from the 2026-11-20
digest so any pending reply still lands.

## How this was verified

Every open backlog item (2026-10-16 → 2026-11-27) was checked for membership against
the current dashboard tree (`~/workspace/your_files/daily-briefing/src/server.ts`) using
research.py's own lexicon loaders, and the 5 new items were re-staged against the real
scorer. No open proposal conflicts with an already-applied word, and no proposed
neutralizer eats an approved word: `drone` and `body` appear in no scored set, so their
exclusions are pure no-ops. Cross-spectrum duplicates are normal, not conflicts: `dying`
is already PESSIMISM tier 3 (this digest proposes only its FEAR side), `hacked` is already
FEAR tier 1 (PESSIMISM side only), `worst` is already PESSIMISM (FEAR side only),
`breach`/`breached` are already FEAR tier 1 (PESSIMISM side only), `uncertainty` is
already PESSIMISM (FEAR side only), `attack` is already FEAR (PESSIMISM side only, line 61),
`discover` is already HOPE (OPTIMISM side only, line 62), and `crash` is already dual-listed
— doom/scam/fraud are already dual-listed the same way. New-item staging: sell-off 0 → −50;
hospitalised −50 → −100 (cap lift, second hit alongside `warning`); self-hosted 0 → +50 on
both evidence headlines; strike 0 → −50; protected 0 → +50 on both evidence headlines
(tier 1 mild — the ±50 single-hit cap gives the same +50 as tier 2 on a lone hit).

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
12. `protests` → FEAR_WORDS, tier 1 — "Arrests over France protests…" 0 → −50 (recurred 10-21, 10-25, 11-01, 11-05, 11-17, 11-18)
13. `referendum` → FEAR_WORDS, tier 1 — Alberta referendum headline 0 → −50
14. `deforestation` → FEAR_WORDS, tier 1 — "…destructive deforestation…" 0 → −50. DEPENDENCY: land together with line 50 (`lowest on record` hope MWE), or "deforestation falls to lowest on record" flips to fear.
15. `fall`/`falls` → FEAR_WORDS, tier 1 — "Global stocks fall amid 'big worries over AI'…" — fall alone does not move the evidence headline (+50 stays +50: a tier-1 hit cannot outweigh tier-3 `triumph`); judge together with line 36.
16. `uncertainty` → FEAR_WORDS, tier 1 — "New Zealand faces weeks of uncertainty…" 0 → −50; with line 33 on the same headline 0 → −100. Cross-spectrum port: already PESSIMISM_WORDS. Note the word's ambivalence cuts both ways: 11-27 HN "An introduction to uncertainty in machine learning" scores −50 off PESSIMISM on a neutral academic title.
17. `exposes`/`expose` → FEAR_WORDS, tier 1 — "exposes passwords in 1,122 public GitHub files" (HN) and "yells and exposes himself in Melbourne court" (Guardian) both 0 → −50.
18. `loom`/`looms`/`looming` → FEAR_WORDS, tier 1 — "…year that 'feels like a recession' looms" −50 → −100 (cap lift). Recurred 11-27, fresh: "Threat from China looms large over Taiwan's local elections" −50 off `threat` alone.

### Batch 2 — Guardian death family, tier 3 (same weight as dead/death/kills)
19. `dies`/`died`/`dying` → FEAR_WORDS, tier 3 — "British woman dies trying to save sons…" +50 → −20 (research.py; dashboard ≈−29 with the 1.2× fear weight); "…Australians dying of dementia…" −50 → −100 (cap lift, second hit). Recurred 11-19 (`died`, two headlines) and 11-27 (`dying`, fresh: "…prison guard was watching TV while Aboriginal man was dying in custody" −50 off `crisis` alone).

### Batch 3 — Guardian fear, tier 2 (default)
20. `hostile`/`hostility` → FEAR_WORDS, tier 2 — "Falklands again face a hostile Argentina" 0 → −50
21. `menace`/`menaces` → FEAR_WORDS, tier 2 — "Hurricane Trudy menaces Mexico…" −50 → −100 (cap lift)
22. `targeted` → FEAR_WORDS, tier 2 — "…targeted with spyware" 0 → −50
23. `injures`/`injured`/`injure`/`injuries` → FEAR_WORDS, tier 2 — "Typhoon Champi kills one and injures more than 500…" −50 → −100 (cap lift). Recurred 11-26 and 11-27 (same elephants story, repeat RSS: "Swiss tourist killed and British and Americans injured by elephants in Cameroon" still −50 off `killed` alone).
24. `weaponise`/`weaponising`/`weaponize`/`weaponizing` → FEAR_WORDS, tier 2 — "…weaponising Somalia's floods…" −50 → −100 (cap lift; recurred 10-28, 10-29)
25. `loss`/`losses` → FEAR_WORDS, tier 2 — "Slovenia mourns loss of glacier…" 0 → −50
26. `victims`/`victim` → FEAR_WORDS, tier 2 — Spain train-crash headline −50 → −100 (cap lift); each of lines 26/27 alone lifts it
27. `mourning`/`mourns`/`mourn` → FEAR_WORDS, tier 2 — same Spain headline −50 → −100 (cap lift); pairs with line 25's grief frame
28. `disquiet` → FEAR_WORDS, tier 2 — "Disquiet grows in Albanese's back yard…" +50 → 0 (research.py; dashboard ≈−9 — corrects a hope misfire: lone `unite` fired while `disquiet` was unscored)
29. `jailed`/`jail` → FEAR_WORDS, tier 2 — "…children's author … jailed over child exploitation material" +50 → 0 (research.py; dashboard ≈−9); recurred in the Kenyan sect-leader headline 11-07, 11-08, 11-09, 11-10, 11-12, 11-13 — six recurrences, still −50 off `murder` alone
30. `ban`/`bans` → FEAR_WORDS, tier 2 — "Australia's social media ban…" / "Denmark pushes for EU ban…" 0 → −50 each
31. `worst` → FEAR_WORDS, tier 2 — judge with line 32; either alone leaves the Aukus headline positive on the fuller version with `deal`
32. `riskiest` → FEAR_WORDS, tier 2 — same Aukus headline; superlative paradigm gap (`risky`/`risks` already listed); together lines 31+32 re-stage 0 → −100 on the headline as recorded
33. `face`/`faces`/`facing`/`faced` → FEAR_WORDS, tier 2 — "ANC faces anger over poor services…" / "Australia faces same issues…" / "Falkland Islanders face 'devastating consequences'…" 0 → −50 each; with line 37 on the ANC headline 0 → −100 (recurred 11-17, 11-18 in the same ANC/NZ headlines)
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
52. Negation-scope extension (scorer logic, no word add) — treat cognition-verb negations ("not convinced", "no evidence", "doubts that") + a lexicon word in the same clause as a damp-to-neutral: "I'm not convinced the AI bubble exists" −50 → 0. Backed by Hogenboom et al. 2011 (fixed 2-word window + optimized inversion factor), Zhu et al. 2014 (negator-dependent sentiment), Carrillo-de-Albornoz & Plaza 2013 (emotion-based modifier modeling), and Okpala et al. 2023 (negation detection + antonymization improving lexicon analyzers). Caveat: narrow pattern list only; broader clause parsing is the parked NegBERT route.

### Batch 6 — Exclusions (preventive no-ops; neither word is in any scored set today)
53. `drone` → EXCLUDED_WORDS (maker-neutral "I built a drone…" stays 0; attack headlines already score via attack/kills)
54. `body` → EXCLUDED_WORDS (high-ambivalence noun; fear frames already carried by murder/kills/attack)

### Batch 7 — Removal
55. `surge`/`surging`/`surged` → REMOVE from HOPE_WORDS — magnitude word, not a valence word: its pole rides entirely on its object. Three days of fear-framed recurrences, all +50 off lone `surge`: "Ukraine captures first Indonesian prisoner of war amid surge in Russian recruitment" (11-11, 11-12, 11-13) and "What's behind Australia's surge in teen extremism?" (11-13, new story). Re-staged: +50 → 0 on removal for both. Note a tier-1 demotion would NOT fix it: the single-hit rule gives ±50 regardless of tier, so removal is the honest fix — and if picked, line 2 (demotion) is moot. Update: the cluster returned once with a fresh story on 11-23 ("Gas prices in Europe surge as forecast cold snap feeds supply shortage fears" scores −20 off `fears`/`shortage` vs `surge` — the magnitude word dilutes a fear frame it should not oppose), then went quiet again 11-24 → 11-27.

### Batch 8 — Guardian fear (2026-11-14 → 2026-11-20)
56. `outage`/`outages` → FEAR_WORDS, tier 2 — "Microsoft 'deeply sorry' for global outage that could have billion-dollar impact on Australia" and "US-bound flights out of Australia delayed after telecommunications outage grounded American planes" both 0 → −50 (re-staged). Unlike `surge`, `outage` has no positive pole — a service outage is always a disruption.
57. `arrested` → FEAR_WORDS, tier 2 — "US basketball player arrested with 75lb of marijuana at Nigerian airport, say authorities" 0 → −50; "Hundreds arrested in anti-Trump protests in Philippines amid anger over Iran war and AI pact" 0 → −50 alone, 0 → −100 together with line 58. Extends the open `jailed` family (line 29); no jail-family word is in any lexicon today.
58. `war` → FEAR_WORDS, tier 2 — morphological gap, not a new concept: the lexicon lists `wars`/`warfare` but not the singular, and scoring is exact-token, so the protests headline above scores neutral despite the war frame. Single occurrence this week, so judge as a fix-up of an existing entry. With line 57 on the same headline 0 → −100.
59. `accused` → FEAR_WORDS, tier 1 — "European Commission accused of sugarcoating figures to release funds to Egypt" and "Trump accused of falling asleep during Xi Jinping speech at Apec summit in China" both 0 → −50 (re-staged). Procedural tier-1 family like `allegations`/`deny`; the accusation frame is fear-leaning even when the charge is mild.

### Batch 9 — Hacker News (2026-11-14 → 2026-11-20)
60. `vulnerability`/`vulnerabilities` → PESSIMISM_WORDS (default tier 2) — "Project Zero will disclose vulnerabilities 90 days after reporting" 0 → −50 (re-staged). Second occurrence after the 11-06 watch ("MS Paint Remote Code Execution Vulnerability"); extends the open breach cluster (lines 44–47). Caveat: single-story evidence across two days.
61. `attack`/`attacks`/`attacked`/`attacker` → PESSIMISM_WORDS (default tier 2) — "Tor Project Issues Rapid-Response DoS-Defense Fix Amid Sustained DDoS Attack" +50 → 0 (re-staged): the attack frame corrects the lone `fix` optimism toward neutral, never flips it. Cross-spectrum port: already FEAR tier 2.
62. `discover`/`discovered`/`discovers` → OPTIMISM_WORDS (default tier 2) — "Frostbite: A new CPU architecture discovered, designed and verified by AI" and "What people are building, discovered through new domains" both 0 → +50 (re-staged). Cross-spectrum port: already HOPE tier 2. Caveat: the family's ambiguous pole on the Guardian side ("wreck … discovered exactly 128 years after sinking" scores +50 off HOPE on a wreck story) does not carry over — on HN the discovery frame is near-always a launch/breakthrough frame.

### Batch 10 — Mechanism (2026-11-14 → 2026-11-20)
63. `dead code` → new NEUTRAL_PHRASES list (checked pre-token, MWE-first), seeded with "dead code" for both spectra — "Show HN: Unref – A Python dead code finder built on Ruff's parser" scores −50 off tier-3 `dead`, though "dead code" is a fixed neutral tech idiom; `dead` itself stays tier 3 in both spectra (load-bearing for real deaths). Second `dead`-in-a-tech-frame misfire in three days (11-16 "Bring Dead Laptops Back to Life" — different idiom, so the class recurs while the phrase is single-occurrence). Grounded in adopted Chen et al. 2026 MWE-first priority order, WorryMWE compositionality, and Hwang & Hidey 2019 (idiom sentiment is not compositional). Caveat: new mechanism, not a word add — the scorer must skip tokens inside a matched neutral phrase, and the existing MWE machinery only adds fear hits; −50 → 0 is the expected effect, not yet staged end-to-end.

### Batch 11 — Guardian fear + hope, new this week (2026-11-21 → 2026-11-27)
65. `hospitalised`/`hospitalized`/`hospitalise`/`hospitalize` → FEAR_WORDS, tier 2 — "Vape users hospitalised after losing consciousness, prompting public health warning in New South Wales" −50 → −100 (re-staged; cap lift, second hit alongside `warning`). Harm-family gap, siblings `wounded`/`casualties` already listed.
67. `strike`/`strikes` → FEAR_WORDS, tier 2 — "Ukraine confirms it used naval drones to strike two Russian ships off Libya" and "…ICE force-feeding tactics that ended a Cuban father's hunger strike" both 0 → −50 (re-staged). Gap: `attack`/`airstrike` are listed but plain `strike` is absent — a verb-form gap in an existing concept, not a new concept. Caveat: "strike a deal"/"strike gold" positive frames would misfire, bounded at tier 2; labor-strike frames read disruption-negative, consistent pole.
68. `protected` → HOPE_WORDS, tier 1 (mild) — "Australian news outlets demand content is protected from AI scraping" and "Sports whistleblowers protected under proposed laws amid Australian cricket ball tampering saga" both 0 → +50 (re-staged). Protection-of-the-vulnerable frame is the hope pole's defensive side; sibling `save`/`rescue` already listed. Caveat: "protected species"/"protected witness" neutral frames would also fire, keep tier 1; the ±50 single-hit cap bounds each headline to 0 → +50 only.

### Batch 12 — Hacker News, new this week (2026-11-21 → 2026-11-27)
64. `sell-off` → PESSIMISM_WORDS, tier 2 — "Nasdaq erases all 2026 gains as AI sell-off dampens Anthropic's second day" 0 → −50 (re-staged). Finance-decline noun with near-zero neutral-framing risk in headlines; the scorer keeps hyphens in tokens, so the hyphenated form matches as written. Caveat: single occurrence; the ±50 single-hit cap bounds it to 0 → −50.
66. `self-hosted` → OPTIMISM_WORDS, tier 1 (modest) — "PcapAnalyzer – self-hosted pcap analyzer with 27 problem detectors" and "Self-hosted library branch over public web OPDS" both 0 → +50 (re-staged). Self-hosting is a user-control/DIY feature claim with no negative pole in headline use, sibling to the open `built` maker-optimism proposal (line 42). Caveat: product-descriptor word, keep tier 1.

## Dropped in re-verification (not pickable)
- `tariffs` tier 2 → tier 1 demotion (2026-10-21): ALREADY tier 1 in the current FEAR_INTENSITY table (re-confirmed). Nothing to apply; the lone-hit −50 it complained about is the ±50 cap, not the tier — today's "…Trump's new tariff proposals" headline scores −50 off lone `tariff` for the same reason.

## Not pickable (no dashboard change)
- Read the 7-day moving average instead of the single-day index (2026-10-18; Guardian −16.7 this week vs −12.1 prior — the fear run is deepening on average, not easing; HN +1.7 vs +3.1).
- VADER-compound cross-check column in daily research output (2026-10-19; not implemented).

## Discussion notes (observed misfires, no proposal)
- `doom` scores −50 on "Show HN: I Turned DOOM into a Transformer" (game title, not pessimism) — load-bearing elsewhere, no removal proposed.
- `open` scores +50 on "Breaking the open web won't stop the bad bots" (pessimistic frame) — load-bearing optimism vocabulary elsewhere, no removal proposed. Recurred 11-25: "Top open problems in mathematics ranked by LLM-assessed importance" +50 off `open` (math term of art).
- `hard` scores −50 on "…beats Fable 5 on LiveCodeBench Hard" (benchmark difficulty name) — load-bearing elsewhere, no removal proposed. Recurred 11-27: "Hard Drive pricing has gotten bad" −50 off `hard` (pricing frame, not difficulty).
- `slow` (tier 1) dilutes "Bones may release proteins that slow aging and extend life span" (+33) — the neg hit is base-form `slow`, not the `slows`/`slowed` resolution mechanism in line 51.
- `abandoned` scores −50 on "Abandoned Quake 4 expansion finished by modders and now playable" (the expansion was abandoned, but modders finishing it is good news) — load-bearing pessimism vocabulary elsewhere, no removal proposed; same proper-noun/title class as the `doom`/`hard`/`open` misfires.
- `expensive` scores −50 on "Why get an expensive Pi when I have an old phone?" (frugality question, not pessimism) — load-bearing cost vocabulary (tier 1 alongside costly/overpriced), no removal proposed; same question-frame class.
- `dead` scores −50 on "The Secret ThinkPad Powerbutton Code to Bring Dead Laptops Back to Life (2007)" (revival story) — load-bearing elsewhere, no removal proposed; the `dead code` mechanism in line 63 covers the fixed-idiom half of this class only.
- `useless` scores −50 on "The Usefulness of Useless Knowledge [pdf] (1939)" (classic essay title, not pessimism) — load-bearing elsewhere, no removal proposed; same title class.
- `fun` scores +50 on "Serving Qwen via AWS Lambdas for fun and 80x negative profit" (money-loss joke) — load-bearing optimism (tier 1, mild), no removal proposed; `negative` is not in any lexicon, so "negative profit" goes unscored, and there is no PESSIMISM_PHRASES mechanism to catch the phrase.
- `faster` scores +100 on "OpenAI cuts GPT-6.2 usage: Astra hits limits 40% faster, Sol 25% faster" (usage cuts and limits hit faster — bad news) — load-bearing optimism vocabulary (tier 1), no removal/demotion proposed; a fix would need phrase-level handling ("hits limits faster"), and there is no PESSIMISM_PHRASES mechanism — same class as the "negative profit" note above.
- `fix` scores +50 on attack/outage headlines ("Tor Project … DoS-Defense Fix Amid Sustained DDoS Attack", "Microsoft blames monster email outage on software defect introduced in July fix") while the negative frame goes unscored — load-bearing optimism vocabulary, no removal proposed; lines 56 and 61 cover the frames instead.
- `crisis` scores −50 on "EU proposes €45bn loan for Ukraine to avert cash crisis and boost defences" though "avert" negates it — supports the open negation-scope proposal (line 52, negated-verb pattern), no new proposal.
- `discovered` scores +50 on "'Remarkable luck': wreck of first Australian-built warship discovered exactly 128 years after sinking" (wreck/sinking frame) — single occurrence with a genuinely positive discovery pole, no removal proposed; same ambiguous-pole class as the `dead`/revival misfire.
- Watch: `ddos`/`dos` (single occurrence 11-16, covered by line 61), `defect` (single occurrence 11-17), `scarcity` (single occurrence 11-14; `shortage` already tier-1 fear), `ground stop`/`grounded` (phrase-level gap, needs a second independent story; `outage` line 56 already covers the Guardian flight headline), `ransomware` (single occurrence 11-10, breach cluster; 11-27's "RansomwareHelp" is a company-name token, not a recurrence), `threaten` (watch since 11-08, never recurred), `oil` (single-story 11-12), `close` / `stop` (single occurrences 11-11, too ambivalent alone), `execution` (single occurrence 11-19, "remote code execution" — `execution` alone is ambiguous), `erases`/`dampens` (single occurrences 11-21, same sell-off headline as line 64).

## Standard caveats
- The ±50 cap means lone-word demotions (lines 1–2) barely move anything: they are invisible on lone-word headlines and bite only in mixed headlines.
- Second hits lift caps rather than deepen a lone score: lines 18, 19, 21, 23, 24, 26, 27, 29, 38, 41, 57+58, 65 move their evidence headlines −50 → −100, which is a cap lift, not a lone-word demotion.
- research.py does not model the dashboard's Guardian 1.2× fear multiplier, so re-staged Guardian mixed-headline numbers read slightly milder than the live widget's; dashboard-adjusted ≈ values are given where they differ. (MWEs are still not modelled in research.py.)
- The 2026-10-23 Friday patches (batches 1–4 drafts) still exist in hidden_files but were written against the pre-OPML tree; if any batch above is approved, apply fresh rather than applying those hunks blindly.
- Recorded skips stay recorded (vaccine, deportation, leave, exit, blast, against, march, takes, ousted, cuts, feral, chatgpt, court, rate, efficient, job, found, code, rights, public, agents, likely, investigation, house, kernel, release [Guardian-only], home, race, used, forces, ended, alleged, defence, old, inquiry, police, steer, and the noise words): none are re-proposed here.

## Awaiting
User's line-number reply (any, all, or none). On reply: move decided items to
`hidden_files/decisions-2026-11-27.md` and clear them from `weekly-backlog.md`;
undecided items stay flagged for the following week. Nothing was applied or cleared
in this run.
