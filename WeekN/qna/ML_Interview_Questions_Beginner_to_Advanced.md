# Machine Learning Questions: Beginner to Advanced

## PART 1: BEGINNER LEVEL

### 1. What is Machine Learning?
Machine Learning is a subfield of AI where systems learn patterns from data and improve their performance on a task without being explicitly programmed with rules. Instead of hard-coding logic, we feed data to an algorithm that learns a function mapping inputs to outputs.

### 2. What are the main types of Machine Learning?
- **Supervised Learning**: Learns from labeled data (input-output pairs). E.g., regression, classification.
- **Unsupervised Learning**: Learns patterns from unlabeled data. E.g., clustering, dimensionality reduction.
- **Semi-supervised Learning**: Uses a small amount of labeled data with a large amount of unlabeled data.
- **Reinforcement Learning**: An agent learns by interacting with an environment and receiving rewards/penalties.

### 3. What is the difference between supervised and unsupervised learning?
Supervised learning uses labeled data to learn a mapping from inputs to known outputs (e.g., predicting house prices). Unsupervised learning finds hidden structure in unlabeled data (e.g., grouping customers into segments) — there's no "correct answer" to compare against.

### 4. What is overfitting and underfitting?
- **Overfitting**: The model learns the training data too well, including noise, and performs poorly on unseen data. It has low bias but high variance.
- **Underfitting**: The model is too simple to capture the underlying pattern, performing poorly on both training and test data. High bias, low variance.

### 5. What is the bias-variance tradeoff?
Bias is the error from overly simplistic assumptions (leads to underfitting). Variance is the error from sensitivity to small fluctuations in training data (leads to overfitting). Total error = Bias² + Variance + Irreducible error. The goal is to find a sweet spot that minimizes both.

### 6. What is a training set, validation set, and test set?
- **Training set**: Used to fit the model's parameters.
- **Validation set**: Used to tune hyperparameters and make model selection decisions.
- **Test set**: Used only once, at the end, to estimate real-world generalization performance.

### 7. What is cross-validation?
A technique to assess how well a model generalizes by partitioning data into multiple folds. In **k-fold cross-validation**, data is split into k subsets; the model trains on k-1 folds and validates on the remaining fold, repeating k times, then averaging results. This gives a more reliable performance estimate than a single train/test split.

### 8. What is a confusion matrix?
A table showing the counts of True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN) for a classification model. It's the basis for metrics like precision, recall, and F1-score.

### 9. Define accuracy, precision, recall, and F1-score.
- **Accuracy** = (TP + TN) / (TP + TN + FP + FN) — overall correctness.
- **Precision** = TP / (TP + FP) — of predicted positives, how many are actually positive.
- **Recall (Sensitivity)** = TP / (TP + FN) — of actual positives, how many were correctly identified.
- **F1-score** = 2 × (Precision × Recall) / (Precision + Recall) — harmonic mean, balances precision and recall.

### 10. What is linear regression?
A supervised algorithm that models the relationship between a dependent variable and one or more independent variables by fitting a straight line: y = β₀ + β₁x₁ + ... + βₙxₙ. It minimizes the sum of squared residuals (errors between predicted and actual values).

### 11. What is logistic regression? How is it different from linear regression?
Logistic regression is used for classification (typically binary). It applies the sigmoid function to a linear combination of inputs to output a probability between 0 and 1. Unlike linear regression, it predicts a class probability rather than a continuous value, and uses log-loss (cross-entropy) instead of mean squared error as its cost function.

### 12. What is the difference between a parametric and non-parametric model?
Parametric models (e.g., linear regression) assume a fixed functional form with a finite set of parameters, regardless of data size. Non-parametric models (e.g., k-NN, decision trees) don't assume a fixed form and can grow in complexity with more data.

### 13. What is feature scaling and why is it important?
Feature scaling normalizes the range of independent variables (e.g., via standardization or min-max normalization). It's important for algorithms sensitive to feature magnitude (gradient descent-based models, k-NN, SVM, PCA) so that no single feature dominates due to scale alone.

