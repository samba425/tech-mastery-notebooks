# Cloud Platforms — Zero to Hero

> **Read this first.** One ordered path: AWS fundamentals → certifications → Azure → ML on AWS → GCP → data engineering.  
> Each step links to a **full guide** already in this repo. Run every hands-on example in the linked guide.

**Web app:** Sidebar → **☁️ Cloud Zero to Hero** → follow phases top to bottom.

---

## Before you start

| Step | Resource | Checkpoint |
|------|----------|------------|
| 1 | Linux CLI basics | Can `ssh`, use `curl`, read logs |
| 2 | Networking basics | Know IP, DNS, HTTP, TLS |
| 3 | Optional: Docker | Can build/run a container |

```bash
# Free-tier AWS account — use a dedicated email, enable MFA on root, then use IAM users daily
aws --version   # install AWS CLI v2
aws configure   # access key for IAM user (not root)
```

---

## Master timeline (12 weeks, ~1.5 h/day)

| Phase | Weeks | Focus | Guides (in order) |
|-------|-------|-------|-------------------|
| **1** | 1–3 | AWS core services | [AWS Cloud Zero to Hero](./aws-cloud-zero-to-hero.md) |
| **2** | 4–6 | AWS certifications | [Cert index](./README-AWS-Certifications.md) → CLF → SAA |
| **3** | 7–8 | Azure | [Azure Cloud Zero to Hero](./azure-cloud-zero-to-hero.md) |
| **4** | 9–10 | ML & GenAI on AWS | [AWS ML & GenAI](./AWS-ML-GENAI-ZERO-TO-HERO.md) |
| **5** | 10–11 | GCP | [GCP Cloud Zero to Hero](./GCP-CLOUD-ZERO-TO-HERO.md) |
| **6** | 11–12 | Data at scale | [Data Engineering Zero to Hero](../big-data-analytics/Data-Engineering-Zero-to-Hero.md) |

**AI/ML engineers:** After Phase 1, you may jump to Phase 4, then return to certs.

---

## Phase 1 — AWS fundamentals (Weeks 1–3)

**Guide:** `aws-cloud-zero-to-hero.md`

| Week | Services | Hands-on checkpoint |
|------|----------|---------------------|
| 1 | IAM, S3, EC2 | Create bucket, launch t3.micro, SSH in |
| 2 | VPC, RDS, ELB | Private subnet + public ALB sketch |
| 3 | Lambda, CloudWatch, SNS/SQS | Hello Lambda + alarm on errors |

### Mini example — S3 upload (CLI)

```bash
aws s3 mb s3://my-learning-bucket-$(date +%s) --region us-east-1
echo "hello cloud" > hello.txt
aws s3 cp hello.txt s3://YOUR_BUCKET/hello.txt
aws s3 ls s3://YOUR_BUCKET/
```

### Mini example — IAM least privilege (concept)

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject", "s3:PutObject"],
    "Resource": "arn:aws:s3:::my-app-data/*"
  }]
}
```

Attach policies to **roles**, not long-lived root keys.

---

## Phase 2 — AWS certification path (Weeks 4–6)

**Start:** [README-AWS-Certifications.md](./README-AWS-Certifications.md)  
**Roadmap:** [AWS Certification Roadmap](../../docs/aws-certification-roadmap.md)

| Order | Exam / guide | When |
|-------|--------------|------|
| 1 | [Cloud Practitioner (CLF-C02)](./AWS-Cloud-Practitioner-Complete-Guide.md) | First cert — vocabulary |
| 2 | [Solutions Architect (SAA-C03)](./AWS-Solutions-Architect-Associate-Guide.md) | Design patterns |
| 3 | [SAA-C03 Solutions Q&A](./AWS_SAA-C03_Solutions.md) | Practice exams |
| 4 | [Exam Quick Reference](./AWS-Exam-Quick-Reference-Cheatsheet.md) | 48h before exam |

**Study rule:** 70% practice questions, 30% reading. Draw one architecture diagram per day.

---

## Phase 3 — Azure (Weeks 7–8)

**Guide:** [azure-cloud-zero-to-hero.md](./azure-cloud-zero-to-hero.md)

| AWS | Azure (learn the mapping) |
|-----|---------------------------|
| EC2 | Virtual Machines |
| S3 | Blob Storage |
| IAM | Microsoft Entra ID + RBAC |
| Lambda | Azure Functions |
| RDS | Azure SQL / Cosmos DB |

**Checkpoint:** Deploy a static site to Blob + CDN; create one Resource Group with tags.

---

## Phase 4 — ML & GenAI on AWS (Weeks 9–10)

**Guide:** [AWS-ML-GENAI-ZERO-TO-HERO.md](./AWS-ML-GENAI-ZERO-TO-HERO.md)

Covers SageMaker training/deploy, Bedrock, S3 data lakes, IAM for ML roles.

**Pairs with:** [AI/ML Zero to Hero](../ai_ml/AI-ML-ZERO-TO-HERO.md) Phase 2 (MLOps).

---

## Phase 5 — GCP (Weeks 10–11)

**Guide:** [GCP-CLOUD-ZERO-TO-HERO.md](./GCP-CLOUD-ZERO-TO-HERO.md)

GCE, GCS, BigQuery, Vertex AI intro — completes **tri-cloud** literacy.

---

## Phase 6 — Data engineering (Weeks 11–12)

**Guide:** [Data Engineering Zero to Hero](../big-data-analytics/Data-Engineering-Zero-to-Hero.md)

| Topic | Why after cloud |
|-------|-----------------|
| S3 / GCS / ADLS | Object storage for lakes |
| IAM + networking | Secure pipelines |
| Batch vs stream | Choose EMR, Glue, Dataflow, etc. |

---

## Tri-cloud comparison (interview table)

| Concern | AWS | Azure | GCP |
|---------|-----|-------|-----|
| VMs | EC2 | Virtual Machines | Compute Engine |
| Object storage | S3 | Blob | GCS |
| Serverless compute | Lambda | Functions | Cloud Functions |
| Managed K8s | EKS | AKS | GKE |
| Data warehouse | Redshift | Synapse | BigQuery |
| ML platform | SageMaker | Azure ML | Vertex AI |
| GenAI API | Bedrock | Azure OpenAI | Vertex AI Gemini |

---

## Cost & security habits (all phases)

- **Billing:** Budget alerts on day 1; tag every resource `Project=learning`.
- **Secrets:** Secrets Manager / Key Vault / Secret Manager — never in git.
- **Network:** Private subnets for databases; no `0.0.0.0/0` on SSH.
- **Identity:** MFA on console; short-lived credentials; role assumption.

---

## What’s next

| Goal | Go to |
|------|--------|
| ML on AWS | [AWS-ML-GENAI-ZERO-TO-HERO.md](./AWS-ML-GENAI-ZERO-TO-HERO.md) |
| DevOps depth | Sidebar → DevOps (Docker, Terraform, K8s) |
| System design | [System Design Practice Track](../../system-design/SYSTEM-DESIGN-PRACTICE-TRACK.md) |
| AI/ML path | [AI-ML-ZERO-TO-HERO.md](../ai_ml/AI-ML-ZERO-TO-HERO.md) |

*Log progress in `LEARNING-CHECKPOINTS.md`.*
