# Vector Databases for RAG
**Retrieval-Augmented Generation (RAG)** is an AI architecture that improves LLM outputs by retrieving external knowledge and injecting it into prompts.

![Vector DB - RAG](./images/image_vector_db.png)

### Key Idea:
* LLM alone → relies on training data (can be outdated/inaccurate)
* RAG → **retrieves relevant documents → feeds into LLM → generates answer**

### Why RAG?
* Adds **real-time / private data**
* Reduces hallucination
* Improves factual accuracy

---

## What is a Vector Database?
A **vector database** stores data as **embeddings (vectors)** and enables **similarity search** rather than exact matching.

### Key Concept:
* Text → converted into **high-dimensional vectors**
* Query → also converted into vector
* Database → finds **closest vectors (semantic similarity)**

Instead of keyword match:
* “fast car” → returns Ferrari even if word “fast” not present

### Core Function:

* Efficient **semantic retrieval at scale** 

---

## Role of Vector DB in RAG
Vector DB is the **core retrieval engine** in RAG.

### Pipeline:
```
User Query → Embedding → Vector DB Search → Top-K Results → LLM → Answer
```

### How it works:
1. Documents are split into chunks
2. Each chunk → converted to embedding
3. Stored in vector DB
4. Query → embedding → similarity search
5. Top relevant chunks → passed to LLM

Uses **K-Nearest Neighbors (KNN)** for retrieval 

---

## Key Components of Vector DB for RAG

### Embeddings
* Numerical representation of meaning
* Generated using models (OpenAI, BERT, etc.)

### Indexing
* Enables fast similarity search
* Common techniques:
  * HNSW (Hierarchical Navigable Small World)
  * IVF (Inverted File Index)
  * PQ (Product Quantization)

### Similarity Metrics
* Cosine similarity
* Euclidean distance
* Dot product

### Metadata Filtering
* Combine semantic + structured filters
* Example:
  * “finance docs from 2024”

---

## Types of Vector Databases

### 1. In-memory (e.g., Chroma)
* Fast retrieval
* Not persistent
* Suitable for experiments

### 2. Distributed DBs (e.g., Milvus)
* Scalable
* Handles large datasets

### 3. Hybrid systems (e.g., Elasticsearch)
* Combine:
  * Keyword search + vector search

---

## Why Vector DB instead of Traditional DB?
| Feature     | Traditional DB | Vector DB            |
| ----------- | -------------- | -------------------- |
| Search type | Exact match    | Semantic similarity  |
| Data type   | Structured     | Unstructured         |
| Query style | SQL            | Embedding similarity |
| Use case    | Transactions   | AI retrieval         |

Vector DB enables:
* Context-aware retrieval
* Better alignment with natural language queries

---

## Advantages in RAG
### 1. Semantic Search
* Finds meaning, not keywords

### 2. Better LLM Responses
* Provides relevant context → improves accuracy

### 3. Scalability
* Handles millions of embeddings

### 4. Real-time Knowledge
* Easily update knowledge base

### 5. Domain Adaptation
* Use private/company data

RAG + vector DB = **dynamic knowledge injection**

---

## Limitations of Vector Databases in RAG

### 1. Lack of Precision
* Similar embeddings ≠ exact meaning
* Can mix related but incorrect info

### 2. Weak Relationship Understanding
* Doesn’t capture structured relationships well

### 3. Retrieval Errors
* May return:
  * partially relevant chunks
  * contradictory data

### 4. Update Challenges
* Re-embedding required for updates

### 5. Cost & Complexity
* Scaling large vector DBs is expensive 

---

## Challenges in Production RAG

### 1. Chunking Strategy
* Too small → lose context
* Too large → irrelevant info

### 2. Embedding Quality
* Poor embeddings → poor retrieval

### 3. Latency
* Vector search + LLM = slower pipeline

### 4. Evaluation
* Hard to measure retrieval quality

### 5. Trade-off
* Speed vs accuracy (approximate search)

---

## Advanced Improvements

### Hybrid Search
* Combine:
  * Vector similarity + keyword search

### Re-ranking
* Use LLM to re-rank retrieved results

### Graph-based RAG (Writer insight)
* Uses relationships between data
* Better for:
  * enterprise knowledge
  * complex queries

### Metadata + Filtering
* Improves precision

---

## Vector DB vs Knowledge Graph
| Aspect   | Vector DB             | Knowledge Graph      |
| -------- | --------------------- | -------------------- |
| Focus    | Similarity            | Relationships        |
| Strength | Semantic search       | Structured reasoning |
| Weakness | Poor relational logic | Complex setup        |

