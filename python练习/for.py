print("输入最小值和最大值，对数列求和求平均值")
a = int(input("输入最小值："))
b = int(input("输入最大值："))
numbers = list(range(a,b+1))  # 因为range[)，所以最大值要+1
i = 0
for num in numbers:
    i = i + num

average = i / len(numbers)

#print("总和:" + str(i))
#print("平均值:" + str(average))
print(f"""总和:{i}
平均值:{average}""")