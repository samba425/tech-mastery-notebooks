# 🚀 MLOps & Production ML - Complete Guide

> **Deploy, Monitor, and Scale Machine Learning Systems**

---

## 🎯 What is MLOps?

MLOps = Machine Learning + DevOps + Data Engineering

**Why Critical?**
- 87% of ML projects never make it to production
- Companies need ML engineers who can DEPLOY, not just train
- **Highest salary premium:** +30-50% over data scientists

---

## 📚 Complete MLOps Stack

```
┌─────────────────────────────────────────────┐
│          MLOps Complete Stack               │
├─────────────────────────────────────────────┤
│  Development                                │
│  ├── Jupyter, VSCode                       │
│  ├── Git, DVC (Data Version Control)       │
│  └── Virtual Environments                   │
├─────────────────────────────────────────────┤
│  Experiment Tracking                        │
│  ├── MLflow                                │
│  ├── Weights & Biases                      │
│  └── TensorBoard                           │
├─────────────────────────────────────────────┤
│  Model Training                             │
│  ├── PyTorch, TensorFlow                  │
│  ├── scikit-learn                          │
│  └── XGBoost, LightGBM                     │
├─────────────────────────────────────────────┤
│  Model Serving                              │
│  ├── FastAPI, Flask                        │
│  ├── TorchServe, TF Serving               │
│  └── ONNX Runtime                          │
├─────────────────────────────────────────────┤
│  Containerization                           │
│  ├── Docker                                │
│  └── Docker Compose                        │
├─────────────────────────────────────────────┤
│  Orchestration                              │
│  ├── Kubernetes                            │
│  ├── Kubeflow                              │
│  └── Airflow                               │
├─────────────────────────────────────────────┤
│  Monitoring                                 │
│  ├── Prometheus                            │
│  ├── Grafana                               │
│  └── ELK Stack                             │
├─────────────────────────────────────────────┤
│  Cloud Platforms                            │
│  ├── AWS (SageMaker, Lambda, ECS)         │
│  ├── GCP (Vertex AI, Cloud Run)           │
│  └── Azure (ML Studio)                     │
└─────────────────────────────────────────────┘
```

---

## Part 1: Experiment Tracking

### **MLflow Complete Setup:**

```python
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import numpy as np

# Start MLflow tracking
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("my-ml-experiment")

def train_model(n_estimators, max_depth, data):
    with mlflow.start_run():
        # Log parameters
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        
        # Train model
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=42
        )
        model.fit(data['X_train'], data['y_train'])
        
        # Predict
        predictions = model.predict(data['X_test'])
        
        # Log metrics
        accuracy = accuracy_score(data['y_test'], predictions)
        f1 = f1_score(data['y_test'], predictions, average='weighted')
        
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("f1_score", f1)
        
        # Log model
        mlflow.sklearn.log_model(model, "model")
        
        # Log artifacts
        import matplotlib.pyplot as plt
        from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
        
        cm = confusion_matrix(data['y_test'], predictions)
        disp = ConfusionMatrixDisplay(cm)
        disp.plot()
        plt.savefig("confusion_matrix.png")
        mlflow.log_artifact("confusion_matrix.png")
        
        print(f"Run ID: {mlflow.active_run().info.run_id}")
        return model

# Hyperparameter tuning with MLflow
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15]
}

for n_est in param_grid['n_estimators']:
    for depth in param_grid['max_depth']:
        train_model(n_est, depth, data)

# Load best model
best_run = mlflow.search_runs(order_by=['metrics.accuracy DESC']).iloc[0]
model_uri = f"runs:/{best_run.run_id}/model"
loaded_model = mlflow.sklearn.load_model(model_uri)
```

### **Start MLflow UI:**

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
# Access at http://localhost:5000
```

---

## Part 2: Model Serving

### **FastAPI Production Server:**

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mlflow.sklearn
import numpy as np
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="ML Model API", version="1.0")

# Load model at startup
@app.on_event("startup")
async def load_model():
    global model
    try:
        model = mlflow.sklearn.load_model("models:/production-model/latest")
        logger.info("Model loaded successfully")
    except Exception as e:
        logger.error(f"Failed to load model: {e}")
        raise

class PredictionRequest(BaseModel):
    features: list[float]

class PredictionResponse(BaseModel):
    prediction: int
    probability: float

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """Make prediction"""
    try:
        # Validate input
        features = np.array(request.features).reshape(1, -1)
        
        # Predict
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features).max()
        
        logger.info(f"Prediction: {prediction}, Probability: {probability}")
        
        return PredictionResponse(
            prediction=int(prediction),
            probability=float(probability)
        )
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict/batch")
async def predict_batch(requests: list[PredictionRequest]):
    """Batch predictions"""
    features = np.array([req.features for req in requests])
    predictions = model.predict(features)
    probabilities = model.predict_proba(features).max(axis=1)
    
    return [
        {"prediction": int(pred), "probability": float(prob)}
        for pred, prob in zip(predictions, probabilities)
    ]

@app.get("/health")
async def health_check():
    """Health check"""
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "version": "1.0"
    }

@app.get("/metrics")
async def get_metrics():
    """Get model metrics"""
    # In production, track actual metrics
    return {
        "requests_total": 1000,
        "predictions_total": 950,
        "errors_total": 50,
        "avg_latency_ms": 45.2
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

---

## Part 3: Docker Containerization

### **Dockerfile (Production-Ready):**

```dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
```

### **docker-compose.yml:**

```yaml
version: '3.8'

