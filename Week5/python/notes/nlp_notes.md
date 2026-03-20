# Natural Language Processing

* **Natural Language Processing (NLP)** is a field of **AI + Computer Science + Linguistics**.
* It enables computers to **understand, interpret, and generate human language**.

---

## 🔹 Need for NLP
* Huge amount of **unstructured data** (text, speech, social media).
* Helps machines:
  * Extract meaning from text
  * Automate language-based tasks
* Major challenge: **ambiguity in language** (same sentence → multiple meanings).

---

## 🔹 NLP Pipeline (Steps)
#### 1. Sentence Segmentation
* Splitting text into sentences.

#### 2. Tokenization
* Breaking sentences into **words/tokens**.

#### 3. Part-of-Speech (POS) Tagging
* Assigning grammatical roles:
  * Noun, Verb, Adjective, etc.

#### 4. Lemmatization
* Converting words to **base/root form**
  (e.g., *running → run*)

#### 5. Stop Word Removal
* Removing common words (e.g., *the, is, and*)

#### 6. Dependency Parsing
* Identifying **relationships between words** (subject–verb–object structure)

---

## 🔹 NLP Techniques

### Rule-Based Approach
* Uses **manually defined rules**
* Simple but less flexible

### Machine Learning & Deep Learning
* Learns from data automatically
* Common models:
  * Decision Trees
  * SVM
  * Neural Networks (RNNs, Transformers)

### Modern Breakthrough
* **Transformers (e.g., BERT, GPT)**
* Excellent for language understanding & generation ([GeeksforGeeks][2])

---

## Key NLP Tasks

### Text Processing
* Tokenization, stemming, lemmatization, normalization

### Syntax Analysis
* POS tagging, parsing

### Semantic Analysis
* Named Entity Recognition (NER)
* Word Sense Disambiguation
* Coreference Resolution

### Information Extraction
* Extract entities & relationships

### Text Classification
* Sentiment Analysis
* Spam Detection
* Topic Modeling

### Language Generation
* Machine Translation
* Text Summarization

### Speech Processing
* Speech-to-text
* Text-to-speech

---

## How NLP Works (Workflow)
1. Data Collection (text sources)
2. Text Preprocessing
3. Text Representation:
   * Bag of Words (BoW)
   * TF-IDF
   * Word Embeddings
4. Feature Extraction
5. Model Training (ML/DL)
6. Deployment & Prediction
7. Evaluation (Accuracy, Precision, Recall, F1-score)

---

## Applications of NLP
* Speech Recognition (Siri, Alexa)
* Machine Translation (Google Translate)
* Chatbots & Virtual Assistants
* Sentiment Analysis
* Text Summarization
* Search Engines / Information Retrieval

---

## Key Challenges
* Ambiguity in language
* Context understanding
* Sarcasm, idioms, slang
* Coreference resolution

---

## Key Concepts to Remember
* NLP = **Text → Structure → Meaning → Action**
* Works using:
  * Linguistics + Algorithms + Data
* Core idea: **Make machines understand human language**

---

## NLP Processing Libraries

### 1. NLTK
* One of the **oldest and most popular NLP libraries**
* Written in Python

#### Features:
* Tokenization
* Stemming & Lemmatization
* POS Tagging
* Parsing
* Access to linguistic datasets (WordNet, corpora)

#### Use:
* Learning & academic purposes
* Basic NLP tasks

---

### 2. spaCy
* **Fast and production-ready** NLP library

#### Features:
* Tokenization
* POS tagging
* Named Entity Recognition (NER)
* Dependency parsing
* Word vectors

#### Use:
* Real-world applications
* High-performance pipelines

---

### 3. TextBlob
* Built on top of NLTK
* Very **simple and beginner-friendly**

#### Features:
* Sentiment analysis
* POS tagging
* Translation
* Noun phrase extraction

#### Use:
* Quick prototyping
* Beginners

---

### 4. Gensim
* Designed for **topic modeling and vector space modeling**

#### Features:
* Word2Vec
* Doc2Vec
* Topic modeling (LDA)

#### Use:
* Large text corpora
* Semantic similarity tasks

