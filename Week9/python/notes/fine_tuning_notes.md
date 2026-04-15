# Fine-Tuning LLMs
Fine-tuning = adapting a pretrained model to a **specific task, domain, or behavior**.

**Why do it?**
* Inject domain knowledge (legal, medical, company data)
* Improve task accuracy (QA, classification, coding)
* Control tone/style/personality
* Build specialized agents

Think: base model = general brain → fine-tuning = specialization

Unsloth highlights that fine-tuning can:
* Learn **new knowledge**
* Customize behavior
* Optimize performance for narrow tasks 

---

## Types of Fine-Tuning

### Supervised Fine-Tuning (SFT)
* Train on **input → output pairs**
* Most common & beginner-friendly

### LoRA (Low-Rank Adaptation)
* Train only **small adapter layers**
* Freeze base model
* ~1% parameters trained

### QLoRA
* LoRA + **4-bit quantization**
* Saves ~75% memory
* Best for low-resource setups
  
### Reinforcement Learning (RL)
* Uses rewards instead of labels
* Examples: DPO, GRPO
* Used for behavior tuning (reasoning, tool use)

### Full Fine-Tuning (FFT)
* Train entire model
* Very expensive → usually unnecessary

---

## Model Selection

**Best practice:**
* Start small → scale later
* Use **instruction-tuned models** (not base models)

Examples:
* LLaMA 3.x (8B)
* Mistral / Gemma / Qwen

Insight:
* Instruct models need **less data + easier setup** 

---

## Dataset

### Format
* Typically:
```
{
  "input": "question",
  "output": "answer"
}
```

### Key Principles
* Quality > Quantity
* Structured data (QA/chat format)
* Clean + consistent formatting

### Tips
* Convert documents → QA pairs
* Use synthetic data generation (LLMs)
* Avoid dumping raw text blindly

Unsloth emphasizes:
> Well-curated QA datasets outperform raw text dumps 

---

## Training Setup

### Important Parameters

* `max_seq_length = 2048` (start small)
* `load_in_4bit = True` → QLoRA
* `dtype = float16 / bfloat16`
* `batch_size = 2`
* `gradient_accumulation_steps = 4`

### Tips

* Increase accumulation instead of batch size (memory safe)
* Match training precision with inference precision

---

## Training Signals

### Loss
* ~0.5–1.0 → good (depends on task)
* Not decreasing → problem
* Too low (~0) → overfitting

### Common Issues
* Bad dataset → worst results
* Overfitting small datasets
* Wrong formatting

---

## Inference & Deployment
After training:
* Save **LoRA adapters (~100MB)**
* Combine with base model

Deployment options:
* Ollama / llama.cpp (local)
* vLLM (production)
* Hugging Face Hub

---

## Key Insights / Best Practices

### Most important lessons
* Dataset quality > hyperparameters
* Start with QLoRA (not FFT)
* Small model + good data > large model + bad data
* Test small runs first

### Experiment strategy
1. Small dataset → test
2. Adjust formatting
3. Scale gradually

---

## Fine-Tuning vs RAG
| Feature          | Fine-Tuning               | RAG       |
| ---------------- | ------------------------- | --------- |
| Learns knowledge | ✅ Yes                     | ❌ No      |
| Updates weights  | ✅                         | ❌         |
| Dynamic info     | ❌                         | ✅         |
| Best for         | Behavior + specialization | Retrieval |

Key idea:
* Fine-tuning = **internal memory**
* RAG = **external memory**

---

## When to Use What
Use **Fine-Tuning** if:
* You need consistent behavior
* Task is repetitive (classification, formatting)
* Domain is stable

Use **RAG** if:
* Knowledge changes frequently
* You need citations
* Large document retrieval

---

## Simple Workflow (Cheat Sheet)
1. Pick model (LLaMA 8B instruct)
2. Prepare QA dataset
3. Use QLoRA (4-bit)
4. Train with small batch
5. Monitor loss
6. Save LoRA adapter
7. Deploy

---

## References

- Datasets for fine tuning
    - https://github.com/mlabonne/llm-datasets?tab=readme-ov-file
    - https://huggingface.co/datasets/NanQiangHF/alpaca_15k_instruction
    - https://huggingface.co/collections/Mahadih534/datasets-for-fine-tuning-llms