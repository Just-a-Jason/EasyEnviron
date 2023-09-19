from Helpers.abstract_class import Abstract
from Environment import SPECIAL_FOLDER
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
                return 'C:\\Program Files\\'

    def GSF(special_folder: SPECIAL_FOLDER) -> str:
        '''
            Shortcut of GetSpecialFolder
        '''
        return ESV.GetSpecialFolder(special_folder)

    def GetFile(path: str) -> File:
        return FileHelper.GetFileInfo(path)

    def GFFSF(special_folder: SPECIAL_FOLDER, search: DIR_SEARCH = DIR_SEARCH.DEFAULT):
        return ESV.GetFilesFromSpecialFolder(special_folder=special_folder, search=search)

    def GetEnvironmentVariable(variable: str):
        return env['USERNAME']

    def GEV():
        pass
