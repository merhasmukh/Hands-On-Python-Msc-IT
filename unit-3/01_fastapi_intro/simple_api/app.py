from fastapi import FastAPI

# Create the FastAPI instance
app = FastAPI()

# Define a root GET route
@app.get("/")
def read_root():
    return {"message": "Welcome to your first FastAPI application!"}

# Define another GET route
@app.get("/ping")
def ping():
    return {"status": "success", "message": "pong"}

# To run this file, open your terminal, navigate to this folder, and run:
# uvicorn app:app --reload
# Then open your browser at http://127.0.0.1:8000
