#python 之file文件操作
file=open('python_test15','w+',encoding='utf-8')
file.write('url:http://47.107.168.87:8080/futureloan/mvc/api/member/register@mobile:18688773467@pwd:123456')
# print(file.read())
a=file.read()
print(a)

