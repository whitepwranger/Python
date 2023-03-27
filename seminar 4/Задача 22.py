n = int(input())
m = int(input())
N = []
M = []
for i in range(n):
    N.append(int(input))
for i in range(m):
    M.append(int(input))
Nset = set(N)
Mset = set(M)
print(sorted(list(Nset & Mset)))