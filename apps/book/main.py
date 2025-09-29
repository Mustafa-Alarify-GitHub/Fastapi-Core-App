from multiprocessing import get_context
from fastapi import FastAPI

from apps.book.factories.book_factory import BookFactory
from apps.book.gql.queries.book_query import BookGqlQuery
from core.db import get_session
import strawberry
from strawberry.fastapi import GraphQLRouter
from core.gql_context import get_context

book_app = FastAPI()
db = get_session()
factory = BookFactory(db)


@book_app.get("/")
def get_books():
    return factory.get_books_use_case.execute()


@book_app.post("/")
def create_books(name: str):
    return factory.create_book_use_case.execute(name)


schema = strawberry.Schema(
    query=BookGqlQuery
)
graphql_app = GraphQLRouter(schema, context_getter=get_context)
book_app.include_router(graphql_app, prefix="/graphql")
