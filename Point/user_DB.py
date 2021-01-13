from typing import List

from DB import manageDB
from Point.point_SQL import initMDB, initDB, tableName


def init():
    manageDB.init(initMDB, initDB)


def get_sleepList() -> List[tuple]:
    sql = f"select name, sleep from {tableName}"
    result = manageDB.getSQL(sql)
    return result


def get_pointList() -> List[tuple]:
    sql = f"select name, point from {tableName}"
    result = manageDB.getSQL(sql)
    return result


def get_point(user: str) -> int:
    sql = f'select point from {tableName} ' \
          f'WHERE name = "{user}"'
    result = manageDB.getSQL(sql)  # 정상 동작 확인후 변경
    return result

def insert_user(name: str, role: str, point: int, sleep: int)