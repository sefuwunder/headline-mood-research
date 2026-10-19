# Weekly lexicon backlog

Proposals accumulate here through the week (one dated section per day, appended by the daily research run). The Friday run consolidates them into one apply-ready ask — research daily, decision weekly (user instruction 2026-10-16).

Format per entry: one line — the change + its grounding + verification status.

Decided items move to dated `decisions-YYYY-MM-DD.md` notes; this file keeps only open items.

## 2026-10-17
- `controversial` → FEAR_WORDS tier 1 — today's Guardian gap words: 2 headlines, both fear-framed ("Guinea-Bissau denies it has approved controversial vaccine trial in newborns", "Controversial vaccine trial touted by RFK Jr gets go-ahead in Guinea-Bissau"); "trial" itself was decided → EXCLUDED 2026-10-16, so the framing word carries the signal. Verification: not yet re-staged against the real scorer.
- `built` → OPTIMISM_WORDS — today's HN gap words (2x): "I built the RealWorld app in Lean 4", "I got tired of btop not seeing my Mac's chip, so I built siltop"; maker-announcement optimism, siblings shipped/launched/released already listed. Verification: not yet re-staged against the real scorer.
- `deforestation` → FEAR_WORDS tier 1 — today's Guardian gap words (2x): "Revealed: VW, Ford and Tesla batteries linked to destructive deforestation of indigenous lands"; caveat per Loughran–McDonald domain audit: "deforestation falls to lowest on record" is positive news, so keep tier 1 modest. Verification: not yet re-staged against the real scorer.

## 2026-10-18
- `protests` → FEAR_WORDS tier 1 — today's Guardian gap words (2x), both unrest/crisis framing ("Arrests over France protests rise to 1,800, with whole streets in Paris 'devastated'", "'We are suffocating': protests spread to Lisbon and Milan as housing and living cost tensions intensify"); siblings `arrests` already → fear. Caveat per Loughran–McDonald domain audit: peaceful-protest frames would misfire, keep tier 1 modest. Verification: not yet re-staged against the real scorer.
- `lowest on record` MWE → HOPE_WORDS — resolution framing today's scorer misses: "Brazilian Amazon deforestation falls to lowest on record as pivotal vote looms" is good news that would score as fear if `deforestation` (2026-10-17 backlog) is applied; same resolution/downtoner class as the Schulder et al. 2018 "outbreak has peaked" misfire (adopted). Verification: not yet re-staged against the real scorer.
- Read the 7-day moving average of trend.jsonl instead of the single-day index — today's lit scan (Teodorescu & Mohammad 2022, adopted): lexicon-only instance scores are noisy but aggregate emotion arcs are high-fidelity; overlapping 7-day windows smooth the arc. Today's Guardian -16 (after -22 / 0 in the two prior days) is a spike, not a trend — the 7d mean tells the real story. Verification: computable directly against existing trend.jsonl; no dashboard change needed.

## 2026-10-19
- `hostile`/`hostility` → FEAR_WORDS (default tier 2) — today's Guardian gap words: 2 neutral-scored headlines carry the framing ("Falklands again face a hostile Argentina", "Pregnant women face workplace hostility") yet scored 0; the signal word is unscored while sibling threat-family words (threat/threatening) are already listed at tier 2. Verification: not yet re-staged against the real scorer.
- `menace`/`menaces` → FEAR_WORDS (default tier 2) — today's Guardian sample ("Hurricane Trudy menaces Mexico's Pacific coast"): the threat verb went unscored (only deadly/floods/hurricane fired); direct synonym of listed threaten/threatening, same domain behavior. Verification: not yet re-staged against the real scorer.
- Add a VADER-compound cross-check column to the daily research output — Ethelb & Balhouq 2025 (headline-domain VADER/human agreement κ=0.82; VADER compound as independent cross-check) + adopted 2026-10-05 (keep separate indicators, don't fuse): a second lexicon read distinguishes real mood shifts from single-lexicon artifacts — matters now, with the Guardian on a three-day fear run (-22, -16, -20). No dashboard change. Verification: not yet implemented.
