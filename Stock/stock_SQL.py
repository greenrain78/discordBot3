initMDB = f"CREATE TABLE IF NOT EXISTS {tableName}(" \
          f"no      INT NOT NULL AUTO_INCREMENT PRIMARY KEY," \
          f"user    VARCHAR(255) NOT NULL," \
          f"point   INT     NOT NULL," \
          f"reason  TEXT    NOT NULL," \
          f"time  datetime  NOT NULL DEFAULT CURRENT_TIMESTAMP," \
          f"total   INT     NOT NULL" \
          f");" \

initDB = f"CREATE TABLE IF NOT EXISTS {tableName}(" \
         f"no      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT," \
         f"user    VARCHAR(255) NOT NULL," \
         f"point   INT     NOT NULL," \
         f"reason  TEXT    NOT NULL," \
         f"time  datetime  NOT NULL DEFAULT CURRENT_TIMESTAMP," \
         f"total   INT     NOT NULL" \
         f");" \
