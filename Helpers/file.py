from Helpers.abstract_class import Abstract
from typing import List


class File:
    extension: str = None
    name: str = None
    directory: str
    fullName: str
    fullpath: str

    def Read(self) -> str:
        with open(self.fullpath, mode='r') as f:
            return f.read()

    def WriteLine(self, content: str, clearFile=False) -> None:
        with open(self.fullpath, mode='a') as f:
            if clearFile:
                f.truncate(0)

            f.write(content+'\n')

    def Delete(self):
        from os import remove
        remove(self.fullpath)

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

    def GetFileInfo(file_path: str) -> File:
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
        file.fullpath = file_path
        file.fullName = name

        return file

    def ReadDir() -> List[str]:
        from os import listdir
