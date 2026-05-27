# LLM Apps Zero to Hero — RAG, Agents, LangChain, LangGraph, Langfuse

> **Read this file top to bottom once.** Short theory, then **simple runnable examples** for each topic.  
> For depth, continue with the full guides linked at the end.

**Prerequisites:** Python Sec. 11 done · basic `pip` / `venv` · optional `OPENAI_API_KEY` (local embeddings work without it for Parts 1–2).

---

## Setup (one time)

```bash
cd tech-mastery-notebooks
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install \
  langchain langchain-community langchain-openai langchain-text-splitters \
  langgraph langfuse faiss-cpu sentence-transformers pypdf
```

| Variable | When needed |
|----------|-------------|
| `OPENAI_API_KEY` | Parts 3–6 (chat model + agent) |
| `LANGFUSE_PUBLIC_KEY` / `LANGFUSE_SECRET_KEY` | Part 7 (free tier at langfuse.com) |

---

## Reading order (end to end)

| Part | Topic | Time |
|------|--------|------|
| 1 | What is RAG? | 15 min |
| 2 | RAG pipeline (local embeddings) | 45 min |
| 3 | LangChain RAG chain | 45 min |
| 4 | LangGraph workflow | 30 min |
| 5 | Agent + tools (ReAct) | 45 min |
| 6 | Agentic pattern (multi-step) | 20 min |
| 7 | Langfuse observability | 30 min |
| 8 | LlamaIndex (short) | 20 min |
| 9 | Go deeper (full guides) | weeks |

---

## Part 1 — RAG in plain language

**RAG = Retrieval-Augmented Generation**

1. **Split** documents into chunks  
2. **Embed** chunks into vectors  
3. **Retrieve** chunks similar to the user question  
4. **Generate** an answer using those chunks as context  

**Why:** LLMs do not know your private PDFs; RAG grounds answers in your data.

```
User question → embed query → search vector DB → top chunks + question → LLM → answer
```

---

## Part 2 — Minimal RAG (no OpenAI required)

**Theory:** Same four steps with local embeddings (`sentence-transformers`) and FAISS.

```python
"""Part 2 — minimal RAG. Run: python part2_rag_minimal.py"""
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

texts = [
    "RAG retrieves facts before the LLM answers.",
    "LangChain connects models, tools, and vector stores.",
    "LangGraph runs agents as a state machine with loops.",
    "Langfuse traces LLM calls for debugging in production.",
]
docs = [Document(page_content=t) for t in texts]

splitter = RecursiveCharacterTextSplitter(chunk_size=80, chunk_overlap=10)
chunks = splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

query = "What is used to debug LLM apps?"
hits = retriever.invoke(query)
print("Retrieved:")
for doc in hits:
    print(" -", doc.page_content)
```

**Practice:** Add 5 sentences about your project; ask 3 questions; check if the right chunk is retrieved.

---

## Part 3 — LangChain RAG chain

**Theory:** LangChain wraps retriever + prompt + LLM in a **chain** (LCEL).

```python
"""Part 3 — LangChain RAG. Needs OPENAI_API_KEY."""
import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

docs = [
    Document(page_content="Our refund policy allows returns within 30 days."),
    Document(page_content="Support email is help@example.com."),
]
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())
retriever = vectorstore.as_retriever()

prompt = ChatPromptTemplate.from_template(
    """Answer using only the context below.
Context:
{context}

Question: {question}
Answer:"""
)

def format_docs(docs):
    return "\n".join(d.page_content for d in docs)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

answer = chain.invoke("How long can I return a product?")
print(answer)
```

**Practice:** Load one `.txt` file with `PyPDFLoader` or plain read; ask 2 questions.

---

## Part 4 — LangGraph (workflow, not one-shot)

**Theory:** **LangGraph** = nodes (steps) + edges (flow). Good for loops: retrieve → draft → check → retry.

```python
"""Part 4 — LangGraph hello world. Needs OPENAI_API_KEY."""
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI

class State(TypedDict):
    topic: str
    draft: str
    done: bool

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def research(state: State) -> State:
    state["draft"] = llm.invoke(f"One sentence about {state['topic']}").content
    return state

def polish(state: State) -> State:
    state["draft"] = llm.invoke(f"Improve clarity: {state['draft']}").content
    state["done"] = True
    return state

graph = StateGraph(State)
graph.add_node("research", research)
graph.add_node("polish", polish)
graph.set_entry_point("research")
graph.add_edge("research", "polish")
graph.add_edge("polish", END)

app = graph.compile()
result = app.invoke({"topic": "RAG", "draft": "", "done": False})
print(result["draft"])
```

**Practice:** Add a `review` node that sets `done=False` to loop back once (see full **AI Agents** guide Sec. 11).

---

## Part 5 — Agent with tools (LangChain + ReAct)

