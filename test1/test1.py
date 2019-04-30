import random
players={'1':'曹操','2':'張飛','3':'劉備'}
hands=['剪刀','石頭','布']
player_hands=[]
mach_hands=[]

polling_active=True
n=0
r=0
x=0
f=0
key=input("Please choose player,input the number(1:曹操,2:張飛,3:劉備):")
player_name=players[key]
while polling_active:
    q=int(input("\nPlease play the game(1:剪刀,2:石頭,3:布):"))
    player_hands.append(hands[q-1])
    mach=random.randint(1,3)
    mach_hands.append(hands[mach-1])

    repeat = input("Would you want to continue the game?(y/n):")
    if repeat == 'n':
        polling_active= False


for hand1 in player_hands:
    if hand1 =='剪刀':
        print(0)
        if hand1 != mach_hands[n] and mach_hands[n]=='石頭':
            x+=1
        elif hand1 != mach_hands[n] and mach_hands[n]=='布':
            r+=1
        else:
            f+=1
    # print(x,r,f)

    elif hand1 =='石頭':
        if hand1 != mach_hands[n] and mach_hands[n]=='布':
            x+=1
        elif hand1 != mach_hands[n] and mach_hands[n]=='剪刀':
            r+=1
        else:
            f+=1

    else :
        if hand1 != mach_hands[n] and mach_hands[n]=='剪刀':
            x+=1
        elif hand1 != mach_hands[n] and mach_hands[n]=='石頭':
            r+=1
        else:
            f += 1
    n+=1


print(player_hands)
print(mach_hands)
print(player_name.title() + ' 贏了 ' + str(r) +' 局，'+
      '電腦贏了 '+ str(x) + ' 局，'+
      '平局 '+ str(f) + ' .')