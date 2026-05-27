# Python Zero to Hero — Learn Everything Here

> **One folder, one path:** fundamentals → data science → **FastAPI** → production Python → **AI/ML**.  
> **Sec.** = section number in [`Python-Complete-Guide.md`](Python-Complete-Guide.md) (theory + runnable code in the same place).

**In the web app:** Sidebar → **🐍 Python (Zero to Hero)** → start with this page → open **Complete Guide** for each Sec.

---

## How to read this path (simplest method)

1. **Read** the Sec. in **Complete Guide** (concept, then copy the code block).
2. **Run** every example in a terminal or Jupyter.
3. **Practice** challenges when a phase says to.
4. **Check off** [`LEARNING-CHECKPOINTS.md`](../LEARNING-CHECKPOINTS.md).

You do **not** need separate theory files and example files for core Python — they are already together in the Complete Guide.

---

## Full curriculum (12–16 weeks at ~2 hours/day)

| Phase | Weeks | What you learn | Where (sidebar under Python) |
|-------|-------|----------------|------------------------------|
| **1** | 1–2 | Syntax, data structures, functions | Complete Guide Sec. 1–4 |
| **2** | 3–4 | OOP, files, virtualenv | Sec. 5, 8, 24 |
| **3** | 5–6 | Decorators, errors, testing | Sec. 6–7, 22, 13, 19 |
| **4** | 7–8 | **NumPy, Pandas, plots, sklearn** | Sec. 11 (all subsections) |
| **5** | 9–10 | **FastAPI, async, APIs, databases** | Sec. 12, 16, 17, 18 |
| **6** | 11–12 | Docker, logging, security, interviews | Sec. 25–27, 21, 28 |
| **7** | 13+ | **AI/ML career track** | AI/ML Path + ML Curriculum guides |
| **8** | Ongoing | Job readiness | Learning Checkpoints |

---

## Phase 1 — Foundations (Weeks 1–2)

| Sec. | Topics | Practice today |
|------|--------|----------------|
| Sec. 1 | Variables, types, strings | 5 mini scripts |
| Sec. 2 | Lists, dicts, sets, tuples | 5 list/dict exercises |
| Sec. 3 | `if`, loops, `break`/`continue` | FizzBuzz, prime checker |
| Sec. 4 | Functions, `*args`, lambdas | Refactor scripts into functions |

**Done when:** You can write small programs without syntax errors.

---

## Phase 2 — OOP & files (Weeks 3–4)

| Sec. | Topics | Practice today |
|------|--------|----------------|
| Sec. 5 | Classes, inheritance, magic methods | `BankAccount` or `Dataset` class |
| Sec. 8 | Files, JSON, CSV | Load a CSV with pure Python |
| Sec. 24 | `venv`, `pip`, `requirements.txt` | Create `.venv` and install packages |

**Done when:** One OOP mini-project + read/write JSON.

---

## Phase 3 — Professional Python (Weeks 5–6)

| Sec. | Topics | Practice today |
|------|--------|----------------|
| Sec. 6–7 | Decorators, generators, packages | Small utility package |
| Sec. 22 | Exceptions, `try/except` | Add error handling to a project |
| Sec. 13 / 19 | `unittest`, pytest | 5 unit tests |
| — | Challenges notebook | 10 easy problems |

**Done when:** Challenges notebook (easy section) mostly complete.

---

## Phase 4 — Data science & AI stack (Weeks 7–8) ⭐

| Sec. | Topics | Practice today |
|------|--------|----------------|
| Sec. 11 | NumPy, Pandas, Matplotlib, seaborn | Follow every code block in Sec. 11 |
| Sec. 11.4–11.6 | Plots, sklearn, Jupyter | One EDA notebook |
| Sec. 11.7 | Mini-project | CSV → clean → features → train/test split |

**Done when:** Mini-project works end-to-end. Mark Phase 2 in [`PYTHON-AIML-PATH.md`](PYTHON-AIML-PATH.md).

---

## Phase 5 — Web & FastAPI (Weeks 9–10) ⭐

