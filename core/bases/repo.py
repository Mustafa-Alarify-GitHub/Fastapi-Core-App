from sqlmodel import Session


class BaseRepo:
    
    def __init__(self, db: Session):
        self.db = db