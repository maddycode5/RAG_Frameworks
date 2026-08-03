from pathlib import Path
# ------------------
# PROJECT PATHS
# ------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
RAW_PDF_DIR = DATA_DIR / "raw_pdfs"
PROCESSED_DIR = DATA_DIR / "processed"
VECTOR_STORE_DIR = DATA_DIR / "vector_store"
FAISS_INDEX_FILE = VECTOR_STORE_DIR / "faiss.index"
FAISS_MAPPING_FILE = VECTOR_STORE_DIR / "chunk_ids.pkl"

BM25_INDEX_FILE =VECTOR_STORE_DIR / "bm25.pkl"

EMBEDDINGS_CACHE_DIR = DATA_DIR /"embeddings"

# ------------------
# CHUNKING
# ------------------

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# -----------------
# EMBEDDINGS
# -----------------

EMBEDDING_BATCH_SIZE =32

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

#-------------------
# VECTOR STORE 
#-------------------

VECTOR_STORE ="FAISS"

TOP_K = 5

# ---------------
# RETRIEVAL
# --------------

RETRIEVAL_TYPE = "hybrid"

# options
# dense
# hybrid
# multiquery
# hyde
# parent_child
# contextual
# self_rag
# crag
# adaptive

# ==========================
# RERANKER
# ==========================

USE_RERANKER = False

RERANKER_MODEL = "BAAI/bge-reranker-base"

# ------------------
# LLM
# ----------------

LLM_PROVIDER= "ollama"
LLM_NAME = "llama3"
TEMPERATURE = 0.2
MAX_TOKENS = 512
