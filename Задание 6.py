n = input()
l = 0
r = 0
arr = list(map(int,n))

for i in range(1,len(arr)):
    for x in arr[:i]:
        l += x
    for x in arr[i:]:
        r += x
    if r == l:
        print("lucky")
        exit(0)
    l = 0
    r = 0
print("unlucky")