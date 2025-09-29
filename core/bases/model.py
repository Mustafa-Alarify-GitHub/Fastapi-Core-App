from typing import Optional, Literal
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


class BaseModel(SQLModel):
    pass


class BaseSchemaModel(BaseModel):
    id: int = Field(default=None, primary_key=True)


class BaseTimesTempModel(BaseSchemaModel):
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: Optional[datetime] = Field(default=None)


class BaseLogModel(BaseModel):
    log_id: int = Field(default=None, primary_key=True)
    log_sequence: Optional[int] = Field(default=None, index=True)
    log_action: Literal["create", "update", "delete"] = Field(default="create")
    log_user_id: Optional[int] = Field(default=None)
    log_timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
