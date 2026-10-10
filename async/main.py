# async = non blocking execution
# await = waits for comletion of instruction
import asyncio
import time

from fastapi import FastAPI

# def task():
#     time.sleep(3)
#     return "task done after 3 seconds"


async def task():
    await asyncio.sleep(3)
    return "task done after 3 seconds"


app = FastAPI()


@app.get("/")
async def home():
    await asyncio.sleep(3)
    return {"message": "async api"}
