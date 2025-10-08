import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session, create_engine, select

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=ENV_PATH)

DATABASE_URL = os.getenv("DATABASE_URL")
assert DATABASE_URL, "DATABASE_URL not set in .env"
engine = create_engine(DATABASE_URL, echo=False)

app = FastAPI(title="DB Dojo")

def get_session():
    with Session(engine) as s:
        yield s

@app.get("/health")
def health():
    return {"ok": True}

from models.user import User
from models.order import Order

@app.get("/users")
def list_users(limit: int = 20, session: Session = Depends(get_session)):
    return session.exec(select(User).limit(limit)).all()

@app.get("/orders/summary")
def orders_summary(session: Session = Depends(get_session)):
    q = """
      select u.id as user_id, count(o.id) as orders, coalesce(sum(o.total_cents),0) as total_cents
      from "user" u left join "order" o on o.user_id = u.id
      group by u.id
      order by orders desc, user_id asc
      limit 20
    """
    rows = session.exec(q)
    return [dict(r) for r in rows]

