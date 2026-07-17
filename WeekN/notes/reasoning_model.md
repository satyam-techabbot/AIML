# **Reasoning Model**

> Generative models usually predict the best possible word after a specific word but when the prediction fails then the LLM can't rechange the generated data and gets stuck by making the wrong decision.

> While Reasoning model, before generating a single word for the user, they spin up an internal monologue to plan, verify, error-correct, and break down complex logic.

---

## **How They Work: The Technical Architecture**

1. Hidden Chain of thought(CoT):

    > When you submit a complex prompt, the model begins generating tokens into a "hidden workspace." 

    > It explicitly talks to itself:"Okay, I need to solve this physics problem. First, let's identify the variables. $v_0 = 0$. Wait, if the surface has friction, I need to calculate the normal force first. Let's do that. $F_n = mg \cos(\theta)$..."
    
    > This internal monologue allows the model to compute complex intermediate steps that would otherwise overload the attention mechanism of a standard token prediction step.

2. Search and Planning (MCTS):
    > Many cutting-edge reasoning systems integrate Monte Carlo Tree Search (MCTS) or similar tree-search algorithms during training or inference.

    > Instead of following a single path of thought, the model can branch out.

    > It explores Path A, realizes it leads to a logical dead-end, backtracks, and tries Path B.

3. Self-Correction and Verification:
    > Standard LLMs suffer from "hallucination compounding"—once they make a mistake, they double down. Reasoning models are trained to act as their own critics. They routinely pause and check their work:

    > "Does this match the constraints given in the prompt?"

    > "Let me re-verify the math in step 3."
    If the verification fails, the model writes a correction to itself before finalizing the response you see.

---

## **How They Are Trained: The RL Revolution**
> You can't easily create a reasoning model just by collecting human text, because humans rarely write out every single micro-thought when solving a problem. Instead, AI labs use **Reinforcement Learning (RL)** with a heavy emphasis on outcome and process rewards.

```
       [ Prompt ]
           │
           ▼
┌───────────────────────┐
│ Internal Monologue    │ ◄─── Driven by RL 
│ (Planning & Backtrack)│      (Rewards for right answers,
└───────────────────────┘      penalties for logical flaws)
           │
           ▼
┌───────────────────────┐
│   Final User Output   │
└───────────────────────┘

```

* **Outcome-based Reward (ORM: Outcome Reward Model):** 

    > The model is given a complex math or coding problem. If it gets the final answer right, it gets a positive reward. 
    
    > If it's wrong, a negative reward. Through millions of iterations, the model naturally *learns* that generating an organized, step-by-step internal monologue yields the correct answer more often.

* **Process-based Reward (PRM: Process Reward Model):** 

    > Humans or evaluator models grade the *individual steps* of the internal reasoning. The model is rewarded for precise logic, even if the final calculation has a minor typo. This prevents the model from getting the right answer via flawed logic.

---

## The Trade-offs

| Feature | Standard LLMs (System 1) | Reasoning Models (System 2) |
| --- | --- | --- |
| **Speed** | Near-instantaneous (low latency). | Slow; can take 5 to 60+ seconds to "think." |
| **Cost** | Significantly cheaper (fewer total tokens). | Expensive (you pay for the hidden thinking tokens). |
| **Best Used For** | Writing, summarization, basic Q&A, chat. | Advanced coding, math proofs, hard debugging, logic puzzles. |
| **Creativity** | High fluidity, good at broad brainstorming. | Can be overly rigid or pedantic due to logic constraints. |

---

## The Next Frontier: Test-Time Compute

> The defining characteristic of reasoning models is **Test-Time Compute** (or inference-time compute).

> With standard models, scaling performance meant making the model bigger during *training* (more parameters). With reasoning models, we can scale performance during *inference*. 

> If you give the model a harder problem and allow it to spend 10 times longer thinking (generating more internal tokens and exploring more paths), the quality of the output scales dramatically upward without changing the underlying base model.

