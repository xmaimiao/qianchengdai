import unittest
from UseExcel.common.do_Excel import Do_Excel
from UseExcel.common.requestHttp import RequestHttp
from ddt import ddt, data
from UseExcel.common import contants
from UseExcel.common import do_Mysql
from UseExcel.common.context import replace,Context
import time
from UseExcel.common.get_log import get_logger

logger = get_logger(__name__)

@ddt
class TestAdd(unittest.TestCase):
    '''測試添加標的'''
    unit = unittest.TestCase()                                               #PermissionError錯誤一定是文件沒關閉
    do_excel = Do_Excel(contants.case_dir, 'add')
    cases = do_excel.read_excel()

    @classmethod                                            #不定義為類方法 就會每次執行一次用例都調用此方法實例化對象，session就不同了，注意是setUpClass
    def setUpClass(cls):
        logger.info('準備測試前置')
        cls.r = RequestHttp()
        cls.mysql = do_Mysql.DoMysql()

    @data(*cases)
    def test_add(self,case):
        logger.info('開始測試：{}'.format(case.title))

        if case.data.find('project_name'):
            date = time.strftime('%Y-%m-%d %H_%M_%S')
            project_name = date + 'Project'
            case.data = case.data.replace('project_name',project_name)

        case.data = replace(case.data)  # 若存在寫在配置文件中的賬號和密碼、項目名，就必須通過replace函數去拿到正則表達式匹配的值
        logger.debug('測試數據：{}'.format(case.data))
        resp =self.r.request(case.method,case.url,case.data)
        code = resp.json()['code']                        #響應信息太多了，這裡需要取到其狀態碼進行斷言即可，.json()轉化為python語言下的str數據
        logger.debug('測試結果：{}'.format(resp.json()['msg']))

        try:
            self.unit.assertEqual(str(case.expectid),code )
            self.do_excel.write_excel(case.id+1,resp.text,'PASS')
        except AssertionError as e:
            self.do_excel.write_excel(case.id+1,resp.text,'FALSE')
            logger.error('報錯了,{}'.format(e))
            raise e                                            #沒有寫這個只會顯示用例執行次數，寫之後控制台顯示有誤信息
        logger.info('結束測試：{}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.info('測試後置處理')
        cls.r.close()
        cls.mysql.close()
