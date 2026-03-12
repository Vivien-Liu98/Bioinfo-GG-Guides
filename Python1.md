# Python1

> 知らない，我的分析很需要。

**1、宣告的print**

所有编程的第一课，使用print函数打印输出。

```python
# 我是注释喵
print("?")
print("Ah"+"?")  # 字符串+连接
print('What is "Ah"?')  # 多重引号的区分
print("What\'s \"Ah\"?")  # 使用\转义
print("Emmm \n?")  # 使用\n换行
print("""hhh
23333""")  # 使用"""换行，注意如果加空格对齐会导致空格也被输出

"""
顺便一提，什么都不加的三个引号
可以用于多行注释
"""
```

**2、赋予的variable**

用变量来表示一个值。

变量名由文字、数字、下划线组成，区分大小写，不可以有空格、数字开头、引号包围。

不要把python自带的函数名用作变量。

```python
name1 = "Vivien"  # 赋值
print("I\'m" + name1)  # 直接使用变量名

name2 = name1  # 赋值顺序为左←右
name1 = "vivi"  # 后赋值会覆写前面的赋值
print("I\'m" + name1)  # name1改变

#print多个变量（以换行分隔）的写法
print(f"{msg1}\n{msg2}\n{msg3}")
print(msg1, msg2, msg3, sep="\n")
print(msg1 + "\n" + msg2 + "\n" + msg3)
print("{}\n{}\n{}".format(msg1, msg2, msg3))
```

**3、数字的calculation**

在生信小教程咱写过perl的四则运算，这里是python版。

<font color =red>注意</font>，由于多数十进制浮点数（小数）无法在二进制中精确表示，所以存储的是近似值。在perl里会自动忽略输出2.3+5.6=7.9，而python里则会输出2.3+5.6=7.8999999999999995。

```python
#!/usr/bin/env python3
print("输入两个数字后的四则运算")
# input()获取输入的值，提示语可以直接写在()里
# float转换为浮点数以支持小数运算（不转换是字符串不能数学运算）
x = float(input("请输入第一个数字:"))  
y = float(input("请输入第二个数字:"))

# +加，-减，*乘，/除，**乘方，==等于，!=不等于
print("和")
z = x + y
print(round(z, 2))  # round()四舍五入到2位小数
print(f"{z:.2f}")  # f-string写法，浮点数保留2位小数

print("乘积")
v = x * y
print(round(v, 2))

print("差")
w = x - y
print(round(w, 2))

print("商")
u = x / y
print(u)
print("计算完毕\n")
```

**4、数据的type**

python内的数据类型：

- 字符串str："？"   " 1"（即便是数字也不会被视作数字）

- 整数int：10   1

- 浮点数float：10.2   1.0

- 布尔类型bool：True   False （必须大写）

- 空值NoneType：None（必须大写）

```python
# 字符串与索引
x = "123 456"  # 指定一个字符串
print(type(x))  # 查看数据类型
print(len(x))  # 计算字符串长度（空格也算）
print(x[2])  # 索引字符串的第三个字符（因为从0开始往右数）

y = 1  # 整数
print("str" + str(y))  # 整数转换为字符串才能和字符串一起打印
print("str", y)  # 另一种解决方案，缺点是中间会出现空格
print(f"str {y}")  # 新世纪方案f-string
```

- 列表list：类似于数组

```python
list = [0.2,"B"]  # 列表内可以共存多种数据类型,可以为空
list.append("C")  # 为列表追加元素
list.remove("B")  # 为列表删除元素
list[1] = "D"  # 指定元素替换
# 其他函数：list.max最大值,min最小值,sorted排序
# 列表可以直接改变值，而前面的数据类型不可以
h = "hi"
h = h.upper()  # 大写化后需要重新赋值才改变
print(h)
print(h.upper()) # 如果不需要改变值，只需要打印的话
```

- 字典dict：键值对

```python
dict = {"一":"111",  # 键：值
        "二":"222"}  # 键不可以是列表
dict["三"] = "333"  # 为字典追加元素，若键已存在则覆写值
del dict["二"]  # 为字典删除元素
print("三" in dict)  # 检索键是否已存在（结果为布尔类型）
# 对于需要同名键的情况，使用元组来让一个键包含多个元素
# 元组同样不可变(追加/删除元素），使用()而非列表的[]
dict2 = {("一", A):"111",
         ("二", A):"222"}
# 其他函数：dict.keys返回键, values返回值, items返回键值对
```

**5、外援的package**

python本身自带一些函数，但是想实现更多功能，则需要调用包（库）。

```python
# 调用包
import package  # 写在脚本开头
package.function(...)  # 调用函数需要加上包名
import package as pk  # 指定包的缩写
pk.function(...)  # 调用时加上缩写名
from package import *  # 包内函数全部引入，这种写法调用时不需要加包名
from package import function as func  # 只调用包里特定函数+指定缩写
# 安装包
pip install package  # 需要联网
pip install ./package.whl  # 安装pypl下载好的本地包
# 查看已安装的包
pip list
```

**6、分断的if**

if-else条件判断，可以嵌套，python通过缩进来判断属于哪个if。

多个条件时可以使用逻辑判断：and与，or或，not非。无括号时优先级非>与>或

```python
age = int(input("输入年龄："))  # 字符串需要转换才能用于运算
# 嵌套写法
if age >= 18:
    if age >= 30:
        print("而立。")
    else:
        print("未立。")
    print("已成年。")
else:
    print("未成年。")

# elif写法
if age < 18:
    print("未成年。")
elif 18 <= age < 30:
    print("已成年。")
    print("未立。")
else:
    print("已成年。")
    print("而立。") 
```

