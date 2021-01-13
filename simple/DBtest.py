from DB import manageDB
from Point.point_SQL import tableName

# sql = f"select user from {tableName} group by user"
# sql = f"SELECT no, user, MAX(time) FROM {tableName} GROUP BY user"
# result = manageDB.getSQL(sql)
sql = f"select user from {tableName} group by user"
userList = manageDB.getSQL(sql)

result = [user[0] for user in userList]
print(result)
# for tmp in result:
#     print(tmp)
#
# print('-----------------------')
# sql = f"SELECT no, user, time " \
#       f"FROM {tableName} " \
#       f"WHERE time " \
#       f"IN (SELECT MAX(time) FROM {tableName} GROUP BY user)"
# result = manageDB.getSQL(sql)
# for tmp in result:
#     print(tmp)
