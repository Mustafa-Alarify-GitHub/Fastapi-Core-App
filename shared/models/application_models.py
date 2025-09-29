from typing import List

from sqlmodel import Relationship
from shared.schemas.application_schemas import BaseApplication, BaseApplicationMetadata


class ApplicationMetadata(BaseApplicationMetadata, table=True):
    """
    Metadata model for applications.
    """

    __tablename__ = "application_metadata"

    application: "Application" = Relationship(back_populates="app_metadata")


class Application(BaseApplication, table=True):
    """
    Application model.
    """

    __tablename__ = "applications"

    app_metadata: List[ApplicationMetadata] = Relationship(
        back_populates="application",
        cascade_delete=True,
    )