| Sec. | Topics | Practice today |
|------|--------|----------------|
| Sec. 12 | Flask basics (optional) | Simple route + template |
| Sec. 16 | `async`/`await`, asyncio | One async script |
| Sec. 17 | **REST APIs & FastAPI** | CRUD API with 3 endpoints |
| Sec. 18 | SQLAlchemy, DB sessions | API + SQLite or Postgres |

**Also useful:** Part 4 teaching (Hours 31–32) in sidebar — FastAPI deep dive.

**Done when:** You can explain routes, Pydantic models, dependency injection, and run `uvicorn` locally.

```bash
pip install fastapi uvicorn sqlalchemy pydantic
# Build along with Sec. 17 in the Complete Guide
```

---

## Phase 6 — Ship code (Weeks 11–12)

| Sec. | Topics | Practice today |
|------|--------|----------------|
| Sec. 25 | Logging, structured logs | Add logging to your API |
| Sec. 26 | Auth basics (JWT, hashing) | Protect one endpoint |
| Sec. 27 | Docker, deploy | `Dockerfile` for your FastAPI app |
| Sec. 21 / 28 | Interview patterns | 5 LeetCode-style problems in Python |

**Done when:** API runs in Docker locally.

---

## Phase 7 — AI/ML (after Sec. 11) ⭐

You **keep using Python** — next step is the ML library, not a new language.

| Step | Resource (sidebar) | Goal |
|------|------------------|------|
| 1 | **AI/ML Path (4 phases)** | Confirm order: Sec. 1–5 → Sec. 11 → ML guides |
| 2 | **ML Learning Order** | Week-by-week ML curriculum |
| 3 | Build ML Models / Feature Engineering / NLP / CV / MLOps | Pick track from roadmap |
| 4 | **ML/DS Complete Roadmap** | See the full picture |

**Shortest chain:**

```
This page (map)
  → Complete Guide Sec. 1–5
  → Complete Guide Sec. 11
  → AI/ML Path
  → ML Learning Order
  → LEARNING-CHECKPOINTS
```

---

## All 29 sections in one book (quick map)

| Sec. | Topic | Best for |
|------|--------|----------|
| 1–4 | Fundamentals | Everyone |
| 5–8 | OOP, files | Everyone |
| 9–10 | Algorithms, concurrency | Interviews / advanced |
| **11** | **NumPy, Pandas, ML stack** | **AI/ML** |
| 12, 16–18 | Web, async, **FastAPI**, DB | Backend jobs |
| 13, 19 | Testing | Production teams |
| 20–29 | Types, regex, Docker, security, patterns | Senior / full-stack |

Open **Complete Guide** and use the table of contents — every Sec. has **theory then code**.

---

## Extra practice (optional, same Python folder)

| Resource | Use when |
|----------|----------|
| Code Examples (`python-mastery-guide.py`) | Longer scripts after each Sec. |
| Challenges notebook | Weekly drill |
| Teaching Parts 1–4 | Classroom-style 40-hour course |
| Live Demos (21 projects) | See full-stack patterns |

---

## Setup once

```bash
cd tech-mastery-notebooks
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install numpy pandas matplotlib seaborn scikit-learn jupyter pytest \
  fastapi uvicorn sqlalchemy pydantic
jupyter lab
```

---

## FAQ

**Sec. vs §?**  
Same meaning: **Section 1, Section 11**, etc. In tables we write **Sec. 1** so it always displays; in prose you may see § with proper styling.

**Is FastAPI included?**  
Yes — **Sec. 17** in the Complete Guide (+ Part 4 teaching hours 31–32).

**Is AI/ML included?**  
Yes — **Sec. 11** for Python + data stack; then **AI/ML Path** and **ML Learning Order** for the full career track.

**Enough for zero to hero?**  
Yes for **Python + APIs + data science basics**. For **ML engineer jobs**, finish Phase 7 guides and checkpoints.

---

**Start now:** Sidebar → **Complete Guide (Theory + Code)** → **Sec. 1** → code every example for 60 minutes.
