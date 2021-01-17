from typing import List

from DB import manageDB
from Point.user_SQL import initMDB, initDB, tableName


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
    result = manageDB.getSQL(sql)
    return result[0][0]


def insert_user(name: str, role: str, point: int, sleep: int):
    sql = f'insert into {tableName} ' \
          f'(name, role, point, sleep) values(' \
          f'"{name}", "{role}", {point}, {sleep})'
    manageDB.runSQL(sql)
    print(f"insert_user: {name}, role({role}), point({point}), sleep({sleep})")


def update_user_point(name: str, point: int):
    sql = f'UPDATE {tableName} ' \
          f'SET point = {point} ' \
          f'WHERE name = "{name}"'

    manageDB.runSQL(sql)
    print(f"update user({name}): point({point})")


def update_user_sleep(name: str, sleep: int):
    sql = f'UPDATE {tableName} ' \
          f'SET sleep = {sleep} ' \
          f'WHERE name = "{name}"'

    manageDB.runSQL(sql)
    print(f"update user({name}): sleep({sleep})")
