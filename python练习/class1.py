class DietChoose:
    def __init__(self, taste, howmuch): 
        self.taste = taste 
        self.price = howmuch
    def eaten(self, type):
        if self.price < 25 and self.taste == "好吃":
            print(f"{type}...社畜优选！")
        else:
            print(f"{type}...都牛马了吃点好的...")
diet1 = DietChoose("好吃", 22) 
print(f"这道菜的味道是{diet1.taste}，价格是{diet1.price}") 
diet1.eaten("猪肘饭")