def sum(a,b):
    if b > 0:
        return sum(a + 1,b - 1)
    else:
        return a
print(sum(0,0))