# Python2 NumPy

> 配列のパイ

###### 1、数组array

NumPy包是针对数组处理和一些科学计算的包，并且提供比列表更快的运算速度。

```python
import numpy as np
x = np.array([1, 2, 3, 4, 5])  # 除了列表，元组也可以
print(x)
print(x[0])  # =1
print(type(x))  # 类型为numpy.ndarray

# 数组拥有被称为维度的属性，表示数组嵌套的深度
y1 = np.array(1)  # 0维
y2 = np.array([1,2,3,4])  # 1维
y3 = np.array([[1,2,3,4],[5,6,7,8]])  # 2维，以此类推
print(y3.ndim)  # 查看维度

# 维度信息可以通过shape查看
print(y3.shape)  # 返回(2，4)，两个维度，第一维度2元素，第二维度4元素
[[[[[1 2 3 4]]]]]  #返回 (1, 1, 1, 1, 4)

# 维度可通过reshape改变，转换需要元素数量满足要求，转换后本质是视图
v = np.array([1,2,3,4,5,6])
newv1 = v.reshape(3,2,1)  # 转为三维[[[1][2]][[3][4]][[5][6]]]
# 在指定转换时，允许有一个维度未知（自动计算），用-1代替
newv2 = newv1.reshape(-1)  # 转为一维

# 切片/截取，注意范围是[)
print(y3[1,0])  # 以2维为例，从0开始，第2组第1个元素，因此打印3
print(y3[1,-1])   # 负数则从末尾往前数，因此打印4
print(x[-4:-1:2])  # 从末尾计算截取范围，步长2，结果是[2 4]
#截取时[:3]表示头到3，[2:]表示2到尾
print(y3[0:2, 1:4])  # 2维，第1-2个组，各自取第2-4元素

# 数据类型
print(z.dtype)  # 支持字符串、整数、浮点、布尔等
z = np.array([1,2,3,4], dtype='S')  # 可以手动指定，S字符串
z2 = z.astype('i')  # 更改类型，i整数
# 如果把浮点更改为整数会自动去零，把数字更改为布尔则0为F其余T

# 复制与视图
w1 = y2.copy()  # 创建副本
w2 = y2.view()  # 创建视图，修改原数组影响视图，修改视图影响原数组
print(w1.base)  # 副本返回None
print(w2.base)  # 视图返回数组内容，表示其没有数据所有权

# 可以使用for循环遍历数组
for n in y3:
    print(n)  # 高维数组遍历时，n维遍历n-1维
for n in y3:  # 以2维为例，想逐个打印需要两层循环
  for m in n:
    print(m)
# 但是这样手动套娃过于麻烦，可以用nditer命令解决
for n in np.nditer(y3):
  printn(n)
# 如果希望同时打印元素和编号（坐标）
for idn, n in np.ndenumerate(y3):
  print(idx,nx)
```

数组的合并与拆分。

