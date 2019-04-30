import random
class Human_Machine:
    def __init__(self):
        self.players={1:'张飞',2:'曹操',3:'刘备'}
        self.game_types={1:'剪刀',2:'石头',3:'布'}
        self.n = 0
        self.i = 0
        self.x = 0


    def choose_player(self):
        p=int(input("请输入选择的游戏角色："))
        return self.players[p]

    def hum_playgame(self):
        hum=int(input("玩家请出拳："))
        hum_p = self.game_types[hum]
        print("玩家出拳：",hum_p)
        return hum

    def mach_playgame(self):
        mach = random.randint(1,3)
        mach_p = self.game_types[mach]
        print("电脑出拳：",mach_p)
        return mach

    def fight(self,hum,mach):

        if int(hum) - int(mach) in [-1,2]:
            self.n += 1
            print("电脑赢！")
        elif int(hum) - int(mach)in [-2,1]:
            self.i += 1
            print("玩家赢！")
        else:
            self.x += 1
            print("平局！")

        return self.n,self.i,self.x

if __name__ == '__main__':
    hm = Human_Machine()
    print("您选择的角色是：",hm.choose_player())
    while True:
        hum_p = hm.hum_playgame()
        mach_p = hm.mach_playgame()
        result = hm.fight(hum_p,mach_p)
        print(result)
        ch = input("是否退出游戏？（y/n）：")
        if ch == 'y':
            print("电脑赢了{}局，玩家赢了{}局，平了{}局！".format(result[0], result[1], result[2]))
            break

# 电脑赢：
# 玩家：1、2、3  -1、2
# 电脑：2、3、1
# 玩家赢：
# 玩家：1、2、3  -2、1
# 电脑：3、1、2