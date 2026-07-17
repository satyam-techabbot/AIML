# Machine Unlearning

Machine Learning **Machine Unlearning (MU)** is a technique that allows an AI model to *forget* specific data it was trained on — without retraining the entire model from scratch.

Think of it like this:

* A model learns from millions of records.
* Later, someone asks:

  * “Delete my personal data.”
  * “Remove poisoned/adversarial samples.”
  * “Forget copyrighted content.”
* Instead of training the whole model again, machine unlearning removes the influence of only that data.

This is becoming important because of:

* privacy laws (GDPR “right to be forgotten”),
* security,
* ethical AI,
* and copyrighted training data issues.

---

# Short Form

The common short form is:

> **MU = Machine Unlearning**

Other related abbreviations:

* **SISA** → Sharded, Isolated, Sliced, and Aggregated training
* **RTBF** → Right To Be Forgotten
* **Exact Unlearning** → mathematically equivalent forgetting
* **Approximate Unlearning** → practical but not perfectly exact forgetting

---

# Simple Intuition

Suppose a spam detection model learned from emails.

Later:

* some emails were added by mistake,
* or contained private data.

Machine unlearning removes the “memory” of those emails so the model behaves as if it never saw them.

---

# How Machine Unlearning Works

There are multiple approaches.

---

## 1. Retraining from Scratch (Baseline)

The simplest method:

1. Remove unwanted data
2. Train model again using remaining data

### Problem

Very expensive for:

* large language models,
* deep neural networks,
* billion-parameter systems.

So researchers created faster methods.

---

# 2. Exact Unlearning

Goal:
Make the final model identical to one trained without deleted data.

Mathematically:

If:

* Original dataset = (D)
* Data to remove = (D_r)

Then retrain on:

[
D' = D - D_r
]

The unlearned model should behave exactly like training on (D').

This is theoretically ideal but computationally hard.

---

# 3. Approximate Unlearning

Most practical systems use this.

Instead of perfect forgetting:

* reduce the influence of deleted data,
* make recovery impossible or very difficult.

This is faster and scalable.

---

# Main Techniques Used

## A. Gradient Reversal / Negative Training

During training:

* data changes model weights using gradients.

To unlearn:

* apply opposite gradients to reverse learning effects.

### Idea

If training did:

[
w = w - \eta \nabla L
]

Unlearning tries:

[
w = w + \eta \nabla L
]

Where:

* (w) = weights
* (\eta) = learning rate
* (L) = loss function

w = w - \eta \nabla L

This approximately “undoes” learning.

---

## B. SISA Training

One of the most famous MU methods.

### SISA =

* **S**harded
* **I**solated
* **S**liced
* **A**ggregated

### How it works

Dataset is divided into smaller shards.

Example:

* 1 million samples
* split into 100 shards

Each shard trains a separate submodel.

If data must be forgotten:

* only retrain affected shard,
* not entire model.

### Benefit

Huge speed improvement.

---

## C. Knowledge Distillation Unlearning

1. Train teacher model
2. Remove sensitive data
3. Train smaller student model using only retained knowledge

The student learns:

* useful information,
* but not deleted samples.

---

## D. Differential Privacy + Unlearning

Uses noise injection to reduce memorization.

If a model never memorizes strongly:

* forgetting becomes easier.

Often combined with:

* secure AI,
* federated learning,
* healthcare systems.

---

# Types of Data Removed

Machine unlearning can remove:

| Type                    | Example                 |
| ----------------------- | ----------------------- |
| Personal data           | names, emails           |
| Poisoned samples        | malicious training data |
| Copyrighted data        | books, images           |
| Bias-inducing data      | unfair samples          |
| Security-sensitive info | passwords, secrets      |

---

# Implementation Approaches

---

# 1. Basic PyTorch-Style Implementation

Simplified example:

```python
# Original training
for x, y in train_loader:
    optimizer.zero_grad()
    loss = model.loss(x, y)
    loss.backward()
    optimizer.step()
```

### Unlearning step

```python
# Reverse effect of unwanted samples
for x, y in forget_loader:
    optimizer.zero_grad()

    loss = model.loss(x, y)

    # reverse gradients
    (-loss).backward()

    optimizer.step()
```

This is approximate unlearning.

---

# 2. SISA-Based Architecture

Implementation pipeline:

```text
Dataset
   ↓
Shard into groups
   ↓
Train separate models
   ↓
Aggregate predictions
```

When deleting data:

```text
Find affected shard
   ↓
Retrain only that shard
   ↓
Update ensemble
```

---

# 3. Federated Learning + Unlearning

In federated systems:

* users train locally,
* server aggregates updates.

If user requests deletion:

* remove their contribution,
* recompute aggregation.

Used in:

* healthcare,
* finance,
* mobile AI.

---

# Challenges in Machine Unlearning

## 1. Verification Problem

How do we prove the model forgot?

This is still an active research problem.

---

## 2. Deep Neural Networks Memorize

Large models may:

* indirectly retain information,
* remember hidden patterns.

Perfect deletion is difficult.

---

## 3. Cost

For huge models:

* retraining is expensive,
* gradient rollback is imperfect.

---

## 4. Security

Attackers may:

* test whether forgotten data still exists,
* use membership inference attacks.

---

# Machine Unlearning in LLMs

For Large Language Models like:

* GPT-style models,
* image generators,
* recommendation systems,

unlearning is much harder because:

* data influence is distributed across billions of parameters.

Current research explores:

* parameter editing,
* low-rank adaptation removal,
* selective fine-tuning,
* activation steering.

---

# Real-World Use Cases

| Industry      | Use                       |
| ------------- | ------------------------- |
| Healthcare    | remove patient data       |
| Social media  | delete user history       |
| Finance       | remove fraudulent records |
| Cybersecurity | remove poisoned data      |
| Generative AI | copyright/data removal    |

---

# Difference Between Retraining and Unlearning

| Feature      | Retraining | Machine Unlearning |
| ------------ | ---------- | ------------------ |
| Speed        | Slow       | Faster             |
| Cost         | High       | Lower              |
| Accuracy     | Exact      | Often approximate  |
| Scalability  | Poor       | Better             |
| Used in LLMs | Difficult  | Active research    |

---

# Key Research Goal

The ideal MU system should be:

* Fast
* Verifiable
* Privacy-preserving
* Scalable
* Accurate

without retraining huge models.

---

# In One Sentence

> Machine Unlearning is the process of making an AI model forget specific training data efficiently without fully retraining the model.