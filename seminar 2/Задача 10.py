# Задание 10
coins = input()
arr_coins = coins.split(',')
n = 0
for c in arr_coins:
    if int(c) == 0:
        n += 1
if len(arr_coins) - n >= n:
    print(n)
else:
    print(arr_coins - n)