### 14. What is the difference between normalization and standardization?
- **Normalization** (min-max scaling): rescales values to a fixed range, typically [0, 1].
- **Standardization** (z-score scaling): rescales data to have mean 0 and standard deviation 1, using (x − μ) / σ. Standardization is less affected by outliers than normalization.

### 15. What is a decision tree?
A tree-structured model that splits data based on feature values to make predictions. Each internal node represents a decision on a feature, branches represent outcomes, and leaves represent final predictions. Splits are chosen to maximize information gain or minimize impurity (Gini/entropy).

### 16. What is k-Nearest Neighbors (k-NN)?
A simple, instance-based (lazy) algorithm that classifies a new point based on the majority class among its k nearest neighbors in the feature space, using a distance metric (usually Euclidean).

### 17. What is the curse of dimensionality?
As the number of features grows, the volume of the feature space grows exponentially, making data increasingly sparse. This makes distance metrics less meaningful and models more prone to overfitting, requiring exponentially more data to maintain the same density.

### 18. What is one-hot encoding?
A technique to convert categorical variables into a binary vector format, where each category becomes a separate binary column (1 if present, 0 otherwise), avoiding a false sense of ordinal relationship between categories.

### 19. What is gradient descent?
An optimization algorithm that iteratively adjusts model parameters in the direction that reduces the loss function, using the negative gradient. The update rule: θ = θ − α∇J(θ), where α is the learning rate.

### 20. What is a loss function / cost function?
A function that measures how far off a model's predictions are from actual values. Training aims to minimize this function. Examples: Mean Squared Error (regression), Cross-Entropy Loss (classification).

---

## PART 2: INTERMEDIATE LEVEL

### 21. Explain the difference between batch, stochastic, and mini-batch gradient descent.
- **Batch GD**: Uses the entire dataset to compute the gradient at each step — stable but slow for large datasets.
- **Stochastic GD (SGD)**: Uses one sample per update — fast, noisy, can escape local minima but doesn't converge smoothly.
- **Mini-batch GD**: Uses a small batch (e.g., 32–256 samples) per update — a practical compromise, standard in deep learning.

### 22. What is regularization? Explain L1 and L2 regularization.
Regularization adds a penalty term to the loss function to discourage overly complex models and reduce overfitting.
- **L1 (Lasso)**: Adds the sum of absolute values of coefficients (λΣ|w|). It can shrink some coefficients to exactly zero, performing feature selection.
- **L2 (Ridge)**: Adds the sum of squared coefficients (λΣw²). It shrinks coefficients smoothly toward zero but rarely to exactly zero.
- **Elastic Net** combines both.

### 23. What is the difference between Gini impurity and entropy in decision trees?
Both measure node impurity for choosing splits.
- **Gini impurity** = 1 − Σpᵢ² — faster to compute, tends to isolate the most frequent class.
- **Entropy** = −Σpᵢlog₂(pᵢ) — rooted in information theory, computationally a bit more expensive (log calculation).
In practice, they usually produce similar trees.

### 24. What is ensemble learning? Name the main types.
Combining multiple models to produce better predictive performance than any single model.
- **Bagging** (Bootstrap Aggregating): Trains models in parallel on bootstrapped subsets and averages/votes results (e.g., Random Forest). Reduces variance.
- **Boosting**: Trains models sequentially, each correcting the errors of the previous one (e.g., AdaBoost, Gradient Boosting, XGBoost). Reduces bias.
- **Stacking**: Combines predictions of multiple different models using a meta-model.

### 25. How does Random Forest work?
It builds many decision trees, each trained on a bootstrapped sample of the data and considering only a random subset of features at each split. Final predictions are made by majority vote (classification) or averaging (regression). This decorrelates the trees and reduces overfitting compared to a single decision tree.

### 26. Explain Gradient Boosting.
Gradient Boosting builds an ensemble of weak learners (usually shallow decision trees) sequentially. Each new tree is trained to predict the residual errors (negative gradient of the loss) of the combined ensemble so far. Predictions are added with a learning rate to control overfitting. XGBoost, LightGBM, and CatBoost are popular optimized implementations.

