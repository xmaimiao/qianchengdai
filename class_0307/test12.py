from test10 import Restaurant
class Restaurant1(Restaurant):
    def discount(self,num=1):
        self.num=num
        self.orders=self.customer_order()
        for order in self.orders:
            if order in self.cooking_type:
                self.num+=1
        if self.num>=2:
            print("你好，订单中超過兩份以上的特惠菜，我們給打7折哦！")
        else:
            print("你好，订单中没有特惠菜，故不参与打折哦！")

    def pay_money(self):
        if self.num>=2:
            print("最终的价格是：",int(len(self.orders)*14*0.7))
        else:
            print("最终的价格是：",int(len(self.orders)*14))

if __name__ == '__main__':
    r=Restaurant1()
    r.discount()
    r.pay_money()