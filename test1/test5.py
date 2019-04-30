# i=input("please input the numbers:")
# print(type(i))
# year=i[0:4]
# month=i[4:6]
# day=i[6:9]
# print("{}年{}月{}日".format(year,month,day))

# d={'arg':20,'name':'七月'}
# print(type(d.values()))
#
# a=10
# b=0
# print(a or b)
#
# s=''
# print(len(s))
# s={1:1}
# print(len(s))
# print(type(s))

s=[2,34,6,90,5,100,89]
for a in range(len(s)-1):
    '''下面的for循環作用是完成每一次相鄰兩個數據的比較并完成數值的交換'''
    for b in range(len(s)-1-a):
        if s[b] > s[b+1]:
            num=s[b]     #s[b],s[b+1]=s[b+1],s[b] python支持這樣的賦值方法
            s[b]=s[b+1]
            s[b+1]=num
        else:
            continue
print(s)

