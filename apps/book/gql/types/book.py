import strawberry
from shared.domain.entities.book_entity import BookEntity


@strawberry.experimental.pydantic.type(
    model=BookEntity,
    all_fields=True
    #fields=[
     #   'id',
     #   "name"
    #]
)
class BookGqlType:
    pass