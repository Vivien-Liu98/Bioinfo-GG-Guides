age = int(input("输入年龄："))
if age < 18:
    print("未成年。")
elif 18 <= age < 30:
    print("已成年。")
    print("未立。")
else:
    print("已成年。")
    print("而立。") 