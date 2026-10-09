from fastapi import FastAPI, Request
import time

app = FastAPI()


@app.middleware("http")
async def log_middleware(req: Request, call_next):
    start_time = time.time()
    res = await call_next(req)
    processed_time = time.time() - start_time
    print(f"path: {req.url.path} | Time: {processed_time}")
    return res


# @app.middleware("http")
async def my_middleware(req: Request, call_next):
    print("request received")
    res = await call_next(req)
    print("response sent")
    return res
