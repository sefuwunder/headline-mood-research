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

## 2026-09-14 — literature scan
- [Sentiment analysis methods for understanding large-scale texts: a case for using continuum-scored words and word shift graphs](https://link.springer.com/article/10.1140/epjds/s13688-017-0121-9) — Reagan, Danforth, Tivnan, Williams & Dodds, 2017 — dictionary methods only produce trustworthy scores when (1) the dictionary covers a frequency-weighted share of the text's lexicon and (2) words are scored on a continuum, not binary; word shift graphs decompose a score into per-word contributions so misfiring words are visible. Verdict: adopt — a per-word contribution audit is the natural debugging view for our daily index swings, and it strengthens the case for graded intensity tiers.
- [The advantages of lexicon-based sentiment analysis in an age of machine learning](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0313092) — van der Veen & Bleich, 2025 — MultiLexScaled (averaging valences across multiple lexicons) validates strongly across domains; binarized valence metrics give wrong conclusions where gradations carry the signal. Verdict: watch — averaging our two-spectra lists with NRC VAD / DepecheMood could smooth single-word spikes, but adds dependency weight.

## 2026-09-15 — literature scan
- [Introducing a Lexicon of Verbal Polarity Shifters for English](https://aclanthology.org/L18-1222.pdf) — Schulder, Wiegand, Ruppenhofer & Roth, 2018 — 1,200+ verbal polarity-shifter lemmas with scope types; downtoners ("hardly satisfying", "slightly problematic") shift intensity toward neutral rather than flipping polarity. Verdict: watch — ready-made wordlist for a downtoner/resolution-dampener list; today's "outbreak has peaked" misfire is a downtoning case the scorer currently misses.
- [Sentiment Analysis of News Headlines as a Tool for Language Learning Enhancement](https://journals.uot.edu.ly/index.php/flj/article/download/2324/1615) — Ethelb & Balhouq, 2025 — VADER applied to Al-Jazeera/BBC Libya headlines with 20% double-coded at Cohen's κ = 0.82, showing a lexicon scorer agrees with human coders on news headlines specifically. Verdict: watch — headline-domain human-agreement evidence; VADER compound could serve as an independent cross-check of our daily indices.

## 2026-09-13 — literature scan
- [GoodNewsEveryone: A Corpus of News Headlines Annotated with Emotions, Semantic Roles, and Reader Perception](http://arxiv.org/pdf/1912.03184v1) — Bostan et al., 2020 — 9,932 news headlines annotated with 15 emotions including Optimism/Pessimism and Fear, from both reader and writer perspectives. Verdict: adopt — headline-domain validation set matching our two spectra almost label-for-label; complements the parked SemEval-2007 set.
- [DepecheMood++: a Bilingual Emotion Lexicon Built Through Simple Yet Powerful Techniques](http://arxiv.org/pdf/1810.03660v1) — Staiano & Guerini, 2018 — refresh of the parked DepecheMood with improved extraction and validation; validates on headlines by averaging word-level emotion scores, the same aggregation our scorer uses. Verdict: watch — AFRAID/INSPIRED dimensions map onto fear/hope and could gap-fill our lists once diffed against current lexicons.

## 2026-09-16 — literature scan
- [Word Affect Intensities](https://arxiv.org/abs/1704.08798v2) — Saif M. Mohammad, 2018 — NRC Affect Intensity Lexicon: ~6,000 words with real-valued 0–1 fear/joy/sadness/anger intensity ratings via best-worst scaling (split-half reliability > 0.91), a manually curated upgrade from binary emotion flags. Verdict: adopt — fear and joy scores map directly onto the Guardian fear↔hope spectrum; diff against our FEAR/HOPE lists and use the ratings to calibrate (or replace) the hand-set intensity tiers.
- [Lexicon-Based Sentiment Analysis in Behavioral Research](https://pmc.ncbi.nlm.nih.gov/articles/PMC11035532/) — Cero, Luo & Falligant, 2024 — surveys the Sentiment Composition Lexicon of Opposing Polarity Phrases (SCL-OPP; Kiritchenko & Mohammad, 2017): affective words pre-paired with negators, modals, and degree adverbs and re-rated as multiword tokens. Verdict: watch — pre-scored negator/degree phrases are the lowest-effort upgrade path past the current sign-flip negation window.

## 2026-09-18 — literature scan
- [Longitudinal analysis of sentiment and emotion in news media headlines using automated labelling with Transformer language models](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0276367) — Rozado, Hughes & Halberstadt, 2022 — 23M headlines from 47 outlets (2000–2019) auto-labelled for sentiment + Ekman emotions incl. fear; found a steady rise in fear/anger-laden headlines and fewer neutral ones over two decades. Verdict: watch — transformer method, not a lexicon we can borrow, but it's the largest longitudinal headline-emotion track record: our Guardian fear index can be sanity-checked against its long-run negativity slope rather than against daily noise.

## 2026-09-17 — literature scan
- [Optimism, Pessimism, and the Language between: Model Interpretability and Psycholinguistic Profiling](https://aclanthology.org/2025.ranlp-1.141/) — Tabusca & Dinu, 2025 — LIWC + LIME analysis of a RoBERTa optimism/pessimism classifier: optimism and pessimism occupy overlapping yet distinguishable psycholinguistic regions, with influential tokens tied to affective intensity, certainty, and social orientation. Verdict: watch — directly targets our HN spectrum, but gives no reusable word list; the "overlapping regions" finding argues for a margin/borderline review of PESSIMISM_WORDS rather than new additions.

## 2026-09-19 — literature scan
- [Hybrid Negation: Enhancing Sentiment Analysis for Complex Sentences](https://www.mdpi.com/2076-3417/16/2/1000) — Qorib & Cotae, 2026 — clause-aware hybrid negation (explicit/implicit/double-negation rules + dependency-based scope detection) beats pure sign-flip polarity inversion; ablations show dependency scope and double negations contribute the largest gains. Verdict: watch — our fixed-window sign flip is cheap and holds up on headlines; adopt only if negation misfires pile up.
