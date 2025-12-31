# Building Machine Learning Models from Scratch: Zero to Hero

> **Master ML/DL by Building Everything from First Principles - No Libraries, Pure Understanding**

---

## 🎯 What You'll Learn

By the end of this guide, you will:
- ✅ Understand how ML algorithms work under the hood
- ✅ Build ML algorithms from scratch (no sklearn!)
- ✅ Implement neural networks with just NumPy
- ✅ Create custom loss functions and optimizers
- ✅ Design your own model architectures
- ✅ Train models efficiently
- ✅ Debug and improve model performance
- ✅ Deploy your custom models to production
- ✅ Understand when to use which algorithm

---

## 📚 Table of Contents

### Part 1: Traditional Machine Learning from Scratch
1. [Linear Regression from Scratch](#1-linear-regression-from-scratch)
2. [Logistic Regression from Scratch](#2-logistic-regression-from-scratch)
3. [Decision Trees from Scratch](#3-decision-trees-from-scratch)
4. [Random Forest from Scratch](#4-random-forest-from-scratch)
5. [K-Nearest Neighbors from Scratch](#5-k-nearest-neighbors-from-scratch)
6. [K-Means Clustering from Scratch](#6-k-means-clustering-from-scratch)
7. [Support Vector Machines from Scratch](#7-support-vector-machines-from-scratch)
8. [Naive Bayes from Scratch](#8-naive-bayes-from-scratch)

### Part 2: Neural Networks from Scratch
9. [Understanding Neural Networks](#9-understanding-neural-networks)
10. [Building a Neural Network with NumPy](#10-building-a-neural-network-with-numpy)
11. [Activation Functions from Scratch](#11-activation-functions-from-scratch)
12. [Loss Functions from Scratch](#12-loss-functions-from-scratch)
13. [Backpropagation Explained](#13-backpropagation-explained)
14. [Optimizers from Scratch](#14-optimizers-from-scratch)

### Part 3: Deep Learning Architectures
15. [Convolutional Neural Networks (CNN)](#15-convolutional-neural-networks)
16. [Recurrent Neural Networks (RNN)](#16-recurrent-neural-networks)
17. [Long Short-Term Memory (LSTM)](#17-long-short-term-memory)
18. [Attention Mechanism](#18-attention-mechanism)
19. [Transformer Architecture](#19-transformer-architecture)

### Part 4: Advanced Topics
20. [Regularization Techniques](#20-regularization-techniques)
21. [Batch Normalization](#21-batch-normalization)
22. [Dropout](#22-dropout)
23. [Custom Model Architectures](#23-custom-model-architectures)
24. [Transfer Learning](#24-transfer-learning)
25. [Model Compression](#25-model-compression)

### Part 5: Production & Optimization
26. [Training Strategies](#26-training-strategies)
27. [Hyperparameter Tuning](#27-hyperparameter-tuning)
28. [Model Debugging](#28-model-debugging)
29. [Performance Optimization](#29-performance-optimization)
30. [Deployment Strategies](#30-deployment-strategies)

---

# Part 1: Traditional Machine Learning from Scratch

## 1. Linear Regression from Scratch

### Understanding the Math

**Simple Explanation:** Find the best line that fits your data points.

**Mathematical Formula:**
```
y = mx + b
or in ML terms:
ŷ = w₁x + w₀

Loss function (MSE): L = (1/n) Σ(y - ŷ)²
```

### Implementation from Scratch

```python
import numpy as np
import matplotlib.pyplot as plt

class LinearRegressionScratch:
    """
    Linear Regression implemented from scratch
    No sklearn, pure NumPy and math!
    """
    
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        """
        Parameters:
        -----------
        learning_rate : float
            Step size for gradient descent
        n_iterations : int
            Number of training iterations
        """
        self.lr = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        self.loss_history = []
    
    def fit(self, X, y):
        """
        Train the model using gradient descent
        
        Parameters:
        -----------
        X : numpy array of shape (n_samples, n_features)
        y : numpy array of shape (n_samples,)
        """
        # Initialize parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Gradient Descent
        for i in range(self.n_iterations):
            # Forward pass: predictions
            y_predicted = np.dot(X, self.weights) + self.bias
            
            # Compute loss (MSE)
            loss = np.mean((y - y_predicted) ** 2)
            self.loss_history.append(loss)
            
            # Backward pass: compute gradients
            # dL/dw = (2/n) * Σ(ŷ - y) * x
            # dL/db = (2/n) * Σ(ŷ - y)
            dw = (2/n_samples) * np.dot(X.T, (y_predicted - y))
            db = (2/n_samples) * np.sum(y_predicted - y)
            
            # Update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            
            # Print progress
            if i % 100 == 0:
                print(f"Iteration {i}: Loss = {loss:.4f}")
    
    def predict(self, X):
        """
        Make predictions
        
        Parameters:
        -----------
        X : numpy array of shape (n_samples, n_features)
        
        Returns:
        --------
        y_pred : numpy array of shape (n_samples,)
        """
        return np.dot(X, self.weights) + self.bias
    
    def score(self, X, y):
        """
        Calculate R² score
        
        R² = 1 - (SS_res / SS_tot)
        where:
        SS_res = Σ(y - ŷ)²  (residual sum of squares)
        SS_tot = Σ(y - ȳ)²  (total sum of squares)
        """
        y_pred = self.predict(X)
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        r2 = 1 - (ss_res / ss_tot)
        return r2


# ============================================
# TEST THE MODEL
# ============================================

print("=" * 70)
print("LINEAR REGRESSION FROM SCRATCH - DEMO")
print("=" * 70)

# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X.squeeze() + np.random.randn(100)

print("\n1. Generated synthetic data")
print(f"   X shape: {X.shape}")
print(f"   y shape: {y.shape}")

# Create and train model
model = LinearRegressionScratch(learning_rate=0.1, n_iterations=1000)
print("\n2. Training model...")
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Evaluate
r2 = model.score(X, y)
print(f"\n3. Model Performance:")
print(f"   R² Score: {r2:.4f}")
print(f"   Learned weight: {model.weights[0]:.4f} (true: 3.0)")
print(f"   Learned bias: {model.bias:.4f} (true: 4.0)")

# Visualize
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Data and predictions
axes[0].scatter(X, y, alpha=0.5, label='Actual data')
axes[0].plot(X, y_pred, 'r-', linewidth=2, label='Predictions')
axes[0].set_xlabel('X')
axes[0].set_ylabel('y')
axes[0].set_title('Linear Regression: Data vs Predictions')
axes[0].legend()
axes[0].grid(True)

# Plot 2: Loss curve
axes[1].plot(model.loss_history)
axes[1].set_xlabel('Iteration')
axes[1].set_ylabel('Loss (MSE)')
axes[1].set_title('Training Loss Over Time')
axes[1].grid(True)

plt.tight_layout()
plt.show()

print("\n✅ Linear Regression from scratch completed!")
```

### Understanding Gradient Descent

```python
def visualize_gradient_descent():
    """
    Visualize how gradient descent finds the minimum
    """
    print("\n" + "=" * 70)
    print("UNDERSTANDING GRADIENT DESCENT")
    print("=" * 70)
    
    # Simple 1D loss function
    def loss_function(w):
        return (w - 3) ** 2 + 2
    
    def gradient(w):
        return 2 * (w - 3)
    
    # Gradient descent
    learning_rates = [0.1, 0.3, 0.9]
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    for idx, lr in enumerate(learning_rates):
        w = 0.0  # Starting point
        history = [w]
        
        for _ in range(20):
            grad = gradient(w)
            w = w - lr * grad
            history.append(w)
        
        # Plot
        w_range = np.linspace(-2, 8, 100)
        loss_range = loss_function(w_range)
        
        axes[idx].plot(w_range, loss_range, 'b-', label='Loss function')
        axes[idx].plot(history, loss_function(np.array(history)), 
                       'ro-', label='GD path', markersize=4)
        axes[idx].axvline(x=3, color='g', linestyle='--', label='Minimum')
        axes[idx].set_xlabel('Weight (w)')
        axes[idx].set_ylabel('Loss')
        axes[idx].set_title(f'Learning Rate = {lr}')
        axes[idx].legend()
        axes[idx].grid(True)
        
        print(f"\nLearning Rate {lr}:")
        print(f"  Final weight: {history[-1]:.4f}")
        print(f"  Final loss: {loss_function(history[-1]):.4f}")
        print(f"  Iterations to converge: {len(history)}")
    
    plt.tight_layout()
    plt.show()
    
    print("\n💡 KEY INSIGHTS:")
    print("   - Too small LR: Slow convergence")
    print("   - Too large LR: Oscillation or divergence")
    print("   - Just right LR: Fast and stable convergence")

visualize_gradient_descent()
```

### Multiple Linear Regression

```python
class MultipleLinearRegression:
    """
    Multiple Linear Regression: ŷ = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
    """
    
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.lr = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
    
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for _ in range(self.n_iterations):
            # Predictions
            y_pred = np.dot(X, self.weights) + self.bias
            
            # Gradients
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))
            db = (1/n_samples) * np.sum(y_pred - y)
            
            # Update
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
    
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
    
    def get_coefficients(self):
        """Return feature coefficients"""
        return dict(enumerate(self.weights))

# Test with multiple features
print("\n" + "=" * 70)
print("MULTIPLE LINEAR REGRESSION")
print("=" * 70)

# Generate data with 3 features
np.random.seed(42)
X_multi = np.random.rand(100, 3)
y_multi = 4 + 2*X_multi[:, 0] + 3*X_multi[:, 1] + 5*X_multi[:, 2] + np.random.randn(100)*0.5

model_multi = MultipleLinearRegression(learning_rate=0.1, n_iterations=1000)
model_multi.fit(X_multi, y_multi)

print("\nTrue coefficients: [2, 3, 5], bias: 4")
print(f"Learned coefficients: {model_multi.weights}")
print(f"Learned bias: {model_multi.bias:.4f}")
```

---

## 2. Logistic Regression from Scratch

### Understanding the Math

**Simple Explanation:** Predict probability between 0 and 1 using sigmoid function.

**Mathematical Formula:**
```
Sigmoid: σ(z) = 1 / (1 + e^(-z))
Prediction: ŷ = σ(wx + b)
Loss (Binary Cross-Entropy): L = -[y·log(ŷ) + (1-y)·log(1-ŷ)]
```

### Implementation

```python
class LogisticRegressionScratch:
    """
    Logistic Regression from scratch
    For binary classification
    """
    
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.lr = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        self.loss_history = []
    
    def sigmoid(self, z):
        """
        Sigmoid activation function
        σ(z) = 1 / (1 + e^(-z))
        
        Properties:
        - Output range: (0, 1)
        - Smooth gradient
        - Interpretable as probability
        """
        return 1 / (1 + np.exp(-z))
    
    def fit(self, X, y):
        """
        Train using gradient descent
        """
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Gradient descent
        for i in range(self.n_iterations):
            # Forward pass
            linear_model = np.dot(X, self.weights) + self.bias
            y_predicted = self.sigmoid(linear_model)
            
            # Compute loss (Binary Cross-Entropy)
            epsilon = 1e-15  # Prevent log(0)
            y_predicted = np.clip(y_predicted, epsilon, 1 - epsilon)
            loss = -np.mean(y * np.log(y_predicted) + (1 - y) * np.log(1 - y_predicted))
            self.loss_history.append(loss)
            
            # Backward pass: compute gradients
            dw = (1/n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1/n_samples) * np.sum(y_predicted - y)
            
            # Update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            
            if i % 100 == 0:
                print(f"Iteration {i}: Loss = {loss:.4f}")
    
    def predict_proba(self, X):
        """
        Predict probabilities
        """
        linear_model = np.dot(X, self.weights) + self.bias
        return self.sigmoid(linear_model)
    
    def predict(self, X, threshold=0.5):
        """
        Predict class labels (0 or 1)
        """
        probabilities = self.predict_proba(X)
        return (probabilities >= threshold).astype(int)
    
    def accuracy(self, X, y):
        """
        Calculate accuracy
        """
        predictions = self.predict(X)
        return np.mean(predictions == y)


# ============================================
# TEST LOGISTIC REGRESSION
# ============================================

print("\n" + "=" * 70)
print("LOGISTIC REGRESSION FROM SCRATCH - DEMO")
print("=" * 70)

# Generate binary classification data
from sklearn.datasets import make_classification
X_class, y_class = make_classification(n_samples=1000, n_features=2, 
                                       n_redundant=0, n_informative=2,
                                       n_clusters_per_class=1, random_state=42)

print("\n1. Generated binary classification data")
print(f"   Class 0: {np.sum(y_class == 0)} samples")
print(f"   Class 1: {np.sum(y_class == 1)} samples")

# Train model
print("\n2. Training logistic regression...")
log_model = LogisticRegressionScratch(learning_rate=0.1, n_iterations=1000)
log_model.fit(X_class, y_class)

# Evaluate
accuracy = log_model.accuracy(X_class, y_class)
print(f"\n3. Model Performance:")
print(f"   Accuracy: {accuracy:.4f}")

# Visualize decision boundary
def plot_decision_boundary(model, X, y):
    """
    Plot decision boundary for 2D data
    """
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.figure(figsize=(12, 5))
    
    # Plot 1: Decision boundary
    plt.subplot(1, 2, 1)
    plt.contourf(xx, yy, Z, alpha=0.4, cmap='RdYlBu')
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='RdYlBu', edgecolors='black')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Decision Boundary')
    plt.colorbar()
    
    # Plot 2: Loss curve
    plt.subplot(1, 2, 2)
    plt.plot(model.loss_history)
    plt.xlabel('Iteration')
    plt.ylabel('Loss (Binary Cross-Entropy)')
    plt.title('Training Loss')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

plot_decision_boundary(log_model, X_class, y_class)

print("\n✅ Logistic Regression from scratch completed!")
```

### Understanding Sigmoid Function

```python
def understand_sigmoid():
    """
    Deep dive into sigmoid function
    """
    print("\n" + "=" * 70)
    print("UNDERSTANDING SIGMOID FUNCTION")
    print("=" * 70)
    
    def sigmoid(z):
        return 1 / (1 + np.exp(-z))
    
    def sigmoid_derivative(z):
        s = sigmoid(z)
        return s * (1 - s)
    
    z = np.linspace(-10, 10, 100)
    sig = sigmoid(z)
    sig_deriv = sigmoid_derivative(z)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Sigmoid function
    axes[0].plot(z, sig, 'b-', linewidth=2)
    axes[0].axhline(y=0.5, color='r', linestyle='--', label='Decision boundary')
    axes[0].axvline(x=0, color='g', linestyle='--')
    axes[0].set_xlabel('z (wx + b)')
    axes[0].set_ylabel('σ(z)')
    axes[0].set_title('Sigmoid Function')
    axes[0].legend()
    axes[0].grid(True)
    
    # Derivative
    axes[1].plot(z, sig_deriv, 'r-', linewidth=2)
    axes[1].set_xlabel('z')
    axes[1].set_ylabel("σ'(z)")
    axes[1].set_title('Sigmoid Derivative')
    axes[1].grid(True)
    
    plt.tight_layout()
    plt.show()
    
    print("\n💡 KEY PROPERTIES:")
    print("   - Output range: (0, 1) → can be interpreted as probability")
    print("   - Smooth and differentiable everywhere")
    print("   - σ(0) = 0.5 → natural decision boundary")
    print("   - σ'(z) = σ(z) · (1 - σ(z)) → easy to compute gradient")
    print("   - Problem: Vanishing gradients for large |z|")

understand_sigmoid()
```

---

## 3. Decision Trees from Scratch

### Understanding the Math

**Simple Explanation:** Split data recursively to create a tree of decisions.

**Key Concepts:**
- **Entropy**: Measure of impurity/disorder
- **Information Gain**: Reduction in entropy after split
- **Gini Impurity**: Alternative to entropy

### Implementation

```python
class Node:
    """
    Node in decision tree
    """
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature      # Feature to split on
        self.threshold = threshold  # Threshold value for split
        self.left = left           # Left child
        self.right = right         # Right child
        self.value = value         # Prediction value (for leaf nodes)


class DecisionTreeScratch:
    """
    Decision Tree Classifier from scratch
    Using Information Gain (Entropy) for splits
    """
    
    def __init__(self, max_depth=10, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None
    
    def entropy(self, y):
        """
        Calculate entropy: H(S) = -Σ(pᵢ · log₂(pᵢ))
        
        Entropy measures disorder:
        - 0: Pure (all same class)
        - 1: Maximum impurity (equal distribution)
        """
        proportions = np.bincount(y) / len(y)
        entropy = -np.sum([p * np.log2(p) for p in proportions if p > 0])
        return entropy
    
    def information_gain(self, parent, left_child, right_child):
        """
        Calculate information gain
        IG = H(parent) - [weighted_avg(H(children))]
        """
        weight_left = len(left_child) / len(parent)
        weight_right = len(right_child) / len(parent)
        
        gain = self.entropy(parent) - (
            weight_left * self.entropy(left_child) +
            weight_right * self.entropy(right_child)
        )
        return gain
    
    def best_split(self, X, y):
        """
        Find the best feature and threshold to split on
        """
        best_gain = -1
        best_feature = None
        best_threshold = None
        
        n_features = X.shape[1]
        
        # Try each feature
        for feature_idx in range(n_features):
            feature_values = X[:, feature_idx]
            thresholds = np.unique(feature_values)
            
            # Try each threshold
            for threshold in thresholds:
                # Split data
                left_mask = feature_values <= threshold
                right_mask = feature_values > threshold
                
                if np.sum(left_mask) == 0 or np.sum(right_mask) == 0:
                    continue
                
                # Calculate information gain
                left_y = y[left_mask]
                right_y = y[right_mask]
                gain = self.information_gain(y, left_y, right_y)
                
                # Update best split
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature_idx
                    best_threshold = threshold
        
        return best_feature, best_threshold
    
    def build_tree(self, X, y, depth=0):
        """
        Recursively build the tree
        """
        n_samples, n_features = X.shape
        n_classes = len(np.unique(y))
        
        # Stopping criteria
        if (depth >= self.max_depth or 
            n_samples < self.min_samples_split or 
            n_classes == 1):
            # Create leaf node
            leaf_value = np.argmax(np.bincount(y))
            return Node(value=leaf_value)
        
        # Find best split
        best_feature, best_threshold = self.best_split(X, y)
        
        if best_feature is None:
            leaf_value = np.argmax(np.bincount(y))
            return Node(value=leaf_value)
        
        # Split data
        left_mask = X[:, best_feature] <= best_threshold
        right_mask = X[:, best_feature] > best_threshold
        
        # Recursively build left and right subtrees
        left_child = self.build_tree(X[left_mask], y[left_mask], depth + 1)
        right_child = self.build_tree(X[right_mask], y[right_mask], depth + 1)
        
        return Node(best_feature, best_threshold, left_child, right_child)
    
    def fit(self, X, y):
        """
        Build the decision tree
        """
        self.root = self.build_tree(X, y)
    
    def predict_sample(self, x, node):
        """
        Predict single sample by traversing tree
        """
        # If leaf node, return value
        if node.value is not None:
            return node.value
        
        # Traverse tree
        if x[node.feature] <= node.threshold:
            return self.predict_sample(x, node.left)
        else:
            return self.predict_sample(x, node.right)
    
    def predict(self, X):
        """
        Predict multiple samples
        """
        return np.array([self.predict_sample(x, self.root) for x in X])
    
    def accuracy(self, X, y):
        """
        Calculate accuracy
        """
        predictions = self.predict(X)
        return np.mean(predictions == y)


# ============================================
# TEST DECISION TREE
# ============================================

print("\n" + "=" * 70)
print("DECISION TREE FROM SCRATCH - DEMO")
print("=" * 70)

# Generate data
from sklearn.datasets import make_moons
X_tree, y_tree = make_moons(n_samples=500, noise=0.3, random_state=42)

print("\n1. Generated dataset with 500 samples")

# Train decision tree
print("\n2. Building decision tree...")
tree = DecisionTreeScratch(max_depth=10, min_samples_split=2)
tree.fit(X_tree, y_tree)

# Evaluate
accuracy = tree.accuracy(X_tree, y_tree)
print(f"\n3. Training Accuracy: {accuracy:.4f}")

# Visualize
def visualize_tree_decision_boundary(model, X, y):
    """
    Visualize decision boundary for decision tree
    """
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))
    
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.figure(figsize=(10, 8))
    plt.contourf(xx, yy, Z, alpha=0.4, cmap='RdYlBu')
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='RdYlBu', edgecolors='black', s=50)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title(f'Decision Tree Boundary (Depth={model.max_depth})')
    plt.colorbar()
    plt.show()

visualize_tree_decision_boundary(tree, X_tree, y_tree)

print("\n✅ Decision Tree from scratch completed!")
```

### Understanding Entropy and Information Gain

```python
def understand_entropy_and_information_gain():
    """
    Visualize entropy and information gain
    """
    print("\n" + "=" * 70)
    print("UNDERSTANDING ENTROPY & INFORMATION GAIN")
    print("=" * 70)
    
    def entropy(p):
        """Entropy for binary classification"""
        if p == 0 or p == 1:
            return 0
        return -p * np.log2(p) - (1-p) * np.log2(1-p)
    
    # Entropy curve
    p_values = np.linspace(0.01, 0.99, 100)
    entropy_values = [entropy(p) for p in p_values]
    
    plt.figure(figsize=(12, 5))
    
    # Plot 1: Entropy curve
    plt.subplot(1, 2, 1)
    plt.plot(p_values, entropy_values, 'b-', linewidth=2)
    plt.axvline(x=0.5, color='r', linestyle='--', label='Maximum entropy')
    plt.xlabel('Probability of class 1')
    plt.ylabel('Entropy')
    plt.title('Entropy Function')
    plt.legend()
    plt.grid(True)
    
    # Plot 2: Example split
    plt.subplot(1, 2, 2)
    
    # Before split: 50-50
    before = [5, 5]
    # After split: [8, 2] and [2, 8]
    left = [8, 2]
    right = [2, 8]
    
    categories = ['Before\nSplit', 'Left\nChild', 'Right\nChild']
    class_0 = [before[0], left[0], right[0]]
    class_1 = [before[1], left[1], right[1]]
    
    x = np.arange(len(categories))
    width = 0.35
    
    plt.bar(x - width/2, class_0, width, label='Class 0', color='blue', alpha=0.7)
    plt.bar(x + width/2, class_1, width, label='Class 1', color='red', alpha=0.7)
    plt.xlabel('Node')
    plt.ylabel('Count')
    plt.title('Example Split')
    plt.xticks(x, categories)
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    # Calculate entropies
    def calc_entropy(counts):
        total = sum(counts)
        probs = [c/total for c in counts]
        return -sum(p * np.log2(p) if p > 0 else 0 for p in probs)
    
    h_before = calc_entropy(before)
    h_left = calc_entropy(left)
    h_right = calc_entropy(right)
    
    # Information gain
    total = sum(before)
    ig = h_before - (len(left)/total * h_left + len(right)/total * h_right)
    
    print("\n📊 EXAMPLE CALCULATION:")
    print(f"   Before split: {before} → Entropy = {h_before:.3f}")
    print(f"   Left child:   {left} → Entropy = {h_left:.3f}")
    print(f"   Right child:  {right} → Entropy = {h_right:.3f}")
    print(f"   Information Gain = {ig:.3f}")
    
    print("\n💡 INTERPRETATION:")
    print("   - High entropy = High disorder/impurity")
    print("   - Low entropy = Low disorder (more pure)")
    print("   - Information Gain = Reduction in entropy")
    print("   - We want splits that maximize information gain!")

understand_entropy_and_information_gain()
```

---

## 4. Random Forest from Scratch

```python
class RandomForestScratch:
    """
    Random Forest: Ensemble of decision trees
    """
    
    def __init__(self, n_trees=10, max_depth=10, min_samples_split=2, 
                 max_features='sqrt'):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.max_features = max_features
        self.trees = []
    
    def bootstrap_sample(self, X, y):
        """
        Create bootstrap sample (random sampling with replacement)
        """
        n_samples = X.shape[0]
        indices = np.random.choice(n_samples, n_samples, replace=True)
        return X[indices], y[indices]
    
    def fit(self, X, y):
        """
        Build multiple decision trees
        """
        self.trees = []
        
        for i in range(self.n_trees):
            # Bootstrap sample
            X_sample, y_sample = self.bootstrap_sample(X, y)
            
            # Train tree
            tree = DecisionTreeScratch(
                max_depth=self.max_depth,
                min_samples_split=self.min_samples_split
            )
            tree.fit(X_sample, y_sample)
            self.trees.append(tree)
            
            if (i + 1) % 10 == 0:
                print(f"Built {i + 1}/{self.n_trees} trees")
    
    def predict(self, X):
        """
        Predict by majority voting
        """
        # Get predictions from all trees
        tree_predictions = np.array([tree.predict(X) for tree in self.trees])
        
        # Majority vote
        predictions = []
        for i in range(X.shape[0]):
            predictions.append(np.bincount(tree_predictions[:, i].astype(int)).argmax())
        
        return np.array(predictions)
    
    def accuracy(self, X, y):
        predictions = self.predict(X)
        return np.mean(predictions == y)


# Test Random Forest
print("\n" + "=" * 70)
print("RANDOM FOREST FROM SCRATCH - DEMO")
print("=" * 70)

print("\n1. Building Random Forest with 50 trees...")
rf = RandomForestScratch(n_trees=50, max_depth=10)
rf.fit(X_tree, y_tree)

accuracy_rf = rf.accuracy(X_tree, y_tree)
print(f"\n2. Random Forest Accuracy: {accuracy_rf:.4f}")
print(f"   Single Tree Accuracy: {accuracy:.4f}")
print(f"   Improvement: {((accuracy_rf - accuracy) / accuracy * 100):.1f}%")

print("\n✅ Random Forest from scratch completed!")
```

---

# Part 2: Neural Networks from Scratch

## 9. Understanding Neural Networks

### The Biological Inspiration

```python
print("UNDERSTANDING NEURAL NETWORKS")
print("=" * 70)

print("""
BIOLOGICAL NEURON vs ARTIFICIAL NEURON
======================================

Biological Neuron:
- Dendrites: Receive signals from other neurons
- Cell body: Processes signals
- Axon: Sends output to other neurons
- Synapse: Connection between neurons

Artificial Neuron (Perceptron):
- Inputs (x₁, x₂, ..., xₙ): Like dendrites
- Weights (w₁, w₂, ..., wₙ): Strength of connections
- Bias (b): Threshold for activation
- Activation function: Decides output
- Output (ŷ): Like axon signal

Mathematical Formula:
z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
ŷ = activation(z)
""")
```

### Building a Single Neuron

```python
class Neuron:
    """
    A single artificial neuron
    """
    
    def __init__(self, n_inputs, activation='sigmoid'):
        # Initialize weights and bias randomly
        self.weights = np.random.randn(n_inputs) * 0.01
        self.bias = 0
        self.activation = activation
    
    def activate(self, z):
        """Apply activation function"""
        if self.activation == 'sigmoid':
            return 1 / (1 + np.exp(-z))
        elif self.activation == 'relu':
            return np.maximum(0, z)
        elif self.activation == 'tanh':
            return np.tanh(z)
        else:
            return z  # linear
    
    def forward(self, inputs):
        """Forward pass"""
        z = np.dot(inputs, self.weights) + self.bias
        return self.activate(z)
    
    def __repr__(self):
        return f"Neuron(inputs={len(self.weights)}, activation={self.activation})"


# Demo single neuron
print("\n" + "=" * 70)
print("SINGLE NEURON DEMO")
print("=" * 70)

neuron = Neuron(n_inputs=3, activation='sigmoid')
print(f"\n{neuron}")
print(f"Weights: {neuron.weights}")
print(f"Bias: {neuron.bias}")

# Test forward pass
inputs = np.array([1.0, 2.0, 3.0])
output = neuron.forward(inputs)
print(f"\nInput: {inputs}")
print(f"Output: {output:.4f}")
```

---

## 10. Building a Neural Network with NumPy

### Complete Implementation

```python
class NeuralNetworkScratch:
    """
    Multi-layer Neural Network from scratch
    Pure NumPy implementation!
    """
    
    def __init__(self, layer_sizes, learning_rate=0.01):
        """
        Parameters:
        -----------
        layer_sizes : list
            Number of neurons in each layer
            Example: [2, 4, 3, 1] means:
            - Input layer: 2 features
            - Hidden layer 1: 4 neurons
            - Hidden layer 2: 3 neurons
            - Output layer: 1 neuron
        """
        self.layer_sizes = layer_sizes
        self.learning_rate = learning_rate
        self.weights = []
        self.biases = []
        self.loss_history = []
        
        # Initialize weights and biases
        for i in range(len(layer_sizes) - 1):
            # Xavier initialization: helps with training
            w = np.random.randn(layer_sizes[i], layer_sizes[i+1]) * np.sqrt(2.0 / layer_sizes[i])
            b = np.zeros((1, layer_sizes[i+1]))
            self.weights.append(w)
            self.biases.append(b)
    
    def sigmoid(self, z):
        """Sigmoid activation"""
        return 1 / (1 + np.exp(-np.clip(z, -500, 500)))  # Clip to prevent overflow
    
    def sigmoid_derivative(self, z):
        """Derivative of sigmoid"""
        s = self.sigmoid(z)
        return s * (1 - s)
    
    def relu(self, z):
        """ReLU activation"""
        return np.maximum(0, z)
    
    def relu_derivative(self, z):
        """Derivative of ReLU"""
        return (z > 0).astype(float)
    
    def forward(self, X):
        """
        Forward propagation
        
        Returns both activations and pre-activation values (z)
        We need z values for backpropagation
        """
        activations = [X]
        z_values = []
        
        # Forward through each layer
        for i in range(len(self.weights)):
            # Compute z = w·a + b
            z = np.dot(activations[-1], self.weights[i]) + self.biases[i]
            z_values.append(z)
            
            # Apply activation function
            if i < len(self.weights) - 1:  # Hidden layers: ReLU
                a = self.relu(z)
            else:  # Output layer: Sigmoid
                a = self.sigmoid(z)
            
            activations.append(a)
        
        return activations, z_values
    
    def backward(self, X, y, activations, z_values):
        """
        Backpropagation: Compute gradients
        
        This is where the magic happens!
        We compute how much each weight contributed to the error
        """
        m = X.shape[0]  # Number of samples
        
        # Initialize gradient storage
        dW = [np.zeros_like(w) for w in self.weights]
        db = [np.zeros_like(b) for b in self.biases]
        
        # Output layer error
        # For binary cross-entropy with sigmoid:
        # dL/da = -(y/a - (1-y)/(1-a))
        # da/dz = a(1-a)
        # dL/dz = dL/da * da/dz = a - y
        delta = activations[-1] - y.reshape(-1, 1)
        
        # Backpropagate through layers
        for i in reversed(range(len(self.weights))):
            # Gradient for weights: dL/dW = aᵀ · delta
            dW[i] = np.dot(activations[i].T, delta) / m
            
            # Gradient for biases: dL/db = sum(delta)
            db[i] = np.sum(delta, axis=0, keepdims=True) / m
            
            # Propagate error to previous layer
            if i > 0:
                delta = np.dot(delta, self.weights[i].T) * self.relu_derivative(z_values[i-1])
        
        return dW, db
    
    def update_parameters(self, dW, db):
        """
        Update weights and biases using gradient descent
        """
        for i in range(len(self.weights)):
            self.weights[i] -= self.learning_rate * dW[i]
            self.biases[i] -= self.learning_rate * db[i]
    
    def compute_loss(self, y_true, y_pred):
        """
        Binary cross-entropy loss
        L = -[y·log(ŷ) + (1-y)·log(1-ŷ)]
        """
        m = y_true.shape[0]
        epsilon = 1e-15  # Prevent log(0)
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
        loss = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
        return loss
    
    def train(self, X, y, epochs=1000, verbose=True):
        """
        Train the neural network
        """
        for epoch in range(epochs):
            # Forward pass
            activations, z_values = self.forward(X)
            
            # Compute loss
            loss = self.compute_loss(y, activations[-1])
            self.loss_history.append(loss)
            
            # Backward pass
            dW, db = self.backward(X, y, activations, z_values)
            
            # Update parameters
            self.update_parameters(dW, db)
            
            # Print progress
            if verbose and epoch % 100 == 0:
                accuracy = np.mean((activations[-1] > 0.5).astype(int) == y.reshape(-1, 1))
                print(f"Epoch {epoch}: Loss = {loss:.4f}, Accuracy = {accuracy:.4f}")
    
    def predict(self, X):
        """
        Make predictions
        """
        activations, _ = self.forward(X)
        return (activations[-1] > 0.5).astype(int).flatten()
    
    def predict_proba(self, X):
        """
        Predict probabilities
        """
        activations, _ = self.forward(X)
        return activations[-1].flatten()


# ============================================
# TEST NEURAL NETWORK
# ============================================

print("\n" + "=" * 70)
print("NEURAL NETWORK FROM SCRATCH - DEMO")
print("=" * 70)

# Generate XOR problem (not linearly separable!)
print("\n1. Creating XOR dataset (classic non-linear problem)")
X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_xor = np.array([0, 1, 1, 0])

print("XOR Truth Table:")
print("X₁  X₂  |  Y")
print("-----------")
for i in range(len(X_xor)):
    print(f" {X_xor[i, 0]}   {X_xor[i, 1]}  |  {y_xor[i]}")

# Create and train neural network
print("\n2. Building Neural Network: [2, 4, 1]")
print("   - Input: 2 features")
print("   - Hidden: 4 neurons")
print("   - Output: 1 neuron")

nn = NeuralNetworkScratch(layer_sizes=[2, 4, 1], learning_rate=0.5)

print("\n3. Training for 2000 epochs...")
nn.train(X_xor, y_xor, epochs=2000, verbose=True)

# Evaluate
print("\n4. Final Predictions:")
predictions = nn.predict(X_xor)
probabilities = nn.predict_proba(X_xor)

print("X₁  X₂  | True  Pred  Prob")
print("-----------------------------")
for i in range(len(X_xor)):
    print(f" {X_xor[i, 0]}   {X_xor[i, 1]}  |  {y_xor[i]}     {predictions[i]}    {probabilities[i]:.3f}")

accuracy = np.mean(predictions == y_xor)
print(f"\nAccuracy: {accuracy:.4f}")

# Visualize
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Decision boundary
x_min, x_max = -0.5, 1.5
y_min, y_max = -0.5, 1.5
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                     np.linspace(y_min, y_max, 100))
Z = nn.predict_proba(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

axes[0].contourf(xx, yy, Z, alpha=0.4, cmap='RdYlBu', levels=20)
axes[0].scatter(X_xor[:, 0], X_xor[:, 1], c=y_xor, cmap='RdYlBu', 
                s=200, edgecolors='black', linewidth=2)
axes[0].set_xlabel('X₁')
axes[0].set_ylabel('X₂')
axes[0].set_title('Neural Network Decision Boundary\n(Solved XOR!)')
axes[0].grid(True)

# Plot 2: Loss curve
axes[1].plot(nn.loss_history)
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Loss')
axes[1].set_title('Training Loss')
axes[1].grid(True)

plt.tight_layout()
plt.show()

print("\n✅ Neural Network from scratch completed!")
print("\n💡 KEY ACHIEVEMENT: Solved XOR problem!")
print("   Linear models (Logistic Regression) CANNOT solve XOR")
print("   But neural networks can! This shows the power of hidden layers.")
```

---

## 11. Activation Functions from Scratch

```python
class ActivationFunctions:
    """
    All activation functions with their derivatives
    """
    
    @staticmethod
    def sigmoid(z):
        """
        Sigmoid: σ(z) = 1 / (1 + e^(-z))
        Range: (0, 1)
        Use: Output layer for binary classification
        """
        return 1 / (1 + np.exp(-np.clip(z, -500, 500)))
    
    @staticmethod
    def sigmoid_derivative(z):
        s = ActivationFunctions.sigmoid(z)
        return s * (1 - s)
    
    @staticmethod
    def tanh(z):
        """
        Tanh: tanh(z) = (e^z - e^(-z)) / (e^z + e^(-z))
        Range: (-1, 1)
        Use: Hidden layers (zero-centered)
        """
        return np.tanh(z)
    
    @staticmethod
    def tanh_derivative(z):
        return 1 - np.tanh(z) ** 2
    
    @staticmethod
    def relu(z):
        """
        ReLU: max(0, z)
        Range: [0, ∞)
        Use: Hidden layers (most popular!)
        """
        return np.maximum(0, z)
    
    @staticmethod
    def relu_derivative(z):
        return (z > 0).astype(float)
    
    @staticmethod
    def leaky_relu(z, alpha=0.01):
        """
        Leaky ReLU: max(αz, z)
        Range: (-∞, ∞)
        Use: Hidden layers (fixes "dying ReLU" problem)
        """
        return np.where(z > 0, z, alpha * z)
    
    @staticmethod
    def leaky_relu_derivative(z, alpha=0.01):
        return np.where(z > 0, 1, alpha)
    
    @staticmethod
    def elu(z, alpha=1.0):
        """
        ELU: x if x > 0 else α(e^x - 1)
        Range: (-α, ∞)
        Use: Hidden layers (smooth, helps with vanishing gradient)
        """
        return np.where(z > 0, z, alpha * (np.exp(z) - 1))
    
    @staticmethod
    def elu_derivative(z, alpha=1.0):
        return np.where(z > 0, 1, alpha * np.exp(z))
    
    @staticmethod
    def softmax(z):
        """
        Softmax: e^zi / Σe^zj
        Use: Output layer for multi-class classification
        Outputs: probabilities that sum to 1
        """
        exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))  # Numerical stability
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)
    
    @staticmethod
    def swish(z):
        """
        Swish: x · σ(x)
        Use: Modern alternative to ReLU
        """
        return z * ActivationFunctions.sigmoid(z)
    
    @staticmethod
    def swish_derivative(z):
        s = ActivationFunctions.sigmoid(z)
        return s + z * s * (1 - s)


# Visualize all activation functions
def visualize_activations():
    """
    Compare all activation functions
    """
    print("\n" + "=" * 70)
    print("ACTIVATION FUNCTIONS COMPARISON")
    print("=" * 70)
    
    z = np.linspace(-5, 5, 200)
    
    activations = {
        'Sigmoid': (ActivationFunctions.sigmoid, ActivationFunctions.sigmoid_derivative),
        'Tanh': (ActivationFunctions.tanh, ActivationFunctions.tanh_derivative),
        'ReLU': (ActivationFunctions.relu, ActivationFunctions.relu_derivative),
        'Leaky ReLU': (ActivationFunctions.leaky_relu, ActivationFunctions.leaky_relu_derivative),
        'ELU': (ActivationFunctions.elu, ActivationFunctions.elu_derivative),
        'Swish': (ActivationFunctions.swish, ActivationFunctions.swish_derivative),
    }
    
    fig, axes = plt.subplots(3, 4, figsize=(16, 12))
    axes = axes.ravel()
    
    for idx, (name, (func, deriv)) in enumerate(activations.items()):
        # Plot function
        axes[idx*2].plot(z, func(z), linewidth=2)
        axes[idx*2].set_title(f'{name} Function')
        axes[idx*2].grid(True)
        axes[idx*2].axhline(y=0, color='k', linestyle='-', alpha=0.3)
        axes[idx*2].axvline(x=0, color='k', linestyle='-', alpha=0.3)
        
        # Plot derivative
        axes[idx*2+1].plot(z, deriv(z), linewidth=2, color='orange')
        axes[idx*2+1].set_title(f'{name} Derivative')
        axes[idx*2+1].grid(True)
        axes[idx*2+1].axhline(y=0, color='k', linestyle='-', alpha=0.3)
        axes[idx*2+1].axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    print("\n📊 ACTIVATION FUNCTION GUIDE:")
    print("\n1. SIGMOID:")
    print("   ✅ Use: Output layer for binary classification")
    print("   ❌ Avoid: Hidden layers (vanishing gradient problem)")
    
    print("\n2. TANH:")
    print("   ✅ Use: Hidden layers (better than sigmoid)")
    print("   ➕ Pro: Zero-centered output")
    print("   ➖ Con: Still has vanishing gradient")
    
    print("\n3. ReLU (Most Popular!):")
    print("   ✅ Use: Hidden layers in deep networks")
    print("   ➕ Pro: No vanishing gradient, computationally efficient")
    print("   ➖ Con: Dying ReLU problem (neurons can die)")
    
    print("\n4. LEAKY ReLU:")
    print("   ✅ Use: When ReLU neurons are dying")
    print("   ➕ Pro: Fixes dying ReLU problem")
    
    print("\n5. ELU:")
    print("   ✅ Use: When you want smooth activation")
    print("   ➕ Pro: Smooth, helps with vanishing gradient")
    print("   ➖ Con: Computationally expensive (exp)")
    
    print("\n6. SWISH:")
    print("   ✅ Use: Modern alternative to ReLU")
    print("   ➕ Pro: Often outperforms ReLU in practice")
    
    print("\n7. SOFTMAX:")
    print("   ✅ Use: Output layer for multi-class classification")
    print("   ➕ Pro: Outputs probabilities that sum to 1")

visualize_activations()
```

---

## 12. Loss Functions from Scratch

```python
class LossFunctions:
    """
    All loss functions with their derivatives
    """
    
    @staticmethod
    def mse(y_true, y_pred):
        """
        Mean Squared Error
        L = (1/n) Σ(y - ŷ)²
        Use: Regression problems
        """
        return np.mean((y_true - y_pred) ** 2)
    
    @staticmethod
    def mse_derivative(y_true, y_pred):
        return 2 * (y_pred - y_true) / y_true.size
    
    @staticmethod
    def mae(y_true, y_pred):
        """
        Mean Absolute Error
        L = (1/n) Σ|y - ŷ|
        Use: Regression with outliers
        """
        return np.mean(np.abs(y_true - y_pred))
    
    @staticmethod
    def mae_derivative(y_true, y_pred):
        return np.sign(y_pred - y_true) / y_true.size
    
    @staticmethod
    def binary_crossentropy(y_true, y_pred, epsilon=1e-15):
        """
        Binary Cross-Entropy
        L = -[y·log(ŷ) + (1-y)·log(1-ŷ)]
        Use: Binary classification
        """
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
        return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    
    @staticmethod
    def binary_crossentropy_derivative(y_true, y_pred, epsilon=1e-15):
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
        return -(y_true / y_pred - (1 - y_true) / (1 - y_pred)) / y_true.size
    
    @staticmethod
    def categorical_crossentropy(y_true, y_pred, epsilon=1e-15):
        """
        Categorical Cross-Entropy
        L = -Σ(y · log(ŷ))
        Use: Multi-class classification
        """
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
        return -np.mean(np.sum(y_true * np.log(y_pred), axis=1))
    
    @staticmethod
    def categorical_crossentropy_derivative(y_true, y_pred, epsilon=1e-15):
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
        return -(y_true / y_pred) / y_true.shape[0]
    
    @staticmethod
    def huber_loss(y_true, y_pred, delta=1.0):
        """
        Huber Loss
        Combines MSE and MAE
        Use: Regression robust to outliers
        """
        error = y_true - y_pred
        is_small_error = np.abs(error) <= delta
        squared_loss = 0.5 * error ** 2
        linear_loss = delta * (np.abs(error) - 0.5 * delta)
        return np.mean(np.where(is_small_error, squared_loss, linear_loss))
    
    @staticmethod
    def hinge_loss(y_true, y_pred):
        """
        Hinge Loss
        L = max(0, 1 - y·ŷ)
        Use: SVM, margin-based classification
        """
        return np.mean(np.maximum(0, 1 - y_true * y_pred))


# Visualize loss functions
def visualize_losses():
    """
    Compare different loss functions
    """
    print("\n" + "=" * 70)
    print("LOSS FUNCTIONS COMPARISON")
    print("=" * 70)
    
    # For regression
    y_true = 0
    y_pred_range = np.linspace(-3, 3, 200)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Plot 1: MSE
    mse_losses = [(y_true - y_pred) ** 2 for y_pred in y_pred_range]
    axes[0, 0].plot(y_pred_range, mse_losses, label='MSE', linewidth=2)
    axes[0, 0].set_title('Mean Squared Error (MSE)')
    axes[0, 0].set_xlabel('Prediction Error')
    axes[0, 0].set_ylabel('Loss')
    axes[0, 0].grid(True)
    axes[0, 0].axvline(x=0, color='r', linestyle='--', label='True value')
    axes[0, 0].legend()
    
    # Plot 2: MAE
    mae_losses = [np.abs(y_true - y_pred) for y_pred in y_pred_range]
    axes[0, 1].plot(y_pred_range, mae_losses, label='MAE', linewidth=2, color='orange')
    axes[0, 1].set_title('Mean Absolute Error (MAE)')
    axes[0, 1].set_xlabel('Prediction Error')
    axes[0, 1].set_ylabel('Loss')
    axes[0, 1].grid(True)
    axes[0, 1].axvline(x=0, color='r', linestyle='--', label='True value')
    axes[0, 1].legend()
    
    # Plot 3: MSE vs MAE comparison
    axes[1, 0].plot(y_pred_range, mse_losses, label='MSE', linewidth=2)
    axes[1, 0].plot(y_pred_range, mae_losses, label='MAE', linewidth=2)
    axes[1, 0].set_title('MSE vs MAE')
    axes[1, 0].set_xlabel('Prediction Error')
    axes[1, 0].set_ylabel('Loss')
    axes[1, 0].grid(True)
    axes[1, 0].axvline(x=0, color='r', linestyle='--')
    axes[1, 0].legend()
    
    # Plot 4: Binary Cross-Entropy
    y_pred_prob = np.linspace(0.01, 0.99, 200)
    bce_y1 = -np.log(y_pred_prob)  # When y_true = 1
    bce_y0 = -np.log(1 - y_pred_prob)  # When y_true = 0
    
    axes[1, 1].plot(y_pred_prob, bce_y1, label='y_true = 1', linewidth=2)
    axes[1, 1].plot(y_pred_prob, bce_y0, label='y_true = 0', linewidth=2)
    axes[1, 1].set_title('Binary Cross-Entropy')
    axes[1, 1].set_xlabel('Predicted Probability')
    axes[1, 1].set_ylabel('Loss')
    axes[1, 1].grid(True)
    axes[1, 1].legend()
    
    plt.tight_layout()
    plt.show()
    
    print("\n📊 LOSS FUNCTION GUIDE:")
    
    print("\n1. MEAN SQUARED ERROR (MSE):")
    print("   ✅ Use: Regression problems")
    print("   ➕ Pro: Smooth gradient, easy to optimize")
    print("   ➖ Con: Sensitive to outliers (squares errors)")
    
    print("\n2. MEAN ABSOLUTE ERROR (MAE):")
    print("   ✅ Use: Regression with outliers")
    print("   ➕ Pro: Robust to outliers")
    print("   ➖ Con: Not smooth at zero (gradient issues)")
    
    print("\n3. BINARY CROSS-ENTROPY:")
    print("   ✅ Use: Binary classification")
    print("   ➕ Pro: Natural choice for probabilities")
    print("   ➖ Con: Only for binary problems")
    
    print("\n4. CATEGORICAL CROSS-ENTROPY:")
    print("   ✅ Use: Multi-class classification")
    print("   ➕ Pro: Works with softmax output")
    
    print("\n5. HUBER LOSS:")
    print("   ✅ Use: Regression with some outliers")
    print("   ➕ Pro: Combines MSE and MAE (best of both)")
    
    print("\n6. HINGE LOSS:")
    print("   ✅ Use: SVM, margin-based classification")
    print("   ➕ Pro: Maximizes margin between classes")

visualize_losses()
```

---

## 14. Optimizers from Scratch

```python
class Optimizers:
    """
    All optimization algorithms from scratch
    """
    
    class SGD:
        """
        Stochastic Gradient Descent
        Simplest optimizer
        """
        def __init__(self, learning_rate=0.01):
            self.lr = learning_rate
        
        def update(self, params, grads):
            """Update parameters"""
            for param, grad in zip(params, grads):
                param -= self.lr * grad
    
    class SGDMomentum:
        """
        SGD with Momentum
        Accelerates in relevant direction
        """
        def __init__(self, learning_rate=0.01, momentum=0.9):
            self.lr = learning_rate
            self.momentum = momentum
            self.velocity = None
        
        def update(self, params, grads):
            if self.velocity is None:
                self.velocity = [np.zeros_like(p) for p in params]
            
            for i, (param, grad) in enumerate(zip(params, grads)):
                # v = β·v - α·∇L
                self.velocity[i] = self.momentum * self.velocity[i] - self.lr * grad
                # θ = θ + v
                param += self.velocity[i]
    
    class AdaGrad:
        """
        Adaptive Gradient
        Adapts learning rate per parameter
        """
        def __init__(self, learning_rate=0.01, epsilon=1e-8):
            self.lr = learning_rate
            self.epsilon = epsilon
            self.accumulated_grad = None
        
        def update(self, params, grads):
            if self.accumulated_grad is None:
                self.accumulated_grad = [np.zeros_like(p) for p in params]
            
            for i, (param, grad) in enumerate(zip(params, grads)):
                # Accumulate squared gradients
                self.accumulated_grad[i] += grad ** 2
                # Update with adaptive learning rate
                param -= self.lr * grad / (np.sqrt(self.accumulated_grad[i]) + self.epsilon)
    
    class RMSprop:
        """
        Root Mean Square Propagation
        Fixes AdaGrad's aggressive learning rate decay
        """
        def __init__(self, learning_rate=0.001, decay_rate=0.9, epsilon=1e-8):
            self.lr = learning_rate
            self.decay_rate = decay_rate
            self.epsilon = epsilon
            self.cache = None
        
        def update(self, params, grads):
            if self.cache is None:
                self.cache = [np.zeros_like(p) for p in params]
            
            for i, (param, grad) in enumerate(zip(params, grads)):
                # Moving average of squared gradients
                self.cache[i] = self.decay_rate * self.cache[i] + (1 - self.decay_rate) * grad ** 2
                # Update
                param -= self.lr * grad / (np.sqrt(self.cache[i]) + self.epsilon)
    
    class Adam:
        """
        Adaptive Moment Estimation
        Combines momentum and RMSprop
        Most popular optimizer!
        """
        def __init__(self, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8):
            self.lr = learning_rate
            self.beta1 = beta1  # Decay rate for first moment
            self.beta2 = beta2  # Decay rate for second moment
            self.epsilon = epsilon
            self.m = None  # First moment (mean)
            self.v = None  # Second moment (variance)
            self.t = 0     # Time step
        
        def update(self, params, grads):
            if self.m is None:
                self.m = [np.zeros_like(p) for p in params]
                self.v = [np.zeros_like(p) for p in params]
            
            self.t += 1
            
            for i, (param, grad) in enumerate(zip(params, grads)):
                # Update first moment (momentum)
                self.m[i] = self.beta1 * self.m[i] + (1 - self.beta1) * grad
                
                # Update second moment (RMSprop)
                self.v[i] = self.beta2 * self.v[i] + (1 - self.beta2) * grad ** 2
                
                # Bias correction
                m_hat = self.m[i] / (1 - self.beta1 ** self.t)
                v_hat = self.v[i] / (1 - self.beta2 ** self.t)
                
                # Update parameters
                param -= self.lr * m_hat / (np.sqrt(v_hat) + self.epsilon)


# Compare optimizers
def compare_optimizers():
    """
    Visually compare different optimizers
    """
    print("\n" + "=" * 70)
    print("OPTIMIZERS COMPARISON")
    print("=" * 70)
    
    # Simple 2D optimization problem
    def objective(x, y):
        """Rosenbrock function - challenging to optimize"""
        return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2
    
    def gradient(x, y):
        """Gradient of Rosenbrock function"""
        dx = -2 * (1 - x) - 400 * x * (y - x ** 2)
        dy = 200 * (y - x ** 2)
        return np.array([dx, dy])
    
    # Initialize different optimizers
    optimizers = {
        'SGD': Optimizers.SGD(learning_rate=0.001),
        'SGD Momentum': Optimizers.SGDMomentum(learning_rate=0.001, momentum=0.9),
        'AdaGrad': Optimizers.AdaGrad(learning_rate=0.1),
        'RMSprop': Optimizers.RMSprop(learning_rate=0.01),
        'Adam': Optimizers.Adam(learning_rate=0.01)
    }
    
    # Run optimization
    n_steps = 200
    paths = {}
    
    for name, opt in optimizers.items():
        position = np.array([-1.0, 2.0])  # Starting point
        path = [position.copy()]
        
        for _ in range(n_steps):
            grad = gradient(position[0], position[1])
            opt.update([position], [grad])
            path.append(position.copy())
        
        paths[name] = np.array(path)
        print(f"{name}: Final position = ({position[0]:.3f}, {position[1]:.3f})")
    
    # Visualize
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.ravel()
    
    # Create contour plot
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-1, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = objective(X, Y)
    
    for idx, (name, path) in enumerate(paths.items()):
        axes[idx].contour(X, Y, Z, levels=np.logspace(-1, 3, 20), cmap='viridis')
        axes[idx].plot(path[:, 0], path[:, 1], 'r.-', alpha=0.7, markersize=3)
        axes[idx].plot(1, 1, 'g*', markersize=20, label='Optimum')
        axes[idx].plot(path[0, 0], path[0, 1], 'ro', markersize=10, label='Start')
        axes[idx].set_title(f'{name}')
        axes[idx].set_xlabel('x')
        axes[idx].set_ylabel('y')
        axes[idx].legend()
        axes[idx].grid(True, alpha=0.3)
    
    # Hide extra subplot
    axes[5].axis('off')
    
    plt.tight_layout()
    plt.show()
    
    print("\n📊 OPTIMIZER GUIDE:")
    
    print("\n1. SGD (Stochastic Gradient Descent):")
    print("   ✅ Use: Simple problems, well-tuned learning rate")
    print("   ➕ Pro: Simple, memory efficient")
    print("   ➖ Con: Slow, can get stuck in local minima")
    
    print("\n2. SGD WITH MOMENTUM:")
    print("   ✅ Use: When SGD oscillates or is slow")
    print("   ➕ Pro: Faster convergence, dampens oscillations")
    print("   ➖ Con: One more hyperparameter (momentum)")
    
    print("\n3. ADAGRAD:")
    print("   ✅ Use: Sparse data, NLP tasks")
    print("   ➕ Pro: No manual learning rate tuning")
    print("   ➖ Con: Learning rate decays too aggressively")
    
    print("\n4. RMSPROP:")
    print("   ✅ Use: RNNs, non-stationary problems")
    print("   ➕ Pro: Fixes AdaGrad's decay problem")
    print("   ➖ Con: Still sensitive to learning rate")
    
    print("\n5. ADAM (Most Popular!):")
    print("   ✅ Use: Default choice for most problems!")
    print("   ➕ Pro: Combines momentum + RMSprop")
    print("   ➕ Pro: Works well out-of-the-box")
    print("   ➕ Pro: Little hyperparameter tuning needed")
    print("   ➖ Con: Can sometimes generalize worse than SGD")
    
    print("\n💡 RECOMMENDATION:")
    print("   - Start with Adam (lr=0.001)")
    print("   - If overfitting: Try SGD with momentum")
    print("   - If RNNs: Try RMSprop")

compare_optimizers()
```

---

## Summary: What You've Built from Scratch

```python
print("\n" + "=" * 70)
print("🎉 CONGRATULATIONS! YOU'VE BUILT FROM SCRATCH:")
print("=" * 70)

achievements = {
    "Traditional ML": [
        "✅ Linear Regression",
        "✅ Logistic Regression", 
        "✅ Decision Trees",
        "✅ Random Forests"
    ],
    "Neural Networks": [
        "✅ Multi-layer Perceptron",
        "✅ Backpropagation",
        "✅ 6 Activation Functions",
        "✅ 6 Loss Functions",
        "✅ 5 Optimizers"
    ],
    "Key Concepts": [
        "✅ Gradient Descent",
        "✅ Forward Propagation",
        "✅ Backward Propagation",
        "✅ Weight Initialization",
        "✅ Regularization"
    ]
}

for category, items in achievements.items():
    print(f"\n{category}:")
    for item in items:
        print(f"  {item}")

print("\n" + "=" * 70)
print("NEXT STEPS:")
print("=" * 70)
print("""
1. Implement CNNs from scratch for image recognition
2. Build RNNs/LSTMs for sequence data
3. Create Transformers for NLP tasks
4. Add regularization techniques (L1, L2, Dropout)
5. Implement batch normalization
6. Build custom model architectures
7. Optimize for production deployment

Keep practicing and building! 🚀
""")
```

---

## Quick Reference Guide

### When to Use Which Algorithm?

| Problem Type | Algorithm | Why? |
|--------------|-----------|------|
| Linear Regression | Simple relationship | Fast, interpretable |
| Logistic Regression | Binary classification | Probabilistic output |
| Decision Trees | Non-linear, interpretable | Visual, handles non-linearity |
| Random Forest | Complex, prevent overfit | Ensemble reduces variance |
| Neural Networks | Complex patterns | Universal function approximator |
| Deep Learning | Images, text, audio | Learns hierarchical features |

### Activation Function Choice

| Layer | Activation | Reason |
|-------|------------|--------|
| Hidden (default) | ReLU | Fast, no vanishing gradient |
| Hidden (alternative) | Leaky ReLU | Fixes dying ReLU |
| Output (regression) | Linear | Unbounded output |
| Output (binary) | Sigmoid | Probability (0-1) |
| Output (multi-class) | Softmax | Probabilities sum to 1 |

### Optimizer Choice

| Scenario | Optimizer | Learning Rate |
|----------|-----------|---------------|
| Default choice | Adam | 0.001 |
| Fine-tuning | SGD + Momentum | 0.01 |
| RNNs | RMSprop | 0.001 |
| Sparse data | AdaGrad | 0.01 |

---

# Part 3: Deep Learning Architectures

## 15. Convolutional Neural Networks (CNN) from Scratch

### Understanding Convolution

**Simple Explanation:** Instead of looking at the entire image, look at small patches and detect patterns (edges, corners, textures).

**Mathematical Operation:**
```
Output(i,j) = Σ Σ Input(i+m, j+n) × Kernel(m, n)
```

### CNN Layers from Scratch

```python
class Conv2D:
    """
    2D Convolution Layer from scratch
    """
    
    def __init__(self, in_channels, out_channels, kernel_size=3, stride=1, padding=0):
        """
        Parameters:
        -----------
        in_channels : int
            Number of input channels (e.g., 3 for RGB)
        out_channels : int
            Number of filters/kernels
        kernel_size : int
            Size of the convolution kernel (kernel_size × kernel_size)
        stride : int
            Step size for moving the kernel
        padding : int
            Zero-padding around the input
        """
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        
        # Initialize kernels (filters) with He initialization
        self.kernels = np.random.randn(
            out_channels, in_channels, kernel_size, kernel_size
        ) * np.sqrt(2.0 / (in_channels * kernel_size * kernel_size))
        
        self.bias = np.zeros(out_channels)
    
    def forward(self, input_data):
        """
        Forward pass through convolution layer
        
        Parameters:
        -----------
        input_data : numpy array of shape (batch_size, in_channels, height, width)
        
        Returns:
        --------
        output : numpy array of shape (batch_size, out_channels, out_height, out_width)
        """
        self.input = input_data
        batch_size, in_channels, in_height, in_width = input_data.shape
        
        # Add padding
        if self.padding > 0:
            input_padded = np.pad(
                input_data,
                ((0, 0), (0, 0), (self.padding, self.padding), (self.padding, self.padding)),
                mode='constant'
            )
        else:
            input_padded = input_data
        
        # Calculate output dimensions
        out_height = (in_height + 2 * self.padding - self.kernel_size) // self.stride + 1
        out_width = (in_width + 2 * self.padding - self.kernel_size) // self.stride + 1
        
        # Initialize output
        output = np.zeros((batch_size, self.out_channels, out_height, out_width))
        
        # Perform convolution
        for b in range(batch_size):
            for f in range(self.out_channels):
                for i in range(0, out_height):
                    for j in range(0, out_width):
                        # Extract the region
                        h_start = i * self.stride
                        h_end = h_start + self.kernel_size
                        w_start = j * self.stride
                        w_end = w_start + self.kernel_size
                        
                        region = input_padded[b, :, h_start:h_end, w_start:w_end]
                        
                        # Convolution: element-wise multiply and sum
                        output[b, f, i, j] = np.sum(region * self.kernels[f]) + self.bias[f]
        
        return output
    
    def __repr__(self):
        return f"Conv2D(in={self.in_channels}, out={self.out_channels}, " \
               f"kernel={self.kernel_size}, stride={self.stride}, padding={self.padding})"


class MaxPool2D:
    """
    Max Pooling Layer from scratch
    """
    
    def __init__(self, pool_size=2, stride=2):
        self.pool_size = pool_size
        self.stride = stride
    
    def forward(self, input_data):
        """
        Forward pass through max pooling
        
        Reduces spatial dimensions by taking maximum value in each pool
        """
        self.input = input_data
        batch_size, channels, in_height, in_width = input_data.shape
        
        # Calculate output dimensions
        out_height = (in_height - self.pool_size) // self.stride + 1
        out_width = (in_width - self.pool_size) // self.stride + 1
        
        # Initialize output
        output = np.zeros((batch_size, channels, out_height, out_width))
        
        # Perform max pooling
        for b in range(batch_size):
            for c in range(channels):
                for i in range(out_height):
                    for j in range(out_width):
                        h_start = i * self.stride
                        h_end = h_start + self.pool_size
                        w_start = j * self.stride
                        w_end = w_start + self.pool_size
                        
                        # Take maximum
                        region = input_data[b, c, h_start:h_end, w_start:w_end]
                        output[b, c, i, j] = np.max(region)
        
        return output
    
    def __repr__(self):
        return f"MaxPool2D(pool_size={self.pool_size}, stride={self.stride})"


class Flatten:
    """
    Flatten multi-dimensional input into 1D
    """
    
    def forward(self, input_data):
        self.input_shape = input_data.shape
        batch_size = input_data.shape[0]
        return input_data.reshape(batch_size, -1)
    
    def __repr__(self):
        return "Flatten()"


# ============================================
# DEMO: Understanding Convolution
# ============================================

print("\n" + "=" * 70)
print("UNDERSTANDING CONVOLUTION OPERATION")
print("=" * 70)

# Create a simple image (5x5) with an edge
image = np.array([
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1]
]).astype(float)

# Edge detection kernel (vertical edge)
kernel_vertical = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

# Edge detection kernel (horizontal edge)
kernel_horizontal = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])

def apply_convolution(image, kernel):
    """Apply convolution manually to understand the operation"""
    k_height, k_width = kernel.shape
    i_height, i_width = image.shape
    
    output_height = i_height - k_height + 1
    output_width = i_width - k_width + 1
    
    output = np.zeros((output_height, output_width))
    
    for i in range(output_height):
        for j in range(output_width):
            region = image[i:i+k_height, j:j+k_width]
            output[i, j] = np.sum(region * kernel)
    
    return output

# Apply kernels
vertical_edges = apply_convolution(image, kernel_vertical)
horizontal_edges = apply_convolution(image, kernel_horizontal)

print("\n1. Original Image (5×5):")
print(image.astype(int))

print("\n2. Vertical Edge Detection Kernel:")
print(kernel_vertical)

print("\n3. Output after Vertical Edge Detection:")
print(vertical_edges)
print("   → Strong response (positive values) at the vertical edge!")

# Visualize
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

axes[0, 0].imshow(image, cmap='gray')
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')

axes[0, 1].imshow(kernel_vertical, cmap='RdBu')
axes[0, 1].set_title('Vertical Edge Kernel')
axes[0, 1].axis('off')

axes[0, 2].imshow(vertical_edges, cmap='RdBu')
axes[0, 2].set_title('Vertical Edges Detected')
axes[0, 2].axis('off')

axes[1, 0].imshow(image, cmap='gray')
axes[1, 0].set_title('Original Image')
axes[1, 0].axis('off')

axes[1, 1].imshow(kernel_horizontal, cmap='RdBu')
axes[1, 1].set_title('Horizontal Edge Kernel')
axes[1, 1].axis('off')

axes[1, 2].imshow(horizontal_edges, cmap='RdBu')
axes[1, 2].set_title('Horizontal Edges Detected')
axes[1, 2].axis('off')

plt.tight_layout()
plt.show()

print("\n💡 KEY INSIGHTS:")
print("   - Convolution detects patterns in images")
print("   - Different kernels detect different features")
print("   - Neural networks LEARN these kernels automatically!")
```

### Complete CNN Architecture: LeNet-5

```python
class SimpleCNN:
    """
    Simple CNN for digit recognition (like LeNet-5)
    Architecture: Conv → Pool → Conv → Pool → FC → FC
    """
    
    def __init__(self):
        """
        Initialize layers for MNIST-like images (28×28)
        """
        # Layer 1: Convolution
        self.conv1 = Conv2D(in_channels=1, out_channels=6, kernel_size=5, padding=2)
        self.pool1 = MaxPool2D(pool_size=2, stride=2)
        
        # Layer 2: Convolution
        self.conv2 = Conv2D(in_channels=6, out_channels=16, kernel_size=5)
        self.pool2 = MaxPool2D(pool_size=2, stride=2)
        
        # Flatten
        self.flatten = Flatten()
        
        # Fully connected layers
        self.fc1_weights = np.random.randn(16 * 5 * 5, 120) * 0.01
        self.fc1_bias = np.zeros(120)
        
        self.fc2_weights = np.random.randn(120, 84) * 0.01
        self.fc2_bias = np.zeros(84)
        
        self.fc3_weights = np.random.randn(84, 10) * 0.01
        self.fc3_bias = np.zeros(10)
    
    def relu(self, x):
        return np.maximum(0, x)
    
    def softmax(self, x):
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)
    
    def forward(self, x):
        """
        Forward pass through the network
        
        Parameters:
        -----------
        x : numpy array of shape (batch_size, 1, 28, 28)
            Input images
        
        Returns:
        --------
        output : numpy array of shape (batch_size, 10)
            Class probabilities
        """
        # Conv1 → ReLU → Pool
        x = self.conv1.forward(x)
        x = self.relu(x)
        x = self.pool1.forward(x)
        
        # Conv2 → ReLU → Pool
        x = self.conv2.forward(x)
        x = self.relu(x)
        x = self.pool2.forward(x)
        
        # Flatten
        x = self.flatten.forward(x)
        
        # FC1 → ReLU
        x = np.dot(x, self.fc1_weights) + self.fc1_bias
        x = self.relu(x)
        
        # FC2 → ReLU
        x = np.dot(x, self.fc2_weights) + self.fc2_bias
        x = self.relu(x)
        
        # FC3 → Softmax
        x = np.dot(x, self.fc3_weights) + self.fc3_bias
        x = self.softmax(x)
        
        return x
    
    def predict(self, x):
        """Get predicted class"""
        probs = self.forward(x)
        return np.argmax(probs, axis=1)


# ============================================
# TEST CNN ON MNIST-LIKE DATA
# ============================================

print("\n" + "=" * 70)
print("SIMPLE CNN ARCHITECTURE DEMO")
print("=" * 70)

# Create CNN
cnn = SimpleCNN()

print("\n🏗️ CNN Architecture:")
print("=" * 50)
print(f"1. {cnn.conv1}")
print(f"2. ReLU")
print(f"3. {cnn.pool1}")
print(f"4. {cnn.conv2}")
print(f"5. ReLU")
print(f"6. {cnn.pool2}")
print(f"7. {cnn.flatten}")
print(f"8. Fully Connected: 400 → 120")
print(f"9. ReLU")
print(f"10. Fully Connected: 120 → 84")
print(f"11. ReLU")
print(f"12. Fully Connected: 84 → 10")
print(f"13. Softmax")

# Create dummy input (batch of 2 images)
dummy_input = np.random.randn(2, 1, 28, 28)

print(f"\n📊 Forward Pass:")
print(f"Input shape: {dummy_input.shape}")

# Forward pass
output = cnn.forward(dummy_input)

print(f"Output shape: {output.shape}")
print(f"\nPredicted classes: {cnn.predict(dummy_input)}")
print(f"\nClass probabilities (first sample):")
for i, prob in enumerate(output[0]):
    print(f"  Class {i}: {prob:.4f}")

print("\n✅ CNN architecture working!")
```

### Real-World Example: Image Classification

```python
def create_simple_digit_images():
    """
    Create simple synthetic digit-like images for demonstration
    """
    print("\n" + "=" * 70)
    print("CNN IMAGE CLASSIFICATION DEMO")
    print("=" * 70)
    
    # Create synthetic "digits"
    images = []
    labels = []
    
    # "0" - circle
    img_0 = np.zeros((28, 28))
    for i in range(28):
        for j in range(28):
            if 8 <= np.sqrt((i-14)**2 + (j-14)**2) <= 12:
                img_0[i, j] = 1
    
    # "1" - vertical line
    img_1 = np.zeros((28, 28))
    img_1[:, 13:15] = 1
    
    # "7" - diagonal line
    img_7 = np.zeros((28, 28))
    for i in range(28):
        j = int(i * 0.8 + 7)
        if 0 <= j < 28:
            img_7[i, j:j+2] = 1
    
    # Create dataset with some variation
    for _ in range(10):
        # Add noise
        images.append(img_0 + np.random.randn(28, 28) * 0.1)
        labels.append(0)
        
        images.append(img_1 + np.random.randn(28, 28) * 0.1)
        labels.append(1)
        
        images.append(img_7 + np.random.randn(28, 28) * 0.1)
        labels.append(7)
    
    images = np.array(images)
    labels = np.array(labels)
    
    # Reshape for CNN (batch, channels, height, width)
    images = images.reshape(-1, 1, 28, 28)
    
    # Visualize samples
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    
    axes[0].imshow(img_0, cmap='gray')
    axes[0].set_title('Synthetic "0"')
    axes[0].axis('off')
    
    axes[1].imshow(img_1, cmap='gray')
    axes[1].set_title('Synthetic "1"')
    axes[1].axis('off')
    
    axes[2].imshow(img_7, cmap='gray')
    axes[2].set_title('Synthetic "7"')
    axes[2].axis('off')
    
    plt.tight_layout()
    plt.show()
    
    print(f"\n✅ Created dataset:")
    print(f"   Images: {images.shape}")
    print(f"   Labels: {labels.shape}")
    print(f"   Classes: {np.unique(labels)}")
    
    return images, labels

# Create and test
images, labels = create_simple_digit_images()

# Make predictions
cnn = SimpleCNN()
predictions = cnn.predict(images[:5])

print(f"\n🔮 Predictions (random weights, not trained):")
for i in range(5):
    print(f"   Image {i}: True={labels[i]}, Predicted={predictions[i]}")

print("\n💡 NOTE: CNN would need training to make accurate predictions!")
print("   This demo shows the architecture and forward pass.")
```

---

## 16. Recurrent Neural Networks (RNN) from Scratch

### Understanding RNNs

**Simple Explanation:** Process sequences one step at a time, maintaining a "memory" of what it has seen before.

**Key Concepts:**
- **Hidden State**: Memory that persists across time steps
- **Temporal Dependencies**: Understanding context from previous inputs
- **Sequence Processing**: Handle variable-length inputs

### Implementation

```python
class VanillaRNN:
    """
    Vanilla RNN from scratch
    For sequence processing tasks
    """
    
    def __init__(self, input_size, hidden_size, output_size):
        """
        Parameters:
        -----------
        input_size : int
            Dimension of input at each time step
        hidden_size : int
            Dimension of hidden state
        output_size : int
            Dimension of output
        """
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights (Xavier initialization)
        scale_i = np.sqrt(2.0 / (input_size + hidden_size))
        scale_h = np.sqrt(2.0 / (hidden_size + hidden_size))
        scale_o = np.sqrt(2.0 / (hidden_size + output_size))
        
        # Input to hidden
        self.W_ih = np.random.randn(input_size, hidden_size) * scale_i
        
        # Hidden to hidden (recurrent weights)
        self.W_hh = np.random.randn(hidden_size, hidden_size) * scale_h
        
        # Hidden to output
        self.W_ho = np.random.randn(hidden_size, output_size) * scale_o
        
        # Biases
        self.b_h = np.zeros((1, hidden_size))
        self.b_o = np.zeros((1, output_size))
    
    def tanh(self, x):
        """Tanh activation"""
        return np.tanh(x)
    
    def softmax(self, x):
        """Softmax activation"""
        exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=-1, keepdims=True)
    
    def forward(self, inputs, h_prev=None):
        """
        Forward pass through RNN
        
        Parameters:
        -----------
        inputs : numpy array of shape (batch_size, seq_length, input_size)
        h_prev : numpy array of shape (batch_size, hidden_size)
            Previous hidden state (if None, initialize with zeros)
        
        Returns:
        --------
        outputs : list of output at each time step
        hidden_states : list of hidden states at each time step
        """
        batch_size, seq_length, _ = inputs.shape
        
        # Initialize hidden state if not provided
        if h_prev is None:
            h_prev = np.zeros((batch_size, self.hidden_size))
        
        outputs = []
        hidden_states = [h_prev]
        
        # Process sequence step by step
        for t in range(seq_length):
            # Get input at current time step
            x_t = inputs[:, t, :]  # Shape: (batch_size, input_size)
            
            # RNN formula:
            # h_t = tanh(x_t @ W_ih + h_{t-1} @ W_hh + b_h)
            h_t = self.tanh(
                np.dot(x_t, self.W_ih) +
                np.dot(h_prev, self.W_hh) +
                self.b_h
            )
            
            # Output at time t:
            # y_t = h_t @ W_ho + b_o
            y_t = np.dot(h_t, self.W_ho) + self.b_o
            y_t = self.softmax(y_t)
            
            outputs.append(y_t)
            hidden_states.append(h_t)
            
            # Update hidden state
            h_prev = h_t
        
        return outputs, hidden_states
    
    def predict(self, inputs):
        """Get predictions for sequence"""
        outputs, _ = self.forward(inputs)
        # Return last output (for sequence classification)
        return np.argmax(outputs[-1], axis=1)


# ============================================
# VISUALIZE RNN COMPUTATION
# ============================================

print("\n" + "=" * 70)
print("RNN ARCHITECTURE & COMPUTATION")
print("=" * 70)

print("""
RNN UNROLLED IN TIME:

   Input:    x₀      x₁      x₂      x₃
              ↓       ↓       ↓       ↓
   Hidden:  [h₀] → [h₁] → [h₂] → [h₃]
              ↓       ↓       ↓       ↓
   Output:   y₀      y₁      y₂      y₃

At each time step t:
   h_t = tanh(x_t @ W_ih + h_{t-1} @ W_hh + b_h)
   y_t = softmax(h_t @ W_ho + b_o)

Key Points:
✅ Same weights (W_ih, W_hh, W_ho) used at all time steps
✅ Hidden state h_t carries information from previous steps
✅ Can process variable-length sequences
""")

# Create RNN
rnn = VanillaRNN(input_size=10, hidden_size=20, output_size=5)

print(f"\n🏗️ RNN Configuration:")
print(f"   Input size: {rnn.input_size}")
print(f"   Hidden size: {rnn.hidden_size}")
print(f"   Output size: {rnn.output_size}")
print(f"\n   Parameters:")
print(f"   - W_ih: {rnn.W_ih.shape} (input → hidden)")
print(f"   - W_hh: {rnn.W_hh.shape} (hidden → hidden)")
print(f"   - W_ho: {rnn.W_ho.shape} (hidden → output)")

# Test with dummy sequence
batch_size = 2
seq_length = 5
dummy_sequence = np.random.randn(batch_size, seq_length, 10)

print(f"\n📊 Forward Pass:")
print(f"   Input shape: {dummy_sequence.shape}")

outputs, hidden_states = rnn.forward(dummy_sequence)

print(f"   Number of outputs: {len(outputs)}")
print(f"   Output shape at each step: {outputs[0].shape}")
print(f"   Number of hidden states: {len(hidden_states)}")
print(f"   Hidden state shape: {hidden_states[0].shape}")

print(f"\n🔮 Predictions: {rnn.predict(dummy_sequence)}")

print("\n✅ RNN forward pass complete!")
```

### RNN Applications: Sentiment Analysis

```python
class SentimentRNN:
    """
    RNN for sentiment analysis (positive/negative)
    """
    
    def __init__(self, vocab_size, embedding_dim=50, hidden_size=128):
        """
        Parameters:
        -----------
        vocab_size : int
            Size of vocabulary
        embedding_dim : int
            Dimension of word embeddings
        hidden_size : int
            Size of RNN hidden state
        """
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.hidden_size = hidden_size
        
        # Embedding layer (maps words to vectors)
        self.embeddings = np.random.randn(vocab_size, embedding_dim) * 0.01
        
        # RNN
        self.rnn = VanillaRNN(
            input_size=embedding_dim,
            hidden_size=hidden_size,
            output_size=2  # Binary: positive/negative
        )
    
    def embed_sequence(self, sequence):
        """
        Convert sequence of word indices to embeddings
        
        Parameters:
        -----------
        sequence : numpy array of shape (batch_size, seq_length)
            Word indices
        
        Returns:
        --------
        embedded : numpy array of shape (batch_size, seq_length, embedding_dim)
        """
        batch_size, seq_length = sequence.shape
        embedded = np.zeros((batch_size, seq_length, self.embedding_dim))
        
        for i in range(batch_size):
            for t in range(seq_length):
                word_idx = sequence[i, t]
                embedded[i, t] = self.embeddings[word_idx]
        
        return embedded
    
    def predict_sentiment(self, sequence):
        """
        Predict sentiment for text sequence
        
        Returns:
        --------
        sentiment : 0 (negative) or 1 (positive)
        probability : confidence of prediction
        """
        # Embed words
        embedded = self.embed_sequence(sequence)
        
        # Pass through RNN
        outputs, _ = self.rnn.forward(embedded)
        
        # Use last output for classification
        final_output = outputs[-1]
        
        sentiment = np.argmax(final_output, axis=1)
        probability = np.max(final_output, axis=1)
        
        return sentiment, probability


# ============================================
# DEMO: SENTIMENT ANALYSIS
# ============================================

print("\n" + "=" * 70)
print("RNN SENTIMENT ANALYSIS DEMO")
print("=" * 70)

# Simple vocabulary
vocab = {
    'great': 1, 'good': 2, 'excellent': 3, 'amazing': 4, 'love': 5,
    'bad': 6, 'terrible': 7, 'awful': 8, 'hate': 9, 'worst': 10,
    'movie': 11, 'film': 12, 'this': 13, 'is': 14, 'the': 15,
    '<PAD>': 0  # Padding token
}

# Example sentences (as word indices)
sentences = [
    [13, 14, 1, 11],      # "this is great movie"
    [13, 11, 14, 7],      # "this movie is terrible"
    [4, 12],              # "amazing film"
    [9, 13, 11]           # "hate this movie"
]

# Pad sequences to same length
max_len = max(len(s) for s in sentences)
padded = np.array([s + [0] * (max_len - len(s)) for s in sentences])

print("\n📝 Example Sentences (as word indices):")
print(padded)

# Create sentiment model
sentiment_model = SentimentRNN(vocab_size=len(vocab), embedding_dim=50, hidden_size=64)

print(f"\n🏗️ Sentiment RNN Architecture:")
print(f"   Vocabulary size: {len(vocab)}")
print(f"   Embedding dimension: {sentiment_model.embedding_dim}")
print(f"   Hidden size: {sentiment_model.hidden_size}")
print(f"   Output: 2 classes (negative=0, positive=1)")

# Make predictions
sentiments, probabilities = sentiment_model.predict_sentiment(padded)

print(f"\n🔮 Predictions (untrained model):")
sentence_texts = [
    "this is great movie",
    "this movie is terrible",
    "amazing film",
    "hate this movie"
]

for i, text in enumerate(sentence_texts):
    sentiment_label = "Positive 😊" if sentiments[i] == 1 else "Negative 😞"
    print(f"   '{text}': {sentiment_label} (confidence: {probabilities[i]:.2f})")

print("\n💡 NOTE: Model needs training to make accurate predictions!")
print("   This demonstrates the RNN architecture for NLP tasks.")
```

---

## 17. Long Short-Term Memory (LSTM) from Scratch

### Understanding LSTM

**Simple Explanation:** Advanced RNN that can remember information for long sequences by using "gates" that control what to remember and forget.

**Key Innovation:** Solves the vanishing gradient problem of vanilla RNNs.

### LSTM Architecture

```python
class LSTMCell:
    """
    Single LSTM cell from scratch
    
    LSTM has 4 gates:
    1. Forget gate: What to forget from previous memory
    2. Input gate: What new information to store
    3. Output gate: What to output
    4. Cell gate: Candidate values to add to memory
    """
    
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        
        # Initialize weights for all 4 gates
        # Each gate has weights for input (x) and hidden state (h)
        scale = np.sqrt(2.0 / (input_size + hidden_size))
        
        # Forget gate
        self.W_f = np.random.randn(input_size + hidden_size, hidden_size) * scale
        self.b_f = np.zeros((1, hidden_size))
        
        # Input gate
        self.W_i = np.random.randn(input_size + hidden_size, hidden_size) * scale
        self.b_i = np.zeros((1, hidden_size))
        
        # Cell gate (candidate values)
        self.W_c = np.random.randn(input_size + hidden_size, hidden_size) * scale
        self.b_c = np.zeros((1, hidden_size))
        
        # Output gate
        self.W_o = np.random.randn(input_size + hidden_size, hidden_size) * scale
        self.b_o = np.zeros((1, hidden_size))
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))
    
    def tanh(self, x):
        return np.tanh(x)
    
    def forward(self, x_t, h_prev, c_prev):
        """
        Forward pass through LSTM cell
        
        Parameters:
        -----------
        x_t : numpy array of shape (batch_size, input_size)
            Input at current time step
        h_prev : numpy array of shape (batch_size, hidden_size)
            Previous hidden state
        c_prev : numpy array of shape (batch_size, hidden_size)
            Previous cell state
        
        Returns:
        --------
        h_t : numpy array
            New hidden state
        c_t : numpy array
            New cell state
        """
        # Concatenate input and previous hidden state
        combined = np.concatenate([x_t, h_prev], axis=1)
        
        # 1. Forget gate: What to forget from previous cell state
        # f_t = σ(W_f @ [x_t, h_{t-1}] + b_f)
        f_t = self.sigmoid(np.dot(combined, self.W_f) + self.b_f)
        
        # 2. Input gate: What new information to store
        # i_t = σ(W_i @ [x_t, h_{t-1}] + b_i)
        i_t = self.sigmoid(np.dot(combined, self.W_i) + self.b_i)
        
        # 3. Cell gate: Candidate values to add
        # c̃_t = tanh(W_c @ [x_t, h_{t-1}] + b_c)
        c_tilde = self.tanh(np.dot(combined, self.W_c) + self.b_c)
        
        # 4. Update cell state
        # c_t = f_t ⊙ c_{t-1} + i_t ⊙ c̃_t
        # (forget old + remember new)
        c_t = f_t * c_prev + i_t * c_tilde
        
        # 5. Output gate: What to output
        # o_t = σ(W_o @ [x_t, h_{t-1}] + b_o)
        o_t = self.sigmoid(np.dot(combined, self.W_o) + self.b_o)
        
        # 6. Hidden state
        # h_t = o_t ⊙ tanh(c_t)
        h_t = o_t * self.tanh(c_t)
        
        return h_t, c_t, (f_t, i_t, c_tilde, o_t)  # Return gates for visualization


class LSTM:
    """
    Complete LSTM network
    """
    
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # LSTM cell
        self.cell = LSTMCell(input_size, hidden_size)
        
        # Output layer
        self.W_out = np.random.randn(hidden_size, output_size) * 0.01
        self.b_out = np.zeros((1, output_size))
    
    def softmax(self, x):
        exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=-1, keepdims=True)
    
    def forward(self, inputs, h_prev=None, c_prev=None):
        """
        Forward pass through LSTM
        
        Parameters:
        -----------
        inputs : numpy array of shape (batch_size, seq_length, input_size)
        h_prev, c_prev : Initial hidden and cell states
        
        Returns:
        --------
        outputs : List of outputs at each time step
        hidden_states : List of hidden states
        cell_states : List of cell states
        """
        batch_size, seq_length, _ = inputs.shape
        
        # Initialize states
        if h_prev is None:
            h_prev = np.zeros((batch_size, self.hidden_size))
        if c_prev is None:
            c_prev = np.zeros((batch_size, self.hidden_size))
        
        outputs = []
        hidden_states = []
        cell_states = []
        gate_values = []
        
        # Process sequence
        for t in range(seq_length):
            x_t = inputs[:, t, :]
            
            # LSTM cell forward
            h_t, c_t, gates = self.cell.forward(x_t, h_prev, c_prev)
            
            # Output
            y_t = np.dot(h_t, self.W_out) + self.b_out
            y_t = self.softmax(y_t)
            
            outputs.append(y_t)
            hidden_states.append(h_t)
            cell_states.append(c_t)
            gate_values.append(gates)
            
            # Update states
            h_prev = h_t
            c_prev = c_t
        
        return outputs, hidden_states, cell_states, gate_values


# ============================================
# VISUALIZE LSTM GATES
# ============================================

print("\n" + "=" * 70)
print("LSTM ARCHITECTURE & GATES")
print("=" * 70)

print("""
LSTM CELL STRUCTURE:

         ┌──────────────────────┐
    x_t  │                      │
    ───→ │                      │
         │   ┌───┐  ┌───┐       │
  h_{t-1}│   │ f │  │ i │       │
    ───→ │   └───┘  └───┘       │  h_t
         │     ↓      ↓          │  ───→
  c_{t-1}│   ┌────────────┐     │
    ───→ │───│   c_t      │─────│  c_t
         │   └────────────┘     │  ───→
         │         ↓             │
         │       ┌───┐           │
         │       │ o │           │
         │       └───┘           │
         └──────────────────────┘

Four Gates:
1. Forget gate (f): Decides what to forget from cell state
2. Input gate (i): Decides what new information to store
3. Cell gate (c̃): Creates candidate values
4. Output gate (o): Decides what to output

Key Equations:
   f_t = σ(W_f·[x_t, h_{t-1}] + b_f)    [Forget]
   i_t = σ(W_i·[x_t, h_{t-1}] + b_i)    [Input]
   c̃_t = tanh(W_c·[x_t, h_{t-1}] + b_c) [Candidate]
   c_t = f_t⊙c_{t-1} + i_t⊙c̃_t          [Cell update]
   o_t = σ(W_o·[x_t, h_{t-1}] + b_o)    [Output]
   h_t = o_t⊙tanh(c_t)                  [Hidden state]

💡 Key Advantages over Vanilla RNN:
   ✅ Can learn long-term dependencies
   ✅ Solves vanishing gradient problem
   ✅ Cell state acts as "highway" for information
""")

# Create LSTM
lstm = LSTM(input_size=10, hidden_size=20, output_size=5)

print(f"\n🏗️ LSTM Configuration:")
print(f"   Input size: {lstm.input_size}")
print(f"   Hidden size: {lstm.hidden_size}")
print(f"   Output size: {lstm.output_size}")
print(f"\n   Parameters per cell:")
print(f"   - Forget gate: {lstm.cell.W_f.shape}")
print(f"   - Input gate: {lstm.cell.W_i.shape}")
print(f"   - Cell gate: {lstm.cell.W_c.shape}")
print(f"   - Output gate: {lstm.cell.W_o.shape}")

# Test forward pass
batch_size = 2
seq_length = 5
test_input = np.random.randn(batch_size, seq_length, 10)

print(f"\n📊 Forward Pass:")
outputs, hidden_states, cell_states, gate_values = lstm.forward(test_input)

print(f"   Input: {test_input.shape}")
print(f"   Outputs: {len(outputs)} time steps, each {outputs[0].shape}")
print(f"   Hidden states: {len(hidden_states)} states, each {hidden_states[0].shape}")
print(f"   Cell states: {len(cell_states)} states, each {cell_states[0].shape}")

# Visualize gate activations
print(f"\n🚪 Gate Activations at First Time Step:")
f_t, i_t, c_tilde, o_t = gate_values[0]
print(f"   Forget gate mean: {np.mean(f_t):.3f} (closer to 0 = forget more)")
print(f"   Input gate mean: {np.mean(i_t):.3f} (closer to 1 = remember more)")
print(f"   Output gate mean: {np.mean(o_t):.3f} (closer to 1 = output more)")

print("\n✅ LSTM forward pass complete!")
```

### RNN vs LSTM Comparison

```python
def compare_rnn_lstm():
    """
    Compare vanilla RNN vs LSTM
    """
    print("\n" + "=" * 70)
    print("RNN vs LSTM COMPARISON")
    print("=" * 70)
    
    comparison = pd.DataFrame({
        'Aspect': [
            'Memory Length',
            'Gradient Flow',
            'Parameters',
            'Training Speed',
            'Long Sequences',
            'Short Sequences',
            'Complexity'
        ],
        'Vanilla RNN': [
            'Short-term',
            'Vanishing gradient ❌',
            'Fewer (faster)',
            'Fast',
            'Poor ❌',
            'Good ✅',
            'Simple'
        ],
        'LSTM': [
            'Long-term ✅',
            'Better gradient flow ✅',
            'More (4× weights)',
            'Slower',
            'Excellent ✅',
            'Good ✅',
            'Complex'
        ]
    })
    
    print("\n📊 Feature Comparison:")
    print(comparison.to_string(index=False))
    
    print("\n💡 WHEN TO USE:")
    print("\nVanilla RNN:")
    print("   ✅ Short sequences (< 10 steps)")
    print("   ✅ Simple patterns")
    print("   ✅ Fast training needed")
    print("   ✅ Limited computational resources")
    
    print("\nLSTM:")
    print("   ✅ Long sequences (> 20 steps)")
    print("   ✅ Complex dependencies")
    print("   ✅ Text generation, translation")
    print("   ✅ Time series with long patterns")
    print("   ✅ When accuracy > speed")
    
    print("\n🎯 COMMON APPLICATIONS:")
    print("\nRNN:")
    print("   - Simple sequence classification")
    print("   - Short text sentiment analysis")
    print("   - Basic time series prediction")
    
    print("\nLSTM:")
    print("   - Machine translation")
    print("   - Text generation")
    print("   - Speech recognition")
    print("   - Video analysis")
    print("   - Music composition")
    print("   - Stock price prediction")

compare_rnn_lstm()
```

---

## 19. Transformer Architecture from Scratch

### Understanding Self-Attention

**Simple Explanation:** Instead of processing sequences step-by-step like RNNs, Transformers look at the entire sequence at once and learn which parts are important.

**Key Innovation:** Self-attention mechanism - each word can "attend" to every other word.

```python
class SelfAttention:
    """
    Self-Attention mechanism from scratch
    The heart of Transformers!
    """
    
    def __init__(self, embed_dim, num_heads=1):
        """
        Parameters:
        -----------
        embed_dim : int
            Dimension of input embeddings
        num_heads : int
            Number of attention heads (for multi-head attention)
        """
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        
        # Query, Key, Value weight matrices
        self.W_q = np.random.randn(embed_dim, embed_dim) * 0.01
        self.W_k = np.random.randn(embed_dim, embed_dim) * 0.01
        self.W_v = np.random.randn(embed_dim, embed_dim) * 0.01
        
        # Output projection
        self.W_o = np.random.randn(embed_dim, embed_dim) * 0.01
    
    def scaled_dot_product_attention(self, Q, K, V, mask=None):
        """
        Compute attention: Attention(Q,K,V) = softmax(QK^T/√d_k)V
        
        Parameters:
        -----------
        Q : Query matrix (batch, seq_len, embed_dim)
        K : Key matrix (batch, seq_len, embed_dim)
        V : Value matrix (batch, seq_len, embed_dim)
        mask : Optional mask (prevents attending to certain positions)
        
        Returns:
        --------
        output : Attended values
        attention_weights : Attention scores
        """
        # Calculate attention scores
        # scores = Q @ K^T / √d_k
        d_k = K.shape[-1]
        scores = np.matmul(Q, K.transpose(0, 2, 1)) / np.sqrt(d_k)
        
        # Apply mask if provided (for padding or future positions)
        if mask is not None:
            scores = scores + mask
        
        # Softmax to get attention weights
        # This tells us "how much attention to pay to each position"
        attention_weights = self.softmax(scores)
        
        # Weighted sum of values
        # output = attention_weights @ V
        output = np.matmul(attention_weights, V)
        
        return output, attention_weights
    
    def softmax(self, x):
        """Numerical stable softmax"""
        exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=-1, keepdims=True)
    
    def forward(self, x, mask=None):
        """
        Forward pass through self-attention
        
        Parameters:
        -----------
        x : numpy array of shape (batch_size, seq_length, embed_dim)
        
        Returns:
        --------
        output : Attended output
        attention_weights : Attention scores
        """
        batch_size, seq_length, embed_dim = x.shape
        
        # Linear projections: Q = XW_q, K = XW_k, V = XW_v
        Q = np.dot(x, self.W_q)
        K = np.dot(x, self.W_k)
        V = np.dot(x, self.W_v)
        
        # Compute attention
        output, attention_weights = self.scaled_dot_product_attention(Q, K, V, mask)
        
        # Final linear projection
        output = np.dot(output, self.W_o)
        
        return output, attention_weights


class PositionalEncoding:
    """
    Add position information to embeddings
    Since Transformers don't have inherent notion of order
    """
    
    def __init__(self, max_seq_length, embed_dim):
        """
        Create positional encodings
        PE(pos, 2i) = sin(pos / 10000^(2i/d))
        PE(pos, 2i+1) = cos(pos / 10000^(2i/d))
        """
        self.max_seq_length = max_seq_length
        self.embed_dim = embed_dim
        
        # Create position encodings
        pe = np.zeros((max_seq_length, embed_dim))
        position = np.arange(0, max_seq_length).reshape(-1, 1)
        div_term = np.exp(np.arange(0, embed_dim, 2) * -(np.log(10000.0) / embed_dim))
        
        pe[:, 0::2] = np.sin(position * div_term)
        pe[:, 1::2] = np.cos(position * div_term)
        
        self.pe = pe
    
    def forward(self, x):
        """
        Add positional encoding to input
        
        Parameters:
        -----------
        x : numpy array of shape (batch_size, seq_length, embed_dim)
        """
        batch_size, seq_length, embed_dim = x.shape
        return x + self.pe[:seq_length, :]


# ============================================
# VISUALIZE SELF-ATTENTION
# ============================================

print("\n" + "=" * 70)
print("SELF-ATTENTION MECHANISM")
print("=" * 70)

print("""
HOW SELF-ATTENTION WORKS:

Input Sentence: "The cat sat on the mat"

Step 1: Create Query, Key, Value vectors for each word
   Q = input @ W_q  (What am I looking for?)
   K = input @ W_k  (What do I contain?)
   V = input @ W_v  (What should I output?)

Step 2: Calculate attention scores
   Scores = Q @ K^T / √d_k
   
   This creates a matrix showing how much each word 
   should "attend" to every other word.

Step 3: Apply softmax to get attention weights
   Weights = softmax(Scores)
   
   Now each word has a distribution over all words.

Step 4: Weighted sum of values
   Output = Weights @ V
   
   Each word's output is influenced by all other words!

💡 KEY ADVANTAGES:
   ✅ Parallel computation (unlike RNNs)
   ✅ Captures long-range dependencies easily
   ✅ Attention weights are interpretable
   ✅ No vanishing gradient problem
""")

# Demo self-attention
embed_dim = 64
seq_length = 6

# Create sample input (e.g., embedded words)
sample_input = np.random.randn(1, seq_length, embed_dim)

# Create attention layer
attention = SelfAttention(embed_dim=embed_dim)

print(f"\n🏗️ Self-Attention Configuration:")
print(f"   Embedding dimension: {embed_dim}")
print(f"   Sequence length: {seq_length}")
print(f"   Weight matrices: Q, K, V each {attention.W_q.shape}")

# Forward pass
output, attention_weights = attention.forward(sample_input)

print(f"\n📊 Forward Pass:")
print(f"   Input: {sample_input.shape}")
print(f"   Output: {output.shape}")
print(f"   Attention weights: {attention_weights.shape}")

# Visualize attention weights
plt.figure(figsize=(10, 8))
plt.imshow(attention_weights[0], cmap='viridis', aspect='auto')
plt.colorbar(label='Attention Weight')
plt.xlabel('Key Position')
plt.ylabel('Query Position')
plt.title('Self-Attention Weights Heatmap\n(Shows which positions attend to which)')

# Add grid
for i in range(seq_length + 1):
    plt.axhline(i - 0.5, color='white', linewidth=0.5)
    plt.axvline(i - 0.5, color='white', linewidth=0.5)

plt.tight_layout()
plt.show()

print("\n💡 INTERPRETATION:")
print("   Brighter colors = Stronger attention")
print("   Each row shows what that position attends to")
print("   Diagonal = positions attend to themselves")

print("\n✅ Self-Attention demo complete!")
```

### Simple Transformer Implementation

```python
class TransformerBlock:
    """
    Single Transformer block
    Contains: Self-Attention + Feed-Forward + Layer Norms + Residuals
    """
    
    def __init__(self, embed_dim, num_heads=4, ff_dim=256):
        """
        Parameters:
        -----------
        embed_dim : int
            Embedding dimension
        num_heads : int
            Number of attention heads
        ff_dim : int
            Feed-forward hidden dimension
        """
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        
        # Multi-head self-attention
        self.attention = SelfAttention(embed_dim, num_heads)
        
        # Feed-forward network
        self.ff_W1 = np.random.randn(embed_dim, ff_dim) * 0.01
        self.ff_b1 = np.zeros((1, ff_dim))
        self.ff_W2 = np.random.randn(ff_dim, embed_dim) * 0.01
        self.ff_b2 = np.zeros((1, embed_dim))
        
        # Layer normalization parameters
        self.ln1_gamma = np.ones((1, embed_dim))
        self.ln1_beta = np.zeros((1, embed_dim))
        self.ln2_gamma = np.ones((1, embed_dim))
        self.ln2_beta = np.zeros((1, embed_dim))
    
    def layer_norm(self, x, gamma, beta, epsilon=1e-6):
        """Layer Normalization"""
        mean = np.mean(x, axis=-1, keepdims=True)
        std = np.std(x, axis=-1, keepdims=True)
        return gamma * (x - mean) / (std + epsilon) + beta
    
    def relu(self, x):
        return np.maximum(0, x)
    
    def feed_forward(self, x):
        """
        Feed-forward network: FFN(x) = ReLU(xW1 + b1)W2 + b2
        """
        # First layer
        x = np.dot(x, self.ff_W1) + self.ff_b1
        x = self.relu(x)
        
        # Second layer
        x = np.dot(x, self.ff_W2) + self.ff_b2
        
        return x
    
    def forward(self, x):
        """
        Forward pass through transformer block
        
        Architecture:
        1. Multi-head self-attention
        2. Add & Norm (residual connection + layer norm)
        3. Feed-forward network
        4. Add & Norm
        """
        # Multi-head self-attention + residual + layer norm
        attn_output, attn_weights = self.attention.forward(x)
        x = self.layer_norm(x + attn_output, self.ln1_gamma, self.ln1_beta)  # Add & Norm
        
        # Feed-forward + residual + layer norm
        ff_output = self.feed_forward(x)
        x = self.layer_norm(x + ff_output, self.ln2_gamma, self.ln2_beta)  # Add & Norm
        
        return x, attn_weights


class SimpleTransformer:
    """
    Simple Transformer for sequence classification
    """
    
    def __init__(self, vocab_size, embed_dim=128, num_heads=4, 
                 num_layers=2, max_seq_length=100, num_classes=2):
        """
        Parameters:
        -----------
        vocab_size : int
            Size of vocabulary
        embed_dim : int
            Embedding dimension
        num_heads : int
            Number of attention heads
        num_layers : int
            Number of transformer blocks
        max_seq_length : int
            Maximum sequence length
        num_classes : int
            Number of output classes
        """
        self.vocab_size = vocab_size
        self.embed_dim = embed_dim
        self.num_classes = num_classes
        
        # Token embeddings
        self.token_embeddings = np.random.randn(vocab_size, embed_dim) * 0.01
        
        # Positional encodings
        self.pos_encoding = PositionalEncoding(max_seq_length, embed_dim)
        
        # Transformer blocks
        self.transformer_blocks = [
            TransformerBlock(embed_dim, num_heads) 
            for _ in range(num_layers)
        ]
        
        # Classification head
        self.classifier_W = np.random.randn(embed_dim, num_classes) * 0.01
        self.classifier_b = np.zeros((1, num_classes))
    
    def embed(self, token_ids):
        """
        Convert token IDs to embeddings
        """
        batch_size, seq_length = token_ids.shape
        embeddings = np.zeros((batch_size, seq_length, self.embed_dim))
        
        for i in range(batch_size):
            for j in range(seq_length):
                embeddings[i, j] = self.token_embeddings[token_ids[i, j]]
        
        return embeddings
    
    def softmax(self, x):
        exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=-1, keepdims=True)
    
    def forward(self, token_ids):
        """
        Forward pass through transformer
        
        Parameters:
        -----------
        token_ids : numpy array of shape (batch_size, seq_length)
            Input token IDs
        
        Returns:
        --------
        logits : numpy array of shape (batch_size, num_classes)
            Class logits
        attention_weights : List of attention weights from each layer
        """
        # 1. Token embeddings
        x = self.embed(token_ids)
        
        # 2. Add positional encodings
        x = self.pos_encoding.forward(x)
        
        # 3. Pass through transformer blocks
        all_attention_weights = []
        for transformer_block in self.transformer_blocks:
            x, attn_weights = transformer_block.forward(x)
            all_attention_weights.append(attn_weights)
        
        # 4. Global average pooling (average over sequence length)
        x = np.mean(x, axis=1)
        
        # 5. Classification head
        logits = np.dot(x, self.classifier_W) + self.classifier_b
        probs = self.softmax(logits)
        
        return probs, all_attention_weights
    
    def predict(self, token_ids):
        """Get predicted class"""
        probs, _ = self.forward(token_ids)
        return np.argmax(probs, axis=1)


# ============================================
# DEMO: TRANSFORMER FOR SENTIMENT ANALYSIS
# ============================================

print("\n" + "=" * 70)
print("TRANSFORMER FOR SEQUENCE CLASSIFICATION")
print("=" * 70)

# Simple vocabulary
vocab = {
    '<PAD>': 0, 'great': 1, 'good': 2, 'excellent': 3, 
    'bad': 4, 'terrible': 5, 'movie': 6, 'film': 7,
    'this': 8, 'is': 9, 'the': 10
}

# Create transformer
transformer = SimpleTransformer(
    vocab_size=len(vocab),
    embed_dim=64,
    num_heads=4,
    num_layers=2,
    max_seq_length=20,
    num_classes=2
)

print(f"\n🏗️ Transformer Architecture:")
print(f"   Vocabulary size: {len(vocab)}")
print(f"   Embedding dimension: {transformer.embed_dim}")
print(f"   Number of layers: {len(transformer.transformer_blocks)}")
print(f"   Number of heads: 4")
print(f"   Output classes: {transformer.num_classes}")

# Example sentences
sentences = np.array([
    [8, 9, 1, 6, 0, 0],  # "this is great movie"
    [8, 6, 9, 5, 0, 0],  # "this movie is terrible"
    [3, 7, 0, 0, 0, 0],  # "excellent film"
])

print(f"\n📊 Forward Pass:")
print(f"   Input shape: {sentences.shape}")

# Forward pass
probs, attention_weights = transformer.forward(sentences)
predictions = transformer.predict(sentences)

print(f"   Output probabilities: {probs.shape}")
print(f"   Number of attention layers: {len(attention_weights)}")

print(f"\n🔮 Predictions:")
for i in range(len(sentences)):
    sentiment = "Positive 😊" if predictions[i] == 1 else "Negative 😞"
    print(f"   Sentence {i+1}: {sentiment} (prob: {probs[i, predictions[i]]:.3f})")

# Visualize attention from first layer
plt.figure(figsize=(8, 6))
plt.imshow(attention_weights[0][0], cmap='viridis', aspect='auto')
plt.colorbar(label='Attention Weight')
plt.xlabel('Key Position')
plt.ylabel('Query Position')
plt.title('First Layer Attention Weights\n(First sample)')
plt.tight_layout()
plt.show()

print("\n✅ Transformer demo complete!")
print("\n💡 KEY DIFFERENCES from RNN/LSTM:")
print("   ✅ Processes entire sequence in parallel (much faster)")
print("   ✅ No vanishing gradient problem")
print("   ✅ Better at capturing long-range dependencies")
print("   ✅ Attention weights are interpretable")
print("   ❌ Requires more memory")
print("   ❌ Needs more data to train effectively")
```

---

# Part 4: Advanced Techniques

## 20. Regularization Techniques from Scratch

### L1 and L2 Regularization

**Simple Explanation:** Add a penalty for large weights to prevent overfitting.

```python
class RegularizedLinearRegression:
    """
    Linear Regression with L1 (Lasso) and L2 (Ridge) regularization
    """
    
    def __init__(self, learning_rate=0.01, n_iterations=1000, 
                 regularization='l2', lambda_param=0.01):
        """
        Parameters:
        -----------
        regularization : str
            'l1' for Lasso, 'l2' for Ridge, 'elastic_net' for both
        lambda_param : float
            Regularization strength
        """
        self.lr = learning_rate
        self.n_iterations = n_iterations
        self.regularization = regularization
        self.lambda_param = lambda_param
        self.weights = None
        self.bias = None
        self.loss_history = []
    
    def fit(self, X, y):
        """
        Train with regularization
        """
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for i in range(self.n_iterations):
            # Predictions
            y_pred = np.dot(X, self.weights) + self.bias
            
            # Compute loss (MSE + regularization)
            mse_loss = np.mean((y - y_pred) ** 2)
            
            if self.regularization == 'l1':
                # L1: λ Σ|w|
                reg_loss = self.lambda_param * np.sum(np.abs(self.weights))
            elif self.regularization == 'l2':
                # L2: λ Σw²
                reg_loss = self.lambda_param * np.sum(self.weights ** 2)
            elif self.regularization == 'elastic_net':
                # Elastic Net: α·L1 + (1-α)·L2
                reg_loss = self.lambda_param * (
                    0.5 * np.sum(np.abs(self.weights)) +
                    0.5 * np.sum(self.weights ** 2)
                )
            else:
                reg_loss = 0
            
            total_loss = mse_loss + reg_loss
            self.loss_history.append(total_loss)
            
            # Compute gradients
            dw = (2/n_samples) * np.dot(X.T, (y_pred - y))
            db = (2/n_samples) * np.sum(y_pred - y)
            
            # Add regularization gradient
            if self.regularization == 'l1':
                dw += self.lambda_param * np.sign(self.weights)
            elif self.regularization == 'l2':
                dw += 2 * self.lambda_param * self.weights
            elif self.regularization == 'elastic_net':
                dw += self.lambda_param * (
                    0.5 * np.sign(self.weights) +
                    0.5 * 2 * self.weights
                )
            
            # Update weights
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            
            if i % 100 == 0:
                print(f"Iteration {i}: Loss = {total_loss:.4f}")
    
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias


# ============================================
# DEMO: REGULARIZATION COMPARISON
# ============================================

print("\n" + "=" * 70)
print("REGULARIZATION TECHNIQUES COMPARISON")
print("=" * 70)

# Generate data with noise and many features
np.random.seed(42)
n_samples = 100
n_features = 20

# Only first 5 features are actually relevant
X_train = np.random.randn(n_samples, n_features)
true_weights = np.array([3, -2, 1, 0.5, -1.5] + [0] * 15)  # Most weights are 0
y_train = X_train @ true_weights + np.random.randn(n_samples) * 0.5

print(f"\n📊 Dataset:")
print(f"   Samples: {n_samples}")
print(f"   Features: {n_features}")
print(f"   Relevant features: 5")
print(f"   Irrelevant features: 15")

# Train models with different regularization
models = {
    'No Regularization': RegularizedLinearRegression(
        regularization=None, learning_rate=0.01, n_iterations=1000
    ),
    'L2 (Ridge)': RegularizedLinearRegression(
        regularization='l2', lambda_param=0.1, learning_rate=0.01, n_iterations=1000
    ),
    'L1 (Lasso)': RegularizedLinearRegression(
        regularization='l1', lambda_param=0.1, learning_rate=0.01, n_iterations=1000
    ),
    'Elastic Net': RegularizedLinearRegression(
        regularization='elastic_net', lambda_param=0.1, learning_rate=0.01, n_iterations=1000
    )
}

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.ravel()

for idx, (name, model) in enumerate(models.items()):
    print(f"\n{'='*50}")
    print(f"Training: {name}")
    print(f"{'='*50}")
    model.fit(X_train, y_train)
    
    # Plot learned weights
    axes[idx].bar(range(n_features), model.weights, alpha=0.7, label='Learned')
    axes[idx].bar(range(n_features), true_weights, alpha=0.7, label='True')
    axes[idx].set_xlabel('Feature Index')
    axes[idx].set_ylabel('Weight Value')
    axes[idx].set_title(f'{name}\nSparsity: {np.sum(np.abs(model.weights) < 0.01)}/{n_features} weights ≈ 0')
    axes[idx].legend()
    axes[idx].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n💡 KEY INSIGHTS:")
print("\n1. NO REGULARIZATION:")
print("   ❌ Overfits: Learns non-zero weights for irrelevant features")
print("   ❌ Weights are large and unstable")

print("\n2. L2 (RIDGE):")
print("   ✅ Shrinks all weights towards zero")
print("   ❌ Doesn't eliminate features (no sparsity)")
print("   ✅ Good when all features are somewhat relevant")

print("\n3. L1 (LASSO):")
print("   ✅ Creates sparse solutions (many weights = exactly 0)")
print("   ✅ Performs feature selection automatically")
print("   ✅ Good when only few features are relevant")

print("\n4. ELASTIC NET:")
print("   ✅ Combines L1 and L2 benefits")
print("   ✅ Some sparsity + stable solutions")
print("   ✅ Best of both worlds")
```

---

## 22. Dropout from Scratch

**Simple Explanation:** Randomly "turn off" neurons during training to prevent over-reliance on specific neurons.

```python
class Dropout:
    """
    Dropout layer from scratch
    """
    
    def __init__(self, drop_prob=0.5):
        """
        Parameters:
        -----------
        drop_prob : float
            Probability of dropping a neuron (0.0 - 1.0)
        """
        self.drop_prob = drop_prob
        self.mask = None
    
    def forward(self, X, training=True):
        """
        Forward pass with dropout
        
        During training: Randomly drop neurons
        During inference: Use all neurons (scaled)
        """
        if training:
            # Create binary mask
            self.mask = (np.random.rand(*X.shape) > self.drop_prob).astype(float)
            
            # Scale remaining neurons to maintain expected value
            # (Inverted dropout)
            return X * self.mask / (1 - self.drop_prob)
        else:
            # No dropout during inference
            return X
    
    def backward(self, grad):
        """
        Backward pass: gradient only flows through non-dropped neurons
        """
        return grad * self.mask / (1 - self.drop_prob)


class NeuralNetworkWithDropout:
    """
    Neural Network with Dropout regularization
    """
    
    def __init__(self, layer_sizes, drop_probs=None):
        """
        Parameters:
        -----------
        layer_sizes : list
            Neurons in each layer
        drop_probs : list
            Dropout probability for each layer
        """
        self.layer_sizes = layer_sizes
        self.weights = []
        self.biases = []
        
        # Initialize weights
        for i in range(len(layer_sizes) - 1):
            w = np.random.randn(layer_sizes[i], layer_sizes[i+1]) * 0.01
            b = np.zeros((1, layer_sizes[i+1]))
            self.weights.append(w)
            self.biases.append(b)
        
        # Initialize dropout layers
        if drop_probs is None:
            drop_probs = [0.2] * (len(layer_sizes) - 2) + [0.0]  # No dropout on output
        
        self.dropout_layers = [Dropout(p) for p in drop_probs]
    
    def relu(self, x):
        return np.maximum(0, x)
    
    def softmax(self, x):
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)
    
    def forward(self, X, training=True):
        """
        Forward pass with dropout
        """
        activations = [X]
        
        for i in range(len(self.weights)):
            # Linear transformation
            z = np.dot(activations[-1], self.weights[i]) + self.biases[i]
            
            # Activation
            if i < len(self.weights) - 1:
                a = self.relu(z)
                # Apply dropout
                a = self.dropout_layers[i].forward(a, training=training)
            else:
                a = self.softmax(z)
            
            activations.append(a)
        
        return activations[-1]
    
    def predict(self, X):
        """Prediction with dropout OFF"""
        probs = self.forward(X, training=False)
        return np.argmax(probs, axis=1)


# ============================================
# DEMO: DROPOUT EFFECT
# ============================================

print("\n" + "=" * 70)
print("DROPOUT REGULARIZATION DEMO")
print("=" * 70)

print("""
HOW DROPOUT WORKS:

During Training:
   Input → [×] [✓] [×] [✓] [✓] → Hidden Layer
           Randomly drop neurons

During Inference:
   Input → [✓] [✓] [✓] [✓] [✓] → Hidden Layer
           Use all neurons

💡 KEY BENEFITS:
   ✅ Prevents co-adaptation of neurons
   ✅ Forces network to learn robust features
   ✅ Acts as ensemble of many networks
   ✅ Simple and effective regularization

💡 TYPICAL VALUES:
   - Hidden layers: 0.5 (drop 50%)
   - Input layer: 0.2 (drop 20%)
   - Output layer: 0.0 (no dropout)
""")

# Demonstrate dropout effect
layer = Dropout(drop_prob=0.5)
X_sample = np.random.randn(5, 10)

print(f"\n📊 Dropout Example:")
print(f"   Input shape: {X_sample.shape}")
print(f"   Drop probability: 0.5")

# Training mode: apply dropout
X_dropped = layer.forward(X_sample, training=True)

print(f"\n   Original values (first neuron):")
print(f"   {X_sample[0, :5]}")
print(f"\n   After dropout (first neuron):")
print(f"   {X_dropped[0, :5]}")
print(f"\n   Dropped neurons: {np.sum(X_dropped[0] == 0)}/{X_sample.shape[1]}")

# Inference mode: no dropout
X_inference = layer.forward(X_sample, training=False)
print(f"\n   Inference mode (no dropout):")
print(f"   {X_inference[0, :5]}")

# Compare models with and without dropout
print(f"\n🏗️ Network Architecture:")
nn_no_dropout = NeuralNetworkWithDropout([10, 50, 50, 5], drop_probs=[0.0, 0.0, 0.0])
nn_with_dropout = NeuralNetworkWithDropout([10, 50, 50, 5], drop_probs=[0.2, 0.5, 0.0])

print(f"   Without dropout: {[0.0, 0.0, 0.0]}")
print(f"   With dropout: {[0.2, 0.5, 0.0]}")

# Generate test data
X_test = np.random.randn(100, 10)

# Forward pass
output_no_dropout = nn_no_dropout.forward(X_test, training=True)
output_with_dropout = nn_with_dropout.forward(X_test, training=True)

print(f"\n📊 Output variance:")
print(f"   Without dropout: {np.var(output_no_dropout):.4f}")
print(f"   With dropout: {np.var(output_with_dropout):.4f}")

print("\n✅ Dropout demonstration complete!")
```

---

## 21. Batch Normalization from Scratch

**Simple Explanation:** Normalize activations within each mini-batch to stabilize and speed up training.

```python
class BatchNormalization:
    """
    Batch Normalization from scratch
    """
    
    def __init__(self, num_features, epsilon=1e-5, momentum=0.9):
        """
        Parameters:
        -----------
        num_features : int
            Number of features (channels)
        epsilon : float
            Small constant for numerical stability
        momentum : float
            Momentum for running mean/variance
        """
        self.epsilon = epsilon
        self.momentum = momentum
        
        # Learnable parameters
        self.gamma = np.ones((1, num_features))  # Scale
        self.beta = np.zeros((1, num_features))  # Shift
        
        # Running statistics (for inference)
        self.running_mean = np.zeros((1, num_features))
        self.running_var = np.ones((1, num_features))
    
    def forward(self, X, training=True):
        """
        Forward pass through batch normalization
        
        During training:
        1. Calculate batch mean and variance
        2. Normalize: x_norm = (x - mean) / sqrt(var + ε)
        3. Scale and shift: y = γ·x_norm + β
        
        During inference:
        - Use running mean and variance
        """
        if training:
            # Calculate batch statistics
            batch_mean = np.mean(X, axis=0, keepdims=True)
            batch_var = np.var(X, axis=0, keepdims=True)
            
            # Normalize
            X_norm = (X - batch_mean) / np.sqrt(batch_var + self.epsilon)
            
            # Update running statistics
            self.running_mean = (
                self.momentum * self.running_mean +
                (1 - self.momentum) * batch_mean
            )
            self.running_var = (
                self.momentum * self.running_var +
                (1 - self.momentum) * batch_var
            )
            
            # Store for backward pass
            self.X = X
            self.X_norm = X_norm
            self.batch_mean = batch_mean
            self.batch_var = batch_var
        else:
            # Use running statistics during inference
            X_norm = (X - self.running_mean) / np.sqrt(self.running_var + self.epsilon)
        
        # Scale and shift
        output = self.gamma * X_norm + self.beta
        
        return output
    
    def __repr__(self):
        return f"BatchNorm(features={self.gamma.shape[1]}, epsilon={self.epsilon})"


# ============================================
# DEMO: BATCH NORMALIZATION
# ============================================

print("\n" + "=" * 70)
print("BATCH NORMALIZATION")
print("=" * 70)

print("""
WHY BATCH NORMALIZATION?

Problem: Internal Covariate Shift
   - Distribution of layer inputs changes during training
   - Makes training unstable and slow
   - Requires careful weight initialization

Solution: Batch Normalization
   - Normalizes each mini-batch
   - Reduces internal covariate shift
   - Allows higher learning rates
   - Acts as regularization

Formula:
   1. μ = mean(X)                    [batch mean]
   2. σ² = var(X)                    [batch variance]
   3. x̂ = (x - μ) / √(σ² + ε)       [normalize]
   4. y = γ·x̂ + β                   [scale & shift]

💡 BENEFITS:
   ✅ Faster training (2-3x speedup)
   ✅ Higher learning rates possible
   ✅ Less sensitive to initialization
   ✅ Acts as regularization
   ✅ Reduces need for dropout
""")

# Create batch norm layer
bn = BatchNormalization(num_features=10)

# Generate sample data with different scales
X_sample = np.random.randn(32, 10) * np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(f"\n📊 Batch Normalization Demo:")
print(f"   Input shape: {X_sample.shape}")
print(f"   Features: {bn.gamma.shape[1]}")

# Forward pass (training)
X_normalized = bn.forward(X_sample, training=True)

print(f"\n   Before BatchNorm:")
print(f"   Mean: {np.mean(X_sample, axis=0)[:5]}")
print(f"   Std: {np.std(X_sample, axis=0)[:5]}")

print(f"\n   After BatchNorm:")
print(f"   Mean: {np.mean(X_normalized, axis=0)[:5]}")
print(f"   Std: {np.std(X_normalized, axis=0)[:5]}")
print(f"   (Should be close to 0 mean, 1 std)")

# Visualize effect
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Before
axes[0].boxplot(X_sample[:, :5])
axes[0].set_xlabel('Feature Index')
axes[0].set_ylabel('Value')
axes[0].set_title('Before Batch Normalization\n(Different scales)')
axes[0].grid(True, alpha=0.3)

# After
axes[1].boxplot(X_normalized[:, :5])
axes[1].set_xlabel('Feature Index')
axes[1].set_ylabel('Value')
axes[1].set_title('After Batch Normalization\n(Normalized scales)')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n✅ Batch Normalization demo complete!")
```

---

# Part 5: Production & Deployment

## 26. Training Strategies

### Learning Rate Schedules

```python
class LearningRateScheduler:
    """
    Various learning rate schedules
    """
    
    @staticmethod
    def step_decay(initial_lr, epoch, drop_rate=0.5, epochs_drop=10):
        """
        Step decay: lr = initial_lr * drop_rate^floor(epoch/epochs_drop)
        """
        return initial_lr * (drop_rate ** np.floor(epoch / epochs_drop))
    
    @staticmethod
    def exponential_decay(initial_lr, epoch, decay_rate=0.95):
        """
        Exponential decay: lr = initial_lr * decay_rate^epoch
        """
        return initial_lr * (decay_rate ** epoch)
    
    @staticmethod
    def cosine_annealing(initial_lr, epoch, max_epochs):
        """
        Cosine annealing: lr = min_lr + 0.5*(max_lr-min_lr)*(1+cos(π*epoch/max_epochs))
        """
        min_lr = initial_lr * 0.01
        return min_lr + 0.5 * (initial_lr - min_lr) * (
            1 + np.cos(np.pi * epoch / max_epochs)
        )
    
    @staticmethod
    def warmup_cosine(initial_lr, epoch, warmup_epochs=5, max_epochs=100):
        """
        Warmup then cosine: Linear warmup followed by cosine decay
        """
        if epoch < warmup_epochs:
            return initial_lr * (epoch + 1) / warmup_epochs
        else:
            return LearningRateScheduler.cosine_annealing(
                initial_lr, epoch - warmup_epochs, max_epochs - warmup_epochs
            )


# Visualize learning rate schedules
def visualize_lr_schedules():
    """
    Compare different learning rate schedules
    """
    print("\n" + "=" * 70)
    print("LEARNING RATE SCHEDULES")
    print("=" * 70)
    
    initial_lr = 0.1
    max_epochs = 100
    epochs = np.arange(max_epochs)
    
    schedules = {
        'Constant': [initial_lr] * max_epochs,
        'Step Decay': [LearningRateScheduler.step_decay(initial_lr, e) for e in epochs],
        'Exponential': [LearningRateScheduler.exponential_decay(initial_lr, e) for e in epochs],
        'Cosine Annealing': [LearningRateScheduler.cosine_annealing(initial_lr, e, max_epochs) for e in epochs],
        'Warmup + Cosine': [LearningRateScheduler.warmup_cosine(initial_lr, e, max_epochs=max_epochs) for e in epochs]
    }
    
    plt.figure(figsize=(12, 6))
    for name, lr_values in schedules.items():
        plt.plot(epochs, lr_values, label=name, linewidth=2)
    
    plt.xlabel('Epoch')
    plt.ylabel('Learning Rate')
    plt.title('Learning Rate Schedules Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    print("\n💡 WHEN TO USE:")
    print("\n1. CONSTANT:")
    print("   ✅ Simple problems")
    print("   ❌ May not converge optimally")
    
    print("\n2. STEP DECAY:")
    print("   ✅ Traditional approach")
    print("   ✅ Easy to tune")
    
    print("\n3. EXPONENTIAL DECAY:")
    print("   ✅ Smooth decrease")
    print("   ❌ Can decay too quickly")
    
    print("\n4. COSINE ANNEALING:")
    print("   ✅ Smooth, gradual decay")
    print("   ✅ Good final performance")
    print("   ✅ Modern default choice")
    
    print("\n5. WARMUP + COSINE:")
    print("   ✅ Best for large models/datasets")
    print("   ✅ Stable start, optimal end")
    print("   ✅ Used in BERT, GPT, etc.")

visualize_lr_schedules()
```

---

## 30. Deployment Strategies

### Saving and Loading Models

```python
class ModelSerializer:
    """
    Save and load models
    """
    
    @staticmethod
    def save_model(model, filepath):
        """
        Save model parameters to file
        """
        model_data = {
            'architecture': {
                'layer_sizes': model.layer_sizes,
            },
            'weights': model.weights,
            'biases': model.biases,
        }
        
        np.save(filepath, model_data)
        print(f"✅ Model saved to {filepath}")
    
    @staticmethod
    def load_model(filepath):
        """
        Load model from file
        """
        model_data = np.load(filepath, allow_pickle=True).item()
        
        # Reconstruct model
        model = NeuralNetworkScratch(model_data['architecture']['layer_sizes'])
        model.weights = model_data['weights']
        model.biases = model_data['biases']
        
        print(f"✅ Model loaded from {filepath}")
        return model


# Model deployment API
class ModelAPI:
    """
    Simple API for model inference
    """
    
    def __init__(self, model):
        self.model = model
        self.request_count = 0
    
    def predict(self, input_data):
        """
        Make prediction
        
        Parameters:
        -----------
        input_data : numpy array or dict
            Input features
        
        Returns:
        --------
        result : dict
            Prediction results with metadata
        """
        self.request_count += 1
        
        # Preprocess input
        if isinstance(input_data, dict):
            X = np.array(list(input_data.values())).reshape(1, -1)
        else:
            X = input_data
        
        # Make prediction
        predictions = self.model.predict(X)
        probabilities = self.model.predict_proba(X)
        
        # Format response
        result = {
            'prediction': int(predictions[0]),
            'probability': float(probabilities[0]),
            'request_id': self.request_count,
            'model_version': '1.0'
        }
        
        return result
    
    def health_check(self):
        """Check if model is working"""
        return {
            'status': 'healthy',
            'requests_served': self.request_count,
            'model_loaded': self.model is not None
        }


# ============================================
# DEMO: MODEL DEPLOYMENT
# ============================================

print("\n" + "=" * 70)
print("MODEL DEPLOYMENT DEMO")
print("=" * 70)

print("""
PRODUCTION DEPLOYMENT CHECKLIST:
================================

1. ✅ Model Serialization
   - Save model weights
   - Save preprocessing params
   - Version control

2. ✅ API Creation
   - REST API (Flask/FastAPI)
   - Input validation
   - Error handling

3. ✅ Monitoring
   - Track predictions
   - Log errors
   - Monitor latency

4. ✅ Scalability
   - Load balancing
   - Caching
   - Batch processing

5. ✅ Model Updates
   - A/B testing
   - Gradual rollout
   - Rollback capability
""")

# Simple API demo
print(f"\n🚀 Creating Model API...")

# Create simple model
simple_model = NeuralNetworkScratch([10, 20, 2])

# Create API
api = ModelAPI(simple_model)

print(f"✅ API initialized")

# Make prediction
test_input = {
    'feature_0': 0.5,
    'feature_1': -0.3,
    'feature_2': 1.2,
    'feature_3': 0.8,
    'feature_4': -0.5,
    'feature_5': 0.2,
    'feature_6': 0.9,
    'feature_7': -0.7,
    'feature_8': 0.4,
    'feature_9': 0.1
}

print(f"\n📊 Making prediction...")
result = api.predict(test_input)

print(f"\n🔮 Prediction Result:")
for key, value in result.items():
    print(f"   {key}: {value}")

# Health check
print(f"\n🏥 Health Check:")
health = api.health_check()
for key, value in health.items():
    print(f"   {key}: {value}")

print("\n✅ Deployment demo complete!")

print("""
\n📦 NEXT STEPS FOR REAL DEPLOYMENT:

1. Create Flask/FastAPI App:
   ```python
   from flask import Flask, request, jsonify
   
   app = Flask(__name__)
   model_api = ModelAPI(load_model('model.npy'))
   
   @app.route('/predict', methods=['POST'])
   def predict():
       data = request.json
       result = model_api.predict(data)
       return jsonify(result)
   ```

2. Containerize with Docker:
   ```dockerfile
   FROM python:3.9-slim
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY model.npy app.py ./
   CMD ["python", "app.py"]
   ```

3. Deploy to Cloud:
   - AWS Lambda + API Gateway (serverless)
   - AWS EC2 + Docker (traditional)
   - Google Cloud Run (containerized)
   - Azure ML Services
   - Heroku (simple deployment)

4. Monitor in Production:
   - CloudWatch / Stackdriver logs
   - Prometheus + Grafana metrics
   - Sentry for error tracking
   - Custom dashboards
""")
```

---

## 🎓 Complete Learning Path Summary

```python
print("\n" + "=" * 70)
print("🎉 CONGRATULATIONS! COMPLETE GUIDE FINISHED!")
print("=" * 70)

learning_path = {
    "Part 1: Traditional ML": [
        "✅ Linear Regression from scratch",
        "✅ Logistic Regression from scratch",
        "✅ Decision Trees from scratch",
        "✅ Random Forests from scratch",
        "✅ K-Nearest Neighbors",
        "✅ K-Means Clustering",
        "✅ SVM",
        "✅ Naive Bayes"
    ],
    "Part 2: Neural Networks": [
        "✅ Single Neuron/Perceptron",
        "✅ Multi-layer Neural Network",
        "✅ 6 Activation Functions",
        "✅ 6 Loss Functions",
        "✅ 5 Optimizers (SGD, Adam, etc.)",
        "✅ Backpropagation algorithm",
        "✅ Gradient Descent variants"
    ],
    "Part 3: Deep Learning": [
        "✅ CNN - Convolution & Pooling",
        "✅ CNN - Complete Architecture",
        "✅ RNN - Vanilla RNN",
        "✅ LSTM - Gates & Cell State",
        "✅ Transformer - Self-Attention",
        "✅ Transformer - Complete Model",
        "✅ Positional Encoding"
    ],
    "Part 4: Advanced Techniques": [
        "✅ L1/L2 Regularization",
        "✅ Dropout",
        "✅ Batch Normalization",
        "✅ Layer Normalization",
        "✅ Early Stopping",
        "✅ Data Augmentation"
    ],
    "Part 5: Production": [
        "✅ Learning Rate Schedules",
        "✅ Model Serialization",
        "✅ API Creation",
        "✅ Deployment Strategies",
        "✅ Monitoring & Logging",
        "✅ A/B Testing"
    ]
}

print("\n📚 WHAT YOU'VE MASTERED:")
for category, topics in learning_path.items():
    print(f"\n{category}:")
    for topic in topics:
        print(f"  {topic}")

print("\n\n🎯 YOUR SKILLS NOW:")
print("="*70)
skills = [
    "✅ Build any ML model from first principles",
    "✅ Understand mathematics behind algorithms",
    "✅ Implement deep learning with just NumPy",
    "✅ Debug models effectively",
    "✅ Optimize model performance",
    "✅ Deploy models to production",
    "✅ Explain any algorithm in interviews",
    "✅ Create custom architectures",
    "✅ Read and implement research papers"
]

for skill in skills:
    print(f"  {skill}")

print("\n\n💼 CAREER PATHS:")
print("="*70)
print("""
With this knowledge, you can pursue:
  🚀 Machine Learning Engineer
  🧠 Deep Learning Researcher
  📊 Data Scientist (Senior/Lead)
  🏗️ ML Infrastructure Engineer
  🎓 AI Researcher
  💡 ML Startup Founder
  📚 ML Educator/Course Creator
""")

print("\n🚀 NEXT STEPS:")
print("="*70)
print("""
1. PRACTICE:
   - Implement models on real datasets
   - Kaggle competitions
   - Personal projects

2. SPECIALIZE:
   - Computer Vision (if interested in images)
   - NLP (if interested in text)
   - Reinforcement Learning (if interested in agents)
   - Time Series (if interested in forecasting)

3. READ RESEARCH:
   - arXiv papers
   - Distill.pub (visual explanations)
   - Papers With Code

4. BUILD PORTFOLIO:
   - GitHub repositories
   - Blog posts explaining concepts
   - YouTube tutorials
   - Kaggle notebooks

5. CONTRIBUTE:
   - Open source ML libraries
   - Answer StackOverflow questions
   - Write tutorials
   - Mentor others

6. STAY UPDATED:
   - Follow ML researchers on Twitter
   - Subscribe to ML newsletters
   - Attend conferences (NeurIPS, ICML, CVPR)
   - Join ML communities
""")

print("\n" + "="*70)
print("Remember: You now understand ML better than 99% of developers!")
print("Keep building, keep learning, keep sharing! 🌟")
print("="*70)
```

---

## 📖 Final Resources

### Books
- **Deep Learning** by Goodfellow, Bengio, Courville
- **Pattern Recognition and Machine Learning** by Bishop
- **Hands-On Machine Learning** by Aurélien Géron
- **The Hundred-Page Machine Learning Book** by Andriy Burkov

### Online Courses
- **Fast.ai** - Practical Deep Learning
- **Coursera** - Deep Learning Specialization (Andrew Ng)
- **Stanford CS231n** - CNN for Visual Recognition
- **Stanford CS224n** - NLP with Deep Learning

### Websites & Tools
- **Papers With Code** - Latest research with code
- **Distill.pub** - Visual explanations
- **Towards Data Science** - Articles & tutorials
- **Kaggle** - Datasets & competitions
- **Google Colab** - Free GPU for experiments

### Communities
- **Reddit**: r/MachineLearning, r/learnmachinelearning
- **Discord**: Many ML community servers
- **Twitter**: Follow researchers and practitioners
- **LinkedIn**: Connect with ML professionals

---

## 🏆 Challenge Yourself

### Beginner Projects
1. Handwritten digit classifier (MNIST)
2. Iris flower classification
3. Housing price prediction
4. Sentiment analysis on reviews

### Intermediate Projects
1. Object detection in images
2. Text generation (character-level)
3. Recommendation system
4. Time series forecasting

### Advanced Projects
1. Style transfer (images)
2. Machine translation
3. Reinforcement learning game agent
4. GANs for image generation
5. Implement a research paper from scratch

---

**🎓 You've completed the ULTIMATE guide to building ML models from scratch!**

**Now go build something amazing! 🚀**
