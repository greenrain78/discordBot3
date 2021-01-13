import os
import sqlite3


def getConn():
    # 있으면 접속 없으면 생성
    path = os.path.join(os.getcwd(), "dbfile.db")
    conn = sqlite3.connect(path)
    return conn


def runSQL(sql):
    conn = getConn()
    cur = conn.cursor()

    print("DB run: ", sql)
    cur.execute(sql)

    conn.commit()
    conn.close()


def getSQL(sql):
    conn = getConn()
    cur = conn.cursor()

    print("DB get run: ", sql)
    cur.execute(sql)
    result = cur.fetchall()

    conn.commit()
    conn.close()
    return result


def getOneSQL(sql):
    conn = getConn()
    cur = conn.cursor()

    print("DB get one run: ", sql)
    cur.execute(sql)
    result = cur.fetchone()

    conn.commit()
    conn.close()
    return result
