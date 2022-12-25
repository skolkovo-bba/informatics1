a=[]
for i in input().split():
    if i in '+*':
        y=a.pop()
        x=a.pop()
        if i=='+':
            a.append(tuple(map(sum,zip(x,y))))
        else:
            a.append((x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0]))
    else:
        a.append(tuple(map(int,i.split(','))))
print(*a.pop(),sep=',')
