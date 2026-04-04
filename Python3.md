# Python3 Pandas

> パンダの群れ

###### 1、数组array

Pandas包是针对数据集清洗、处理和分析的包。

```python
import pandas as pd
# 从文件导入数据
df = pd.read_csv('data.csv')  # 读取csv文件
print(df.to_string())  # 打印文件内容

# 手动输入数据
mydataset = {
  'cars': ["A", "B", "C"],
  'passings': [1, 2, 3]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
```

Pandas的数据由系列（列）和数据表（表格）构成。

```python
# 系列
a = [1, 2, 3]
myvar = pd.Series(a)  # 转换为系列
print(myvar[0])  # 通过标签可以访问系列中的指定值，默认标签为数字
myvar = pd.Series(a, index = ["x", "y", "z"])  # 手动指定标签
calories = {"day1": 10, "day2": 20, "day3": 30}  # 字典
myvar = pd.Series(calories)  # 字典的键自动成为标签
myvar = pd.Series(calories, index = ["day1", "day2"])  # 只使用部分字典

```



~次回予告：biopython~
