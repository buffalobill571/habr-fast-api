from fastapi import APIRouter
from app.api.websocket.endpoints import init

router = APIRouter()

router.include_router(init.router, prefix='/posts')
