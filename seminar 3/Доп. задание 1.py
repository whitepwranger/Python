a = input()
b = input()
D = {}
result = 'True'
if len(a) != len(b):
    print("False")
else:
    for i in range(len(a)):
        if a[i] not in D.keys():
            D.update({a[i]:b[i]})
        elif D[a[i]] != b[i]:
            result = "False"
            break
if result != 'False':
    print('True')
else:
    print('False')