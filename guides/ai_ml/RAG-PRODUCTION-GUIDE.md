# RAG in Production — Complete Guide

> **Beyond interview Q&A:** chunking, evaluation (RAGAS), vector DBs, framework comparison.  
> Start with [LLM Apps Zero to Hero](./LLM-APPS-ZERO-TO-HERO.md) for first RAG code, then read this.

---

## Production RAG architecture

```
Sources (PDF, wiki, tickets)
        ↓
Ingestion (parse, clean, PII redact)
        ↓
Chunking + metadata
        ↓
Embed → Vector DB (+ optional keyword index)
        ↓
Retriever (hybrid, rerank)
        ↓
LLM (grounded prompt) → Answer + citations
        ↓
Eval (RAGAS) + logging (Langfuse)
```

---

## 1. Chunking strategies

| Strategy | When | Risk |
|----------|------|------|
| Fixed size (512 tokens, 10% overlap) | General docs | Splits tables/code badly |
| Recursive (headers → paragraphs) | Markdown/HTML | Better semantics |
| Semantic (embed sentences, merge) | Long prose | Higher cost |
| Parent–child | Small chunks retrieve, large chunk for LLM | Best quality/cost tradeoff |

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=80,
    separators=["\n## ", "\n### ", "\n", " "],
)
chunks = splitter.split_text(open("policy.md").read())
for i, c in enumerate(chunks[:3]):
    print(f"--- chunk {i} ({len(c)} chars) ---\n{c[:200]}...\n")
```

**Rules:**

- Attach metadata: `source`, `page`, `updated_at`, `acl`
- Keep code blocks intact
- Deduplicate near-identical chunks (cosine similarity > 0.95)

---

## 2. Embeddings & vector stores

| Store | Strength | Weakness |
|-------|----------|----------|
| **Chroma** | Local dev, fast setup | Scale limits |
| **pgvector** | SQL + vectors in one DB | Ops tuning needed |
| **Pinecone** | Managed, scalable | Vendor lock-in |
| **Weaviate / Qdrant** | Hybrid search, filters | Learning curve |
| **OpenSearch** | AWS-native, hybrid | Cluster ops |

```python
# Chroma minimal example
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("docs")

collection.add(
    documents=["Refund policy allows 30 days.", "Shipping is free over $50."],
    ids=["chunk-1", "chunk-2"],
    metadatas=[{"doc": "policy"}, {"doc": "shipping"}],
)

results = collection.query(query_texts=["How long to return?"], n_results=1)
print(results["documents"])
```

**Production:** namespace per tenant; encrypt at rest; backup snapshots.

---

## 3. Retrieval quality

```python
# Hybrid: keyword + vector (conceptual with LangChain)
# 1) BM25 top 20
# 2) Vector top 20
# 3) Merge + cross-encoder rerank top 5
```

| Technique | Gain |
|-----------|------|
| HyDE | Generate hypothetical answer, embed it, retrieve |
| Query rewriting | LLM expands acronyms / typos |
| Reranker (Cohere, bge-reranker) | +10–25% nDCG common |
| Metadata filters | `department == "HR"` before vector search |

---

## 4. Grounded generation prompt

```python
SYSTEM = """Answer ONLY from the context below.
If unknown, say "I don't have that information."
Cite sources as [1], [2] matching context blocks."""

def build_prompt(question: str, contexts: list[str]) -> str:
    blocks = "\n\n".join(f"[{i+1}] {c}" for i, c in enumerate(contexts))
    return f"{SYSTEM}\n\nContext:\n{blocks}\n\nQuestion: {question}"
```

---

## 5. Evaluation with RAGAS

```bash
pip install ragas datasets langchain-openai
```

```python
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision
from datasets import Dataset

data = Dataset.from_dict({
    "question": ["What is the refund window?"],
    "answer": ["Refunds are allowed within 30 days."],
    "contexts": [["Refund policy allows 30 days from purchase."]],
    "ground_truth": ["30 days"],
})

result = evaluate(data, metrics=[faithfulness, answer_relevancy, context_precision])
print(result)
```

| Metric | Measures |
|--------|----------|
| **Faithfulness** | Answer supported by context (hallucination) |
| **Answer relevancy** | On-topic response |
| **Context precision** | Retrieved chunks useful |
| **Context recall** | Needed info was retrieved |

**CI gate:** fail deploy if faithfulness &lt; 0.85 on golden set.

---

## 6. Framework comparison

| Framework | Best for | Notes |
|-----------|----------|-------|
| **LangChain** | Agents, many integrations | Large ecosystem; watch abstraction leaks |
| **LlamaIndex** | Data ingestion, RAG pipelines | Strong connectors, query engines |
| **Haystack** | Production pipelines, eval | Good for search-heavy apps |
| **Raw SDK + vector DB** | Full control | Less magic, more code |

**Recommendation:** prototype in LangChain/LlamaIndex; extract stable interfaces; move hot path to thin Python + vector DB for scale.

---

## 7. Observability & cost

| Tool | Role |
|------|------|
| **Langfuse** | Traces, prompts, scores |
| **OpenTelemetry** | Latency breakdown |
| CloudWatch / Datadog | Infra metrics |

Log: `trace_id`, `retrieved_ids`, `token_counts`, `latency_ms`, `user_feedback`.

**Cost levers:** smaller embed model, cache embeddings, reduce `k`, summarize long contexts, batch embed overnight.

---

## 8. Security

- Filter retrieved docs by user ACL **before** LLM  
- Redact PII at ingest  
- Prompt injection: separate system vs user; sanitize HTML  
- Rate limit API; audit exports  

---

## 9. Deployment checklist

- [ ] Golden dataset (50+ Q/A) with expected citations  
- [ ] RAGAS scores in CI  
- [ ] Chunking versioned (`chunker_v3`)  
- [ ] Reindex job when sources change  
- [ ] Fallback when retrieval empty  
- [ ] Human feedback loop  

**Also see:** [RAG Interview Questions](./RAG-Interview-Questions-Complete.md), [AWS ML & GenAI](../cloud-platforms/AWS-ML-GENAI-ZERO-TO-HERO.md) (Bedrock + OpenSearch).
