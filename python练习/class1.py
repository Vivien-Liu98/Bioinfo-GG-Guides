class DietChoose:
    def __init__(self, howtaste, howmuch):  # 对象参数，第一个固定为self
        self.taste = howtaste  # 对象的属性
        self.price = howmuch
    def eaten(self, type):  # 定义对象的方法
        if self.price < 25 and self.taste == "好吃":  # 可调用前面的属性
            print(f"{type}...社畜优选！")
        else:
            print(f"{type}...都牛马了吃点好的...")
diet1 = DietChoose("好吃", 22)  # 之后调用类就可以创建对象
print(f"这道菜的味道是{diet1.taste}，价格是{diet1.price}")  # 查看对象属性值
diet1.eaten("猪肘饭")