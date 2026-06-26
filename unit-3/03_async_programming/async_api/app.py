import asyncio
import time
from fastapi import FastAPI

app = FastAPI(title="Async vs Sync Demo")

@app.get("/")
def home():
    return {"message": "Go to /docs to test the endpoints"}

# ---------------------------------------------------------
# 1. The Right Way to be Sync
# ---------------------------------------------------------
@app.get("/sync-slow")
def sync_slow():
    """
    FastAPI runs standard 'def' routes in a threadpool.
    So even though time.sleep() blocks, it only blocks ONE thread.
    Other requests can still be processed.
    """
    print("Starting sync sleep...")
    time.sleep(3)
    print("Finished sync sleep!")
    return {"message": "Sync sleep finished"}

# ---------------------------------------------------------
# 2. The Right Way to be Async
# ---------------------------------------------------------
@app.get("/async-slow")
async def async_slow():
    """
    Proper async. Uses asyncio.sleep(), which gives control 
    BACK to the event loop while waiting. Very efficient!
    """
    print("Starting async sleep...")
    await asyncio.sleep(3)
    print("Finished async sleep!")
    return {"message": "Async sleep finished"}

# ---------------------------------------------------------
# 3. The WRONG Way! (Do not do this)
# ---------------------------------------------------------
@app.get("/bad-async")
async def bad_async():
    """
    DANGER! We declared this 'async def', meaning FastAPI runs it 
    directly on the main event loop. 
    But we use a blocking time.sleep(). This freezes the ENTIRE SERVER 
    for 3 seconds. Nobody else can connect!
    """
    print("Starting BAD async sleep...")
    time.sleep(3)
    print("Finished BAD async sleep!")
    return {"message": "I just blocked the server for 3 seconds."}

# Run with: uvicorn app:app --reload
