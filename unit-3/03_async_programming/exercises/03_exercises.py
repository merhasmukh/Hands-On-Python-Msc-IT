"""
03_exercises.py — Async Programming
===================================
MSc (IT) — Unit 3: Modern API Development with FastAPI

Instructions:
- Write the code below.
- Run the app using `uvicorn 03_exercises:app --reload`.
"""

from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

# ===========================================================================
# Exercise 1: Write an Async Route
# ===========================================================================
"""
Create a GET route at "/download" that is ASYNCHRONOUS.
It should simulate downloading a file by awaiting asyncio.sleep(2).
Return {"status": "Download complete"}
"""
# Write your code here:


# ===========================================================================
# Exercise 2: Identify the Bug
# ===========================================================================
"""
The route below is badly designed and will block the server. 
Fix it by either:
1. Changing it to a standard synchronous function (remove `async`)
2. Or replacing `time.sleep` with `await asyncio.sleep`
"""
@app.get("/buggy")
async def buggy_route():
    time.sleep(2)  # This is bad!
    return {"message": "I fixed the bug!"}


