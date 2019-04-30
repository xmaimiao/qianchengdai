import unittest
from UseExcel.common.do_Excel import Do_Excel
from UseExcel.common.requestHttp import RequestHttp
from ddt import ddt,data
from UseExcel.common import contants
from UseExcel.common import do_Mysql
from UseExcel.common.get_log import get_logger

logger = get_logger(__name__)

@ddt
class TestRegister(unittest.TestCase):                #注意ddt模式一定要放在類上運行，否則顯示找不到測試模塊
    '''測試註冊接口'''
    unit = unittest.TestCase()                                               #PermissionError錯誤一定是文件沒關閉
    do_excel = Do_Excel(contants.case_dir, 'register')
    cases = do_excel.read_excel()

    @classmethod                    #不定義為類方法 就會每次執行一次用例都調用此方法實例化對象，session就不同了，注意是setUpClass
    def setUpClass(cls):
        logger.info('準備測試前置')
        cls.r = RequestHttp()
        cls.mysql = do_Mysql.DoMysql()

    @data(*cases)
    def test_register(self,case):
        logger.info('開始測試：{}'.format(case.title))
        logger.debug('測試數據：{}'.format(case.data))
        # if case.data.find('register_mobile'):
        #     result = self.mysql.fetch_one('select max(mobilephone) from future.member')
        #     print(result)
        #     max_mobile = int(result[0])+1
        #     print(max_mobile)
        #     case.data = case.data.replace('register_mobile',str(max_mobile))
        #     print(case.data)

        resp =self.r.request(case.method,case.url,case.data)
        logger.debug('測試結果：{}'.format(resp.json()['msg']))
        try:
            self.unit.assertEqual(case.expectid,resp.text)
            self.do_excel.write_excel(case.id+1,resp.text,'PASS')
        except AssertionError as e:
            self.do_excel.write_excel(case.id+1,resp.text,'FALSE')
            logger.error('報錯了,{}'.format(e))
            raise e                  #沒有寫這個只會顯示用例執行次數，寫之後控制台顯示有誤信息
        logger.info('結束測試：{}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.info('測試後置處理')
        cls.r.close()
        cls.mysql.close()
