from fastapi import APIRouter, status

router = APIRouter(tags=["users"])


@router.get("/user/health")
async def user_health():
    """
    Currently it is just for test and will not be on final product.
    """
    return {"status": status.HTTP_200_OK}
