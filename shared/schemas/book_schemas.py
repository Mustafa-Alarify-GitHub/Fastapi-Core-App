from typing import Optional
from sqlmodel import SQLModel, Field
from core.bases.model import BaseModel, BaseTimesTempModel
import strawberry


class BaseBookSchema(BaseTimesTempModel):
    name: str


class BaseAuthorSchema(BaseTimesTempModel):
    name: str
    phone: str


class BaseAuthorBookSchema(BaseModel):
    book_id: int = Field(foreign_key="books.id", primary_key=True)
    author_id: int = Field(foreign_key="authors.id", primary_key=True)
