from fastapi import FastAPI, status
from src.logging.logger import logger as log

server = FastAPI(title="IndexDB", version="0.0.1", description="A simple DB Engine")


@server.get("/", tags=["health"])
async def health():
    log.info("health")
    return {"status": status.HTTP_200_OK}