services:
  ml-api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - MODEL_PATH=/models
      - LOG_LEVEL=INFO
    volumes:
      - ./models:/models
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G
    restart: unless-stopped
  
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data
    restart: unless-stopped
  
  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus-data:/prometheus
    restart: unless-stopped
  
  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana-data:/var/lib/grafana
    restart: unless-stopped

volumes:
  redis-data:
  prometheus-data:
  grafana-data:
```

### **Build & Run:**

```bash
# Build image
docker build -t ml-model:latest .

# Run container
docker run -d -p 8000:8000 --name ml-api ml-model:latest

# Run with compose
docker-compose up -d

# View logs
docker-compose logs -f ml-api

# Scale service
docker-compose up -d --scale ml-api=3
```

---

## Part 4: Kubernetes Deployment

### **deployment.yaml:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ml-model-deployment
  labels:
    app: ml-model
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ml-model
  template:
    metadata:
      labels:
        app: ml-model
    spec:
      containers:
      - name: ml-model
        image: ml-model:latest
        ports:
        - containerPort: 8000
        env:
        - name: MODEL_PATH
          value: "/models"
        resources:
          requests:
            memory: "2Gi"
            cpu: "1000m"
          limits:
            memory: "4Gi"
            cpu: "2000m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: ml-model-service
spec:
  selector:
    app: ml-model
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
  type: LoadBalancer
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: ml-model-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ml-model-deployment
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

### **Deploy to Kubernetes:**

```bash
# Apply deployment
kubectl apply -f deployment.yaml

# Check status
kubectl get deployments
kubectl get pods
kubectl get services

# View logs
kubectl logs -f deployment/ml-model-deployment

# Scale manually
kubectl scale deployment ml-model-deployment --replicas=5

# Update deployment
kubectl set image deployment/ml-model-deployment ml-model=ml-model:v2

# Rollback
kubectl rollout undo deployment/ml-model-deployment
```

---

## Part 5: Monitoring & Observability

### **Prometheus Metrics:**

```python
from prometheus_client import Counter, Histogram, Gauge, start_http_server
from functools import wraps
import time

# Define metrics
REQUEST_COUNT = Counter(
    'ml_requests_total',
    'Total ML prediction requests',
    ['endpoint', 'http_status']
)

REQUEST_LATENCY = Histogram(
    'ml_request_latency_seconds',
    'Request latency in seconds',
    ['endpoint']
)

PREDICTIONS_COUNT = Counter(
    'ml_predictions_total',
    'Total predictions made',
    ['model_version']
)

MODEL_CONFIDENCE = Histogram(
    'ml_prediction_confidence',
    'Prediction confidence scores',
    buckets=[0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99, 1.0]
)

ACTIVE_MODELS = Gauge(
    'ml_active_models',
    'Number of active models loaded'
)

# Decorator for monitoring
def monitor_predictions(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        
        try:
            result = await func(*args, **kwargs)
            REQUEST_COUNT.labels(endpoint=func.__name__, http_status=200).inc()
            return result
        except Exception as e:
            REQUEST_COUNT.labels(endpoint=func.__name__, http_status=500).inc()
            raise
        finally:
            REQUEST_LATENCY.labels(endpoint=func.__name__).observe(
                time.time() - start_time
            )
    
    return wrapper

# Use in FastAPI
@app.post("/predict")
@monitor_predictions
async def predict(request: PredictionRequest):
    prediction = model.predict(...)
    confidence = model.predict_proba(...).max()
    
    PREDICTIONS_COUNT.labels(model_version="v1").inc()
    MODEL_CONFIDENCE.observe(confidence)
    
    return {"prediction": prediction, "confidence": confidence}

# Start Prometheus metrics server
start_http_server(9091)
```

### **Grafana Dashboard (JSON):**

```json
{
  "dashboard": {
    "title": "ML Model Monitoring",
    "panels": [
      {
        "title": "Request Rate",
        "targets": [
          {
            "expr": "rate(ml_requests_total[5m])"
          }
        ]
      },
      {
        "title": "P95 Latency",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(ml_request_latency_seconds_bucket[5m]))"
          }
        ]
      },
      {
        "title": "Prediction Confidence",
        "targets": [
          {
            "expr": "ml_prediction_confidence"
          }
        ]
      },
      {
        "title": "Error Rate",
        "targets": [
          {
            "expr": "rate(ml_requests_total{http_status=\"500\"}[5m])"
          }
        ]
      }
    ]
  }
}
```

---

## Part 6: CI/CD for ML

### **GitHub Actions Workflow:**

```yaml
name: ML Model CI/CD

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest pytest-cov
    
    - name: Run tests
      run: |
        pytest tests/ --cov=src --cov-report=xml
    
    - name: Check model performance
      run: |
        python scripts/evaluate_model.py --threshold 0.85
  
  build:
    needs: test
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Build Docker image
      run: |
        docker build -t ml-model:${{ github.sha }} .
    
    - name: Run security scan
      run: |
        docker scan ml-model:${{ github.sha }}
    
    - name: Push to registry
      run: |
        echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin
        docker push ml-model:${{ github.sha }}
  
  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - name: Deploy to Kubernetes
      run: |
        kubectl set image deployment/ml-model ml-model=ml-model:${{ github.sha }}
        kubectl rollout status deployment/ml-model
