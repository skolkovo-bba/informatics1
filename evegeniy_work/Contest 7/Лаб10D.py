a=[]
for s in input().split():
    if s in '%#':
        if s=='%':
            if len(a)<2:
                print(0)
                break
            else:
                a.append(a.pop()*a.pop()/100)
        else:
            if a:
                a[:]=[sum(a)]
            else:
                print(0)
                break
    else:
        a.append(float(s))
else:
    print(a[-1])
