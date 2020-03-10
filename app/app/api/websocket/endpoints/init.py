import asyncio
import json
import logging
from typing import List

from fastapi import APIRouter, Depends
from starlette.websockets import WebSocket

from app import crud
from app.api.utils.db import get_db
from app.api.utils.errors import NotFoundSchema
from app.db.session import Session
from app.schemas.post import Post


router = APIRouter()
logger = logging.getLogger(__name__)


@router.websocket("/", name="posts-channel")
async def read_posts(
    websocket: WebSocket,
):
    db = Session()
    await websocket.accept()
    while True:
        message = await websocket.receive_text()
        try:
            post_id = int(message)
        except ValueError:
            break
        post = crud.post.get(db, post_id)
        if not post:
            await websocket.send_json(NotFoundSchema(message="Post not found").dict())
            continue
        logger.warning(f"post id = {post_id} = {post}")
        post = Post.from_orm(post)
        await websocket.send_text(json.dumps(post.dict(), default=lambda a: str(a)))
    await websocket.close()
