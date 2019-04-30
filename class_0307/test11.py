class User:
    def __init__(self):
        self.first_name='邢'
        self.last_name='麥苗'
        self.sex='女'
        self.age=25

    def describe_user(self):
        print('''深夜主播：今天要介紹的人物姓名是：{}，是個可愛的{}孩子，今年已經{}歲了，但是還是單身汪一隻，歡迎廣大男性朋友聯繫！'''.format(self.first_name+self.last_name,self.sex,self.age))

    def greet_user(self,content):
        self.content=content
        print("那麼我們來聽一聽這位女士要跟大家說什麼呢：{}".format(self.content))

t=User()
t.describe_user()
s=input("來賓跟大家打招呼的話：")
t.greet_user(s)