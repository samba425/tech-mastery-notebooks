# 🚀 ML/DS Quick Reference Cheat Sheet
## Everything You Need at a Glance

---

## 📊 Algorithm Selection Flowchart

```
┌─────────────────────────────────────────┐
│ What type of problem do you have?      │
└──────────────┬──────────────────────────┘
               │
       ┌───────┴───────┐
       │               │
    SUPERVISED    UNSUPERVISED
       │               │
   ┌───┴───┐       ┌───┴───┐
   │       │       │       │
REGRESS CLASSIFY CLUSTER REDUCE
   │       │       │       │
   ▼       ▼       ▼       ▼

REGRESSION:           CLASSIFICATION:        CLUSTERING:         DIM REDUCTION:
├─ Linear             ├─ Logistic            ├─ K-Means          ├─ PCA
├─ Ridge/Lasso        ├─ Decision Tree       ├─ DBSCAN           ├─ t-SNE
├─ Decision Tree      ├─ Random Forest       ├─ Hierarchical     ├─ LDA
├─ Random Forest      ├─ SVM                 └─ GMM              └─ Autoencoder
├─ XGBoost            ├─ Neural Network
├─ Neural Network     ├─ Naive Bayes
└─ SVR                └─ KNN
```

---

## 🎯 Quick Decision Matrix

| Scenario | Best Algorithm | Why? |
|----------|---------------|------|
| Small dataset (<1K samples) | Logistic Regression, Naive Bayes | Simple, less overfitting |
| Large dataset (>100K samples) | Neural Networks, XGBoost | Can learn complex patterns |
| Need interpretability | Decision Tree, Linear models | Easy to explain |
| High dimensional data | Regularized models, PCA first | Handles many features |
| Imbalanced classes | XGBoost, SMOTE + RF | Handle class imbalance well |
| Text data | Naive Bayes, LSTM, Transformers | Designed for sequences |
| Image data | CNN, Vision Transformers | Spatial patterns |
| Time series | ARIMA, LSTM, Prophet | Temporal dependencies |
| Real-time prediction | Simple models, XGBoost | Low latency |
| Non-linear relationships | SVM, Random Forest, Neural Networks | Capture non-linearity |

---

## 📐 Essential Formulas

### **Linear Regression**
```
ŷ = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
Loss (MSE) = (1/n) Σ(y - ŷ)²
Gradient: dL/dw = (2/n) X^T(ŷ - y)
Update: w = w - α·dL/dw
```

### **Logistic Regression**
```
z = wx + b
ŷ = σ(z) = 1/(1 + e^(-z))
Loss (BCE) = -[y·log(ŷ) + (1-y)·log(1-ŷ)]
```

### **Entropy & Information Gain**
```
Entropy: H(S) = -Σ pᵢ·log₂(pᵢ)
Information Gain: IG = H(parent) - Σ(wᵢ·H(childᵢ))
```

### **Backpropagation**
```
Forward: a = σ(w·x + b)
Loss: L = (y - a)²
Backward: dL/dw = dL/da · da/dz · dz/dw
         = 2(a-y) · σ'(z) · x
```

### **Common Metrics**
```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
Precision = TP / (TP + FP)
Recall = TP / (TP + FN)
F1 = 2 · (Precision · Recall) / (Precision + Recall)
```

---

## 🔧 Feature Engineering Cheat Sheet

### **Handling Missing Values**

| Method | When to Use | Formula |
|--------|-------------|---------|
| **Drop** | <5% missing | `df.dropna()` |
| **Mean** | Normal distribution | `df.fillna(df.mean())` |
| **Median** | Skewed/outliers | `df.fillna(df.median())` |
| **Mode** | Categorical | `df.fillna(df.mode()[0])` |
| **Forward Fill** | Time series | `df.fillna(method='ffill')` |
| **KNN** | Complex patterns | `KNNImputer(n_neighbors=5)` |

### **Handling Outliers**

| Method | Formula | When to Use |
|--------|---------|-------------|
| **IQR** | Q1-1.5×IQR, Q3+1.5×IQR | Default choice |
| **Z-score** | \|z\| > 3 | Normal distribution |
| **Remove** | Delete rows | <1% outliers |
| **Cap** | Clip to bounds | Valid but extreme |
| **Transform** | log, sqrt | Reduce impact |

