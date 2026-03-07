print("输入任意数量的数字求和与平均值，输入q开始计算")
i = 0
total = 0
j = -1
while i != "q":
    total += float(i)
    i = input("请输入数字：")
    j += 1
if j == 0:
    print("没有数字喵...")
else:
    print(f"总和:{total},平均值：{total/j}")
