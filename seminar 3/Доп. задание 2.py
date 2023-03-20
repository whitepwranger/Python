def query(D={}):
    result = ''

    for i in sorted(D.keys()):
        result += i + '=' + str(D[i]) + '&'
    return result.rstrip('&')
print(query({'course': 'python', 'lesson': 2, 'challenge': 17}))