"""
This file is responsible for creating setting.json

"""


class IndexDBSetting:
    def __init__(self,installation_path:str,debug:bool) -> None:
        self.installation_path = installation_path 
        self.debug = debug

    async def generate_config(self):
        pass
    
