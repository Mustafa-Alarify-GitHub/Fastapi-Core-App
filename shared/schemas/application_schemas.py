from sqlmodel import SQLModel, Field

from typing import Optional, List
from enum import Enum


class ApplicationStatus(str, Enum):
    """
    Enum representing the status of an application.
    """

    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    DEPRECATED = "deprecated"
    UNKNOWN = "unknown"
    # Add more statuses as needed


class BaseApplication(SQLModel):
    """
    Base class for all applications.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    version: str
    status: ApplicationStatus = Field(default=ApplicationStatus.UNKNOWN)


class BaseApplicationMetadata(SQLModel):
    """
    Metadata class for applications.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    application_id: int = Field(foreign_key="applications.id")
    key: str
    value: str
