import unittest
import requests_case
import HTMLTestRunnerNew
import time

suite = unittest.TestSuite()

loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(requests_case))
#按照一定格式獲取當前時間
now = time.strftime('%Y-%m-%d %H_%M_%S')
#定義報告存放路徑
filename = './'+now+'result.html'

with open(filename,'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream = file,verbosity = 2,title='0329測試報告',description='有關HTML的requests請求',tester='mai')
    runner.run(suite)