import sqlite3

# 连接数据库
conn = sqlite3.connect('gongyi.db')
cursor = conn.cursor()

print('hello world')
# 关闭数据库
cursor.close()
conn.commit()
conn.close()
