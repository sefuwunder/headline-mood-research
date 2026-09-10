# Headline mood research

Daily research artifacts for refining the headline-mood scoring on the
[daily-briefing](https://github.com/sefuwunder/daily-briefing) dashboard.

- Hacker News headlines are scored on **pessimism ↔ optimism**
- The Guardian world headlines are scored on **fear ↔ hope**

## Files

- `research.py` — fetches the day's HN front page (Algolia API) and Guardian
  world RSS, scores headlines with the dashboard's word-list lexicons (parsed
  from its `src/server.ts`), appends the day's indices to `trend.jsonl`, and
  prints JSON including candidate gap words.
- `trend.jsonl` — one line per day: `{date, hn_index, hn_n, guardian_index, guardian_n}`.
- `bibliography.md` — running record of research papers reviewed
  (title, authors/year, link, one-line idea, verdict).

## Method

Lexicon-based scoring with basic negation handling. Each headline gets an index
from -100 (negative pole) to +100 (positive pole), averaged per source. A
vibe check, not science — the daily research proposes evidence-backed lexicon
tweaks, and a human approves them.
