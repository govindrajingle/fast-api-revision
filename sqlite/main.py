from fastapi import FastAPI
import sqlite3

app = FastAPI()

conn = sqlite3.connect("test.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
    create table if not exists todos (
        id integer primary key,
        title text,
        completed text
    )
""")

conn.commit()


@app.get("/")
def home():
    return {"message": "sqlite connected"}
