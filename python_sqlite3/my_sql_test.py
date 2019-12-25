import sqlite3

DB_NAME = 'gongyi.db'

class my_db():
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    
    def __del__(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    ############################以下接口为调试使用##########################
    def execute_sql(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
        print(self.cursor.fetchall())

db_test = my_db(DB_NAME)

while True:
    sql = input('请输入sql语句：')
    if sql == 'z':
        break
    try:
        db_test.execute_sql(sql)
    except Exception as e:
        print(e)



