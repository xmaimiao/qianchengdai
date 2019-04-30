class Login_Test:
    def __init__(self):
        self.url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
        self.tests=[
            {"data":{'mobilephone': 18218813160, 'pwd': 123456,'regname':None},"expect":"登录成功"},
            {"data":{'mobilephone': 1821881316, 'pwd': 123456,'regname':None},"expect":"用户名或密码错误"},
            {"data":{'mobilephone': 182188131602, 'pwd': 123456,'regname':None},"expect":"用户名或密码错误"},
            {"data":{'mobilephone': 18218813160, 'pwd': 12345,'regname':None},"expect":"用户名或密码错误"},
            {"data":{'mobilephone': 18218813160, 'pwd': 1234561,'regname':None},"expect":"用户名或密码错误"},
            {"data":{'mobilephone': None, 'pwd': 123456,'regname':None},"expect":"手机号不能为空"},
            {"data":{'mobilephone': 18218813160, 'pwd': None,'regname':None},"expect":"用户名或密码错误"},
        ]