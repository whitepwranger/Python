import random
N = int(input())
X = int(input())
A = [random.randint(0,10) for x in range(N)]
count = 0
for i in A:
    if i == X:
        count += 1
print(count)