# Mood-scoring bibliography

Running record of research papers reviewed for the headline-mood lexicon work.
Each entry: title, authors/year, link, one-line idea, verdict (adopted / rejected + reason / parked).

## 2026-09-10 — deep survey in progress
A broad survey of lexicon-based sentiment/emotion approaches (classic: LIWC, VADER,
AFINN, NRC, SentiWordNet; recent: embedding-expanded lexicons, hybrid lexicon+transformer
methods, negation-scope handling) was commissioned 2026-09-10. Findings will be
distilled into entries below when they land.

## 2026-09-10 — deep survey results (~24 papers)
- VADER (Hutto & Gilbert 2014) — https://eecs.csuohio.edu/~sschung/CIS593/VADER_Paper2014_AAAI.pdf — 7,500 graded features + 5 heuristics (punctuation, caps, intensifiers, "but"-clauses, negation window); beat human raters on tweets. Verdict: parked — intensifier weighting + wider negation window are the most portable ideas for our scorer.
- AFINN (Nielsen 2011) — https://ar5iv.labs.arxiv.org/html/1103.2903 — 2,477 words hand-scored -5..+5 valence. Verdict: parked — graded intensity beats binary counts; could rescore our word lists on a -5..+5 scale.
- NRC Emotion Lexicon (Mohammad & Turney 2013) — https://web3.arxiv.org/pdf/1308.6297 — 14k words x 8 Plutchik emotions via crowdsourcing. Verdict: parked — candidate source for expanding fear/hope lists.
- NRC VAD Lexicon (Mohammad 2018) — https://aclweb.org/anthology/P18-1017.pdf — 20k words with valence/arousal/dominance 0..1; fear ~= low valence + high arousal, hope ~= high valence. Verdict: parked — continuous VAD ratings could replace discrete word lists for both spectra.
- SentiStrength (Thelwall et al. 2010) — http://ideas.repec.org/a/bla/jamist/v61y2010i12p2544-2558.html — dual 1-5 pos/neg scales, booster/negation rules, built for short informal text. Verdict: parked — dual-accumulator design maps directly onto fear<->hope / pessimism<->optimism.
- DepecheMood (Staiano & Guerini 2014) — http://arxiv.org/pdf/1405.1605 — 37k terms incl. "afraid", harvested from news readers' emotion votes; most domain-matched to headlines. Verdict: parked — best off-the-shelf news-domain emotion lexicon.
- SentProp (Hamilton et al. 2016) — http://arxiv.org/abs/1606.02820v1 — random-walk label propagation over embeddings to induce domain lexicons from seeds. Verdict: parked — principled way to grow our tech/pessimism list.
- SemEval-2007 Task 14 Affective Text (Strapparava & Mihalcea) — https://aclanthology.org/S07-1013.pdf — 1,250 news headlines scored on 6 emotions 0-100 + valence. Verdict: parked — ideal validation set for our scorer.
- Loughran & McDonald 2011 — https://doi.org/10.1111/j.1540-6261.2010.01625.x — ~75% of a general lexicon's negative words misfire in finance text. Verdict: adopted as principle — audit every lexicon word against the target domain (HN vs Guardian separately).
- Kotelnikov 2021 — http://arxiv.org/abs/2111.10097v1 — lexicon method (SO-CAL) beat RuBERT on 4/16 corpora. Verdict: noted — lexicons remain competitive; no need to reach for heavy models yet.
- NegBERT (Khandelwal & Sawant 2020) — http://arxiv.org/abs/1911.04211 — BERT-based negation cue+scope resolution, F1 ~91-96. Verdict: parked — full syntax-aware negation is overkill today, but worth revisiting if negation errors pile up.

## 2026-09-12 — literature scan
- Polanyi & Zaenen (2006), "Contextual Valence Shifters" — https://doi.org/10.1007/1-4020-4102-0_1 — negators, intensifiers and modals shift a word's valence along a scale rather than flipping it: a negated negative moves toward neutral, not to positive ("not bad" ≠ "good"). Verdict: adopt — today's HN sample ("SystemIO conflicts are not firmware bugs" → +100 optimism from a single negated "bugs") shows the scorer's sign-flip overreaches; negated hits should damp toward neutral.

## 2026-09-11 — literature scan
- TriLex (Alharbi, Aljurbua, Gupta & Obradovic, 2025) — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0317100 — unsupervised fusion of TextBlob/VADER/AFINN via majority vote + cross-lexicon score normalization beat individual lexicons by 2-8% on short texts. Verdict: watch — score normalization across two spectra is portable; full fusion is heavier than our needs.

## 2026-09-13 — literature scan
- [GoodNewsEveryone: A Corpus of News Headlines Annotated with Emotions, Semantic Roles, and Reader Perception](http://arxiv.org/pdf/1912.03184v1) — Bostan et al., 2020 — 9,932 news headlines annotated with 15 emotions including Optimism/Pessimism and Fear, from both reader and writer perspectives. Verdict: adopt — headline-domain validation set matching our two spectra almost label-for-label; complements the parked SemEval-2007 set.
- [DepecheMood++: a Bilingual Emotion Lexicon Built Through Simple Yet Powerful Techniques](http://arxiv.org/pdf/1810.03660v1) — Staiano & Guerini, 2018 — refresh of the parked DepecheMood with improved extraction and validation; validates on headlines by averaging word-level emotion scores, the same aggregation our scorer uses. Verdict: watch — AFRAID/INSPIRED dimensions map onto fear/hope and could gap-fill our lists once diffed against current lexicons.
