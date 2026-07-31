from dataclasses import dataclass , field
from typing import Dict,Any

@dataclass 
class Document:
    """Represent a single document or page extracted from a source"""

    text:str
    metadata:Dict[str,Any] = field(default_factory  = dict)

    def __len__(self) -> int:
        """
        Return the number of characters
        """

    @property
    def word_count(self) ->int:
        """
        return the total number of words in the document
        """

    def preview(self,chars:int=100) ->str:
        """
        Returns the first few characters
        """
        return self.text[:chars] + ("..."if len(self.text)>chars else "")

    def to_dict(self) ->Dict[str,Any]:
        """
        Convert Documnet to dictionary
        """
        return{
        "text":self.text,
        "metadata": self.metadata 
        }

    