from Settings import debug

if not debug:
    tableName = 'discord_user'
else:
    tableName = 'discord_user_test'


initMDB = f'CREATE TABLE IF NOT EXISTS {tableName}(' \
          f'no      INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ' \
          f'name    VARCHAR(255) NOT NULL, ' \
          f'role    VARCHAR(255) NOT NULL, ' \
          f'join_time  datetime  NOT NULL DEFAULT CURRENT_TIMESTAMP, ' \
          f'point   INT     NOT NULL, ' \
          f'sleep   INT     NOT NULL' \
          f');'

initDB = f'CREATE TABLE IF NOT EXISTS {tableName}(' \
         f'no      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' \
         f'name    VARCHAR(255) NOT NULL,' \
         f'role    VARCHAR(255) NOT NULL,' \
         f'join_time  datetime  NOT NULL DEFAULT CURRENT_TIMESTAMP,' \
         f'point   INT     NOT NULL' \
         f');'