---

### 5. Stanford CoreNLP
* Developed by Stanford University

#### Features:
* POS tagging
* NER
* Sentiment analysis
* Coreference resolution

#### Use:
* Research-level NLP
* Deep linguistic analysis

---

### 6. Transformers
* Modern NLP library using **deep learning models**

#### Features:
* Pretrained models (BERT, GPT, RoBERTa)
* Text classification
* Translation
* Summarization
* Question answering

#### Use:
* State-of-the-art NLP tasks

---

### 7. fastText
* Developed by Facebook (Meta)

#### Features:
* Word embeddings
* Text classification
* Handles out-of-vocabulary words

#### Use:
* Efficient text classification
* Large datasets

---

## 8. Flair
* Simple and powerful NLP framework

#### Features:
* Contextual word embeddings
* NER
* POS tagging

#### Use:
* Easy deep learning NLP tasks

---

## 🔹 Quick Comparison Table

| Library      | Best For          | Level        |
| ------------ | ----------------- | ------------ |
| NLTK         | Learning & basics | Beginner     |
| spaCy        | Production apps   | Intermediate |
| TextBlob     | Simple tasks      | Beginner     |
| Gensim       | Topic modeling    | Intermediate |
| CoreNLP      | Research          | Advanced     |
| Transformers | Deep learning     | Advanced     |
| fastText     | Classification    | Intermediate |
| Flair        | Embeddings        | Intermediate |



## Phases of Natural Language Processing (NLP)
NLP works in **5 main phases**, each focusing on understanding language at a deeper level.

---

### 1. Lexical & Morphological Analysis
Deals with **words and their structure**

#### Key Points:
* **Tokenization** → Split text into words
* **POS Tagging** → Identify noun, verb, etc.
* **Stemming** → Reduce to root form (running → run)
* **Lemmatization** → Convert to base meaning word

#### Purpose:
* Understand **basic units of language**
* Simplify text for further processing 

---

### 2. Syntactic Analysis (Parsing)
Deals with **grammar and sentence structure**

#### Key Points:
* Checks **correct arrangement of words**
* Builds **parse tree (structure of sentence)**
* Identifies:
  * Subject
  * Verb
  * Object

#### Purpose:
* Ensure sentence is **grammatically correct**
* Understand **relationships between words** 

---

### 3. Semantic Analysis
Deals with **meaning of words and sentences**

#### Key Points:
* **NER (Named Entity Recognition)** → Identify names, places, etc.
* **WSD (Word Sense Disambiguation)** → Correct meaning of ambiguous words

#### Purpose:
* Ensure sentence is **meaningful and logical**
* Understand **contextual meaning** 

---

### 4. Discourse Integration
Deals with **context across multiple sentences**

#### Key Points:
* **Anaphora Resolution** → Link pronouns to correct nouns
  (e.g., “She” → “Taylor”)
* Maintains **context continuity**

#### Purpose:
* Understand **full paragraph or conversation**
* Maintain **coherence across sentences** 

---

### 5. Pragmatic Analysis
Deals with **real-world meaning & intention**

#### Key Points:
* Understand **speaker’s intent**
* Interpret:
  * Idioms
  * Sarcasm
  * Indirect requests

#### Purpose:
* Go beyond literal meaning
* Understand **actual intention in context** ([GeeksforGeeks][1])

---

## Text Preprocessing Techniques
Preprocessing is an important to clean and prepare the raw text data for analysis. Common preprocessing steps include:

### Tokenization
Splitting text into **words/sentences (tokens)**

#### Working:
* Breaks text using spaces/punctuation
* Types: word tokenization, sentence tokenization

#### Code:
```python
from nltk.tokenize import word_tokenize

text = "NLP is amazing!"
tokens = word_tokenize(text)
print(tokens)
# ['NLP', 'is', 'amazing', '!']
```

---

### Stopword Removal
Removes **common words** (no important meaning)

#### Working:
* Filters words like: *is, the, and*

#### Code:
```python
from nltk.corpus import stopwords

words = ["this", "is", "nlp"]
filtered = [w for w in words if w not in stopwords.words('english')]
print(filtered)
# ['nlp']
```

