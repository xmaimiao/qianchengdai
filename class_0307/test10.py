class Restaurant:
    def __init__(self):
        self.retaurant_name='好運來餐廳'
        self.favorite_food='玫瑰鼓油雞'
        self.cooking_type=['酸筍炒肉','小炒包菜','糖醋排骨','乾鍋牛肉','農家肉']

    def describr_restaurant(self):
        print("這家餐館的名字是:{}".format(self.retaurant_name))
        print("他們最受歡迎的食物是：{}".format(self.favorite_food))

    def open_restautrant(self):
        print("這家餐館目前的營業時間是：8:00-23:00")

    def customer_order(self):
        self.orders=[]
        print("我們上次去吃點了（按y结束）：")
        while True:
            num=input()
            if num =='y':
                break
            else:
                self.orders.append(num)
        return self.orders




t=Restaurant()
print(t.retaurant_name)
print(t.cooking_type)
t.describr_restaurant()
t.open_restautrant()