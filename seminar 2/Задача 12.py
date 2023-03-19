#Задание 12
S = int(input())
P = int(input())

D = S * S - 4 * P
x1 = (S - D ** 0.5)/2
x2 = (S + D ** 0.5)/2
print(int(x1),int(x2))