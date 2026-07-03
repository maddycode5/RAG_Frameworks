from pathlib import Path
# ------------------
# PROJECT PATHS
# ------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA = DATA_DIR / "raw_pdfs"
VECTOR_DB = DATA_DIR / "vector_store"

# ------------------
# CHUNKING
# ------------------

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# -----------------
# EMBEDDINGS
# -----------------

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

#-------------------
# VECTOR STORE 
#-------------------

VECTOR_STORE ="FAISS"

TOP_K = 5

# ---------------
# RETRIEVAL
# --------------

RETRIEVAL_TYPE = "dense"

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
