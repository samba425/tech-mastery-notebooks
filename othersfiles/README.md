# DevOps Interview Preparation Suite

A comprehensive, hands-on interview preparation library for **Ansible**, **Terraform**, **Kubernetes**, and **Docker**. Each topic file is structured identically so you can study them in parallel.

---

## Contents

| File | Purpose |
|------|---------|
| [Installation-Guide-Mac-Linux.md](Installation-Guide-Mac-Linux.md) | Install and configure all four tools on macOS (Intel + Apple Silicon) and Linux (Ubuntu/Debian, RHEL/Fedora, Arch). Includes local-lab setup. |
| [Docker-Interview-Questions.md](Docker-Interview-Questions.md) | 300+ Docker Q&A from fundamentals through advanced security, BuildKit, multi-arch, troubleshooting, mock interviews. |
| [Kubernetes-Interview-Questions.md](Kubernetes-Interview-Questions.md) | 300+ K8s Q&A covering CKA / CKAD / CKS curricula, operators, networking, security, scheduling, troubleshooting. |
| [Ansible-Interview-Questions.md](Ansible-Interview-Questions.md) | 300+ Ansible Q&A: playbooks, roles, Jinja2, Vault, AWX, dynamic inventory, performance, scenarios. |
| [Terraform-Interview-Questions.md](Terraform-Interview-Questions.md) | 300+ Terraform Q&A: HCL, state management, modules, providers, Terraform Cloud, Sentinel, testing. |

Each interview file follows the same 12-section template:

```
A. Fundamentals & Core Concepts          (~60 Qs)
B. Architecture & Internals              (~60 Qs)
C. Configuration & Day-to-Day Usage      (~60 Qs)
D. Advanced Topics                       (~60 Qs)
E. Security, Performance & Best Practices (~30 Qs)
F. Troubleshooting & Debugging           (~30 Qs)
G. Real-World Scenario-Based Questions   (~30 Qs)
H. Comparison Tables
I. Hands-On Labs                         (5-10 exercises)
J. Mock Interview Sets                   (3 timed sets)
K. Cheat Sheet
L. Curated Resources
```

---

## Suggested Study Order

```
Week 1: Docker          (foundation for everything containerized)
Week 2: Kubernetes      (builds directly on Docker concepts)
Week 3: Ansible         (configuration management cross-cuts both)
Week 4: Terraform       (IaC layer that often provisions clusters)
```

If you already know Docker basics, skip to Kubernetes in Week 1 and use the freed week for a deep dive on whichever tool you're weakest in.

---

## 4-Week Detailed Schedule

### Week 1 — Docker

| Day | Focus | Action |
|-----|-------|--------|
| Mon | Sections A + B | Read fundamentals & architecture, install Docker locally |
| Tue | Section C | Hands-on: build first images, run containers, networks |
| Wed | Section D | Multi-stage builds, BuildKit, Compose, Swarm basics |
| Thu | Sections E + F | Security hardening, scan with Trivy, debug a broken container |
| Fri | Section G + I (Labs 1-3) | Scenario questions + labs |
| Sat | Section J Mock Set 1 | 60-min timed mock interview |
| Sun | Review weak areas + cheat sheet | Spaced repetition on missed questions |

### Week 2 — Kubernetes

| Day | Focus | Action |
|-----|-------|--------|
| Mon | Sections A + B | Install kind/minikube, walk through control plane |
| Tue | Section C | Deploy pods/services/deployments, kubectl drills |
| Wed | Section D | StatefulSets, operators, Helm, autoscaling |
| Thu | Sections E + F | RBAC, NetworkPolicies, troubleshoot CrashLoopBackOff |
| Fri | Section G + I (Labs 1-4) | CKAD/CKA scenario practice |
| Sat | Mock Set 1 + 2 | Timed sets, focus on speed |
| Sun | Mock Set 3 + cheat sheet review | Memorize key kubectl one-liners |

### Week 3 — Ansible

| Day | Focus | Action |
|-----|-------|--------|
| Mon | Sections A + B | Install Ansible, inventory basics, ad-hoc commands |
| Tue | Section C | Write 3 playbooks, use roles |
| Wed | Section D | Vault, dynamic inventory, custom modules |
| Thu | Sections E + F | Idempotency, performance, debugging plays |
| Fri | Labs + Scenarios | Multi-tier app deployment lab |
| Sat | Mock Set 1 + 2 | Timed |
| Sun | Mock Set 3 + cheat sheet | Memorize module names and patterns |

### Week 4 — Terraform

| Day | Focus | Action |
|-----|-------|--------|
| Mon | Sections A + B | Install Terraform + AWS CLI / LocalStack |
| Tue | Section C | Write providers, resources, variables |
| Wed | Section D | Modules, remote state, workspaces |
| Thu | Sections E + F | Sentinel/OPA, state surgery, drift |
| Fri | Labs | Build VPC + 3-tier app module |
| Sat | Mock Set 1 + 2 | Timed |
| Sun | Mock Set 3 + final review | Cross-tool integration scenarios |

---

## How to Use This Library

1. **Read actively.** Don't passively skim — for every question, answer aloud first, then read the answer.
2. **Build muscle memory with the labs.** Reading about Kubernetes will not get you through a CKA. Type the commands.
3. **Time the mock sets.** 4 minutes per question average. Simulate a real screen.
4. **Iterate on weak topics.** Tag each missed question and re-review the next morning.
5. **Cross-reference cheat sheets daily.** 10 minutes/day of cheat-sheet review compounds quickly.

---

## Conventions Used Across All Files

- Code blocks are language-tagged for syntax highlighting (`bash`, `yaml`, `hcl`, `dockerfile`, `python`).
- Placeholders use angle-bracket notation: `<YOUR_AWS_ACCESS_KEY>`, `<CLUSTER_NAME>`, `<NAMESPACE>`. **Never** commit a real secret.
- Commands tested against the latest stable releases as of 2026: Docker 27.x, Kubernetes 1.31, Ansible-core 2.18, Terraform 1.10.
- Scenarios marked **[CKA]**, **[CKAD]**, **[CKS]**, **[DCA]**, **[HCTA]**, or **[EX407]** map to common certification exam objectives.

---

## Companion Material

These interview files **complement** (don't replace) the existing zero-to-hero courses in this repo:

- `../Docker-Zero-to-Hero.md`
- `../Kubernetes-Zero-to-Hero.md`
- `../Ansible-Zero-to-Hero.md`
- `../Terraform-Zero-to-Hero.md`

Use the zero-to-hero files to *learn* the topic; use the interview files to *test* and *cement* what you've learned.

Good luck.
