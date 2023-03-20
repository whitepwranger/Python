D = {1:'AEIOULNSTR', 2: 'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JX', 10:'QZ'}
r = 0
word = input().upper()

for i in word:
    for k in D.keys():
        if i in D[k]:
            r += k
print(r)