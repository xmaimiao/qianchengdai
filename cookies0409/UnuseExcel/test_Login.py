import requests
import unittest
import json
from UnuseExcel.login_tests import Login_Test
from ddt import ddt,data,unpack

@ddt
class Test_Login(unittest.TestCase):

    url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
    unit = unittest.TestCase()

    @data(*Login_Test().tests)
    @unpack
    def test_login(self,data,expect):
        resp = requests.request('post', self.url, data=data)
        text = json.loads(resp.text)
        self.unit.assertEqual(expect,text['msg'])

