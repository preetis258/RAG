# RAG 1 — RAG From Scratch

A simple Retrieval-Augmented Generation (RAG) system built **without LangChain**.

The purpose of this project is to understand the fundamental components of a RAG pipeline by implementing each stage independently instead of relying on a RAG framework.

---

## Objective

The goal of this project is to understand what happens internally in a RAG system:

- How documents are loaded
- How documents are split into chunks
- How text is converted into embeddings
- How embeddings are stored and searched
- How a user query is embedded
- How relevant chunks are retrieved
- How retrieved context is passed to an LLM
- How the LLM generates the final answer

This project intentionally avoids LangChain abstractions so that each component of the RAG pipeline can be understood independently.

---

## Architecture

```text
                         INDEXING
                            │
                            ▼
                          PDF
                            │
                            ▼
                         Loader
                            │
                            ▼
                         Chunking
                            │
                            ▼
                        Embeddings
                            │
                            ▼
                          FAISS
                            │
                            │
                            ▼
                         RETRIEVAL
                            │
                         User Query
                            │
                            ▼
                    Query Embedding
                            │
                            ▼
                        Retriever
                            │
                            ▼
                       Top-K Chunks
                            │
                            ▼
                          Prompt
                            │
                            ▼
                           LLM
                            │
                            ▼
                         Answer