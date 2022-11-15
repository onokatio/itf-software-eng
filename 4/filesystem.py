from directory import Directory
from file import File
from abc import ABC, abstractmethod
from typing import Optional


class FileSystem(ABC):
    _instance: Optional[FileSystem] = None

    @staticmethod
    def get_instance(cls):
        # 唯一のインスタンスを(必要なら生成して)返す．

        # (ここに何らかの処理を記述する)
        if FileSystem._instance == None:
            FileSystem._instance = cls.__new__()

        return FileSystem._instance

    @abstractmethod
    def create_directory(self, name: str) -> Directory:
        pass

    @abstractmethod
    def create_file(self, name: str) -> File:
        pass


class _SimpleFileSystem(FileSystem):
    def create_directory(self, name: str) -> Directory:
        return Directory(name)

    def create_file(self, name: str) -> File:
        return File(name)
