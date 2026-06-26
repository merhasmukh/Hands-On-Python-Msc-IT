"""
06_exercises.py — Testing and Pytest
====================================
MSc (IT) — Unit 3: Modern API Development with FastAPI

Instructions:
- Below is a simple FastAPI application.
- Write Pytest tests to verify it works correctly.
- Run `pytest 06_exercises.py` in your terminal to see if you pass!
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/math/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}

# ===========================================================================
# The TestClient
# ===========================================================================
client = TestClient(app)

# ===========================================================================
# Exercise 1: Write a Test for Addition
# ===========================================================================
"""
Write a function `test_add_numbers_success()` that uses `client.get(...)`
to send a request to `/math/add?a=5&b=10`.
Assert that the status code is 200.
Assert that the JSON response is {"result": 15}.
"""
# Write your code here:


# ===========================================================================
# Exercise 2: Write a Test for Validation Error
# ===========================================================================
"""
Write a function `test_add_numbers_validation_error()` that sends a request
with a string instead of an integer: `/math/add?a=five&b=10`.
Assert that the status code is 422 (Unprocessable Entity).
"""
# Write your code here:

