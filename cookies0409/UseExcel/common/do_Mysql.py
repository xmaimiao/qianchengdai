import pymysql
from configparser import ConfigParser
from UseExcel.common import contants

class DoMysql:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(contants.mysql_dir,encoding='utf-8')
        host =self.config.get('mysql','host')
        user = self.config.get('mysql','user')
        password =self.config.get('mysql','password')
        port = self.config.get('mysql','port')
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=int(port))  #port 從配置文件拿的值是str，所以注意做一個轉化
        #pymysql.cursors.DictCursor设置游标为返回字典模式
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)


    def fetch_one(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()

    def fetch_all(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.mysql.close()

# if __name__ == '__main__':
#     mysql = DoMysql()
#     try:
#         mysql.fetch_all('select * from future.loan limit 10')
#     except Exception as e:
#         print("sad!")
#         # raise e
#     finally:
#         mysql.close()

    # mysql = DoMysql().fetch_one('select max(mobilephone) from future.member')
    # print(mysql)