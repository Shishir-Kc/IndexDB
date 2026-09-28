from pydantic import BaseModel


class Setting(BaseModel):
    """
    This schema is used to create
     - dbsettings.json
    """

    root_path: str
    debug: bool
    version: str
    data_bases_path: str
