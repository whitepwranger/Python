f = open('грядка.txt','r')
bush = [ int(x) for x in f.readline().split()]
l = len(bush)
r = 0
t = 0
for i in range(l):
    t = bush[(l+i-1)%l] + bush[i] + bush[(l+i+1)%l]
    if r < t:
        r = t
print(r)