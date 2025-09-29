from typing import List
import strawberry
from apps.book.factories.book_factory import BookFactory
from core.gql_context import GQLContext

from apps.book.gql.types.book import BookGqlType

@strawberry.type
class BookGqlQuery:

    @strawberry.field
    def books(self,info: strawberry.Info[GQLContext])->List[BookGqlType]:
        factory = BookFactory(info.context.db)

        books = factory.get_books_use_case.execute()

        return [
            BookGqlType.from_pydantic(book) for book in books
        ]