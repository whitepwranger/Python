n = int(input())
k = int(n / 2)
ps = int(n / 4)
if n % 4 == 2 or n % 4 == 3:
    ps += 1
elif n % 4 == 1:
    k += 1
print(str(ps) + " " + str(k) + " " + str(ps))