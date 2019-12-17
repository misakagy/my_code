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
        self.conn.commit()

    # 按照传入参数指定查找前day天的数据
    def select_day_data(self, day):
        sql = "select *from my_work where time between datetime('now','-%d day') and datetime('now', '+1 day')" % (day)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    ############################以下接口为调试使用##########################
    def execute_sql(self, sql):
        print(sql)
        self.cursor.execute(sql)

    def fetchall_print(self):
        print(self.cursor.fetchall())


def summary_print(summary_list):
    temp = {}
    for work in summary_list:
        ret = temp.get(work[1], False)
        if ret == False:
            temp[work[1]] = work[2]
        else:
            temp[work[1]] = temp[work[1]] + ' ' + work[2]
    for key in temp:
        output = '[%s]\n' % (key)
        for i in temp[key]:
            
        print(output)

def collect_input():
    data = []
    while True:
        work = input('输入工作内容：z-退出\n')
        if work == 'z':
            print(data)
            return data
        work = work.split()
        if len(work) == 2:
            data.append(work)
        
if __name__ == '__main__':
    my_work = my_db(DB_NAME)
    # 按格式打印前7天数据
    print('最近7天工作情况：')
    for work in my_work.select_day_data(7):
        output = '[%s] -- [%s] : %s' % (work[3], work[1], work[2])
        print(output)
    
    while(True):
        user_input = input('输入命令执行相关操作：q-查询30天数据，w-查询7天数据，e-录入模式，z-退出\n')
        if user_input == 'q':
            summary_print(my_work.select_day_data(7))                
        elif user_input == 'w':
            summary_print(my_work.select_day_data(30))       
        elif user_input == 'e':
            ret = collect_input()
            for one in ret:
                my_work.insert_data(one[0], one[1])
            print('insert data ok')
        elif user_input == 'z':
            break

