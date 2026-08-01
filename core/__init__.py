# CORE PACKAGE
# contains alll common data models, interface,
# types and exceptions used across the framework

from .document import Document
from .chunk import Chunk

__all__ = [
    "Document" ,
     "Chunk"
]
