from Helpers.abstract_class import Abstract
from typing import List
from enum import Enum


class WRITE_MODE:
    APPEND_BINARY = 3
    WRITE_BINARY = 1
    APPEND = 2
    WRITE = 0


class READ_MODE(Enum):
    BINARY = 1
    DEFAULT = 0


class FILE_ENCODING(Enum):
    ISO_8859_1 = 3
    UTF_16 = 1
    ASCII = 2
    UTF_8 = 0
    CP1252 = 4


class File:
    isDirectory: bool = False
    extension: str = None
    name: str = None
    directory: str
    fullName: str
    fullPath: str

    def Read(self, readMode: READ_MODE = READ_MODE.DEFAULT, encoding: FILE_ENCODING = FILE_ENCODING.UTF_8) -> str:
        if self.isDirectory:
            return

        with open(self.fullPath, mode=FileHelper.GetReadMode(readMode), encoding=FileHelper.GetEncoding(encoding)) as f:
            return f.read()

    def WriteLine(self, content: str, clearFile=False, writeMode: WRITE_MODE = WRITE_MODE.WRITE, encoding: FILE_ENCODING = FILE_ENCODING.UTF_8) -> None:
        if self.isDirectory:
            return

        with open(self.fullPath, mode=FileHelper.GetWriteMode(writeMode), encoding=FileHelper.GetEncoding(encoding)) as f:

            if clearFile:
                f.truncate(0)

            f.write(content+'\n')

    def WriteContent(self, content, clearFile: bool = True, writeMode: WRITE_MODE = WRITE_MODE.WRITE, encoding: FILE_ENCODING = FILE_ENCODING.UTF_8):
        if self.isDirectory:
            return

        with open(self.fullPath, mode=FileHelper.GetWriteMode(writeMode), encoding=FileHelper.GetEncoding(encoding)) as f:
            if clearFile:
                f.truncate(0)

            f.write(content)

    def Delete(self):
        if self.isDirectory:
            return
        from os import remove
        remove(self.fullPath)

        del self


class FileHelper(Abstract):
    def Create(path: str):
        from os.path import exists

        if exists(path):
            return FileHelper.GetFileInfo(path)

        try:
            f = open(path, 'w')
            f.close()
            return FileHelper.GetFileInfo(path)
        except Exception:
            print(Exception)

    def GetFileInfo(file_path: str, isDirectory=False) -> File:
        from os import path

        if not path.exists(file_path):
            raise FileNotFoundError(f'File not found! path: {file_path}')

        file: File = File()

        name: str = path.basename(file_path)

        if not '.' in name:
            file.name = name
        else:
            fileData: List[str] = name.split('.')
            file.name = fileData[0]
            file.extension = '.'+fileData[1]

        file.directory = path.dirname(file_path)
        file.isDirectory = isDirectory
        file.fullPath = file_path
        file.fullName = name

        return file

    def GetReadMode(readMode: READ_MODE) -> str:
        match readMode:
            case READ_MODE.BINARY:
                return 'rb'
            case READ_MODE.DEFAULT:
                return 'r'

    def GetWriteMode(writeMode: WRITE_MODE) -> str:
        match writeMode:
            case WRITE_MODE.WRITE_BINARY:
                return 'wb'
            case WRITE_MODE.APPEND_BINARY:
                return 'ab'
            case WRITE_MODE.WRITE:
                return 'w'
            case WRITE_MODE.APPEND:
                return 'a'

    def GetEncoding(encoding: FILE_ENCODING) -> str:
        match encoding:
            case FILE_ENCODING.UTF_8:
                return 'utf-8'
            case FILE_ENCODING.UTF_16:
                return 'utf-16'
            case FILE_ENCODING.ASCII:
                return 'ascii'
            case FILE_ENCODING.ISO_8859_1:
                return 'iso-8859-1'
            case FILE_ENCODING.CP1252:
                return 'cp1252'
