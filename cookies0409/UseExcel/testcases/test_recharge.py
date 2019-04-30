import unittest
from UseExcel.common.do_Excel import Do_Excel
from UseExcel.common.requestHttp import RequestHttp
from ddt import ddt, data
from UseExcel.common import contants
from UseExcel.common import do_Mysql
from UseExcel.common.context import replace
from UseExcel.common.config import Config
from UseExcel.common.get_log import get_logger

logger = get_logger(__name__)
@ddt
class TestRecharge(unittest.TestCase):                     #注意ddt模式一定要放在類上運行，否則顯示找不到測試模塊
    '''測試充值接口'''
    unit = unittest.TestCase()                                               #PermissionError錯誤一定是文件沒關閉
    do_excel = Do_Excel(contants.case_dir, 'test')
    cases =do_excel.read_excel()
    sql = Config().get('data', 'sql_normal_id')

    @classmethod                                            #不定義為類方法 就會每次執行一次用例都調用此方法實例化對象，session就不同了，注意是setUpClass
    def setUpClass(cls):
        logger.info('準備測試前置')
        cls.r = RequestHttp()
        cls.mysql = do_Mysql.DoMysql()

    @data(*cases)
    def test_recharge(self,case):
        logger.info('開始測試：{}'.format(case.title))
        #查询充值前的账户余额
        money_be = self.mysql.fetch_one(self.sql)
        before_amount = money_be['leaveamount']
        logger.debug('充值前投资人的账户余额为：{}'.format(before_amount))

        case.data = replace(case.data)                         #若存在寫在配置文件中的賬號和密碼，就必須通過replace函數去拿到正則表達式匹配的值
        resp =self.r.request(case.method,case.url,case.data)
        code = resp.json()['code']                        #響應信息太多了，這裡需要取到其狀態碼進行斷言即可，.json()轉化為python語言下的str數據
        logger.debug('结果信息：{}'.format(resp.json()['msg']))
        try:
            self.unit.assertEqual(str(case.expectid),code )
            self.do_excel.write_excel(case.id+1,resp.text,'PASS')

            if resp.json()['msg'] == '充值成功':
            # 查询充值后的账户余额，并校验数据库数据
                money_af = self.mysql.fetch_one(self.sql)
                after_amount = money_af['leaveamount']
                logger.debug('充值后投资人的账户余额为：{}'.format(after_amount))
                self.assertEqual(float(before_amount)+float(eval(case.data)['amount']), float(after_amount))

        except AssertionError as e:
            self.do_excel.write_excel(case.id+1,resp.text,'FAIL')
            logger.error('報錯了,{}'.format(e))
            raise e                                            #沒有寫這個只會顯示用例執行次數，寫之後控制台顯示有誤信息
        logger.info('結束測試：{}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.info('測試後置處理')
        cls.r.close()
        cls.mysql.close()
