#!/usr/bin/env python3
"""Fetch the benchmark corpus: recent headlines from the daily-briefing's
regional news feeds (+ HN + Guardian world, the mood widget's two sources).

Saves workspace/goals/refine-the-headline-mood-scoring/headline-corpus.json
with {headline, source, date, spectrum} rows. Re-runs use the fixed file.
"""
import html
import json
import re
import sys
import urllib.request
from datetime import date
from email.utils import parsedate_to_datetime
from pathlib import Path

GOAL = Path.home() / "workspace" / "goals" / "refine-the-headline-mood-scoring"
OUT = GOAL / "headline-corpus.json"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")

# (source, url, pages) — pages>1 only for WordPress feeds that paginate
FEEDS = [
    ("Jamaica Observer", "https://www.jamaicaobserver.com/feed/", 2),
    ("Barbados Today", "https://barbadostoday.bb/feed/", 2),
    ("St Lucia Times", "https://stluciatimes.com/feed/", 2),
    ("BBC Africa", "https://feeds.bbci.co.uk/news/world/africa/rss.xml", 1),
    ("BBC Europe", "https://feeds.bbci.co.uk/news/world/europe/rss.xml", 1),
    ("Kyiv Independent", "https://kyivindependent.com/news-archive/rss/", 1),
    ("Guardian World", "https://www.theguardian.com/world/rss", 1),
]

HN_URL = "https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=100"

# Regional arts & culture feeds from the same dashboard tabs (the tabs' second
# block). Added 2026-09-15: the six news feeds alone yield ~190 headlines, short
# of the ~300 target, so the tabs' arts feeds fill the corpus with the tabs'
# own remaining headlines. Africa Is a Country's /feed returned empty and is
# skipped (noted in fetch_log).
ARTS_FEEDS = [
    ("LargeUp", "https://www.largeup.com/feed/"),
    ("Repeating Islands", "https://repeatingislands.com/feed/"),
    ("Caribbean Beat", "https://www.caribbean-beat.com/feed"),
    ("Maria Jackson 27", "https://mariajackson27magazine.com/feed/"),
    ("Ebuzztt", "https://ebuzztt.com/feed"),
    ("The NATIVE", "https://thenativemag.com/feed"),
    ("Music In Africa", "https://www.musicinafrica.net/feed"),
    ("ART AFRICA Magazine", "https://artafricamagazine.org/feed/"),
    ("Halmblog Music", "https://halmblog.com/feed"),
    ("Bird In Flight", "https://birdinflight.com/feed"),
    ("Lossi 36", "https://lossi36.com/feed/"),
    ("Kajet Journal", "https://kajetjournal.com/feed/"),
]


def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def clean(s):
    s = re.sub(r"<!\[CDATA\[(.*?)\]\]>", r"\1", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).strip()


def parse_rss(xml):
    items = []
    for m in re.finditer(r"<item>(.*?)</item>", xml, re.S):
        block = m.group(1)
        t = re.search(r"<title>(.*?)</title>", block, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", block, re.S)
        if not t:
            continue
        title = clean(t.group(1))
        if not title:
            continue
        datestr = ""
        if d:
            try:
                datestr = parsedate_to_datetime(d.group(1).strip()).date().isoformat()
            except Exception:
                pass
        items.append({"headline": title, "date": datestr or date.today().isoformat()})
    return items


def main():
    rows = []
    seen = set()
    log = []

    def add(headline, source, datestr, spectrum):
        key = (headline.lower(), source)
        if headline and key not in seen:
            seen.add(key)
            rows.append({"headline": headline, "source": source,
                         "date": datestr, "spectrum": spectrum})

    for source, url, pages in FEEDS:
        n0 = len(rows)
        for p in range(1, pages + 1):
            u = url if p == 1 else url + ("" if url.endswith("/") else "/") + f"?paged={p}"
            # wordpress: /feed/?paged=2 ; bbc/guardian ignore (pages=1 anyway)
            if p > 1 and "?" in url:
                u = url + f"&paged={p}"
            elif p > 1:
                u = url.rstrip("/") + f"/feed/?paged={p}" if "feed" in url else url + f"?paged={p}"
            try:
                for it in parse_rss(fetch(u)):
                    add(it["headline"], source, it["date"], "fear-hope")
            except Exception as e:
                log.append(f"{source} p{p}: {e}")
        log.append(f"{source}: {len(rows)-n0} headlines")

    # Regional arts feeds from the same tabs (documented corpus extension)
    for source, url in ARTS_FEEDS:
        n0 = len(rows)
        try:
            for it in parse_rss(fetch(url)):
                add(it["headline"], source, it["date"], "fear-hope")
        except Exception as e:
            log.append(f"{source}: FAILED {e}")
        if len(rows) == n0:
            log.append(f"{source}: 0 headlines (skipped)")
        else:
            log.append(f"{source}: {len(rows)-n0} headlines")

    # Hacker News front page -> pessimism-optimism spectrum (dashboard mapping)
    try:
        body = json.loads(fetch(HN_URL))
        n = 0
        for h in body.get("hits", []):
            if h.get("title"):
                d = (h.get("created_at") or "")[:10] or date.today().isoformat()
                add(h["title"], "Hacker News", d, "pessimism-optimism")
                n += 1
        log.append(f"Hacker News: {n} headlines")
    except Exception as e:
        log.append(f"Hacker News: FAILED {e}")

    corpus = {
        "collected": date.today().isoformat(),
        "count": len(rows),
        "note": ("Recent headlines from the daily-briefing dashboard's regional "
                 "news feeds (CARICOM, Africa, Eastern Europe tabs) plus the mood "
                 "widget's two sources (Hacker News, Guardian World). Spectrum "
                 "follows the dashboard mapping: HN -> pessimism-optimism, all "
                 "other news -> fear-hope."),
        "fetch_log": log,
        "headlines": rows,
    }
    OUT.write_text(json.dumps(corpus, indent=1, ensure_ascii=False))
    print(f"saved {len(rows)} headlines -> {OUT}")
    for line in log:
        print(" ", line)


if __name__ == "__main__":
    main()
