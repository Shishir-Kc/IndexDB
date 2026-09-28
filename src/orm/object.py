import asyncio
from enum import pickle_by_enum_name
import os
from os.path import abspath
from pathlib import Path

import aiofiles

from src.config.settings import (
    ROOT_PATH,  # ROOT_PATH => path where IndexDB and it's content is stored !,
    SETTING_NAME,  # SETTING_NAME => name for the json file .
)
from src.schema.errors import GeneralError


class Objects:
    def __init__(self) -> None:
        self.root_path = ROOT_PATH

    def _checkpath(self, path):
        """
        Args:

         path:str => path of the expected directory

        Working: It will return bool for thr given condition,
        were if dir exists then it returns True and False if it doen't.

        Returns:

            Bool


        """
        return os.path.isdir(f"{Path.home()}/{path}")

    async def _create_dir(self, path: str="",abpath:str=""):
        """
            Args: 

            path: path / dir you want to create .

            Working: creates a path from {self.root_path} to the path you desire
        """
        if abpath:
            os.makedirs(abpath,exist_ok=True)

        if not self._checkpath(f"{self.root_path}/{path}"):
            try:
                os.makedirs(f"{Path.home()}/{self.root_path}/{path}")
            except OSError as e:
                return GeneralError(
                    status="failed",
                    reason="I/O operations",
                    detail=f"Unnable to create  {path} due to I/O operations. \n {e!s}",
                )
        return GeneralError(
            status="failed",
            reason="DataBase dir exists",
            detail="DataBase dir already exists on this machine.",
        )

    async def _create_file(self,path:str="",abpath:str=""):
        """

            Args 

                path:str => path for the fiel that you want to create 
                
                abpath: str => direct path controll 

            Working : wil create a file under self.root .
        """
        temp_path= abpath 
        if not abpath:

         temp_path = f"{Path.home()}/{self.root_path}/{path}"
        
        print(temp_path)
        try:
            async with aiofiles.open(temp_path,"w") as file:
               await file.close()
        except OSError as e:
                return GeneralError(
                    status="failed",
                    reason="I/O operations",
                    detail=f"Unnable to create  {path} due to I/O operations. \n {e!s}",
                )
 

    async def _read_setting(self):
        if self._checkpath(self.root_path):
            try:
                async with aiofiles.open(
                    f"{Path.home() / ROOT_PATH}/{SETTING_NAME}", "r"
                ) as file:
                    data = await file.read()
                if not data.strip():
                    return GeneralError(
                        status="failed",
                        reason="setting_content_is_empty",
                        detail="looks like setting content has been removed or tampered .",
                    )
                return data

            except FileNotFoundError as e:
                return GeneralError(
                    status="failed", reason="file_not_found", detail=str(e)
                )
            except OSError as e:
                return GeneralError(
                    status="failed", reason="I/O operations", detail=str(e)
                )
        return GeneralError(
            status="failed",
            reason="IndexDB path not found",
            detail="IndexDB is no where to found ",
        )

    async def create_database(self, data_base_name: str):
        """
            Args:

            data_base_name: str => name of your database

        Working: it will create a database with the naem you have given and be stored on DataBase root directory.

        """
        await self._create_dir(path="DataBase")
        await self._create_dir(path=f"DataBase/{data_base_name}")
        await self._create_file(f"DataBase/{data_base_name}/index.json")
        return Path.home() / self.root_path / "DataBase" / data_base_name

    async def create_table(self,table_name:str,database_path:str):
        """
            Args:

                table_name :  str => name of your table 
    
            Working : will create a tbale of your given name 

        """

        await self._create_dir(abpath=f"{database_path}/Table")
        await self._create_file(abpath=f"{database_path}/Table/{table_name}.json") 

def main():
    object = Objects()
    print(asyncio.run(object._read_setting()))
    database = asyncio.run(object.create_database(data_base_name="testing"))
    print(asyncio.run(object.create_table(table_name="trial",database_path=str(database))))
