from typing import Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import text

class Order(SQLModel, table=True):
    __tablename__ = "order"
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(index=True, foreign_key="user_id")
    total_cents: int
    created_at: str = Field(
        default=None,
        sa_column_kwargs={"server_default": text("now()")}
    )
