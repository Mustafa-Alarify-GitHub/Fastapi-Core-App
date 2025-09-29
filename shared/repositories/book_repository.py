from typing import List, Optional
from shared.domain.entities.book_entity import BookEntity 
from core.bases.repo import BaseRepo
from sqlmodel import select, Text

from shared.models.application_models import Application
from shared.models.book_models import Book

class BookRepository(BaseRepo):
    def all(self) -> List[BookEntity]:
        books = self.db.exec(select(Book)).all() # tuple[Type[Book]] | List[Book] // orm
        
        return [
            BookEntity(id= book.id,book_name=book.name) for book in books
        ]
    
    def create(self,name:str)->BookEntity:
        book = Book(
            name=name
        )
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)

        return BookEntity(id= book.id,book_name=book.name)
         

            





