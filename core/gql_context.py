from sqlmodel import Session
from strawberry.fastapi import BaseContext

from core.db import get_session
class GQLContext(BaseContext):

    @property
    def db(self)-> Session:
        return get_session()
    

async def get_context() -> GQLContext:
    return GQLContext()