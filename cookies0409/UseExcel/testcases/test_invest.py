import unittest
from UseExcel.common.do_Excel import Do_Excel
from UseExcel.common.requestHttp import RequestHttp
from ddt import ddt, data
from UseExcel.common import contants
from UseExcel.common import do_Mysql
from UseExcel.common.context import replace,Context
from UseExcel.common.config import Config
import time
from UseExcel.common.get_log import get_logger

logger = get_logger(__name__)

@ddt
class TestInvest(unittest.TestCase):
    '''測試投資'''
    unit = unittest.TestCase()                                               #PermissionError錯誤一定是文件沒關閉
    do_excel = Do_Excel(contants.case_dir, 'invest')
    cases = do_excel.read_excel()
    # sql_normal = Config().get('data', 'sql_normal')
    # sql_borrow = Config().get('data', 'sql_borrow')
    sql_loan_id =  Config().get('data','sql_loan_id')


    @classmethod                                            #不定義為類方法 就會每次執行一次用例都調用此方法實例化對象，session就不同了，注意是setUpClass
    def setUpClass(cls):
        logger.info('準備測試前置')
        cls.r = RequestHttp()
        cls.mysql = do_Mysql.DoMysql()

    @data(*cases)
    def test_invest(self,case):
        logger.info('開始測試：{}'.format(case.title))
        # 判断投资人投资前标的为多少
        if case.sql is not None:
            money_be = self.mysql.fetch_one(case.sql)
            before_amount = money_be['leaveamount']
            logger.debug('投资前投资人的账户余额为：{}'.format(before_amount))

        # if case.data.find('member_loan_id'):
        #     member_loan_id = self.mysql.fetch_one(self.sql_borrow)
        #     print('借款人ID：',member_loan_id['id'])
        #     if hasattr(Context,'member_loan_id'):
        #         setattr(Context,'member_loan_id',member_loan_id['id'])

        # if case.data.find('normal_user_id'):
        #     normal_user_id = self.mysql.fetch_one(self.sql_normal)
        #     print('投资人ID：', normal_user_id['id'])
        #     if hasattr(Context, 'normal_user_id'):
        #         setattr(Context, 'normal_user_id', normal_user_id['id'])

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
            if resp.json()['msg'] =='加标成功':
                logger.debug('取到的sql語句：{}'.format(case.sql))
                loan_id = self.mysql.fetch_one(self.sql_loan_id)
                print(loan_id)
                loan_id = int(loan_id['max(id)'])
                logger.debug('標的ID：{}'.format(loan_id))
                #把取到的标的id加到类中
                setattr(Context,'loan_id',str(loan_id))

            # 判断投资人投资后标的为多少
            if case.sql is not None:
                money_af = self.mysql.fetch_one(case.sql)
                after_amount = money_af['leaveamount']
                logger.debug('投资后投资人的账户余额为：{}'.format(after_amount))             #为什么判断case.sql is not None的时候断言有误才答打印出来？？？
                self.unit.assertEqual(float(before_amount)-float(eval(case.data)['amount']), float(after_amount))

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
