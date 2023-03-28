def sqr(a,b):
    if b > 1:
        return a * sqr(a,b - 1)
    else:
        return a

print(sqr(2,8))