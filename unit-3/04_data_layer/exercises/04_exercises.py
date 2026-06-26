"""
04_exercises.py — Data Layer
============================
MSc (IT) — Unit 3: Modern API Development with FastAPI

Instructions:
- Write the code below.
- Run the app using `uvicorn 04_exercises:app --reload`.
"""

from fastapi import FastAPI, Depends

app = FastAPI()

# ===========================================================================
# Exercise 1: Create a basic Dependency
# ===========================================================================
"""
Create a dependency function `verify_token(token: str)`.
If the token is NOT "supersecret", raise an HTTPException with status 400.
If it is correct, return "Valid Token".
"""
# Write your code here:


# ===========================================================================
# Exercise 2: Use the Dependency in a Route
# ===========================================================================
"""
Create a GET route at "/secure-data".
It should use `verify_token` as a Dependency.
If successful, it should return {"data": "This is highly classified data."}.
"""
# Write your code here:


