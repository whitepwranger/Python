def func(a = 0, b = 0):
    t = int(input())
    if t > b:
        func(b, t)
    elif t > a and t != b:
        func(t, b)
    elif t == 0:
        print(a)
        return a
    else:
        func(a, b)
func()