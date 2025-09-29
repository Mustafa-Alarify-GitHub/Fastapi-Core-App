from typing import Optional
from core.bases.model import BaseModel


class BookEntity(BaseModel):
    id: int
    book_name: str
