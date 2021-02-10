import mysql.connector
from DB.DBLog import getLogger
from Settings import mariaDB_password, mariaDB_ID, mariaDB_IP

log = getLogger()

config = {
    'user': mariaDB_ID,
    'password': mariaDB_password,
    'host': mariaDB_IP,
    'database': 'ERBS_DB',
    'port': '5306'
}


def getConn():
    # ** 가변인자 전달 방법
    conn = mysql.connector.connect(**config)
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
