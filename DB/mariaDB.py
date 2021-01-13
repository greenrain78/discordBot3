import mysql.connector

config = {
    'user': 'greenrain',
    'password': 'Prosto1449@db',
    'host': '192.168.219.107',
    'database': 'discord_bot',
    'port': '5306'
}


def getConn():
    # ** 가변인자 전달 방법
    conn = mysql.connector.connect(**config)
    return conn


def runSQL(sql):
    conn = getConn()
    cur = conn.cursor()

    print("MDB run: ", sql)
    cur.execute(sql)

    conn.commit()
    conn.close()


def getSQL(sql):
    conn = getConn()
    cur = conn.cursor()

    # print("DB get run: ", sql)
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
