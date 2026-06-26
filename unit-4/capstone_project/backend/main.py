from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import sqlite3

app = FastAPI(title="Capstone API")

# Allow requests from the frontend (in production, specify the exact domain)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Run DB init on startup
init_db()

class Message(BaseModel):
    text: str

@app.get("/api/messages")
def get_messages():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, text FROM messages")
    messages = [{"id": row[0], "text": row[1]} for row in cursor.fetchall()]
    conn.close()
    return {"messages": messages}

@app.post("/api/messages", status_code=201)
def create_message(msg: Message):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (text) VALUES (?)", (msg.text,))
    conn.commit()
    conn.close()
    return {"status": "Message added successfully"}

@app.get("/api/health")
def health_check():
    # Example of reading an environment variable
    environment = os.getenv("ENVIRONMENT", "development")
    return {"status": "ok", "environment": environment}
