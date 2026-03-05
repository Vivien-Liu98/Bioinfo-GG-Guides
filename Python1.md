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
23333
wwww""")  # 使用"""换行，注意如果加空格对齐会导致空格也被输出

"""
顺便一提
什么都不加的三个引号
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
```

**3、数字的calculation**

在生信小教程咱写过perl的四则运算，这里是python版。

<font color =red>注意</font>，由于多数十进制浮点数（小数）无法在二进制中精确表示，所以存储的是近似值。在perl里会自动忽略输出2.3+5.6=7.9，而python里则会输出2.3+5.6=7.8999999999999995。

```python
#!/usr/bin/env python3
print("输入两个数字后的四则运算")
print("请输入第一个数字:")  # input()获取输入的值
x = float(input())  # 转换为浮点数以小数运算（不转换则是字符串不能数学运算）
print("请输入第二个数字:")
y = float(input())

# +加，-减，*乘，/除，**乘方
print("和")
z = x + y
print(round(z, 2))  # round()四舍五入到2位小数

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
```

**5、外援的package**

python本身自带一些函数，但是想实现更多功能，则需要调用包（库）。

```python
# 调用包
import package  # 写在脚本开头
package.function(...)  # 调用函数需要加上包名
import package as pk  # 指定缩写
pk.function(...)  # 调用缩写
from package import function as func  # 只调用包里特定功能+指定缩写

# 安装包
pip install package  # 需要联网
pip install ./package.whl  # 安装pypl下载好的本地包
# 查看已安装的包
pip list
```

~未完待续~


