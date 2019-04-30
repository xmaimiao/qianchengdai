import requests
class Request_test:
    def __init__(self,url,params):
        self.url =url
        self.params = params
    def http_request(self,method):
        if method.lower() == 'post':
            Resp = requests.request(method.lower(),self.url,data=self.params)
        else:
            Resp=requests.request(method.lower(),self.url,params=self.params)
        return Resp

    def request_status_code(self,method):
        resp = self.http_request(method)
        return resp.status_code

if __name__ == '__main__':
    url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    # params = {'mobilephone':18688773467 , 'pwd': 123456}
    # params = {'mobilephone':None , 'pwd': 123456}
    params = {'mobilephone': 18688773467, 'pwd': None}
    r=Request_test(url,params)
    resp=r.http_request('get')
    print(resp.reason)
    print(resp.text)
    # print(resp.content)
    # print(resp.reason)
    # print(resp.headers)
    # print(resp.request)
    # print(resp.url)
    # print(resp.apparent_encoding)
    # print(resp.ok)
    # print(resp.status_code)

