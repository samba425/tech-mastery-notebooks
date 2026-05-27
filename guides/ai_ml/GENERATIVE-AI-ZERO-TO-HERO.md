# Generative AI — Zero to Hero

> **Beyond LLM text:** GANs, diffusion, image fine-tuning — concepts + minimal PyTorch examples.  
> **Prerequisite:** [PyTorch Zero to Hero](./PYTORCH-ZERO-TO-HERO.md) + [Computer Vision](./Computer-Vision-Complete-Guide.md) (helpful).

**Path:** [AI/ML Zero to Hero](./AI-ML-ZERO-TO-HERO.md) → Phase 3 specialization.

---

## What is generative AI?

| Modality | Classic approach | Modern approach |
|----------|------------------|-----------------|
| Images | GANs | Diffusion (Stable Diffusion, SDXL) |
| Text | n-gram | Transformers (GPT, Claude) |
| Audio | WaveNet | Diffusion + transformers |
| Video | — | Diffusion + temporal models |

This guide focuses on **images** (GANs + diffusion) and points to LLM guides for text.

---

## Phase 1 — GAN intuition (Week 1)

**Generator G** fakes data; **Discriminator D** detects fake vs real. Adversarial training.

```
Noise z ──→ G(z) ──→ fake image
                      ↓
Real image ─────────→ D(·) ──→ probability "real"
```

```python
import torch
import torch.nn as nn

class Generator(nn.Module):
    def __init__(self, latent_dim=100, img_dim=28 * 28):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, img_dim),
            nn.Tanh(),
        )

    def forward(self, z):
        return self.net(z)

class Discriminator(nn.Module):
    def __init__(self, img_dim=28 * 28):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(img_dim, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        return self.net(x)
```

**Training loop (sketch):**

```python
# For each batch:
# 1) Train D on real + fake (detach G for fake)
# 2) Train G to fool D (maximize D(G(z)))
```

**Issues:** mode collapse, unstable training → led to **diffusion** dominance.

---

## Phase 2 — Diffusion models (Week 2)

Forward process: gradually add noise. Learn to **denoise** step by step.

```
x_0 (image) → x_1 → ... → x_T ≈ pure noise
Model predicts noise ε_θ(x_t, t) at each step t
```

**Intuition:** easier than GANs — stable MSE loss on noise prediction.

Use **Hugging Face Diffusers** for real images (don't train from scratch unless research):

```python
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
)
pipe = pipe.to("cuda")  # or "mps" on Apple Silicon

prompt = "a watercolor painting of a robot reading a book"
image = pipe(prompt, num_inference_steps=30).images[0]
image.save("robot.png")
```

---

## Phase 3 — Fine-tuning images (Week 3)

| Method | Data needed | Use case |
|--------|-------------|----------|
| **DreamBooth** | 3–20 photos of subject | Personalize object/style |
| **LoRA** | Small image set | Low-cost adapter weights |
| **ControlNet** | Pairs with edges/pose | Structure-guided generation |

```bash
# Example: train LoRA with kohya_ss or diffusers training scripts
# pip install diffusers transformers accelerate peft
# Prepare folder: train/001.png + 001.txt caption per image
```

**Checkpoint:** Generate 10 images with your LoRA; compare to base model.

---

## Phase 4 — Evaluation & safety

| Concern | Practice |
|---------|----------|
| Quality | FID, CLIP score (research); human eval (product) |
| Bias | Audit prompts across demographics |
| Safety | NSFW filters, watermarking, provenance metadata |
| Copyright | Train only on licensed data; document lineage |

---

## Phase 5 — Connect to LLM stack

| Topic | Guide |
|-------|-------|
| Text gen + RAG | [LLM Apps Zero to Hero](./LLM-APPS-ZERO-TO-HERO.md) |
| Production RAG | [RAG Production Guide](./RAG-PRODUCTION-GUIDE.md) |
| Multimodal (image + text) | Vision-language models in [NLP Guide](./NLP-Complete-Guide.md) |
| Cloud APIs | [AWS ML & GenAI](../cloud-platforms/AWS-ML-GENAI-ZERO-TO-HERO.md) |

---

## 6-week study plan

| Week | Focus |
|------|-------|
| 1 | PyTorch tensors + GAN code above on MNIST |
| 2 | Diffusers pipeline — generate 50 prompts |
| 3 | LoRA fine-tune on 15 images |
| 4 | ControlNet or img2img experiments |
| 5 | Deploy: Gradio demo + API rate limits |
| 6 | Safety review + portfolio write-up |

---

## Next steps

- Deep CV: [Computer-Vision-Complete-Guide.md](./Computer-Vision-Complete-Guide.md)  
- Deep LLMs: [NLP-Complete-Guide.md](./NLP-Complete-Guide.md)  
- MLOps for models: [MLOps-Production-Complete-Guide.md](./MLOps-Production-Complete-Guide.md)
