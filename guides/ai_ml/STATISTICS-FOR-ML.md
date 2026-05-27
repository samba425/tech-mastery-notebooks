# Statistics for Machine Learning

> **Read before Feature Engineering.** Short primer: distributions, inference, bias/variance.  
> Every example uses NumPy/Pandas — no heavy math proofs.

**Path:** [AI/ML Zero to Hero](./AI-ML-ZERO-TO-HERO.md) → Phase 1 (first item).

---

## Why ML needs statistics

| Question | Statistical tool |
|----------|-------------------|
| Is this feature related to the target? | Correlation, chi-square |
| Did model A beat model B? | Confidence intervals, hypothesis tests |
| Why did test error jump? | Distribution shift, variance |
| How much data do I need? | Sample size, power (intuition) |

---

## 1. Descriptive statistics

```python
import numpy as np
import pandas as pd

x = np.array([12, 15, 14, 10, 18, 22, 11, 13, 16, 14])
print("mean", x.mean())
print("std (sample)", x.std(ddof=1))
print("median", np.median(x))
print("IQR", np.percentile(x, 75) - np.percentile(x, 25))
```

| Measure | Use in ML |
|---------|-----------|
| Mean | Center of feature; sensitive to outliers |
| Median | Robust center for skewed data |
| Std / IQR | Scaling, outlier detection |
| Correlation | Feature redundancy (|r| > 0.9 → consider drop) |

```python
df = pd.DataFrame({"age": [25, 30, 35, 40, 45], "income": [50, 55, 60, 70, 90]})
print(df.corr(numeric_only=True))
```

---

## 2. Probability distributions

### Normal (Gaussian)

Many errors and aggregated features are **approximately** normal (Central Limit Theorem intuition).

```python
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
samples = rng.normal(loc=0, scale=1, size=10_000)
plt.hist(samples, bins=50, density=True)
plt.title("Standard normal samples")
plt.show()
```

### Bernoulli / Binomial

- **Bernoulli:** one trial (click / no click) → binary classification labels  
- **Binomial:** n Bernoulli trials → count of positives

### Poisson

Counts per interval (events per hour) → regression with Poisson loss.

**Rule:** Match loss function to data type (MSE for continuous, log-loss for probabilities, Poisson for counts).

---

## 3. Sampling & train/test thinking

```python
from sklearn.model_selection import train_test_split

# Stratify for classification — keep class proportions
y = [0, 0, 0, 1, 1, 1, 1, 1]
idx = np.arange(len(y))
train_idx, test_idx = train_test_split(idx, test_size=0.25, stratify=y, random_state=42)
```

| Mistake | Fix |
|---------|-----|
| Tune on test set | Hold out **validation**; test once at end |
| Leak future into past | Time-based split for time series |
| Small test set | High variance in metric — use CV |

---

## 4. Hypothesis testing (practical)

**Question:** Is mean revenue different between groups A and B?

```python
from scipy import stats

a = rng.normal(100, 15, size=200)
b = rng.normal(105, 15, size=200)
t_stat, p_value = stats.ttest_ind(a, b, equal_var=False)
print(f"p-value: {p_value:.4f}")
```

| p-value | Plain English |
|---------|---------------|
| &lt; 0.05 | Unlikely if groups were same — **evidence of difference** (not proof) |
| ≥ 0.05 | Not enough evidence to claim difference |

**A/B tests in ML products:** define metric, sample size, run test, check practical significance (not only p-value).

---

## 5. Bias–variance tradeoff

```
High bias (underfitting):     model too simple → high train AND test error
High variance (overfitting):  model too complex → low train, high test error
```

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

X = rng.normal(size=(500, 5))
y = (X[:, 0] + X[:, 1] > 0).astype(int)

for depth in [1, 3, 20]:
    clf = DecisionTreeClassifier(max_depth=depth, random_state=42)
    scores = cross_val_score(clf, X, y, cv=5)
    print(f"depth={depth:2d}  CV accuracy mean={scores.mean():.3f}  std={scores.std():.3f}")
```

**Fix underfitting:** more features, complex model, less regularization  
**Fix overfitting:** more data, regularization, simpler model, dropout (neural nets)

---

## 6. Confidence intervals (metrics)

```python
# Bootstrap CI for accuracy
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=500).fit(X[:400], y[:400])
acc = accuracy_score(y[400:], model.predict(X[400:]))
boot = []
for _ in range(500):
    idx = rng.integers(0, 100, size=100)
    boot.append(accuracy_score(y[400:][idx], model.predict(X[400:][idx])))
print("accuracy", acc, "95% CI", np.percentile(boot, [2.5, 97.5]))
```

Report **metric ± uncertainty** in model cards.

---

## 7. Checklist before Feature Engineering

- [ ] EDA: histograms, missing %, class balance  
- [ ] Correlation matrix for numeric features  
- [ ] Chose train/val/test split appropriate to problem  
- [ ] Understand bias/variance symptoms on learning curves  
- [ ] Know which distribution your target follows  

**Next:** [Feature Engineering Complete Guide](./Feature-Engineering-Complete-Guide.md)

---

## Further reading (in repo)

| Topic | Guide |
|-------|-------|
| Full ML path | [AI-ML-ZERO-TO-HERO.md](./AI-ML-ZERO-TO-HERO.md) |
| Build models | [Build ML Models From Scratch](./Build-ML-Models-From-Scratch-Complete-Guide.md) |
| Deep learning | [PyTorch Zero to Hero](./PYTORCH-ZERO-TO-HERO.md) |
