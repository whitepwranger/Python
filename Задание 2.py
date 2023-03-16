s = input()
result = 0
for i in s:
    if i.isdigit():
        result += int(i)
print(result)