### **Feature Scaling**

| Method | Formula | Use Case |
|--------|---------|----------|
| **Standardization** | (x - μ) / σ | Normal dist, Most ML |
| **Min-Max** | (x - min) / (max - min) | Neural networks, [0,1] needed |
| **Robust** | (x - median) / IQR | Has outliers |
| **Log** | log(x + 1) | Skewed data |

### **Encoding Categorical**

| Cardinality | Method | Example |
|-------------|--------|---------|
| **Binary (2)** | Label Encoding | Male=0, Female=1 |
| **Low (3-10)** | One-Hot Encoding | Color → [is_red, is_blue, is_green] |
| **Medium (11-50)** | Target Encoding | Category → mean(target) for that category |
| **High (>50)** | Frequency/Hash | Category → frequency or hash value |

---

## 🧠 Neural Network Quick Guide

### **Activation Functions**

| Function | Formula | Range | Use Case |
|----------|---------|-------|----------|
| **Sigmoid** | 1/(1+e^(-x)) | (0, 1) | Output layer (binary) |
| **Tanh** | (e^x - e^(-x))/(e^x + e^(-x)) | (-1, 1) | Hidden layers |
| **ReLU** | max(0, x) | [0, ∞) | Hidden layers (default) |
| **Leaky ReLU** | max(0.01x, x) | (-∞, ∞) | Fix dying ReLU |
| **Softmax** | e^xi / Σe^xj | (0, 1), sum=1 | Output (multi-class) |

### **Loss Functions**

| Problem Type | Loss Function | Formula |
|--------------|---------------|---------|
| **Regression** | MSE | (1/n)Σ(y-ŷ)² |
| **Regression (robust)** | MAE | (1/n)Σ\|y-ŷ\| |
| **Binary Classification** | Binary Cross-Entropy | -[y·log(ŷ) + (1-y)·log(1-ŷ)] |
| **Multi-class** | Categorical Cross-Entropy | -Σy·log(ŷ) |
| **SVM** | Hinge Loss | max(0, 1 - y·ŷ) |

### **Optimizers Comparison**

| Optimizer | Learning Rate | Speed | Memory | Use Case |
|-----------|---------------|-------|--------|----------|
| **SGD** | 0.01-0.1 | Fast | Low | Simple problems |
| **SGD + Momentum** | 0.01-0.1 | Medium | Low | Faster than SGD |
| **AdaGrad** | 0.01 | Medium | Medium | Sparse data |
| **RMSprop** | 0.001 | Medium | Medium | RNNs |
| **Adam** | 0.001 | Fast | High | Default choice! |

### **Network Architecture Rules**

```
Input Layer:  Number of features
Hidden Layers: 
  - Start with 1-2 layers
  - Each layer: 2x to input_size
  - More layers for complex problems
  - Use dropout (0.2-0.5) between layers
Output Layer:
  - Regression: 1 neuron, linear activation
  - Binary: 1 neuron, sigmoid activation  
  - Multi-class: n neurons, softmax activation
```

---

## 🎨 Deep Learning Architectures

### **CNN Layers**

| Layer | Purpose | Typical Values |
|-------|---------|----------------|
| **Conv2D** | Feature extraction | filters=32/64/128, kernel=3×3 |
| **MaxPool2D** | Downsampling | pool_size=2×2 |
| **Dropout** | Regularization | rate=0.25-0.5 |
| **Dense** | Classification | units=128/256/512 |
| **BatchNorm** | Stabilize training | After Conv/Dense |

**Typical CNN Architecture:**
```
Input (224×224×3)
  ↓
Conv2D(32, 3×3) → ReLU → MaxPool(2×2)
  ↓
Conv2D(64, 3×3) → ReLU → MaxPool(2×2)
  ↓
Conv2D(128, 3×3) → ReLU → MaxPool(2×2)
  ↓
Flatten
  ↓
Dense(256) → ReLU → Dropout(0.5)
  ↓
Dense(num_classes) → Softmax
```

