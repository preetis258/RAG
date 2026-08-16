# RAG Projects & Experiments

This repository contains my hands-on work, experiments, and implementations related to **Retrieval-Augmented Generation (RAG)**.

The goal of this repository is to understand RAG systems from fundamentals to advanced production-oriented architectures.

Rather than only using frameworks and pre-built abstractions, the projects progressively explore what happens internally at each stage of a RAG pipeline.

---

## Repository Goals

This repository is being built as a practical learning journey covering:

- Document ingestion
- Document parsing
- Text chunking
- Embeddings
- Vector databases
- Similarity search
- Retrieval strategies
- Prompt construction
- LLM generation
- Retrieval evaluation
- RAG debugging
- RAG optimization
- Advanced retrieval techniques

The emphasis is on **understanding the reasoning behind each component**, not just implementing it.

---

# Projects

## 1. Manual RAG

📁 `manual_rag/`

A basic RAG system implemented **without LangChain**.

The purpose of this project is to understand the individual components of a RAG pipeline by implementing them separately.

### Pipeline

```text
PDF
 ↓
Document Loader
 ↓
Chunking
 ↓
Embedding Model
 ↓
FAISS
 ↓
Query Embedding
 ↓
Retriever
 ↓
Context
 ↓
Prompt
 ↓
LLM
 ↓
Answer