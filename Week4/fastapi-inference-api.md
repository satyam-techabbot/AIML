# Basic Inference APIs with FastAPI

## 1️⃣ What is an Inference API?

An **Inference API** is a web service that allows users or applications to **send input data to a trained ML model and receive predictions**.

### Typical Flow

```
Client (User/App)
        ↓
HTTP Request
        ↓
FastAPI Server
        ↓
Load Model + Preprocessor
        ↓
Run Prediction
        ↓
Return Result (JSON / HTML)
```

Example request:

```
POST /predict
{
   "age": 45,
   "income": 50000
}
```

Example response:

```
{
   "prediction": "Approved"
}
```

---

## 2️⃣ Why Use FastAPI for ML Inference?

FastAPI is one of the best frameworks for ML deployment.

### Advantages

* Extremely **fast**
* **Automatic API documentation**
* Built-in **data validation**
* Supports **async operations**
* Easy integration with ML libraries

---

## 3️⃣ Installing FastAPI

Install required packages:

```bash
pip install fastapi uvicorn
```

Run server:

```bash
uvicorn app:app --reload
```

Explanation:

```
app → python file
app → FastAPI object
--reload → auto restart server
```

Server runs at:

```
http://127.0.0.1:8000
```

---

## 4️⃣ Basic FastAPI Application

Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ML API is running"}
```

Test in browser:

```
http://127.0.0.1:8000
```

---

## 5️⃣ Automatic API Documentation

FastAPI automatically creates interactive docs.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 6️⃣ Loading a Trained Model

Models are usually saved using **pickle or joblib**.

Example:

```python
import joblib

model = joblib.load("model.pkl")
```

For ML projects we usually load:

```
model.pkl
preprocessor.pkl
```

---

## 7️⃣ Basic Prediction API

Example inference API:

```python
from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.pkl")

@app.post("/predict")
def predict(data: list):

    prediction = model.predict([data])

    return {"prediction": prediction.tolist()}
```

Request example:

```
POST /predict
[45, 60000]
```

Response:

```
{
 "prediction": [1]
}
```

---

## 8️⃣ Using Pydantic for Input Validation

FastAPI uses **Pydantic models** to validate request data.

Example:

```python
from pydantic import BaseModel

class InputData(BaseModel):
    age: int
    salary: float
```

Prediction route:

```python
@app.post("/predict")
def predict(data: InputData):

    features = [[data.age, data.salary]]
    prediction = model.predict(features)

    return {"prediction": int(prediction[0])}
```

Advantages:

* Automatic validation
* Cleaner code
* Prevents invalid inputs

---

## 9️⃣ File Upload Inference API

Used when predicting from **CSV files**.

Example:

```python
from fastapi import UploadFile, File
import pandas as pd

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)
    predictions = model.predict(df)

    return {"prediction": predictions.tolist()}
```

This is similar to your **Network Security project**.

---

## 🔟 Using Preprocessor + Model

In real ML systems we must apply **same preprocessing used during training**.

Example:

```python
preprocessor = joblib.load("preprocessor.pkl")
model = joblib.load("model.pkl")

@app.post("/predict")

def predict(data: InputData):

    df = pd.DataFrame([data.dict()])
    transformed = preprocessor.transform(df)
    prediction = model.predict(transformed)

    return {"prediction": int(prediction[0])}
```

Pipeline:

```
Input Data
     ↓
Preprocessor
     ↓
ML Model
     ↓
Prediction
```

---

## 1️⃣1️⃣ Tools Used with FastAPI in ML

Common tools:

| Tool          | Purpose           |
| ------------- | ----------------- |
| FastAPI       | API framework     |
| Uvicorn       | ASGI server       |
| Scikit-learn  | ML models         |
| Pandas        | Data processing   |
| Pickle/Joblib | Model persistence |
| Docker        | Deployment        |
| MLflow        | Model tracking    |
