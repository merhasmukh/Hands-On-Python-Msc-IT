from fastapi import FastAPI
import os

app = FastAPI(title="Dockerized App")

@app.get("/")
def read_root():
    # Read environment variable passed by Docker Compose
    db_host = os.getenv("DB_HOST", "Unknown")
    return {"message": "Hello from Docker!", "database_host": db_host}
