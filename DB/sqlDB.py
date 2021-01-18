import os
import sqlite3
from DB.DBLog import getLogger

log = getLogger()


def getConn():
    # 있으면 접속 없으면 생성
    path = os.path.join(os.getcwd(), "dbfile.db")
    conn = sqlite3.connect(path)
    return conn

def runSQL(sql):
    try:
        conn = getConn()
        cur = conn.cursor()

        cur.execute(sql)

        conn.commit()
        conn.close()
        log.info("run: %s", sql)
    except Exception as e:
        log.exception("run error: %s", sql)


def getSQL(sql):
    try:
        conn = getConn()
        cur = conn.cursor()

        cur.execute(sql)
        result = cur.fetchall()

        conn.commit()
        conn.close()

        log.info("get: %s \n \t %s", sql, result)
        return result
    except Exception as e:
        log.exception("get error: %s", sql)


def getOneSQL(sql):
    try:
        conn = getConn()
        cur = conn.cursor()

        cur.execute(sql)
        result = cur.fetchone()

        conn.commit()
        conn.close()
        log.info("get: %s \n \t %s", sql, result)
        return result
    except Exception as e:
        log.exception("get error: %s", sql)
