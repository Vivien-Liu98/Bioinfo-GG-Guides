import random
# 借用这个功能来生成随机数
def fortune(user_input):
    x = random.randint(1,9)  # 生成一个1-9的随机整数
    if x < 4:
        print(f"输入了{user_input}...抽到了末吉！")
    elif 4 <= x < 7:
        print(f"输入了{user_input}...抽到了中吉！")
    else:
        print(f"输入了{user_input}...抽到了大吉！")
    return x

user_input = input("输入任意内容抽签：")
result=fortune(user_input)

#print(f"调试用，result={result}")
