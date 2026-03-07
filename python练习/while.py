numbers = list(range(1,11))
i = 0
total = 0
while i < len(numbers):
    total = total + numbers[i]
    i = i + 1
print(f"总和:{total}")