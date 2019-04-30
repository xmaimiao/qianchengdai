import requests
import unittest
import json
from ddt import ddt,data,unpack
from read_excel import Read_Excel

@ddt
class Requests_Case(unittest.TestCase):
    '''驗證登錄是否正常'''
    url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'

    @data(*Read_Excel().readdata())
    @unpack
    def test_001(self,params,expect,code_id):
        '''验证登录成功'''
        resp = requests.get(self.url,params=eval(params))
        text = json.loads(resp.text)
        print(text)
        # expect = '登录成功'
        unit = unittest.TestCase()
        # try:
        #     '''用try來手機驗證異常，故控制台默認為：用例通過了'''
        #     unit.assertEqual(expect,text['msg'])
        # except AssertionError as e:
        #     Read_Excel().writedata(int(code_id), 'failed')
        unit.assertEqual(expect, text['msg'])


    # def test_002(self):
    #     '''验证登录不成功,提示：用户名或密码错误'''
    #     params = {'mobilephone':'18688773467','pwd':'1234567'}
    #     resp = requests.get(self.url,params=params)
    #     text = json.loads(resp.text)
    #     print(text)
    #     expect = '用户名或密码错误'
    #     unit = unittest.TestCase()
    #     unit.assertEqual(expect,text['msg'])
    #
    # def test_003(self):
    #     '''验证登录不成功,不输入密码，提示：用户名或密码不能为空'''
    #     params = {'mobilephone': '18688773467', 'pwd': None}
    #     resp = requests.get(self.url, params=params)
    #     text = json.loads(resp.text)
    #     print(text)
    #     expect = '用户名或密码不能为空'
    #     unit = unittest.TestCase()
    #     unit.assertEqual(expect, text['msg'])
    #
    # def test_004(self):
    #     '''验证登录不成功,不输入用户名，提示：用户名或密码不能为空'''
    #     params = {'mobilephone': None, 'pwd': 123456}
    #     resp = requests.get(self.url, params=params)
    #     text = json.loads(resp.text)
    #     print(text)
    #     expect = '用户名或密码不能为空'
    #     unit = unittest.TestCase()
    #     unit.assertEqual(expect, text['msg'])