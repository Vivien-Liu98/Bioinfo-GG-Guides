class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.what = "能吃" 
    def eaten(self): 
        print(f"要吃{self.name}吗？")
class ZhongCan(Food): 
    def exp_z(self):
        print(f"{self.name}是中餐。")
class XiCan(Food):
    def __init__(self,name,price,taste) :
        super().__init__(name, price) 
        self.taste = taste
    def exp_x(self):
        if self.taste == "好吃":
            print(f"{self.name}是好吃的西餐。")
        else:
            print(f"{self.name}...嗯...")

zhong1 = ZhongCan("烧鸭饭",21)
zhong1.eaten() 
zhong1.exp_z()
xi1 = XiCan("牛排",45,"好吃")
xi1.exp_x()