Trend: **Hybrid (Vector + Graph RAG)**

---

## Popular Vector Databases (Examples)
* Pinecone
* Milvus
* Weaviate
* Chroma
* Elasticsearch (hybrid)

---

## Real-world Use Cases

### Enterprise Search
* Internal docs retrieval

### Chatbots
* Customer support

### Analytics
* Financial insights

### Recommendation systems
* Product similarity

---

## End-to-End RAG Architecture
```
Data Sources → Chunking → Embeddings → Vector DB
                                     ↓
User Query → Embedding → Retrieval → Context
                                     ↓
                                LLM → Response
```

---

## Key Takeaways
* Vector DB = **semantic retrieval engine**
* Core of RAG pipeline
* Uses:
  * embeddings
  * similarity search (KNN)
* Strength:
  * meaning-based retrieval
* Weakness:
  * lacks reasoning & relationships
* Future:
  * hybrid (vector + graph + keyword)

--- 

## Similarity Search

### What is Similarity Search?
Similarity search retrieves items that are **most similar (semantically)** to a query instead of exact matches.

#### Example:
Query: *“best smartphone for photos”*
→ Returns documents about **camera quality phones**, even if wording differs.

Core idea:
Convert data into **vectors → compare distances**

---

### Why it Matters in RAG
In RAG:
* Query → embedding
* Documents → embeddings
* Similarity search → finds relevant context

Without it → LLM has no external knowledge access.

---

### Mathematical Intuition

#### Vector Representation
Each text → vector in **high-dimensional space**

Example:
```
"cat" → [0.2, -0.5, 0.8, ...]
"dog" → [0.25, -0.45, 0.75, ...]
```

Similar meaning → vectors are **close**

---

### Distance Metrics

#### 1. Cosine Similarity (Most Common)
Measures angle between vectors:
```math
\text{cosine similarity} = \frac{A \cdot B}{||A|| \cdot ||B||}
```

* Range: [-1, 1]
* 1 = identical direction

Used in NLP because magnitude doesn’t matter

---

#### 2. Euclidean Distance
```math
d(A,B) = \sqrt{\sum (A_i - B_i)^2}
```

* Measures straight-line distance

Smaller distance = more similar

---

#### 3. Dot Product
```math
A \cdot B = \sum A_i B_i
```

* Faster computation
* Often used in optimized systems

---

### Geometric Intuition
Think of:
* Each document = point in space
* Query = another point

Similarity search = **find nearest neighbors**

---

### K-Nearest Neighbors (KNN)
Find top **K closest vectors**

Example:
```
Query → find top 5 nearest docs
```

---

### Types of Similarity Search

#### 1. Exact Search
* Computes distance with **all vectors**
* Accurate but **slow (O(n))**

#### 2. Approximate Nearest Neighbor (ANN)
* Faster but slightly less accurate
* Used in production systems

FAISS uses ANN heavily

---

## FAISS
**FAISS (Facebook AI Similarity Search)** is a library by
Meta AI

Used for:
* Fast similarity search
* Large-scale vector storage

### Why FAISS?
* Handles **millions/billions of vectors**
* Optimized in **C++ + GPU**
* Supports ANN indexing

---

### How FAISS Works (Step-by-Step)

#### Step 1: Convert Data → Vectors
Use embedding model:
```
docs → embeddings → vectors
```

#### Step 2: Build Index
FAISS creates a **data structure (index)** for fast search.

Types:
* Flat index (exact search)
* IVF (cluster-based)
* HNSW (graph-based)

#### Step 3: Store Vectors
Vectors stored inside index

#### Step 4: Query Search
```
query → embedding → search index → nearest vectors
```

#### Step 5: Return Top-K
Returns:
* nearest vectors
* similarity scores

---

### FAISS Index Types (Important)

#### 1. IndexFlatL2 (Brute Force)
* Exact search
* Uses Euclidean distance

Pros:
* Accurate

Cons:
* Slow for large data

#### 2. IVF (Inverted File Index)
Idea:
* Cluster vectors into groups
* Search only relevant clusters

Like:
* Find city → then house

##### Steps:
1. K-means clustering
2. Assign vectors to clusters
3. Search only closest clusters

#### 3. HNSW (Graph-Based)
Idea:
* Build graph of neighbors

Search:
* Traverse graph → find nearest nodes

* Very fast
* High accuracy

#### 4. PQ (Product Quantization)
Product Quantization (PQ) is a lossy compression technique for high-dimensional vectors that drastically reduces memory footprint (up to 95%+) and speeds up approximate nearest neighbor (ANN) search.

