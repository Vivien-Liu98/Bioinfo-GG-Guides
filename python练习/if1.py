age = int(input("输入年龄："))
if age >= 18:
    print("已成年。")
    if age >= 30:
        print("而立。")
    else:
        print("未立。")
else:
    print("未成年。")