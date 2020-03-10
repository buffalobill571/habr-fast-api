from fastapi import APIRouter
from app.api.v1.endpoints import posts, echo

router = APIRouter()

router.include_router(posts.router, prefix='/posts')
router.include_router(echo.router, prefix='/echo')