Idea:
* Compress vectors

Reduces:
* Memory usage
* Computation cost

---

### FAISS Architecture (Conceptual)
```
Vectors → Index → Clusters/Graph → Search → Top-K Results
```

---

### Hands-on Tutorial (Python)

#### Step 1: Install FAISS
```bash
pip install faiss-cpu
```

#### Step 2: Basic Example
```python
import faiss
import numpy as np

# Create random vectors (5 vectors, 3 dimensions)
data = np.array([
    [1.0, 2.0, 3.0],
    [2.0, 3.0, 4.0],
    [10.0, 10.0, 10.0],
    [1.1, 2.1, 3.1],
    [8.0, 9.0, 10.0]
]).astype('float32')

# Build index
index = faiss.IndexFlatL2(3)

# Add vectors
index.add(data)

# Query vector
query = np.array([[1.0, 2.0, 3.0]]).astype('float32')

# Search top 2 nearest neighbors
distances, indices = index.search(query, k=2)

print(indices)
print(distances)
```

Output Interpretation
```
indices → nearest vectors
distances → similarity score
```

#### Step 3: Using IVF Index
```python
nlist = 2  # number of clusters
quantizer = faiss.IndexFlatL2(3)

index = faiss.IndexIVFFlat(quantizer, 3, nlist)

index.train(data)
index.add(data)

index.nprobe = 1  # clusters to search

distances, indices = index.search(query, k=2)
```

---

### FAISS in RAG Pipeline

Workflow
```
Documents → Embeddings → FAISS Index
User Query → Embedding → Search → Top-K Docs → LLM
```

#### Example Stack:
* Embeddings: OpenAI / Sentence Transformers
* Vector DB: FAISS
* Framework: LangChain / LlamaIndex

---

### Performance Considerations

Key Trade-offs
| Factor   | Impact                |
| -------- | --------------------- |
| Accuracy | Exact vs ANN          |
| Speed    | Index type            |
| Memory   | PQ compression        |
| Latency  | nprobe / cluster size |

#### Optimization Tips
* Normalize vectors for cosine similarity
* Tune:
  * `nlist` (clusters)
  * `nprobe` (search scope)
* Use GPU for large datasets

---

### Limitations
* Approximation Errors
    * ANN may miss best match

* Memory Usage
    * Large embeddings = high RAM

* No Native Metadata Filtering
    * Needs external handling

---

### FAISS vs Vector Databases
| Feature   | FAISS     | Vector DB   |
| --------- | --------- | ----------- |
| Type      | Library   | Full system |
| Storage   | In-memory | Persistent  |
| Scaling   | Manual    | Built-in    |
| Filtering | Limited   | Advanced    |

FAISS = **engine**

Vector DB = **complete system**

---

## Chroma DB
Chroma DB is an open-source vector database designed for:
* storing embeddings
* performing similarity search
* building RAG applications easily

Think of it as:
**“FAISS + storage + metadata + developer-friendly API”**

---

### Why Chroma DB?
Compared to raw libraries like FAISS:
Feature            | FAISS       | Chroma DB         
------------------ | ----------- | ----------------- 
Storage            | In-memory   | Persistent        
Metadata filtering | Limited     | Yes               
API                | Low-level   | High-level        
Ease of use        | Harder      | Beginner-friendly 

Chroma is built **specifically for LLM apps**

---

### Role in RAG

#### RAG Pipeline with Chroma
```
Documents → Chunking → Embeddings → Chroma DB
User Query → Embedding → Similarity Search → Context → LLM
```

#### What Chroma Handles
* Stores embeddings
* Performs similarity search
* Filters with metadata
* Returns relevant documents

---

### Core Concepts

#### 1. Collection
* Equivalent to a **table**
* Stores:
  * embeddings
  * documents
  * metadata

Example:
```
collection = chroma_client.create_collection("docs")
```

#### 2. Embeddings
* Vectors representing text
* Generated using:
  * OpenAI
  * Sentence Transformers

#### 3. Documents
* Original text chunks

#### 4. Metadata
Extra info:
```
{
  "source": "pdf",
  "year": 2024
}
```
Used for filtering

#### 5. Query
Search for similar vectors

---

### How Chroma Works Internally

#### Step-by-step
1. Input text
2. Convert → embedding
3. Store in collection
4. Build index (ANN)
5. Query:
   * convert query → embedding
   * find nearest neighbors
6. Return:
   * documents
   * distances
   * metadata

#### Under the Hood
* Uses **Approximate Nearest Neighbor (ANN)**
* Often backed by:
  * HNSW (Hierarchical Navigable Small Worlds) graphs
