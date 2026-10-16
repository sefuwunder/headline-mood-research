# Consolidated lexicon apply-list — 2026-10-15

All undecided proposals from Oct 12–15 in one list, with the exact code change
staged as a patch and every claimed effect verified against the dashboard's
real scorer before/after.

Patch: `~/workspace/goals/refine-the-headline-mood-scoring/hidden_files/lexicon-consolidated-2026-10-15.patch`
Applies to `~/workspace/your_files/daily-briefing/src/server.ts` with `git apply`.
Verified: patch applies cleanly, the patched file bundles + parses, and the
extracted scorer was run before/after on 17 example headlines (bun).

## Group A — corrected older pack (Oct 14 letter, still undecided)
1. Demote `wins` one hope tier (2 → 1)
2. Demote `surge` one hope tier (2 → 1)
3. Add `self-replicate` → PESSIMISM_WORDS
4. Add `power` / `legal` / `action` → EXCLUDED_WORDS
5. `death threats` MWE → DECISION: weight 2 on top of existing single-word
   hits, or omit entirely

## Group B — Oct 14 morning three (still undecided)
6. `backdoor` / `backdoors` → PESSIMISM_WORDS, plus `spy chip` MWE
   (patch adds a PESSIMISM_MWES list and wires it into the spectrum —
   HN pole had no MWE plumbing before)
7. `arrests` → FEAR_WORDS, mild tier 1
8. `trial` → EXCLUDED_WORDS

## Group C — Oct 15 morning three (asked 07:26 EDT, still undecided)
9. `poisoning` → FEAR_WORDS, tier 2
10. `betrayal` → FEAR_WORDS, tier 2
11. `deny` / `denies` / `denied` as implicit-negation cues — new DENIAL_VERBS
    set, 4-token lookback, neutralizes like a negator on both poles

Held (not in patch): the ×0.7 downtoner tier — needs the cited paper read first.

## Verified effects (real scorer, before → after)
- poisoning / betrayal / arrests / backdoor / spy chip / spy-chip headlines:
  0 → −50 or +50 → −50, as proposed.
- "Guinea-Bissau denies it has approved controversial vaccine trial in
  newborns": +50 → 0. (The 2-token negator window would never have caught it;
  the denial sits 3 tokens back — hence the 4-token window.)
- wins demotion: invisible on lone-word headlines (single-hit scores cap at
  ±50 either way). Shows up in mixed headlines: "startup wins funding amid
  fears of market crash" −33 → −60. Same mechanics for surge.
- spy chip needed BOTH forms: the tokenizer keeps hyphens, so "spy-chip"
  never matches the "spy chip" phrase — the patch ships both MWE entries.
- death threats at weight 2 (decision item, NOT in patch): −25 → −40 on a
  mixed headline; pure-fear headlines sit at −100 either way (the "40% louder"
  is in fear points, 5 → 7, exactly as the letter said).
- power / legal / action / trial exclusions: zero scoring change today — none
  of the four appear in any scored list. Purely preventive (guards future
  lexicon additions).

## Honest caveats
- The deny-verbs change mutes fear hits too, not just hope: "CEO denies
  fraud allegations in leaked memo" −50 → 0. That's the price of the
  implicit-negation mechanism; it neutralizes, never flips.
- The wins/surge demotions are near-no-ops for the ceremonial one-word
  headlines that motivated them (the ±50 cap), and mostly bite in
  mixed-valence headlines.

## The "2 & 3" ambiguity
The Oct 14 14:59 "2 & 3" reply landed minutes after the lexicon correction
letter and was read as the Sherry skills answer (reminders + Abba capture —
built, 132/132). Under the lexicon reading it meant #2 arrests + #3 trial
from that morning's three. It was never corrected, so arrests and trial stay
on this list awaiting their own word — the user can resolve it in one line.

## Applying
On the user's answer: `git apply` the patch in the daily-briefing tree,
re-run the 17-headline check, rebuild the zip, run the pre-push hash audit,
push. Patch is dated; re-verify against the tree if days pass.
