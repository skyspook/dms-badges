from fastapi import FastAPI, Request, Depends
from app.core.settings import settings
from app.api.api_v1.api import api_router
from starlette.requests import Request
from starlette.responses import HTMLResponse

app = FastAPI()

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get('/')
async def homepage(
    request: Request
    ):
    return HTMLResponse('<h1>Hello World</h1>')