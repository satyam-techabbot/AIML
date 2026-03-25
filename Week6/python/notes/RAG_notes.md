# RAG (Retrieval-Augmented Generation)

**Retrieval-Augmented Generation (RAG)** is an AI framework that:
* combines **retrieval (searching external data)**
* with **generation (LLM output)**

    ![Vector DB - RAG](images/image_vector_db.png)

Instead of relying only on trained knowledge, it:
* **retrieves relevant documents**
* then **uses them to generate answers** 

---

## Why RAG is Needed
Traditional LLM problems:
* Outdated knowledge
* Hallucinations (wrong answers)
* No access to private data

RAG solves these by:
* accessing **real-time external data**
* improving **accuracy and relevance** 

---

## Key Benefits
* **Up-to-date information** (dynamic retrieval)
* **Better accuracy** (less hallucination)
* **Domain-specific knowledge** (e.g., legal, medical)
* **Cost efficient** (no need to retrain models)
* **Personalization** (user-specific data) 

---

## Core Components of RAG

### Main Components:
1. **External Knowledge Source**
   * Documents, APIs, databases

2. **Text Chunking**
   * Break large text into smaller parts

3. **Embedding Model**
   * Converts text → vectors

4. **Vector Database**
   * Stores embeddings

5. **Query Encoder**
   * Converts query → vector

6. **Retriever**
   * Finds relevant chunks

7. **Prompt Augmentation**
   * Adds retrieved data to query

8. **LLM (Generator)**
   * Generates final answer

9. **Updater (optional)**
   * Keeps data fresh 

---

## Working of RAG (Step-by-Step)

### Pipeline:
```text
1. Collect external data
2. Convert to embeddings
3. Store in vector DB
4. User query → embedding
5. Retrieve similar documents
6. Add to prompt
7. LLM generates answer
```

Key idea:
* Retrieval happens **before generation** 

---

## Problems Solved by RAG

1. Hallucination
    * Grounds answers in real data

2. Outdated Knowledge
    * Retrieves latest information

3. Poor Context
    * Adds relevant documents

4. Lack of Expertise
    * Uses domain-specific datasets

5. High Training Cost
    * Avoids retraining LLMs 

---

## Challenges of RAG
* Complex system design
* Latency (slow due to retrieval step)
* Depends on retrieval quality
* Bias in retrieved data

---

## Applications of RAG
* Chatbots & Q&A systems
* Document search & summarization
* Virtual assistants
* Educational tools
* Enterprise knowledge systems 

---

## RAG vs Other Approaches
| Method             | Description             | When to Use               |
| ------------------ | ----------------------- | ------------------------- |
| Prompt Engineering | Modify input prompt     | Simple tasks              |
| RAG                | Retrieve + generate     | Real-time + accurate info |
| Fine-tuning        | Train model on new data | Specialized tasks         |
| Pre-training       | Train from scratch      | Large-scale models        |

RAG = **best for dynamic + factual systems** 

---

## Types of RAG
RAG systems can be categorized based on **how retrieval and generation are designed and optimized**.

---

### Naive RAG (Basic RAG)
Idea:
* Simple pipeline:

```text
Query → Retrieve → Add Context → LLM → Answer
```

Working:
1. Convert query → embedding
2. Retrieve top-K documents
3. Append to prompt
4. Generate answer

Advantages:
* Easy to implement
* Good for small projects

Limitations:
* No optimization
* May retrieve irrelevant chunks
* No ranking/refinement

Used in: **basic chat-with-docs apps**

---

### Advanced RAG
Idea:
Improves retrieval quality and response accuracy.

Enhancements:
1. Better Chunking
    * Smart splitting (semantic, recursive)

2. Query Expansion
    * Rewrite query into multiple forms

3. Re-ranking
    * Rank retrieved documents using:
        * LLM
        * cross-encoder models

4. Filtering
    * Metadata-based filtering

Advantages:
* Higher accuracy
* Better context relevance

Limitations:
* More complex
* Higher latency

---

### Modular RAG
Idea:
Break RAG into independent modules that can be customized.

Modules:
* Retriever
* Ranker
* Generator
* Query processor

Benefit:
You can swap components:
* FAISS → Pinecone
* GPT → other LLM

Advantages:
* Flexible
* Scalable

---

### Hybrid RAG
Idea:
Combine **multiple retrieval methods**

Types of Hybrid:
1. Keyword + Vector Search
    * BM25 (keyword)
        * embedding similarity

2. Multi-source Retrieval
    * PDFs + APIs + DBs

Advantages:
* Better recall & precision
* Handles diverse queries

---

### Graph RAG
Idea:
Combine **vector search + knowledge graphs**

How it works:
* Use graph relationships between data
* Retrieve based on:
  * similarity + relationships

Advantages:
* Better reasoning
* Handles complex queries

Limitation:
* Complex to build

---

### Agentic RAG
Idea:
Use **AI agents to control retrieval**

What agents do:
* Decide:
  * what to retrieve
  * how many queries
  * when to stop

Features:
* Multi-step reasoning
* Tool usage

Advantages:
* Dynamic retrieval
* More intelligent

---

### Multi-hop RAG
Idea:
Answer requires **multiple retrieval steps**

Example:
* “Who is the CEO of the company that acquired X?”

Needs:
1. Find company
2. Find CEO

Advantages:
* Handles complex questions

---

### Fusion RAG
Idea:
Combine results from **multiple queries or retrievers**

Example:
* Generate 5 query variations
* Retrieve results
* Merge + rank

Benefit:
* Improves retrieval coverage

---

### Self-RAG
Idea:
Model evaluates its own responses

Features:
* Checks:
  * relevance
  * correctness

* Can:
  * re-retrieve
  * refine answer

Advantage:
* Reduces hallucination

---

### Adaptive RAG
Idea:
System adapts based on query type

Example:
* Simple query → basic retrieval
* Complex query → multi-hop + re-ranking

Benefit:
* Efficient + intelligent

---

### Summary Table

| Type          | Key Idea               | Complexity | Use Case           |
| ------------- | ---------------------- | ---------- | ------------------ |
| Naive RAG     | Basic retrieval        | Low        | Beginners          |
| Advanced RAG  | Optimized pipeline     | Medium     | Better accuracy    |
| Modular RAG   | Replaceable components | Medium     | Flexible systems   |
| Hybrid RAG    | Keyword + vector       | Medium     | Search systems     |
| Graph RAG     | Relationships          | High       | Enterprise data    |
| Agentic RAG   | AI-controlled          | High       | Autonomous systems |
| Multi-hop RAG | Multi-step retrieval   | High       | Complex queries    |
| Fusion RAG    | Combine results        | Medium     | Better recall      |
| Self-RAG      | Self-evaluation        | High       | Reliable AI        |
| Adaptive RAG  | Dynamic approach       | High       | Smart systems      |



















