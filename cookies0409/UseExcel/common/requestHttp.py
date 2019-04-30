import requests
from UseExcel.common.config import config
from UseExcel.common.get_log import get_logger

logger = get_logger(__name__)
class RequestHttp:

    def __init__(self):
        self.session = requests.sessions.session()
        self.config = config.get('api','pre_url')

    def request(self,method=None,url=None,data=None,json=None):

        if type(data) == str:  #這裡記得直接判斷是不是str，'str'必跪，參數壓根穿不進去！！
            data = eval(data)

        url= self.config + url  #拼接URL

        method = method.lower()

        if method == 'get':
            resp = self.session.request(method,url,params=data)
        elif method == 'post':
            if json :
                resp = self.session.request(method, url, json=data)
            else:
                resp = self.session.request(method,url,data=data)
        else:
            resp = None                         #不傳入URL時resp為空
            logger.error("請求response:{}".format(resp.text))
        return resp

    def close(self):
        self.session.close()

# if __name__ == '__main__':
#     url='http://test.lemonban.com/futureloan/mvc/api/member/login'
#     data={'mobilephone': 18218813160, 'pwd': 123456,'regname':None}
#     resp=RequestHttp()  #注意這裡要統一實例化類，分開實例化表示使用不同的session，充值時會顯示“先登錄”
#     resp1=resp.request('post',url,data)
#     print(resp1.text)
#     url='http://test.lemonban.com/futureloan/mvc/api/member/recharge'
#     data={"mobilephone": 18218813160, "amount": 5000}
#     resp2=resp.request('post',url, data)
#     text=json.loads(resp2.text)
#     print(resp2.text)
#     RequestHttp().close()
#     if text['msg']== '充值成功':
#         print("good!")
