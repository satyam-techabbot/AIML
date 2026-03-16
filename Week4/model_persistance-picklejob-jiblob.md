# Model Persistence (Pickle/Joblib)

Model persistence means **saving a trained ML model to disk and loading it later without retraining**. This is essential in **MLOps, APIs, and production systems**.

In Python ML projects, the two most common tools are:
* **Pickle**
* **Joblib**

Both serialize Python objects so they can be reused later.

---

# 1️⃣ What is Model Persistence?

Normally the ML workflow is:

```
Train Model → Use Model → Program Ends → Model Lost
```

Model persistence allows:

```
Train Model → Save Model → Load Model Later → Predict
```

Example real workflow:

```
Training Pipeline
     ↓
model.pkl + preprocessor.pkl saved
     ↓
FastAPI / Flask API
     ↓
Load model and predict
```

This is exactly what your **prediction route** is doing.

---

# 2️⃣ What is Serialization?

Serialization converts a Python object into a **byte stream** that can be saved to a file.

Example object:
```python
RandomForestClassifier()
```

Serialized into:

```
model.pkl
```

Later you deserialize it back into a Python object.

---

# 3️⃣ Pickle (Standard Python Library)

The **pickle module** is built into Python.

It can serialize almost any Python object.

### Save Model with Pickle

```python
import pickle
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X_train, y_train)

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)
```

---

### Load Model with Pickle

```python
import pickle

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

predictions = model.predict(X_test)
```

---

# 4️⃣ Joblib (Recommended for ML)

**Joblib** is optimized for **large numpy arrays** and **scikit-learn models**.

That’s why most ML pipelines prefer it.

Install:

```bash
pip install joblib
```

---

### Save Model with Joblib

```python
import joblib
joblib.dump(model, "model.pkl")
```

---

### Load Model with Joblib

```python
import joblib
model = joblib.load("model.pkl")
```

---

# 5️⃣ Pickle vs Joblib

| Feature             | Pickle                | Joblib    |
| ------------------- | --------------------- | --------- |
| Built-in            | Yes                   | No        |
| Speed               | Slower for big arrays | Faster    |
| Best for            | General objects       | ML models |
| Compression         | No                    | Yes       |
| Large numpy support | Limited               | Excellent |

Recommendation:

```
Small objects → pickle
ML models → joblib
```

---

# 6️⃣ Saving Preprocessing Pipelines

In ML projects you must save **both**:

```
preprocessor
model
```

Example:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

pipeline.fit(X_train, y_train)

joblib.dump(pipeline, "pipeline.pkl")
```

Now the **entire pipeline** is saved.

---

# 7️⃣ Security Warning ⚠️

Pickle is **not secure**.

Never load pickle files from **untrusted sources**.

Why?

Because pickle can execute **arbitrary code**.

Safer alternatives:

* ONNX
* TorchScript
* TensorFlow SavedModel

But for **internal ML pipelines**, pickle/joblib are fine.

---

# 8️⃣ Best Practices for Model Persistence

### Save Model Version

```
model_v1.pkl
model_v2.pkl
```

---

### Save Metadata

```
model.pkl
preprocessor.pkl
config.yaml
metrics.json
```

---

### Save Inside Artifact Folder

```
artifacts/
   2026_03_16/
       model.pkl
       preprocessor.pkl
```
