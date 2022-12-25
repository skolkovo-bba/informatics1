A,B=(list(map(int,input().split())) for i in (1,1))
n = len(A)//4
for i in range(len(A)):
    j=B.index(A[i])
    if A[i:i+n]==B[j:j+n]:
        print('NO')
        break
else:
    print('YES')
    
