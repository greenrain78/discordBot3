from DB import manageDB
from Point.point_SQL import initMDB, initDB, tableName


def init():
    manageDB.init(initMDB, initDB)


def insert(user: str, point: int, reason: str, total: int):
    sql = f'insert into {tableName} ' \
          f'(user, point, reason, total) values(' \
          f'"{user}", {point}, "{reason}", {total})'
    manageDB.runSQL(sql)
    print(f"{user} insert point{point}, total{total}, reason{reason} ")
