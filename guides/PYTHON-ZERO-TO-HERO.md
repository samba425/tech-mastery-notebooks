# Python Zero to Hero — Everything in One Place

> **Theory + examples + practice paths — all organized here.**  
> You do **not** need to hunt across random folders. One main guide holds almost everything.

---

## Your one main book (theory + code together)

| What you need | Where it lives |
|---------------|----------------|
| **Concept explanation (theory)** | [`Python-Complete-Guide.md`](Python-Complete-Guide.md) — every section has prose *then* code |
| **Runnable examples** | Same file — code blocks under each topic (copy-paste and run) |
| **Extra runnable scripts** | [`../code-examples/python-mastery-guide.py`](../code-examples/python-mastery-guide.py) |
| **Coding challenges** | [`../programming-challenges/python.challenges.ipynb`](../programming-challenges/python.challenges.ipynb) |
| **40-hour course style** | [`../pythonclass/Part1_Python_Fundamentals_Hours_1-10.md`](../pythonclass/Part1_Python_Fundamentals_Hours_1-10.md) (optional) |
| **Progress tracking** | [`../LEARNING-CHECKPOINTS.md`](../LEARNING-CHECKPOINTS.md) |
| **AI/ML after Python basics** | [`PYTHON-AIML-PATH.md`](PYTHON-AIML-PATH.md) |

**In the web app:** open **Python Zero to Hero (All-in-One)** → then **Python Complete Guide**.

---

## What “theory + example” looks like in the guide

Every major section follows this pattern:

1. **Concept** — what it is and when to use it  
2. **Code example** — working Python you can run  
3. **Common patterns** — interview / real-world usage  

Example from Section 1 (Fundamentals):

- Theory: variables, types, dynamic typing  
- Example: `integer_var = 42`, `type()`, `isinstance()`  
- More: string methods, f-strings, type conversion  

**29 sections** from beginner → expert (see table below).

---

## Zero to Hero roadmap (10 weeks, 2 hours/day)

### Weeks 1–2 — Foundations

| Read in guide | Theory topics | Practice |
|---------------|---------------|----------|
| §1 | Variables, types, strings | 5 mini scripts |
| §2 | Lists, dicts, sets, tuples | 5 list/dict exercises |
| §3 | `if`, loops, `break`/`continue` | FizzBuzz, prime checker |
| §4 | Functions, `*args`, lambdas | Refactor scripts into functions |

**Checkpoint:** Run code without syntax errors on small programs.

### Weeks 3–4 — OOP & files

| Read in guide | Theory topics | Practice |
|---------------|---------------|----------|
| §5 | Classes, inheritance, magic methods | Build `BankAccount` or `Dataset` class |
| §8 | Read/write files, JSON, CSV | Load a CSV with pure Python |
| §24 | venv, `pip`, `requirements.txt` | Create `.venv` and install packages |

**Checkpoint:** One small OOP project + read/write a JSON file.

### Weeks 5–6 — Intermediate Python

| Read in guide | Theory topics | Practice |
|---------------|---------------|----------|
| §6–§7 | Decorators, generators, modules | Package a small utility module |
| §22 | Exceptions, `try/except` | Add error handling to projects |
| §13 / §19 | `unittest`, pytest basics | Write 5 unit tests |

**Checkpoint:** 10 challenges from `python.challenges.ipynb` (easy).

### Weeks 7–8 — Data science & AI/ML stack

| Read in guide | Theory topics | Practice |
|---------------|---------------|----------|
| §11 | **NumPy, Pandas, Matplotlib, sklearn** | Section 11 mini-project |
| §11.6 | Jupyter notebooks | One EDA notebook |

**Checkpoint:** CSV → clean → features → train model (see §11.7 in guide).

**Then:** switch to [`PYTHON-AIML-PATH.md`](PYTHON-AIML-PATH.md) Phase 3 for full ML.

### Weeks 9–10 — Professional Python (pick your track)

| Track | Guide sections |
|-------|----------------|
| **Web / API** | §12, §16, §17, §18 |
| **DevOps** | §24, §27 |
| **Interview depth** | §9, §21, §28 |
| **All-round** | §15, §20, §23, §25 |

---

## Full section map (theory + examples in one file)

| § | Topic | Level |
|---|--------|-------|
| 1 | Python fundamentals | Beginner |
| 2 | Data structures | Beginner |
| 3 | Control flow | Beginner |
| 4 | Functions | Beginner |
| 5 | OOP | Intermediate |
| 6 | Advanced features (decorators, generators) | Intermediate |
| 7 | Modules & packages | Intermediate |
| 8 | File operations | Intermediate |
| 9 | Algorithms | Intermediate |
| 10 | Concurrency | Advanced |
| 11 | **NumPy, Pandas, ML stack** | AI/ML |
| 12 | Web (Flask) | Web |
| 13–19 | Testing, advanced, FastAPI, DB | Professional |
| 20–29 | Types, interviews, regex, venv, Docker, patterns | Expert |

---

## Practice lab (use after each week)

Do these in order — they **supplement** the guide, not replace it:

1. **Type along** — every code block in the section you read today  
2. **Modify** — change one example (different numbers, add a feature)  
3. **Challenges** — `programming-challenges/python.challenges.ipynb`  
4. **Script bank** — `code-examples/python-mastery-guide.py` for longer examples  
5. **Mark done** — `LEARNING-CHECKPOINTS.md` → Python guide section  

---

## AI/ML learners — shortest path

You still use **this same guide** for Python; you do not need a different book.

```
PYTHON-ZERO-TO-HERO.md (you are here — map)
    ↓
Python-Complete-Guide.md §1–§5  (theory + examples)
    ↓
Python-Complete-Guide.md §11   (NumPy, Pandas, sklearn)
    ↓
PYTHON-AIML-PATH.md Phase 3      (ML guides)
    ↓
LEARNING-CHECKPOINTS.md          (track)
```

---

## Setup once

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install numpy pandas matplotlib scikit-learn jupyter pytest
jupyter lab
```

---

## FAQ

**Is NumPy and Pandas included?**  
Yes — **Section 11** in `Python-Complete-Guide.md` (theory + full examples).

**Do I need other Python files?**  
No for learning. Optional: challenges notebook + `python-mastery-guide.py` for extra practice.

**Is this enough for zero to hero?**  
Yes for **Python language + data science basics**. For **jobs in ML**, continue with `guides/ai_ml/` after §11.

**How do I use the UI?**  
Sidebar → **Python Zero to Hero** → open sections in **Python Complete Guide** → check off **Learning Checkpoints**.

---

**Start now:** Open [`Python-Complete-Guide.md`](Python-Complete-Guide.md) → Section 1 → code every example for 60 minutes.