---

## The Reasoning Model Production Pipeline

1. **Select & Prepare the Base Model:** 

    > ***Prerequisite.***

    > Start with a high-quality, instruction-tuned base model. It needs a massive context window (ideally **32k to 128k+ tokens**) because the hidden reasoning monologues consume a large number of tokens before generating the final answer.

2. **Cold-Start SFT (Supervised Fine-Tuning):** 
    > ***Phase 1: Bootstrapping.***

    > An LLM won't naturally start thinking in tags like `<thought>...</thought>` without examples. Fine-tune your base model on a small, high-quality dataset (e.g., 5,000–10,000 samples) of structured reasoning.

    > * **Data structure:** The target output must look like: `<thought> [Step-by-step logic and verification] </thought> [Final Answer]`.
    > * This prevents the model from diverging during early RL phases.

3. **Construct Deterministic Reward Functions:** 
    > ***Phase 2: Defining Success.***
    
    > Avoid using an LLM as a judge here—it's too slow and noisy. Build precise, rule-based reward scripts:

    > * **Accuracy Reward:** For math, check if the string inside a `\boxed{}` LaTeX block matches the ground truth. For coding, run the generated Python script against a test suite; pass = 1, fail = 0.
    > * **Format Reward:** Enforce that the model correctly uses `<thought>` and `</thought>` tags. Penalize it if it leaks the answer early.

4. **Large-Scale Reinforcement Learning (GRPO/PPO):** Phase 3: The Core Engine.
    > Train the SFT model using an RL loop. **GRPO (Group Relative Policy Optimization)** is the modern standard here because it eliminates the need for a massive secondary Critic Model, saving up to 50% GPU memory.

    > * **The Loop:** The model receives a prompt $\rightarrow$ samples 4 to 8 different reasoning paths $\rightarrow$ the reward function scores them comparatively $\rightarrow$ the model updates its weights to favor paths that get the right answer and use clear formatting.

5. **Rejection Sampling & Distillation:** Phase 4: Refining.
    > Once the model learns to reason efficiently, use it to generate hundreds of thousands of correct reasoning paths for a wider pool of prompts. Filter out the dead-ends and syntactical mess. Use this clean, synthetic dataset to perform a final round of standard SFT on a fresh model (or a smaller model) to distill the reasoning capability cleanly.


---

## The Code implementation Strategy (DeepSeek-R1 style)

If you are setting this up locally using tools like PyTorch and Hugging Face's **TRL (Transformer Reinforcement Learning)** library, your custom training loop will leverage a GRPO trainer.

Here is how you write a custom **Reward Function** in Python to reward accurate formatting and correct answers—the two levers that force an LLM to develop an internal monologue:

```python
import re

def correctness_reward_func(prompts, completions, answer, **kwargs):
    """Rewards the model if the final extracted text matches the ground truth answer."""
    rewards = []
    for completion, ground_truth in zip(completions, answer):
        # Extract content outside of thought tags or inside a final answer box
        # Simple string match example
        final_answer = completion.split("</thought>")[-1].strip()
        if ground_truth.strip() in final_answer:
            rewards.append(1.0)
        else:
            rewards.append(0.0)
    return rewards

def format_reward_func(prompts, completions, **kwargs):
    """Rewards the model for strictly following the reasoning tag structure."""
    rewards = []
    pattern = r"^<thought>\n.*?\n</thought>\n"
    for completion in completions:
        # Check if the generation starts with a valid thought block
        if re.match(pattern, completion, re.DOTALL):
            rewards.append(0.5)  # Partial reward for correct structural format
        else:
            rewards.append(0.0)
    return rewards

```

> **The "Ah-Ha" Moment of RL:** When you run this pipeline, you will notice the model's output lengths swell over generations. It figures out on its own that the longer it spends re-evaluating its math steps inside the `<thought>` block, the higher its `correctness_reward` climbs.