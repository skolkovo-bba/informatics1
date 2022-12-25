def getpos():
    s=input()
    return '-abcdefgh-'.index(s[0]),'012345678'.index(s[1])
n=int(input())
F=[[0]*10 for _ in range(9)]
for _ in range(n):
    c,r=getpos()
    F[r][c]=-1
C,R=getpos()
F[R][C]=1
#print(*F,sep='\n')
for i in range(R+1,9):
    for j in range(1,9):
        if F[i][j]==0:
            F[i][j]=max(F[i-1][j],0)
        if F[i][j]==-1:
            F[i][j]=max(F[i-1][j-1],0)+max(F[i-1][j+1],0)
#print(*F,sep='\n')
print(sum(i for i in F[8] if i>0))

