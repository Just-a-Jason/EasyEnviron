from Environment import SPECIAL_FOLDER, ENVIRONMENT_VARIABLE
from Helpers.abstract_class import Abstract
from Helpers.file import File, FileHelper
from dir_search import DIR_SEARCH
from os import environ as env
from typing import List


class ESV(Abstract):
    '''
        Easy Environ Class

        @Abstract
    '''
    def CreateFile(path) -> File:
        return FileHelper.Create(path)

    def SYSTEM(command: str) -> None:
        from os import system
        system(command)

    def GetSpecialFolder(special_folder: SPECIAL_FOLDER) -> str:
        if special_folder == SPECIAL_FOLDER.USER_PROFILE:
            return env['USERPROFILE']

        userProfile: str = ESV.GetSpecialFolder(
            SPECIAL_FOLDER.USER_PROFILE)

        match special_folder:
            case SPECIAL_FOLDER.DESKTOP:
                return userProfile + '\\Desktop\\'

            case SPECIAL_FOLDER.APP_DATA:
                return userProfile + '\\AppData\\'

            case SPECIAL_FOLDER.APP_DATA_LOCAL:
                return ESV.GetSpecialFolder(SPECIAL_FOLDER.APP_DATA) + 'Local\\'

            case SPECIAL_FOLDER.APP_DATA_LOCAL_LOW:
                return ESV.GetSpecialFolder(SPECIAL_FOLDER.APP_DATA) + 'LocalLow\\'

            case SPECIAL_FOLDER.APP_DATA_ROAMING:
                return ESV.GetSpecialFolder(SPECIAL_FOLDER.APP_DATA) + 'Roaming\\'

            case SPECIAL_FOLDER.DOWNLOADS:
                return userProfile + '\\Downloads\\'

            case SPECIAL_FOLDER.DOCUMENTS:
                return userProfile + '\\Documents\\'

            case SPECIAL_FOLDER.VIDEOS:
                return userProfile + '\\Videos\\'

            case SPECIAL_FOLDER.PICTURES:
                return userProfile + '\\Pictures\\'

            case SPECIAL_FOLDER.MUSIC:
                return userProfile + '\\Music\\'

            case SPECIAL_FOLDER.PROGRAM_FILES:
                return env['PROGRAMFILES'] + '\\'

            case SPECIAL_FOLDER.PROGRAM_FILES_X86:
                return env['PROGRAMFILES(X86)'] + '\\'

            case SPECIAL_FOLDER.WINDIR:
                return env['WINDIR']

    def GSF(special_folder: SPECIAL_FOLDER) -> str:
        '''
            Shortcut of GetSpecialFolder
        '''
        return ESV.GetSpecialFolder(special_folder)

    def GetFile(path: str) -> File:
        return FileHelper.GetFileInfo(path)

    def GetEnvironmentVariable(variable: str | ENVIRONMENT_VARIABLE) -> str:
        if type(variable) is ENVIRONMENT_VARIABLE:
            match variable:
                case ENVIRONMENT_VARIABLE.USER_NAME:
                    variable = 'USERNAME'
                case ENVIRONMENT_VARIABLE.SYSTEM_LANG:
                    variable = 'LANG'
                case ENVIRONMENT_VARIABLE.COMPUTER_NAME:
                    variable = 'COMPUTERNAME'
                case ENVIRONMENT_VARIABLE.SYSTEM_DRIVE:
                    variable = 'SYSTEMDRIVE'

        if variable in env.keys():
            return env[variable]
        else:
            raise KeyError(
                f'Variable "{variable} does not exists on this system"')

    def Exists(file: File | str) -> bool:
        from os import path

        if type(file) is File:
            return path.exists(file.fullPath)

        return path.exists(file)

    def GEV(variable: str | ENVIRONMENT_VARIABLE) -> str:
        return ESV.GetEnvironmentVariable(variable)

    def ReadDirectory(path: str | SPECIAL_FOLDER, search: DIR_SEARCH = DIR_SEARCH.DEFAULT) -> List[File]:
        from os import listdir

        if type(path) is SPECIAL_FOLDER:
            path = ESV.GetSpecialFolder(path)

        if not ESV.Exists(path):
            raise FileNotFoundError(f'Directory: {path}does not exist.')

        files: List[str] = listdir(path)

        from os.path import isfile

        if search == DIR_SEARCH.FILES_ONLY:
            files = [FileHelper.GetFileInfo(path+file)
                     for file in files if isfile(path+file)]

        elif search == DIR_SEARCH.DEFAULT:
            files = [FileHelper.GetFileInfo(
                path+file, not isfile(path+file)) for file in files]

        elif search == DIR_SEARCH.FOLDERS_ONLY:
            files = [FileHelper.GetFileInfo(path+file, True)
                     for file in files if not isfile(path+file)]

        return files

    def RD(path: str | SPECIAL_FOLDER, search: DIR_SEARCH = DIR_SEARCH.DEFAULT) -> List[File]:
        return ESV.ReadDirectory(path, search)
