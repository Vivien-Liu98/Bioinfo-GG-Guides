dict = {"一":"111",
        "二":"222"} 
print(dict)
dict["三"] = "333"
print(dict)
del dict["二"] 
print(dict)
print("三" in dict) 

dict2 = {("一", 1):"111",
         ("二", 2):"222"}
print(dict2)
