import random
N = int(input())
X = int(input())
A = [random.randint(0,N) for x in range(N)]
t = X
r = 0
for i in A:
    if ((X - i)**2)**0.5 < t:
        r = i
        t = ((X - i)**2)**0.5
print(A)
print(r)