from typing import Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import text

class User(SQLModel, table=True):
    __tablename__= "user"
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    full_name: str
    created_at: str = Field(
        default=None,
        sa_column_kwargs={"server_default": text("now()")}
    )
