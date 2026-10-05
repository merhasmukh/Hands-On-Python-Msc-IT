import asyncio
import time
from fastapi import FastAPI

app = FastAPI()


@app.get("/async")
async def async_route():

    print("ASYNC started")

    await asyncio.sleep(5)

    print("ASYNC finished")

    return {"message": "async done"}


@app.get("/normal")
def normal_route():

    print("NORMAL started")

    time.sleep(5)

    print("NORMAL finished")

    return {"message": "normal done"}