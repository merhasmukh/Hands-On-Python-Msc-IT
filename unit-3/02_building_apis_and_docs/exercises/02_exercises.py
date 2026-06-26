"""
02_exercises.py — APIs and Pydantic
===================================
MSc (IT) — Unit 3: Modern API Development with FastAPI

Instructions:
- Write the code below.
- Run the app using `uvicorn 02_exercises:app --reload`.
- Go to http://127.0.0.1:8000/docs to test your API!
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ===========================================================================
# Exercise 1: Create a Pydantic Model
# ===========================================================================
"""
Create a Pydantic model named `Book`.
It should have:
- title: string
- author: string
- year: integer
- pages: integer (optional, default to None)
"""
# Write your code here:


# ===========================================================================
# Exercise 2: POST Route with Request Body
# ===========================================================================
"""
Create a POST route at "/books/".
It should accept a `Book` object as a request body.
It should return a dictionary: {"message": "Book added!", "book": book}
"""
# Write your code here:


# ===========================================================================
# Exercise 3: GET Route with Path and Query Parameters
# ===========================================================================
"""
Create a GET route at "/books/{book_id}".
It should accept `book_id` as a Path Parameter (integer).
It should accept `details` as a Query Parameter (boolean, default to False).
Return {"book_id": book_id, "show_details": details}
"""
# Write your code here:


