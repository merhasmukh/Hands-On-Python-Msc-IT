"""
05_exercises.py — Security and Middleware
=========================================
MSc (IT) — Unit 3: Modern API Development with FastAPI

Instructions:
- Write the code below.
- Run the app using `uvicorn 05_exercises:app --reload`.
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI()

# ===========================================================================
# Exercise 1: Add CORS Middleware
# ===========================================================================
"""
Add the CORSMiddleware to the `app`.
Allow the origin "http://localhost:3000".
Allow all methods and all headers.
"""
# Write your code here:



# ===========================================================================
# Exercise 2: Add Custom Middleware
# ===========================================================================
"""
Create a custom middleware using `@app.middleware("http")`.
It should intercept the request, calculate how long the request took (in seconds),
and print the message: "Request took X seconds" to the terminal console.
Then it should return the response.
"""
# Write your code here:



@app.get("/")
def home():
    time.sleep(1) # Simulating a slow database query
    return {"message": "Hello World"}
