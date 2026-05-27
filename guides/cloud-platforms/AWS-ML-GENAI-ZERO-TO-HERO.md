# AWS ML & GenAI — Zero to Hero

> **For ML engineers:** S3 data → IAM roles → SageMaker train/deploy → Bedrock inference.  
> Simple, copy-paste examples. Pair with [AI/ML Zero to Hero](../ai_ml/AI-ML-ZERO-TO-HERO.md).

**Prerequisite:** [AWS Cloud Zero to Hero](./aws-cloud-zero-to-hero.md) — IAM + S3 sections.

---

## Learning path (4 weeks)

| Week | Topic | Checkpoint |
|------|-------|------------|
| 1 | S3 + IAM for ML | Versioned bucket, role with least privilege |
| 2 | SageMaker training | sklearn job on CSV in S3 |
| 3 | SageMaker deploy | Real-time endpoint, invoke |
| 4 | Bedrock | Converse API + RAG from S3 docs |

---

## 1. S3 layout for ML projects

```
s3://my-ml-project/
├── raw/           # immutable uploads
├── processed/     # feature tables
├── models/        # model.tar.gz artifacts
└── metrics/       # experiment logs
```

```python
import boto3

s3 = boto3.client("s3")
bucket = "my-ml-project-UNIQUE"
key = "processed/train.csv"

# Upload local file
s3.upload_file("train.csv", bucket, key)
print(s3.head_object(Bucket=bucket, Key=key)["ContentLength"])
```

Enable **versioning** on the bucket; block public access.

---

## 2. IAM for ML (roles, not users)

**Pattern:** SageMaker execution role + optional human role for notebooks.

| Role | Trust | Typical permissions |
|------|-------|---------------------|
| `SageMakerExecutionRole` | `sagemaker.amazonaws.com` | S3 read/write on project prefix, ECR pull, CloudWatch logs |
| `DataScientistRole` | Your SSO user | SageMaker Studio, limited S3 prefix |

```json
{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject", "s3:ListBucket"],
  "Resource": [
    "arn:aws:s3:::my-ml-project-UNIQUE",
    "arn:aws:s3:::my-ml-project-UNIQUE/*"
  ]
}
```

Never embed access keys in notebooks — use the instance/notebook role.

---

## 3. SageMaker — train sklearn on S3 data

```python
# train_local.py — run locally first, then adapt for SageMaker Processing/Training
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv("train.csv")
X = df.drop(columns=["target"])
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("accuracy", accuracy_score(y_test, model.predict(X_test)))
joblib.dump(model, "model.joblib")
```

**SageMaker Training (concept):**

1. Upload `train.csv` to `s3://bucket/data/train.csv`
2. Use built-in **SKLearn** container or custom script in `s3://bucket/code/train.py`
3. `Estimator.fit({"train": "s3://bucket/data/train.csv"})`
4. Model artifact lands in `s3://bucket/models/`

CLI sketch:

```bash
aws sagemaker create-training-job \
  --training-job-name sklearn-demo-$(date +%s) \
  --role-arn arn:aws:iam::ACCOUNT:role/SageMakerExecutionRole \
  --algorithm-specification TrainingImage=246618743249.dkr.ecr.us-east-1.amazonaws.com/sagemaker-scikit-learn:1.2-1-cpu-py3,TrainingInputMode=File \
  --input-data-config file://input-config.json \
  --output-data-config S3OutputPath=s3://my-ml-project-UNIQUE/models/ \
  --resource-config InstanceType=ml.m5.large,InstanceCount=1 \
  --stopping-condition MaxRuntimeInSeconds=3600
```

Use **SageMaker Studio** or Python SDK (`sagemaker`) once CLI flow makes sense.

---

## 4. SageMaker — deploy endpoint

```python
import boto3

runtime = boto3.client("sagemaker-runtime")
endpoint_name = "sklearn-rf-demo"

# Payload format depends on container — often CSV or JSON
response = runtime.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType="text/csv",
    Body="5.1,3.5,1.4,0.2",
)
print(response["Body"].read())
```

**Production checklist:**

- Auto-scaling on invocations
- Multi-variant A/B (`ProductionVariants`)
- CloudWatch alarms on `ModelLatency`, `4XXError`
- Delete endpoint when done (cost)

---

## 5. Amazon Bedrock — managed foundation models

```python
import boto3
import json

client = boto3.client("bedrock-runtime", region_name="us-east-1")

body = json.dumps({
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 256,
    "messages": [{"role": "user", "content": "Explain S3 versioning in one paragraph."}],
})

response = client.invoke_model(
    modelId="anthropic.claude-3-haiku-20240307-v1:0",
    body=body,
)
result = json.loads(response["body"].read())
print(result["content"][0]["text"])
```

**Enable model access** in Bedrock console per region. Use **inference profiles** for cross-region routing in production.

---

## 6. RAG on AWS (simple pattern)

```
Documents (PDF) → S3
       ↓
Chunk + embed (Lambda or SageMaker Processing)
       ↓
OpenSearch Serverless / Aurora pgvector (vector store)
       ↓
Bedrock Converse + retrieval tool
```

See also: [RAG Production Guide](../ai_ml/RAG-PRODUCTION-GUIDE.md), [LLM Apps Zero to Hero](../ai_ml/LLM-APPS-ZERO-TO-HERO.md).

---

## 7. MLOps hooks

| Tool | Use |
|------|-----|
| SageMaker Pipelines | CI/CD for train → evaluate → register |
| Model Registry | Versioned models with approval gates |
| Experiments | Track runs (like MLflow) |
| Model Monitor | Data drift on endpoints |

Link: [MLOps Production Guide](../ai_ml/MLOps-Production-Complete-Guide.md).

---

## Security summary

- Encrypt S3 (SSE-S3 or KMS); encrypt EBS on training instances
- VPC endpoints for S3/Bedrock in private subnets
- SCPs at org level for allowed regions
- Log all API calls with CloudTrail

---

## Next steps

| Goal | Resource |
|------|----------|
| Full cloud path | [CLOUD-ZERO-TO-HERO.md](./CLOUD-ZERO-TO-HERO.md) |
| GCP Vertex | [GCP-CLOUD-ZERO-TO-HERO.md](./GCP-CLOUD-ZERO-TO-HERO.md) |
| RAG depth | [RAG-PRODUCTION-GUIDE.md](../ai_ml/RAG-PRODUCTION-GUIDE.md) |