---

### Punctuation Removal
Removes symbols like **.,!?**

#### Working:
* Uses string filters or regex

#### Code:
```python
import string
text = "Hello, NLP!"
clean = text.translate(str.maketrans('', '', string.punctuation))
print(clean)
# Hello NLP
```

---

### Stemming
Reduces words to **root form (not always meaningful)**

#### Working:
* Cuts suffixes (fast but crude)

#### Code:
```python
from nltk.stem import PorterStemmer
ps = PorterStemmer()
print(ps.stem("running"))
# run
```

---

### Lemmatization
Converts word to **dictionary base form**

#### Working:
* Uses vocabulary + POS
* More accurate than stemming

#### Code:
```python
from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()
print(lem.lemmatize("running", pos='v'))
# run
```

---

### Text Normalization
Standardizes text format

#### Working:
* Lowercasing
* Removing numbers, extra spaces
* Expanding contractions

#### Code:
```python
text = "NLP IS FUN 123"
normalized = text.lower()
print(normalized)
# nlp is fun 123
```

---

### Parts of Speech (POS) Tagging
Assigns **grammatical roles** (noun, verb, etc.)

#### Working:
* Uses trained models to label tokens

#### Code:
```python
from nltk import pos_tag, word_tokenize
text = "NLP is fun"
print(pos_tag(word_tokenize(text)))
# [('NLP', 'NNP'), ('is', 'VBZ'), ('fun', 'JJ')]
```

---

### Parsing
Analyzes **sentence structure (syntax)**

#### Working:
* Builds tree showing relationships between words

#### Code (simple):
```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("NLP is fun")

for token in doc:
    print(token.text, token.dep_)
```

---

## Text Representation Techniques
It converts textual data into numerical vectors.

### One-Hot Encoding
Represents each word as a **binary vector**

#### Working:
* Create vocabulary of all unique words
* Each word → vector of size *V* (vocab size)
* Only one position = 1, rest = 0

Example:
Vocabulary = [I, love, NLP]
* I → [1,0,0]
* love → [0,1,0]

#### Pros:
* Simple

#### Cons:
* High dimensional, no meaning captured

#### Code:
```python
from sklearn.preprocessing import OneHotEncoder
import numpy as np

words = np.array([["I"], ["love"], ["NLP"]])
encoder = OneHotEncoder(sparse=False)
print(encoder.fit_transform(words))
```

---

### Bag of Words (BoW)
Represents text based on **word frequency**

#### Working:
* Create vocabulary
* Count frequency of each word in document

Example:
"I love NLP NLP" → [I=1, love=1, NLP=2]

#### Pros:
* Easy, useful baseline

#### Cons:
* Ignores order & context

#### Code:
```python
from sklearn.feature_extraction.text import CountVectorizer

docs = ["I love NLP", "NLP is fun"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(docs)

print(vectorizer.get_feature_names_out())
print(X.toarray())
```

---

### TF-IDF (Term Frequency – Inverse Document Frequency)
Measures **importance of a word**

#### Working:
* **TF** → frequency in document
* **IDF** → rarity across documents
* Formula:
  TF-IDF = TF × log(N / DF)

    Rare words → higher weight
    Common words → lower weight

#### Pros:
* Better than BoW

#### Cons:
* Still ignores context

#### Code:
```python
from sklearn.feature_extraction.text import TfidfVectorizer

docs = ["I love NLP", "NLP is fun"]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

print(X.toarray())
```

---

### N-Gram Language Modeling
Considers **sequence of words**

#### Working:
* N = number of words in sequence
  * Unigram → 1 word
  * Bigram → 2 words
  * Trigram → 3 words

Example:
"I love NLP"
* Bigrams → ["I love", "love NLP"]

#### Pros:
* Captures context & word order

#### Cons:
* Large feature size

#### Code:
```python
from sklearn.feature_extraction.text import CountVectorizer

docs = ["I love NLP"]
vectorizer = CountVectorizer(ngram_range=(2,2))  # bigrams
X = vectorizer.fit_transform(docs)

print(vectorizer.get_feature_names_out())
```

---

## 