from typing import List
from core.bases.use_case import BaseUseCase
from shared.domain.entities.book_entity import BookEntity


class GetBooksUseCase(BaseUseCase):
    def execute(self)-> List[BookEntity]:
        return self.repo.all()
