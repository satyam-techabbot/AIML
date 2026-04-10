# Evaluation Metrics

Evaluating a **RAG (Retrieval-Augmented Generation)** system is more complex than evaluating a standard LLM because you have to measure two distinct moving parts: how well the system **finds** information and how well it **uses** that information.

The industry standard for this is the **RAG Triad**, which focuses on Faithfulness, Answer Relevance, and Context Relevance.

---

## 1. The Retrieval Metrics (The "Finding" Part)
These metrics determine if your vector database is actually surfacing the right documents.

* **Context Precision:** Does the system rank the ground-truth relevant documents at the top of the results?
* **Context Recall:** Did the system actually find all the necessary information needed to answer the question?
* **MRR (Mean Reciprocal Rank):** A measure of where the first relevant document appears in the list.
    * Formula: 
```math
MRR = \frac{1}{|Q|} \sum_{i=1}^{|Q|} \frac{1}{rank_i}
```
* **Hit Rate:** The percentage of queries for which the correct chunk was retrieved in the top $k$ results.

---

## 2. The Generation Metrics (The "Writing" Part)
These ensure the LLM isn't hallucinating and is actually answering the user's prompt.

* **Faithfulness (Groundedness):** Is the answer derived *only* from the retrieved context? If the LLM uses its own pre-trained knowledge to answer something not in the text, it fails this metric.
* **Answer Relevance:** Does the response actually address the user's query? (e.g., if the user asks for a price and the LLM describes the product features instead, relevance is low).
* **Answer Semantic Similarity:** Compares the generated answer to a "gold standard" ground-truth answer using embeddings to see how close they are in meaning.

---

## 3. Evaluation Frameworks
Manually checking thousands of RAG outputs is impossible. Most developers use **LLM-as-a-Judge** frameworks to automate this process:

| Framework | Best For |
| :--- | :--- |
| **Ragas** | The gold standard for automated RAG Triad evaluation. |
| **TruLens** | Great for visualizing the "Triad" and tracking experiments. |
| **DeepEval** | Unit testing for LLMs; integrates well with CI/CD pipelines. |
| **Arize Phoenix** | Excellent for tracing and observability in production. |

---

## 4. Why "Traditional" Metrics Fail
You might be tempted to use **BLEU** or **ROUGE** (standard for translation/summarization). **Don't.**
These rely on exact word matching. In RAG, an LLM can provide a 100% accurate answer using completely different synonyms than the reference text, causing these old metrics to give a "failing" score to a perfect answer.

> **Pro Tip:** If your RAG system is hallucinating, the issue is usually **Context Precision**. If the system says "I don't know," the issue is usually **Context Recall**.

---







