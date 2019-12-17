import sqlite3
import datetime
import os

DB_NAME = 'gongyi.db'

class my_db():
    def __init__(self, db_name):
        # 查找是否存在数据库
        exist = False
        for file in os.listdir(os.getcwd()):
            if file == db_name:
                exist = True
        
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        if exist == False:
            print('sql is not create, create now !!')
            self.create_table()
    
    def __del__(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def create_table(self):
        self.cursor.execute('''
        create table my_work
        (num integer primary key autoincrement, 
        work uvarchar(100), 
        summary uvarchar(200), 
        time timestamp not null default (datetime('now','localtime')))
        ''')
        print('create my_work table')
    
    def insert_data(self, work, summary, *arg):
        print(work, summary, arg)
        sql = "insert into my_work(num, work, summary) values(null, '%s', '%s')" 
        sql = sql % (work, summary)
        self.cursor.execute(sql)

    # 按照传入参数指定查找前day天的数据
    def select_day_data(self, day):
        sql = "select *from my_work where time between datetime('now','-%d day') and datetime('now')" % (day)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def execute_sql(self, sql):
        print(sql)
        self.cursor.execute(sql)

    def fetchall_print(self):
        print(self.cursor.fetchall())



if __name__ == '__main__':
    my_work = my_db(DB_NAME)
    # 按格式打印前7天数据
    for work in my_work.select_day_data(7):
        output = '[%s] -- [%s] : %s' % (work[3], work[1], work[2])
        print(output)

    while(True):
        user_input = input('输入命令执行相关操作：q-查询30天数据，w-查询7天数据，e-录入模式')
        print('test')
        if user_input == 'q':
            print(user_input)
            pass
        elif user_input == 'w':
            pass
        elif user_input == 'e':
            pass

     







