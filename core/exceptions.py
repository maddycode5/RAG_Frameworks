# Framework exceptions

class RAGFrameworkException(Exception):
    """
    BaseFramework Exception
    """
    pass
class DocumentLoaderError(RAGFrameworkException):
    """
    Raised when Document loading fails
    """
class EmbeddingError(RAGFrameworkException):
    """
    Raised when Embedding generation fails
    """
    pass

class ChunkingError(RAGFrameworkException):
    """
    Raised when Chunking fails
    """
    pass
class VectorStoreError(RAGFrameworkException):
    """
    Raised when VectorStore operation fails
    """
    pass
class RetrievalError(RAGFrameworkException):
    """
    Raised when Retrieval operation fails
    """
    pass
