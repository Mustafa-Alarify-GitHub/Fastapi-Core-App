from abc import ABC, abstractmethod

from core.bases.model import BaseModel
from core.bases.repo import BaseRepo

class BaseUseCase(ABC):
    def __init__(self, repo:BaseRepo):
        self.repo = repo

    @abstractmethod
    def execute(self):
        pass