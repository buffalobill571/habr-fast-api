from fastapi import APIRouter
from starlette.responses import Response, JSONResponse, UJSONResponse

router = APIRouter()


@router.get('/', response_class=UJSONResponse)
async def echo():
    return {"message": "ok"}
