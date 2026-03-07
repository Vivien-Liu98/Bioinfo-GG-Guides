list = [0.2,"B"] 
print(list)
list.append("C") 
print(list)
list.remove("B") 
print(list)
list[1] = "D" 
print(list)
# 列表可以直接改变值，而前面的数据类型不可以
h = "hi"
print(h)
# print(h.upper())
h = h.upper()
print(h)
