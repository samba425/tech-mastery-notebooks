# Python for AI/ML — Your 4-Phase Path

> **Follow these four steps in order.** Track every phase in [`LEARNING-CHECKPOINTS.md`](../LEARNING-CHECKPOINTS.md).

| Phase | What | Guide | Time (2 h/day) |
|-------|------|-------|----------------|
| **1** | Python syntax & core | `Python-Complete-Guide.md` §1–§5 | ~2 weeks |
| **2** | NumPy, Pandas, first model | `Python-Complete-Guide.md` §11 | ~2 weeks |
| **3** | Full ML curriculum | `ai_ml/LEARNING-ORDER-GUIDE.md` | ~12–16 weeks |
| **4** | Progress & job readiness | `LEARNING-CHECKPOINTS.md` | Ongoing |

---

## Setup (Day 0 — 30 minutes)

```bash
python3 --version          # need 3.10+
cd tech-mastery-notebooks
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install numpy pandas matplotlib seaborn scikit-learn jupyter ipykernel
jupyter lab
```

In the web app: open **Python for AI/ML — 4-Phase Path** (this file) and pin **Learning Checkpoints**.

---

## Phase 1 — Python guide §1–§5 (Syntax)

**Guide:** [`Python-Complete-Guide.md`](Python-Complete-Guide.md)

| Week | Sections | You should be able to |
|------|----------|------------------------|
| 1 | §1 Fundamentals, §2 Data structures | Variables, lists, dicts, loops, comprehensions |
| 2 | §3 Control flow, §4 Functions | `if/for/while`, functions, `*args`, lambdas |

### §5 Object-Oriented Programming (end of Phase 1)

| Topic | Practice |
|-------|----------|
| Classes, `__init__`, methods | Model a `Dataset` class with `rows`, `columns`, `summary()` |
| Inheritance | `TabularDataset` extends `Dataset` |
| Special methods | Implement `__len__`, `__repr__` |

### Phase 1 checkpoint — mark in `LEARNING-CHECKPOINTS.md`

- [ ] Wrote 10 small scripts without looking up syntax  
- [ ] Solved 5 list/dict problems from `programming-challenges/python.challenges.ipynb`  
- [ ] Built one `class` for a real concept (user, product, or dataset)  
- [ ] **Date completed:** __________  

**Do not start Phase 2 until all four are checked.**

---

## Phase 2 — Python guide §11 (NumPy + Pandas + mini-project)

**Guide:** [`Python-Complete-Guide.md`](Python-Complete-Guide.md) — Section 11 only (§11.1–§11.8)

| Week | Focus | Practice |
|------|-------|----------|
| 3 | §11.2 NumPy | Arrays, shape, broadcasting, normalize a column |
| 4 | §11.3–§11.6 Pandas + plots + sklearn | CSV EDA, missing values, first `train_test_split` |

### Mini-project (required)

1. Pick a dataset (Iris, Titanic, or any Kaggle CSV ≥500 rows).  
2. **Pandas:** `head`, `info`, `describe`, fix nulls, create **2 features**, one `groupby`.  
3. **NumPy:** normalize one numeric column with `(x - mean) / std`.  
4. **Plot:** one histogram + one scatter.  
5. **sklearn:** `LogisticRegression` or `RandomForestClassifier`, report accuracy + F1 or ROC-AUC.  

Save notebook or script in a GitHub repo.

### Phase 2 checkpoint — mark in `LEARNING-CHECKPOINTS.md`

- [ ] Can explain NumPy `shape` and broadcasting in one sentence each  
- [ ] Can load CSV, handle nulls, and `merge` two tables  
- [ ] Mini-project repo link: __________  
- [ ] **Date completed:** __________  

**Do not start Phase 3 until mini-project is done.**

---

## Phase 3 — `ai_ml/LEARNING-ORDER-GUIDE.md`

**Guide:** [`ai_ml/LEARNING-ORDER-GUIDE.md`](ai_ml/LEARNING-ORDER-GUIDE.md)

Read the full file once, then follow **Path 1: Complete Beginner → ML Engineer** (or your chosen specialization).

### Recommended order after Phase 2

| Order | Guide | Outcome |
|-------|-------|---------|
| 1 | `Feature-Engineering-Complete-Guide.md` | Production-quality tabular pipelines |
| 2 | `Build-ML-Models-From-Scratch-Complete-Guide.md` | Understand models beyond sklearn API |
| 3 | `MLOps-Production-Complete-Guide.md` | Deploy one model as API |
| 4 | Pick one: `NLP-Complete-Guide.md`, `Computer-Vision-Complete-Guide.md`, or `AI-Agents-Complete-Guide.md` | Specialization |
| 5 | `LLM-Interview-Questions-Complete.md` + `RAG-Interview-Questions-Complete.md` | Interview prep |

### Phase 3 checkpoint — mark in `LEARNING-CHECKPOINTS.md`

- [ ] `LEARNING-ORDER-GUIDE.md` read; path chosen (General / Agents / NLP / CV / MLOps)  
- [ ] Feature engineering guide — one end-to-end pipeline  
- [ ] Build-models guide — at least linear + tree model understood  
- [ ] MLOps guide — one deployment  
- [ ] **3 portfolio projects** listed: __________  

---

## Phase 4 — Track in `LEARNING-CHECKPOINTS.md`

**Guide:** [`LEARNING-CHECKPOINTS.md`](../LEARNING-CHECKPOINTS.md)

### Weekly habit (15 minutes every Sunday)

1. Open `LEARNING-CHECKPOINTS.md`.  
2. Update the **Progress Log** at the bottom.  
3. Check one folder section (guides, system-design, challenges, etc.).  
4. Set **two goals** for the coming week.

### AI/ML “ready to apply” (G4) — final gate

From `LEARNING-CHECKPOINTS.md` → **AI/ML Engineer (G4)**:

- [ ] Phase 1 + Phase 2 complete (this path)  
- [ ] Phase 3 core guides done  
- [ ] 3 ML projects on GitHub  
- [ ] 20 LLM/RAG interview questions self-tested  
- [ ] 3 system design L2 prompts (`SYSTEM-DESIGN-PRACTICE-TRACK.md`)  

---

## Quick reference — where to click in the UI

| Step | Sidebar item |
|------|----------------|
| Full map (theory + examples) | **Python Zero to Hero (All-in-One)** |
| This path | **Python for AI/ML — 4-Phase Path** |
| Phase 1 & 2 | **Python Complete Guide** |
| Phase 3 | **AI/ML Learning Order** (under AI/ML) |
| Phase 4 | **Learning Checkpoints (All Folders)** |
| PDFs | **PDF Library** |

---

## If you get stuck

| Problem | Action |
|---------|--------|
| Syntax errors | Re-read §1–§4, run every example in the guide |
| NumPy shape errors | Print `.shape` on every array before operations |
| Pandas confusion | `df.head()`, `df.info()`, `df.isnull().sum()` every time |
| Model bad accuracy | Check leakage, class balance, train/test split |
| Overwhelmed | Stay on Phase 1–2 only until checkpoints pass |

---

**Start today:** Phase 1, §1 — open `Python-Complete-Guide.md` and code along for 60 minutes.
