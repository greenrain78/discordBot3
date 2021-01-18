from DB import manageDB
from Point.point_SQL import initMDB, initDB, tableName
from Log.infoLog import logger as log


def init():
    manageDB.init(initMDB, initDB)


def insert(user: str, point: int, reason: str, total: int):
    sql = f'insert into {tableName} ' \
          f'(user, point, reason, total) values(' \
          f'"{user}", {point}, "{reason}", {total})'
    manageDB.runSQL(sql)
    log.debug(f"{user} insert point{point}, total{total}, reason{reason} ")