### **RNN/LSTM Use Cases**

| Architecture | Use Case | Why? |
|--------------|----------|------|
| **Vanilla RNN** | Short sequences (<10 steps) | Simple, fast |
| **LSTM** | Long sequences, text, time series | Handles long dependencies |
| **GRU** | Similar to LSTM but faster | Good tradeoff |
| **Bidirectional** | Context from both directions | Better understanding |
| **Seq2Seq** | Translation, summarization | Input seq → output seq |

### **Transformer Concepts**

```
Self-Attention:
  Q = Query (what I'm looking for)
  K = Key (what I contain)
  V = Value (what I output)
  
  Attention(Q,K,V) = softmax(QK^T/√d)V

Use: NLP, Vision, Multi-modal
Advantages: Parallel, long-range, interpretable
Disadvantages: Memory intensive, needs more data
```

---

## 📊 Evaluation Metrics Guide

### **Classification Metrics**

```
Confusion Matrix:
                Predicted
              Pos    Neg
Actual  Pos   TP     FN
        Neg   FP     TN

Accuracy = (TP+TN) / Total        [Overall correctness]
Precision = TP / (TP+FP)          [Of predicted positive, how many correct?]
Recall = TP / (TP+FN)             [Of actual positive, how many found?]
F1 = 2·P·R / (P+R)                [Harmonic mean of P and R]
```

**When to Use What:**
- **Accuracy**: Balanced classes
- **Precision**: Cost of false positive high (spam detection)
- **Recall**: Cost of false negative high (disease detection)
- **F1**: Imbalanced classes
- **ROC-AUC**: Overall model quality

### **Regression Metrics**

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **MAE** | (1/n)Σ\|y-ŷ\| | Average error (same units as y) |
| **MSE** | (1/n)Σ(y-ŷ)² | Penalizes large errors more |
| **RMSE** | √MSE | Same units as y, popular |
| **R²** | 1 - (SS_res/SS_tot) | % variance explained (0-1) |
| **MAPE** | (100/n)Σ\|y-ŷ\|/\|y\| | % error, easy to interpret |

---

## 🔍 Debugging ML Models

### **Common Problems & Solutions**

| Problem | Symptoms | Solutions |
|---------|----------|-----------|
| **Underfitting** | Low train & test accuracy | • More features<br>• More complex model<br>• Less regularization<br>• Train longer |
| **Overfitting** | High train, low test accuracy | • More data<br>• Regularization (L1/L2)<br>• Dropout<br>• Simpler model<br>• Early stopping |
| **Vanishing Gradient** | NN not learning | • ReLU activation<br>• Batch normalization<br>• Skip connections<br>• Better initialization |
| **Exploding Gradient** | NaN/Inf losses | • Gradient clipping<br>• Lower learning rate<br>• Batch normalization |
| **Slow Training** | Takes too long | • Smaller model<br>• Larger batch size<br>• Better optimizer (Adam)<br>• GPU/TPU |
| **Poor Convergence** | Loss oscillates | • Lower learning rate<br>• LR schedule<br>• Better optimizer<br>• Normalize inputs |

### **Training Checklist**

```
Before Training:
☑ Normalize/scale features
☑ Check for data leakage
☑ Split data properly (train/val/test)
☑ Handle class imbalance
☑ Set random seed for reproducibility

During Training:
☑ Monitor train & validation loss
☑ Check for overfitting
☑ Visualize predictions
☑ Log metrics
☑ Save checkpoints

After Training:
☑ Evaluate on test set
☑ Analyze errors
☑ Check feature importance
☑ Try ensembling
☑ Document everything
```

---

## 💻 Code Snippets

### **Quick Data Preprocessing**

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load data
df = pd.read_csv('data.csv')

# Handle missing values
df['numeric_col'].fillna(df['numeric_col'].median(), inplace=True)
df['categorical_col'].fillna(df['categorical_col'].mode()[0], inplace=True)

# Remove outliers (IQR method)
Q1 = df['numeric_col'].quantile(0.25)
Q3 = df['numeric_col'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['numeric_col'] >= Q1 - 1.5*IQR) & (df['numeric_col'] <= Q3 + 1.5*IQR)]

