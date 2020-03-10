from fastapi import APIRouter
from starlette.responses import Response, JSONResponse

router = APIRouter()


@router.get('/')
async def echo():
    return {"message": "ok"}