不太好理解，画了一张图。合并是按照指定方向拼接，切分则是垂直于指定方向分割。二维数组每一行是一组，换行则换组。注意三维数组的结构和直觉不同。
![图寄啦！](https://github.com/Vivien-Liu98/Git-images/blob/main/arr-stack.jpg?raw=true)

```python
# 合并
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2))  # 结果[[1 2][3 4][5 6][7 8]]

# 堆叠（可以导致升维）
arr = np.hstack((arr1, arr2))  # 沿行[[1 2 5 6][3 4 7 8]]
arr = np.vstack((arr1, arr2))  # 沿列[[1 2][3 4][5 6][7 8]]
arr = np.dstack((arr1, arr2))  # 沿高[[[1 5][2 6]][[3 7][4 8]]]
# hstack等效于np.stack((arr1, arr2), axis=1),v等效于axis0，d等效于axis2

#拆分
newarr = np.array_split(arr1, 2)  # 如果元素数量不能均分，会从结尾开始自动调整
print(newarr[0])  # 结果是包含数组的列表
arr3 = np.array([[[1,5],[2,6]],[[3,7],[4,8]]])
# 按行切hsplit，[array([[[1, 5]],[[3, 7]]]), array([[[2, 6]],[[4, 8]]])]
# 按列切vsplit，[array([[[1, 5],[2, 6]]]), array([[[3, 7],[4, 8]]])]
# 按高切dsplit, 3维及以上的数组才能使用
# [array([[[1],[2]],[[3],[4]]]), array([[[5],[6]],[[7],[8]]])]
```

数组的查找与筛选。

```python
# 排序
arr = np.array([3, 1, 0, 2])  # 字符串（字母）、布尔（FT）也可以被排序
print(np.sort(arr))  # 原始数组没有改变
# 2维数组排序是分别排[[1, 0], [3, 2]]→[[0, 1], [2, 3]]

# 查找
arr = np.array([1, 1, 3, 3, 5, 7])
x = np.where(arr == 3)  # 查找元素位置，结果是元组(array([2, 3]),)
x1 = np.where(arr%2 == 0)  # 查找奇数
x2 = np.where(arr%2 == 1)  # 查找偶数
# 对于已排序的数组，查找指定元素可按顺序插入的位置
y = np.searchsorted(arr, 4, side='left')  # 结果为4，可指定从左还是右计
y1 = np.searchsorted(arr, [2, 4, 6])  # 结果为[2 4 5]，支持多个查找

# 筛选（本质是指定T/F来筛选)
arr = np.array([1, 2, 3, 4])
filter_arr = []  # 建立一个空数组用于存放筛选的TF
for element in arr:  # 循环判断
  if element > 2:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]  # 使用TF数组过滤原数组
print(filter_arr)
print(newarr)

# 另一种方法
filter_arr = arr > 2
newarr = arr[filter_arr]
```

###### 2、随机random

如果随机数由程序算法生成，那么其可预测，属于伪随机。

```python
from numpy import random  
x=random.rand(5)  # 随机数组，5个0-1随机浮点数
x=random.randint(100, size=(5))  # 随机数组，5个0-100随机整数
x=random.rand(3, 5)  # 随机2维数组，3*5
x=random.choice([3, 5, 7, 9], size=(3, 5))  # 可以手动指定随机值的范围
x=random.choice([0, 1, 2], p=[0.5, 0.5, 0.0], size=(10))  # 指定出现概率
random.shuffle(arr)  # 随机打乱顺序（修改原始数组）
print(random.permutation(arr))  # 随机打乱顺序（不修改原始数组）
```

绘制图表，其中seaborn包安装时自动安装matplotlib.pyplot。

```python
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot([0, 1, 2, 3, 4, 5])  # 直方图
plt.show()
sns.displot([0, 1, 2, 3, 4, 5], kind="kde")  # 曲线图
plt.show()
```

###### 3、分布distribution

通过随机功能，生成符合特定分布的数据。

```python
# 正态分布
x = random.normal(loc=1, scale=2, size=(2, 3))  # 均值1,标准差2
sns.displot(random.normal(size=1000), kind="kde")  # 可视化绘图

# 二项分布(抛硬币)
x = random.binomial(n=10, p=0.5, size=10)  # 10次试验，重复10次
sns.displot(random.binomial(n=10, p=0.5, size=1000)) 
# 区别在于正态分布是连续的，而二项分布是离散的。但数据够多，后者和前者相似

# 多项分布（二项亚种，抛骰子）
x = random.multinomial(n=6, pvals=[1/6]*6)  # 也可以概率不均等
# 注意，返回的结果是所有结果出现的次数。即骰子1-6出现的次数

# 泊松分布（事件在单位时间内随机发生的次数）
x = random.poisson(lam=2, size=10)  # 发生2次
sns.displot(random.poisson(lam=2, size=1000))
# 同样是离散，但数据够多时会类似于具有一定标准差和均值的正态分布
# n极大而p≈0时，与二项分布非常接近，n*p≈lam

# 指数分布（描述下一次事件发生的时间）
x = random.exponential(scale=2, size=(2, 3))  # scale 速率的倒数
sns.displot(random.exponential(size=1000), kind="kde")
# 区别在于泊松分布是在一段时间内事件发生的次数，指数分布是事件之间的时间间隔。

# 卡方分布（假设检验）
x = random.chisquare(df=2, size=(2, 3))  # 自由度2
sns.displot(random.chisquare(df=1, size=1000), kind="kde")
# 由于平方只有正值使曲线右偏，可理解为大量小偏差和少量大偏差
# 自由度越高越接近正态分布

# 均匀分布（每个事件发生概率均等）
x = random.uniform(size=(2, 3))  # 下限low默认0，上限high默认1
sns.displot(random.uniform(size=10000), kind="kde")
# 图是不规则的波浪线，数据越多越趋近平滑

# 逻辑分布（来自S型增长函数）
x = random.logistic(loc=1, scale=2, size=(2, 3))  # 均值1，标准差2
# 比正态分布更容易出现极端值的钟形分布


# Rayleigh分布（二维随机长度波动）
x = random.rayleigh(scale=2, size=(2, 3))
# 理解为在平面上随机抖动（x方向 + y方向）→ 到原点的距离。例如无线信号、风速等。

# Pareto 分布（少数支配多数）
x = random.pareto(a=2, size=(2, 3))
# 例如80%财富由20%人拥有

# Zipf分布（排名规律）
x = random.zipf(a=2, size=(2, 3))
# 第k名的频率 ≈ 1/k，例如词频，网站访问量等。Pareto的离散版。
```

~未完待续~