```

---

## Part 7: Model Versioning with DVC

### **Setup DVC:**

```bash
# Initialize DVC
dvc init

# Add remote storage (S3)
dvc remote add -d myremote s3://my-bucket/dvc-storage

# Track data
dvc add data/train.csv
dvc add models/model.pkl

# Commit to Git
git add data/train.csv.dvc models/model.pkl.dvc .dvc/config
git commit -m "Track data and model with DVC"

# Push data to remote
dvc push

# Pull data
dvc pull
```

### **DVC Pipeline (dvc.yaml):**

```yaml
stages:
  prepare:
    cmd: python src/prepare.py
    deps:
      - data/raw
    outs:
      - data/processed
    params:
      - prepare.test_size
  
  train:
    cmd: python src/train.py
    deps:
      - data/processed
      - src/train.py
    outs:
      - models/model.pkl
    metrics:
      - metrics.json:
          cache: false
    params:
      - train.n_estimators
      - train.max_depth
  
  evaluate:
    cmd: python src/evaluate.py
    deps:
      - models/model.pkl
      - data/processed
    metrics:
      - eval_metrics.json:
          cache: false
```

### **Run Pipeline:**

```bash
# Run entire pipeline
dvc repro

# Run specific stage
dvc repro train

# Compare experiments
dvc metrics show
dvc metrics diff

# Visualize pipeline
dvc dag
```

---

## Part 8: AWS Deployment

### **Deploy to AWS Lambda:**

```python
# handler.py
import json
import boto3
import pickle

s3 = boto3.client('s3')

def load_model():
    """Load model from S3"""
    obj = s3.get_object(Bucket='my-models', Key='model.pkl')
    model = pickle.loads(obj['Body'].read())
    return model

model = load_model()

def lambda_handler(event, context):
    """Lambda function handler"""
    try:
        # Parse input
        body = json.loads(event['body'])
        features = body['features']
        
        # Predict
        prediction = model.predict([features])[0]
        probability = model.predict_proba([features]).max()
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'prediction': int(prediction),
                'probability': float(probability)
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
```

### **Deploy with Serverless Framework:**

```yaml
# serverless.yml
service: ml-model-api

provider:
  name: aws
  runtime: python3.9
  region: us-east-1
  memorySize: 1024
  timeout: 30
  
functions:
  predict:
    handler: handler.lambda_handler
    events:
      - http:
          path: predict
          method: post
    environment:
      MODEL_BUCKET: my-models
      MODEL_KEY: model.pkl

plugins:
  - serverless-python-requirements
```

```bash
# Deploy
serverless deploy

# Invoke
serverless invoke -f predict -d '{"features": [1,2,3,4]}'
```

---

## 📚 Complete MLOps Checklist

### **Pre-Production:**
- [ ] Code in version control (Git)
- [ ] Data versioned (DVC)
- [ ] Experiments tracked (MLflow)
- [ ] Models tested (pytest)
- [ ] API documented (FastAPI/Swagger)
- [ ] Docker image built
- [ ] Security scan passed

### **Production:**
- [ ] Deployed to cloud/K8s
- [ ] Auto-scaling configured
- [ ] Monitoring setup (Prometheus)
- [ ] Logging configured (ELK)
- [ ] Alerts configured
- [ ] CI/CD pipeline working
- [ ] Backup strategy in place

### **Post-Production:**
- [ ] Model performance monitored
- [ ] Data drift detected
- [ ] Retraining automated
- [ ] A/B testing setup
- [ ] Cost optimized

---

## 💼 Career Impact

**Without MLOps Skills:**
- Data Scientist: $90K-$120K
- ML Engineer: $100K-$140K

**With MLOps Skills:**
- MLOps Engineer: $130K-$180K
- ML Platform Engineer: $150K-$200K
- Principal ML Engineer: $200K-$300K+

**Skills Multiplier: +40-60% salary** 🚀

---

## 🎯 8-Week Learning Path

```
Week 1-2: Experiment Tracking & Model Serving
Week 3-4: Docker & Kubernetes
Week 5-6: Monitoring & CI/CD
Week 7-8: Cloud Deployment & Production

Project: Deploy end-to-end ML system
```

---

*MLOps Complete Guide*
*From Development to Production*
*Career game-changer skills* 💰

