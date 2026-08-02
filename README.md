# RAG Framework

A modular Retrieval-Augmented Generation framework built completely from scratch using Python.

# current Framework

                    PDF
                     │
                     ▼
               Ingestion Pipeline
                     │
                     ▼
                  Chunks
                     │
                     ▼
             Embedding Pipeline
                     │
                     ▼
                Embedding Objects
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
    ChunkRepository        FAISS Store
          │
          ▼
      BM25 Store
          │
          ▼
      Index Manager



## Features

- Dense Retrieval
- Hybrid Search
- Multi Query Retrieval
- HyDE
- Parent Child Retrieval
- Contextual Compression
- Self RAG
- CRAG
- Adaptive RAG
- Cross Encoder Re-ranking
- FAISS Vector Store
- Ollama Integration
- Streamlit UI
