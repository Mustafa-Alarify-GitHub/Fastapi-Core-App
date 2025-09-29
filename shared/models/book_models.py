from typing import List

from sqlmodel import Relationship
from shared.schemas.book_schemas import BaseAuthorBookSchema, BaseAuthorSchema, BaseBookSchema

class AuthorBook(BaseAuthorBookSchema,table=True):
    __tablename__= "author_books"

class Book(BaseBookSchema, table=True):
    __tablename__ = "books"

    authors: List["Author"] = Relationship(
        back_populates="books",
        link_model=AuthorBook
    )


class Author(BaseAuthorSchema, table=True):
    __tablename__ = "authors"

    books: List["Book"] = Relationship(
        back_populates="authors",
        link_model=AuthorBook
    )

