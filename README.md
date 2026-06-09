# AI Engineering Study Notes

A collection of Jupyter notebooks covering foundational NLP concepts and Python programming, built while studying AI Engineering.

---

## Repository Structure

```
ai-engineer/
├── python/
│   └── python-variables.ipynb       # Python fundamentals
├── lower.ipynb                      # Text lowercasing
├── regex.ipynb                      # Regular expressions
├── stop words.ipynb                 # Stop word removal
├── textproeprocessing.ipynb         # Full NLP preprocessing pipeline
├── speech-tagging.ipynb             # Part-of-speech (POS) tagging
├── named entity recognition.ipynb  # Named Entity Recognition (NER)
├── pos-ner-practical.ipynb          # Combined POS + NER on BBC News dataset
├── rule-based-sentitment.ipynb      # Rule-based sentiment analysis
├── bag-of-words.ipynb               # Bag of Words text vectorisation
├── tf-idf.ipynb                     # TF-IDF text vectorisation
├── lda.ipynb                        # Topic modelling with LDA and LSA
├── sentiment-practical.ipynb        # Sentiment analysis on real book reviews
├── bbc_news.csv                     # BBC News headlines dataset (1,000 articles)
├── tripadvisor_hotel_reviews.csv    # TripAdvisor hotel reviews dataset (109 reviews)
├── book_reviews_sample.csv          # Amazon book reviews dataset (100 reviews)
└── news_articles.csv                # News articles dataset (100 articles)
```

---

## Topics Covered

### Python Fundamentals (`python/python-variables.ipynb`)
- Defining and calling functions
- Loops (`for`, `range`, conditional logic)
- Working with lists and dictionaries
- Importing standard library modules (`math`)

### Text Preprocessing

NLP pipelines require raw text to be cleaned before analysis. The notebooks build up each step individually, then combine them.

| Notebook | Concept | Key techniques |
|---|---|---|
| `lower.ipynb` | Lowercasing | `.lower()`, list comprehensions |
| `regex.ipynb` | Regular expressions | `re.search`, raw strings |
| `stop words.ipynb` | Stop word removal | NLTK `stopwords`, custom additions/removals |
| `textproeprocessing.ipynb` | Full pipeline | All steps below, end-to-end on hotel reviews |

#### Full Pipeline (`textproeprocessing.ipynb`)
Applied to the **TripAdvisor hotel reviews** dataset (109 reviews, rated 1–5):

1. **Lowercasing** — normalise text casing
2. **Stop word removal** — remove common words (e.g. "the", "is"), with `"not"` preserved for sentiment
3. **Punctuation handling** — replace `*` with `"star"`, strip remaining punctuation via regex
4. **Tokenisation** — split text into word tokens using `nltk.word_tokenize`
5. **Stemming** — reduce words to root form using NLTK `PorterStemmer` (e.g. `"parking"` → `"park"`)
6. **Lemmatisation** — reduce words to dictionary base form using NLTK `WordNetLemmatizer` (e.g. `"pillows"` → `"pillow"`)
7. **N-gram analysis** — compute unigram and bigram frequency counts across the corpus

Top bigrams found: `(great, location)`, `(space, needle)`, `(hotel, monaco)`

---

### Part-of-Speech Tagging (`speech-tagging.ipynb`)
Using **spaCy** (`en_core_web_sm`) on an opening sentence from *Emma* by Jane Austen:
- Assigns POS tags: `PROPN`, `ADJ`, `NOUN`, `VERB`, `PUNCT`, etc.
- Builds a frequency table of tokens by POS tag
- Extracts top nouns from the passage

---

### Named Entity Recognition (`named entity recognition.ipynb`)
Using **spaCy** on a paragraph about Google's founding:
- Identifies entities: `ORG`, `PERSON`, `GPE`, `DATE`, `PERCENT`
- Visualises entity spans with `displacy`
- Demonstrates how lowercasing degrades NER accuracy (e.g. `"Larry Page"` → detected, `"larry page"` → partial miss)

---

### Sentiment Analysis (`rule-based-sentitment.ipynb`)
Compares three approaches — rule-based lexicons through to pre-trained transformers — using the same four test sentences:

