# System Design Practice Track

> Graded prompts, time boxes, and scoring rubrics for interview-ready system design practice.

**How to use:** Pick one prompt per session. Follow the timing template. Score yourself with the rubric. Log weak areas in `LEARNING-CHECKPOINTS.md`.

---

## Session Template (45 minutes)

| Phase | Time | Deliverable |
|-------|------|-------------|
| Requirements + constraints | 5 min | Functional + non-functional list |
| Capacity estimation | 5 min | QPS, storage, bandwidth |
| High-level design | 15 min | Component diagram + data flow |
| Deep dive (2 topics) | 15 min | Schema, cache, queue, or failure mode |
| Wrap-up | 5 min | Bottlenecks, trade-offs, evolution |

---

## Grading Levels

| Level | Target role | What “pass” looks like |
|-------|-------------|-------------------------|
| **L1** | Junior / new grad | Clear components, basic scale numbers, one storage choice with reason |
| **L2** | Mid-level (2–5 yrs) | Trade-offs, caching/DB split, failure handling, API sketch |
| **L3** | Senior (5+ yrs) | Sharding, consistency model, observability, cost/latency reasoning |
| **L4** | Staff / principal | Multi-region, migration, org/team boundaries, explicit risk register |

**Scoring rubric (0–4 each, max 20):**

1. **Requirements** — Clarifies scope, assumptions, out-of-scope  
2. **Estimation** — Order-of-magnitude math is sane  
3. **Architecture** — Coherent diagram, clear boundaries  
4. **Depth** — Schema, queues, cache, or CAP choice explained  
5. **Communication** — Trade-offs stated; listens to hints  

- **16–20:** Ready for target level  
- **12–15:** Repeat with same prompt in 48 hours  
- **&lt;12:** Study linked guide section, then retry  

---

## L1 — Foundations (Weeks 1–2)

| # | Prompt | Focus | Study after |
|---|--------|-------|-------------|
| 1.1 | Design a URL shortener | Read/write ratio, ID generation, redirect | `COMPLETE-SYSTEM-DESIGN-GUIDE.md` §4.1 |
| 1.2 | Design a paste bin (text storage) | Object storage vs DB, TTL | §2 Core Components |
| 1.3 | Design a rate limiter (API) | Token bucket, Redis, per-user vs global | §5.2 Rate Limiting |
| 1.4 | Design a key-value cache service | Eviction, TTL, memory bounds | §1.3 Caching |
| 1.5 | Design a simple chat room (single region) | WebSockets vs polling, message order | HLD notebook — messaging basics |

**L1 stretch:** Add “what breaks if Redis dies?” for any prompt above.

---

## L2 — Intermediate (Weeks 3–5)

| # | Prompt | Focus | Study after |
|---|--------|-------|-------------|
| 2.1 | Design Twitter/X timeline (read-heavy) | Fan-out on write vs read, celebrity problem | §4.2 Instagram |
| 2.2 | Design a notification system | Push/email/SMS, queues, idempotency | §1.5 Message Queues |
| 2.3 | Design a file upload service (images) | CDN, metadata DB, multipart upload | §2.3 CDN |
| 2.4 | Design a search autocomplete | Trie vs ES, ranking, latency | §4 + caching |
| 2.5 | Design a ticket booking system (concerts) | Consistency, locks, overselling | CAP / ACID in HLD notebook |
| 2.6 | Design a metrics monitoring system | Time-series DB, aggregation, cardinality | Architecture patterns — observability |

**L2 stretch:** Draw sequence diagram for one write path and one read path.

---

## L3 — Senior (Weeks 6–8)

| # | Prompt | Focus | Study after |
|---|--------|-------|-------------|
| 3.1 | Design Instagram (photos + feed) | Fan-out hybrid, S3, feed ranking | §4.2 |
| 3.2 | Design Netflix video streaming | Encoding, CDN, ABR | §4.3 |
| 3.3 | Design Uber ride matching | Geo-index, dispatch, surge | §4.4 |
| 3.4 | Design WhatsApp messaging | Delivery guarantees, E2E, groups | Event-driven + LLD |
| 3.5 | Design a payment system (Stripe-like) | Idempotency, ledger, PCI boundaries | Saga pattern notebook |
| 3.6 | Design a distributed job scheduler | Leases, retries, priority queues | §5.3 Distributed Locking |
| 3.7 | Design YouTube (upload + view) | Transcoding pipeline, viral traffic | Microservices chapter |

**L3 stretch:** 10-minute “design review” as if presenting to a principal engineer.

---

## L4 — Staff / Principal (Weeks 9–12)

| # | Prompt | Focus | Study after |
|---|--------|-------|-------------|
| 4.1 | Design Google Search (simplified) | Crawl, index, rank, serve | Architecture patterns |
| 4.2 | Design a multi-tenant SaaS platform | Isolation, noisy neighbor, billing | §3 Microservices |
| 4.3 | Migrate monolith e-commerce to microservices | Strangler fig, data dual-write | Architecture — evolution |
| 4.4 | Design a global chat with &lt;100ms p99 | Multi-region, conflict resolution | CAP + consistency deep dive |
| 4.5 | Design ML feature store + serving | Online/offline features, freshness | `guides/ai_ml/`, infrastructure notebooks |
| 4.6 | Design generative AI app (RAG at scale) | Vector DB, guardrails, cost controls | PDF library + `rag-interview` guide |

**L4 stretch:** Write a one-page ADR (Architecture Decision Record) for your top trade-off.

---

## Weekly Practice Plan (10 weeks)

| Week | Sessions | Levels | Goal |
|------|----------|--------|------|
| 1 | 3× | L1 (1.1–1.3) | Timing discipline |
| 2 | 3× | L1 (1.4–1.5) + 1 retry | Failure modes |
| 3 | 3× | L2 (2.1–2.3) | Fan-out + queues |
| 4 | 3× | L2 (2.4–2.6) | Consistency stories |
| 5 | 2× | L2 retry lowest score | Stabilize L2 |
| 6 | 3× | L3 (3.1–3.3) | End-to-end cases |
| 7 | 3× | L3 (3.4–3.6) | Distributed patterns |
| 8 | 2× | L3 mock with peer | Communication |
| 9 | 2× | L4 (4.1–4.3) | Evolution + tenancy |
| 10 | 2× | L4 (4.4–4.6) + portfolio doc | Publish 3 write-ups |

---

## Mock Interview Checklist

Before session:

- [ ] Whiteboard or Excalidraw ready  
- [ ] Timer visible  
- [ ] No notes for first 25 minutes  

After session:

- [ ] Score rubric filled  
- [ ] 3 things done well  
- [ ] 3 gaps with guide links  
- [ ] Retry date scheduled  

---

## Related Materials

| Resource | Path |
|----------|------|
| Complete guide | `system-design/COMPLETE-SYSTEM-DESIGN-GUIDE.md` |
| HLD notebook | `system-design/hld/system-design-hld.ipynb` |
| LLD notebook | `system-design/lld/system-design-lld.ipynb` |
| Architecture patterns | `system-design/architecture/system-architecture-patterns.ipynb` |
| Learning checkpoints | `LEARNING-CHECKPOINTS.md` |
| Generative AI system design PDF | UI → PDF Library |

---

**Target:** Complete at least **15 prompts** with average score **≥16** at your target level before senior/staff interviews.
