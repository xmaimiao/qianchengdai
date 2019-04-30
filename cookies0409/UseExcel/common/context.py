import re
from UseExcel.common.config import config
import configparser
from UseExcel.common.do_Mysql import DoMysql

class Context:
    # member_loan_id = None
    # normal_user_id = None
    loan_id = None

def replace(data):
    p='#(.*?)#'
    while re.search(p,data):
        data_new = re.search(p,data).group(1)
        try:
            if 'sql' in data_new:
                sql = config.get('data',data_new)   #根據文件取配置文件裡面的值
                da = DoMysql().fetch_one(sql)
                da = str(da['id'])                   #從數據庫取出來的id是int
            else:
                da = config.get('data', data_new)
        except configparser.NoOptionError as e:
            if hasattr(Context,data_new):
                da = str(getattr(Context,data_new))
            else:
                print("找不到参数信息！")
                raise e
        data = re.sub(p,da,data,count=1)  #查找替換，count查找替換的次數
    return data

if __name__ == '__main__':
    get = getattr(Context,'loan_id')
    print(get)