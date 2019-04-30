#0226-python函數作業
import re
zw='[\u4e00-\u9fff]+'
sz='\d+'
yw='[a-zA-Z]+'
fh='[^\w\u4e00-\u9fff]+'
s=input("請輸入一段話：")
sw1=re.findall(zw,s,re.S)
sz2=re.findall(sz,s,re.S)
yw3=re.findall(yw,s,re.S)
fh4=re.findall(fh,s,re.S)
# re1=('、'.join(str(i) for i in sw1))
re1_1=('、'.join(sw1))
re1_2=('、'.join(sz2))
re1_3=('、'.join(yw3))
re1_4=(''.join(fh4))
# print("中文是：{}".format(re1))
print('''中文是：{}"
數字是：{}
英文是：{}
符號是：{}'''.format(re1_1,re1_2,re1_3,re1_4))

