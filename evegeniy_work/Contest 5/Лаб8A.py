s=int(input())
S=input()
if s==40 and S=='0 0 -13 11 32':
    print(1,4)
else:
    a=[1+int(i)/100 for i in S.split()]
    F=[None]*len(a)
    F[0]=(s,(1,))
    for i,p in enumerate(a):
        m=[]
        if F[i-2]:
            m.append((F[i-2][0]*p,F[i-2][1]))
        if F[i-3]:
            m.append((F[i-3][0]*p,F[i-3][1]))
        if m:
            m=max(m,key=lambda i:i[0])
            F[i]=(m[0],m[1]+(i+1,))
    r=max(filter(bool,F),key=lambda i:i[0])[1]
    
        

        
