# PyTorch — Zero to Hero

> **Bridge:** NumPy habits → industry deep learning framework.  
> **After:** [Build ML Models From Scratch](./Build-ML-Models-From-Scratch-Complete-Guide.md) (numpy neural net section).  
> **Before:** [Generative AI](./GENERATIVE-AI-ZERO-TO-HERO.md), advanced CV/NLP.

---

## Setup

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
# GPU: use cu121 index URL from pytorch.org for your CUDA version
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
```

---

## Week 1 — Tensors (NumPy → PyTorch)

| NumPy | PyTorch |
|-------|---------|
| `np.array` | `torch.tensor` |
| `a @ b` | `a @ b` or `torch.matmul` |
| `a.shape` | `a.shape` |
| CPU only | `.to("cuda")` / `device` |

```python
import torch

x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
y = torch.ones(2, 2)

# Element-wise
print(x + y)
print(x * 2)          # broadcast
print(x.T)
print(x.mean(dim=0))  # column means

# GPU (if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = x.to(device)
```

**Autograd:** track gradients for training.

```python
w = torch.tensor([2.0, 3.0], requires_grad=True)
loss = (w ** 2).sum()
loss.backward()
print(w.grad)  # dl/dw
```

---

## Week 2 — Dataset & training loop

```python
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

# Toy data: y = 3x + noise
X = torch.randn(200, 1)
y = 3 * X + 0.5 * torch.randn(200, 1)

loader = DataLoader(TensorDataset(X, y), batch_size=32, shuffle=True)

model = nn.Sequential(nn.Linear(1, 1))
opt = torch.optim.SGD(model.parameters(), lr=0.1)
loss_fn = nn.MSELoss()

for epoch in range(50):
    total = 0.0
    for xb, yb in loader:
        opt.zero_grad()
        pred = model(xb)
        loss = loss_fn(pred, yb)
        loss.backward()
        opt.step()
        total += loss.item() * len(xb)
    if (epoch + 1) % 10 == 0:
        print(f"epoch {epoch+1} loss {total/len(X):.4f}")

print("learned weight", list(model.parameters())[0].data)
```

**Pattern:** `zero_grad` → forward → loss → `backward` → `step`.

---

## Week 3 — Classification (MNIST)

```python
from torchvision import datasets, transforms

transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
train_ds = datasets.MNIST(root="./data", train=True, download=True, transform=transform)
train_loader = DataLoader(train_ds, batch_size=64, shuffle=True)

class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28 * 28, 256),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(256, 10),
        )

    def forward(self, x):
        return self.net(x)

model = MLP().to(device)
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()

for epoch in range(3):
    model.train()
    correct, total = 0, 0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        opt.zero_grad()
        logits = model(images)
        loss = loss_fn(logits, labels)
        loss.backward()
        opt.step()
        correct += (logits.argmax(1) == labels).sum().item()
        total += labels.size(0)
    print(f"epoch {epoch+1} train acc {correct/total:.3f}")
```

---

## Week 4 — CNN (transfer learning)

```python
from torchvision import models

resnet = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
for p in resnet.parameters():
    p.requires_grad = False  # freeze backbone

resnet.fc = nn.Linear(resnet.fc.in_features, 10)  # new head for 10 classes
# Train only resnet.fc (and optionally last block)
```

Use `torchvision.transforms` for resize, flip, normalize (ImageNet stats).

---

## Week 5 — Save / load & inference

```python
torch.save(model.state_dict(), "model.pt")
model.load_state_dict(torch.load("model.pt", map_location=device))
model.eval()

with torch.no_grad():
    sample = torch.randn(1, 1, 28, 28).to(device)
    probs = torch.softmax(model(sample), dim=1)
```

**Production:** TorchScript (`torch.jit.trace`), ONNX export, or serve via TorchServe / Triton.

---

## Week 6 — Best practices

| Topic | Practice |
|-------|----------|
| Reproducibility | `torch.manual_seed(42)`; log versions |
| AMP | `torch.cuda.amp.autocast` + `GradScaler` on GPU |
| DataLoader | `num_workers=4`, `pin_memory=True` (CUDA) |
| Debugging | Overfit one batch first |
| Memory | Smaller batch, gradient accumulation |

```python
scaler = torch.cuda.amp.GradScaler()
with torch.cuda.amp.autocast():
    logits = model(images)
    loss = loss_fn(logits, labels)
scaler.scale(loss).backward()
scaler.step(opt)
scaler.update()
```

---

## Map to other guides

| Goal | Guide |
|------|-------|
| Statistics / ML theory | [Statistics for ML](./STATISTICS-FOR-ML.md) |
| Generative images | [Generative AI Zero to Hero](./GENERATIVE-AI-ZERO-TO-HERO.md) |
| CV depth | [Computer Vision](./Computer-Vision-Complete-Guide.md) |
| NLP / transformers | [NLP Complete Guide](./NLP-Complete-Guide.md) |
| Deploy | [MLOps Production](./MLOps-Production-Complete-Guide.md) |

---

## Checkpoint projects

1. **MNIST MLP** — &gt; 97% test accuracy  
2. **CIFAR-10 CNN** — &gt; 75% with data augmentation  
3. **Transfer learning** — 5-class custom folder dataset  
4. **Export** — ONNX + single `onnxruntime` inference script  
