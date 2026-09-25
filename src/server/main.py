from fastapi import FastAPI, status

from src.logging.logger import logger as log
from src.server.api.v1 import v1_router

server = FastAPI(title="IndexDB", version="0.0.1", description="A simple DB Engine")


@server.get("/", tags=["health"])
async def health():
    log.info("health")
    return {"status": status.HTTP_200_OK}


server.include_router(v1_router, prefix="/api/v1")
