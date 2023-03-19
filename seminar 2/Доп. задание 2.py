ls = ['1','2','3','4','5','6','7','8','9']
lsr = []
nt = 1
t = ls[0]
R = 0
test = ''
Result = ''
for n in range(1,256):
    N_SIGN = 0
    SIGN = 0
    T_SIGN = 0
    for j in range(8):
        SIGN <<= 1
        if nt % 2 == 1:
            N_SIGN += 1;
            SIGN ^= 1
        nt >>= 1
    nt = n
    T_SIGN = SIGN
    for i in range(N_SIGN):
        for j in range(8):
            if nt % 2 == 1:
                if(T_SIGN % 2 == 1):
                    R += int(t)
                    Result += '+' + t
                else:
                    R -= int(t)
                    Result += '-' + t
                T_SIGN >>= 1
                t = ls[j + 1]
            else:
                t += ls[j + 1]
            nt >>= 1
        if (T_SIGN % 2 == 1):
            R += int(t)
            Result += '+' + t
        else:
            R -= int(t)
            Result += '-' + t
        T_SIGN >>= 1
        if R == 100:
            lsr.append(Result)
        Result = ''
        SIGN -= 1
        T_SIGN = SIGN
        nt = n
        R = 0
        t = '1'
    n += 1
    nt = n
print([x.lstrip('+').lstrip('-') for x in lsr])