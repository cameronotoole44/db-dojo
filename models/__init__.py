from sqlmodel import SQLModel
from .user import User
from .order import Order

def all_metadata():
    return SQLModel.metadata
