from abc import ABC , abstractmethod

from sqlmodel import Session

class BaseFactory(ABC):
    def __init__(self, db:Session):
        self.db = db