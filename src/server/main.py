from fastapi import FastAPI, status

server = FastAPI(title="IndexDB", version="0.0.1", description="A simple DB Engine")

server.get("/")


async def health():
    return {"status": status.HTTP_200_OK}
