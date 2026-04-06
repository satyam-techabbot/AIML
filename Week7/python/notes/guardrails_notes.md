# Guardrails in GenAI

Guardrails are **control + validation layers** around LLM systems that regulate:
* **Inputs (prompts)**
* **Model behavior**
* **Outputs (responses)**

They act as **“safety nets” between user and model** to ensure:
* safety
* reliability
* consistency 

Analogy:
> Like highway barriers preventing a car from going off-road 

---

## Why Guardrails Are Critical
LLMs are:
* probabilistic (not deterministic)
* prone to:
  * hallucinations
  * data leakage
  * prompt injection

So raw “prompt → output” is **not production-safe** 

---

## Key Risks Guardrails Solve

### 1. Hallucinations
* Confident but false outputs
  → Guardrails verify against trusted sources

### 2. Prompt Injection / Jailbreaks
* e.g. “Ignore all instructions…”
  → Detect and block malicious prompts

### 3. Data Leakage (PII)
* Prevent exposure of sensitive info

### 4. Toxic / Unsafe Content
* Filter harmful or biased outputs

### 5. Compliance Risks
* Ensure outputs follow legal/regulatory constraints 

---

## Where Guardrails Sit in Pipeline
Guardrails operate at **multiple stages**:

### 1. Input Guardrails
* Detect:
  * prompt injection
  * unsafe queries
  * off-topic requests
* Normalize prompts

### 2. Orchestration / Tool Guardrails
* Control:
  * which tools can be used
  * API access
  * function calling
* Sandbox execution

### 3. Output Guardrails
* Enforce:
  * structured output (JSON, schema)
  * factual correctness
  * safety filters

This is exactly where your **quiz JSON problem lives**

---

## Types of Guardrails

### 1. Input Guardrails
* Prompt filtering
* Injection detection

### 2. Output Guardrails
* Toxicity filtering
* Format enforcement
* Fact-checking

### 3. Alignment Guardrails
* Keep response aligned with:
  * user intent
  * business rules
  * brand tone 

### 4. Validation Guardrails
* Ensure:
  * required fields exist
  * schema correctness

Example:
```json
must contain: ["question", "options", "correct"]
```

### 5. Hallucination Guardrails
* Cross-check with:
  * RAG sources
  * knowledge base

---

## How Guardrails Work (Architecture)
Typical components:

### Checker
* Detect issues:
  * unsafe content
  * wrong format
  * hallucinations

### Corrector
* Fix output:
  * rewrite
  * sanitize
  * reformat

### Policy Layer
* Defines:
  * rules
  * constraints
  * compliance targets

### Monitoring Layer
* Logs + audits outputs
Guardrails are often **deterministic systems wrapped around probabilistic LLMs** 

---

## Guardrails Techniques

### Rule-based
* Regex
* keyword filtering

### Schema Enforcement
* JSON / Pydantic validation

### LLM-as-Judge
* Secondary model validates output

### RAG-based Validation
* Check answers against retrieved context

### Red Teaming
AI red teaming is the process of intentionally probing, testing, and attacking AI systems to identify security vulnerabilities, safety flaws, and potential for misuse.
* Test with adversarial prompts

---

## Guardrails vs Prompt Engineering
| Prompt Engineering | Guardrails                 |
| ------------------ | -------------------------- |
| Suggests behavior  | Enforces behavior          |
| Soft control       | Hard constraints           |
| Can fail easily    | Designed to catch failures |

Important insight:
> Guardrails = **contracts**, not suggestions

---

## Key Insight
> Guardrails standardize LLM outputs

Example:
* Always return JSON
* Always follow schema

This removes:
* brittle parsing
* inconsistent outputs 

---

## Real-World Implementation Layers
Think in **3-layer architecture**:

### Layer 1: Input Control
* sanitize prompts

### Layer 2: Model Control
* system prompts
* tool restrictions

### Layer 3: Output Control
* validation + filtering

---

### Advanced Insight
> “Guardrails are more important than the model in production.”

Why?
* Models are becoming commoditized
* Control & safety = real challenge

---

## Limitations of Guardrails
* Not 100% foolproof
* Can be bypassed (prompt injection)
* Trade-off:
  * safety vs usefulness

Need **layered defense** (defense-in-depth)

---

## One-Line Definition
> “Guardrails are deterministic validation and control layers that constrain LLM inputs, outputs, and behavior to ensure safety, reliability, and consistency in production systems.”

