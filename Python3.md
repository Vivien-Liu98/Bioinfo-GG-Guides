# Python3 Pandas

> パンダの群れ

###### 1、读取read

Pandas包是针对数据集清洗、处理和分析的包。其内部的数据由系列Series（列）和数据表DataFrames（表格）构成。

```python
import pandas as pd
# 系列
a = [1, 2, 3]
myvar = pd.Series(a)  # 转换为系列
print(myvar[0])  # 通过标签可以访问系列中的指定值，默认标签为数字
myvar = pd.Series(a, index = ["x", "y", "z"])  # 手动指定标签
calories = {"day1": 10, "day2": 20, "day3": 30}  # 字典
myvar = pd.Series(calories)  # 字典的键自动成为标签
myvar = pd.Series(calories, index = ["day1", "day2"])  # 只使用部分字典

# 数据表
data = {
  "calories": [420, 380, 390],  # 第一列行名+内容
  "duration": [50, 40, 45]  # 第二列行名+内容
}
df = pd.DataFrame(data)  # 注意，生成的表格第0列为行号（索引）
print(df.loc[0])  # 返回指定行（是系列）
print(df.loc[[0, 1]])  # 返回指定行（是数据表）
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])  # 自定义索引
```

pandas可以读取文件从而获得数据。

```python
# csv文件（逗号分割的纯文本文件，字符串）
import pandas as pd
df = pd.read_csv('data.csv')  # 读取
print(df.to_string())   # to_string打印完整数据表
print(df)  # 对大表格默认只打印标题行和前5+后5行
pd.options.display.max_rows = 100  # 修改打印阈值，行数超过该值则只打印前后5行

# json文件（具有对象格式的纯文本文件，字符串/数字/布尔/null）
df = pd.read_json('data.json')  # 读取
print(df.to_string()) 
# 关于json格式，该格式比起csv优势是可以表达嵌套结构以及不同对象字段数可以不同
# 按列组织
{  
  "列名": {  # 除索引外的第一列
    "行索引": 值
  }
}
# 按行组织
[
  {"列1名":值, "列2名":值},  # 除题头外的第一行
]
```

###### 2、分析Analyze

使用pandas快捷地处理数据。

```python
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head(10))  # 打印前10行（默认5行）
print(df.tail())   # 打印后5行
print(df.info())  # 查看行列等信息
```



~次回予告：biopython~
