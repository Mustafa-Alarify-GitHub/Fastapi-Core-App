from core.bases.use_case import BaseUseCase
from shared.domain.entities.book_entity import BookEntity


class CreateBookUseCase(BaseUseCase):
    def execute(self,name:str)-> BookEntity:
        return self.repo.create(name)