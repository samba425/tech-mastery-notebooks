# Python Zero to Hero — Everything in One File

> **Read only this page for the full plan.** Theory + runnable examples for Python and the **AI/ML Python stack** live in [`Python-Complete-Guide.md`](Python-Complete-Guide.md) (Sec. 1–29).  
> **Sec.** = section in that guide. Open it from the sidebar: **Complete Guide (Theory + Code)**.

**Web app:** [Tech Mastery — All guides](https://samba425.github.io/tech-mastery-notebooks/all) → **🐍 Python Zero to Hero** → **Start Here — Full Path** (this page).

---

## How to learn (do not skip)

| Step | Action |
|------|--------|
| 1 | Read the **theory** line for the step below |
| 2 | Open **Complete Guide** at that **Sec.** and run **every** code block |
| 3 | Do the **practice** for that week |
| 4 | Check the box in **Learning Checkpoints** (sidebar top) |

---

## Master roadmap (all tracks)

| Phase | Weeks | Topic | Where to read & code |
|-------|-------|--------|----------------------|
| 1 | 1–2 | Python syntax | Complete Guide Sec. 1–4 |
| 2 | 3–4 | OOP, files, venv | Sec. 5, 8, 24 |
| 3 | 5–6 | Decorators, errors, tests | Sec. 6–7, 22, 13, 19 |
| 4 | 7–8 | **NumPy, Pandas, sklearn** | Sec. 11 + examples below |
| 5 | 9–10 | **FastAPI**, async, DB | Sec. 12, 16, 17, 18 |
| 6 | 11–12 | Docker, logging, security | Sec. 25–27, 21, 28 |
| 7 | 13+ | **AI/ML career** | Sec. 11 + [AI/ML 4-phase](#ai-ml-4-phase-path) below + **AI/ML** sidebar folder |
| 8 | Ongoing | Job readiness | **Learning Checkpoints** |

---

## Phase 1 — Foundations (Weeks 1–2)

| Sec. | Theory (what to understand) | Practice |
|------|----------------------------|----------|
| Sec. 1 | Types, variables, strings, f-strings | 5 mini scripts |
| Sec. 2 | list, dict, set, tuple, comprehensions | 5 list/dict exercises |
| Sec. 3 | `if`, `for`, `while`, `break`/`continue` | FizzBuzz, prime checker |
| Sec. 4 | Functions, `*args`, `**kwargs`, lambdas | Refactor scripts into functions |

**Done when:** Small programs run without syntax errors.

---

## Phase 2 — OOP & files (Weeks 3–4)

| Sec. | Theory | Practice |
|------|--------|----------|
| Sec. 5 | Classes, `self`, inheritance, `__len__` / `__repr__` | `Dataset` class with `summary()` |
| Sec. 8 | Files, JSON, CSV | Load and save JSON |
| Sec. 24 | `venv`, `pip`, `requirements.txt` | Create `.venv`, install packages |

**Done when:** One OOP project + read/write JSON.

---

## Phase 3 — Professional Python (Weeks 5–6)

| Sec. | Theory | Practice |
|------|--------|----------|
| Sec. 6–7 | Decorators, generators, packages | Small utility module |
| Sec. 22 | `try` / `except`, custom errors | Error handling on a project |
| Sec. 13, 19 | `unittest`, pytest | 5 unit tests |
| — | Challenges notebook | 10 easy problems |

---

## Phase 4 — Data science stack (Weeks 7–8)

**Full theory + long examples:** Complete Guide **Sec. 11** (11.1–11.8).

### Quick theory

| Library | Role |
|---------|------|
| **NumPy** | Numeric arrays, shape, vectorized math |
| **Pandas** | Tables (CSV), cleaning, features |
| **Matplotlib** | Plots for EDA |
| **scikit-learn** | Train/test split, models, metrics |

### Minimal examples (run after reading Sec. 11)

```python
# NumPy — always check shape
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.shape, (arr - arr.mean()) / arr.std())
```

```python
# Pandas — inspect first on every dataset
import pandas as pd
df = pd.read_csv("data.csv")  # or use a sample DataFrame
print(df.head(), df.info(), df.isnull().sum())
df["age"] = df["age"].fillna(df["age"].median())
```

```python
# sklearn — first pipeline
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

X = df[["feature1", "feature2"]]
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
preds = model.predict(X_test)
print("accuracy:", accuracy_score(y_test, preds))
print("f1:", f1_score(y_test, preds, average="weighted"))
```

### Sec. 11 mini-project (required before AI/ML Phase 3)

1. CSV with ≥500 rows, ≥5 columns  
2. Pandas: nulls, 2 new features, one `groupby`  
3. NumPy: normalize one column  
4. Two plots (histogram + scatter)  
5. `RandomForestClassifier` or `LogisticRegression` + accuracy + F1  

- [ ] Mini-project repo: __________  
- [ ] Date: __________  

---

## Phase 5 — Web & FastAPI (Weeks 9–10)

| Sec. | Theory | Practice |
|------|--------|----------|
| Sec. 12 | Flask (optional) | One route + JSON response |
| Sec. 16 | `async` / `await`, asyncio | One async script |
| Sec. 17 | **FastAPI**, Pydantic, routes | CRUD API, 3 endpoints |
| Sec. 18 | SQLAlchemy, sessions | API + SQLite |

```bash
pip install fastapi uvicorn sqlalchemy pydantic
uvicorn main:app --reload
```

**Done when:** You can explain routes, validation, and run the API locally.

---

## Phase 6 — Ship code (Weeks 11–12)

| Sec. | Theory | Practice |
|------|--------|----------|
| Sec. 25 | Logging | Add logs to your API |
| Sec. 26 | Auth (JWT, hashing) | Protect one endpoint |
| Sec. 27 | Docker | `Dockerfile` + run container |
| Sec. 21, 28 | Interview patterns | 5 Python coding problems |

---

## AI/ML 4-Phase Path {#ai-ml-4-phase-path}

> **Everything for Python → AI/ML is on this page.** After Sec. 11, continue here — do not rely on a separate thin “AI/ML path” file.

| Phase | What | Read & code | Time (~2 h/day) |
|-------|------|-------------|-----------------|
| **A1** | Python for ML | Complete Guide **Sec. 1–5** | ~2 weeks |
| **A2** | NumPy, Pandas, first model | **Sec. 11** + [Phase 4 mini-project](#phase-4--data-science-stack-weeks-78) | ~2 weeks |
| **A3** | Full ML curriculum | **AI/ML & Data Science** folder (sidebar) | ~12–16 weeks |
| **A4** | Job readiness | **Learning Checkpoints** | Ongoing |

### Setup (Day 0)

```bash
python3 --version   # 3.10+
cd tech-mastery-notebooks
python -m venv .venv
source .venv/bin/activate
pip install numpy pandas matplotlib seaborn scikit-learn jupyter ipykernel pytest \
  fastapi uvicorn sqlalchemy pydantic
jupyter lab
```

---

### AI/ML Phase A1 — Syntax (Sec. 1–5)

| Week | Sec. | You should be able to |
|------|------|------------------------|
| 1 | Sec. 1–2 | Variables, lists, dicts, loops, comprehensions |
| 2 | Sec. 3–4 | Control flow, functions, lambdas |
| 2 | Sec. 5 | OOP: `Dataset` class, `__len__`, `__repr__` |

**Checkpoint A1**

- [ ] 10 small scripts without looking up syntax  
- [ ] 5 problems from **Challenges Notebook**  
- [ ] One real `class` (dataset, user, or product)  
- [ ] Date: __________  

---

### AI/ML Phase A2 — Data stack (Sec. 11)

| Week | Focus | Practice |
|------|-------|----------|
| 3 | Sec. 11.2 NumPy | Shape, broadcasting, normalize a column |
| 4 | Sec. 11.3–11.6 | Pandas EDA, plots, `train_test_split` |
| 4 | Sec. 11.7 | [Mini-project](#sec-11-mini-project-required-before-aiml-phase-3) |

**Checkpoint A2**

- [ ] Explain NumPy `shape` and broadcasting in one sentence each  
- [ ] Load CSV, fix nulls, `merge` two tables  
- [ ] Mini-project link: __________  
- [ ] Date: __________  

---

### AI/ML Phase A3 — ML Zero to Hero (after Python is solid)

**Do not start until A1 + A2 checkpoints pass.**

Open **🤖 AI/ML Zero to Hero** on [the all-guides page](https://samba425.github.io/tech-mastery-notebooks/all):

| Step | Sidebar | Guide |
|------|---------|-------|
| 1 | **Start Here — Enterprise ML Path** | `AI-ML-ZERO-TO-HERO.md` (this plan) |
| 2 | **Phase 1** → Feature Engineering | Weeks 1–3 |
| 3 | **Phase 1** → Build ML Models | Weeks 4–8 |
| 4 | **Phase 2** → Roadmap + MLOps | Weeks 9–14 |
| 5 | **Phase 3** → pick ONE track | NLP, CV, or Agents |
| 6 | **LLM Apps — RAG & Agents** | LangChain, LangGraph, Langfuse examples |
| 7 | **Phase 4** → LLM + RAG interviews | Job prep |

**16-week summary (General ML path)**

| Weeks | Guide | Project |
|-------|-------|---------|
| 1–3 | Feature Engineering | Clean 3 datasets |
| 4–5 | Build ML Models | Classifier from scratch |
| 6–8 | MASTER roadmap + quick ref | Mid-term review |
| 9–12 | MLOps | Deploy model API |
| 13–16 | Specialization + interviews | 3 portfolio projects |

**Checkpoint A3**

- [ ] **AI/ML Learning Order** read; path chosen  
- [ ] Feature engineering — one end-to-end pipeline  
- [ ] Build-models — linear + tree understood  
- [ ] MLOps — one deployment  
- [ ] 3 portfolio projects: __________  

---

### AI/ML Phase A4 — Track progress

Every week (15 min):

1. Open **Learning Checkpoints** in the sidebar  
2. Update the progress log  
3. Set two goals for next week  

**Ready to apply (G4 gate)**

- [ ] A1 + A2 complete  
- [ ] A3 core guides done  
- [ ] 3 ML projects on GitHub  
- [ ] 20 LLM/RAG interview questions self-tested  
- [ ] 3 system design L2 prompts (System Design Practice Track)  

---

## Where to click in the UI

| Goal | Sidebar item |
|------|----------------|
| This full plan | **🐍 Python Zero to Hero** → **Start Here — Full Path** |
| Theory + code per topic | **Complete Guide (Theory + Code)** |
| Extra scripts | **Code Examples** |
| Drills | **Challenges Notebook** |
| ML after Sec. 11 | **🤖 AI/ML & Data Science** (same site, separate folder) |
| Pass/fail tracking | **Learning Checkpoints** |
| PDF books | **PDF Library** (bottom of sidebar on /all) |

---

## All 29 sections (Complete Guide map)

| Sec. | Topic | Track |
|------|--------|-------|
| 1–4 | Fundamentals | Everyone |
| 5–8 | OOP, files | Everyone |
| 9–10 | Algorithms, concurrency | Advanced |
| **11** | **NumPy, Pandas, ML stack** | **AI/ML** |
| 12, 16–18 | Web, **FastAPI**, DB | Backend |
| 13, 19 | Testing | Production |
| 20–29 | Types, regex, Docker, security | Senior |

---

## If you get stuck

| Problem | Action |
|---------|--------|
| Syntax errors | Sec. 1–4 again; run every example |
| NumPy shape errors | `print(x.shape)` before every operation |
| Pandas confusion | `head()`, `info()`, `isnull().sum()` every time |
| Bad model accuracy | Check leakage, balance, train/test split |
| Too much at once | Finish Phase A1–A2 only before ML guides |

---

## FAQ

**Is AI/ML in this file?**  
Yes — [AI/ML 4-phase path](#ai-ml-4-phase-path) + Sec. 11 in the Complete Guide. Deep ML topics are in the **AI/ML** folder (too large for one page).

**Old “Python for AI/ML — 4-Phase Path” page?**  
Merged here. Use **Start Here — Full Path** only.

**JavaScript background?**  
Skim Sec. 1–4 in a few days; focus on Sec. 5, 11, 17.

---

**Start now:** **Complete Guide** → **Sec. 1** → code for 60 minutes.
