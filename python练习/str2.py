name = ["老刘","老李","老张"]
year = "2026"
for bro in name:
    blessing_msg = "祝" + bro + year + "新年快乐！"
    print(blessing_msg)
# 其他写法
print(" ")
for bro in name:
    blessing_msg1 = "祝{}{}新年快乐！".format(bro,year) 
    blessing_msg2 = "祝{bro}{yr}新年快乐！".format(bro=bro,yr=year) 
    blessing_msg3 = f"祝{bro}{year}新年快乐！" 
    print(f"{blessing_msg1}\n{blessing_msg2}\n{blessing_msg3}")
    
#print(blessing_msg1, blessing_msg2, blessing_msg3, sep="\n")
#print(blessing_msg1 + "\n" + blessing_msg2 + "\n" + blessing_msg3)
#print("{}\n{}\n{}".format(blessing_msg1, blessing_msg2, blessing_msg3))
