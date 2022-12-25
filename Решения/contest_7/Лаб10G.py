a=[]
s=input()
while s!='=':
    if s in '+-*':
        x=a.pop()
        y=a.pop()
        a.append(str(eval(y+s+x)))
    else:
        a.append(s)
    s=input()
print(*a)
