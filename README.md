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

# HYBRID RETRIEVAL ENGINE

      User Query
            │
            ▼
      Retriever
            │
            ▼
      Hybrid Retriever
            │
            ├── Dense Retriever (FAISS)
            ├── Sparse Retriever (BM25)
            └── RRF Fusion
            ▼
      RetrievalResult[]
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
