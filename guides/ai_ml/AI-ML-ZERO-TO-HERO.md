# AI/ML & Data Science — Zero to Hero (Enterprise Path)

> **Read this first.** One ordered path: prerequisites → core ML → production → specialization → interviews.  
> Each step links to a **full guide** (theory + examples inside that file). Run every code block.

**Web app:** [All guides](https://samba425.github.io/tech-mastery-notebooks/all) → **🤖 AI/ML Zero to Hero** → follow phases top to bottom.

---

## Before you start (required)

| Step | Resource | Checkpoint |
|------|----------|------------|
| 1 | **Python Zero to Hero** → Sec. 1–5 | Can write functions, classes, read CSV |
| 2 | **Python Complete Guide** → **Sec. 11** (NumPy, Pandas, sklearn) | [Mini-project done](../PYTHON-ZERO-TO-HERO.md#phase-4--data-science-stack-weeks-78) |
| 3 | Environment below | `jupyter lab` runs |

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install numpy pandas scikit-learn matplotlib seaborn jupyter mlflow
jupyter lab
```

**Do not open Phase 1 ML guides until Sec. 11 is complete.**

**Deploy models to cloud:** After MLOps phase, see [Cloud Zero to Hero](../cloud-platforms/CLOUD-ZERO-TO-HERO.md) → Phase 4 (AWS ML & GenAI).

---

## Enterprise learning rules

| Rule | Why (production teams expect this) |
|------|-------------------------------------|
| **Reproducibility** | Fix `random_state=42`, pin `requirements.txt`, version datasets |
| **Train / validation / test** | Never tune on test; hold out test until final evaluation |
| **Pipelines** | Fit preprocessing on train only — use `sklearn.pipeline.Pipeline` |
| **Experiment tracking** | Log params, metrics, artifacts (MLflow or similar) |
| **Model cards** | Document data, limitations, metrics, and intended use |
| **Monitoring** | After deploy: drift, latency, errors (see MLOps guide) |

---

## Master timeline (16 weeks, ~2 h/day)

| Phase | Weeks | Sidebar folder | Guides (in order) |
|-------|-------|----------------|-------------------|
| **0** | Done first | Python folder | Sec. 11 + mini-project |
| **1** | 1 | Phase 1 — Core ML | **Statistics for ML** → then Feature Engineering |
| **2** | 2–6 | Phase 1 — Core ML | Feature Engineering + Build ML Models |
| **2b** | 7–8 | Phase 1 — Core ML | **PyTorch Zero to Hero** |
| **3** | 9–10 | Phase 2 — Career map | ML/DS Roadmap + Quick Reference |
| **4** | 11–14 | Phase 2 — MLOps | MLOps Production |
| **5** | 14–15 | **LLM Apps** + **RAG Production** | `LLM-APPS-ZERO-TO-HERO.md` → `RAG-PRODUCTION-GUIDE.md` |
| **6** | 15–16 | Phase 3 — Pick one | NLP **or** CV **or** AI Agents **or** Generative AI |
| **7** | Parallel | Phase 4 — Interviews | LLM + RAG interview guides |

---

## Phase 1 — Core ML (Weeks 1–8)

### Week 0–1: Statistics for ML

**Guide:** `STATISTICS-FOR-ML.md` — mean/variance, distributions, hypothesis tests, bias/variance.

**Checkpoint:** Explain train vs validation error for underfitting and overfitting on a whiteboard.

### Week 1–3: Feature Engineering

**Guide:** `Feature-Engineering-Complete-Guide.md` (Parts 1–2 first)

| Week | Learn | Enterprise practice |
|------|-------|---------------------|
| 1 | Missing values, dtypes, EDA | Data contracts, `df.info()` every time |
| 2 | Scaling, encoding, outliers | Fit scaler on **train** only |
| 3 | Feature selection, pipelines | `Pipeline` + `ColumnTransformer` |

**Minimal example (fit on train only):**

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

df = pd.read_csv("data.csv")
X = df.drop(columns=["target"])
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

pipe = Pipeline([
    ("scale", StandardScaler()),
    ("clf", LogisticRegression(max_iter=1000, random_state=42)),
])
pipe.fit(X_train, y_train)
print(classification_report(y_test, pipe.predict(X_test)))
```

**Project:** Clean **3** real datasets; save one `preprocessing.py` module.

- [ ] Phase 1.1 complete — date: __________

---

### Week 4–8: Build ML Models

**Guide:** `Build-ML-Models-From-Scratch-Complete-Guide.md`

| Week | Learn | Project |
|------|-------|---------|
| 4 | Linear & logistic regression | Implement + sklearn compare |
| 5 | Trees, forests, boosting | Tabular classifier benchmark |
| 6 | Neural nets basics | MNIST or tabular MLP |
| 7–8 | CNN/RNN intro (as per guide) | One deep learning mini-project |

**Checkpoint**

- [ ] Explain bias–variance in your own words  
- [ ] Train vs validation vs test — when to use each  
- [ ] One model saved with `joblib` or MLflow  

---

## Phase 2 — Roadmap & reference (Weeks 9–10)

| Order | Guide | Use |
|-------|-------|-----|
| 1 | `MASTER-ML-DS-COMPLETE-ROADMAP.md` | Career plan, portfolio ideas |
| 2 | `ML-DS-QUICK-REFERENCE-CHEATSHEET.md` | Keep open while coding |

**Choose specialization** for Phase 3 (one only):

| Track | Guide | Best for |
|-------|-------|----------|
| **A** General ML engineer | MLOps heavy + tabular projects | Most job listings |
| **B** NLP / LLM | `NLP-Complete-Guide.md` | Text, chatbots, RAG roles |
| **C** Computer Vision | `Computer-Vision-Complete-Guide.md` | Vision, medical imaging |
| **D** AI Agents | `AI-Agents-Complete-Guide.md` | Agentic AI, automation |

---

## Phase 3 — MLOps & production (Weeks 11–14)

**Guide:** `MLOps-Production-Complete-Guide.md`

| Week | Topic | Deliverable |
|------|-------|-------------|
| 11 | Containerize model (`Docker`) | `Dockerfile` for inference |
| 12 | API serving (FastAPI) | `/predict` endpoint |
| 13 | MLflow or experiment tracking | Logged run with metrics |
| 14 | Monitoring basics | Health check + simple drift note |

```python
# Enterprise-style predict API sketch (expand in MLOps guide)
from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load("model.joblib")

@app.post("/predict")
def predict(features: list[float]):
    return {"prediction": model.predict([features]).tolist()}
```

**Project:** End-to-end — train → register → serve → document in README.

- [ ] Phase 3 complete — demo URL or repo: __________

---

## Phase 5 — LLM Apps (RAG, agents, observability)

**Read end-to-end:** `LLM-APPS-ZERO-TO-HERO.md` (sidebar: **LLM Apps — RAG & Agents**)

| Part | Topic |
|------|--------|
| 1–2 | RAG theory + local FAISS example |
| 3 | LangChain RAG chain |
| 4 | LangGraph workflow |
| 5–6 | Agents, ReAct, agentic patterns |
| 7 | **Langfuse** tracing |
| 8 | LlamaIndex intro |

Then open **AI Agents (full guide)** for CrewAI, production, security.

- [ ] Ran all Part 2–7 examples — date: __________

---

## Phase 6 — Specialization (Weeks 15–16, pick ONE)

Open **only one** guide in the sidebar **Phase 3 — Specialization**:

| Guide | Build this |
|-------|------------|
| NLP | Sentiment + summarization or RAG prototype |
| Computer Vision | Image classifier on real dataset |
| AI Agents | Tool-using agent with guardrails |

---

## Phase 7 — Interviews & system design

| Guide | When |
|-------|------|
| `LLM-Interview-Questions-Complete.md` | 2 weeks before LLM interviews |
| `RAG-Interview-Questions-Complete.md` | With any RAG portfolio project |
| `LEARNING-ORDER-GUIDE.md` | Extra detail on 5 career paths |
| Python **System Design Practice Track** | ML system design (feature stores, serving) |

**Weekly drill:** 5 interview questions + 1 whiteboard system (data + model + serving).

---

## Portfolio gate (job-ready)

- [ ] **3** GitHub projects (clean data → model → API or app)  
- [ ] README with metrics, limitations, how to reproduce  
- [ ] `LEARNING-CHECKPOINTS.md` → AI/ML Engineer (G4) checked  
- [ ] Can explain one project for 10 minutes without slides  

---

## If you get stuck

| Problem | Action |
|---------|--------|
| Lost in sidebar | Stay in **Phase 1 → Feature Engineering** only |
| Leakage / too good accuracy | Separate test set; check target in features |
| Deployment fear | MLOps guide Week 11–12 only until API works |
| Too many topics | One specialization in Phase 4, not all three |

---

## Detailed paths (optional)

For **Agents**, **NLP-only**, or **20-week** schedules, see `LEARNING-ORDER-GUIDE.md` — same order, more week-by-week detail.

---

**Start Phase 1 today:** Sidebar → **Phase 1 — Core ML** → **1. Feature Engineering** → Part 1, Section 1.
