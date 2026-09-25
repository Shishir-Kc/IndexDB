"""
This file is responsible for creating setting.json

"""

import asyncio

import aiofiles

from src.schema.dbsetting import Setting


class IndexDBSetting:
    def __init__(self, installation_path: str, debug: bool) -> None:
        self.installation_path = installation_path
        self.debug = debug

    async def generate_config(self):
        async with aiofiles.open("dbsetting.json", "w") as file:
            await file.write(
                Setting(
                    installation_path=self.installation_path, debug=self.debug
                ).model_dump_json(indent=2)
            )


def main():
    test = IndexDBSetting(installation_path=".config/IndexDB", debug=True)
    asyncio.run(test.generate_config())
