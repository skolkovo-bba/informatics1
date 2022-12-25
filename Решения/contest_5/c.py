m = list(map(int, input().split()))

ans = [None] * len(m)
for i in range(len(m)):
    now = 0
    for j in range(i):
        if ans[j] > now and m[j] < m[i]:
            now = ans[j]
    
    ans[i] = now + 1

print(max(ans))