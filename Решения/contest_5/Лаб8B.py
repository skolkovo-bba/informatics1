s=int(input())
a=[int(i) for i in input().split()]
F=[None]*len(a)
for i in range(len(a)):
    m=0
    for j in range(i):
        if F[j]>m and a[j]<a[i]:
            m=F[j]
    F[i]=m+1
print(max(F))

        
