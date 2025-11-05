from fastapi import FastAPI
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://user:password@db-endpoint:5432/demo"
engine = create_engine(DATABASE_URL)

app = FastAPI()

@app.get("/users")
def get_users():
    with engine.connect() as conn:
        rows = conn.execute(text("SELECT * FROM users")).mappings().all()
        return list(rows)