* Stores data locally (SQLite / DuckDB)

---

### Key Features
1. Persistent Storage
    * Data saved on disk

2. Metadata Filtering
    ```
    where={"year": 2024}
    ```

3. Simple API
    * Python & JS support

4. Built-in Embedding Support
    * Can auto-generate embeddings

5. Lightweight
    * No heavy infra needed

---

### Hands-on Tutorial (Python)

Step 1: Install
```bash
pip install chromadb
```

Step 2: Basic Setup
```python
import chromadb
client = chromadb.Client()
collection = client.create_collection(name="my_docs")
```

Step 3: Add Data
```python
collection.add(
    documents=[
        "AI is transforming the world",
        "Machine learning is a subset of AI",
        "Deep learning uses neural networks"
    ],
    ids=["1", "2", "3"]
)
```

Step 4: Query Data
```python
results = collection.query(
    query_texts=["What is AI?"],
    n_results=2
)
print(results)
```

##### Output
```
{
  'documents': [...],
  'ids': [...],
  'distances': [...]
}
```

---

### Using Custom Embeddings

Example with Sentence Transformers
```python
from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.Client()
collection = client.create_collection(name="custom")

docs = ["AI is powerful", "Dogs are animals"]

embeddings = model.encode(docs).tolist()

collection.add(
    embeddings=embeddings,
    documents=docs,
    ids=["1", "2"]
)
```

---

### Persistence (Important)

#### Save to Disk
```python
client = chromadb.PersistentClient(path="./chroma_db")
```

Data remains after restart

---

### Metadata Filtering
```python
collection.add(
    documents=["AI in healthcare", "AI in finance"],
    metadatas=[{"domain": "health"}, {"domain": "finance"}],
    ids=["1", "2"]
)

results = collection.query(
    query_texts=["AI"],
    where={"domain": "health"}
)
```

---

### Chroma in RAG (Full Example)
```python
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

db = Chroma.from_texts(
    texts=["AI is amazing", "ML is part of AI"],
    embedding=OpenAIEmbeddings()
)
docs = db.similarity_search("What is AI?", k=2)
```

---

### Advanced Features

1. Upserts
    * Update or insert data

2. Delete
    ```python
    collection.delete(ids=["1"])
    ```

3. Count
    ```python id="0tq0f5"
    collection.count()
    ```

---

### Performance Tips
1. Chunking Strategy
    * 200–500 tokens per chunk

2. Use Good Embeddings
    * Quality > quantity

3. Limit Results (k)
    * Avoid too many irrelevant docs

4. Persist DB
    * Avoid recomputation

---

### Limitations

* Not Distributed
    * Not ideal for massive scale

* Memory Constraints
    * Large datasets need tuning

* Less Powerful than Enterprise DBs

* Compared to:
  * Pinecone
  * Weaviate

---

### Chroma vs FAISS
| Feature     | Chroma   | FAISS              |
| ----------- | -------- | ------------------ |
| Type        | DB       | Library            |
| Persistence | ✅        | ❌                  |
| Metadata    | ✅        | ❌                  |
| Ease        | Easy     | Complex            |
| Use case    | RAG apps | Core search engine |

---

### When to Use Chroma
Best For:
* Prototyping RAG apps
* Local development
* Small–medium datasets

Avoid When:
* Need distributed scaling
* Billion-scale vectors

---

## Pinecone
**Pinecone** is a **managed cloud vector database** designed for:
* storing embeddings
* performing fast similarity search
* scaling to millions/billions of vectors

Think of it as:
> “Production-ready vector database (like Chroma, but scalable and managed)”

---

### Why Pinecone?

#### Key Advantages
* Fully Managed
  * No infrastructure setup
  * No index tuning required

* Scalable
  * Handles **billions of vectors**

* Fast Retrieval
  * Optimized ANN search

* High Availability
  * Cloud-native (low latency APIs)

### Compared to Others
| Feature          | FAISS  | Chroma  | Pinecone      |
| ---------------- | ------ | ------- | ------------- |
| Setup            | Manual | Local   | Managed cloud |
| Scaling          | Hard   | Limited | Excellent     |
| Persistence      | Manual | Local   | Built-in      |
| Production ready | ❌      | ⚠️      | ✅             |

---

### Role in RAG

#### RAG Pipeline with Pinecone
```
Documents → Chunking → Embeddings → Pinecone Index
User Query → Embedding → Search → Top-K Results → LLM → Answer
```

#### What Pinecone Does
* Stores embeddings
* Performs similarity search
* Filters using metadata
* Returns relevant documents

---

### Core Concepts