# Encode categorical
le = LabelEncoder()
df['categorical_col'] = le.fit_transform(df['categorical_col'])

# Split data
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### **Quick Model Training**

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate
y_pred = model.predict(X_test_scaled)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Feature importance
importance = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)
print(importance)
```

### **Quick Neural Network (Keras)**

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Build model
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')  # Binary classification
])

# Compile
model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train
history = model.fit(
    X_train_scaled, y_train,
    validation_split=0.2,
    epochs=50,
    batch_size=32,
    verbose=1
)

# Evaluate
loss, accuracy = model.evaluate(X_test_scaled, y_test)
print(f'Test Accuracy: {accuracy:.4f}')
```

---

## 🎯 Hyperparameter Tuning Guide

### **Common Hyperparameters**

**Random Forest:**
```python
{
    'n_estimators': [100, 200, 500],           # Number of trees
    'max_depth': [10, 20, None],               # Tree depth
    'min_samples_split': [2, 5, 10],           # Min samples to split
    'min_samples_leaf': [1, 2, 4],             # Min samples in leaf
    'max_features': ['sqrt', 'log2', None]     # Features per split
}
```

**XGBoost:**
```python
{
    'learning_rate': [0.01, 0.1, 0.3],         # Shrinkage
    'n_estimators': [100, 200, 500],           # Boosting rounds
    'max_depth': [3, 5, 7],                    # Tree depth
    'subsample': [0.8, 0.9, 1.0],              # Sample ratio
    'colsample_bytree': [0.8, 0.9, 1.0]        # Feature ratio
}
```

**Neural Network:**
```python
{
    'hidden_layers': [[128, 64], [256, 128, 64]],  # Architecture
    'dropout_rate': [0.2, 0.3, 0.5],                # Dropout
    'learning_rate': [0.001, 0.0001],               # LR
    'batch_size': [32, 64, 128],                    # Batch size
    'optimizer': ['adam', 'rmsprop']                # Optimizer
}
```

### **Grid Search vs Random Search**

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

# Grid Search (exhaustive)
grid_search = GridSearchCV(
    model, param_grid, cv=5, scoring='accuracy', n_jobs=-1
)
grid_search.fit(X_train, y_train)

# Random Search (faster)
random_search = RandomizedSearchCV(
    model, param_distributions, n_iter=50, cv=5, random_state=42
)
random_search.fit(X_train, y_train)

# Best parameters
print(f"Best params: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_:.4f}")
```

---

## 🚀 Production Deployment

### **Model Serving Options**

| Method | Latency | Scalability | Complexity | Use Case |
|--------|---------|-------------|------------|----------|
| **Flask API** | Medium | Low | Low | Small apps |
| **FastAPI** | Low | Medium | Low | Modern APIs |
| **TF Serving** | Very Low | High | High | Production TF |
| **AWS Lambda** | Medium | Very High | Medium | Serverless |
| **Docker + K8s** | Low | Very High | High | Enterprise |

### **Simple API Example**

```python
from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

@app.post("/predict")
def predict(features: list):
    # Preprocess
    X = np.array(features).reshape(1, -1)
    X_scaled = scaler.transform(X)
    
    # Predict
    prediction = model.predict(X_scaled)[0]
    probability = model.predict_proba(X_scaled)[0].max()
    
    return {
        "prediction": int(prediction),
        "confidence": float(probability)
    }

