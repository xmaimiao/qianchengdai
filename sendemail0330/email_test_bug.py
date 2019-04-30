#coding=utf-8
import smtplib
from setting import Setting

#1.設置郵件發送商
#2.登錄
#3.發送郵件

# class Send_Email:
#     def __init__(self,msg):
#         self.msg=msg
#         self.set = Setting()
#
#     def s_email(self):
#         with smtplib.SMTP('smtp.163.com',25) as server:
#             server.login(self.set.usename,self.set.password)
#             server.sendmail(self.set.usename,self.set.receiver,self.msg)
#
# if __name__ == '__main__':
#     msg = '''\\
#     From: 18218813163@163.com
#     Subject: second...
#
#     Hello '''
#     Send_Email(msg).s_email()
#

#
set = Setting()
server = smtplib.SMTP('smtp.163.com',25)
server.login(set.usename,set.password)
msg = '''\\
From: 18218813163@163.com
Subject: Python email test

你好！  '''
server.sendmail('18218813163@163.com','mai@doocom.cn',msg.encode())
server.quit()

# def send():
#
#     server = smtplib.SMTP('smtp.163.com', 25)
#     server.login('18218813163@163.com', 'xmm18218813163')
#     msg = '''\\
#     From: 18218813163@163.com
#     Subject: first
#
#     hello  '''
#     server.sendmail('18218813163@163.com', 'mai@doocom.cn', msg.encode())
#     server.quit()
#
# send()