**7、遍历的for**

对所有内容逐个进行操作，可以嵌套，需要缩进。

```python
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
平均值:{average}""")  # f-string支持三引号多行输出

# 综合练习：打印九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}×{i}={i*j}", end=" ")  # end=" "，用空格代替print默认换行
    print()  # 换行，等于print(end="\n")

# range(a,b,c)，取[a,b)，间隔为c（默认1，可以为负数，即递减）
# range(b),取[0,b)
```

**8、循回的while**

重复操作，直到不再满足条件，可以嵌套，需要缩进。

```python
# while求数列和（不如for简单）
numbers = list(range(1,11))  # 从1至10
i = 0
total = 0
while i < len(numbers):
    total = total + numbers[i]
    i = i + 1
print(f"总和:{total}")

# 但是在未知需要循环多少次时，只能使用while
# 一些无意义的巧思（）
print("输入任意数量的数字求和与平均值，输入q开始计算")
i = 0
total = 0
j = -1  # 第一次循环都是0所以j从-1开始，用于统计输入次数
while i != "q":
    total += float(i)
    i = input("请输入数字：")  # 第一次循环后正式开始输入
    j += 1  # 简写j = j + 1
if j == 0:  # 防止0作为除数报错
    print("没有数字喵...")
else:
    print(f"总和:{total},平均值：{total/j}")

# 另一种写法（局部）
while True:  # 无限循环
    i = input("请输入数字：")
    if i == "q":  # if和else并不是锁定的，特定时候可以只写if
        break  # 终止循环
    total += float(i)
    j += 1
```

**9、整顿的readability**

对于长文字填空生成的整理与优化。

```python
name = ["老刘","老李","老张"]
year = "2026"
for bro in name:
    blessing_msg = "祝" + bro + year + "新年快乐！"
    print(blessing_msg)
# 其他写法
    blessing_msg = "祝{0}{1}新年快乐！".format(bro,year)  # 顺序，数字可不写
    blessing_msg = "祝{bro}{yr}新年快乐！".format(bro=bro,yr=year)  #自定义
    blessing_msg = f"祝{bro}{year}新年快乐！"  # f-string
# format也可以直接用于其他数据类型
```

**10、创造的function**

将一段代码自定义为函数便于调用，仅限同一脚本内。

```python
import random  # 借用这个包来生成随机数
def fortune(user_input):
    x = random.randint(1,9)  # 生成一个1-9的随机整数
    if x < 4:
        print(f"输入了{user_input}...抽到了末吉！")
    elif 4 <= x < 7:
        print(f"输入了{user_input}...抽到了中吉！")
    else:
        print(f"输入了{user_input}...抽到了大吉！")

user_input = input("输入任意内容抽签：")
fortune(user_input)

# 自定义函数内的变量是无法在函数外调用的
def example(user_input):
    y = user_input + 1
    return y  # 返回变量的值，默认返回None
z = example(user_input)  # 返回后的值需要赋值给新的变量来使用
print(z)  # 不可以直接打印y
# 如果需要返回多个变量，需用多个变量分别接受，单个变量接收则会变成元组
```

**11、对象的nonexistence**

之前的代码是『面向过程』编程，也就是详细描述程序每一步做什么。而『面向对象』编程则是以程序执行的对象（类）为核心，为其添加属性、方法，适用于复杂情况。

举个例子，前者是我做饭→我吃饭，后者是我（爱吃肉；做，吃）和饭（好吃；被吃）

```python
# 定义一个类，注意要用首字母大写而非下划线分隔
class DietChoose:
    def __init__(self, taste, howmuch):  # 定义对象属性，第一个固定为self
        self.taste = taste  # 可以重名
        self.price = howmuch
    def eaten(self, type):  # 定义对象的方法
        if self.price < 25 and self.taste == "好吃":  # 可调用前面的属性
            print(f"{type}...社畜优选！")
        else:
            print(f"{type}...都牛马了吃点好的...")

diet1 = DietChoose("好吃", 22)  # 类可以理解为创建对象的模板
print(f"这道菜的味道是{diet1.taste}，价格是{diet1.price}")  # 查看该对象属性值
diet1.eaten("猪肘饭")  # 运行该对象方法
```

类可以嵌套，子类会继承父类的属性。

```python
class Food:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.what = "能吃"   # 如果不需要外界传入，就不用写在def里
    def eaten(self):  # 定义对象的方法
        print(f"要吃{self.name}吗？")
class ZhongCan(Food):  # 子类需要标注父类
    def exp_z(self):
        print(f"{self.name}是中餐。")
class XiCan(Food):
    def __init__(self,name,price,taste):  # 若子类需要在父类基础上追加特有属性
        super().__init__(name,price)  # 若不super继承则子类属性只有taste
        self.taste = taste
    def exp_x(self):
        if self.taste == "好吃":
            print(f"{self.name}是好吃的西餐。")
        else:
            print(f"{self.name}...嗯...")

zhong1 = ZhongCan("烧鸭饭",21)  # 子类没有定义属性时，使用父类的属性创建
zhong1.eaten()  # 子类没有定义方法时，也继承父类的方法
zhong1.exp_z()
xi1 = XiCan("牛排",45,"好吃")
xi1.exp_x()
```

~未完待续~