1. Clearly positive — `"I had a great time at the movie it was really funny"`
2. Mixed (explicit negative word) — `"...but the parking was terrible"`
3. Mixed (contraction negation) — `"...the parking wasn't great"`
4. Neutral — `"I went to see a movie"`

**TextBlob** — single `polarity` score (−1 to +1), lexicon lookup only:

| Sentence | Polarity |
|---|---|
| Clearly positive | `0.525` |
| Mixed (terrible) | `-0.10` |
| Mixed (wasn't great) | `0.80` ⚠️ misses negation |
| Neutral | `0.0` |

**VADER** — returns `neg`, `neu`, `pos`, and `compound`; handles negation and intensifiers:

| Sentence | compound |
|---|---|
| Clearly positive | `0.807` |
| Mixed (terrible) | `-0.382` |
| Mixed (wasn't great) | `-0.439` ✓ handles negation |
| Neutral | `0.0` |

**DistilBERT** (`distilbert-base-uncased-finetuned-sst-2-english`) via Hugging Face `pipeline` — fine-tuned transformer, returns POSITIVE/NEGATIVE + confidence score:

| Sentence | Label | Score |
|---|---|---|
| Clearly positive | POSITIVE | `0.9998` |
| Mixed (terrible) | NEGATIVE | `0.9977` |
| Mixed (wasn't great) | NEGATIVE | `0.9985` ✓ handles negation |
| Neutral | POSITIVE | `0.9803` ⚠️ overconfident |

**BERTweet** (`finiteautomata/bertweet-base-sentiment-analysis`) — Twitter-trained model, returns POS/NEG/NEU:

| Sentence | Label | Score |
|---|---|---|
| Clearly positive | POS | `0.992` |
| Mixed (terrible) | NEG | `0.514` (low confidence) |
| Mixed (wasn't great) | POS | `0.635` ⚠️ misses negation |
| Neutral | NEU | `0.902` ✓ correctly neutral |

**Key takeaways:**
- VADER beats TextBlob on negation handling without needing a model
- DistilBERT (fine-tuned on SST-2 reviews) is the most accurate overall but classifies the neutral sentence as positive
- BERTweet correctly identifies the neutral sentence but struggles with contraction negation, showing that domain of fine-tuning matters

---

### Bag of Words (`bag-of-words.ipynb`)
Introduces text vectorisation — converting raw sentences into numerical feature matrices that machine learning models can consume.

Using scikit-learn's `CountVectorizer` on 6 sample sentences:
- Builds a vocabulary of all unique tokens across the corpus (71 words)
- Produces a document-term matrix where each row is a sentence and each column is a word, with cell values representing word counts
- Demonstrates that sentences sharing no words produce entirely separate columns, and sentences with common words (e.g. `"the"`) share those columns

This is a foundational step before any supervised ML on text — the output matrix feeds directly into classifiers like Naive Bayes or Logistic Regression.

---

### Topic Modelling (`lda.ipynb`)
Unsupervised discovery of latent themes across a corpus using **LDA** and **LSA**, applied to the **news articles** dataset (100 articles).

**Preprocessing pipeline:**
- Lowercase + punctuation removal → stop word removal → tokenisation → **stemming** (PorterStemmer used here for speed over lemmatisation given corpus size)
- Gensim `Dictionary` built from all tokens (8,693 unique stems)
- Corpus converted to bag-of-words format using `doc2bow`

**LDA** (Latent Dirichlet Allocation) with 2 topics:
- Both topics surface similar top words (`mr`, `said`, `trump`, `state`) — suggests the corpus may not have strongly separated themes at `k=2`

**LSA** (Latent Semantic Analysis) with 2 topics:
- Topic 0: `mr`, `said`, `trump`, `state` — general political/news
- Topic 1: negative loading on `mr`/`trump`, positive on `saudi`, `weight` — contrasting sub-theme

**Coherence-based topic selection:**
- LSA models trained for `k = 2–11`
- `CoherenceModel` (c_v) score computed for each
- Plotted to find the elbow — **k=3** selected as optimal

**Final LSA model (3 topics):**
- Topic 0: `mr`, `said`, `trump`, `state`, `would` — US politics
- Topic 1: `saudi`, `taliban`, `afghanistan` — international/conflict
- Topic 2: `weight`, `dr` — health/medicine

---

### TF-IDF (`tf-idf.ipynb`)
Extends Bag of Words by weighting words based on how distinctive they are to a document, using scikit-learn's `TfidfVectorizer` on the same 6 sentences.

**TF-IDF = Term Frequency × Inverse Document Frequency**
- Words that appear in many documents (e.g. `"the"`) get low scores — they're not informative
- Words that appear frequently in one document but rarely elsewhere get high scores — they're distinctive

Using the same corpus as `bag-of-words.ipynb`, the output matrix has the same shape (6 × 71) but float weights instead of raw counts. For example:
- `"admirable"` scores `0.294` in sentence 2 (unique to that doc)
- `"are"` scores only `0.215` in sentence 1 and `0.222` in sentence 4 (appears in two docs, so penalised)

**Key takeaway:** TF-IDF produces better features than raw counts for tasks like search and classification because common words are down-weighted automatically — no manual stop word removal needed.

---

### Sentiment Analysis Practical (`sentiment-practical.ipynb`)
Applies VADER and DistilBERT to the **Amazon book reviews** dataset (100 reviews, rated 1–5) to compare rule-based vs transformer sentiment at scale.

**Preprocessing:**
- Lowercase + punctuation removal (keeping sentiment words intact — no stop word removal)

**VADER pipeline:**
- Compute `compound` score per review
- Bin into labels using thresholds: `compound < -0.1` → negative, `-0.1–0.1` → neutral, `> 0.1` → positive
- Results visualised as a bar chart

**DistilBERT pipeline:**
- Run each cleaned review through `pipeline("sentiment-analysis")` (DistilBERT SST-2)
- Returns POSITIVE/NEGATIVE label per review
- Results visualised as a bar chart

This notebook bridges the concepts from `rule-based-sentitment.ipynb` into a real dataset workflow, showing how to apply both approaches at scale and compare their label distributions.

---

### Combined POS + NER Practical (`pos-ner-practical.ipynb`)
Applied to the **BBC News headlines** dataset (1,000 articles):

**Preprocessing pipeline:**
- Lowercase → stop word removal → punctuation removal → tokenisation → lemmatisation

**POS analysis across all headlines:**
- Top nouns: `world`, `war`, `man`, `cup`, `women`, `police`
- Top verbs: `says`, `found`, `killed`, `wins`
- Top adjectives: `new`, `russian`, `final`, `first`

**NER across all headlines:**
- Top entities: `2022` (CARDINAL), `russian` (NORP), `england` / `uk` (GPE)
- Shows NER applied to real-world news text at scale

---

## Libraries Used

| Library | Purpose |
|---|---|
| `nltk` | Tokenisation, stemming, lemmatisation, stop words, n-grams |
| `spacy` (`en_core_web_sm`) | POS tagging, NER, dependency parsing |
| `pandas` | Tabular data manipulation |
| `matplotlib` | Visualisation (bigram frequency charts) |
| `re` | Regular expression text cleaning |
| `textblob` | Rule-based sentiment analysis (polarity scoring) |
| `vaderSentiment` | Rule-based sentiment analysis with negation handling |
| `transformers` | Hugging Face pipeline for pre-trained transformer sentiment models |
| `scikit-learn` | Text vectorisation (`CountVectorizer`) and ML utilities |
| `gensim` | Topic modelling (LDA, LSA), dictionary and corpus utilities |

---

## Setup

```bash
pip install nltk spacy pandas matplotlib textblob vaderSentiment transformers torch scikit-learn gensim
python -m spacy download en_core_web_sm
```

```python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')
```

---

## Datasets

**`tripadvisor_hotel_reviews.csv`** — 109 hotel reviews with:
- `Review`: raw review text
- `Rating`: integer score (1–5)

**`bbc_news.csv`** — 1,000 BBC News articles with:
- `title`, `description`, `pubDate`, `guid`, `link`

**`book_reviews_sample.csv`** — 100 Amazon book reviews with:
- `index`, `reviewText`, `rating` (1–5)

**`news_articles.csv`** — 100 news articles with:
- `id`, `title`, `content`