### 27. What is the difference between bagging and boosting?
| Aspect | Bagging | Boosting |
|---|---|---|
| Training | Parallel | Sequential |
| Goal | Reduce variance | Reduce bias |
| Base learners | Independent, often deep trees | Weak learners, shallow trees |
| Weighting | Equal | Weighted based on errors |
| Overfitting risk | Lower | Higher if not tuned |

### 28. What is Support Vector Machine (SVM)?
A classifier that finds the optimal hyperplane maximizing the margin between classes. Points closest to the hyperplane are called support vectors. For non-linearly separable data, SVM uses the **kernel trick** (e.g., RBF, polynomial kernels) to implicitly map data into higher-dimensional space where it becomes linearly separable.

### 29. What is the kernel trick?
A method that allows SVMs (and other algorithms) to operate in high-dimensional feature space without explicitly computing the transformation, by using a kernel function K(x, x') that computes the dot product in that space directly — saving significant computation.

### 30. What is Naive Bayes and why is it "naive"?
A probabilistic classifier based on Bayes' theorem: P(y|X) ∝ P(X|y)P(y). It's "naive" because it assumes all features are conditionally independent given the class label — an assumption rarely true in practice, yet the algorithm often performs surprisingly well, especially for text classification.

### 31. What is PCA (Principal Component Analysis)?
An unsupervised dimensionality reduction technique that transforms data into a new set of orthogonal axes (principal components) ordered by the amount of variance they explain. It's computed via eigendecomposition of the covariance matrix or SVD, and helps reduce dimensionality while preserving as much variance as possible.

### 32. What is the difference between PCA and t-SNE/UMAP?
PCA is a linear technique focused on preserving global variance and is good for reducing dimensions for downstream modeling. t-SNE and UMAP are non-linear techniques primarily used for visualization; they preserve local neighborhood structure but distort global distances, and are not typically used as preprocessing for other models due to being non-deterministic and hard to invert.

### 33. What is clustering? Name common algorithms.
Clustering groups similar unlabeled data points together.
- **K-Means**: Partitions data into k clusters by minimizing within-cluster variance; iteratively assigns points to nearest centroid and updates centroids.
- **Hierarchical clustering**: Builds a tree (dendrogram) of nested clusters, either agglomerative (bottom-up) or divisive (top-down).
- **DBSCAN**: Density-based; groups points that are closely packed, and marks sparse points as outliers/noise — doesn't require specifying number of clusters upfront.

### 34. How do you choose the value of k in k-means?
- **Elbow method**: Plot within-cluster sum of squares (WCSS) against k and look for the "elbow" where improvement diminishes.
- **Silhouette score**: Measures how similar a point is to its own cluster vs other clusters; higher average silhouette indicates better k.
- Domain knowledge is often used alongside these statistical methods.

### 35. What is the ROC curve and AUC?
The ROC (Receiver Operating Characteristic) curve plots True Positive Rate (recall) against False Positive Rate at various classification thresholds. AUC (Area Under the Curve) summarizes this into a single number between 0 and 1, representing the model's ability to discriminate between classes — 0.5 means random guessing, 1.0 means perfect separation.

### 36. When would you use precision over recall, or vice versa?
- Prioritize **precision** when false positives are costly (e.g., spam detection — you don't want important emails marked as spam).
- Prioritize **recall** when false negatives are costly (e.g., cancer/disease detection — missing a true case is dangerous).
- **F1-score** or the **precision-recall curve** helps when you need a balance, especially with imbalanced classes.

### 37. How do you handle imbalanced datasets?
- Resampling: oversampling the minority class (e.g., SMOTE) or undersampling the majority class.
- Use class weights in the loss function to penalize misclassifying the minority class more.
- Use appropriate metrics: precision, recall, F1, AUC-PR instead of accuracy.
- Try ensemble techniques like balanced random forest or algorithms designed for imbalance.
- Collect more data for the minority class if possible.

### 38. What is multicollinearity and how do you detect/handle it?
Multicollinearity occurs when independent variables in a regression model are highly correlated with each other, making coefficient estimates unstable and hard to interpret. Detect it using the **Variance Inflation Factor (VIF)** — VIF > 5 or 10 typically signals a problem. Handle it by removing correlated features, combining them, or applying regularization (Ridge regression).

### 39. What is the difference between a generative and a discriminative model?
- **Generative models** learn the joint probability P(X, Y) and can generate new data (e.g., Naive Bayes, GANs, Hidden Markov Models).
- **Discriminative models** learn the conditional probability P(Y|X) directly, focusing only on the decision boundary (e.g., logistic regression, SVM).

### 40. Explain the difference between Type I and Type II errors.
- **Type I error (False Positive)**: Rejecting a true null hypothesis — e.g., predicting a healthy patient has a disease.
- **Type II error (False Negative)**: Failing to reject a false null hypothesis — e.g., predicting a sick patient is healthy.
There's usually a tradeoff between the two, controlled by the decision threshold.

---

## PART 3: ADVANCED LEVEL

### 41. Explain how backpropagation works in neural networks.
Backpropagation computes the gradient of the loss function with respect to each weight using the chain rule, propagating error backward from the output layer to the input layer. For each layer, it computes ∂L/∂w by multiplying the local gradient by the gradient received from the layer ahead, enabling efficient computation of gradients for all parameters in a single backward pass, which are then used by gradient descent (or a variant like Adam) to update weights.

### 42. What is the vanishing/exploding gradient problem, and how do you address it?
In deep networks, gradients can shrink (vanish) or grow (explode) exponentially as they propagate backward through many layers, especially with saturating activations like sigmoid/tanh. This makes training unstable or extremely slow.
**Solutions**: 
- Use ReLU or its variants (Leaky ReLU, ELU) instead of sigmoid/tanh.
- Proper weight initialization (Xavier/Glorot, He initialization).
- Batch normalization.
- Gradient clipping (for exploding gradients).
- Residual/skip connections (ResNets).
- Use architectures like LSTM/GRU for sequential data.

### 43. Explain the difference between batch normalization and layer normalization.
- **Batch Normalization** normalizes activations across the batch dimension for each feature — computed per-feature, across the mini-batch. Effective for CNNs but depends on batch size and behaves differently at train vs inference time.
- **Layer Normalization** normalizes across the feature dimension for each individual sample, independent of batch size — commonly used in Transformers and RNNs where batch statistics are less meaningful or batch size varies.

### 44. What is dropout and how does it prevent overfitting?
Dropout randomly "drops" (zeroes out) a fraction of neurons during each training iteration, forcing the network to not rely too heavily on any single neuron and effectively training an ensemble of sub-networks that share weights. At inference time, all neurons are active but outputs are scaled to account for the dropped units during training (or scaling is done during training itself — "inverted dropout").

### 45. Explain the architecture and intuition behind Convolutional Neural Networks (CNNs).
CNNs use convolutional layers with learnable filters/kernels that slide over the input to detect local spatial patterns (edges, textures, shapes), exploiting spatial locality and parameter sharing to drastically reduce parameters compared to fully connected layers. Pooling layers (max/average) downsample feature maps, providing translation invariance and reducing computation. Stacking convolutional layers builds increasingly abstract, hierarchical feature representations, from edges in early layers to complex objects in deeper layers.

### 46. What is the difference between RNN, LSTM, and GRU?
- **RNN**: Processes sequences by maintaining a hidden state updated at each timestep, but suffers from vanishing gradients over long sequences.
- **LSTM (Long Short-Term Memory)**: Introduces a cell state and three gates (input, forget, output) that regulate information flow, allowing it to retain long-range dependencies.
- **GRU (Gated Recurrent Unit)**: A simplified LSTM variant with two gates (reset, update) and no separate cell state — fewer parameters, often comparable performance, and faster to train.

### 47. Explain the Transformer architecture and self-attention mechanism.
Transformers process entire sequences in parallel (unlike RNNs) using **self-attention**, which computes a weighted representation of each token based on its relevance to every other token in the sequence. For each token, Query (Q), Key (K), and Value (V) vectors are computed; attention weights are calculated as softmax(QKᵀ/√dₖ), then used to weight the V vectors. **Multi-head attention** runs several attention operations in parallel with different learned projections, capturing different types of relationships. Since there's no inherent sequence order, **positional encodings** are added to token embeddings. This architecture underlies models like BERT and GPT.

### 48. What is the difference between self-attention and cross-attention?
**Self-attention** computes attention within a single sequence — Q, K, and V all come from the same source (e.g., a sentence attending to itself). **Cross-attention** computes attention between two different sequences — Q comes from one sequence (e.g., decoder output) while K and V come from another (e.g., encoder output), used in encoder-decoder architectures like machine translation.

### 49. What is transfer learning and fine-tuning?
Transfer learning reuses a model pretrained on a large dataset (e.g., ImageNet, or a large text corpus) as a starting point for a new, often smaller, task. **Fine-tuning** involves further training some or all layers of the pretrained model on the new task's data, typically with a lower learning rate. This is effective because early layers learn general features (edges, basic syntax) that transfer well across tasks, while later layers are more task-specific.

### 50. Explain the Adam optimizer and why it's popular.
Adam (Adaptive Moment Estimation) combines the benefits of Momentum and RMSProp. It maintains an exponentially decaying average of past gradients (first moment, like momentum) and an exponentially decaying average of past squared gradients (second moment, like RMSProp), using both to compute adaptive per-parameter learning rates, with bias correction terms to account for their initialization at zero. It's popular because it converges quickly, requires little tuning, and works well across a wide range of problems.

### 51. What is the exploration-exploitation tradeoff in reinforcement learning?
An agent must balance **exploration** (trying new actions to discover their rewards) with **exploitation** (choosing the action currently believed to yield the highest reward). Too much exploration wastes time on suboptimal actions; too much exploitation risks missing better strategies. Common approaches: epsilon-greedy, softmax action selection, Upper Confidence Bound (UCB), and Thompson sampling.

### 52. Explain the difference between Q-learning and policy gradient methods.
- **Q-learning** is a value-based, off-policy method that learns the action-value function Q(s, a) representing expected future reward, then derives a policy by choosing the action with the highest Q-value. Works well for discrete action spaces.
- **Policy gradient methods** directly parameterize and optimize the policy π(a|s) by following the gradient of expected reward, allowing them to naturally handle continuous action spaces and stochastic policies (e.g., REINFORCE, PPO, A3C).

### 53. What is the difference between generative adversarial networks (GANs) and variational autoencoders (VAEs)?
- **GANs** consist of a generator (creates fake samples) and a discriminator (distinguishes real from fake) trained adversarially in a minimax game. They tend to produce sharper, more realistic outputs but training can be unstable (mode collapse).
- **VAEs** learn a probabilistic latent space by encoding inputs into a distribution (mean, variance) and decoding samples from it, optimizing a reconstruction loss plus a KL-divergence regularization term. Training is more stable, but outputs tend to be blurrier than GANs.

### 54. What is attention's computational complexity, and how do efficient Transformers address it?
Standard self-attention has O(n²) time and memory complexity with respect to sequence length n, since every token attends to every other token. This becomes prohibitive for long sequences. Efficient variants address this via sparse attention (attending to a subset of tokens), low-rank approximations (e.g., Linformer), kernel-based linear attention (e.g., Performer), or chunking/recurrence approaches (e.g., Longformer, Transformer-XL) that reduce complexity toward O(n) or O(n log n).

### 55. What is catastrophic forgetting and how is it mitigated?
Catastrophic forgetting occurs when a neural network, trained sequentially on new tasks, abruptly loses performance on previously learned tasks because new weight updates overwrite important prior knowledge. Mitigation strategies include: rehearsal/replay (retaining a memory buffer of old task data), regularization-based methods that penalize changes to weights important for old tasks (e.g., Elastic Weight Consolidation), and architectural approaches that allocate separate parameters per task.

### 56. Explain how gradient boosted trees (like XGBoost) differ from standard gradient boosting, and how they mitigate overfitting.
XGBoost improves on standard gradient boosting with: a **regularized objective** (L1/L2 penalties on leaf weights and tree complexity), **second-order gradient information** (uses both gradient and Hessian for more accurate updates — Newton boosting), built-in handling of missing values, column and row subsampling for regularization (similar to Random Forest), and efficient parallel/distributed tree construction. These features make it far less prone to overfitting than naive gradient boosting and much faster to train.

### 57. What is the difference between L-BFGS and SGD-based optimization for training models?
L-BFGS is a quasi-Newton method that approximates the inverse Hessian to take more informed steps, converging faster in fewer iterations for smooth, convex, or moderately-sized problems — but it's memory-intensive and doesn't scale well to the massive, non-convex, mini-batch settings of deep learning. SGD (and its variants) uses only first-order gradient information, is much cheaper per step, scales to huge datasets via mini-batching, and its inherent noise can help escape sharp local minima/saddle points — making it the standard choice for training deep neural networks.

### 58. How would you detect and address data leakage in a machine learning pipeline?
Data leakage occurs when information from outside the training set (often inadvertently from the test/future data) influences model training, leading to unrealistically good validation performance that doesn't hold in production. Common causes: preprocessing (scaling, imputation, feature selection) done on the full dataset before splitting; including features that wouldn't be available at prediction time; duplicate or near-duplicate records across train/test splits; target leakage (features that are proxies for the label). Detection: suspiciously high validation performance, feature importance dominated by one unexpectedly predictive feature, performance dropping sharply in production. Prevention: always split data before any preprocessing/fitting, use pipelines that fit transformers only on training folds, carefully audit feature timing relative to the prediction point, and use time-based splits for temporal data.

### 59. What is the difference between model calibration and model accuracy, and why does it matter?
Accuracy measures whether predicted classes are correct; **calibration** measures whether predicted probabilities reflect true likelihoods (e.g., among all predictions with 0.8 confidence, roughly 80% should actually be correct). A model can be highly accurate yet poorly calibrated (overconfident or underconfident). This matters in high-stakes applications (medical diagnosis, risk scoring) where downstream decisions depend on probability estimates, not just the predicted class. Calibration is assessed via reliability diagrams and Expected Calibration Error (ECE), and can be corrected using techniques like Platt scaling or isotonic regression.

### 60. How do you approach designing an ML system end-to-end for a production use case (ML system design)?
A structured approach typically covers:
1. **Problem framing**: Translate the business problem into an ML task (classification, ranking, regression) and define success metrics (both offline like AUC/F1, and online like click-through rate).
2. **Data**: Identify data sources, labeling strategy, handle class imbalance, and define train/validation/test splits (respecting temporal order if relevant).
3. **Feature engineering**: Design features, consider a feature store for consistency between training and serving.
4. **Modeling**: Start with a simple baseline, iterate toward more complex models, and justify tradeoffs (interpretability vs performance, latency constraints).
5. **Evaluation**: Offline metrics plus a plan for online A/B testing.
6. **Deployment**: Batch vs real-time inference, latency/throughput requirements, model versioning.
7. **Monitoring**: Track data/concept drift, prediction distribution shifts, and retraining triggers.
8. **Scalability & maintenance**: Plan for retraining cadence, rollback strategy, and logging/feedback loops for continuous improvement.

---

## Quick-Reference Tips for the Interview

- **Always tie concepts back to trade-offs** (bias/variance, precision/recall, speed/accuracy) — interviewers want to see you understand *why*, not just definitions.
- **Use concrete examples** from projects when explaining concepts; it shows applied understanding.
- **For coding rounds**: be comfortable implementing k-NN, k-means, linear/logistic regression, and a basic neural network forward/backward pass from scratch (numpy).
- **For system design rounds**: structure your answer (problem → data → model → evaluation → deployment → monitoring) rather than jumping straight to model choice.
- **Ask clarifying questions** for open-ended prompts (e.g., "build a recommendation system") before diving in — this is often part of what's being evaluated.

---

*Good luck with your interview prep! If you'd like, I can turn this into flashcards, generate mock interview questions on a specific topic (e.g., deep learning, NLP, or ML system design), or create a Word/PDF version of this guide.*
