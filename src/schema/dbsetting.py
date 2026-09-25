from pydantic import BaseModel


class Setting(BaseModel):
    installation_path: str
    debug: bool
