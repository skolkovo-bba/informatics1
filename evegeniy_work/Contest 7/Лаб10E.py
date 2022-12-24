a=[]
c=0
for s in input().split():
    if a and a[-1][0]==s[0] and abs(int(a[-1][1])-int(s[1]))<=2:
        a.pop()
        c+=2
        if len(a)>=2 and a[-1][0]==a[0][0]:
            a.pop()
            a.pop(0)
            c+=2
    else:
        a.append(s)
print(c)
            
