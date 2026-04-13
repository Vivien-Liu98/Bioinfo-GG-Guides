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

使用pandas快捷地清洗和分析数据。

```python
# 示例数据（只是展示数据表外观，并不严格按照这个写）
 Duration          Date  Pulse  Maxpulse  Calories
  0         60  '2020/12/01'    110       130     409.1
  1         60  '2020/12/02'    117       145     479.0
  2         60  '2020/12/03'    103       135     340.0

import pandas as pd
df = pd.read_csv('data.csv')
print(df.head(10))  # 打印前10行（默认5行）
print(df.tail())   # 打印后5行
print(df.shape)  # 查看行数和列数
print(df.columns)  # 查看所有列名
print(df.info())  # 查看行列等表格信息
print(df.describe())  # 查看平均值等统计信息

# 行列选择
cols = ['ID', 'Calories']
new_df = df[cols]  # 选择多列并建立为新表
df.loc[0]  # 选择行（根据第0列标签）
df.iloc[0]  # 选择行（根据实际位置）
df.loc[2, 'Duration'] = 45  # 选择具体单元格并替换（iloc同理）
# 列重命名
df.rename(columns={'Calories': 'Cal'}, inplace=True)
# 条件筛选（适用且&或|取反~)
df[(df['Calories'] > 300) & (df['Duration'] < 60)]
df[df['Sport'] == 'Run']
df.filter(like='gene')  # 包含gene的列
df.filter(regex='^RNA')  # 以RNA开头
# 借助循环进行替换
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
# 排序
df.sort_values(by='Calories', ascending=False, inplace=True)  # 降序
df.sort_values(by='Calories', na_position='first', inplace=True)  # NA置顶
df.sort_values(by=['Calories', 'Duration'])  # 两列的顺序

# 创建新列
df['Calories_per_min'] = df['Calories'] / df['Duration']
df['High'] = df['Calories'] > 300
# 创建新行
df.loc[2] = [5,6]  # 添加一行，索引为2
df.loc[len(df)] = [5,6]  # 自动追加新行到末尾
# 删除行列
df.drop(2, inplace = True)  # 删掉第3行
df.drop('Calories', axis=1, inplace=True)  # 删除Calories列

# 空单元格处理
df.isna()  # 输出一个布尔系列，是否缺失值
df.isna().sum()  # 在前面的基础上，统计缺失值数量
new_df = df.dropna()  # 删除有空单元格的行，存为新表格
df.dropna(inplace = True)  # 直接在原表删除
df.fillna(0, inplace = True)  # 将空单元格替换为指定值

# 重置索引（重要）
df.reset_index(drop=True, inplace=True)  # 删除/筛选后必须重置

# 计算
x = df["Calories"].mean()  # 计算平均值（median中位数，mode众数）
df.fillna({"Calories": x}, inplace=True)  # 将指定列的空单元格替换为平均值
# 分组统计
df.groupby('Duration')['Calories'].sum()  # 根据Duration值分组统计Calories
df.groupby('Duration').agg({  # 根据Duration值进行分组，agg聚合函数
    'Calories': 'sum',  # 求和
    'Maxpulse': 'mean'  # 平均值
})
# 聚合表（透视表）
pivot = df.pivot_table(
    values='Calories',  # 要聚合的值
    index='Date',  # 行索引（聚合后的第0列）
    columns='Duration',  # 列索引（聚合后的第0行）
    aggfunc='sum'  # 聚合方法
)

# 日期格式修复
df['Date'] = pd.to_datetime(df['Date'], format='mixed')  
# 符合日期（例如20201212）均可，非日期的数据会变成NaT

# 字符串处理
df['Example'].str.lower()   # 转小写
df['Example'].str.contains('hi')  # 输出一个布尔系列，是否包含指定词

# 重复/唯一
print(df.duplicated())  # 查看重复值
df.drop_duplicates(inplace = True)  # 去重，在原表操作
df['Duration'].unique()   # 唯一值
df['Duration'].value_counts()  # 频数统计

# 相关性
df.corr()  # 输出结果为各列两两组合相关系数表，非数值列自动忽略
# 越接近1/-1相关性越高，越接近0相关性越低

# 自定义函数
df['Calories'] = df['Calories'].apply(lambda x: x * 1.1)  # 全部1.1倍

# 多表格操作
pd.concat([df1, df2])  # 纵向拼接
pd.concat([df1, df2], axis=1)  # 横向拼接
df1.merge(df2, on='ID', how='inner')  # 根据ID列合并，仅保留相同索引的行
df_merged = pd.merge(df1, df2, left_on='id', right_on='ID')  # 不同列名
# how:outer保留所有结果缺失值为NaN，left/right仅保留左/右表所有结果
pd.merge(df1, df2, on='ID', suffixes=('_left', '_right'))
# 当存在索引列之外的同名列时，添加后缀以区分(默认为_x，_y)
# 建立索引后拼接
df1 = df1.set_index('ID')
df2 = df2.set_index('id')
df_merged = df1.join(df2, how='inner')
# 注意，当索引不唯一的时候，会因为拼接了所有可能性导致行数膨胀
df1['ID'].duplicated().sum()  # 查重

# 列顺序调整
df = df[['Date', 'Duration', 'Calories']]  # 手动指定
col = df.pop('Calories')  # 将指定列存为系列，并从原表删除该列
df.insert(0, 'Cal', col)   # 将存好的系列插到第0列，列名为Cal
df = df.reindex(sorted(df.columns), axis=1)  # 按照字母顺序排序
```

此外，pandas也可以结合matplotlib进行绘图。

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.plot()  # 折线图
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')  # 散点图
df["Duration"].plot(kind = 'hist')  # 直方图
plt.show()
```

~不过不写脚本的时候……似乎还是用别的更方便……~

~次回予告：biopython~
