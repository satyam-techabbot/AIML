# MLOps deployment workflow

```
Developer → GitHub → GitHub Actions → Build Docker Image → Push Image → AWS ECR → Deploy on EC2 → Run FastAPI container
```

## AWS ECR
Amazon Elastic Container Registry is a fully managed, secure, and scalable Docker container registry service. It allows developers to easily store, manage, and deploy container images, integrating seamlessly with Amazon ECS, EKS, and Lambda.

## AWS EC2
Amazon Elastic Compute Cloud (EC2) is a central AWS service providing secure, resizable virtual servers (instances) in the cloud, allowing users to rent computing capacity on-demand.


---

## 1️⃣ Project Architecture

Typical structure for your project:

```
network-security-mlops/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
│
├── network_security/
│   ├── pipeline/
│   ├── components/
│   ├── utils/
│
├── final_model/
│
└── .github/
    └── workflows/
        └── main.yaml
```

---

## 2️⃣ Workflow Overview

Full automation pipeline:
```
Developer pushes code
        ↓
GitHub Repository
        ↓
GitHub Actions workflow triggered
        ↓
Docker image built
        ↓
Image pushed to AWS ECR
        ↓
EC2 pulls latest image
        ↓
Container runs FastAPI app
```

---

## 3️⃣ Step 1 — Create AWS ECR Repository

Go to AWS console:
```
AWS Console
 → ECR
 → Create Repository
```

Example:
```
Repository name: network-security-app
```

ECR image URL example:
```
123456789012.dkr.ecr.ap-south-1.amazonaws.com/network-security-app
```

---

## 4️⃣ Step 2 — Create EC2 Instance
Launch an EC2 instance:
```
Ubuntu 22.04
t2.micro
```

Install Docker on EC2:
```bash
sudo apt update
sudo apt install docker.io -y
sudo usermod -aG docker ubuntu
```

Restart the instance or log out/login.

---

## 5️⃣ Step 3 — Update Dockerfile (Recommended)

Clean Dockerfile:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
```

---

## 6️⃣ Step 4 — Configure GitHub Secrets
Go to:
```
GitHub repo
→ Settings
→ Secrets and variables
→ Actions
```

Add these secrets:
```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
ECR_REPOSITORY
```

Example:
```
AWS_REGION=ap-south-1
ECR_REPOSITORY=network-security-app
```

---

## 7️⃣ Step 5 — GitHub Actions Workflow
`.github/workflows/main.yaml`

```yaml
name: Build and Push Docker Image

on:
  push:
    branches: [ "main" ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:

      - name: Checkout code
        uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_REGION }}

      - name: Login to ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v2

      - name: Build Docker Image
        run: |
          docker build -t ${{ secrets.ECR_REPOSITORY }} .

      - name: Tag Image
        run: |
          docker tag ${{ secrets.ECR_REPOSITORY }}:latest \
          ${{ steps.login-ecr.outputs.registry }}/${{ secrets.ECR_REPOSITORY }}:latest

      - name: Push Image to ECR
        run: |
          docker push ${{ steps.login-ecr.outputs.registry }}/${{ secrets.ECR_REPOSITORY }}:latest
```

Now every push will:
```
build image
push image to AWS ECR
```

---

## 8️⃣ Step 6 — Pull Image on EC2
Login to EC2:
```bash
ssh ubuntu@your-ec2-ip
```

Login to ECR:
```bash
aws ecr get-login-password --region ap-south-1 \
| docker login --username AWS \
--password-stdin 123456789012.dkr.ecr.ap-south-1.amazonaws.com
```

Pull image:
```bash
docker pull 123456789012.dkr.ecr.ap-south-1.amazonaws.com/network-security-app:latest
```

Run container:
```bash
docker run -d -p 8000:8000 network-security-app
```

---

## 9️⃣ Access the API

Open browser:
```
http://EC2_PUBLIC_IP:8000/docs
```
You will see your FastAPI Swagger UI.

---

## 🔟 Final Production Pipeline

Your ML deployment pipeline becomes:

```
Code Push
   ↓
GitHub
   ↓
GitHub Actions
   ↓
Build Docker Image
   ↓
Push to AWS ECR
   ↓
EC2 pulls latest image
   ↓
Run container
   ↓
FastAPI inference API
```

---

## 1️⃣1️⃣ Optional Production Improvements
Real ML teams also add:
```
MLflow model registry
Kubernetes (EKS)
Auto-scaling
Monitoring (Prometheus/Grafana)
CI tests
```
