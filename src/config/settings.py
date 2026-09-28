"""
This file is responsible for creating setting.json.

it's settings will be used to derive the behaviour of the DB it self.

NOTE: There is a posibillity for 2 setting implementation .
"""

import asyncio
import os
from pathlib import Path

import aiofiles

from src.logging.logger import logger as log
from src.schema.dbsetting import Setting

ROOT_PATH = ".config/IndexDB"
SETTING_NAME = "dbsetting.json"


class IndexDBSetting:
    def __init__(
        self,
        debug: bool,
        version: str,
        data_bases_path: str,
        setting_name: str = SETTING_NAME,
        root_path: str = ROOT_PATH,
    ) -> None:

        self.root_path = root_path
        self.debug = debug
        self.version = version
        self.setting_name = setting_name
        self.data_bases_path = data_bases_path
        self.is_path = asyncio.run(self._creatandcheckroot())
        self.INDEXDBROOT = Path.home() / self.root_path

    async def _creatandcheckroot(self):
        """
        This is an internal method which will check
        if there is a root file or not if there is no
        root file it will create one and if there is one
        then it will do no nothing
        """
        log.info("checking for existance of root path ")
        os.makedirs(f"{Path.home()}/{self.root_path}", exist_ok=True)

    async def generate_config(self):
        async with aiofiles.open(
            f"{self.INDEXDBROOT}/{self.setting_name}", "w"
        ) as file:
            await file.write(
                Setting(
                    root_path=self.root_path,
                    debug=self.debug,
                    version=self.version,
                    data_bases_path=f"{self.INDEXDBROOT}/{self.data_bases_path}",
                ).model_dump_json(indent=2)
            )


def main():
    test = IndexDBSetting(
        root_path=ROOT_PATH, debug=True, version="0.1.0", data_bases_path="DataBase"
    )
    asyncio.run(test.generate_config())
