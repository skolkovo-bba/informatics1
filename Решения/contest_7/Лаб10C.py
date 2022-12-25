a=[]
d={'(':')','[':']','{':'}'}
for s in input():
    if s in d.keys():
        a.append(s)
    elif s in d.values():
        if a and d[a[-1]]==s:
            a.pop()
        else:
            print('NO')
            exit()
        

print('NO' if a else 'YES')