**Theory:** An **agent** picks **tools** (search, calculator, DB) in a loop: think → act → observe.

```python
"""Part 5 — simple tool agent. Needs OPENAI_API_KEY."""
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
tools = [multiply]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Use tools when needed."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

print(executor.invoke({"input": "What is 12 times 8? Use the tool."})["output"])
```

**Practice:** Add a `@tool` that returns fake weather; ask the agent to use it.

---

## Part 6 — Agentic AI (idea + tiny pattern)

**Theory:** **Agentic** = the system **plans multiple steps** itself (not one prompt → one answer).

| Pattern | Meaning |
|---------|---------|
| **ReAct** | Reason + call tool + repeat |
| **Plan-and-execute** | Plan all steps, then run |
| **Multi-agent** | Researcher + writer + reviewer (CrewAI) |

```python
# Agentic loop (conceptual — same as Part 5, explicit steps)
def agentic_answer(question: str, max_steps: int = 3):
  context = ""
  for step in range(max_steps):
    # 1) decide action   2) run tool   3) update context
    context += f"\nStep {step + 1} done."
    if "final answer" in context.lower():
      break
  return context
```

**Deep dive:** `AI-Agents-Complete-Guide.md` — Sec. 2 (agentic), Sec. 4 (ReAct), Sec. 9 (CrewAI).

---

## Part 7 — Langfuse (trace RAG & agents)

**Theory:** **Langfuse** logs prompts, outputs, latency, and cost — like “APM for LLMs.” Use it in dev and production.

1. Create project at [https://langfuse.com](https://langfuse.com)  
2. Set keys in environment  

```python
"""Part 7 — Langfuse + LangChain. Needs OPENAI_API_KEY + Langfuse keys."""
import os
from langfuse import Langfuse
from langfuse.langchain import CallbackHandler
from langchain_openai import ChatOpenAI

# LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY, LANGFUSE_HOST in env
langfuse = Langfuse()
handler = CallbackHandler()

llm = ChatOpenAI(model="gpt-4o-mini")
response = llm.invoke(
    "Explain RAG in one sentence.",
    config={"callbacks": [handler]},
)
print(response.content)

langfuse.flush()  # send traces
# Open Langfuse UI → see trace, tokens, latency
```

| Tool | Best for |
|------|----------|
| **Langfuse** | Open-source friendly tracing, evals, cost |
| **LangSmith** | LangChain-native debugging (see Agents guide) |

**Practice:** Run Part 3 chain with `config={"callbacks": [handler]}` and inspect the trace.

---

## Part 8 — LlamaIndex (RAG-focused library)

**Theory:** **LlamaIndex** = indexing + querying documents (often simpler than building RAG from scratch).

```python
"""Part 8 — LlamaIndex minimal. pip install llama-index"""
# pip install llama-index llama-index-embeddings-huggingface

from llama_index.core import VectorStoreIndex, Document
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents = [Document(text="LlamaIndex helps build RAG over your data.")]
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
query_engine = index.as_query_engine()
# response = query_engine.query("What does LlamaIndex help with?")
# print(response)
print("Index built OK — uncomment query lines when llama-index is installed.")
```

**When to use:** Heavy document corpora, query engines, agents on top of index.  
**Interview mentions:** `RAG-Interview-Questions-Complete.md` (LangChain vs LlamaIndex vs Haystack).

---

## Part 9 — Checklist & full guides

### You should be able to explain

- [ ] RAG: chunk → embed → retrieve → generate  
- [ ] LangChain: chains, retrievers, tools  
- [ ] LangGraph: nodes, edges, loops  
- [ ] Agent vs chain: when tools are needed  
- [ ] Langfuse: why trace LLM calls  

### Read next (in order)

| Topic | Full guide |
|-------|------------|
| **RAG in production** (chunking, RAGAS, vector DBs) | `RAG-PRODUCTION-GUIDE.md` |
| Agents, CrewAI, LangGraph depth | `AI-Agents-Complete-Guide.md` |
| RAG interview & design | `RAG-Interview-Questions-Complete.md` |
| LLM interview | `LLM-Interview-Questions-Complete.md` |
| NLP + transformers | `NLP-Complete-Guide.md` |
| Master plan | `AI-ML-ZERO-TO-HERO.md` |

**Sidebar:** **AI/ML Zero to Hero** → **LLM Apps — RAG & Agents** (this file) → then **AI Agents** (full book).

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `OPENAI_API_KEY` missing | `export OPENAI_API_KEY=sk-...` |
| Slow first run | Downloads embedding model once |
| Empty retrieval | Smaller chunks or more documents |
| Langfuse no traces | Call `langfuse.flush()`; check keys / host |

---

**Done with this file?** Open **AI Agents Complete Guide** Sec. 6–11 and build one end-to-end project: **PDF → RAG → agent with tools → Langfuse trace**.
