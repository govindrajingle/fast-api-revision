from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app = FastAPI()

# Create the limiter using the client's IP address.
limiter = Limiter(key_func=get_remote_address)

# Attach the limiter to the FastAPI application.
app.state.limiter = limiter


# Handle requests that exceed the configured limit.
@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(status_code=429, content={"detail": "Too many requests"})


# Allow a maximum of 5 requests per minute per client IP.
@app.get("/data")
@limiter.limit("5/minute")
async def get_data(request: Request):
    return {"message": "success"}
