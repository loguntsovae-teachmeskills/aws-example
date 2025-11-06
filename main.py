from fastapi import FastAPI
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://postgres:postgres@demo-db.c7umuy8uul98.eu-central-1.rds.amazonaws.com:5432/demo"
engine = create_engine(DATABASE_URL)

app = FastAPI()

@app.get("/")
def index():
    return {"status": "ok"}

@app.get("/users")
def get_users():
    with engine.connect() as conn:
        rows = conn.execute(text("SELECT * FROM users")).mappings().all()
        return list(rows)