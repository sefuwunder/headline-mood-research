#!/usr/bin/env python3
"""Daily mood-scoring research.

Fetches today's Hacker News front page + Guardian world headlines, scores them
with the dashboard's current lexicons (parsed from src/server.ts), appends the
day's indices to trend.jsonl, and prints JSON including candidate words found in
neutral-scored headlines (lexicon gaps worth considering).
"""
import json
import re
import urllib.request
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SERVER_TS = Path.home() / "workspace" / "your_files" / "daily-briefing" / "src" / "server.ts"
TREND = ROOT / "trend.jsonl"

NEGATORS = {
    "not", "no", "never", "neither", "none", "without", "cannot", "can't", "won't",
    "isn't", "aren't", "wasn't", "weren't", "don't", "doesn't", "didn't", "couldn't",
    "shouldn't", "wouldn't", "hasn't", "haven't", "hadn't",
}

STOPWORDS = set(
    """a an the and or of to in on for with at by from as is are was were be been being
    it its this that these those i you he she we they them his her our their my your me
    so nor but if then than too very can will just now new over under out up down off
    all any each more most other some such only own same via vs de la le les des du
    der die das und im zur zum den einem einer eine says say said tells told asks asked
    after before during while again once here there when where which who whom whose what
    why how do does did doing have has had having would could should may might must shall
    wont cant dont isnt arent wasnt werent hasnt havent hadnt couldnt shouldnt wouldnt
    im ive id youre hes shes theyre weve us also per per cent pct""".split()
)


def load_lexicons():
    src = SERVER_TS.read_text()
    out = {}
    for name in ("FEAR_WORDS", "HOPE_WORDS", "PESSIMISM_WORDS", "OPTIMISM_WORDS"):
        m = re.search(
            r"const " + name + r" = new Set\(\s*\((.*?)\)\.split", src, re.S
        )
        if not m:
            raise RuntimeError(f"could not parse {name} from server.ts")
        words = []
        for chunk in re.findall(r'"([^"]*)"', m.group(1)):
            words.extend(chunk.split())
        out[name] = set(words)
    return out


def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def hn_headlines(n=35):
    body = json.loads(
        fetch("https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=40")
    )
    items = []
    for h in body.get("hits", [])[:n]:
        if h.get("title"):
            items.append(
                {
                    "title": h["title"],
                    "link": h.get("url")
                    or f"https://news.ycombinator.com/item?id={h.get('objectID')}",
                }
            )
    return items


def guardian_headlines(n=25):
    xml = fetch("https://www.theguardian.com/world/rss")
    items = []
    for m in re.finditer(r"<item>(.*?)</item>", xml, re.S):
        block = m.group(1)
        t = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", block, re.S)
        l = re.search(r"<link>(.*?)</link>", block, re.S)
        if t and l:
            items.append({"title": t.group(1).strip(), "link": l.group(1).strip()})
        if len(items) >= n:
            break
    return items


def tokenize(title):
    return [
        t
        for t in re.sub(r"[^a-z0-9'\s-]", " ", title.lower()).split()
        if t
    ]


def score(title, neg_words, pos_words):
    tokens = tokenize(title)
    neg = pos = 0
    neg_hits, pos_hits = [], []
    for i, raw in enumerate(tokens):
        word = raw.strip("'")
        kind = "neg" if word in neg_words else ("pos" if word in pos_words else None)
        if not kind:
            continue
        prev = [t.strip("'") for t in tokens[max(0, i - 2) : i]]
        # Negators neutralize valence rather than flipping polarity
        # (Polanyi & Zaenen 2006) — matches the dashboard.
        if any(t in NEGATORS or t.endswith("n't") for t in prev):
            continue
        if kind == "neg":
            neg += 1
            neg_hits.append(word)
        else:
            pos += 1
            pos_hits.append(word)
    total = neg + pos
    index = 0 if total == 0 else round(100 * (pos - neg) / total)
    return {
        "index": index,
        "neg": neg,
        "pos": pos,
        "negWords": sorted(set(neg_hits))[:5],
        "posWords": sorted(set(pos_hits))[:5],
    }


def summarize(scored):
    n = len(scored)
    return {
        "count": n,
        "index": round(sum(s["index"] for s in scored) / n) if n else 0,
        "negLeaning": sum(1 for s in scored if s["index"] <= -20),
        "posLeaning": sum(1 for s in scored if s["index"] >= 20),
        "neutral": sum(1 for s in scored if -20 < s["index"] < 20),
    }


def load_excluded():
    """Words reviewed and rejected as mood signals (EXCLUDED_WORDS in server.ts)."""
    src = SERVER_TS.read_text()
    m = re.search(r"const EXCLUDED_WORDS = new Set\(\[(.*?)\]\);", src, re.S)
    if not m:
        return set()
    return set(re.findall(r'"([^"]+)"', m.group(1)))


def candidates(scored_items, lexicon_words, excluded):
    """Frequent non-lexicon words inside neutral-scored headlines."""
    freq = Counter()
    examples = {}
    for item, s in scored_items:
        if abs(s["index"]) >= 20:
            continue
        for tok in tokenize(item["title"]):
            w = tok.strip("'")
            if len(w) > 2 and w not in lexicon_words and w not in STOPWORDS and w not in excluded:
                freq[w] += 1
                examples.setdefault(w, []).append(item["title"])
    out = []
    for w, c in freq.most_common(15):
        if c >= 2:
            out.append(
                {"word": w, "count": c, "examples": examples[w][:2]}
            )
    return out


def main():
    lex = load_lexicons()
    hn = hn_headlines()
    g = guardian_headlines()

    hn_scored = [
        (h, score(h["title"], lex["PESSIMISM_WORDS"], lex["OPTIMISM_WORDS"])) for h in hn
    ]
    g_scored = [
        (h, score(h["title"], lex["FEAR_WORDS"], lex["HOPE_WORDS"])) for h in g
    ]
    hn_sum, g_sum = summarize([s for _, s in hn_scored]), summarize(
        [s for _, s in g_scored]
    )

    # trend log
    ROOT.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    last_date = None
    if TREND.exists():
        lines = TREND.read_text().strip().splitlines()
        if lines:
            last_date = json.loads(lines[-1]).get("date")
    if last_date != today:
        with TREND.open("a") as f:
            f.write(
                json.dumps(
                    {
                        "date": today,
                        "hn_index": hn_sum["index"],
                        "hn_n": hn_sum["count"],
                        "guardian_index": g_sum["index"],
                        "guardian_n": g_sum["count"],
                    }
                )
                + "\n"
            )

    hn_lex = lex["PESSIMISM_WORDS"] | lex["OPTIMISM_WORDS"]
    g_lex = lex["FEAR_WORDS"] | lex["HOPE_WORDS"]
    excluded = load_excluded()

    report = {
        "date": today,
        "hn": {**hn_sum, "spectrum": "pessimism↔optimism"},
        "guardian": {**g_sum, "spectrum": "fear↔hope"},
        "hn_candidates": candidates(hn_scored, hn_lex, excluded),
        "guardian_candidates": candidates(g_scored, g_lex, excluded),
        "hn_sample": [
            {"title": h["title"], **s} for h, s in hn_scored if s["index"] != 0
        ][:10],
        "guardian_sample": [
            {"title": h["title"], **s} for h, s in g_scored if s["index"] != 0
        ][:10],
    }
    print(json.dumps(report, indent=1))


if __name__ == "__main__":
    main()
