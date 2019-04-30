r=1
n=0
while r<4:
    sex=input("\nPlease input your sex(m/f):")
    age=int(input("Please input your age:"))
    if sex=='m':
        if age >=10 and age <= 12:
            print("Congratulations on joining the team!")
            n+=1
    r+=1
print("Number of eligible persons is "+ str(n))