1. Index
    * Equivalent to a **database**
    * Stores vectors

    Example:
    ```id="pine1"
    index = pc.Index("my-index")
    ```

2. Vectors
    
    Each vector:
    ```
    {
      "id": "doc1",
      "values": [0.12, 0.98, ...],
      "metadata": {"topic": "AI"}
    }
    ```

3. Namespace
    * Logical partition inside index
    * Useful for:
      * multi-user apps
      * environments

4. Metadata

    Used for filtering:
    ```
    {"category": "finance"}
    ```

5. Query
    * Search similar vectors

---

### How Pinecone Works Internally

#### Workflow
1. Text → embedding
2. Store vectors in index
3. Build ANN index (internally)
4. Query:
   * embedding
   * similarity search
5. Return top-K matches

#### Under the Hood
* Uses **Approximate Nearest Neighbor (ANN)**
* Optimized indexing (proprietary + HNSW-like)
* Distributed infrastructure

---

### Similarity Metrics
You can configure:
* Cosine similarity (most common)
* Dot product
* Euclidean distance

---

### Hands-on Tutorial (Python)
Step 1: Install
```bash
pip install pinecone-client
```

Step 2: Initialize
```python
from pinecone import Pinecone
pc = Pinecone(api_key="YOUR_API_KEY")
```

Step 3: Create Index
```python
pc.create_index(
    name="my-index",
    dimension=1536,
    metric="cosine"
)
```

Step 4: Connect to Index
```python
index = pc.Index("my-index")
```

Step 5: Insert Vectors
```python
index.upsert([
    {
        "id": "1",
        "values": [0.1, 0.2, 0.3],
        "metadata": {"topic": "AI"}
    },
    {
        "id": "2",
        "values": [0.2, 0.3, 0.4],
        "metadata": {"topic": "ML"}
    }
])
```

Step 6: Query
```python 
query_vector = [0.1, 0.2, 0.3]

results = index.query(
    vector=query_vector,
    top_k=2,
    include_metadata=True
)

print(results)
```

#### Output
```
{
  "matches": [
    {"id": "1", "score": 0.99, "metadata": {...}},
    ...
  ]
}
```

---

### Using with Embeddings (Real RAG Setup)

Example with OpenAI Embeddings
```python
from openai import OpenAI
from pinecone import Pinecone

client = OpenAI()
pc = Pinecone(api_key="YOUR_API_KEY")

index = pc.Index("my-index")

# Create embedding
embedding = client.embeddings.create(
    input="What is AI?",
    model="text-embedding-3-small"
)

query_vector = embedding.data[0].embedding

results = index.query(vector=query_vector, top_k=3)
```

---

### Metadata Filtering
```python
results = index.query(
    vector=query_vector,
    top_k=5,
    filter={"topic": {"$eq": "AI"}}
)
```

---

#### Why Important?
* Improves precision
* Enables structured queries

---

### Namespaces (Multi-Tenant Design)
```python
index.upsert(vectors=data, namespace="user1")

index.query(vector=query_vector, namespace="user1")
```

Useful for:
* SaaS apps
* User isolation

---

### Pinecone in Full RAG System
Architecture
```
Docs → Chunk → Embeddings → Pinecone
Query → Embedding → Search → Context → LLM → Answer
```

---

#### With LangChain
```python
from langchain.vectorstores import Pinecone

vectorstore = Pinecone.from_texts(
    texts,
    embedding,
    index_name="my-index"
)

docs = vectorstore.similarity_search("Explain AI", k=3)
```

---

### Performance Optimization
Key Parameters

1. Top-K
    * Higher = more context
    * Lower = faster

2. Embedding Quality
    * Better embeddings → better retrieval

3. Metadata Filtering
    * Reduces noise

---

#### Best Practices
* Normalize vectors for cosine similarity
* Use proper chunk size (200–500 tokens)
* Avoid too many results (k ≤ 10)

---

### Limitations
* Paid Service
  * Not fully free

* Vendor Lock-in
  * Cloud dependency

* Black-box Indexing
  * Less control vs FAISS

---

### When to Use Pinecone
Best For:
* Production RAG apps
* Large-scale systems
* SaaS AI products

Avoid When:
* Small local project
* Budget constraints

---

### Pinecone vs Chroma vs FAISS
| Feature | Pinecone  | Chroma   | FAISS   |
| ------- | --------- | -------- | ------- |
| Type    | Cloud DB  | Local DB | Library |
| Scaling | Excellent | Limited  | Manual  |
| Setup   | Easy      | Easy     | Hard    |
| Cost    | Paid      | Free     | Free    |

