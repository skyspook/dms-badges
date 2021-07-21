from fastapi import APIRouter
from app.api.api_v1.endpoints import groups, badges

api_router = APIRouter()
api_router.include_router(groups.router, tags=["groups"])
api_router.include_router(badges.router, tags=["badges"])
