import requests


class Recharge_Tests:
    def __init__(self):
        # 充值接口
        self.rechargr_url = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
        self.login_url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
        self.login_data = {'mobilephone': 18218813160, 'pwd': 123456, 'regname': None}
        self.session = requests.sessions.session()
        self.resp = self.session.request('post',self.login_url, data=self.login_data)
        self.tests = [
            {"data": {"mobilephone": 18218813160, "amount": 5000}, "expect": "充值成功"},
            {"data": {"mobilephone": 18218813160, "amount": 0}, "expect": "充值成功"},
            {"data": {"mobilephone": 18218813160, "amount": 50000000}, "expect": "充值成功"},
            {"data": {"mobilephone": 18218813161, "amount": 500}, "expect": "充值成功"}
        ]
