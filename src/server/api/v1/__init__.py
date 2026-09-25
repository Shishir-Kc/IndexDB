from fastapi import APIRouter

from src.server.api.v1.user import router as user_router

v1_router = APIRouter()
v1_router.include_router(user_router)
