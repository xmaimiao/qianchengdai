import smtplib
from setting import Setting
from email.mime.text import MIMEText  #設置郵件的格式
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import ssl

class Send_Email:
    set = Setting()
    context = ssl.create_default_context()
    total_msg = MIMEMultipart()
    #定義內容標題和來源，否則報錯554
    total_msg['Subject'] = '0331郵件測試'
    total_msg['To'] = 'mai@doocom.cn'
    total_msg['From'] = '18218813163@163.cn'
    #傳入文本模塊
    msg_new = """<p style = "color:blue">你好！</p>"""
    msg = MIMEText(msg_new, 'html', 'utf-8')
    total_msg.attach(msg)
    # 傳入附件模塊
    filedata = open('../unittest_case0321/filename.txt', 'rb').read()
    file = MIMEApplication(filedata)
    file.add_header('content-disposition', 'attachment', filename='filename.txt')
    total_msg.attach(file)

    def send_email(self):
        with smtplib.SMTP(self.set.smtpserver,25) as server:
            server.login(self.set.usename,self.set.password)
            server.starttls(context = self.context)  #這一步就出錯了
            server.sendmail(self.set.usename,self.set.receiver,self.total_msg.as_string())   #msg若作為參數導進來就會出現554錯誤，為什麼？

if __name__ == '__main__':
    Send_Email().send_email()