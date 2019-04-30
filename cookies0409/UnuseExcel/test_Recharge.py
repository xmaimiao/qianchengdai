from UnuseExcel.recharge_tests import Recharge_Tests
import unittest
import json
from ddt import ddt,data,unpack

# @ddt
# class Test_Recharge(unittest.TestCase):
#     '''以下方法是用了第一種方法，傳入cookie模式'''
#     set = Recharge_Tests()
#     url = set.rechargr_url
#     resp = set.resp
#     unit = unittest.TestCase()
#
#     @data(*Recharge_Tests().tests)
#     @unpack
#     def test_recharge(self,data,expect):
#         resp=requests.request('post',self.url,data=data,cookies=self.resp.cookies)
#         text=json.loads(resp.text)
#         self.unit.assertEqual(expect,text['msg'])

@ddt
class Test_Recharge(unittest.TestCase):
    '''以下方法是用了第二種方法，不傳入cookie'''
    set = Recharge_Tests()
    url = set.rechargr_url
    session =set.session
    resp = set.resp
    unit = unittest.TestCase()

    @data(*Recharge_Tests().tests)
    @unpack
    def test_recharge(self,data,expect):
        resp=self.session.request('post',self.url,data=data)
        text=json.loads(resp.text)
        self.unit.assertEqual(expect,text['msg'])



