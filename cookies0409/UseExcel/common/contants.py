import os
# base_dir=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
base_dir=os.path.dirname(os.path.dirname(__file__))
print(base_dir)

case_dir=os.path.join(base_dir,'data','testcases.xlsx')
print(case_dir)

global_dir=os.path.join(base_dir,'config','global.cfg')
print(global_dir)

online_dir=os.path.join(base_dir,'config','online.cfg')

test_dir=os.path.join(base_dir,'config','test.cfg')     #注意這裡別寫錯，寫錯傳入的地址都不知道對不對 ，明天需要查一下join()
print(test_dir)

mysql_dir=os.path.join(base_dir,'config','mysql.cfg')

log_dir=os.path.join(base_dir,'log')

cases_dir=os.path.join(base_dir,'testcases')

report_dir=os.path.join(base_dir,'reports')