from pydantic import BaseModel
from typing import Optional

class Document(BaseModel):
    title: str
    content: str
    category: Optional[str] = None
