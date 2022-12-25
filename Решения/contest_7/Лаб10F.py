a,b=(list(map(int,input().split())) for i in '..')
r=[k for i in a for k in b[:b.index(i)+1]]
print(*r)

