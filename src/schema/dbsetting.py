from pydantic import BaseModel


class Setting(BaseModel):
    """
    This schema is used to create
     - dbsettings.json
    """

    installation_path: str
    debug: bool
    version: str
