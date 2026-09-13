// Proposal 3 validation: score a GoodNewsEveryone sample with the dashboard's
// REAL lexicons (extracted from server.ts) and compare lean vs gold labels.
import { readFileSync } from "fs";

const src = readFileSync(
  process.env.HOME + "/workspace/your_files/daily-briefing/src/server.ts",
  "utf8"
);
function getSet(name) {
  const start = src.indexOf(`const ${name} = new Set(`);
  const end = src.indexOf(");", start);
  return new Set(
    [...src.slice(start, end).matchAll(/"([^"]*)"/g)]
      .map((m) => m[1]).join(" ").split(/\s+/).filter(Boolean)
  );
}
const FEAR_WORDS = getSet("FEAR_WORDS"), HOPE_WORDS = getSet("HOPE_WORDS");
const PESS_WORDS = getSet("PESSIMISM_WORDS"), OPT_WORDS = getSet("OPTIMISM_WORDS");
const EXCLUDED = getSet("EXCLUDED_WORDS"), NEGATORS = getSet("NEGATORS");

function score(title, negWords, posWords) {
  const tokens = title.toLowerCase().replace(/[^a-z0-9'\s-]/g, " ").split(/\s+/).filter(Boolean);
  let neg = 0, pos = 0;
  const negHits = [], posHits = [];
  tokens.forEach((raw, i) => {
    const word = raw.replace(/^'+|'+$/g, "");
    if (EXCLUDED.has(word)) return;
    let kind = null;
    if (negWords.has(word)) kind = "neg";
    else if (posWords.has(word)) kind = "pos";
    if (!kind) return;
    const prev = tokens.slice(Math.max(0, i - 2), i).map((t) => t.replace(/^'+|'+$/g, ""));
    if (prev.some((t) => NEGATORS.has(t) || t.endsWith("n't"))) return; // neutralize
    if (kind === "neg") { neg++; negHits.push(word); } else { pos++; posHits.push(word); }
  });
  const total = neg + pos;
  const raw = total === 0 ? 0 : Math.round((100 * (pos - neg)) / total);
  const index = total === 1 ? Math.max(-50, Math.min(50, raw)) : raw;
  return { neg, pos, index, negHits, posHits, tokens };
}

const lines = readFileSync("/tmp/gne/gne.jsonl", "utf8").trim().split("\n");
const recs = [];
for (const ln of lines) {
  try {
    const o = JSON.parse(ln);
    const gold = o?.annotations?.dominant_emotion?.gold;
    if (gold && o.headline) recs.push({ h: o.headline, gold });
  } catch { /* skip */ }
}

// spectrum eval sets: only headlines whose gold label sits on that spectrum
const spectra = {
  "fear-hope": { nw: FEAR_WORDS, pw: HOPE_WORDS, neg: new Set(["fear"]), pos: new Set(["joy", "optimism", "love", "trust"]) },
  "pessimism-optimism": { nw: PESS_WORDS, pw: OPT_WORDS, neg: new Set(["negative_anticipation_including_pessimism"]), pos: new Set(["positive_anticipation_including_optimism"]) },
};

const out = {};
for (const [name, sp] of Object.entries(spectra)) {
  const sub = recs.filter((r) => sp.neg.has(r.gold) || sp.pos.has(r.gold));
  let tp = 0, fp = 0, tn = 0, fn = 0, neutral = 0;
  const missTok = {}, fpTok = {};
  for (const r of sub) {
    const s = score(r.h, sp.nw, sp.pw);
    const goldNeg = sp.neg.has(r.gold);
    const lean = s.index < 0 ? "neg" : s.index > 0 ? "pos" : "neu";
    if (lean === "neu") {
      neutral++;
      // coverage gap: which content tokens appear in missed polarized headlines?
      for (const t of new Set(s.tokens)) {
        const w = t.replace(/^'+|'+$/g, "");
        if (w.length > 3 && !EXCLUDED.has(w) && !sp.nw.has(w) && !sp.pw.has(w)) missTok[w] = (missTok[w] || 0) + 1;
      }
      continue;
    }
    if (goldNeg && lean === "neg") tp++;
    else if (!goldNeg && lean === "pos") tn++;
    else if (goldNeg && lean === "pos") fn++;
    else fp++;
    if ((goldNeg && lean === "pos") || (!goldNeg && lean === "neg")) {
      const hits = goldNeg ? s.posHits : s.negHits; // the wrong-direction cue words
      for (const w of hits) fpTok[w] = (fpTok[w] || 0) + 1;
    }
  }
  const top = (m, n) => Object.entries(m).sort((a, b) => b[1] - a[1]).slice(0, n);
  const decided = tp + fp + tn + fn;
  out[name] = {
    n: sub.length,
    goldNeg: sub.filter((r) => sp.neg.has(r.gold)).length,
    goldPos: sub.filter((r) => sp.pos.has(r.gold)).length,
    coverage: +(100 * decided / sub.length).toFixed(1) + "%",
    neutralPct: +(100 * neutral / sub.length).toFixed(1) + "%",
    directionPrecision: decided ? +(100 * (tp + tn) / decided).toFixed(1) + "%" : "n/a",
    recallNeg: (tp + fn) ? +(100 * tp / (tp + fn)).toFixed(1) + "%" : "n/a",
    recallPos: (tn + fp) ? +(100 * tn / (tn + fp)).toFixed(1) + "%" : "n/a",
    topMissedTokens: top(missTok, 12),
    topWrongDirectionCues: top(fpTok, 12),
  };
}
console.log(JSON.stringify(out, null, 1));
