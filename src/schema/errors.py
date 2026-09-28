from pydantic import BaseModel


class GeneralError(BaseModel):
    status: str
    reason: str
    detail: str
