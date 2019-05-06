import sys             #必須要在第一行!!
sys.path.append('./')
print(sys.path)
import unittest
from UseExcel.common import contants
import time
import HTMLTestRunnerNew

suite = unittest.TestSuite()
loader = unittest.TestLoader()
discover = unittest.defaultTestLoader.discover(contants.cases_dir,'test_*.py')

result = time.strftime('%Y-%m-%d %H_%M_%S')
result1 = contants.report_dir + '/' + result + 'report.html'    #別忘了“/”
with open(result1,'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title="PYTHON API TEST RESULT",
                                              description="前程貸",
                                              tester="mai")
    runner.run(discover)