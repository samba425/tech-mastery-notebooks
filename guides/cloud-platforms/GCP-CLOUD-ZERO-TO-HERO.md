# GCP Cloud — Zero to Hero

> **Tri-cloud completion:** Compute Engine, Cloud Storage, BigQuery, Vertex AI intro.  
> Shorter than AWS guide — enough to interview and prototype. Compare with [CLOUD-ZERO-TO-HERO.md](./CLOUD-ZERO-TO-HERO.md).

---

## Setup (30 minutes)

```bash
# Install gcloud CLI: https://cloud.google.com/sdk/docs/install
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud services enable compute.googleapis.com storage.googleapis.com bigquery.googleapis.com aiplatform.googleapis.com
```

Create a project with **billing linked**; set budget alerts.

---

## Week 1 — Compute & storage

| Service | AWS analog | Mini task |
|---------|------------|-----------|
| **Compute Engine** | EC2 | Create e2-micro VM, SSH in |
| **Cloud Storage (GCS)** | S3 | Upload file to bucket |
| **Cloud IAM** | IAM | Service account for apps |

### GCS upload (Python)

```python
from google.cloud import storage

client = storage.Client()
bucket = client.bucket("my-learning-bucket-unique")
blob = bucket.blob("data/hello.txt")
blob.upload_from_string("hello gcp")
print(blob.public_url)  # keep bucket private in production
```

### GCE — create VM (gcloud)

```bash
gcloud compute instances create demo-vm \
  --zone=us-central1-a \
  --machine-type=e2-micro \
  --image-family=debian-12 \
  --image-project=debian-cloud
gcloud compute ssh demo-vm --zone=us-central1-a
```

**Stop/delete** VMs when done.

---

## Week 2 — BigQuery (analytics)

Serverless warehouse — SQL on petabytes.

```sql
-- Public dataset demo
SELECT name, SUM(number) AS total
FROM `bigquery-public-data.usa_names.usa_1910_current`
WHERE state = 'CA'
GROUP BY name
ORDER BY total DESC
LIMIT 10;
```

```python
from google.cloud import bigquery

client = bigquery.Client()
query = """
SELECT corpus, COUNT(*) AS n
FROM `bigquery-public-data.samples.shakespeare`
GROUP BY corpus
LIMIT 5
"""
for row in client.query(query):
    print(row)
```

**Patterns:** partitioned tables, clustered columns, scheduled queries, IAM dataset-level access.

---

## Week 3 — Vertex AI intro

| Piece | Purpose |
|-------|---------|
| Vertex AI Workbench | Managed notebooks |
| Training | Custom or AutoML jobs |
| Endpoints | Online prediction |
| Model Garden | Pre-trained + Gemini APIs |

### Gemini text (Vertex AI SDK)

```python
import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(project="YOUR_PROJECT_ID", location="us-central1")
model = GenerativeModel("gemini-1.5-flash")
response = model.generate_content("What is BigQuery in one sentence?")
print(response.text)
```

Enable **Vertex AI API** and billing. For production RAG, use **Vector Search** + embedding models (see [RAG Production Guide](../ai_ml/RAG-PRODUCTION-GUIDE.md)).

---

## Week 4 — Networking & security (essentials)

| Topic | GCP |
|-------|-----|
| VPC | Custom VPC + subnets per region |
| Firewall | VPC firewall rules (not security groups) |
| Load balancing | HTTP(S) LB + backend services |
| Secrets | Secret Manager |
| KMS | Customer-managed encryption keys |

**Rule:** Default deny; use service accounts per workload; no JSON keys in git.

---

## AWS ↔ GCP cheat sheet

| Need | AWS | GCP |
|------|-----|-----|
| VM | EC2 | Compute Engine |
| Object store | S3 | GCS |
| IAM | IAM roles | Service accounts + IAM |
| K8s | EKS | GKE |
| Serverless fn | Lambda | Cloud Functions |
| Data warehouse | Redshift | BigQuery |
| ML | SageMaker | Vertex AI |
| GenAI API | Bedrock | Vertex AI (Gemini) |

---

## Practice project

**Batch ML on GCP:** CSV in GCS → BigQuery table → train sklearn in Workbench → export model to GCS → optional Vertex endpoint.

---

## Next steps

| Resource | Link |
|----------|------|
| Full cloud path | [CLOUD-ZERO-TO-HERO.md](./CLOUD-ZERO-TO-HERO.md) |
| AWS ML | [AWS-ML-GENAI-ZERO-TO-HERO.md](./AWS-ML-GENAI-ZERO-TO-HERO.md) |
| Data pipelines | [Data Engineering Zero to Hero](../big-data-analytics/Data-Engineering-Zero-to-Hero.md) |
