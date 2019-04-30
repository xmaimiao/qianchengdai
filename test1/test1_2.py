import random
class Human_Machine:
    def __init__(self):
        self.players={1:'张飞',2:'曹操',3:'刘备'}
        self.game_types={1:'剪刀',2:'石头',3:'布'}

    def choose_player(self):
        while True:
            p=int(input("请输入选择的游戏角色："))
            if p not in self.players.keys():
                print("请重新选择角色！")
                continue
            else:
                print("您选择的角色是：", self.players[p])
                break

    def hum_playgame(self):
        while True:
            hum=int(input("玩家请出拳："))
            if hum not in self.game_types.keys():
                print("请重新出拳！")
                continue
            else:
                hum_p = self.game_types[hum]
                print("玩家出拳：",hum_p)
                break
        return hum

    def mach_playgame(self):
        mach = random.randint(1,3)
        mach_p = self.game_types[mach]
        print("电脑出拳：",mach_p)
        return mach

    def fight(self,n=0,i=0,x=0):
        while True:
            hum = self.hum_playgame()
            mach = self.mach_playgame()
            if int(hum) - int(mach) in [-1,2]:
                n += 1
                print("电脑赢！")
            elif int(hum) - int(mach)in [-2,1]:
                i += 1
                print("玩家赢！")
            else:
                x += 1
                print("平局！")
            ch = input("是否退出游戏？（y/n）：")
            if ch == 'y':
                print("电脑赢了{}局，玩家赢了{}局，平了{}局！".format(n, i, x))
                break

if __name__ == '__main__':
    hm = Human_Machine()
    hm.choose_player()
    hm.fight()


# 电脑赢：
# 玩家：1、2、3  -1、2
# 电脑：2、3、1
# 玩家赢：
# 玩家：1、2、3  -2、1
# 电脑：3、1、2