# Run: uvicorn app:app --reload
```

---

## 📚 Interview Cheat Sheet

### **Top 10 ML Interview Questions**

1. **Explain bias-variance tradeoff**
   - Bias: Error from wrong assumptions (underfitting)
   - Variance: Error from sensitivity to training data (overfitting)
   - Tradeoff: Can't minimize both simultaneously

2. **Difference between L1 and L2 regularization**
   - L1 (Lasso): Creates sparse solutions, feature selection
   - L2 (Ridge): Shrinks all weights, no feature selection
   - Formula: L1 = λΣ|w|, L2 = λΣw²

3. **How does Random Forest work?**
   - Ensemble of decision trees
   - Bootstrap sampling + random features
   - Majority voting for classification
   - Reduces variance, prevents overfitting

4. **Explain cross-validation**
   - Split data into K folds
   - Train on K-1, validate on 1
   - Repeat K times, average results
   - Better estimate of model performance

5. **How to handle imbalanced data?**
   - SMOTE (oversampling minority)
   - Undersampling majority
   - Class weights
   - Ensemble methods
   - Proper metrics (F1, not accuracy)

6. **Gradient descent variants**
   - Batch: All data (slow, stable)
   - Stochastic: One sample (fast, noisy)
   - Mini-batch: Batch of samples (best tradeoff)

7. **Activation functions comparison**
   - Sigmoid: (0,1), output layer
   - ReLU: Fast, most used in hidden layers
   - Tanh: (-1,1), zero-centered
   - Softmax: Multi-class output

8. **Overfitting prevention**
   - More data
   - Regularization (L1/L2/Dropout)
   - Simpler model
   - Cross-validation
   - Early stopping

9. **Feature scaling necessity**
   - Required: KNN, SVM, Neural Networks, PCA
   - Not required: Tree-based (Decision Tree, RF, XGBoost)
   - Reason: Distance/gradient-based need same scale

10. **Precision vs Recall**
    - Precision: Of predicted positive, how many correct?
    - Recall: Of actual positive, how many found?
    - Precision for spam (avoid false positives)
    - Recall for disease (find all positives)

---

## 🔥 Hot Tips & Tricks

### **Pandas Power Moves**
```python
# Quick EDA
df.info()                           # Overview
df.describe()                       # Statistics
df.isnull().sum()                   # Missing values
df.corr()                           # Correlations

# Fast operations
df.query('age > 30')                # Filter
df.groupby('category').agg(['mean', 'sum'])  # Group
df.pipe(func1).pipe(func2)          # Chain functions
```

### **Numpy Tricks**
```python
# Efficient operations
np.where(condition, x, y)           # Conditional
np.clip(array, min, max)            # Limit values
np.percentile(array, [25, 75])      # Quartiles
np.vectorize(func)(array)           # Apply function
```

### **Plotting Quick**
```python
import matplotlib.pyplot as plt
import seaborn as sns

# One-liners
sns.pairplot(df)                    # All relationships
sns.heatmap(df.corr(), annot=True)  # Correlation matrix
df.hist(figsize=(12,10))            # All histograms
```

---

## 🎓 Learning Resources Priority

### **Must-Read (Do First)**
1. ✅ Feature-Engineering-Complete-Guide.md
2. ✅ Build-ML-Models-From-Scratch-Complete-Guide.md
3. ✅ MASTER-ML-DS-COMPLETE-ROADMAP.md
4. ✅ This cheat sheet!

### **Books (Pick 2-3)**
- "Hands-On Machine Learning" - Aurélien Géron ⭐⭐⭐
- "Deep Learning" - Goodfellow ⭐⭐
- "Introduction to Statistical Learning" - James et al. ⭐⭐

### **Online (Free)**
- Fast.ai - Practical DL ⭐⭐⭐
- Stanford CS229 ⭐⭐
- Kaggle Learn ⭐⭐

---

## ⚡ Command Line Quick Reference

```bash
# Python environment
python -m venv env
source env/bin/activate
pip install -r requirements.txt

# Jupyter
jupyter notebook
jupyter lab

# Git (save your work!)
git add .
git commit -m "descriptive message"
git push origin main

# Common installations
pip install numpy pandas matplotlib seaborn scikit-learn
pip install tensorflow torch torchvision
pip install xgboost lightgbm catboost
pip install jupyterlab notebook

# Check versions
python --version
pip list
```

---

## 🎯 Today's Action Items

```
□ Save this cheat sheet
□ Read one section from main guides
□ Code one algorithm from scratch
□ Work on one project (30 min)
□ Push code to GitHub
□ Review one concept before bed

Remember: Small daily progress > Large irregular bursts!
```

---

**🌟 You've got everything you need. Now GO CODE! 💻**

*Print this. Pin it. Reference it daily. Master it weekly.*
