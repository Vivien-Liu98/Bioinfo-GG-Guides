try:
    x1 = float(input("输入被除数:"))
    x2 = float(input("输入除数:"))
    y = x1 / x2
except ValueError: 
    print("老大这个好像不能算喵...")
except ZeroDivisionError: 
    print("老大这个好像不能除喵...")
except: 
    print("老大不知道发生什么了总之行不通喵...")
else: 
    print(f"老大结果是{y}喵！")
finally: 
    print("好困喵...")