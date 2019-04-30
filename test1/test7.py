list=[1,2,3,4]
sum=[]
for i in list:
    for y in list:
        if i !=y:
            for x in list:
                if i != x and y != x:
                    sum.append(str(i)+str(y)+str(x))
                else:
                    continue
        else:
            continue
print(len(sum))

def student(*args):
    print(args)

student()


