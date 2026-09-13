# GoodNewsEveryone validation — 2026-09-13

Scored the 5,000 phase-2 headlines (`gne-release-v1.0.jsonl`, gold
`dominant_emotion`) with the dashboard's real lexicons (extracted from
`server.ts`; same scoring logic incl. negation neutralization and the
single-word ±50 cap).

Eval sets: only headlines whose gold label sits on the spectrum.

## fear ↔ hope (n=807: 419 gold fear, 388 gold joy/optimism/love/trust)

- Coverage 35.6% (64.4% neutral) — the lexicon fires on about a third of
  emotionally polarized headlines.
- Direction precision when firing: 86.1%.
- Recall: 90.4% on fear, 74.4% on hope — the hope side is weaker.
- Wrong-direction cues are low-count noise (deal 4, win 3, peace 3…).
- Missed tokens are mostly stopwords — no single obvious missing cue word.

## pessimism ↔ optimism (n=642)

Gold labels in this release are `negative_anticipation_including_pessimism`
(323) and `positive_anticipation_including_optimism` (319).

- Coverage 12.1% (87.9% neutral) — the HN-tuned lexicon barely fires on
  general news. Expected: it was built for tech headlines.
- Direction precision when firing: 80.8%.

## Calibration takeaway

Precision-when-firing is solid on both spectra (81–86%); coverage is the
weak spot, which is inherent to a cue-list approach rather than a bug.
No strong evidence-backed word change emerges from the misses — the
dominant missed tokens are stopwords and topic words. Notable weak
signal: "deal" (HOPE_WORDS) misfires in fear-gold contexts 4× — worth
watching, too thin to act on.

Method note: gold labels are reader-perceived dominant emotions, so this
measures directional agreement, not exact scoring.
