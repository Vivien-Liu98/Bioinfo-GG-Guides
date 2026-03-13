f = open("./test.txt")
print(f.readline())
print(f.readline())
print(f.readline(1))
f.close()

i = 0
with open("./test.txt") as f:
    text = f.readlines()
    for line in text:
        i += 1
    print(i)