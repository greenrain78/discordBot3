from DB import mariaDB, sqlDB
from Settings import  on_MariaDB, on_sqlDB


def init(initMDB, initDB):
    if on_MariaDB:
        mariaDB.runSQL(initMDB)

    if on_sqlDB:
        sqlDB.runSQL(initDB)  # 도커 오류로 일시정지


def runSQL(sql):
    if on_MariaDB:
        mariaDB.runSQL(sql)

    if on_sqlDB:
        sqlDB.runSQL(sql)  # 도커 오류로 일시정지


def getSQL(sql):
    if on_MariaDB:
        result = mariaDB.getSQL(sql)

    if on_sqlDB:
        result = sqlDB.getSQL(sql)  # 도커 오류로 일시정지

    return result


def getOneSQL(sql):
    if on_MariaDB:
        result = mariaDB.getOneSQL(sql)

    if on_sqlDB:
        result = sqlDB.getOneSQL(sql)  # 도커 오류로 일시정지

    return result
