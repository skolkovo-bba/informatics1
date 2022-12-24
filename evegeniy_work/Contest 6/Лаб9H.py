s=input()
k=int(input())
if k>=0:print(s*k)
else:
    k=-k
    if len(s)%k==0 and s[:len(s)//k]*k==s:
        print(s[:len(s)//k])
    else:print('NO SOLUTION')
