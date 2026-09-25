"""
This file is responsible for creating setting.json.

it's settings will be used to derive the behaviour of the DB it self.

NOTE: There is a posibillity for 2 setting implementation .
"""

import asyncio

import aiofiles

from src.schema.dbsetting import Setting


class IndexDBSetting:
    def __init__(self, installation_path: str, debug: bool,version:str) -> None:
        self.installation_path = installation_path
        self.debug = debug
        self.version = version

    async def generate_config(self):
        async with aiofiles.open("dbsetting.json", "w") as file:
            await file.write(
                Setting(
                    installation_path=self.installation_path,
                    debug=self.debug,
                    version=self.version,
                ).model_dump_json(indent=2)
            )


def main():
    test = IndexDBSetting(installation_path=".config/IndexDB", debug=True,version="0.1.0")
    asyncio.run(test.generate_config())
