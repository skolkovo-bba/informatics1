a=input().split(' ')
for i,v in enumerate(a):
    if len(v)<=3:
        a[i]=''
print(' '.join(a))

