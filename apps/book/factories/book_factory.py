from sqlmodel import Session
from apps.book.usecases.create_book_use_case import CreateBookUseCase
from apps.book.usecases.get_books_use_case import GetBooksUseCase
from core.bases.factory import BaseFactory
from shared.domain.repositories.book_repository import BookRepository
from core.db import get_session

class BookFactory(BaseFactory):
    def __init__(self, db: Session):
        super().__init__(db)
        book_repo = BookRepository(db)
        self.get_books_use_case = GetBooksUseCase(book_repo)
        self.create_book_use_case = CreateBookUseCase(book_repo)
