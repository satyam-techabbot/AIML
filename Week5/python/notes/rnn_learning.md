# Recurrent Neural Network Tutorial (RNN)

A **Recurrent Neural Network (RNN)** is a type of neural network designed for **sequential data** (like time series, text, speech).

* Unlike traditional neural networks, **RNNs remember past inputs** using an internal memory.
* Output depends on **current input + previous inputs**. ([DataCamp][1])

Example: predicting stock prices, language translation, text generation.

Sequential task processing is required in Recurrent Neural Networks (RNNs) because they are specifically designed to model data where the order of elements carries critical information. 

---

## 📝 Key Concepts & Notes

### 1. How RNN Works
* Data flows in a **loop (cycle)** instead of one direction.
* Same weights are reused at each time step (parameter sharing).
* Hidden state carries information forward.

Formula idea:
```
Current output = f(current input + previous hidden state)
```

* Training uses **Backpropagation Through Time (BPTT)**
  → calculates error across all time steps. ([DataCamp][1])

---

### 2. Types of RNN Architectures
| Type         | Input → Output      | Example             |
| ------------ | ------------------- | ------------------- |
| One-to-One   | Single → Single     | Basic NN            |
| One-to-Many  | Single → Sequence   | Image captioning    |
| Many-to-One  | Sequence → Single   | Sentiment analysis  |
| Many-to-Many | Sequence → Sequence | Machine translation |

---

### 3. RNN vs CNN
| Feature   | RNN         | CNN              |
| --------- | ----------- | ---------------- |
| Data type | Sequential  | Spatial (images) |
| Memory    | Yes         | No               |
| Training  | BPTT        | Backpropagation  |
| Use cases | NLP, speech | Computer vision  |

---

### 4. Limitations of Basic RNN

### (a) Vanishing Gradient
* Gradients become very small → model stops learning.

### (b) Exploding Gradient
* Gradients become too large → unstable training.

These issues make RNNs bad at **long-term dependencies**.

---

### 5. Advanced RNN Architectures

### 🔹 LSTM (Long Short-Term Memory)
* Designed to handle long-term dependencies.
* Uses **gates** (input, forget, output).
* More complex but powerful.

👉 Applications:
* Speech recognition
* Machine translation

---

### 🔹 GRU (Gated Recurrent Unit)
* Simpler version of LSTM.
* Uses:
  * Update gate
  * Reset gate
* Faster training, fewer parameters.

👉 Key difference:
* GRU = simpler + faster
* LSTM = more control + slightly heavier

---

### 6. Practical Example (from tutorial)
Task: Predict **MasterCard stock prices**

#### Steps:
1. Data preprocessing
   * Train/test split
   * Scaling (MinMaxScaler)

2. Convert sequence → supervised learning format

3. Build models:

   * LSTM model
   * GRU model

4. Train:

   * 50 epochs
   * Batch size = 32

5. Evaluate:

   * GRU performed better (lower RMSE)

---

### 7. Key Takeaways
* RNNs are best for **sequence data**
* They use **memory (hidden states)** to capture context
* Training is done using **BPTT**
* Basic RNN struggles with long sequences
* **LSTM & GRU solve these issues**
* GRU can be faster with similar performance

---

## Final Quick Notes (Exam Style)
* RNN = Neural network with loops
* Handles sequential data
* Uses hidden state (memory)
* BPTT = training method
* Problems:
  * Vanishing gradient
  * Exploding gradient
* Solutions:
  * LSTM
  * GRU
* Applications:
  * NLP
  * Time series
  * Speech recognition

---

[1]: https://www.datacamp.com/tutorial/tutorial-for-recurrent-neural-network?utm_source=chatgpt.com "Recurrent Neural Network Tutorial (RNN) | DataCamp"
