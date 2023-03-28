def get_num(t,s,r,n):
    for i in range(len(t)):
        while t[0] < 10:
            m = sum(t) + r
            if m == s:
                n = n + 1
                return n
            n = get_num(t[1:], s, m, n)
            t[0] = t[0] + 1
    return n
k = int(input())
s = int(input())

t = [0] * k
t[0] = 1
print(get_num(t,s,0,0))