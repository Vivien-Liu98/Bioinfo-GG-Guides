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

~未完待续~
